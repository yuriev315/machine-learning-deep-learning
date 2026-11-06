#!/usr/bin/env python3
"""Read stdin, pass it through, and append every RESULT line to manifests/runtime_test_results.csv.
usage: <cmd> | record_result.py --status RUNNABLE_VERIFIED --hw "x86-64 AMD Ryzen 5 3600 CPU" --api "C++"
Latest measurement per route+hardware wins. Nothing is ever written by hand into this file."""
import argparse, csv, datetime, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "manifests/runtime_test_results.csv")
F = ["route","status","hardware","execution","api","threads","n","accuracy","latency_mean_us","latency_p95_us","peak_rss_kb","model_bytes","date"]
a = argparse.ArgumentParser(); a.add_argument("--status", default="RUNNABLE_VERIFIED"); a.add_argument("--hw", default="x86-64 AMD Ryzen 5 3600 CPU")
a.add_argument("--exec", default="native"); a.add_argument("--api", default="C++"); a.add_argument("--threads", default="1"); o = a.parse_args()
rows = {}
if os.path.exists(P):
    rows = {(r["route"], r["hardware"]): r for r in csv.DictReader(open(P))}
seen = 0
for line in sys.stdin:
    sys.stdout.write(line)
    if line.startswith("RESULT "):
        d = json.loads(line[7:]); seen += 1
        d = {**{k: d.get(k, "") for k in F}, "status": o.status, "hardware": o.hw, "execution": o.exec, "api": o.api, "threads": o.threads, "date": datetime.date.today().isoformat()}
        rows[(d["route"], d["hardware"])] = d
with open(P, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=F); w.writeheader()
    for k in sorted(rows): w.writerow(rows[k])
sys.exit(0 if seen else 3)   # no RESULT line means the run did not complete
