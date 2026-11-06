# Caffe

- **维护状态：** **基本停止维护**：BVLC/caffe 最后提交 2020-02（未正式归档）
- **使用版本：** 未安装；只处理模型文件
- **验证状态：** CONVERSION_VERIFIED
- **项目：** [examples/21_legacy_caffe_darknet](../../examples/21_legacy_caffe_darknet)

官方 SqueezeNet 1.1 经 `caffe2ncnn` 转成 ncnn，与 OpenCV DNN 加载原始模型的结果对比：Top-5 完全相同。没有编译 Caffe，也没有用它训练。

## 官方资料

- [仓库](https://github.com/BVLC/caffe)
- [SqueezeNet](https://github.com/forresti/SqueezeNet)
- [ncnn 转换说明](https://github.com/Tencent/ncnn/wiki)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
