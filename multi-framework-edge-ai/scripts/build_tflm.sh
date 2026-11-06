#!/usr/bin/env bash
# Builds TFLite Micro for the host; its Makefile fetches pinned deps (flatbuffers, kissfft, gemmlowp, ruy).
cd "$(dirname "$0")/.." && source scripts/env.sh; cd third_party/tflite-micro
make -f tensorflow/lite/micro/tools/make/Makefile -j2 BUILD_TYPE=release microlite
