# 多框架深度学习训练、转换与边缘部署：最终报告

日期：2026-11-05。生成方式：`scripts/gen_report.py`，所有测量数字都直接取自实际运行写入的 CSV。

## 结论

- 从训练到 C/C++ 推理的完整流程，已在本机 x86-64 CPU 上跑通，覆盖 PyTorch、TensorFlow/Keras、JAX/Flax、Paddle、MindSpore 和 MXNet。
- 没有硬件的部分都尽量用模拟补上：ARM64（含干净的 Debian 系统）、ARM32、Cortex-M4、Cortex-M55、Android 14（x86_64 模拟器）、V4L2 摄像头、软件 Vulkan、Core ML 图解释、RKNN 模拟器。
- **实体设备部署测试仍为 0 项。** 模拟不算设备部署，所以 `DEVICE_DEPLOYMENT_VERIFIED` 没有授予任何路线。模拟能证明模型、程序和部署包是对的，但**不能证明真实硬件上的速度、功耗、NPU 或 GPU 行为**。
- 无法模拟、仍然没有跑通的：TensorRT、Qualcomm QNN、Hailo、STM32Cube.AI、Ascend（缺 SDK 或硬件），以及真实的 Neural Engine、NPU 和 GPU。

## 这一版的主要变化

- 经你批准放宽 100 MiB 下载限制后，TensorFlow 从 2.0.4 升到 2.19.0，MindSpore 从 1.0.0 升到 2.7.2（PyPI 没有 2.6，2.7.2 是最早支持 Python 3.12 的正式版），Paddle 3.0.0 第一次能本地训练。
- torch 2.7.1 改为独立安装，不再依赖本机其他项目。
- 旧环境只留给 MXNet 和 Paddle Lite 的转换工具。
- 单个大于 100 MiB 的 wheel 放在 Release 的 tar 包里，从不进 Git。Android NDK、模拟器和系统镜像的许可证禁止再分发，只留在本机。

## 1. 覆盖的框架

| 框架 | 维护状态 | 使用版本 | 训练 | 项目 |
|---|---|---|---|---|
| PyTorch | Active | 2.7.1+cpu | RUNNABLE_VERIFIED | examples/01_pytorch |
| TensorFlow | Active | 2.19.0 | RUNNABLE_VERIFIED | examples/02_tensorflow_keras |
| Keras | Active | 3.10.0 | RUNNABLE_VERIFIED | examples/02_tensorflow_keras, examples/03_jax_flax |
| JAX/Flax | Active | 0.6.2 / 0.10.7 | RUNNABLE_VERIFIED | examples/03_jax_flax |
| PaddlePaddle | Active; Paddle Lite low activity, last commit 2025-05 | 3.0.0 / Lite 2.12 | RUNNABLE_VERIFIED | examples/04_paddle_lite |
| MindSpore | Active | 2.7.2 / Lite 2.6.0 | RUNNABLE_VERIFIED | examples/04b_mindspore_lite |
| Apache MXNet | Retired: repo archived, moved to the Apache Attic | 1.9.1 | RUNNABLE_VERIFIED | examples/05_mxnet_legacy |
| Caffe | Unmaintained: BVLC/caffe last commit 2020-02, not formally archived | Not installed | NOT_TESTED | examples/21_legacy_caffe_darknet |
| Darknet | pjreddie stale since 2022; AlexeyAB slow; hank-ai fork active | AlexeyAB master snapshot | NOT_TESTED | examples/21_legacy_caffe_darknet |
| tinygrad, Burn, others | Not evaluated |  | NOT_TESTED |  |

维护状态依据 GitHub API 在当天查询的结果，见 `manifests/maintenance_status.csv`。

## 2. 覆盖的模型格式

共 36 种，见 `manifests/model_format_matrix.csv`。

