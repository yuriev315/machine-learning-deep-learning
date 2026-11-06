# Paddle Lite 与 Paddle2ONNX

`paddle_lite_opt` 把 Paddle 模型转成 `.nb`，已验证，输入必须是旧版 `.pdmodel`。Paddle2ONNX 2.0.1 把 PIR 模型转成 ONNX，已验证；缺 onnxoptimizer 只会跳过优化。

项目：[examples/04_paddle_lite](../../examples/04_paddle_lite)

## 官方资料

- [Paddle Lite](https://github.com/PaddlePaddle/Paddle-Lite)
- [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
