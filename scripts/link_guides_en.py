#!/usr/bin/env python3
"""Turn 〔LRL-…〕 markers in guide drafts into links to verified local files.

  python3 -I scripts/link_guides_en.py

Reads scripts/guide_src/*_cn.md (drafts), writes guides/*_cn.md. Every marker must resolve to a
catalog_cn.csv row whose local path exists; otherwise the script stops and lists the bad markers
(so a guide never cites an unverified or missing item).
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "guide_src"
OUT = ROOT / "guides"
MARK = re.compile(r"〔(LRL-[A-Z]-?[0-9]{2}-[0-9A-Z]{3}|LRL-E-[0-9]{2})〕")


def main():
    with open(ROOT / "catalog_cn.csv", encoding="utf-8-sig") as f:
        rows = {r["文献编号"]: r for r in csv.DictReader(f)}
    OUT.mkdir(exist_ok=True)
    bad, used = [], set()
    for src in sorted(SRC.glob("*_cn.md")):
        text = src.read_text("utf-8")

        def repl(m):
            rid = m.group(1)
            r = rows.get(rid)
            path = (r or {}).get("本地路径", "").split("；")[0]
            if not r or not path or not (ROOT / path).exists():
                bad.append(f"{src.name}: {rid}")
                return m.group(0)
            used.add(rid)
            title = re.sub(r"[\[\]|]", " ", r["标题"])[:70].strip()
            return f"[{rid}｜{title}](../{path})"
        out = MARK.sub(repl, text)
        (OUT / src.name).write_text(out, "utf-8")
    if bad:
        print("UNRESOLVED markers:\n  " + "\n  ".join(bad))
        sys.exit(1)
    print(f"linked {len(used)} distinct items into {len(list(SRC.glob('*_cn.md')))} guides")


if __name__ == "__main__":
    main()
