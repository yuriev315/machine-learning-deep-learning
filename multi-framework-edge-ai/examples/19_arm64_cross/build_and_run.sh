#!/usr/bin/env bash
# Project 19: cross-compile the same C++ sources for ARM64 and run them under QEMU user-mode.
# QEMU proves the binaries, libraries and models work on the ARM64 ISA. Its latency says nothing about real hardware,
# so results are recorded with execution=qemu-user and never as DEVICE_DEPLOYMENT_VERIFIED.
cd "$(dirname "$0")/../.." && source scripts/env.sh
T=$PWD/third_party; E=$PWD/examples; A=$E/artifacts; D=$E/data/digits_test.bin; B=$PWD/build/a64; TC=$PWD/scripts/toolchains/zig-aarch64.cmake; Q="qemu-aarch64 -L $A64_SYSROOT"
rec="python3 scripts/record_result.py --status RUNNABLE_VERIFIED --hw qemu-aarch64-user --exec qemu-user"
mkdir -p logs
b(){ n=$1; s=$2; shift 2; if cmake -G Ninja -S $s -B $B/$n -DCMAKE_TOOLCHAIN_FILE=$TC -DCMAKE_BUILD_TYPE=Release "$@" > logs/a64_$n.log 2>&1 && cmake --build $B/$n -j2 >> logs/a64_$n.log 2>&1; then echo "A64_BUILD_OK   $n"; else echo "A64_BUILD_FAIL $n (logs/a64_$n.log)"; return 1; fi; }
b ort $E/06_onnxruntime_cpp -DORT_ROOT=$T/onnxruntime-aarch64 && LD_LIBRARY_PATH=$T/onnxruntime-aarch64/lib $Q -E LD_LIBRARY_PATH=$T/onnxruntime-aarch64/lib $B/ort/ort_digits $A/pytorch/tinycnn.onnx $D 1 pytorch_onnx_ort_cpp_a64 | $rec
b ncnn $E/12_ncnn_arm -Dncnn_DIR=$T/_build/ncnn_a64/install/lib/cmake/ncnn && $Q $B/ncnn/ncnn_digits $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $D input logits 1 pytorch_onnx_ncnn_cpp_a64 | $rec
if [ -f $T/_build/mnn_a64/libMNN.so ]; then b mnn $E/13_mnn_arm -DMNN_INCLUDE=$T/mnn-src/include -DMNN_LIB=$T/_build/mnn_a64/libMNN.so && $Q -E LD_LIBRARY_PATH=$T/_build/mnn_a64 $B/mnn/mnn_digits $A/mnn/tinycnn.mnn $D 1 pytorch_onnx_mnn_cpp_a64 | $rec; fi
if [ -f $T/_build/tflite_a64/libtensorflowlite_c.so ]; then b litert $E/07_litert_c -DTFLITE_SRC=$T/tensorflow -DTFLITE_LIB=$T/_build/tflite_a64/libtensorflowlite_c.so && for m in float int8; do $Q -E LD_LIBRARY_PATH=$T/_build/tflite_a64 $B/litert/litert_digits $A/tensorflow/tinycnn_$m.tflite $D 1 tf_litert_${m}_c_api_a64 | $rec --api "C API"; done; fi
