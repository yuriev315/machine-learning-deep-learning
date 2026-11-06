# PaddlePaddle

- **维护状态：** Paddle 活跃；Paddle Lite 活跃度低（最后提交 2025-05）
- **使用版本：** Paddle 3.0.0；Paddle Lite 2.12；Paddle2ONNX 2.0.1
- **验证状态：** RUNNABLE_VERIFIED（ARM 为 QEMU 模拟）
- **项目：** [examples/04_paddle_lite](../../examples/04_paddle_lite)

本地训练 → `.pdparams` → 推理模型 → Paddle Inference、ONNX 和 `.nb`。Lite 2.12 读不了 Paddle 3 默认的 PIR `.json`，导出时要设 `FLAGS_enable_pir_api=0` 生成旧版 `.pdmodel`。`.nb` 在 QEMU ARM64 上用 C++ 运行，准确率与训练一致。

## 官方资料

- [安装](https://www.paddlepaddle.org.cn/install/quick)
- [Paddle Lite](https://github.com/PaddlePaddle/Paddle-Lite)
- [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
