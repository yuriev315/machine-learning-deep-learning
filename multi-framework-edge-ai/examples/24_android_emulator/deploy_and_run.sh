#!/usr/bin/env bash
# Project 24: deploy native CLIs to a real Android 14 system image (x86_64, KVM, Android's own kernel and bionic) with adb, and measure accuracy.
# It proves Android packaging, bionic linking and SELinux/exec behaviour on a real Android OS. It is x86_64, not ARM, and it is an emulator.
cd "$(dirname "$0")/../.." && source scripts/env.sh
ADB="third_party/android/platform-tools/adb -s emulator-5580"; D=/data/local/tmp/mfea; A=examples/artifacts; O=build/android; B=third_party/_build/android; NDK=third_party/android/android-ndk-r27d
rec="python3 scripts/record_result.py --status RUNNABLE_VERIFIED --hw Android-14-emulator-x86_64-KVM --exec android-emulator"
timeout 600 $ADB wait-for-device || { echo "no device"; exit 1; }
for i in $(seq 1 120); do [ "$($ADB shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')" = 1 ] && break; read -t 5 < /dev/zero 2>/dev/null || python3 -c "import time;time.sleep(5)"; done
echo "boot_completed=$($ADB shell getprop sys.boot_completed | tr -d '\r') android=$($ADB shell getprop ro.build.version.release | tr -d '\r') abi=$($ADB shell getprop ro.product.cpu.abi | tr -d '\r') kernel=$($ADB shell uname -r | tr -d '\r')"
$ADB shell "mkdir -p $D/lib"
p(){ $ADB push "$@" >/dev/null || echo "push failed: $*"; }
p $O/ort_x86_64/ort_digits $D/; p third_party/onnxruntime-android/jni/x86_64/libonnxruntime.so $D/lib/
p $O/ncnn_x86_64/ncnn_digits $D/; p $O/mnn_x86_64/mnn_digits $D/
[ -f $O/et_x86_64/et_digits ] && { p $O/et_x86_64/et_digits $D/; p $A/executorch/tinycnn_xnnpack.pte $D/; p $A/executorch/tinycnn_xnnpack_int8.pte $D/; }
[ -f $O/litert_x86_64/litert_digits ] && { p $O/litert_x86_64/litert_digits $D/; p $B/tflite_x86_64/libtensorflowlite_c.so $D/lib/; p $NDK/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/x86_64-linux-android/libc++_shared.so $D/lib/; }
for f in $A/pytorch/tinycnn.onnx $A/ncnn/tinycnn_opt.param $A/ncnn/tinycnn_opt.bin $A/mnn/tinycnn.mnn $A/tensorflow/tinycnn_float.tflite $A/tensorflow/tinycnn_int8.tflite examples/data/digits_test.bin; do p $f $D/; done
$ADB shell "chmod 755 $D/*_digits"
run(){ $ADB shell "cd $D && LD_LIBRARY_PATH=$D/lib ./$*" 2>&1 | tr -d '\r' | grep -E 'RESULT|rror|CANNOT|not found' | cut -c1-220; }
run ort_digits tinycnn.onnx digits_test.bin 1 pytorch_onnx_ort_android_x86_64 | $rec
run ncnn_digits tinycnn_opt.param tinycnn_opt.bin digits_test.bin input logits 1 pytorch_onnx_ncnn_android_x86_64 | $rec
run mnn_digits tinycnn.mnn digits_test.bin 1 pytorch_onnx_mnn_android_x86_64 | $rec
if [ -f $O/litert_x86_64/litert_digits ]; then for m in float int8; do run litert_digits tinycnn_$m.tflite digits_test.bin 1 tf_litert_${m}_android_x86_64 | $rec --api "C API"; done; fi
if [ -f $O/et_x86_64/et_digits ]; then for m in "tinycnn_xnnpack pytorch_executorch_android_x86_64" "tinycnn_xnnpack_int8 pytorch_executorch_int8_android_x86_64"; do set -- $m; run et_digits $1.pte digits_test.bin $2 | $rec; done; fi
