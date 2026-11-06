#!/usr/bin/env python3
"""Unzip that keeps symlinks and permissions, which Python's `zipfile -e` drops. Needed for the Android NDK and emulator."""
import os, stat, sys, zipfile
src, dest = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(src) as z:
    for i in z.infolist():
        p = os.path.join(dest, i.filename); mode = i.external_attr >> 16
        if os.path.abspath(p) != os.path.abspath(dest) and not os.path.abspath(p).startswith(os.path.abspath(dest) + os.sep):
            sys.exit("unsafe path in archive: " + i.filename)
        if i.is_dir():
            os.makedirs(p, exist_ok=True); continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if stat.S_ISLNK(mode):
            if os.path.lexists(p): os.remove(p)
            os.symlink(z.read(i).decode(), p); continue
        with open(p, "wb") as f: f.write(z.read(i))
        if mode: os.chmod(p, stat.S_IMODE(mode))
