# PyTorch

- **维护状态：** 活跃维护
- **使用版本：** 2.7.1+cpu（独立安装，哈希已对照官方索引）
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/01_pytorch](../../examples/01_pytorch)

训练 → `.pth` → TorchScript / `.pt2` / ONNX。C++ 推理走 ONNX Runtime、ExecuTorch、ncnn、MNN、OpenVINO 或 MindSpore Lite。量化做了 FX QAT 和 PT2E INT8。

## 官方资料

- [安装](https://pytorch.org/get-started/locally/)
- [序列化](https://pytorch.org/docs/stable/notes/serialization.html)
- [torch.export](https://pytorch.org/docs/stable/export.html)
- [ONNX 导出](https://pytorch.org/docs/stable/onnx.html)
- [LibTorch C++](https://pytorch.org/cppdocs/)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