| 格式 | 类别 | 能否跨设备 | 本机状态 |
|---|---|---|---|
| PyTorch checkpoint | framework | Needs PyTorch and the Python class | RUNNABLE_VERIFIED |
| TorchScript | framework | Where LibTorch runs | RUNNABLE_VERIFIED |
| ExportedProgram | framework | No, an intermediate | CONVERSION_VERIFIED |
| SavedModel | framework | Needs TF or a converter | CONVERSION_VERIFIED |
| GraphDef (frozen) | framework | Legacy | CONVERSION_VERIFIED |
| Keras | framework | Needs Keras | RUNNABLE_VERIFIED |
| ONNX | interchange | Interchange: operators vary by runtime | RUNNABLE_VERIFIED |
| Orbax checkpoint | framework | No | RUNNABLE_VERIFIED |
| StableHLO | interchange | Compiler input, not a deployable | CONVERSION_VERIFIED |
| Paddle inference model | framework | No | CONVERSION_VERIFIED |
| MindIR | framework | No: 1.0 to 2.6 failed | UNSUPPORTED |
| Caffe | legacy | No | CONVERSION_VERIFIED |
| MXNet | legacy | No | RUNNABLE_VERIFIED |
| Darknet | legacy | No | CONVERSION_VERIFIED |
| LiteRT / TFLite | mobile | CPU-portable; delegates vary | RUNNABLE_VERIFIED |
| ExecuTorch | mobile | No: tied to lowering choices | RUNNABLE_VERIFIED |
| Core ML | mobile | Apple only | CONVERSION_VERIFIED |
| Core ML legacy | mobile | Apple only | NOT_TESTED |
| ncnn | mobile | All ncnn targets | RUNNABLE_VERIFIED |
| MNN | mobile | All MNN targets | RUNNABLE_VERIFIED |
| TNN | mobile | TNN targets | NOT_TESTED |
| MindSpore Lite | mobile | Lite targets | RUNNABLE_VERIFIED |
| Paddle Lite | embedded | No: the .nb here targets ARM | RUNNABLE_VERIFIED |
| TensorRT | gpu | No | SDK_REQUIRED |
| OpenVINO IR | gpu | Across OpenVINO devices | RUNNABLE_VERIFIED |
| QNN / SNPE | npu | No | SDK_REQUIRED |
| RKNN | npu | No: RK3588 target here | CONVERSION_VERIFIED |
| Hailo | npu | No | SDK_REQUIRED |
| Edge TPU | npu | Coral only | CONVERSION_VERIFIED |
| Ascend | npu | No | SDK_REQUIRED |
| Micro C array | embedded | MCU-portable with TFLM | RUNNABLE_VERIFIED |
| CMSIS-NN C model | embedded | Arm Cortex-M | RUNNABLE_VERIFIED |
| TVM module | embedded | No: tied to target | RUNNABLE_VERIFIED |
| IREE | embedded | No: tied to compile target | RUNNABLE_VERIFIED |
| GGUF | llm | Across ggml runtimes; LLM-focused | RUNNABLE_VERIFIED |
| ggml whisper | audio | Across whisper.cpp targets | RUNNABLE_VERIFIED |

GGUF 单独归为 LLM 类，不是通用交换格式。ONNX 也不是必经之路：ExecuTorch、Core ML、LiteRT、IREE 路线都没有经过它。

## 3. 转换工具链

- **已实际运行：** torch.onnx、torch.export、ExecuTorch 0.6.0、coremltools 9.0、TF 2.19 TFLiteConverter、tf2onnx、Paddle2ONNX、ovc 与 NNCF、onnx2ncnn、pnnx、caffe2ncnn、darknet2ncnn、mxnet2ncnn、mnnconvert、converter_lite、paddle_lite_opt、rknn-toolkit2 2.3.2、edgetpu_compiler 16.0、iree-compile 3.5.0、TVM 0.25.0.post1。
- **没有运行：** trtexec、QAIRT（直链返回 403）、Hailo DFC、X-CUBE-AI、CANN ATC（都需要登录或硬件）。

各工具的输入、输出、限制见 `conversion/*/README.md` 和 `manifests/sdk_versions.csv`。

## 4. 硬件目标

| 目标 | 本机测试方式 | 最高状态 | 缺什么 |
|---|---|---|---|
| Ubuntu/Linux x64, AMD CPU | Native on Ryzen 5 3600 | RUNNABLE_VERIFIED | 无 |
| Intel CPU | Not tested | HARDWARE_REQUIRED | Intel machine |
| Windows x64 | Not tested | NOT_TESTED | Windows and MSVC |
| NVIDIA GPU | Source only | HARDWARE_REQUIRED | GPU, CUDA, TensorRT SDK |
| AMD GPU | Vulkan path on software lavapipe only | HARDWARE_REQUIRED | ROCm or Vulkan setup |
| Intel GPU/NPU | Not tested | HARDWARE_REQUIRED | Hardware and drivers |
| ARM64 Linux | QEMU user-mode; clean Debian 12 in QEMU system mode | RUNNABLE_VERIFIED | Real board; real timing |
| ARM32 Linux | QEMU user-mode, static musl | RUNNABLE_VERIFIED | Real board |
| Raspberry Pi | Not tested | HARDWARE_REQUIRED | Board. zig builds target glibc 2.28 |
| NVIDIA Jetson | Source only | HARDWARE_REQUIRED | Board, JetPack |
| Rockchip RK3588 | Toolkit simulator; C app links | CONVERSION_VERIFIED | Board and NPU driver |
| Qualcomm Hexagon | C++ compiles | CPP_BUILD_VERIFIED | QAIRT SDK, Snapdragon device |
| Android | Android 14 x86_64 emulator with KVM; arm64-v8a compile and link | RUNNABLE_VERIFIED | ARM phone; APK flow not built |
| iOS, iPadOS, Apple Silicon | Conversion on Linux; own MIL interpreter | CONVERSION_VERIFIED | Mac, Xcode, device |
| Arm Cortex-M | QEMU M4 and M55: CMSIS-NN, TFLM on M4 | RUNNABLE_VERIFIED | Real board, cycle counts |
| STM32 | Not tested | SDK_REQUIRED | X-CUBE-AI, board |
| ESP32 | Example collected | SOURCE_ONLY | ESP-IDF, board |
| Google Edge TPU | Compiled the model; all ops mapped | CONVERSION_VERIFIED | Coral device |
| Hailo | Example collected | SDK_REQUIRED | DFC login, device |
| Huawei Ascend | Not tested | SDK_REQUIRED | CANN, Ascend device |


## 5. C/C++ 运行时选项

已运行：ONNX Runtime 1.22.0、LiteRT C API（TF 2.19.0 源码）、OpenVINO 2025.2.0、ncnn 20250503、MNN 3.2.0、MindSpore Lite 2.6.0、ExecuTorch 0.6.0、IREE 3.5.0、TFLite Micro、CMSIS-NN 7.0.0、Paddle Lite 2.12、llama.cpp、whisper.cpp。

