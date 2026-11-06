# 运行方式：android

ORT、ncnn、MNN、LiteRT、ExecuTorch 都用 NDK r27d 编译，并在 **Android 14 x86_64 模拟器**（KVM）上用 adb 部署运行，见 [examples/24_android_emulator](../../examples/24_android_emulator)。这是真实的 Android 系统和 bionic，但不是 ARM。arm64-v8a 只验证了编译和链接。**没有手机，也没有构建 APK**，[Gradle 和 JNI 代码](../../examples/12_ncnn_arm/android)里只有 JNI `.so` 编译过。
