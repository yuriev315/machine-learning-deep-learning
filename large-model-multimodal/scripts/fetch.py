#!/usr/bin/env python3
"""Resumable fetch of library files.

usage: python3 -I fetch.py <items.json> <library_root> <status.jsonl> [--cache DIR] [--workers N]

items.json: {path: {path, url, size?, sha256?}}. Files over 100 MiB are not kept; their
status is OVERSIZE with the size seen. Each finished item appends one JSON line to status.jsonl.
"""
import hashlib, json, os, sys, threading, time, urllib.request, urllib.error, collections, shutil

LIMIT = 100 * 1048576
UA = 'Mozilla/5.0 (X11; Linux x86_64) literature-archive/1.0'
args = sys.argv[1:]
items = json.load(open(args[0])); root = args[1]; stpath = args[2]
cache = args[args.index('--cache') + 1] if '--cache' in args else None
workers = int(args[args.index('--workers') + 1]) if '--workers' in args else 6
done = {}
if os.path.exists(stpath):
    for l in open(stpath):
        try: d = json.loads(l)
        except Exception: continue
        done[d['path']] = d
lock = threading.Lock(); out = open(stpath, 'a')
def rec(d):
    with lock:
        out.write(json.dumps(d, ensure_ascii=False) + '\n'); out.flush()
DELAY = {'arxiv.org': 3.2, 'export.arxiv.org': 3.2}
last = collections.defaultdict(float); hl = collections.defaultdict(threading.Lock)
def host(u): return u.split('/')[2]
def throttle(h):
    with hl[h]:
        w = last[h] + DELAY.get(h, 0.6) - time.time()
        if w > 0: time.sleep(w)
        last[h] = time.time()
def fetch(it):
    p = it['path']; u = it.get('url'); dest = os.path.join(root, p)
    r = dict(path=p, url=u, expect_sha256=it.get('sha256'), expect_size=it.get('size'))
    if cache and it.get('sha256') and os.path.exists(os.path.join(cache, it['sha256'])):
        os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.copyfile(os.path.join(cache, it['sha256']), dest)
        r.update(status='OK', how='disk', size=os.path.getsize(dest), sha256=it['sha256']); return rec(r)
    if not u: r.update(status='NOURL'); return rec(r)
    if it.get('size') and it['size'] > LIMIT: r.update(status='OVERSIZE', size=it['size']); return rec(r)
    tmp = dest + '.part'; os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(4):
        throttle(host(u))
        try:
            req = urllib.request.Request(u, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                cl = resp.headers.get('Content-Length'); ct = resp.headers.get('Content-Type', '')
                if cl and int(cl) > LIMIT:
                    r.update(status='OVERSIZE', size=int(cl), final=resp.geturl()); return rec(r)
                h = hashlib.sha256(); n = 0; first = b''
                with open(tmp, 'wb') as f:
                    while True:
                        b = resp.read(1 << 20)
                        if not b: break
                        if not first: first = b[:16]
                        n += len(b)
                        if n > LIMIT:
                            f.close(); os.remove(tmp); r.update(status='OVERSIZE', size=n, note='stream over limit'); return rec(r)
                        h.update(b); f.write(b)
            sha = h.hexdigest()
            if 'text/html' in ct and not p.endswith(('.html', '.htm')):
                os.remove(tmp); r.update(status='HTML', http=200, ctype=ct, final=resp.geturl()); return rec(r)
            if p.endswith('.pdf') and not first.startswith(b'%PDF'):
                os.remove(tmp); r.update(status='NOTPDF', first=first.hex()); return rec(r)
            os.replace(tmp, dest)
            st = 'OK' if (not it.get('sha256') or it['sha256'] == sha) else 'CHANGED'
            r.update(status=st, how='web', size=n, sha256=sha, final=resp.geturl(), ctype=ct); return rec(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 3: time.sleep(10 * (attempt + 1)); continue
            r.update(status='HTTP', http=e.code); return rec(r)
        except Exception as e:
            if attempt < 3: time.sleep(5 * (attempt + 1)); continue
            r.update(status='ERROR', error=repr(e)[:200]); return rec(r)
todo = [it for p, it in items.items() if done.get(p, {}).get('status') not in ('OK', 'CHANGED', 'OVERSIZE')]
print('todo', len(todo), 'of', len(items), flush=True)
# one queue per host so slow hosts do not block others
q = collections.defaultdict(list)
for it in todo: q[host(it['url']) if it.get('url') else '-'].append(it)
pool = list(q.values()); plock = threading.Lock()
def worker():
    while True:
        with plock:
            pool.sort(key=len, reverse=True)
            # pick the host with most items whose lock is free
            it = None
            for lst in pool:
                if lst:
                    h = host(lst[0]['url']) if lst[0].get('url') else '-'
                    if not hl[h].locked() or h == '-': it = lst.pop(0); break
            if it is None and not any(pool): return
        if it is None: time.sleep(0.2); continue
        fetch(it)
ts = [threading.Thread(target=worker) for _ in range(workers)]
[t.start() for t in ts]; [t.join() for t in ts]
print('finished', flush=True)