已编译但无法运行：RKNN C API（缺 NPU）、ORT QNN EP（缺 SDK 和设备）、ncnn JNI `.so`（没有构建 APK）。

只做过语法检查：TensorRT（用官方头文件和 CUDA 占位头）。从未编译：Swift Core ML。

## 6. 已验证的转换路线

共 63 条。转换成功和设备部署是分开记录的。“无实测行”表示没有写入结果 CSV，要看对应备注。

| ID | 来源 | 转换工具 | 目标格式 | 目标系统 | 硬件 | 运行状态 | 实测准确率 |
|---|---|---|---|---|---|---|---|
| R01a | PyTorch nn.Module / .pth | torch.onnx.export (TorchScript exporter) | ONNX opset 17 | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R01b | PyTorch nn.Module / .pth | torch.onnx.export | ONNX opset 17 | Windows x64 | Intel/AMD CPU | NOT_TESTED | 无实测行 |
| R01c | PyTorch nn.Module / .pth | torch.onnx.export | ONNX opset 17 | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9756 |
| R01d | PyTorch nn.Module | torch.jit.trace | TorchScript | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R01e | PyTorch nn.Module | torch.export | .pt2 ExportedProgram | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | NOT_TESTED | 无实测行 |
| R02a | PyTorch torch.export | ExecuTorch to_edge_transform_and_lower + XNNPACK | .pte | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R02b | PyTorch PT2E INT8 | ExecuTorch XNNPACKQuantizer + XNNPACK | .pte INT8 | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R02c | PyTorch torch.export | ExecuTorch | .pte | Android 14 emulator (KVM) | Android-14-emulator-x86_64-KVM | RUNNABLE_VERIFIED | 0.9756 |
| R02d | PyTorch torch.export | ExecuTorch | .pte | Android | Android phone | HARDWARE_REQUIRED | 无实测行 |
| R04 | PyTorch TorchScript | coremltools | .mlpackage (mlprogram, FP16; INT8 weights) | iOS, iPadOS, macOS | Apple Neural Engine, GPU, CPU | HARDWARE_REQUIRED | 无实测行 |
| R04b | PyTorch TorchScript | coremltools | MIL program in .mlpackage | Ubuntu 26.04 x64 | Independent MIL interpreter on x86-64 (not Core ML) | RUNNABLE_VERIFIED | 0.9756 |
| R05a | TensorFlow tf.keras / .h5 | TFLiteConverter | .tflite FP32 | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R05b | TensorFlow tf.keras / .h5 | TFLiteConverter + representative dataset | .tflite INT8 (uint8 I/O) | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9844 |
| R05c | TensorFlow tf.keras / .h5 | TFLiteConverter | .tflite FP32 | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9867 |
| R05d | TensorFlow tf.keras / .h5 | TFLiteConverter | .tflite INT8 | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9844 |
| R05e | TensorFlow tf.keras | TFLiteConverter | .tflite | Android 14 emulator (KVM) | Android-14-emulator-x86_64-KVM | RUNNABLE_VERIFIED | 0.9867 |
| R06a | TensorFlow tf.function | tf2onnx | ONNX | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R07a | TensorFlow SavedModel | ovc | OpenVINO IR | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R07b | TensorFlow .tflite | ovc | OpenVINO IR | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R07c | PyTorch ONNX | ovc | OpenVINO IR | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R07d | PyTorch OpenVINO IR | NNCF post-training | OpenVINO IR INT8 | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9778 |
| R07e | TensorFlow SavedModel | ovc | OpenVINO IR | Linux, Windows | Intel iGPU, Intel NPU | HARDWARE_REQUIRED | 无实测行 |
| R08a | JAX/Flax jax.export | iree-compile llvm-cpu | StableHLO, then VMFB | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9822 |
| R08b | JAX/Flax StableHLO | iree-compile llvm-cpu | VMFB aarch64 | Linux | ARM64 Linux | HARDWARE_REQUIRED | 无实测行 |
| R08c | JAX/Flax StableHLO | iree-compile llvm-cpu | VMFB riscv64 | Linux | RISC-V Linux | HARDWARE_REQUIRED | 无实测行 |
| R08d | Keras 3 (JAX backend) .keras | jax.export + iree-compile | StableHLO, then VMFB | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9778 |
| R09a | PaddlePaddle __model__ + params | paddle_lite_opt | .nb | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 无实测行 |
| R09b | PaddlePaddle Layer, legacy .pdmodel | paddle.jit.save, paddle_lite_opt | .nb | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9778 |
| R09c | PaddlePaddle PIR .json | paddle2onnx | ONNX | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9778 |
| R09d | PaddlePaddle PIR .json | paddle.jit.save | .json + .pdiparams | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9778 |
| R10a | MindSpore Cell / .ckpt | mindspore.export ONNX, then converter_lite | .ms | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9822 |
| R10b | MindSpore MINDIR | converter_lite | .ms | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9822 |
| R10c | PyTorch ONNX | converter_lite | .ms | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R10d | TensorFlow .tflite | converter_lite | .ms | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R11 | Caffe prototxt + caffemodel | caffe2ncnn | ncnn .param/.bin | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 无实测行 |
| R11b | Darknet cfg + weights | darknet2ncnn | ncnn .param/.bin | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 无实测行 |
| R11c | MXNet Symbol JSON + params | mxnet2ncnn | ncnn .param/.bin | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R11d | MXNet Symbol JSON + params | mx.onnx.export_model | ONNX | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R11e | MindSpore Cell | mindspore.export | ONNX | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9822 |
| R12a | PyTorch ONNX | onnx2ncnn + ncnnoptimize | ncnn .param/.bin | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R12b | PyTorch ONNX | onnx2ncnn + ncnnoptimize | ncnn .param/.bin | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9756 |
| R12c | PyTorch ONNX | onnx2ncnn + ncnnoptimize | ncnn .param/.bin | Linux (user-mode emulation) | qemu-arm-user | RUNNABLE_VERIFIED | 0.9756 |
| R12d | PyTorch TorchScript | pnnx | ncnn .param/.bin | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R12e | PyTorch ONNX | onnx2ncnn | ncnn .param/.bin | Android 14 emulator (KVM) | Android-14-emulator-x86_64-KVM | RUNNABLE_VERIFIED | 0.9756 |
| R13a | PyTorch ONNX | mnnconvert | .mnn | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R13b | PyTorch ONNX | mnnconvert --weightQuantBits 8 | .mnn weight INT8 | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R13c | PyTorch ONNX | mnnconvert | .mnn | Linux (user-mode emulation) | qemu-aarch64-user | RUNNABLE_VERIFIED | 0.9756 |
| R13d | TensorFlow .tflite | mnnconvert | .mnn | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9867 |
| R13e | PyTorch ONNX | mnnconvert | .mnn | Android 14 emulator (KVM) | Android-14-emulator-x86_64-KVM | RUNNABLE_VERIFIED | 0.9756 |
| R14 | PyTorch ONNX | rknn-toolkit2 | .rknn INT8 for RK3588 | Linux | Rockchip RK3588 NPU | HARDWARE_REQUIRED | 0.9756 |
| R16 | TensorFlow .tflite INT8 | edgetpu_compiler | _edgetpu.tflite | Linux | Google Coral Edge TPU | HARDWARE_REQUIRED | 无实测行 |
| R17a | TensorFlow .tflite INT8 | gen_cmsis_model.py + CMSIS-NN | C arrays + kernels | Bare metal | QEMU mps2-an386 Cortex-M4 | RUNNABLE_VERIFIED | 0.9844 |
| R17a2 | TensorFlow .tflite INT8 | gen_cmsis_model.py + CMSIS-NN | C arrays + Helium kernels | Bare metal | QEMU mps3-an547 Cortex-M55 | RUNNABLE_VERIFIED | 0.9844 |
| R17b | TensorFlow .tflite INT8 | C array of .tflite | C++ array | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9844 |
| R17e | TensorFlow .tflite INT8 | C array of .tflite | C++ array + CMSIS-NN kernels | Bare metal | QEMU mps2-an386 Cortex-M4 | RUNNABLE_VERIFIED | 0.9844 |
| R18a | PyTorch ONNX | TVM relax | compiled .so | Ubuntu 26.04 x64 | x86-64 AMD Ryzen 5 3600 CPU | RUNNABLE_VERIFIED | 0.9756 |
| R21 | PyTorch ONNX | n/a | ONNX + runtime tarball | Isolated chroot, no network, empty env | isolated chroot on x86-64 host | RUNNABLE_VERIFIED | 0.9756 |
| R22 | PyTorch ONNX | n/a | ONNX | Linux | USB/CSI camera | HARDWARE_REQUIRED | 无实测行 |
| R23a | PyTorch ONNX | n/a | ONNX | Clean Debian 12 arm64 in QEMU | QEMU virt Cortex-A76, clean Debian 12 | RUNNABLE_VERIFIED | 0.9756 |
| R23b | PyTorch ONNX | onnx2ncnn | ncnn | Clean Debian 12 arm64 in QEMU | QEMU virt Cortex-A76, clean Debian 12 | RUNNABLE_VERIFIED | 0.9756 |
| R23c | PyTorch ONNX | mnnconvert | .mnn | Clean Debian 12 arm64 in QEMU | QEMU virt Cortex-A76, clean Debian 12 | RUNNABLE_VERIFIED | 0.9756 |
| R24 | PyTorch ONNX | onnx2ncnn | ncnn | Ubuntu 26.04 x64 | Mesa lavapipe software Vulkan on x86-64 | RUNNABLE_VERIFIED | 0.9756 |
| R25 | PyTorch ONNX | torch.onnx.export | ONNX | Android 14 emulator (KVM) | Android-14-emulator-x86_64-KVM | RUNNABLE_VERIFIED | 0.9756 |

