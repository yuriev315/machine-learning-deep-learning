# 环境说明

原则：每个工具一个版本，一套互相兼容的依赖。详细版本见 [sdk_versions.csv](../manifests/sdk_versions.csv) 和 [dependency_matrix.csv](../manifests/dependency_matrix.csv)。

## 两个 Python 环境

| 环境 | Python | 内容 | 为什么单独存在 |
|---|---|---|---|
| `.envs/main` | 3.12.3 | torch 2.7.1、TensorFlow 2.19、Paddle 3.0、MindSpore 2.7.2、ONNX 1.18、ORT 1.22.0、OpenVINO 2025.2、JAX 0.6.2、Keras 3.10、IREE 3.5、coremltools 9.0、ExecuTorch 0.6.0、rknn-toolkit2 2.3.2、NumPy 1.26.4 等 | 主环境 |
| `.envs/legacy37` | 3.7.9 | MXNet 1.9.1、Paddle Lite 2.12 工具 | 这两个只支持旧 Python |

**同一个环境，但每个进程只用一个框架。** TF、Paddle、MindSpore 单独导入都正常，放在同一进程会因 protobuf 冲突而段错误。

## 版本是怎么选出来的

- **基准是 torch 2.7.1。** 其余工具统一到 2025 年中的成熟版本，而不是最新版。
- **rknn-toolkit2 决定了 NumPy 和 ONNX。** 它要求 `numpy<=1.26.4`、`onnx<=1.18.0`、`protobuf<=4.25.4`。其他工具都接受这几个版本，所以一个环境就够了。
- **C++ SDK 和 Python 包同版本。** ORT、OpenVINO、ncnn、MNN、IREE、ExecuTorch、Paddle Lite 都如此。例外：LiteRT C API 来自 TF 2.19.0 源码，Python 侧是 ai-edge-litert 1.4.0。
- **100 MiB 限制在 2026-11-05 经批准放宽。** 大文件通过 `approved_oversize` 明确列在 `manifests/resources.json` 里，其余仍受限制。
- **MindSpore 例外。** PyPI 没有 2.6，2.7.2 是最早支持 Python 3.12 的正式版。Lite 2.7 的压缩包返回 403，所以 Lite 用 2.6.0。

## 状态词

| 状态 | 含义 |
|---|---|
| `RUNNABLE_VERIFIED` | 实际运行并得到结果。`execution` 和硬件列写明是真机、模拟器还是解释器 |
| `CONVERSION_VERIFIED` | 转换成功，产物存在。不代表已在目标硬件运行 |
| `CPP_BUILD_VERIFIED` | C/C++ 编译链接成功 |
| `DEVICE_DEPLOYMENT_VERIFIED` | 在实体目标设备上部署并运行。**本项目没有任何路线获得这个状态** |
| `SOURCE_ONLY` | 只有源码，从未编译 |
| `HARDWARE_REQUIRED` | 缺硬件 |
| `SDK_REQUIRED` | 缺 SDK（超限或需要登录） |
| `DEPENDENCIES_INCOMPLETE` | 依赖不全 |
| `UNSUPPORTED` | 已确认不支持 |
| `NOT_TESTED` | 没有测试 |

## 本地补丁

都在项目目录内，没有改动系统：

- `third_party/local_libs/`：`libprotobuf.so.32`（ncnn 工具需要）。使用时要设置 `LD_LIBRARY_PATH`。
- `third_party/local_x11/`：X11 客户端库。服务器上没有它们时，Android 模拟器即使用 `-no-window` 也会段错误。
- `third_party/lavapipe/`：Mesa 软件 Vulkan 驱动。
- `third_party/gcc-aarch64/`：解压的 Ubuntu 交叉工具链。`libc.so`、`libm.so` 链接脚本里的绝对路径已改成相对路径。
- `.envs/tools/bin/`（由 `scripts/setup_tools.sh` 创建）：zig 和 GCC 的包装脚本、QEMU 链接，以及一个最小的 `unzip` 替代（本机没有 unzip，TFLM 下载脚本需要）。

## Release 打包

```bash
mkdir -p build/release
tar cf build/release/deps-wheels-py312-core.tar --exclude='rknn_toolkit2*' --exclude='tensorflow_cpu*' --exclude='paddlepaddle*' --exclude='mindspore*' --exclude='torch-2.7.1*' deps/wheels/py312 deps/wheels/py312_nodeps
tar cf build/release/deps-wheels-py312-frameworks.tar deps/wheels/py312/tensorflow_cpu* deps/wheels/py312/paddlepaddle* deps/wheels/py312/mindspore* deps/wheels/py312_nodeps/torch-2.7.1*
tar cf build/release/deps-wheels-py37.tar deps/wheels/py37
```

`deps-archives.tar` 不包含许可证不允许或不明确的内容，排除列表见最终报告第 13 节。
