# MindSpore

- **维护状态：** 活跃维护
- **使用版本：** MindSpore 2.7.2；MindSpore Lite 2.6.0
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/04b_mindspore_lite](../../examples/04b_mindspore_lite)

训练 → `.ckpt` → MINDIR 和 ONNX → `.ms` → C++，两条路都可用。PyPI 上没有 2.6.0，2.7.2 是最早支持 Python 3.12 的正式版；2.7 的 Lite 压缩包返回 403，所以 Lite 仍是 2.6.0，相差一个小版本。

## 官方资料

- [安装](https://www.mindspore.cn/install/en)
- [MindSpore Lite](https://www.mindspore.cn/lite/en)
- [源码](https://github.com/mindspore-ai/mindspore)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