第 6 节要求的 18 条研究路线，全部有记录（包括失败和未测试的），见 `manifests/conversion_compatibility_matrix.csv` 和 `manifests/unsupported_conversion_routes.csv`。

## 7. 编译成功的 C/C++ 项目

全部使用同一个测试集（UCI digits，450 张 8x8 图，真实数据但模型很小）。x86-64 真机，单线程。

| 路线 | 准确率 | 平均延迟 µs | P95 µs | 峰值内存 KB | 模型字节 |
|---|---|---|---|---|---|
| jax_stablehlo_iree_c_api | 0.9822 | 7.43 | 7.45 | 4396 | 27901 |
| mindspore_mindir_lite_cpp | 0.9822 | 8.38 | 10.34 | 12644 | 10304 |
| mindspore_onnx_lite_cpp | 0.9822 | 9.45 | 11.07 | 12528 | 10032 |
| mindspore_onnx_ort_cpp | 0.9822 | 9.9 | 6.47 | 22264 | 8442 |
| mxnet_ncnn_cpp | 0.9756 | 13.02 | 17.83 | 6728 | 7604 |
| mxnet_onnx_ort_cpp | 0.9756 | 11.33 | 11.51 | 22608 | 8925 |
| paddle_onnx_ort_cpp | 0.9778 | 10.24 | 11.64 | 22676 | 10666 |
| pytorch_executorch_xnnpack_cpp | 0.9756 | 3.87 | 4.94 | 5200 | 12584 |
| pytorch_executorch_xnnpack_int8_cpp | 0.9756 | 4.96 | 6.56 | 5344 | 8232 |
| pytorch_onnx_mindspore_lite_cpp | 0.9756 | 10.26 | 12.85 | 12800 | 10160 |
| pytorch_onnx_mnn_cpp | 0.9756 | 4.16 | 4.09 | 6920 | 10900 |
| pytorch_onnx_mnn_weightq8_cpp | 0.9756 | 4.12 | 4.09 | 7164 | 6584 |
| pytorch_onnx_ncnn_cpp | 0.9756 | 16.68 | 15.7 | 6680 | 7604 |
| pytorch_onnx_openvino_cpp | 0.9756 | 33.39 | 19.9 | 42592 | 3812 |
| pytorch_onnx_openvino_nncf_int8_cpp | 0.9778 | 21.54 | 21.85 | 47700 | 2104 |
| pytorch_onnx_ort_cpp | 0.9756 | 7.27 | 6.23 | 21644 | 9157 |
| pytorch_onnx_ort_static_int8_cpp | 0.9778 | 15.81 | 21.2 | 22900 | 9760 |
| pytorch_pnnx_ncnn_cpp | 0.9756 | 15.35 | 20.44 | 6836 | 3876 |
| tf_litert_dynrange_c_api | 0.9867 | 8.52 | 8.65 | 7572 | 6736 |
| tf_litert_float_c_api | 0.9867 | 8.14 | 6.68 | 7104 | 10072 |
| tf_litert_int8_c_api | 0.9844 | 12.09 | 10.95 | 7480 | 5648 |
| tf_savedmodel_openvino_cpp | 0.9867 | 15.67 | 15.05 | 44932 | 3876 |
| tf_tflite_mindspore_lite_cpp | 0.9867 | 9.43 | 10.2 | 12428 | 10064 |
| tf_tflite_mnn_cpp | 0.9867 | 4.88 | 4.8 | 7168 | 11900 |
| tf_tflite_openvino_cpp | 0.9867 | 17.31 | 20.27 | 44884 | 3868 |
| tf_tflm_int8_x86 | 0.9844 | 38.1 | 41.49 | 4156 | 0 |

