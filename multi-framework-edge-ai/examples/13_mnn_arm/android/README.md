# MNN on Android

Status: `SDK_REQUIRED` and `HARDWARE_REQUIRED`. Not built here, because the NDK is over the download limit.

`deps/archives/mnn-android/` holds the official prebuilt library for arm64-v8a. The C++ in `../main.cpp` needs no changes:

```
cmake -S .. -B build-android -G Ninja \
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-24 -DANDROID_STL=c++_shared \
  -DMNN_INCLUDE=<sdk>/include -DMNN_LIB=<sdk>/arm64-v8a/libMNN.so
cmake --build build-android
adb push build-android/mnn_digits tinycnn.mnn digits_test.bin <sdk>/arm64-v8a/libMNN.so $ANDROID_NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/libc++_shared.so /data/local/tmp/
adb shell "cd /data/local/tmp && LD_LIBRARY_PATH=. ./mnn_digits tinycnn.mnn digits_test.bin 2"
```
