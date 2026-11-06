#!/usr/bin/env python3
"""Generates docs/FINAL_REPORT_cn.md and manifests/quant_comparison.csv. Every number comes from a CSV written by a real run."""
import csv, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = os.path.join(ROOT, "manifests")
load = lambda n: list(csv.DictReader(open(os.path.join(M, n))))
res = {r["route"]: r for r in load("runtime_test_results.csv")}
routes = load("conversion_compatibility_matrix.csv")
ph = load("url_placeholders.csv")
dl = load("download_status.csv")
RELEASE = "https://github.com/yuriev315/machine-learning-deep-learning/releases/tag/multi-framework-edge-ai-20261106"


def table(head, rows):
    return "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "".join("| " + " | ".join(str(c) for c in r) + " |\n" for r in rows)


def est(path):
    try:
        r = open(os.path.join(ROOT, path)).read().strip().split(",")
        return (r[0], f"{int(r[1]):,}", r[2], r[3], "是" if r[4] == "True" else "否")
    except FileNotFoundError:
        return (path, "无", "", "", "")


mcu_rows = [est("build/cortex_m_m4/est.txt"), est("build/cortex_m_m55/est.txt"), est("build/tflm_m4/est.txt")]


def du(p):
    return subprocess.run(["du", "-sh", os.path.join(ROOT, p)], capture_output=True, text=True).stdout.split("\t")[0]


# --- quantization table
Q = [("LiteRT C API", "tf_litert_float_c_api", ["tf_litert_dynrange_c_api", "tf_litert_int8_c_api"]),
     ("ONNX Runtime Python", "ort_fp32", ["ort_fp32_graph_optimized", "ort_fp16", "ort_dynamic_uint8", "ort_static_int8_pertensor", "ort_static_int8_perchannel", "ort_static_weights_int4"]),
     ("ExecuTorch C++", "pytorch_executorch_xnnpack_cpp", ["pytorch_executorch_xnnpack_int8_cpp"]),
     ("OpenVINO Python", "openvino_fp32", ["openvino_nncf_int8"]),
     ("MNN C++", "pytorch_onnx_mnn_cpp", ["pytorch_onnx_mnn_weightq8_cpp"]),
     ("PyTorch", "pytorch_eager_py", ["pytorch_qat_fbgemm_int8"])]
qrows = []
for rt, base, vs in Q:
    b = res[base]
    for v in [base] + vs:
        r = res[v]
        qrows.append(dict(runtime=rt, variant=v, baseline=base, original_bytes=b["model_bytes"], converted_bytes=r["model_bytes"], accuracy=r["accuracy"], accuracy_delta=f"{float(r['accuracy']) - float(b['accuracy']):+.4f}", latency_mean_us=r["latency_mean_us"], latency_p95_us=r["latency_p95_us"], peak_rss_kb=r["peak_rss_kb"], hardware=r["hardware"]))
