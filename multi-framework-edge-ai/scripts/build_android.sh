#!/usr/bin/env bash
# Builds SDKs and example CLIs with NDK r27d, for arm64-v8a (compile and link only) and x86_64 (runs on the emulator). Linking is dynamic: libandroid has no static form.
cd "$(dirname "$0")/.." && source scripts/env.sh
T=$PWD/third_party; NDK=$T/android/android-ndk-r27d; TC=$NDK/build/cmake/android.toolchain.cmake; B=$T/_build/android; E=$PWD/examples; O=$PWD/build/android; mkdir -p $B $O logs
J=3
for ABI in x86_64 arm64-v8a; do
  C="-DCMAKE_TOOLCHAIN_FILE=$TC -DANDROID_ABI=$ABI -DANDROID_PLATFORM=android-24 -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5"
  cmake -G Ninja -S $T/ncnn-src -B $B/ncnn_$ABI $C -DNCNN_BUILD_TOOLS=OFF -DNCNN_BUILD_EXAMPLES=OFF -DNCNN_BUILD_BENCHMARK=OFF -DNCNN_VULKAN=OFF -DNCNN_SHARED_LIB=OFF -DNCNN_OPENMP=OFF -DNCNN_THREADS=ON -DNCNN_SIMPLEOCV=OFF -DCMAKE_INSTALL_PREFIX=$B/ncnn_$ABI/install > logs/android_ncnn_$ABI.log 2>&1 && cmake --build $B/ncnn_$ABI -j$J --target install >> logs/android_ncnn_$ABI.log 2>&1 && echo "OK ncnn $ABI" || echo "FAIL ncnn $ABI"
  cmake -G Ninja -S $E/12_ncnn_arm -B $O/ncnn_$ABI $C -Dncnn_DIR=$B/ncnn_$ABI/install/lib/cmake/ncnn > logs/android_ncnn_app_$ABI.log 2>&1 && cmake --build $O/ncnn_$ABI >> logs/android_ncnn_app_$ABI.log 2>&1 && echo "OK ncnn app $ABI" || echo "FAIL ncnn app $ABI"
  cmake -G Ninja -S $T/mnn-src -B $B/mnn_$ABI $C -DMNN_BUILD_TOOLS=OFF -DMNN_BUILD_SHARED_LIBS=OFF -DMNN_SEP_BUILD=OFF -DMNN_ARM82=OFF > logs/android_mnn_$ABI.log 2>&1 && cmake --build $B/mnn_$ABI -j$J >> logs/android_mnn_$ABI.log 2>&1 && echo "OK MNN $ABI" || echo "FAIL MNN $ABI"
  rm -f $O/mnn_$ABI/CMakeCache.txt $O/ncnn_$ABI/CMakeCache.txt   # earlier configurations used -static, which bionic log/android libs cannot satisfy
  cmake -G Ninja -S $E/13_mnn_arm -B $O/mnn_$ABI $C -DMNN_INCLUDE=$T/mnn-src/include -DMNN_LIB=$B/mnn_$ABI/libMNN.a > logs/android_mnn_app_$ABI.log 2>&1 && cmake --build $O/mnn_$ABI >> logs/android_mnn_app_$ABI.log 2>&1 && echo "OK MNN app $ABI" || echo "FAIL MNN app $ABI"
done
# ONNX Runtime: official Android AAR, laid out as an SDK. LiteRT C API from source.
for ABI in x86_64 arm64-v8a; do
  R=$T/onnxruntime-android; mkdir -p $R/sdk_$ABI/lib; cp $R/jni/$ABI/libonnxruntime.so $R/sdk_$ABI/lib/; ln -sfn ../headers $R/sdk_$ABI/include
  cmake -G Ninja -S $E/06_onnxruntime_cpp -B $O/ort_$ABI -DCMAKE_TOOLCHAIN_FILE=$TC -DANDROID_ABI=$ABI -DANDROID_PLATFORM=android-24 -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release -DORT_ROOT=$R/sdk_$ABI > logs/android_ort_app_$ABI.log 2>&1 && cmake --build $O/ort_$ABI >> logs/android_ort_app_$ABI.log 2>&1 && echo "OK ORT app $ABI" || echo "FAIL ORT app $ABI"
done
for ABI in x86_64 arm64-v8a; do
  C="-DCMAKE_TOOLCHAIN_FILE=$TC -DANDROID_ABI=$ABI -DANDROID_PLATFORM=android-24 -DANDROID_STL=c++_shared -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5"
  cmake -G Ninja -S $T/tensorflow/tensorflow/lite/c -B $B/tflite_$ABI $C -DTFLITE_ENABLE_GPU=OFF -DXNNPACK_ENABLE_KLEIDIAI=OFF -DTFLITE_HOST_TOOLS_DIR=$(dirname $(find $T/_build/tflite_c -type f -name flatc -perm -u+x | head -1)) > logs/android_tflite_$ABI.log 2>&1 && cmake --build $B/tflite_$ABI -j$J >> logs/android_tflite_$ABI.log 2>&1 && echo "OK LiteRT $ABI" || echo "FAIL LiteRT $ABI"
  cmake -G Ninja -S $E/07_litert_c -B $O/litert_$ABI $C -DTFLITE_SRC=$T/tensorflow -DTFLITE_LIB=$B/tflite_$ABI/libtensorflowlite_c.so > logs/android_litert_app_$ABI.log 2>&1 && cmake --build $O/litert_$ABI >> logs/android_litert_app_$ABI.log 2>&1 && echo "OK LiteRT app $ABI" || echo "FAIL LiteRT app $ABI"
  C2="-DCMAKE_TOOLCHAIN_FILE=$TC -DANDROID_ABI=$ABI -DANDROID_PLATFORM=android-24 -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5"
  cmake -G Ninja -S $E/12_ncnn_arm/android/app/src/main/cpp -B $O/jni_$ABI $C2 -Dncnn_DIR=$B/ncnn_$ABI/install/lib/cmake/ncnn > logs/android_jni_$ABI.log 2>&1 && cmake --build $O/jni_$ABI >> logs/android_jni_$ABI.log 2>&1 && echo "OK ncnn JNI .so $ABI" || echo "FAIL ncnn JNI .so $ABI"
done