**如何看这些数字：** 这是在跑着其他在线服务的共享机器上做的单次测量，还有 CPU 配额限制，只能说明“能跑、量级如何”，不是严谨的性能基准。同一路线多次运行差异明显，平均值和 P95 都可能受线程池与调度影响，不要拿个位数或几十微秒的差距下结论。一个实际踩到的坑：ExecuTorch 默认线程池的线程数等于核心数，在 CPU 配额下会被反复限流，同一模型测出过约 41.8 ms；固定为 1 个线程后，三次重复都稳定在约 3.6–4.2 µs。Python 版 ExecuTorch 路线没有固定线程池，其延迟不要参考。不同框架训练出的权重也不同，准确率差异不代表运行时优劣。TFLM 那一行的模型字节是 0，因为模型直接编译进了程序，大小要看 `tinycnn_int8.tflite`。

模拟环境中的运行。这些是真实执行，但硬件是模拟的，延迟没有参考意义，“字节”一列对 MCU 是 Flash 占用：

| 路线 | 执行方式 | 准确率 | 模型或 Flash 字节 |
|---|---|---|---|
| packaged_ort_cpp | isolated chroot on x86-64 host | 0.9756 | 9157 |
| paddle_lite_nb_cpp_a64 | qemu-aarch64-user | 0.9778 | 19062 |
| pytorch_coreml_fp16_mil_interpreter_py | Independent MIL interpreter on x86-64 (not Core ML) | 0.9756 | 4244 |
| pytorch_coreml_int8_mil_interpreter_py | Independent MIL interpreter on x86-64 (not Core ML) | 0.9756 | 4244 |
| pytorch_executorch_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9756 | 12584 |
| pytorch_executorch_int8_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9756 | 8232 |
| pytorch_onnx_mnn_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9756 | 10900 |
| pytorch_onnx_mnn_cpp_a64 | qemu-aarch64-user | 0.9756 | 10900 |
| pytorch_onnx_mnn_cpp_vm | QEMU virt Cortex-A76, clean Debian 12 | 0.9756 | 10900 |
| pytorch_onnx_ncnn_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9756 | 7604 |
| pytorch_onnx_ncnn_cpp_a64 | qemu-aarch64-user | 0.9756 | 7604 |
| pytorch_onnx_ncnn_cpp_arm32 | qemu-arm-user | 0.9756 | 7604 |
| pytorch_onnx_ncnn_cpp_vm | QEMU virt Cortex-A76, clean Debian 12 | 0.9756 | 7604 |
| pytorch_onnx_ncnn_vulkan_lavapipe_cpp | Mesa lavapipe software Vulkan on x86-64 | 0.9756 | 7604 |
| pytorch_onnx_ort_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9756 | 9157 |
| pytorch_onnx_ort_cpp_a64 | qemu-aarch64-user | 0.9756 | 9157 |
| pytorch_onnx_ort_cpp_vm | QEMU virt Cortex-A76, clean Debian 12 | 0.9756 | 9157 |
| pytorch_onnx_rknn_int8_simulator_py | RKNN-Toolkit2 x86 simulator | 0.9756 | 41221 |
| tf_cmsisnn_int8_cortex_m4 | QEMU mps2-an386 Cortex-M4 | 0.9844 | 43532 |
| tf_cmsisnn_int8_cortex_m55_helium | QEMU mps3-an547 Cortex-M55 | 0.9844 | 39472 |
| tf_litert_float_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9867 | 10072 |
| tf_litert_float_c_api_a64 | qemu-aarch64-user | 0.9867 | 10072 |
| tf_litert_int8_android_x86_64 | Android-14-emulator-x86_64-KVM | 0.9844 | 5648 |
| tf_litert_int8_c_api_a64 | qemu-aarch64-user | 0.9844 | 5648 |
| tf_tflm_cmsisnn_int8_cortex_m4 | QEMU mps2-an386 Cortex-M4 | 0.9844 | 95384 |

