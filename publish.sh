#!/usr/bin/env bash
# Publish the awesome-agent-infrastructure repo from the generated workspace.
# Idempotent: creates the repo on first run, pushes on every run.
set -uo pipefail

REPO_DIR=/tmp/ghw/awesome
GH=/usr/bin/gh
OWNER=Amz34
NAME=awesome-agent-infrastructure

cd "$REPO_DIR" || exit 1
export GH_PAGER=cat

# 1. Point the generator at its own directory so CI refreshes work.
python3 - <<'PY'
from pathlib import Path
p = Path("build_awesome.py")
s = p.read_text()
s = s.replace('OUT = Path("/tmp/ghw/awesome")', 'OUT = Path(__file__).resolve().parent')
s = s.replace("license-CC0--1.0-lightgrey", "license-MIT-lightgrey")
s = s.replace(
    "Released under CC0-1.0 — copy, remix, republish freely.",
    "Released under the MIT License — see [LICENSE](LICENSE).",
)
p.write_text(s)
print("generator localized + license aligned to MIT")
PY

# 2. Regenerate so the README matches the committed generator.
python3 build_awesome.py 2>/dev/null | tail -1 || exit 1

# 3. Normalize line endings + strip anything secret-shaped (safety gate).
find . -name '*.py' -o -name '*.md' -o -name '*.yml' -o -name '*.json' | while read -r f; do
  sed -i 's/\r$//' "$f"
done
if grep -rIlE 'gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|eyJ[A-Za-z0-9_-]{25,}\.' . --exclude-dir=.git 2>/dev/null; then
  echo "ABORT: secret-shaped string found in tracked files" >&2
  exit 2
fi

# 4. Commit + push.
git init -q 2>/dev/null || true
git add -A
if ! git diff --cached --quiet 2>/dev/null; then
  git -c user.name="Amz34" -c user.email="aamir1zahran@gmail.com" \
    commit -q -m "feat: live-checked index of agent infrastructure projects"
fi

if $GH repo view "$OWNER/$NAME" >/dev/null 2>&1; then
  git remote remove origin 2>/dev/null || true
  git remote add origin "https://github.com/$OWNER/$NAME.git"
  git branch -M main
  git push -u origin main --force-with-lease
else
  $GH repo create "$OWNER/$NAME" --public --source=. --remote=origin --push \
    --description "A live-checked index of production-grade, self-hostable building blocks for AI agents and LLM workloads."
  git branch -M main 2>/dev/null || true
  git push -u origin main 2>/dev/null || true
fi

# 5. Metadata: topics (JSON file — array form is required) + homepage.
cat > /tmp/ghw/awesome/topics.json <<'JSON'
{"names":["awesome-list","awesome","ai-agents","llm","self-hosted","on-premise","mcp","rag","llmops","homelab","free-tier","infrastructure","devops","vector-database","local-llm","observability","monitoring","open-source","curated-list","machine-learning"]}
JSON
$GH api --method PUT "repos/$OWNER/$NAME/topics" --input /tmp/ghw/awesome/topics.json >/dev/null 2>&1 \
  && echo "topics: ok" || echo "topics: FAILED"

$GH repo edit "$OWNER/$NAME" \
  --homepage "https://github.com/$OWNER/$NAME#readme" \
  --add-topic awesome-list >/dev/null 2>&1 && echo "edit: ok" || echo "edit: skipped"

# 6. Read back the truth.
echo "--- verify ---"
$GH api "repos/$OWNER/$NAME" \
  --jq '"repo=\(.full_name) visibility=\(.visibility) topics=\(.topics|length) desc_len=\(.description|length)"'
$GH api "repos/$OWNER/$NAME/contents/README.md" --jq '.size as $s | "readme_bytes=\($s)"'
$GH api "repos/$OWNER/$NAME/contents/md" >/dev/null 2>&1
echo "entries_in_readme=$(grep -c '^| \[' README.md)"
echo "sections=$(grep -c '^## ' README.md)"
