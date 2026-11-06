# TensorRT

输入：ONNX。输出：`.engine`。需要 NVIDIA 账号下载 SDK 和 NVIDIA GPU，这里都没有。C++ 代码用官方头文件和一个 CUDA 占位头做过语法检查，没有链接，也没有运行，状态 SOURCE_ONLY。

项目：[examples/09_tensorrt_cpp](../../examples/09_tensorrt_cpp)

## 官方资料

- [文档](https://docs.nvidia.com/deeplearning/tensorrt/latest/)
- [官方仓库](https://github.com/NVIDIA/TensorRT)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
