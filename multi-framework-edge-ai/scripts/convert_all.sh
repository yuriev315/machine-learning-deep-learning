#!/usr/bin/env bash
# Runs model conversions on examples/artifacts. Each route reports OK/FAIL with its log in logs/conv_<name>.log.
cd "$(dirname "$0")/.." && source scripts/env.sh
A=examples/artifacts; P=$A/pytorch; TF=$A/tensorflow; N=third_party/ncnn-ubuntu/$(ls third_party/ncnn-ubuntu)/bin
ONNX=$P/tinycnn.onnx
export LD_LIBRARY_PATH=$PWD/third_party/local_libs:$LD_LIBRARY_PATH
r(){ n=$1; shift; if "$@" > logs/conv_$n.log 2>&1; then echo "OK   $n"; else echo "FAIL $n (logs/conv_$n.log)"; fi; }
mkdir -p $A/openvino $A/ncnn $A/mnn $A/mindspore_lite
r ovc_onnx      ovc $ONNX --output_model $A/openvino/tinycnn_onnx.xml --input "input[1,1,8,8]"
r ovc_savedmodel ovc $TF/saved_model --output_model $A/openvino/tinycnn_tf.xml --input "[1,8,8,1]"
r ovc_tflite    ovc $TF/tinycnn_float.tflite --output_model $A/openvino/tinycnn_tflite.xml
r onnx2ncnn     $N/onnx2ncnn $ONNX $A/ncnn/tinycnn.param $A/ncnn/tinycnn.bin
[ -s $A/ncnn/tinycnn.bin ] && r ncnnoptimize  $N/ncnnoptimize $A/ncnn/tinycnn.param $A/ncnn/tinycnn.bin $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin 0
r pnnx_ts       bash -c "cd $A/ncnn && pnnx ../pytorch/tinycnn.torchscript.pt inputshape=[1,1,8,8] pnnxparam=tinycnn_pnnx.pnnx.param pnnxbin=tinycnn_pnnx.pnnx.bin pnnxpy=tinycnn_pnnx_pnnx.py pnnxonnx=tinycnn_pnnx.pnnx.onnx ncnnparam=tinycnn_pnnx.ncnn.param ncnnbin=tinycnn_pnnx.ncnn.bin ncnnpy=tinycnn_pnnx_ncnn.py"
r mxnet2ncnn    $N/mxnet2ncnn $A/mxnet/tinycnn-symbol.json $A/mxnet/tinycnn-0000.params $A/ncnn/mxnet.param $A/ncnn/mxnet.bin
r mnn_onnx      mnnconvert -f ONNX --modelFile $ONNX --MNNModel $A/mnn/tinycnn.mnn --bizCode mfea
r mnn_tflite    mnnconvert -f TFLITE --modelFile $TF/tinycnn_float.tflite --MNNModel $A/mnn/tinycnn_tflite.mnn --bizCode mfea
r mnn_weightq8  mnnconvert -f ONNX --modelFile $ONNX --MNNModel $A/mnn/tinycnn_w8.mnn --bizCode mfea --weightQuantBits 8
M=third_party/mindspore-lite/tools/converter; export LD_LIBRARY_PATH_MS=$PWD/$M/lib
r msl_onnx      env LD_LIBRARY_PATH=$PWD/$M/lib $M/converter/converter_lite --fmk=ONNX --modelFile=$ONNX --outputFile=$A/mindspore_lite/tinycnn_onnx
r msl_tflite    env LD_LIBRARY_PATH=$PWD/$M/lib $M/converter/converter_lite --fmk=TFLITE --modelFile=$TF/tinycnn_float.tflite --outputFile=$A/mindspore_lite/tinycnn_tflite
find $A -maxdepth 2 -type f -newermt "-20 minutes" -printf '%s %p\n' | grep -E 'openvino|ncnn|mnn|mindspore' | sed "s|$A/||"
