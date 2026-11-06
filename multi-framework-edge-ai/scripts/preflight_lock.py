#!/usr/bin/env python3
"""Check every locked wheel for this platform stays under the 100 MiB file limit, before downloading."""
import json, re, sys, urllib.request
lock, py = sys.argv[1], sys.argv[2]   # e.g. cp312
tot = 0; bad = []
for line in open(lock):
    m = re.match(r"^([A-Za-z0-9_.\-]+)==([^ \\]+)", line)
    if not m: continue
    name, ver = m.groups()
    d = json.load(urllib.request.urlopen(f"https://pypi.org/pypi/{name}/{ver}/json", timeout=30))
    c = [f for f in d["urls"] if f["packagetype"] == "bdist_wheel" and ("none-any" in f["filename"] or (("x86_64" in f["filename"]) and "linux" in f["filename"] and (py in f["filename"] or "py3-none" in f["filename"] or "abi3" in f["filename"] or "cp312-none" in f["filename"])))]
    s = max((f["size"] for f in c), default=0)
    if not c: print("NO WHEEL", name, ver)
    tot += s
    if s > 104857600: bad.append((name, ver, s))
print(f"packages ok; total ≈ {tot/1048576:.0f} MiB; over limit: {bad}")
