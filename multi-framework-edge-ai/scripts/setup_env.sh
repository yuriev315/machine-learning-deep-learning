#!/usr/bin/env bash
# Rebuilds both Python environments from the wheels in deps/wheels, offline and hash-checked where a lock hash exists.
# Downloading deps/wheels: get the Release assets (see README), or run with ONLINE=1 to fetch from PyPI.
# usage: scripts/setup_env.sh [target-dir, default .envs]
set -euo pipefail
cd "$(dirname "$0")/.."; ROOT=$PWD; T=${1:-.envs}; export UV_LINK_MODE=hardlink
command -v uv >/dev/null || { echo "uv is required: https://docs.astral.sh/uv/"; exit 1; }
SRC="--no-index --find-links deps/wheels/py312"; [ "${ONLINE:-0}" = 1 ] && SRC=""
uv venv -q --python 3.12 "$T/main"
uv pip install -q --python "$T/main/bin/python" $SRC --no-deps --require-hashes -r manifests/requirements-main.lock
NOD=$(grep -vE '^\s*(#|$)|^torch==' manifests/requirements-nodeps.lock.in | sed 's/ *#.*//' | tr '\n' ' ')
if [ "${ONLINE:-0}" = 1 ]; then uv pip install -q --python "$T/main/bin/python" --no-deps $NOD
else uv pip install -q --python "$T/main/bin/python" --no-deps --no-index --find-links deps/wheels/py312_nodeps $NOD; fi
uv pip install -q --python "$T/main/bin/python" --no-deps "$(ls deps/wheels/py312_nodeps/torch-2.7.1*.whl)" 2>/dev/null || uv pip install -q --python "$T/main/bin/python" --no-deps torch==2.7.1 --index-url https://download.pytorch.org/whl/cpu
PY37=${PY37:-third_party/python37/install/bin/python3}
"$PY37" -m venv "$T/legacy37"
"$T/legacy37/bin/python" -m pip -q install --no-index --find-links deps/wheels/py37 -r manifests/requirements-legacy37.txt
echo "done: $T/main, $T/legacy37"
