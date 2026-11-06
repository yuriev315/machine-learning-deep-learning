# Core ML

输入：TorchScript。输出：`.mlpackage`。Linux 上没有 Core ML 运行时，所以用一个独立的 MIL 解释器执行转换后的图和权重，准确率与原模型一致。这验证了转换结果，**不代表 Core ML 或 Neural Engine 的行为**。Swift 代码未编译。

项目：[examples/11_coreml_ios](../../examples/11_coreml_ios)

## 官方资料

- [文档](https://apple.github.io/coremltools/docs-guides/)
- [优化](https://apple.github.io/coremltools/docs-guides/source/opt-overview.html)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
