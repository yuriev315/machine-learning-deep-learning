# OpenVINO

输入：ONNX、SavedModel、TFLite，三者都已验证。输出：IR。NNCF INT8 已验证。运行在 AMD CPU 上，没有测试 Intel GPU 或 NPU。

项目：[examples/10_openvino_cpp](../../examples/10_openvino_cpp)

## 官方资料

- [文档](https://docs.openvino.ai/)
- [模型转换](https://docs.openvino.ai/2025/openvino-workflow/model-preparation/convert-model-to-ir.html)
- [NNCF](https://github.com/openvinotoolkit/nncf)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
