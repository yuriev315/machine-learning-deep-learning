#!/usr/bin/env python3
"""Writes a README into each knowledge-base directory. Official links live here and are checked by scripts/check_urls.py."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON = "状态词含义见 [docs/ENVIRONMENT.md](../../docs/ENVIRONMENT.md)，路线和实测数据见 [conversion_compatibility_matrix.csv](../../manifests/conversion_compatibility_matrix.csv)。\n"


def links(pairs):
    return "\n".join(f"- [{t}]({u})" for t, u in pairs) + "\n"


FRAMEWORKS = {
 "pytorch": ("PyTorch", "活跃维护", "2.7.1+cpu（独立安装，哈希已对照官方索引）", "RUNNABLE_VERIFIED", "[examples/01_pytorch](../../examples/01_pytorch)",
   "训练 → `.pth` → TorchScript / `.pt2` / ONNX。C++ 推理走 ONNX Runtime、ExecuTorch、ncnn、MNN、OpenVINO 或 MindSpore Lite。量化做了 FX QAT 和 PT2E INT8。",
   [("安装", "https://pytorch.org/get-started/locally/"), ("序列化", "https://pytorch.org/docs/stable/notes/serialization.html"), ("torch.export", "https://pytorch.org/docs/stable/export.html"), ("ONNX 导出", "https://pytorch.org/docs/stable/onnx.html"), ("LibTorch C++", "https://pytorch.org/cppdocs/")]),
 "tensorflow_keras": ("TensorFlow / Keras", "活跃维护", "TensorFlow 2.19.0，Keras 3.10.0", "RUNNABLE_VERIFIED", "[examples/02_tensorflow_keras](../../examples/02_tensorflow_keras)",
   "训练 → `.keras` / `.h5` / SavedModel / 冻结 GraphDef / `.tflite`（FP32、动态范围、全整数 INT8）/ ONNX（tf2onnx）。新版转换器会给全连接层用逐通道量化，手写 CMSIS-NN 调用时要用 `arm_fully_connected_per_channel_s8`。TF、Paddle、MindSpore 不能在同一进程导入，protobuf 会冲突。",
   [("TF 安装", "https://www.tensorflow.org/install"), ("SavedModel", "https://www.tensorflow.org/guide/saved_model"), ("Keras 保存", "https://keras.io/guides/serialization_and_saving/"), ("LiteRT 转换", "https://ai.google.dev/edge/litert/models/convert")]),
 "jax_flax": ("JAX / Flax", "活跃维护", "JAX 0.6.2，Flax 0.10.7，Orbax 0.11.16", "RUNNABLE_VERIFIED", "[examples/03_jax_flax](../../examples/03_jax_flax)",
   "训练 → Orbax → `jax.export` → StableHLO → IREE VMFB → IREE C API。ARM64 和 RISC-V 的 VMFB 只验证了编译，没有运行。",
   [("JAX 安装", "https://docs.jax.dev/en/latest/installation.html"), ("jax.export", "https://docs.jax.dev/en/latest/jax.export.html"), ("Flax", "https://flax.readthedocs.io/"), ("Orbax", "https://orbax.readthedocs.io/"), ("StableHLO", "https://openxla.org/stablehlo")]),
 "paddlepaddle": ("PaddlePaddle", "Paddle 活跃；Paddle Lite 活跃度低（最后提交 2025-05）", "Paddle 3.0.0；Paddle Lite 2.12；Paddle2ONNX 2.0.1", "RUNNABLE_VERIFIED（ARM 为 QEMU 模拟）", "[examples/04_paddle_lite](../../examples/04_paddle_lite)",
   "本地训练 → `.pdparams` → 推理模型 → Paddle Inference、ONNX 和 `.nb`。Lite 2.12 读不了 Paddle 3 默认的 PIR `.json`，导出时要设 `FLAGS_enable_pir_api=0` 生成旧版 `.pdmodel`。`.nb` 在 QEMU ARM64 上用 C++ 运行，准确率与训练一致。",
   [("安装", "https://www.paddlepaddle.org.cn/install/quick"), ("Paddle Lite", "https://github.com/PaddlePaddle/Paddle-Lite"), ("Paddle2ONNX", "https://github.com/PaddlePaddle/Paddle2ONNX")]),
 "mindspore": ("MindSpore", "活跃维护", "MindSpore 2.7.2；MindSpore Lite 2.6.0", "RUNNABLE_VERIFIED", "[examples/04b_mindspore_lite](../../examples/04b_mindspore_lite)",
   "训练 → `.ckpt` → MINDIR 和 ONNX → `.ms` → C++，两条路都可用。PyPI 上没有 2.6.0，2.7.2 是最早支持 Python 3.12 的正式版；2.7 的 Lite 压缩包返回 403，所以 Lite 仍是 2.6.0，相差一个小版本。",
   [("安装", "https://www.mindspore.cn/install/en"), ("MindSpore Lite", "https://www.mindspore.cn/lite/en"), ("源码", "https://github.com/mindspore-ai/mindspore")]),
 "mxnet_legacy": ("Apache MXNet", "**已退役**：仓库已归档，项目移入 Apache Attic，不再维护", "1.9.1（最后的正式版本线，Python 3.7，单独的旧环境）", "RUNNABLE_VERIFIED", "[examples/05_mxnet_legacy](../../examples/05_mxnet_legacy)",
   "训练 → Symbol JSON + params → 重新加载 → ONNX 和 ncnn。依赖旧版 NumPy 和 Python，不会再有安全更新，只应用于历史模型迁移，不要加载不受信任的模型。",
   [("Apache Attic", "https://attic.apache.org/projects/mxnet.html"), ("归档仓库", "https://github.com/apache/mxnet"), ("PyPI", "https://pypi.org/project/mxnet/")]),
 "caffe_legacy": ("Caffe", "**基本停止维护**：BVLC/caffe 最后提交 2020-02（未正式归档）", "未安装；只处理模型文件", "CONVERSION_VERIFIED", "[examples/21_legacy_caffe_darknet](../../examples/21_legacy_caffe_darknet)",
   "官方 SqueezeNet 1.1 经 `caffe2ncnn` 转成 ncnn，与 OpenCV DNN 加载原始模型的结果对比：Top-5 完全相同。没有编译 Caffe，也没有用它训练。",
   [("仓库", "https://github.com/BVLC/caffe"), ("SqueezeNet", "https://github.com/forresti/SqueezeNet"), ("ncnn 转换说明", "https://github.com/Tencent/ncnn/wiki")]),
 "darknet": ("Darknet", "pjreddie 版 2022 年后停滞；AlexeyAB 版更新缓慢；hank-ai 分支活跃", "AlexeyAB master 快照（记录了压缩包哈希，不是固定 tag）", "RUNNABLE_VERIFIED", "[examples/21_legacy_caffe_darknet](../../examples/21_legacy_caffe_darknet)",
   "源码编译成功（CPU）。官方 YOLOv4-tiny 在 dog.jpg 上检出 dog、truck、bicycle、car；转 ncnn 后检出 truck、dog、bicycle，与 OpenCV 参考结果一致。没有训练。",
   [("AlexeyAB", "https://github.com/AlexeyAB/darknet"), ("pjreddie", "https://github.com/pjreddie/darknet"), ("hank-ai", "https://github.com/hank-ai/darknet")]),
}
FORMATS = {
 "interchange": ("交换格式", "ONNX、StableHLO。它们是通往运行时或编译器的中间形式，不是最终产物。ONNX 不是必经之路：Core ML、ExecuTorch、LiteRT 都有自己的直接路线。", [("ONNX", "https://onnx.ai/"), ("StableHLO", "https://openxla.org/stablehlo")]),
 "mobile": ("移动端格式", "`.tflite`、`.pte`、`.mlpackage`、ncnn、`.mnn`、`.ms`、TNN（未测试）。", [("LiteRT", "https://ai.google.dev/edge/litert"), ("ExecuTorch", "https://pytorch.org/executorch/"), ("Core ML Tools", "https://apple.github.io/coremltools/docs-guides/"), ("ncnn", "https://github.com/Tencent/ncnn"), ("MNN", "https://github.com/alibaba/MNN"), ("TNN", "https://github.com/Tencent/TNN")]),
 "gpu": ("GPU 与加速器格式", "TensorRT `.engine` 绑定 TensorRT 版本和 GPU 系列；OpenVINO IR 可跨 OpenVINO 设备。TensorRT 这里没有 SDK 和 GPU，未生成。", [("TensorRT", "https://docs.nvidia.com/deeplearning/tensorrt/latest/"), ("OpenVINO", "https://docs.openvino.ai/")]),
 "npu": ("NPU 格式", "`.rknn`、`_edgetpu.tflite` 已实际编译；`.dlc`、`.hef`、`.om` 需要需登录下载的 SDK。这些产物都绑定具体芯片，不能跨设备使用。", [("RKNN Toolkit2", "https://github.com/airockchip/rknn-toolkit2"), ("Qualcomm AI Engine Direct", "https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk"), ("Hailo", "https://hailo.ai/developer-zone/"), ("Coral 编译器", "https://coral.ai/docs/edgetpu/compiler/"), ("Ascend CANN", "https://www.hiascend.com/software/cann")]),
 "embedded": ("嵌入式格式", "TFLite Micro 的 C 数组、CMSIS-NN 的 C 模型、TVM `.so`、IREE VMFB、Paddle Lite `.nb`。TVM 和 IREE 产物绑定编译目标。", [("TFLite Micro", "https://github.com/tensorflow/tflite-micro"), ("CMSIS-NN", "https://github.com/ARM-software/CMSIS-NN"), ("TVM", "https://tvm.apache.org/docs/"), ("IREE", "https://iree.dev/")]),
 "llm": ("LLM 与专用格式", "GGUF 是 llama.cpp 和 ggml 生态的格式，主要用于 LLM，**不是通用神经网络交换格式**。语音用 whisper.cpp 的 ggml 模型单独验证。", [("llama.cpp", "https://github.com/ggml-org/llama.cpp"), ("GGUF 规范", "https://github.com/ggml-org/ggml/blob/master/docs/gguf.md"), ("whisper.cpp", "https://github.com/ggml-org/whisper.cpp")]),
}
CONVERT = {
 "onnx": ("ONNX 与 ONNX Runtime", "输入：PyTorch、MXNet、MindSpore 等。输出：`.onnx`。运行时 1.22.0，C/C++ API。量化：动态（UInt8）、静态 QDQ（逐张量、逐通道）、FP16、INT4 权重。注意：`ConvInteger` 配 int8 权重在 CPU 上没有实现。", "examples/06_onnxruntime_cpp", [("ORT 文档", "https://onnxruntime.ai/docs/"), ("量化", "https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html"), ("官方示例", "https://github.com/microsoft/onnxruntime-inference-examples")]),
 "litert": ("LiteRT / TensorFlow Lite", "输入：Keras、SavedModel、concrete function。输出：`.tflite`。C API 从 TF 2.19.0 源码编译，x86-64、QEMU ARM64 和 Android 模拟器都已运行。量化：动态范围、全整数 INT8。", "examples/07_litert_c", [("LiteRT", "https://ai.google.dev/edge/litert"), ("CMake 编译", "https://ai.google.dev/edge/litert/build/cmake"), ("训练后量化", "https://ai.google.dev/edge/litert/models/post_training_quantization")]),
 "executorch": ("ExecuTorch", "输入：`torch.export`。输出：`.pte`。版本 0.6.0，配套 torch 2.7。XNNPACK 后端，FP32 和 PT2E INT8 都已验证。编译时会自动下载 buck2 生成源文件列表。默认线程池的线程数等于核心数，在容器或 CPU 配额下会严重限流，要用 `_unsafe_reset_threadpool` 固定线程数。", "examples/08_executorch_cpp", [("文档", "https://pytorch.org/executorch/"), ("仓库", "https://github.com/pytorch/executorch")]),
 "coreml": ("Core ML", "输入：TorchScript。输出：`.mlpackage`。Linux 上没有 Core ML 运行时，所以用一个独立的 MIL 解释器执行转换后的图和权重，准确率与原模型一致。这验证了转换结果，**不代表 Core ML 或 Neural Engine 的行为**。Swift 代码未编译。", "examples/11_coreml_ios", [("文档", "https://apple.github.io/coremltools/docs-guides/"), ("优化", "https://apple.github.io/coremltools/docs-guides/source/opt-overview.html")]),
 "tensorrt": ("TensorRT", "输入：ONNX。输出：`.engine`。需要 NVIDIA 账号下载 SDK 和 NVIDIA GPU，这里都没有。C++ 代码用官方头文件和一个 CUDA 占位头做过语法检查，没有链接，也没有运行，状态 SOURCE_ONLY。", "examples/09_tensorrt_cpp", [("文档", "https://docs.nvidia.com/deeplearning/tensorrt/latest/"), ("官方仓库", "https://github.com/NVIDIA/TensorRT")]),
 "openvino": ("OpenVINO", "输入：ONNX、SavedModel、TFLite，三者都已验证。输出：IR。NNCF INT8 已验证。运行在 AMD CPU 上，没有测试 Intel GPU 或 NPU。", "examples/10_openvino_cpp", [("文档", "https://docs.openvino.ai/"), ("模型转换", "https://docs.openvino.ai/2025/openvino-workflow/model-preparation/convert-model-to-ir.html"), ("NNCF", "https://github.com/openvinotoolkit/nncf")]),
 "paddle_lite": ("Paddle Lite 与 Paddle2ONNX", "`paddle_lite_opt` 把 Paddle 模型转成 `.nb`，已验证，输入必须是旧版 `.pdmodel`。Paddle2ONNX 2.0.1 把 PIR 模型转成 ONNX，已验证；缺 onnxoptimizer 只会跳过优化。", "examples/04_paddle_lite", [("Paddle Lite", "https://github.com/PaddlePaddle/Paddle-Lite"), ("Paddle2ONNX", "https://github.com/PaddlePaddle/Paddle2ONNX")]),
 "mindspore_lite": ("MindSpore Lite", "`converter_lite` 的 ONNX、TFLite 和 MINDIR（来自 2.7.2）输入都已验证。旧版 1.0 的 MINDIR 被拒绝。输出 `.ms`，C++ 运行正常。", "examples/04b_mindspore_lite", [("文档", "https://www.mindspore.cn/lite/en")]),
 "ncnn": ("ncnn", "`onnx2ncnn`、`pnnx`、`caffe2ncnn`、`darknet2ncnn`、`mxnet2ncnn` 都已验证。工具依赖 `libprotobuf.so.32`，这里解压到本地提供。注意 `ncnn::Mat` 必须是三维输入（w, h, c），写错不会报错，但准确率会掉到 10%。", "examples/12_ncnn_arm", [("仓库", "https://github.com/Tencent/ncnn"), ("pnnx", "https://github.com/pnnx/pnnx")]),
 "mnn": ("MNN", "`mnnconvert` 的 ONNX、TFLite 输入和权重 INT8 都已验证。来自 TF 的模型保持 NHWC，来自 ONNX 的是 NCHW，代码要读模型的布局，不能写死。", "examples/13_mnn_arm", [("仓库", "https://github.com/alibaba/MNN"), ("文档", "https://mnn-docs.readthedocs.io/")]),
 "tvm": ("Apache TVM", "`apache-tvm` 0.25.0.post1 配 `apache-tvm-ffi` 0.1.12（ffi 版本更新会导致符号缺失）。ONNX → Relax → x86-64 `.so`，Python 运行正常。", "conversion/tvm", [("文档", "https://tvm.apache.org/docs/"), ("仓库", "https://github.com/apache/tvm")]),
 "iree": ("IREE", "StableHLO → VMFB。x86-64 运行正常；aarch64、riscv64 只验证了编译。riscv64 必须指定 lp64d ABI。iree-dist 3.5.0 缺运行时头文件，要从同版本源码补齐。", "examples/03_jax_flax", [("文档", "https://iree.dev/"), ("仓库", "https://github.com/iree-org/iree")]),
 "vendor_compilers": ("厂商编译器", "RKNN Toolkit2 和 Edge TPU compiler 已实际运行。QAIRT、Hailo DFC、X-CUBE-AI、CANN ATC 需要账号，只有 `.url` 占位和官方示例。", "examples/14_rknn_rockchip", [("RKNN Toolkit2", "https://github.com/airockchip/rknn-toolkit2"), ("Edge TPU 编译器", "https://coral.ai/docs/edgetpu/compiler/"), ("QAIRT", "https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk"), ("Hailo", "https://hailo.ai/developer-zone/"), ("X-CUBE-AI", "https://www.st.com/en/embedded-software/x-cube-ai.html"), ("CANN", "https://www.hiascend.com/software/cann")]),
}
RUNTIMES = {
 "python": "Python 运行方式用于转换和快速核对，见各项目的 `train_export.py`。Python 行的峰值内存是整个进程的累计值，不能和 C++ 对比。",
 "cpp": "C++ 项目都用 `examples/common/cpp/digits.h` 统一读取测试集、计时、报告峰值内存。入口：`scripts/build_examples.sh`。",
 "c_api": "C API 项目：[LiteRT](../../examples/07_litert_c)、[IREE](../../examples/03_jax_flax/iree_c)、[RKNN](../../examples/14_rknn_rockchip/c_api)、[CMSIS-NN](../../examples/16_tflm_cmsisnn/cortex_m)、[llama.cpp](../../examples/22_llm_gguf)。",
 "android": "ORT、ncnn、MNN、LiteRT、ExecuTorch 都用 NDK r27d 编译，并在 **Android 14 x86_64 模拟器**（KVM）上用 adb 部署运行，见 [examples/24_android_emulator](../../examples/24_android_emulator)。这是真实的 Android 系统和 bionic，但不是 ARM。arm64-v8a 只验证了编译和链接。**没有手机，也没有构建 APK**，[Gradle 和 JNI 代码](../../examples/12_ncnn_arm/android)里只有 JNI `.so` 编译过。",
 "ios": "iOS 是 **HARDWARE_REQUIRED**：需要 Mac、Xcode 和设备。转换已完成，并用独立的 MIL 解释器验证了图和权重。Swift 代码在 [examples/11_coreml_ios](../../examples/11_coreml_ios) 中，从未编译。",
 "embedded_linux": "ARM64 和 ARM32 用 QEMU 用户态运行，入口是 [examples/19_arm64_cross](../../examples/19_arm64_cross)。此外还在 QEMU 系统模拟的干净 Debian 12 上完整部署过，见 [examples/23_clean_device_vm](../../examples/23_clean_device_vm)。这证明指令集、库和部署包正确，但延迟数字没有参考意义，也不算设备部署。",
 "microcontrollers": "CMSIS-NN 在 QEMU Cortex-M4 和 Cortex-M55（Helium）上、TFLite Micro 在 Cortex-M4 上，都跑完 450 张测试图，预测与桌面 LiteRT 完全一致。入口：[examples/16_tflm_cmsisnn/cortex_m](../../examples/16_tflm_cmsisnn/cortex_m)。QEMU 不精确模拟周期，只有估算的指令数，不是时序数据。",
}
HARDWARE = {
 "x86": ("x86-64", "本机 AMD Ryzen 5 3600 上实际运行了全部 x86 路线。延迟是共享机器上的单次测量。"),
 "arm": ("ARM", "QEMU 用户态（ARM64、ARM32）和 QEMU 系统模拟（Cortex-A76 上的干净 Debian、Cortex-M4、Cortex-M55）。没有实体开发板。"),
 "nvidia": ("NVIDIA", "**HARDWARE_REQUIRED**。本机没有 NVIDIA GPU，也没有 TensorRT SDK。"),
 "intel": ("Intel", "**HARDWARE_REQUIRED**。OpenVINO 实际运行在 AMD CPU 上，这不等于 Intel CPU、iGPU 或 NPU 的结果。"),
 "amd": ("AMD", "只在 AMD CPU 上真机运行。GPU 计算路径只用软件 Vulkan 驱动（lavapipe）跑过 ncnn，不反映真实 GPU。"),
 "qualcomm": ("Qualcomm", "**SDK_REQUIRED + HARDWARE_REQUIRED**。C++ 只验证了编译，见 [examples/15_qualcomm_qnn](../../examples/15_qualcomm_qnn)。"),
 "rockchip": ("Rockchip", "**HARDWARE_REQUIRED**。`.rknn` 已生成，工具包模拟器上的全测试集准确率已测，C 程序已交叉编译。程序启动后报无法打开 NPU 设备，符合预期。"),
 "hailo": ("Hailo", "**SDK_REQUIRED + HARDWARE_REQUIRED**。只收集了官方示例。"),
 "stm32": ("STM32", "**SDK_REQUIRED + HARDWARE_REQUIRED**。X-CUBE-AI 需要登录。TFLM 和 CMSIS-NN 已在 QEMU Cortex-M4 上运行，可以作为起点。"),
 "coral": ("Google Coral", "**HARDWARE_REQUIRED**。Edge TPU 编译通过，7 个算子全部映射到 TPU。编译器仓库已归档，长期可用性有风险。"),
}


def put(path, text):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)


for k, (name, maint, ver, st, proj, body, ln) in FRAMEWORKS.items():
    put(f"framework/{k}/README.md", f"# {name}\n\n- **维护状态：** {maint}\n- **使用版本：** {ver}\n- **验证状态：** {st}\n- **项目：** {proj}\n\n{body}\n\n## 官方资料\n\n{links(ln)}\n{COMMON}")
for k, (name, body, ln) in FORMATS.items():
    put(f"formats/{k}/README.md", f"# {name}\n\n{body}\n\n完整对照见 [model_format_matrix.csv](../../manifests/model_format_matrix.csv)。\n\n## 官方资料\n\n{links(ln)}")
for k, (name, body, proj, ln) in CONVERT.items():
    put(f"conversion/{k}/README.md", f"# {name}\n\n{body}\n\n项目：[{proj}](../../{proj})\n\n## 官方资料\n\n{links(ln)}\n{COMMON}")
for k, body in RUNTIMES.items():
    put(f"runtimes/{k}/README.md", f"# 运行方式：{k}\n\n{body}\n")
for k, (name, body) in HARDWARE.items():
    put(f"hardware/{k}/README.md", f"# {name}\n\n{body}\n\n详情见 [hardware_runtime_matrix.csv](../../manifests/hardware_runtime_matrix.csv)。\n")
print("readmes:", len(FRAMEWORKS) + len(FORMATS) + len(CONVERT) + len(RUNTIMES) + len(HARDWARE))
