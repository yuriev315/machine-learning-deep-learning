# ncnn

`onnx2ncnn`、`pnnx`、`caffe2ncnn`、`darknet2ncnn`、`mxnet2ncnn` 都已验证。工具依赖 `libprotobuf.so.32`，这里解压到本地提供。注意 `ncnn::Mat` 必须是三维输入（w, h, c），写错不会报错，但准确率会掉到 10%。

项目：[examples/12_ncnn_arm](../../examples/12_ncnn_arm)

## 官方资料

- [仓库](https://github.com/Tencent/ncnn)
- [pnnx](https://github.com/pnnx/pnnx)

状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。
