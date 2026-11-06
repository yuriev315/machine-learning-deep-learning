# ONNX 与 ONNX Runtime

输入：PyTorch、MXNet、MindSpore 等。输出：`.onnx`。运行时 1.22.0，C/C++ API。量化：动态（UInt8）、静态 QDQ（逐张量、逐通道）、FP16、INT4 权重。注意：`ConvInteger` 配 int8 权重在 CPU 上没有实现。

项目：[examples/06_onnxruntime_cpp](../../examples/06_onnxruntime_cpp)

## 官方资料

- [ORT 文档](https://onnxruntime.ai/docs/)
- [量化](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html)
- [官方示例](https://github.com/microsoft/onnxruntime-inference-examples)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
