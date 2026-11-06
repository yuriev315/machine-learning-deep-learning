#!/usr/bin/env bash
# Configures, builds and runs the x86-64 C++ examples (GCC + CMake + Ninja). Measurements go to manifests/runtime_test_results.csv.
cd "$(dirname "$0")/.." && source scripts/env.sh
T=$PWD/third_party; E=examples; A=$E/artifacts; D=$E/data/digits_test.bin; B=$PWD/build; mkdir -p $B logs
rec="python3 scripts/record_result.py --status RUNNABLE_VERIFIED"
cfg(){ n=$1; src=$2; shift 2; if cmake -G Ninja -S $src -B $B/x64/$n -DCMAKE_BUILD_TYPE=Release "$@" > logs/cpp_$n.log 2>&1 && cmake --build $B/x64/$n -j4 >> logs/cpp_$n.log 2>&1; then echo "BUILD_OK   $n"; return 0; else echo "BUILD_FAIL $n (logs/cpp_$n.log)"; return 1; fi; }
if cfg ort $E/06_onnxruntime_cpp -DORT_ROOT=$T/onnxruntime-x64; then
  $B/x64/ort/ort_digits $A/pytorch/tinycnn.onnx $D 1 pytorch_onnx_ort_cpp | $rec; fi
if cfg litert $E/07_litert_c -DTFLITE_SRC=$T/tensorflow -DTFLITE_LIB=$T/_build/tflite_c/libtensorflowlite_c.so; then
  for m in float int8 dynrange; do $B/x64/litert/litert_digits $A/tensorflow/tinycnn_$m.tflite $D 1 tf_litert_${m}_c_api | $rec --api "C API"; done; fi
if cfg ov $E/10_openvino_cpp -DOpenVINO_DIR=$T/openvino/runtime/cmake "-DCMAKE_EXE_LINKER_FLAGS=-Wl,-rpath-link,$T/openvino/runtime/3rdparty/tbb/lib"; then
  export LD_LIBRARY_PATH=$T/openvino/runtime/lib/intel64:$T/openvino/runtime/3rdparty/tbb/lib:$LD_LIBRARY_PATH
  $B/x64/ov/ov_digits $A/openvino/tinycnn_onnx.xml $D CPU 1 pytorch_onnx_openvino_cpp | $rec
  if [ -f $A/openvino/tinycnn_int8.xml ]; then $B/x64/ov/ov_digits $A/openvino/tinycnn_int8.xml $D CPU 1 pytorch_onnx_openvino_nncf_int8_cpp | $rec; fi; fi
NC=$T/ncnn-ubuntu/$(ls $T/ncnn-ubuntu)
if cfg ncnn $E/12_ncnn_arm -Dncnn_DIR=$NC/lib/cmake/ncnn; then
  $B/x64/ncnn/ncnn_digits $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $D input logits 1 pytorch_onnx_ncnn_cpp | $rec
  $B/x64/ncnn/ncnn_digits $A/ncnn/tinycnn_pnnx.ncnn.param $A/ncnn/tinycnn_pnnx.ncnn.bin $D in0 out0 1 pytorch_pnnx_ncnn_cpp | $rec; fi
if cfg mnn $E/13_mnn_arm -DMNN_INCLUDE=$T/mnn-src/include -DMNN_LIB=$T/_build/mnn_x64/libMNN.so; then
  $B/x64/mnn/mnn_digits $A/mnn/tinycnn.mnn $D 1 pytorch_onnx_mnn_cpp | $rec
  $B/x64/mnn/mnn_digits $A/mnn/tinycnn_w8.mnn $D 1 pytorch_onnx_mnn_weightq8_cpp | $rec; fi
if cfg msl $E/04b_mindspore_lite -DMSL_RUNTIME=$T/mindspore-lite/runtime; then
  $B/x64/msl/msl_digits $A/mindspore_lite/tinycnn_onnx.ms $D 1 pytorch_onnx_mindspore_lite_cpp | $rec
fi
