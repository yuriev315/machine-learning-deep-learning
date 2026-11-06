# IREE

StableHLO → VMFB。x86-64 运行正常；aarch64、riscv64 只验证了编译。riscv64 必须指定 lp64d ABI。iree-dist 3.5.0 缺运行时头文件，要从同版本源码补齐。

项目：[examples/03_jax_flax](../../examples/03_jax_flax)

## 官方资料

- [文档](https://iree.dev/)
- [仓库](https://github.com/iree-org/iree)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
