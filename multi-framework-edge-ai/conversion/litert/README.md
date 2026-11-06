# LiteRT / TensorFlow Lite

输入：Keras、SavedModel、concrete function。输出：`.tflite`。C API 从 TF 2.19.0 源码编译，x86-64、QEMU ARM64 和 Android 模拟器都已运行。量化：动态范围、全整数 INT8。

项目：[examples/07_litert_c](../../examples/07_litert_c)

## 官方资料

- [LiteRT](https://ai.google.dev/edge/litert)
- [CMake 编译](https://ai.google.dev/edge/litert/build/cmake)
- [训练后量化](https://ai.google.dev/edge/litert/models/post_training_quantization)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
