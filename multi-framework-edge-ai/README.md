# 多框架深度学习训练、转换与边缘部署知识库

从训练到设备推理的工程资源库：DATA → 训练 → 检查点 → 导出 → 转换 → 优化 → 量化 → 硬件编译 → C/C++ 推理 → 性能验证。

所有路线都用同一个小模型和同一个测试集（UCI digits，450 张图），所以结果可以比较，也能发现转换悄悄出错的情况。

**先看 [最终报告](docs/FINAL_REPORT_cn.md)。** 重要限制：没有实体设备，`DEVICE_DEPLOYMENT_VERIFIED` 为 0 项。ARM、MCU、Android、摄像头和 GPU 路径的结果都来自模拟，能证明模型和程序是对的，不能证明真实硬件的速度或 NPU 行为。

## 目录

| 目录 | 内容 |
|---|---|
| [docs/](docs/) | 最终报告、环境说明 |
| [manifests/](manifests/) | 全部矩阵、版本清单、校验和、实测结果 |
| [examples/](examples/) | 可运行项目、C++ 源码、转换产物（`artifacts/`） |
| [framework/](framework/)、[formats/](formats/)、[conversion/](conversion/)、[runtimes/](runtimes/)、[hardware/](hardware/) | 按维度组织的说明和官方链接 |
| [scripts/](scripts/) | 环境重建、下载校验、编译、清单生成 |
| [placeholders/](placeholders/) | 超过 100 MiB 或需要登录的资源的 `.url` 占位 |
| third_party/official_examples/ | 精简的官方示例，提交号见 [official_examples.csv](manifests/official_examples.csv) |

## 项目

| # | 项目 | 目录 | 状态 |
|---|---|---|---|
| 01 | PyTorch 训练 → 导出 → 推理 | [01_pytorch](examples/01_pytorch) | 已运行 |
| 02 | TF、Keras 训练 → 转换 | [02_tensorflow_keras](examples/02_tensorflow_keras) | 已运行（TF 2.19） |
| 03 | JAX、Flax → StableHLO → IREE | [03_jax_flax](examples/03_jax_flax) | 已运行 |
| 04 | Paddle → Paddle Lite | [04_paddle_lite](examples/04_paddle_lite) | 训练已运行；`.nb` 在 QEMU ARM64 运行 |
| 04b | MindSpore → Lite | [04b_mindspore_lite](examples/04b_mindspore_lite) | 已运行（MindSpore 2.7.2） |
| 05 | MXNet 历史模型 | [05_mxnet_legacy](examples/05_mxnet_legacy) | 已运行 |
| 06 | ONNX Runtime C++ | [06_onnxruntime_cpp](examples/06_onnxruntime_cpp) | 已运行 |
| 07 | LiteRT C API | [07_litert_c](examples/07_litert_c) | 已运行 |
| 08 | ExecuTorch C++ | [08_executorch_cpp](examples/08_executorch_cpp) | x86 和 Android 模拟器已运行 |
| 09 | TensorRT C++ | [09_tensorrt_cpp](examples/09_tensorrt_cpp) | **只做过语法检查**，需 SDK 和 GPU |
| 10 | OpenVINO C++ | [10_openvino_cpp](examples/10_openvino_cpp) | 已运行（AMD CPU） |
| 11 | Core ML | [11_coreml_ios](examples/11_coreml_ios) | 转换加独立解释器验证；Swift 未编译 |
| 12 | ncnn | [12_ncnn_arm](examples/12_ncnn_arm) | x86、QEMU、Android 模拟器、软件 Vulkan 已运行 |
| 13 | MNN | [13_mnn_arm](examples/13_mnn_arm) | x86、QEMU、Android 模拟器已运行 |
| 14 | RKNN | [14_rknn_rockchip](examples/14_rknn_rockchip) | 转换、模拟器已运行；C 程序已编译；需硬件 |
| 15 | Qualcomm QNN | [15_qualcomm_qnn](examples/15_qualcomm_qnn) | C++ 已编译；需 SDK 和硬件 |
| 16 | TFLM、CMSIS-NN | [16_tflm_cmsisnn](examples/16_tflm_cmsisnn) | QEMU Cortex-M4、M55 已运行 |
| 17 | 实时摄像头流程 | [17_realtime_camera](examples/17_realtime_camera) | 合成帧和 V4L2 模拟已运行；真实摄像头需硬件 |
| 18 | INT8 量化对比 | [18_int8_comparison](examples/18_int8_comparison) | 已运行 |
| 19 | ARM64 交叉编译 | [19_arm64_cross](examples/19_arm64_cross) | QEMU 已运行 |
| 20 | 运行时打包 | [20_packaging](examples/20_packaging) | chroot 已运行；不算实体设备 |
| 21 | Caffe、Darknet 真实模型 | [21_legacy_caffe_darknet](examples/21_legacy_caffe_darknet) | 已运行 |
| 22 | GGUF LLM | [22_llm_gguf](examples/22_llm_gguf) | 已运行 |
| 23 | 干净设备模拟 | [23_clean_device_vm](examples/23_clean_device_vm) | QEMU 上的 Debian 12 arm64 已运行 |
| 24 | Android 部署 | [24_android_emulator](examples/24_android_emulator) | Android 14 模拟器已运行（x86_64） |

## 依赖下载

Git 仓库不包含 SDK 和 wheel。它们在 [multi-framework-edge-ai-20261106 Release](https://github.com/yuriev315/machine-learning-deep-learning/releases/tag/multi-framework-edge-ai-20261106)，在本目录（`multi-framework-edge-ai/`）下解压。

Android 工具、专有和 GPL 二进制不在 Release 中，用 `python3 scripts/fetch.py` 和 `scripts/setup_tools.sh` 从官方地址下载。复现步骤见[最终报告第 12 节](docs/FINAL_REPORT_cn.md#12-精确复现命令)。

## 许可证

本仓库自己写的脚本和示例代码按 MIT 发布。第三方代码、模型和 SDK 保留各自的许可证，见 `manifests/essential_resources.csv` 和各目录中的 LICENSE。
