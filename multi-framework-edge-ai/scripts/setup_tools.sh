#!/usr/bin/env bash
# Unpacks SDK archives into third_party/ and creates the project-local cross tools. Touches nothing outside the project. Idempotent.
# Run after scripts/fetch.py and scripts/setup_env.sh. Needs apt-get only to fetch the GCC cross debs (no root changes, no install).
set -uo pipefail
cd "$(dirname "$0")/.." && source scripts/env.sh
A=deps/archives; T=third_party; mkdir -p "$T" .envs/tools/bin logs
x(){ d="$T/$1"; [ -n "$(ls -A "$d" 2>/dev/null)" ] && return 0; mkdir -p "$d"; case "$2" in
  *.tgz|*.tar.gz) tar xzf "$2" -C "$d" --strip-components="${3:-1}" 2>/dev/null ;;
  *.tar.xz) tar xJf "$2" -C "$d" --strip-components="${3:-1}" ;;
  *.tar.zst) tar --zstd -xf "$2" -C "$d" --strip-components="${3:-1}" ;;
  *.zip) python3 -I -m zipfile -e "$2" "$d/" ;;
esac; echo "extracted $1"; }
x onnxruntime-x64 $A/onnxruntime-x64/*.tgz; x onnxruntime-aarch64 $A/onnxruntime-aarch64/*.tgz; x ncnn-ubuntu $A/ncnn-ubuntu/*.zip; x ncnn-android $A/ncnn-android/*.zip; x ncnn-src $A/ncnn-src/*.zip; x mnn-src $A/mnn-src/*.gz; x mnn-android $A/mnn-android/*.zip; x openvino $A/openvino-ubuntu24/*.tgz; x iree-dist $A/iree-dist/*.xz 0; x mindspore-lite $A/mindspore-lite/*.gz; x qemu-arm $A/qemu-arm-xpack/*.gz; x tensorflow $A/tensorflow-src/*.gz; x tflite-micro $A/tflite-micro-src/*.gz; x cmsis-nn $A/cmsis-nn-src/*.gz; x paddle-lite-armv8 $A/paddle-lite-armv8/*.gz; x paddle-mobilenet $A/paddle-mobilenet-v1/*.gz 0; x darknet $A/darknet-src/*.gz; x llama.cpp $A/llama-cpp-src/*.gz; x whisper.cpp $A/whisper-cpp-src/*.gz
x arm-gcc $A/arm-none-eabi-gcc/*.tar.gz
mkdir -p $T/android/system-images/android-34/default
[ -x $T/android/android-ndk-r27d/ndk-build ] || for z in $A/android-ndk/*.zip $A/android-platform-tools/*.zip $A/android-emulator/*.zip; do python3 -I scripts/unzip_full.py "$z" $T/android; done
[ -d $T/android/system-images/android-34/default/x86_64 ] || python3 -I scripts/unzip_full.py $A/android-sysimg-34-x86_64/*.zip $T/android/system-images/android-34/default
[ -f $T/onnxruntime-android/AndroidManifest.xml ] || python3 -I scripts/unzip_full.py $A/onnxruntime-android/*.aar $T/onnxruntime-android
[ -x "$T/python37/install/bin/python3" ] || x python37 $A/python37-standalone/*.zst 1
chmod +x $T/ncnn-ubuntu/*/bin/* 2>/dev/null
if [ -z "$(ls -A $T/iree-src 2>/dev/null)" ]; then mkdir -p $T/iree-src; tar xzf $A/iree-src/iree-3.5.0.tar.gz -C $T/iree-src --strip-components=1 --wildcards '*/runtime/src/iree/*.h' 2>/dev/null; fi
# runtime libraries unpacked locally, never installed
mkdir -p $T/local_libs
for d in $A/libprotobuf32-deb/*.deb $A/libssl1.1-deb/*.deb; do t=$(mktemp -d -p "$T"); dpkg-deb -x "$d" "$t"; find "$t" -name '*.so*' -exec cp -a {} $T/local_libs/ \; ; rm -rf -- "$t"; done
# X11 client libraries for the headless Android emulator, unpacked locally
mkdir -p $A/x11-debs $T/local_x11; [ -n "$(ls -A $A/x11-debs)" ] || (cd $A/x11-debs && apt-get download libx11-6 libx11-xcb1 libxcb1 libxau6 libxdmcp6 libbsd0 libmd0 libxext6 libxrender1 libxi6 libxfixes3 libxkbcommon0)
for d in $A/x11-debs/*.deb; do t=$(mktemp -d -p "$T"); dpkg-deb -x "$d" "$t"; find "$t" -name '*.so*' -exec cp -a {} $T/local_x11/ \; ; rm -rf -- "$t"; done
# QEMU
chmod +x $A/qemu-aarch64-static/qemu-aarch64-static $A/qemu-arm-static/qemu-arm-static
ln -sf ../../../$A/qemu-aarch64-static/qemu-aarch64-static .envs/tools/bin/qemu-aarch64; ln -sf ../../../$A/qemu-arm-static/qemu-arm-static .envs/tools/bin/qemu-arm
# GCC aarch64 cross toolchain, from Ubuntu debs. apt verifies them; this only downloads to the project folder.
P="gcc-15-aarch64-linux-gnu g++-15-aarch64-linux-gnu cpp-15-aarch64-linux-gnu binutils-aarch64-linux-gnu libc6-dev-arm64-cross libc6-arm64-cross linux-libc-dev-arm64-cross libgcc-15-dev-arm64-cross libstdc++-15-dev-arm64-cross libstdc++6-arm64-cross libgcc-s1-arm64-cross libgomp1-arm64-cross libatomic1-arm64-cross libasan8-arm64-cross libitm1-arm64-cross liblsan0-arm64-cross libtsan2-arm64-cross libubsan1-arm64-cross libhwasan0-arm64-cross"
if [ ! -x $T/gcc-aarch64/usr/bin/aarch64-linux-gnu-g++-15 ]; then
  mkdir -p $A/gcc-aarch64-debs; [ -n "$(ls -A $A/gcc-aarch64-debs)" ] || (cd $A/gcc-aarch64-debs && apt-get download $P)
  mkdir -p $T/gcc-aarch64; for d in $A/gcc-aarch64-debs/*.deb; do dpkg-deb -x "$d" $T/gcc-aarch64; done
fi
G=$PWD/$T/gcc-aarch64/usr; for f in libc.so libm.so; do sed -i "s|/usr/aarch64-linux-gnu/lib/||g; s|/lib/ld-linux-aarch64.so.1|ld-linux-aarch64.so.1|g" $G/aarch64-linux-gnu/lib/$f; done
LIBD=$G/lib/x86_64-linux-gnu; for c in gcc g++; do printf '#!/bin/sh\nLD_LIBRARY_PATH="%s:$LD_LIBRARY_PATH" exec "%s/bin/aarch64-linux-gnu-%s-15" "$@"\n' "$LIBD" "$G" "$c" > .envs/tools/bin/a64-$c; done
# zig wrappers
Z=$PWD/.envs/main/lib/python3.12/site-packages/ziglang/zig
w(){ printf '#!/bin/sh\nexec "%s" %s "$@"\n' "$Z" "$2" > .envs/tools/bin/$1; }
w zcc-aarch64 "cc -target aarch64-linux-gnu.2.28"; w zcxx-aarch64 "c++ -target aarch64-linux-gnu.2.28"; w zcc-arm32 "cc -target arm-linux-gnueabihf.2.28"; w zcxx-arm32 "c++ -target arm-linux-gnueabihf.2.28"
w zcc-arm32musl "cc -target arm-linux-musleabihf -mcpu=cortex_a7"; w zcxx-arm32musl "c++ -target arm-linux-musleabihf -mcpu=cortex_a7"; w zig-ar ar; w zig-ranlib ranlib
cat > .envs/tools/bin/unzip <<'U'
#!/usr/bin/env python3
"""Minimal unzip stand-in for hosts without unzip: supports -q, -o and -d, as used by third-party download scripts."""
import sys, zipfile
a = sys.argv[1:]; dest = "."; f = None; i = 0
while i < len(a):
    if a[i] == "-d": dest = a[i + 1]; i += 2; continue
    if not a[i].startswith("-"): f = a[i]
    i += 1
zipfile.ZipFile(f).extractall(dest)
U
chmod +x .envs/tools/bin/*
# Vendor files fetched outside fetch.py
mkdir -p $T/rknn_sdk; cp $A/rknn-api-h/rknn_api.h $A/rknnrt-aarch64/librknnrt.so $T/rknn_sdk/
if [ ! -f $T/edgetpu_compiler/edgetpu_compiler ]; then mkdir -p $T/edgetpu_compiler; b=https://raw.githubusercontent.com/google-coral/edgetpu/master/compiler/x86_64/edgetpu_compiler_bin
  for n in LICENSES NOTICE edgetpu_compiler ld-linux-x86-64.so.2 libc++.so.1 libc++abi.so.1 libc.so.6 libdl.so.2 libm.so.6 libpthread.so.0 libresolv.so.2 librt.so.1; do curl -sfL -m 120 -o $T/edgetpu_compiler/$n $b/$n; done; fi
chmod +x $T/edgetpu_compiler/edgetpu_compiler $T/edgetpu_compiler/ld-linux-x86-64.so.2
# TensorRT public headers, for a compile check only (no SDK, no GPU)
if [ -z "$(ls -A $T/tensorrt-headers 2>/dev/null)" ]; then mkdir -p $T/tensorrt-headers; gh api 'repos/NVIDIA/TensorRT/contents/include?ref=release/10.11' --jq '.[]|select(.type=="file")|[.name,.download_url]|@tsv' | while IFS=$'\t' read -r n u; do curl -sfL -m 60 -o "$T/tensorrt-headers/$n" "$u"; done; fi
# Mesa lavapipe software Vulkan, unpacked locally
if [ -z "$(ls -A $T/lavapipe 2>/dev/null)" ]; then mkdir -p $A/lavapipe-debs $T/lavapipe/icd; [ -n "$(ls -A $A/lavapipe-debs)" ] || (cd $A/lavapipe-debs && apt-get download mesa-vulkan-drivers libvulkan1 libllvm21 libdisplay-info3 libwayland-client0 libxcb-dri3-0 libxcb-present0 libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxshmfence1); for d in $A/lavapipe-debs/*.deb; do dpkg-deb -x "$d" $T/lavapipe; done; fi
LVP=$(find $T/lavapipe -name libvulkan_lvp.so | head -1); python3 - "$(find $T/lavapipe -name 'lvp_icd*.json' | head -1)" "$PWD/$LVP" <<'P'
import json, sys
d = json.load(open(sys.argv[1])); d["ICD"]["library_path"] = sys.argv[2]; json.dump(d, open("third_party/lavapipe/icd/lvp.json", "w"))
P
echo "tools ready"