**MCU 估算（来自 QEMU `-icount`，不是周期数）：**

| 路线 | 估算指令数/次推理 | Flash 字节 | RAM 字节 | 预测与桌面 LiteRT 一致 |
|---|---|---|---|---|
| tf_cmsisnn_int8_cortex_m4 | 450,040 | 43532 | 3072 | 是 |
| tf_cmsisnn_int8_cortex_m55_helium | 44,438 | 39472 | 3072 | 是 |
| tf_tflm_cmsisnn_int8_cortex_m4 | 129,240 | 95384 | 8356 | 是 |

Flash 中有 28800 字节是内置测试图。Cortex-M55 用 Helium 后指令数约为 M4 的 1/10，方向合理，但指令数不等于周期数。TFLM 在 M4 上的估算反而比纯 CMSIS-NN 少约 3 倍，这不合常理；我试过 `memcpy`、优化级别、CMSIS-NN 版本都不是原因，**目前未解释**，所以不要用这些数字比较框架。

**编译器覆盖：** GCC 15、Clang（经 zig 0.14.1）、Android NDK clang、Arm GCC、CMake、Ninja、ARM64 交叉编译、ARM32 静态链接都已验证。MSVC **未测试**。

## 8. 实际设备部署测试

**0 项。** 下面这些是模拟，能发现真实问题，但都不算设备部署：

| 模拟 | 证明了什么 | 不能证明什么 |
|---|---|---|
| QEMU 上的干净 Debian 12 arm64 | 部署包在全新系统上能解包运行，三个运行时准确率一致 | 真实板子的速度和外设 |
| Android 14 模拟器（x86_64，KVM） | NDK 编译、adb 部署、bionic 和 SELinux 下能运行 | ARM 手机、NNAPI、APK 流程 |
| QEMU Cortex-M4、M55 | 裸机代码和 Helium 内核预测正确，内存占用真实 | 周期数、功耗、真实外设 |
| 用户态 V4L2 驱动模拟 | 摄像头采集代码流程正确 | 真实摄像头的时序和驱动差异 |
| lavapipe 软件 Vulkan | ncnn GPU 着色器路径能运行 | 真实 GPU 的速度 |
| 独立 MIL 解释器 | Core ML 转换后的图和权重正确 | Core ML 运行时和 Neural Engine |
| RKNN 工具包模拟器 | INT8 转换后的准确率 | 真实 NPU 的算子支持和速度 |
| 空环境、无网络的 chroot | 运行时打包完整（准确率 0.9756） | 内核和 CPU 都还是本机 |

## 9. 量化与优化

