#!/usr/bin/env bash
# Packs ARM64 binaries, libraries, models and test data for the clean VM. Uses the zig builds, which target glibc 2.28, so they run on older systems.
cd "$(dirname "$0")/../.." && source scripts/env.sh
A=examples/artifacts; B=build/a64; T=third_party
cp $B/ort/ort_digits $B/ncnn/ncnn_digits $B/mnn/mnn_digits $O/bin/
cp -L $T/onnxruntime-aarch64/lib/libonnxruntime.so.1 $O/lib/; cp -L $T/_build/mnn_a64/libMNN.so $O/lib/
cp $A/pytorch/tinycnn.onnx $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $A/mnn/tinycnn.mnn examples/data/digits_test.bin $O/model/
cat > $O/run_all.sh <<'S'
#!/bin/sh
export LD_LIBRARY_PATH=$PWD/lib
echo "LOG $(uname -m) kernel $(uname -r)"
bin/ort_digits model/tinycnn.onnx model/digits_test.bin 1 pytorch_onnx_ort_cpp_vm 2>/dev/null
bin/ncnn_digits model/tinycnn_opt.param model/tinycnn_opt.bin model/digits_test.bin input logits 1 pytorch_onnx_ncnn_cpp_vm 2>/dev/null
bin/mnn_digits model/tinycnn.mnn model/digits_test.bin 1 pytorch_onnx_mnn_cpp_vm 2>/dev/null
S
