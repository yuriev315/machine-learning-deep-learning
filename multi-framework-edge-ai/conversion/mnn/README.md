# MNN

`mnnconvert` 的 ONNX、TFLite 输入和权重 INT8 都已验证。来自 TF 的模型保持 NHWC，来自 ONNX 的是 NCHW，代码要读模型的布局，不能写死。

项目：[examples/13_mnn_arm](../../examples/13_mnn_arm)

## 官方资料

- [仓库](https://github.com/alibaba/MNN)
- [文档](https://mnn-docs.readthedocs.io/)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
