#!/usr/bin/env python3
"""Download one PDF into a fresh scratch dir and print text of selected pages (manual checks).
  python3 -I scripts/inspect_pdf_en.py <url> [first_pages=10] [chars=1500] [--grep REGEX]"""
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402

url = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 10
chars = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 1500
grep = sys.argv[sys.argv.index("--grep") + 1] if "--grep" in sys.argv else None
d = Path("/root/.cache/lrl_lit/inspect") / str(int(time.time() * 1000))
d.mkdir(parents=True)
f = d / "doc.pdf"
if url.startswith("/"):
    f = Path(url)
else:
    C.http_get(url, dest=f, max_bytes=400 * 1024 * 1024, timeout=300)
pypdf = C.load_pypdf()
rd = pypdf.PdfReader(str(f), strict=False)
print(f"pages={len(rd.pages)} file={f}")
pages = range(len(rd.pages)) if grep else range(min(n, len(rd.pages)))
for i in pages:
    t = re.sub(r"\s+", " ", rd.pages[i].extract_text() or "")
    if grep:
        if re.search(grep, t):
            print(f"--- p{i + 1}: {t[:chars]}")
            n -= 1
            if n <= 0:
                break
    else:
        print(f"--- p{i + 1}: {t[:chars]}")
