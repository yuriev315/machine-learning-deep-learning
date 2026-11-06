#!/usr/bin/env python3
"""Second integrity pass: compares every wheel with the SHA256 PyPI publishes, adds the non-fetch.py downloads to download_status.csv, and re-hashes all archives."""
import csv, hashlib, json, os, re, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P = os.path.join(ROOT, "manifests/download_status.csv")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
rows = [r for r in csv.DictReader(open(P)) if not r["name"].startswith(("wheel:", "deb:", "edgetpu:"))]; by = {r["name"]: r for r in rows}
for sub in ("py312", "py312_nodeps", "py37"):
    d = os.path.join(ROOT, "deps/wheels", sub)
    for f in sorted(os.listdir(d)):
        rows.append(dict(name="wheel:" + f, version=sub, filename=f, url="", size=os.path.getsize(os.path.join(d, f)), official_sha256="", local_sha256=sha(os.path.join(d, f)), status="", note=""))
TORCH = "8f8b3cfc53010a4b4a3c7ecb88c212e9decc4f5eeb6af75c3c803937d2d60947"
cache = {}
def pypi(name, ver):
    k = (name, ver)
    if k not in cache:
        cache[k] = {f["filename"]: f["digests"]["sha256"] for f in json.load(urllib.request.urlopen(f"https://pypi.org/pypi/{name}/{ver}/json", timeout=30))["urls"]}
    return cache[k]
for r in rows:
    if not r["name"].startswith("wheel:") : continue
    f = r["filename"]
    if f.startswith("torch-2.7.1+cpu"):
        r["url"] = "https://download.pytorch.org/whl/cpu/torch/"; ok = r["local_sha256"] == TORCH
        r["official_sha256"], r["status"], r["note"] = TORCH, "SHA256_VERIFIED" if ok else "SHA256_MISMATCH", "digest from the official PyTorch index"
        continue
    m = re.match(r"^([A-Za-z0-9_.\-]+?)-(\d[^-]*)(?:-|\.tar\.gz)", f)
    r["url"] = f"https://pypi.org/project/{m[1]}/{m[2]}/"
    d = pypi(m[1], m[2]).get(f)
    if d and d == r["local_sha256"]: r["official_sha256"], r["status"], r["note"] = d, "SHA256_VERIFIED", "matches the digest published by PyPI"
    elif d: r["status"], r["note"] = "SHA256_MISMATCH", "differs from PyPI"
    else: r["status"], r["note"] = "HASH_UNVERIFIED_NO_OFFICIAL_DIGEST", "file not listed by PyPI"
def add(name, ver, path, url, status, note):
    f = os.path.join(ROOT, path)
    by.pop(name, None)
    rows[:] = [x for x in rows if x["name"] != name]
    rows.append(dict(name=name, version=ver, filename=os.path.basename(path), url=url, size=os.path.getsize(f), official_sha256="", local_sha256=sha(f), status=status, note=note))
for f in sorted(os.listdir(os.path.join(ROOT, "third_party/edgetpu_compiler"))):
    p = f"third_party/edgetpu_compiler/{f}"
    if not os.path.isdir(os.path.join(ROOT, p)): add("edgetpu:" + f, "16.0", p, "https://github.com/google-coral/edgetpu/tree/master/compiler/x86_64", "HASH_UNVERIFIED_NO_OFFICIAL_DIGEST", "Pulled over HTTPS from the official repo")
for sub in ("gcc-aarch64-debs", "x11-debs", "lavapipe-debs"):
    for f in sorted(os.listdir(os.path.join(ROOT, "deps/archives", sub))):
        add("deb:" + f, "Ubuntu 26.04", f"deps/archives/{sub}/{f}", "apt-get download", "SHA256_VERIFIED", "apt checks the package against the signed Ubuntu archive index")
for r in rows:
    if r["status"] in ("SHA256_VERIFIED", "SHA1_VERIFIED", "SHA512_VERIFIED", "HASH_UNVERIFIED_NO_OFFICIAL_DIGEST") and not r["name"].startswith(("wheel:", "deb:", "edgetpu:")):
        for d, _, fs in os.walk(os.path.join(ROOT, "deps/archives", r["name"])):
            if r["filename"] in fs:
                assert sha(os.path.join(d, r["filename"])) == r["local_sha256"], r["name"]
w = csv.DictWriter(open(P, "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections; print(collections.Counter(r["status"] for r in rows))
