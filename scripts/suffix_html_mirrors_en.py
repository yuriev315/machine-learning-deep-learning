#!/usr/bin/env python3
"""Language-suffix naming for complete offline HTML mirrors (books/*_html_en/<site>/).

A website needs its original file names to work offline, so for each mirror:
  1. <site>_original_en.tar.gz  = the mirror in its ORIGINAL layout (extract to read offline);
  2. <site>/ is replaced by a COPY whose file names carry the language suffix (contents unchanged,
     links not rewritten -> NOT a working site), with <site>/path_map_en.csv (original -> renamed, sha256).
The verification record keeps the original per-file hashes; this step is recorded under
"naming_conversion".  python3 -I scripts/suffix_html_mirrors_en.py
"""
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402
import engineering_en as E  # noqa: E402

RES = C.RESULTS / "18_books_en.json"


def main():
    res = C.load_json(RES, {})
    for sid, rec in res.items():
        if rec.get("status") != "verified" or not rec.get("mirror") or rec.get("naming_conversion"):
            continue
        book = C.ROOT / rec["local_path"]
        sites = [p for p in book.iterdir() if p.is_dir()]
        conv = []
        for site in sites:
            arch = book / f"{site.name}_original_en.tar.gz"
            E.det_tar(site, arch, site.name)
            rels = sorted(str(p.relative_to(site)) for p in site.rglob("*") if p.is_file())
            tmp = book / f".{site.name}_renaming"
            rows = E.renamed_copy(site, rels, tmp)
            shutil.rmtree(site)
            tmp.rename(site)
            conv.append({"site_dir": str(site.relative_to(C.ROOT)), "original_archive": str(arch.relative_to(C.ROOT)),
                         "original_archive_sha256": C.sha256_file(arch), "files": len(rows),
                         "path_map": str((site / "path_map_en.csv").relative_to(C.ROOT))})
            print(f"[{sid}] {site.name}: {len(rows)} files renamed; archive {arch.name}")
        rec["naming_conversion"] = {"time": time.strftime("%F %T"), "sites": conv,
                                    "note": "原始结构网站在 *_original_en.tar.gz（解压后可离线阅读）；目录内为加语言后缀的只读副本，链接未改写，不能直接作为网站使用"}
        res[sid] = rec
    C.save_json(RES, res)


if __name__ == "__main__":
    main()
