# TensorFlow / Keras

- **维护状态：** 活跃维护
- **使用版本：** TensorFlow 2.19.0，Keras 3.10.0
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/02_tensorflow_keras](../../examples/02_tensorflow_keras)

训练 → `.keras` / `.h5` / SavedModel / 冻结 GraphDef / `.tflite`（FP32、动态范围、全整数 INT8）/ ONNX（tf2onnx）。新版转换器会给全连接层用逐通道量化，手写 CMSIS-NN 调用时要用 `arm_fully_connected_per_channel_s8`。TF、Paddle、MindSpore 不能在同一进程导入，protobuf 会冲突。

## 官方资料

- [TF 安装](https://www.tensorflow.org/install)
- [SavedModel](https://www.tensorflow.org/guide/saved_model)
- [Keras 保存](https://keras.io/guides/serialization_and_saving/)
- [LiteRT 转换](https://ai.google.dev/edge/litert/models/convert)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
