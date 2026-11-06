# Apache MXNet

- **维护状态：** **已退役**：仓库已归档，项目移入 Apache Attic，不再维护
- **使用版本：** 1.9.1（最后的正式版本线，Python 3.7，单独的旧环境）
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/05_mxnet_legacy](../../examples/05_mxnet_legacy)

训练 → Symbol JSON + params → 重新加载 → ONNX 和 ncnn。依赖旧版 NumPy 和 Python，不会再有安全更新，只应用于历史模型迁移，不要加载不受信任的模型。

## 官方资料

- [Apache Attic](https://attic.apache.org/projects/mxnet.html)
- [归档仓库](https://github.com/apache/mxnet)
- [PyPI](https://pypi.org/project/mxnet/)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
