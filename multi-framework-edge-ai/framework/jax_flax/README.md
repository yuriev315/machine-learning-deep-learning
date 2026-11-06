# JAX / Flax

- **维护状态：** 活跃维护
- **使用版本：** JAX 0.6.2，Flax 0.10.7，Orbax 0.11.16
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/03_jax_flax](../../examples/03_jax_flax)

训练 → Orbax → `jax.export` → StableHLO → IREE VMFB → IREE C API。ARM64 和 RISC-V 的 VMFB 只验证了编译，没有运行。

## 官方资料

- [JAX 安装](https://docs.jax.dev/en/latest/installation.html)
- [jax.export](https://docs.jax.dev/en/latest/jax.export.html)
- [Flax](https://flax.readthedocs.io/)
- [Orbax](https://orbax.readthedocs.io/)
- [StableHLO](https://openxla.org/stablehlo)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