| 运行时 | 变体 | 原始字节 | 转换后字节 | 准确率 | 变化 | 平均 µs | 峰值内存 KB |
|---|---|---|---|---|---|---|---|
| LiteRT C API | tf_litert_float_c_api | 10072 | 10072 | 0.9867 | +0.0000 | 8.14 | 7104 |
| LiteRT C API | tf_litert_dynrange_c_api | 10072 | 6736 | 0.9867 | +0.0000 | 8.52 | 7572 |
| LiteRT C API | tf_litert_int8_c_api | 10072 | 5648 | 0.9844 | -0.0023 | 12.09 | 7480 |
| ONNX Runtime Python | ort_fp32 | 9157 | 9157 | 0.9756 | +0.0000 | 16.57 | 280644 |
| ONNX Runtime Python | ort_fp32_graph_optimized | 9157 | 9624 | 0.9756 | +0.0000 | 11.58 | 285136 |
| ONNX Runtime Python | ort_fp16 | 9157 | 6065 | 0.9756 | +0.0000 | 25.4 | 284860 |
| ONNX Runtime Python | ort_dynamic_uint8 | 9157 | 7772 | 0.9756 | +0.0000 | 26.41 | 281088 |
| ONNX Runtime Python | ort_static_int8_pertensor | 9157 | 9251 | 0.9778 | +0.0022 | 20.7 | 284860 |
| ONNX Runtime Python | ort_static_int8_perchannel | 9157 | 9760 | 0.9778 | +0.0022 | 17.77 | 284860 |
| ONNX Runtime Python | ort_static_weights_int4 | 9157 | 9112 | 0.9778 | +0.0022 | 25.13 | 285136 |
| ExecuTorch C++ | pytorch_executorch_xnnpack_cpp | 12584 | 12584 | 0.9756 | +0.0000 | 3.87 | 5200 |
| ExecuTorch C++ | pytorch_executorch_xnnpack_int8_cpp | 12584 | 8232 | 0.9756 | +0.0000 | 4.96 | 5344 |
| OpenVINO Python | openvino_fp32 | 3812 | 3812 | 0.9756 | +0.0000 | 82.43 | 999272 |
| OpenVINO Python | openvino_nncf_int8 | 3812 | 2104 | 0.9778 | +0.0022 | 85.84 | 1001532 |
| MNN C++ | pytorch_onnx_mnn_cpp | 10900 | 10900 | 0.9756 | +0.0000 | 4.16 | 6920 |
| MNN C++ | pytorch_onnx_mnn_weightq8_cpp | 10900 | 6584 | 0.9756 | +0.0000 | 4.12 | 7164 |
| PyTorch | pytorch_eager_py | 10517 | 10517 | 0.9756 | +0.0000 | 96.64 | 360492 |
| PyTorch | pytorch_qat_fbgemm_int8 | 10517 | 23728 | 0.9756 | +0.0000 | 63.78 | 1023328 |

全部测量硬件：AMD Ryzen 5 3600，单线程。

- **INT8 在这里并没有普遍更快。** 模型极小，量化节点的开销占比高；这个结果不能推广到大模型或 NPU。
- **小模型的 ONNX QDQ 文件反而比 FP32 大**，因为多出的节点信息超过了省下的权重空间。
- Python 行的峰值内存是整个进程的累计值，主要反映 Python 和框架本身，不是模型占用。
- **已做：** FP32、FP16、INT8、INT4 权重（ORT）、训练后量化、QAT（PyTorch FX）、校准集、逐通道和逐张量、动态和静态量化、图优化（ORT 节点 8 → 7，ncnnoptimize 融合）、内存规划（TFLM arena 2592 字节）、XNNPACK 和 CMSIS-NN 内核选择。
- **未做：** BF16（本机 CPU 不支持 avx512_bf16，这条路线没有运行）、真实 GPU 和 NPU 的加速对比（没有硬件）。

## 10. 缺少的 SDK 和硬件

| 项目 | 完整验证需要 | 本机有无 | 状态 |
|---|---|---|---|
| 08 ExecuTorch on Android | ARM Android phone | x86_64 emulator only | HARDWARE_REQUIRED |
| 09 TensorRT | NVIDIA GPU or Jetson, TensorRT SDK | no | HARDWARE_REQUIRED |
| 10 OpenVINO on Intel GPU/NPU | Intel Core Ultra or similar | no; AMD CPU only | HARDWARE_REQUIRED |
| 11 Core ML | Mac, Xcode, iPhone or iPad | own MIL interpreter only | HARDWARE_REQUIRED |
| 12 ncnn Android | ARM Android phone | x86_64 emulator only | HARDWARE_REQUIRED |
| 13 MNN Android | ARM Android phone | x86_64 emulator only | HARDWARE_REQUIRED |
| 14 RKNN | RK3588 board with NPU driver | no | HARDWARE_REQUIRED |
| 15 QNN | Snapdragon device, QAIRT SDK | no | HARDWARE_REQUIRED |
| 16 MCU | Cortex-M board such as an STM32 Nucleo, for timing and memory | QEMU only | HARDWARE_REQUIRED |
| 17 Camera | UVC USB camera | user-space driver simulation only | HARDWARE_REQUIRED |
| 19 ARM64 | Raspberry Pi or similar, for real latency | QEMU only | HARDWARE_REQUIRED |
| 20, 23 Clean device | A second physical Linux machine | chroot; clean Debian in QEMU | HARDWARE_REQUIRED |

以后如果能提供硬件，优先级建议：RK3588 开发板或树莓派（同时验证 ARM64 真实延迟和干净设备部署）→ Android 手机 → NVIDIA GPU 或 Jetson → STM32 Nucleo。

## 11. 用 URL 占位的资源

这些需要登录、下载地址无法访问，或者这里已从源码编译而不需要，所以没有下载。每个都有 `placeholders/*.url`。

| 名称 | 版本 | 预计大小 | 官方 SHA256 | 用途 |
|---|---|---|---|---|
| mnn-linux-prebuilt | 3.2.0 | 198 MiB | 3e86ac8fc0eb… | MNN prebuilt desktop libs; built from source here  |
| tensorrt-sdk | 10.x | 需登录，未知 | 无 | TensorRT C++ SDK, needs an NVIDIA GPU |
| qairt-sdk | 2.x | 需登录，未知 | 无 | Qualcomm AI Runtime SDK (QNN, SNPE) |
| hailo-dfc | 3.x | 需登录，未知 | 无 | Hailo Dataflow Compiler and HailoRT |
| x-cube-ai | 10.x | 需登录，未知 | 无 | STM32Cube.AI |
| cann-toolkit | 8.x | 需登录，未知 | 无 | Huawei Ascend CANN and ATC compiler |
| xcode | 16+ | 需登录，未知 | 无 | Xcode: Core ML / Swift build and on-device test |