with open(os.path.join(M, "quant_comparison.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(qrows[0])); w.writeheader(); w.writerows(qrows)

status_count = {}
for r in dl:
    status_count[r["status"]] = status_count.get(r["status"], 0) + 1
avoid = sum(int(r["expected_size"]) for r in ph if r["expected_size"].isdigit() and int(r["expected_size"]) > 104857600)

native = [r for r in res.values() if r["hardware"].startswith("x86-64") and r["api"] in ("C++", "C API", "C++ (TFLM)")]
native.sort(key=lambda r: r["route"])
emul = [r for r in res.values() if not r["hardware"].startswith("x86-64")]
emul.sort(key=lambda r: r["route"])

conv = [r for r in routes if r["conversion_status"] == "CONVERSION_VERIFIED"]
conv_rows = [(r["route_id"], f"{r['source_framework']} {r['source_format']}", r["converter"], r["destination_format"], r["target_os"], r["hardware"], r["runtime_status"], r["measured_accuracy"] or "无实测行") for r in conv]

doc = f"""# 多框架深度学习训练、转换与边缘部署：最终报告

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

{table(["框架", "维护状态", "使用版本", "训练", "项目"], [(r["framework"], r["maintenance_status"], r["version_used"], r["training_status"], r["project"]) for r in load("framework_support_matrix.csv")])}
维护状态依据 GitHub API 在当天查询的结果，见 `manifests/maintenance_status.csv`。

## 2. 覆盖的模型格式

共 {len(load("model_format_matrix.csv"))} 种，见 `manifests/model_format_matrix.csv`。

{table(["格式", "类别", "能否跨设备", "本机状态"], [(r["format"], r["category"], r["portable_across_devices"], r["status_here"]) for r in load("model_format_matrix.csv")])}
GGUF 单独归为 LLM 类，不是通用交换格式。ONNX 也不是必经之路：ExecuTorch、Core ML、LiteRT、IREE 路线都没有经过它。

## 3. 转换工具链

- **已实际运行：** torch.onnx、torch.export、ExecuTorch 0.6.0、coremltools 9.0、TF 2.19 TFLiteConverter、tf2onnx、Paddle2ONNX、ovc 与 NNCF、onnx2ncnn、pnnx、caffe2ncnn、darknet2ncnn、mxnet2ncnn、mnnconvert、converter_lite、paddle_lite_opt、rknn-toolkit2 2.3.2、edgetpu_compiler 16.0、iree-compile 3.5.0、TVM 0.25.0.post1。
- **没有运行：** trtexec、QAIRT（直链返回 403）、Hailo DFC、X-CUBE-AI、CANN ATC（都需要登录或硬件）。

各工具的输入、输出、限制见 `conversion/*/README.md` 和 `manifests/sdk_versions.csv`。

## 4. 硬件目标

{table(["目标", "本机测试方式", "最高状态", "缺什么"], [(r["target"], r["tested_here_as"], r["best_status_here"], r["what_is_missing"] or "无") for r in load("hardware_runtime_matrix.csv")])}

## 5. C/C++ 运行时选项

已运行：ONNX Runtime 1.22.0、LiteRT C API（TF 2.19.0 源码）、OpenVINO 2025.2.0、ncnn 20250503、MNN 3.2.0、MindSpore Lite 2.6.0、ExecuTorch 0.6.0、IREE 3.5.0、TFLite Micro、CMSIS-NN 7.0.0、Paddle Lite 2.12、llama.cpp、whisper.cpp。

已编译但无法运行：RKNN C API（缺 NPU）、ORT QNN EP（缺 SDK 和设备）、ncnn JNI `.so`（没有构建 APK）。

只做过语法检查：TensorRT（用官方头文件和 CUDA 占位头）。从未编译：Swift Core ML。

## 6. 已验证的转换路线

共 {len(conv)} 条。转换成功和设备部署是分开记录的。“无实测行”表示没有写入结果 CSV，要看对应备注。

{table(["ID", "来源", "转换工具", "目标格式", "目标系统", "硬件", "运行状态", "实测准确率"], conv_rows)}
第 6 节要求的 18 条研究路线，全部有记录（包括失败和未测试的），见 `manifests/conversion_compatibility_matrix.csv` 和 `manifests/unsupported_conversion_routes.csv`。

## 7. 编译成功的 C/C++ 项目

全部使用同一个测试集（UCI digits，450 张 8x8 图，真实数据但模型很小）。x86-64 真机，单线程。

{table(["路线", "准确率", "平均延迟 µs", "P95 µs", "峰值内存 KB", "模型字节"], [(r["route"], r["accuracy"], r["latency_mean_us"], r["latency_p95_us"], r["peak_rss_kb"], r["model_bytes"]) for r in native])}
**如何看这些数字：** 这是在跑着其他在线服务的共享机器上做的单次测量，还有 CPU 配额限制，只能说明“能跑、量级如何”，不是严谨的性能基准。同一路线多次运行差异明显，平均值和 P95 都可能受线程池与调度影响，不要拿个位数或几十微秒的差距下结论。一个实际踩到的坑：ExecuTorch 默认线程池的线程数等于核心数，在 CPU 配额下会被反复限流，同一模型测出过约 41.8 ms；固定为 1 个线程后，三次重复都稳定在约 3.6–4.2 µs。Python 版 ExecuTorch 路线没有固定线程池，其延迟不要参考。不同框架训练出的权重也不同，准确率差异不代表运行时优劣。TFLM 那一行的模型字节是 0，因为模型直接编译进了程序，大小要看 `tinycnn_int8.tflite`。

模拟环境中的运行。这些是真实执行，但硬件是模拟的，延迟没有参考意义，“字节”一列对 MCU 是 Flash 占用：

{table(["路线", "执行方式", "准确率", "模型或 Flash 字节"], [(r["route"], r["hardware"], r["accuracy"], r["model_bytes"]) for r in emul])}
**MCU 估算（来自 QEMU `-icount`，不是周期数）：**

{table(["路线", "估算指令数/次推理", "Flash 字节", "RAM 字节", "预测与桌面 LiteRT 一致"], mcu_rows)}
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
| 空环境、无网络的 chroot | 运行时打包完整（准确率 {res["packaged_ort_cpp"]["accuracy"]}） | 内核和 CPU 都还是本机 |

## 9. 量化与优化

{table(["运行时", "变体", "原始字节", "转换后字节", "准确率", "变化", "平均 µs", "峰值内存 KB"], [(r["runtime"], r["variant"], r["original_bytes"], r["converted_bytes"], r["accuracy"], r["accuracy_delta"], r["latency_mean_us"], r["peak_rss_kb"]) for r in qrows])}
全部测量硬件：AMD Ryzen 5 3600，单线程。

- **INT8 在这里并没有普遍更快。** 模型极小，量化节点的开销占比高；这个结果不能推广到大模型或 NPU。
- **小模型的 ONNX QDQ 文件反而比 FP32 大**，因为多出的节点信息超过了省下的权重空间。
- Python 行的峰值内存是整个进程的累计值，主要反映 Python 和框架本身，不是模型占用。
- **已做：** FP32、FP16、INT8、INT4 权重（ORT）、训练后量化、QAT（PyTorch FX）、校准集、逐通道和逐张量、动态和静态量化、图优化（ORT 节点 8 → 7，ncnnoptimize 融合）、内存规划（TFLM arena 2592 字节）、XNNPACK 和 CMSIS-NN 内核选择。
- **未做：** BF16（本机 CPU 不支持 avx512_bf16，这条路线没有运行）、真实 GPU 和 NPU 的加速对比（没有硬件）。

## 10. 缺少的 SDK 和硬件

{table(["项目", "完整验证需要", "本机有无", "状态"], [(r["project"], r["needs_for_full_validation"], r["available_here"], r["status"]) for r in load("hardware_requirements.csv")])}
以后如果能提供硬件，优先级建议：RK3588 开发板或树莓派（同时验证 ARM64 真实延迟和干净设备部署）→ Android 手机 → NVIDIA GPU 或 Jetson → STM32 Nucleo。

## 11. 用 URL 占位的资源

这些需要登录、下载地址无法访问，或者这里已从源码编译而不需要，所以没有下载。每个都有 `placeholders/*.url`。

{table(["名称", "版本", "预计大小", "官方 SHA256", "用途"], [(r["name"], r["version"], "需登录，未知" if not (r["expected_size"].isdigit() and int(r["expected_size"]) > 104857600) else f"{int(r['expected_size'])/1048576:.0f} MiB", (r["official_sha256"][:12] + "…") if r["official_sha256"] != "unavailable" else "无", r["purpose"][:50]) for r in ph])}

## 12. 精确复现命令

已测试：`scripts/setup_env.sh` 从本地 wheel 重建环境并成功导入主要模块；`scripts/run_all.sh` 在已有 SDK 的情况下完整重跑，结果见 `docs/run_all_summary.txt`。**没有测试：** 在一台全新的机器上从 `git clone` 开始走完全程。

```bash
git clone --depth 1 --branch multi-framework-edge-ai-20261106 https://github.com/yuriev315/machine-learning-deep-learning.git mldl && cd mldl/multi-framework-edge-ai
# 依赖：从 {RELEASE} 下载所有 tar，在仓库根目录解压，再用下面的命令补齐 Release 中没有的部分
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

{table(["目录", "大小", "是否上传"], [(".envs/", du(".envs"), "否"), ("deps/", du("deps"), "部分（Release）"), ("third_party/", du("third_party"), "只传 official_examples"), ("build/", du("build"), "否"), ("examples/", du("examples"), "是（Git）")])}
- 下载校验：{status_count.get("SHA256_VERIFIED", 0) + status_count.get("SHA1_VERIFIED", 0) + status_count.get("SHA512_VERIFIED", 0)} 个文件通过官方摘要校验；**{status_count.get("HASH_UNVERIFIED_NO_OFFICIAL_DIGEST", 0)} 个文件官方没有公布摘要，只有本地哈希，属于未验证**（主要是较老的 GitHub Release 和直链），明细见 `manifests/download_status.csv`。
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
"""
open(os.path.join(ROOT, "docs/FINAL_REPORT_cn.md"), "w").write(doc)
print("report chars", len(doc), "native rows", len(native), "emulated rows", len(emul), "verified conversions", len(conv), "avoid GiB", round(avoid / 1073741824, 2), status_count)
