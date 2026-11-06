# Darknet

- **维护状态：** pjreddie 版 2022 年后停滞；AlexeyAB 版更新缓慢；hank-ai 分支活跃
- **使用版本：** AlexeyAB master 快照（记录了压缩包哈希，不是固定 tag）
- **验证状态：** RUNNABLE_VERIFIED
- **项目：** [examples/21_legacy_caffe_darknet](../../examples/21_legacy_caffe_darknet)

源码编译成功（CPU）。官方 YOLOv4-tiny 在 dog.jpg 上检出 dog、truck、bicycle、car；转 ncnn 后检出 truck、dog、bicycle，与 OpenCV 参考结果一致。没有训练。

## 官方资料

- [AlexeyAB](https://github.com/AlexeyAB/darknet)
- [pjreddie](https://github.com/pjreddie/darknet)
- [hank-ai](https://github.com/hank-ai/darknet)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