## 12. 精确复现命令

已测试：`scripts/setup_env.sh` 从本地 wheel 重建环境并成功导入主要模块；`scripts/run_all.sh` 在已有 SDK 的情况下完整重跑，结果见 `docs/run_all_summary.txt`。**没有测试：** 在一台全新的机器上从 `git clone` 开始走完全程。

```bash
git clone --depth 1 --branch multi-framework-edge-ai-20261106 https://github.com/yuriev315/machine-learning-deep-learning.git mldl && cd mldl/multi-framework-edge-ai
# 依赖：从 https://github.com/yuriev315/machine-learning-deep-learning/releases/tag/multi-framework-edge-ai-20261106 下载所有 tar，在 multi-framework-edge-ai 目录解压，再用下面的命令补齐 Release 中没有的部分
python3 scripts/fetch.py        # 校验并补齐压缩包；超过 100 MiB 的只写占位，不下载
tar --zstd -xf deps/archives/python37-standalone/*.zst --strip-components=1 --one-top-level=third_party/python37
scripts/setup_env.sh            # 创建 Python 环境，torch 使用 Release 里的 wheel
scripts/setup_tools.sh          # 解压 SDK、创建交叉工具和本地库，不改动系统
source scripts/env.sh
scripts/build_sdks.sh && scripts/build_extra.sh && scripts/build_extra.sh et_android && scripts/build_tflm.sh && scripts/build_tflm_m.sh   # 约 1 小时（4 核）
scripts/run_all.sh              # 从数据到全部推理；每步输出 PASS 或 FAIL，日志在 logs/step_*.log
python scripts/gen_manifests.py && python3 scripts/gen_report.py              # 用新结果重新生成清单和本报告
```

单独的转换和运行命令见各项目目录。环境说明见 `docs/ENVIRONMENT.md`。

## 13. 磁盘占用与避免的下载

| 目录 | 大小 | 是否上传 |
|---|---|---|
| .envs/ | 8.7G | 否 |
| deps/ | 5.4G | 部分（Release） |
| third_party/ | 19G | 只传 official_examples |
| build/ | 4.3G | 否 |
| examples/ | 48M | 是（Git） |

- 下载校验：245 个文件通过官方摘要校验；**42 个文件官方没有公布摘要，只有本地哈希，属于未验证**（主要是较老的 GitHub Release 和直链），明细见 `manifests/download_status.csv`。
- 整个过程没有用 apt 往系统安装任何东西，全部工具都在项目目录内。编译和模拟都通过 cgroup 限制了 CPU 和内存。
- `third_party/_build/`、`build/` 可以删除后重新生成，见 `manifests/cleanup_candidates.csv`。

**上传说明：** 仓库是公开的。以下内容已下载到本地，但没有放进公开仓库或 Release：Android NDK、模拟器和系统镜像（许可证禁止再分发）、Rockchip 专有运行库和工具包（许可证没有明确允许再分发）、Edge TPU 编译器、GPL 二进制（QEMU、GCC 交叉工具链、Arm GCC），以及 Debian 镜像和 Mesa 包。它们的下载地址和哈希在清单里，可用 `scripts/fetch.py` 和 `scripts/setup_tools.sh` 重新获取。

## 14. 维护状态与兼容性风险

- **已归档或退役：** MXNet（已移入 Attic）、google-coral/edgetpu（仓库已归档）。
- **基本停滞：** Caffe（2020 年后无提交）、pjreddie/darknet、Paddle Lite（最后提交 2025-05）、Tencent/TNN（2025-03）。
- **安全风险：** `legacy37` 环境里的 MXNet 1.9.1、Paddle Lite 2.12 工具和 Python 3.7 都已停止维护，有已知漏洞。只能用于处理可信模型，不要接入生产环境。
- **框架不能混用：** TF、Paddle、MindSpore 在同一进程导入会因 protobuf 冲突而段错误，每个进程只用一个框架。
- **版本未完全对齐：** MindSpore 2.7.2 配 Lite 2.6.0，测试通过，但不是官方配对。
- **依赖版本声明与实际不符：** executorch 0.6.0 要求 torch==2.7.0，这里用 2.7.1；rknn-toolkit2 2.3.2 的声明要求旧版 torch，这里用 `--no-deps` 安装，转换和模拟器能跑，但未经官方支持。
- **版本绑定：** apache-tvm 0.25 必须配 ffi 0.1.12。MindIR 1.0 不能转 Lite 2.6。`.engine`、`.rknn`、`.hef`、`_edgetpu.tflite` 都绑定具体芯片或版本。
- **环境差异：** GCC 15 交叉编译的程序需要目标设备 glibc ≥ 2.43，大多数现有设备不满足；要部署到真实设备时，应该用 zig 工具链（面向 glibc 2.28），或用设备自己的 SDK 重新编译。
- **未固定版本：** Darknet 用的是 master 分支快照。部分官方示例也跟踪主分支，提交号记录在 `manifests/official_examples.csv`。
