#!/usr/bin/env python3
"""Turn status.json into a shields.io endpoint badge (live count)."""
import json
import pathlib
import sys

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "status.json")
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "badge.json")
d = json.loads(src.read_text())
s = d["summary"]
total = s.get("total", 0)
live = s.get("LIVE", 0)
dead = s.get("GONE", 0) + s.get("ARCHIVED", 0)
color = "brightgreen" if dead == 0 and live == total else ("yellow" if dead == 0 else "red")
badge = {
    "schemaVersion": 1,
    "label": "live-checked",
    "message": f"{live}/{total}",
    "color": color,
}
out.write_text(json.dumps(badge) + "\n")
print(f"badge: {live}/{total} live, {dead} dead -> {out}")
