#!/usr/bin/env bash
# Resume every collection step (idempotent: verified items are skipped, failed ones are not retried
# unless RETRY=1). Run from anywhere:  bash /root/low_resource_language_llm_literature/scripts/resume_all_en.sh
# Optional: CATS="03 06" to limit paper categories; RETRY=1 to retry failed downloads.
set -u
cd "$(dirname "$0")/.." || exit 1
PY="python3 -I"
RF=""
[ "${RETRY:-0}" = "1" ] && RF="--retry-failed"
for c in ${CATS:-01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16}; do
  ls scripts/seeds/${c}_*_seed*_cn.json >/dev/null 2>&1 || continue
  $PY scripts/papers_en.py resolve "$c"
  $PY scripts/papers_en.py download "$c" --target 55 $RF
done
for c in 17 18; do
  ls scripts/seeds/${c}_*_seed*_cn.json >/dev/null 2>&1 && $PY scripts/materials_en.py fetch "$c" $RF
done
[ -f scripts/seeds/19_engineering_seed_cn.json ] && $PY scripts/engineering_en.py fetch $RF
$PY scripts/build_catalog_en.py
