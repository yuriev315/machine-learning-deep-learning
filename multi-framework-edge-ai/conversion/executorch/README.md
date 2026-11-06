# ExecuTorch

输入：`torch.export`。输出：`.pte`。版本 0.6.0，配套 torch 2.7。XNNPACK 后端，FP32 和 PT2E INT8 都已验证。编译时会自动下载 buck2 生成源文件列表。默认线程池的线程数等于核心数，在容器或 CPU 配额下会严重限流，要用 `_unsafe_reset_threadpool` 固定线程数。

项目：[examples/08_executorch_cpp](../../examples/08_executorch_cpp)

## 官方资料

- [文档](https://pytorch.org/executorch/)
- [仓库](https://github.com/pytorch/executorch)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
