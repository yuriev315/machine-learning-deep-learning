#!/usr/bin/env bash
# Runs every other converted model through a real C++ runtime and measures accuracy, so a conversion is never counted just because a file was written.
cd "$(dirname "$0")/.." && source scripts/env.sh
A=examples/artifacts; D=examples/data/digits_test.bin; B=build/x64; rec="python3 scripts/record_result.py"
export LD_LIBRARY_PATH=$PWD/third_party/openvino/runtime/lib/intel64:$PWD/third_party/openvino/runtime/3rdparty/tbb/lib:$PWD/third_party/local_libs
cmake --build $B/mnn >/dev/null 2>&1
$B/ort/ort_digits $A/mxnet/tinycnn.onnx $D 1 mxnet_onnx_ort_cpp | $rec
$B/ort/ort_digits $A/mindspore/tinycnn.onnx $D 1 mindspore_onnx_ort_cpp | $rec
$B/ort/ort_digits $A/paddle/tinycnn.onnx $D 1 paddle_onnx_ort_cpp | $rec
$B/ort/ort_digits $A/quant/static_qdq_perchannel.onnx $D 1 pytorch_onnx_ort_static_int8_cpp | $rec
L=$(tail -1 $A/ncnn/mxnet.param | awk '{print $NF}' ); O=$(tail -1 $A/ncnn/mxnet.param | awk '{for(i=1;i<=NF;i++) if($i ~ /fwd|output|dense/) x=$i} END{print x}')
$B/ncnn/ncnn_digits $A/ncnn/mxnet.param $A/ncnn/mxnet.bin $D data "$O" 1 mxnet_ncnn_cpp | $rec
$B/mnn/mnn_digits $A/mnn/tinycnn.mnn $D 1 pytorch_onnx_mnn_cpp 2>/dev/null | $rec
$B/mnn/mnn_digits $A/mnn/tinycnn_tflite.mnn $D 1 tf_tflite_mnn_cpp 2>/dev/null | $rec
$B/ov/ov_digits $A/openvino/tinycnn_tf.xml $D CPU 1 tf_savedmodel_openvino_cpp | $rec
$B/ov/ov_digits $A/openvino/tinycnn_tflite.xml $D CPU 1 tf_tflite_openvino_cpp | $rec
$B/ov/ov_digits $A/openvino/tinycnn_int8.xml $D CPU 1 pytorch_onnx_openvino_nncf_int8_cpp | $rec
$B/msl/msl_digits $A/mindspore_lite/tinycnn_onnx.ms $D 1 pytorch_onnx_mindspore_lite_cpp 2>/dev/null | $rec
$B/msl/msl_digits $A/mindspore_lite/tinycnn_tflite.ms $D 1 tf_tflite_mindspore_lite_cpp 2>/dev/null | $rec
# IREE: the same StableHLO cross-compiled for other targets (compile only; no runtime for them here)
iree-compile --iree-input-type=stablehlo --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-triple=aarch64-linux-gnu $A/jax/tinycnn.stablehlo.mlir -o $A/jax/tinycnn_aarch64-linux-gnu.vmfb && echo "iree cross-compile ok: aarch64"
# riscv64 needs an explicit hard-float ABI: with the default, iree-lld fails on __mulsf3 and other soft-float helpers
iree-compile --iree-input-type=stablehlo --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-triple=riscv64-linux-gnu --iree-llvmcpu-target-abi=lp64d --iree-llvmcpu-target-cpu-features=+m,+a,+f,+d,+c $A/jax/tinycnn.stablehlo.mlir -o $A/jax/tinycnn_riscv64-linux-gnu.vmfb && echo "iree cross-compile ok: riscv64"
[ -s $A/jax/tinycnn_aarch64-linux-gnu.vmfb ] && [ -s $A/jax/tinycnn_riscv64-linux-gnu.vmfb ]
