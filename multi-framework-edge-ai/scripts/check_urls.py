#!/usr/bin/env python3
"""Checks every external link in the generated READMEs and writes manifests/doc_links_status.csv."""
import concurrent.futures as cf, csv, os, re, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urls = {}
for base in ("framework", "formats", "conversion", "runtimes", "hardware", "docs", "examples"):
    for d, _, fs in os.walk(os.path.join(ROOT, base)):
        for f in fs:
            if f.endswith(".md") and "artifacts" not in d:
                for u in re.findall(r"\((https?://[^)\s]+)\)", open(os.path.join(d, f), errors="ignore").read()):
                    urls.setdefault(u, os.path.relpath(os.path.join(d, f), ROOT))
def check(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (link-check)"}), timeout=25); return u, r.status, r.geturl()
    except urllib.error.HTTPError as e: return u, e.code, ""
    except Exception as e: return u, type(e).__name__, ""
with cf.ThreadPoolExecutor(6) as ex: res = list(ex.map(check, sorted(urls)))
with open(os.path.join(ROOT, "manifests/doc_links_status.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["url", "http_status", "final_url", "first_seen_in"])
    for u, s, fu in res: w.writerow([u, s, fu, urls[u]])
print(len(res), "links;", "failing:")
for u, s, _ in res:
    if s != 200: print(" ", s, u)
