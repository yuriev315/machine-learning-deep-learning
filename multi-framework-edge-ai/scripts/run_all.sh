#!/usr/bin/env bash
# Full pipeline after SDKs exist: data -> training -> conversion -> build -> inference on every route available here.
# Each step reports PASS or FAIL and the run continues, so one broken route does not hide the others. Logs: logs/step_*.log
cd "$(dirname "$0")/.." && source scripts/env.sh
L37=$PWD/.envs/legacy37/bin; export LD_LIBRARY_PATH=$PWD/third_party/local_libs
rec="python3 scripts/record_result.py"; pass=0; fail=0
s(){ n=$1; shift; if ( set -o pipefail; "$@" ) > logs/step_$n.log 2>&1; then echo "PASS $n"; pass=$((pass+1)); else echo "FAIL $n (logs/step_$n.log)"; fail=$((fail+1)); fi; }
s data python examples/common/prepare_data.py
s pytorch bash -c "python -W ignore examples/01_pytorch/train_export.py | $rec --api Python"
s tensorflow python examples/02_tensorflow_keras/tf_train_convert.py
s tf2onnx_check bash -c "python -W ignore examples/02_tensorflow_keras/check_tf2onnx.py | $rec --api Python"
s jax_keras bash -c "python -W ignore examples/03_jax_flax/train_export.py | $rec --api Python"
s mxnet $L37/python examples/05_mxnet_legacy/train_export.py
s mindspore python $PWD/examples/04b_mindspore_lite/train_export.py
s paddle_train bash -c "python examples/04_paddle_lite/train_export.py train | grep -E 'accuracy|RESULT' | tee /dev/stderr | grep RESULT | $rec --api Python"
s paddle_legacy_export python examples/04_paddle_lite/train_export.py legacy
s paddle2onnx python -W ignore -c "import paddle2onnx; paddle2onnx.export('examples/artifacts/paddle/pir/tinycnn.json','examples/artifacts/paddle/pir/tinycnn.pdiparams','examples/artifacts/paddle/tinycnn.onnx',opset_version=17)"
s paddle_lite_opt $L37/paddle_lite_opt --model_file=examples/artifacts/paddle/legacy/tinycnn.pdmodel --param_file=examples/artifacts/paddle/legacy/tinycnn.pdiparams --valid_targets=arm --optimize_out=examples/artifacts/paddle/tinycnn_arm
s conversions scripts/convert_all.sh
M=$PWD/third_party/mindspore-lite/tools/converter
s mindspore_mindir_lite env LD_LIBRARY_PATH=$M/lib $M/converter/converter_lite --fmk=MINDIR --modelFile=examples/artifacts/mindspore/tinycnn.mindir --outputFile=examples/artifacts/mindspore_lite/tinycnn_ms_mindir
s mindspore_onnx_lite env LD_LIBRARY_PATH=$M/lib $M/converter/converter_lite --fmk=ONNX --modelFile=examples/artifacts/mindspore/tinycnn.onnx --outputFile=examples/artifacts/mindspore_lite/tinycnn_ms_onnx
s paddle_opt $L37/paddle_lite_opt --model_dir=third_party/paddle-mobilenet --valid_targets=arm --optimize_out=examples/artifacts/paddle/mobilenet_v1_arm
s quant bash -c "python -W ignore examples/18_int8_comparison/compare_quant.py | grep RESULT | $rec --api Python"
s executorch_export bash -c "python -W ignore examples/08_executorch_cpp/export_pte.py | grep RESULT | $rec --api 'Python (ExecuTorch pybindings)' --threads 'default pool'"
s coreml bash -c "python -W ignore examples/11_coreml_ios/convert_coreml.py | grep RESULT | $rec --status RUNNABLE_VERIFIED --hw 'Independent MIL interpreter on x86-64 (not Core ML)' --exec simulated-interpreter --api Python"
s rknn bash -c "python -W ignore examples/14_rknn_rockchip/convert_rknn.py | grep RESULT | $rec --status CONVERSION_VERIFIED --hw 'RKNN-Toolkit2 x86 simulator' --exec simulator --api Python"
s tvm bash -c "python -W ignore conversion/tvm/compile_tvm.py | grep RESULT | $rec --api Python"
s edgetpu bash -c "D=third_party/edgetpu_compiler; mkdir -p examples/artifacts/edgetpu; \$D/ld-linux-x86-64.so.2 --library-path \$D \$D/edgetpu_compiler -s -o examples/artifacts/edgetpu examples/artifacts/tensorflow/tinycnn_int8.tflite"
s legacy_models bash -c "N=third_party/ncnn-ubuntu/\$(ls third_party/ncnn-ubuntu)/bin; A=examples/artifacts; D=deps/archives; mkdir -p \$A/caffe \$A/darknet; \$N/caffe2ncnn \$D/squeezenet11-prototxt/deploy.prototxt \$D/squeezenet11-caffemodel/squeezenet_v1.1.caffemodel \$A/caffe/squeezenet.param \$A/caffe/squeezenet.bin && \$N/darknet2ncnn \$D/yolov4-tiny-cfg/yolov4-tiny.cfg \$D/yolov4-tiny-weights/yolov4-tiny.weights \$A/darknet/yolov4tiny.param \$A/darknet/yolov4tiny.bin 1 && python examples/21_legacy_caffe_darknet/verify_legacy.py"
s cpp_x64 bash -c "scripts/build_examples.sh 2>&1 | tee /dev/stderr | grep -q BUILD_FAIL && exit 1 || exit 0"
T=$PWD/third_party; B=$PWD/build; D=examples/data/digits_test.bin; A=examples/artifacts
s et_cpp bash -c "cmake -G Ninja -S examples/08_executorch_cpp -B $B/x64/et -DCMAKE_BUILD_TYPE=Release -DET_ROOT=$T/_build/executorch/install -DET_SRC_PARENT=$T && cmake --build $B/x64/et && for m in 'tinycnn_xnnpack pytorch_executorch_xnnpack_cpp' 'tinycnn_xnnpack_int8 pytorch_executorch_xnnpack_int8_cpp'; do set -- \$m; $B/x64/et/et_digits $A/executorch/\$1.pte $D \$2 2>/dev/null | $rec; done"
s iree_c bash -c "cmake -G Ninja -S examples/03_jax_flax/iree_c -B $B/x64/iree -DCMAKE_BUILD_TYPE=Release -DIREE_DIST=$T/iree-dist -DIREE_RUNTIME_SRC=$T/iree-src/runtime/src && cmake --build $B/x64/iree && $B/x64/iree/iree_digits $A/jax/tinycnn.vmfb jit__lambda_.main $D jax_stablehlo_iree_c_api | $rec --api 'C API'"
s cross_routes scripts/verify_cross_routes.sh
s mindspore_lite_cpp bash -c "$B/x64/msl/msl_digits $A/mindspore_lite/tinycnn_ms_onnx.ms $D 1 mindspore_onnx_lite_cpp 2>/dev/null | $rec; $B/x64/msl/msl_digits $A/mindspore_lite/tinycnn_ms_mindir.ms $D 1 mindspore_mindir_lite_cpp 2>/dev/null | $rec"
s tflm bash -c "O=$B/tflm; TM=$T/tflite-micro; mkdir -p \$O; python3 -c \"b=open('$A/tensorflow/tinycnn_int8.tflite','rb').read();f=open('\$O/tinycnn_int8_model.cc','w');f.write('// C array of tinycnn_int8.tflite: what gets flashed on an MCU\n#include <cstdint>\nalignas(16) extern const unsigned char g_model[] = {'+','.join(str(x) for x in b)+'};\nextern const unsigned int g_model_len = %d;\n'%len(b))\" && cp \$O/tinycnn_int8_model.cc $A/cmsis_nn/tinycnn_int8_tflm_model.cc; g++ -std=c++17 -O2 -DTF_LITE_STATIC_MEMORY -DTF_LITE_STRIP_ERROR_STRINGS -DTF_LITE_DISABLE_X86_NEON -I\$TM -I\$TM/tensorflow/lite/micro/tools/make/downloads/flatbuffers/include -I\$TM/tensorflow/lite/micro/tools/make/downloads/gemmlowp -Iexamples/common/cpp examples/16_tflm_cmsisnn/tflm_digits.cc \$O/tinycnn_int8_model.cc \$TM/gen/linux_x86_64_release_gcc/lib/libtensorflow-microlite.a -o \$O/tflm_digits && \$O/tflm_digits $D tf_tflm_int8_x86 2>&1 | $rec --api 'C++ (TFLM)'"
s cmsis_m4 bash -c "examples/16_tflm_cmsisnn/cortex_m/build_run.sh m4 2>/dev/null | $rec --status RUNNABLE_VERIFIED --hw 'QEMU mps2-an386 Cortex-M4' --exec qemu-system --api 'C (CMSIS-NN)'"
s cmsis_m55_helium bash -c "examples/16_tflm_cmsisnn/cortex_m/build_run.sh m55 2>/dev/null | $rec --status RUNNABLE_VERIFIED --hw 'QEMU mps3-an547 Cortex-M55' --exec qemu-system --api 'C (CMSIS-NN)'"
s tflm_cortex_m4 bash -c "examples/16_tflm_cmsisnn/cortex_m/build_tflm_m4.sh 2>&1 | $rec --status RUNNABLE_VERIFIED --hw 'QEMU mps2-an386 Cortex-M4' --exec qemu-system --api 'C++ (TFLM + CMSIS-NN)'"
s arm64 bash -c "examples/19_arm64_cross/build_and_run.sh 2>&1 | grep -E 'A64_BUILD|RESULT'"
s paddle_arm64 bash -c "cmake -G Ninja -S examples/04_paddle_lite -B $B/a64/paddle -DCMAKE_TOOLCHAIN_FILE=$PWD/scripts/toolchains/gcc-aarch64.cmake -DCMAKE_BUILD_TYPE=Release -DPADDLE_LITE_CXX=$T/paddle-lite-armv8/cxx && cmake --build $B/a64/paddle && cp $T/paddle-lite-armv8/cxx/lib/libpaddle_light_api_shared.so $B/a64/paddle/ && qemu-aarch64 -L $A64_SYSROOT $B/a64/paddle/paddle_mobilenet $A/paddle/mobilenet_v1_arm.nb && qemu-aarch64 -L $A64_SYSROOT $B/a64/paddle/paddle_digits $A/paddle/tinycnn_arm.nb $D paddle_lite_nb_cpp_a64 | $rec --status RUNNABLE_VERIFIED --hw qemu-aarch64-user --exec qemu-user"
s arm32 bash -c "cmake -G Ninja -S examples/12_ncnn_arm -B $B/a32/ncnn -DCMAKE_TOOLCHAIN_FILE=$PWD/scripts/toolchains/zig-arm32-musl.cmake -DCMAKE_BUILD_TYPE=Release -Dncnn_DIR=$T/_build/ncnn_a32/install/lib/cmake/ncnn && cmake --build $B/a32/ncnn && qemu-arm $B/a32/ncnn/ncnn_digits $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $D input logits 1 pytorch_onnx_ncnn_cpp_arm32 | $rec --status RUNNABLE_VERIFIED --hw qemu-arm-user --exec qemu-user"
s rknn_c_build_only bash -c "cmake -G Ninja -S examples/14_rknn_rockchip/c_api -B $B/a64/rknn -DCMAKE_TOOLCHAIN_FILE=$PWD/scripts/toolchains/gcc-aarch64.cmake -DCMAKE_BUILD_TYPE=Release -DRKNN_API_INCLUDE=$T/rknn_sdk -DRKNN_RT_LIB=$T/rknn_sdk/librknnrt.so && cmake --build $B/a64/rknn"
s qnn_c_build_only bash -c "cmake -G Ninja -S examples/15_qualcomm_qnn -B $B/x64/qnn -DCMAKE_BUILD_TYPE=Release -DORT_ROOT=$T/onnxruntime-x64 && cmake --build $B/x64/qnn"
s camera bash -c "cmake -G Ninja -S examples/17_realtime_camera -B $B/x64/camera -DCMAKE_BUILD_TYPE=Release -DORT_ROOT=$T/onnxruntime-x64 && cmake --build $B/x64/camera && $B/x64/camera/realtime_camera $A/pytorch/tinycnn.onnx $D --source=synthetic --frames=450 --fps=60"
s camera_fake_v4l2 bash -c "gcc -shared -fPIC -O2 -o $B/fake_v4l2.so examples/17_realtime_camera/fake_v4l2.c -ldl && LD_PRELOAD=$B/fake_v4l2.so FAKE_V4L2_BIN=$PWD/$D $B/x64/camera/realtime_camera $A/pytorch/tinycnn.onnx $D --source=/dev/video0 --frames=450 --label-in-chroma"
s ncnn_vulkan_lavapipe bash -c "L=\$(dirname \$(find $T/lavapipe -name libvulkan_lvp.so | head -1)); LD_LIBRARY_PATH=\$L:$T/local_x11 VK_ICD_FILENAMES=$T/lavapipe/icd/lvp.json MFEA_NCNN_VULKAN=1 $B/x64/ncnn/ncnn_digits $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $D input logits 2 pytorch_onnx_ncnn_vulkan_lavapipe_cpp | $rec --status RUNNABLE_VERIFIED --hw 'Mesa lavapipe software Vulkan on x86-64' --exec software-gpu --threads 2"
s tensorrt_syntax_check g++ -std=c++17 -c -I$T/tensorrt-headers -Iexamples/09_tensorrt_cpp/stub -Iexamples/common/cpp examples/09_tensorrt_cpp/main.cpp -o $B/trt_main.o
s clean_vm_arm64 bash -c "examples/23_clean_device_vm/make_package.sh && python -u examples/23_clean_device_vm/run_vm_test.py | tee logs/step_vm.log | grep RESULT | $rec --status RUNNABLE_VERIFIED --hw 'QEMU virt Cortex-A76, clean Debian 12' --exec qemu-system"
s android_build scripts/build_android.sh
s android_emulator scripts/run_android.sh
s packaging bash -c "examples/20_packaging/package_and_test.sh 2>&1 | $rec --status RUNNABLE_VERIFIED --hw 'isolated chroot on x86-64 host' --exec chroot-no-network"
s llm bash -c "cmake -G Ninja -S examples/22_llm_gguf -B $B/x64/llm -DCMAKE_BUILD_TYPE=Release -DLLAMA_SRC=$T/llama.cpp -DLLAMA_BUILD=$T/_build/llama && cmake --build $B/x64/llm && $B/x64/llm/llm_gguf deps/archives/stories260k-gguf/stories260K.gguf 'Once upon a time' 40"
s whisper $T/_build/whisper/bin/whisper-cli -m deps/archives/ggml-tiny-en-q5/ggml-tiny.en-q5_1.bin -f $T/whisper.cpp/samples/jfk.wav -t 2 -nt
echo "steps passed=$pass failed=$fail"
[ "$fail" = 0 ]
