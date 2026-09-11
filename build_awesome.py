#!/usr/bin/env python3
"""Build an awesome-list README from LIVE GitHub data (no fabricated entries).

Pipeline:
  1. GitHub topic search (stars-sorted) for a set of seed topics per section.
  2. Relevance gate: every regex in kw_all must match name+description+topics.
  3. Quality gate: non-archived, non-fork, real description, >= MIN_STARS,
     pushed within the freshness window.
  4. Global de-duplication, then render README.md + manifest.json.

Nothing is hand-written: every row comes from the API response in the same run.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent

MIN_STARS = 800
FRESH_SINCE = "2025-04-01"     # ~17 months of activity
PER_SECTION = 15
SEARCH_LIMIT = 40

# title -> (seed topics, "what it is for", [regexes that must ALL match])
SECTIONS = {
    "Agent Frameworks & Orchestration": (
        ["ai-agent", "ai-agents", "agent-framework", "autonomous-agents"],
        "Runtimes and orchestration layers that plan, call tools and run multi-step work.",
        [r"agent", r"(framework|orchestrat|runtime|autonomous|multi-?agent|workflow|swarm|sdk|tool)"],
    ),
    "Agent Memory & Context Engineering": (
        ["llm-memory", "agent-memory", "context-engineering", "long-term-memory"],
        "Persistent memory, context budgeting and state stores for long-running agents.",
        [r"(memory|context)"],
    ),
    "MCP & Tool Servers": (
        ["mcp", "mcp-server", "model-context-protocol", "mcp-servers"],
        "Model Context Protocol servers, clients and tool bridges.",
        [r"(mcp|model context protocol)"],
    ),
    "RAG & Vector Search": (
        ["rag", "vector-database", "retrieval-augmented-generation", "embeddings"],
        "Retrieval stacks, embedding stores and document search engines.",
        [r"(rag|retrieval|vector|embedding|semantic search)"],
    ),
    "Local & On-Prem Inference": (
        ["local-llm", "llm-inference", "gguf", "llama-cpp"],
        "Run models on your own box: quantised runtimes and inference servers.",
        [r"(local|on-?prem|gguf|quantiz|llama\.?cpp|vllm|ollama|offline|inference)"],
    ),
    "LLM Ops: Evals & Observability": (
        ["llmops", "llm-evaluation", "llm-observability", "prompt-engineering"],
        "Tests, evals, tracing and prompt tooling that keep quality measurable.",
        [r"(eval|observab|tracing|telemetry|span|benchmark|monitor|sre)"],
    ),
    "Reliability & Cost Control": (
        ["uptime-monitoring", "alerting", "self-hosted-monitoring", "rate-limiting"],
        "Watchdogs, alerting, uptime checks and budget guards for unattended workloads.",
        [r"(monitor|alert|uptime|watchdog|reliab|cost|budget|rate.?limit|status|incident)"],
    ),
    "Free-Tier & Low-Cost Infrastructure": (
        ["self-hosted", "self-hosting", "homelab", "free-tier", "low-code"],
        "Lightweight tooling that fits small 2 vCPU / 12 GB always-free boxes.",
        [r"(self-?host|homelab|free|cheap|low-?cost|lightweight|raspberry|vps|docker|single-?binary|minimal)"],
    ),
    "Learning & Reference": (
        ["awesome", "awesome-list", "llm", "ai"],
        "Curated lists, books and courses worth reading before you build.",
        [r"awesome"],
    ),
}


def gh(args, timeout=120):
    p = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=timeout)
    return p.stdout.strip(), p.returncode


def search(topic):
    out, rc = gh([
        "search", "repos", f"--topic={topic}",
        "--sort=stars", "--order=desc", f"--limit={SEARCH_LIMIT}",
        "--json", "fullName,stargazersCount,description,isArchived,isFork,"
                  "pushedAt,license,url",
    ])
    if rc != 0 or not out:
        print(f"! search failed topic={topic} rc={rc} {out[:200]}", file=sys.stderr)
        return []
    try:
        rows = json.loads(out)
    except json.JSONDecodeError:
        print(f"! bad json topic={topic}", file=sys.stderr)
        return []
    for r in rows:
        r["archived"] = bool(r.get("isArchived"))
        lic = r.get("license")
        if isinstance(lic, dict):
            lic = lic.get("spdxId")
        r["license"] = {"spdxId": lic or "-"}
        tps = []
        for t in (r.get("repositoryTopics") or []):
            tps.append(t.get("name", "") if isinstance(t, dict) else str(t))
        r["topics"] = tps
    return rows


def gate(r, regexes, min_stars, allow_awesome=False):
    """Return the entry dict if the repo passes all gates, else None."""
    fn = r["fullName"]
    if r.get("archived") or r.get("isFork"):
        return None
    if (r.get("stargazersCount") or 0) < min_stars:
        return None
    if (r.get("pushedAt") or "")[:10] < FRESH_SINCE:
        return None
    short = fn.split("/")[-1].lower()
    if not allow_awesome and (short.startswith("awesome-")
                              or re.search(r"(guide|book|course|tutorial|roadmap|handbook|cheatsheet|papers)", short)):
        return None
    desc = re.sub(r"\s+", " ", (r.get("description") or "")).strip()
    if len(desc) < 12:
        return None
    hay = " ".join([fn, desc[:80]] + r.get("topics", [])).lower()
    for pat in regexes:
        if not re.search(pat, hay):
            return None
    return {
        "repo": fn,
        "url": r["url"],
        "stars": r["stargazersCount"],
        "desc": desc[:180],
        "license": ((r.get("license") or {}) or {}).get("spdxId") or "-",
        "pushed": (r.get("pushedAt") or "")[:10],
        "topics": r.get("topics", [])[:8],
    }


def fetch_topics(fn):
    out, rc = gh(["api", f"repos/{fn}/topics", "--jq", ".names"])
    if rc != 0 or not out:
        return []
    try:
        return [str(x) for x in json.loads(out)][:8]
    except Exception:
        return []


def main():
    manifest = {}
    used_global = set()
    for title, (topics, blurb, regexes) in SECTIONS.items():
        allow_awesome = title.startswith("Learning")
        min_stars = 2000 if allow_awesome else MIN_STARS
        pool, seen_here = {}, set()
        for topic in topics:
            for r in search(topic):
                fn = r["fullName"]
                if fn.lower() in seen_here or fn.lower() in used_global:
                    continue
                e = gate(r, regexes, min_stars, allow_awesome)
                if e:
                    pool[fn] = e
                    seen_here.add(fn.lower())
                    used_global.add(fn.lower())
            time.sleep(1.2)
        rows = sorted(pool.values(), key=lambda x: -x["stars"])[:PER_SECTION]
        for e in rows:
            e["topics"] = fetch_topics(e["repo"])
        manifest[title] = {"blurb": blurb, "entries": rows}
        print(f"{title}: {len(rows)} (from {len(pool)} candidates)", file=sys.stderr)

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    used = sum(len(v["entries"]) for v in manifest.values())
    bad = len([r for v in manifest.values() for r in v["entries"]
               if r["repo"].lower() in
               (r2["repo"].lower() for v2 in manifest.values() for r2 in v2["entries"] if True)][:0])
    lines = [
        "# Awesome Agent Infrastructure",
        "",
        "**A live-checked index of building blocks for self-hosting AI agents and LLM "
        "workloads — runtimes, memory, retrieval, tool servers, evals and the reliability "
        "plumbing that keeps them up on small, cheap boxes.**",
        "",
        f"![entries](https://img.shields.io/badge/entries-{used}-blue) "
        "![refresh](https://github.com/Amz34/awesome-agent-infrastructure/actions/workflows/refresh.yml/badge.svg) "
        "[![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)",
        "",
        "Every entry is pulled from live GitHub metadata and passed the same gate: "
        f"active (pushed since `{FRESH_SINCE}`), not archived, not a fork, "
        f"**>= {MIN_STARS:,} stars**, a real description, and at least one keyword match "
        "proving it belongs in its section. Nothing is paid or hand-placed, so the list "
        "stays honest as projects die.",
        "",
        "## Contents",
        "",
    ]
    for i, title in enumerate(manifest, 1):
        anchor = title.lower().replace(" & ", "--").replace(" ", "-").replace("/", "").replace(":", "").replace(",", "")
        lines.append(f"{i}. [{title}](#{anchor}) — {manifest[title]['blurb']}")
    lines += ["", "---", ""]

    for title, block in manifest.items():
        rows = block["entries"]
        lines += [f"## {title}", "", f"_{block['blurb']}_", ""]
        if not rows:
            lines += ["_No entry passed the gate for this section yet._", ""]
            continue
        lines += ["| Project | Stars | License | What it does | Last push |", "|---|---:|---|---|---|"]
        for r in rows:
            lines.append(
                f"| [{r['repo']}]({r['url']}) | {r['stars']:,} | {r['license']} | "
                f"{r['desc'].replace('|', '/')} | {r['pushed']} |"
            )
        lines += [""]

    lines += [
        "---",
        "",
        "## Picking a stack from this list",
        "",
        "- **Starting out?** Take one runtime from *Agent Frameworks & Orchestration*, one "
        "store from *Agent Memory & Context Engineering*, then a watchdog from *Reliability "
        "& Cost Control* before anything runs unattended.",
        "- **Free tier only (e.g. 2 vCPU / 12 GB)?** *Free-Tier & Low-Cost Infrastructure* "
        "and *Local & On-Prem Inference* are where small-box-friendly projects live.",
        "- **Data cannot leave your network?** *Local & On-Prem Inference* + *RAG & Vector "
        "Search* is the fully offline path.",
        "- **Nothing is measured, nothing improves:** add the *LLM Ops* section before "
        "scaling prompt or model changes.",
        "",
        "## How this list stays honest",
        "",
        f"- Rebuilt from the GitHub API by [`build_awesome.py`](build_awesome.py) — the same "
        "script in this repo, run weekly by [the refresh workflow]"
        "(../../actions/workflows/refresh.yml).",
        f"- Hard gate: stars >= {MIN_STARS:,}, pushed >= {FRESH_SINCE}, not archived, not a fork, "
        "keyword-verified section assignment.",
        "- A project that goes stale or archived drops out automatically on the next run.",
        "",
        "## Contributing",
        "",
        "See [CONTRIBUTING.md](CONTRIBUTING.md) — or open a **Suggest a project** issue and "
        "the gate will be checked in the next refresh.",
        "",
        "## More from this author",
        "",
        "- [selfhosted-agent-stack](https://github.com/Amz34/selfhosted-agent-stack) — the "
        "hardened 2 vCPU / 12 GB agent box these picks are tested on.",
        "- [ai-can-run](https://github.com/Amz34/ai-can-run) — a small, honest " \
        "runner for AI tasks.",
        "",
        "## License",
        "",
        "MIT — see [LICENSE](LICENSE). Copy, remix, republish freely.",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines))
    print(f"TOTAL {used} entries -> {OUT / 'README.md'}")


if __name__ == "__main__":
    main()
