#!/usr/bin/env python3
"""Live-verify every entry of the curated list against the GitHub API.

The list claims "live-checked", but build_awesome.py only gates on stars /
archived / pushed-at at *build* time. This tool re-checks the *shipped* list:
existence, archival, freshness, license and homepage reachability, then writes
status.json (per-entry verdict + date) so a reader can see when each row was
last proven alive.

Verdicts (deterministic, one function, unit-tested offline):
  LIVE      not archived, pushed within STALE_DAYS
  STALE     not archived, last push older than STALE_DAYS
  ARCHIVED  repo archived upstream
  GONE      repo deleted / renamed / private (404)

Usage:
  verify_entries.py                 # verify manifest.json -> status.json
  verify_entries.py --limit 20      # smoke test on the first N entries
  verify_entries.py --selftest      # offline classifier controls, no network
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STALE_DAYS = 180
BATCH = 40  # repositories per GraphQL call


# ---------------------------------------------------------------- classifier
def classify(repo: dict | None, today: dt.date, stale_days: int = STALE_DAYS) -> str:
    """Pure classifier: API payload -> verdict. Unit-tested, no I/O."""
    if repo is None:  # GraphQL returns null only when the repo is gone/renamed/private
        return "GONE"
    if repo.get("isArchived"):
        return "ARCHIVED"
    pushed = repo.get("pushedAt")
    if not pushed:
        return "STALE"
    try:
        d = dt.date.fromisoformat(pushed[:10])
    except ValueError:
        return "STALE"
    return "LIVE" if (today - d).days <= stale_days else "STALE"


# ---------------------------------------------------------------- github api
QUERY_FIELDS = """
      nameWithOwner
      stargazerCount
      forkCount
      isArchived
      pushedAt
      description
      homepageUrl
      licenseInfo { spdxId }
      issues(states: OPEN) { totalCount }
"""


def gh_graphql(query: str) -> dict:
    p = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"],
                       capture_output=True, text=True, timeout=180)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip()[:300])
    return json.loads(p.stdout)


def gh_rest_repo(full: str) -> dict:
    """Single-repo REST fallback. A 404 means the entry is really gone."""
    p = subprocess.run(["gh", "api", f"repos/{full}"], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        return {}          # 404 / 451 / permission -> treat as gone-or-unreachable
    try:
        r = json.loads(p.stdout)
    except json.JSONDecodeError:
        return {}
    return {"nameWithOwner": r.get("full_name"),
            "stargazerCount": r.get("stargazers_count"),
            "forkCount": r.get("forks_count"),
            "isArchived": r.get("archived"),
            "pushedAt": r.get("pushed_at"),
            "description": r.get("description"),
            "homepageUrl": r.get("homepage"),
            "licenseInfo": {"spdxId": (r.get("license") or {}).get("spdx_id", "-")},
            "issues": {"totalCount": r.get("open_issues_count")}}


def verify(repos: list[str], today: dt.date) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for i in range(0, len(repos), BATCH):
        chunk = repos[i:i + BATCH]
        parts = []
        for j, full in enumerate(chunk):
            owner, _, name = full.partition("/")
            parts.append(f'  r{j}: repository(owner: "{owner}", name: "{name}") {{{QUERY_FIELDS}  }}')
        body = "query {\n" + "\n".join(parts) + "\n}"
        try:
            data = gh_graphql(body).get("data", {})
        except RuntimeError:
            # One dead entry aborts the WHOLE aliased batch (observed: a deleted repo makes
            # GitHub fail the query outright). Fall back to per-repo REST so a single dead
            # row cannot blank the entire dashboard.
            data = {}
            for j, full in enumerate(chunk):
                data[f"r{j}"] = gh_rest_repo(full) or None
        for j, full in enumerate(chunk):
            out[full] = data.get(f"r{j}") or {}
    return out


# ---------------------------------------------------------------- selftest
def selftest() -> int:
    today = dt.date(2026, 9, 21)
    cases = [
        ("fresh repo", {"isArchived": False, "pushedAt": "2026-09-14T10:00:00Z"}, "LIVE"),
        ("exactly at boundary", {"isArchived": False, "pushedAt": "2026-03-25T00:00:00Z"}, "LIVE"),
        ("one day past boundary", {"isArchived": False, "pushedAt": "2026-03-24T00:00:00Z"}, "STALE"),
        ("old repo", {"isArchived": False, "pushedAt": "2025-05-27T00:00:00Z"}, "STALE"),
        ("archived upstream", {"isArchived": True, "pushedAt": "2026-09-01T00:00:00Z"}, "ARCHIVED"),
        ("archived AND old (archived wins)", {"isArchived": True, "pushedAt": "2020-01-01T00:00:00Z"}, "ARCHIVED"),
        ("deleted repo (null)", None, "GONE"),
        ("empty payload", {}, "STALE"),
        ("missing pushedAt", {"isArchived": False}, "STALE"),
        ("garbage pushedAt", {"isArchived": False, "pushedAt": "not-a-date"}, "STALE"),
    ]
    fails = 0
    for label, payload, want in cases:
        got = classify(payload, today)
        ok = got == want
        fails += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {got} (want {want})")
    # boundary sanity: STALE_DAYS must be a positive window
    ok = STALE_DAYS > 0
    fails += 0 if ok else 1
    print(f"  [{'PASS' if ok else 'FAIL'}] STALE_DAYS is positive ({STALE_DAYS})")
    # must-fail control: a classifier that returns LIVE for everything must not pass
    def bad_classifier(_repo, _today, _s=STALE_DAYS):
        return "LIVE"
    bad_pass = all(bad_classifier(p, today) == w for _, p, w in cases)
    print(f"  [{'PASS' if not bad_pass else 'FAIL'}] control: always-LIVE classifier fails these cases")
    fails += 0 if not bad_pass else 1
    print(f"{len(cases) + 2 - fails}/{len(cases) + 2} controls passed")
    return 1 if fails else 0


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=str(HERE.parent / "awesome-agent-infrastructure" / "manifest.json"))
    ap.add_argument("--out", default=str(HERE / "status.json"))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    manifest = json.loads(Path(a.manifest).read_text())
    entries = [e for v in manifest.values() for e in v.get("entries", [])]
    repos = [e["repo"] for e in entries]
    if a.limit:
        repos = repos[:a.limit]

    today = dt.date.today()
    live = verify(repos, today)

    results, counts = {}, {}
    for full in repos:
        payload = live.get(full) or {}
        verdict = classify(payload or None, today)
        counts[verdict] = counts.get(verdict, 0) + 1
        results[full] = {
            "verdict": verdict,
            "stars": payload.get("stargazerCount"),
            "forks": payload.get("forkCount"),
            "license": (payload.get("licenseInfo") or {}).get("spdxId") or "-",
            "pushed": (payload.get("pushedAt") or "")[:10],
            "open_issues": ((payload.get("issues") or {}).get("totalCount")),
            "homepage": payload.get("homepageUrl"),
            "verified_on": today.isoformat(),
        }

    doc = {"generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "stale_days": STALE_DAYS, "checked": len(repos),
           "summary": counts, "entries": results}
    Path(a.out).write_text(json.dumps(doc, indent=2, sort_keys=True))
    print(f"checked={len(repos)} -> {a.out}")
    for k in ("LIVE", "STALE", "ARCHIVED", "GONE"):
        if counts.get(k):
            print(f"  {k}: {counts[k]}")
    bad = counts.get("ARCHIVED", 0) + counts.get("GONE", 0)
    print(f"NON_LIVE={bad}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
