#!/usr/bin/env python3
"""Generates manifests/resources.json: one pinned version per tool; official digests pulled from
the GitHub release API or vendor .sha256 files when they exist."""
import json, subprocess, urllib.request, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def gh_asset(repo, tag, name):
    a = json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}/releases/tags/{tag}", "--jq", f'.assets[]|select(.name=="{name}")']))
    return dict(url=a["browser_download_url"], expected_size=a["size"], sha256=(a.get("digest") or "").replace("sha256:", ""), filename=name)
def R(name, version, purpose, license, platform, **k):
    return dict(name=name, version=version, purpose=purpose, license=license, platform=platform, **k)
ov = "https://storage.openvinotoolkit.org/repositories/openvino/packages/2025.2/linux/openvino_toolkit_ubuntu24_2025.2.0.19140.c01cd93e24d_x86_64.tgz"
ovs = urllib.request.urlopen(ov + ".sha256").read().decode().split()[0]
raw = "https://raw.githubusercontent.com"
DEB = next(l.split()[0] for l in urllib.request.urlopen("https://cloud.debian.org/images/cloud/bookworm/latest/SHA512SUMS").read().decode().splitlines() if l.endswith("debian-12-nocloud-arm64.qcow2"))
res = [
 R("onnxruntime-x64","1.22.0","ONNX Runtime C/C++ SDK","MIT","linux-x64",**gh_asset("microsoft/onnxruntime","v1.22.0","onnxruntime-linux-x64-1.22.0.tgz")),
 R("onnxruntime-aarch64","1.22.0","ONNX Runtime C/C++ SDK","MIT","linux-aarch64",**gh_asset("microsoft/onnxruntime","v1.22.0","onnxruntime-linux-aarch64-1.22.0.tgz")),
 R("ncnn-ubuntu","20250503","ncnn libs and converters (onnx2ncnn, caffe2ncnn, darknet2ncnn, mxnet2ncnn, ncnn2table, ncnn2int8)","BSD-3-Clause","linux-x64",**gh_asset("Tencent/ncnn","20250503","ncnn-20250503-ubuntu-2404.zip")),
 R("ncnn-android","20250503","ncnn Android prebuilt","BSD-3-Clause","android",**gh_asset("Tencent/ncnn","20250503","ncnn-20250503-android.zip")),
 R("ncnn-src","20250503","ncnn full source incl. submodules: cross builds","BSD-3-Clause","source",**gh_asset("Tencent/ncnn","20250503","ncnn-20250503-full-source.zip")),
 R("mnn-src","3.2.0","MNN source","Apache-2.0","source",url="https://codeload.github.com/alibaba/MNN/tar.gz/refs/tags/3.2.0",filename="MNN-3.2.0.tar.gz"),
 R("mnn-android","3.2.0","MNN Android prebuilt","Apache-2.0","android",**gh_asset("alibaba/MNN","3.2.0","mnn_3.2.0_android_armv7_armv8_cpu_opencl_vulkan.zip")),
 R("openvino-ubuntu24","2025.2.0","OpenVINO C/C++ runtime archive","Apache-2.0","linux-x64",url=ov,sha256=ovs),
 R("iree-dist","3.5.0","IREE compiler/runtime tools, C headers and static libs","Apache-2.0 WITH LLVM-exception","linux-x64",**gh_asset("iree-org/iree","v3.5.0","iree-dist-3.5.0rc20250609-linux-x86_64.tar.xz")),
 R("mindspore-lite","2.6.0","MindSpore Lite converter and C++ runtime","Apache-2.0","linux-x64",url="https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.6.0/MindSpore/lite/release/linux/x86_64/mindspore-lite-2.6.0-linux-x64.tar.gz"),
 R("qemu-arm-xpack","9.2.4-1","Cortex-M/A system emulation (qemu-system-arm)","GPL-2.0","linux-x64",**gh_asset("xpack-dev-tools/qemu-arm-xpack","v9.2.4-1","xpack-qemu-arm-9.2.4-1-linux-x64.tar.gz")),
 R("qemu-aarch64-static","7.2.0-1","ARM64 user-mode emulation","GPL-2.0","linux-x64",**gh_asset("multiarch/qemu-user-static","v7.2.0-1","qemu-aarch64-static")),
 R("qemu-arm-static","7.2.0-1","ARM32 user-mode emulation","GPL-2.0","linux-x64",**gh_asset("multiarch/qemu-user-static","v7.2.0-1","qemu-arm-static")),
 R("tensorflow-src","2.19.0","TensorFlow source: tensorflow/lite CMake build of LiteRT C API","Apache-2.0","source",url="https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.19.0.tar.gz",filename="tensorflow-2.19.0.tar.gz"),
 R("tflite-micro-src","3200ccd","TFLite Micro source pinned to 2025-06-17 commit","Apache-2.0","source",url="https://codeload.github.com/tensorflow/tflite-micro/tar.gz/3200ccd18268346d0ea965720c5599a3d051e853",filename="tflite-micro-3200ccd.tar.gz"),
 R("cmsis-nn-src","7.0.0","CMSIS-NN kernels","Apache-2.0","source",url="https://codeload.github.com/ARM-software/CMSIS-NN/tar.gz/refs/tags/v7.0.0",filename="CMSIS-NN-7.0.0.tar.gz"),
 R("rknnrt-aarch64","2.3.2","Rockchip NPU runtime for RK3588/RK356x","Rockchip proprietary, see repo","linux-aarch64 + NPU",url=raw+"/airockchip/rknn-toolkit2/v2.3.2/rknpu2/runtime/Linux/librknn_api/aarch64/librknnrt.so"),
 R("rknn-api-h","2.3.2","RKNN C API header","Rockchip, see repo","any",url=raw+"/airockchip/rknn-toolkit2/v2.3.2/rknpu2/runtime/Linux/librknn_api/include/rknn_api.h"),
 R("paddle-lite-armv8","2.12","Paddle Lite C++ tiny-publish lib, ARMv8 Linux GCC","Apache-2.0","linux-aarch64",**gh_asset("PaddlePaddle/Paddle-Lite","v2.12","inference_lite_lib.armlinux.armv8.gcc.with_extra.tar.gz")),
 R("paddle-mobilenet-v1","fluid","Small official Paddle inference model (no local training is possible, see report)","Apache-2.0","any",url="https://paddlelite-demo.bj.bcebos.com/models/mobilenet_v1_fp32_224_fluid.tar.gz"),
 R("squeezenet11-caffemodel","1.1","Real Caffe model","BSD-2-Clause","any",url=raw+"/forresti/SqueezeNet/master/SqueezeNet_v1.1/squeezenet_v1.1.caffemodel"),
 R("squeezenet11-prototxt","1.1","Caffe net definition","BSD-2-Clause","any",url=raw+"/forresti/SqueezeNet/master/SqueezeNet_v1.1/deploy.prototxt"),
 R("yolov4-tiny-weights","yolov4","Real Darknet detector weights","YOLO LICENSE (public domain style)","any",url="https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights"),
 R("yolov4-tiny-cfg","yolov4","Darknet cfg","see repo","any",url=raw+"/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg"),
 R("darknet-src","ed59050","AlexeyAB Darknet source snapshot; legacy fork","YOLO LICENSE","source",url="https://github.com/AlexeyAB/darknet/archive/refs/heads/master.tar.gz",filename="darknet-master.tar.gz"),
 R("llama-cpp-src","b6000","llama.cpp source for GGUF inference","MIT","source",url="https://github.com/ggml-org/llama.cpp/archive/refs/tags/b6000.tar.gz",filename="llama.cpp-b6000.tar.gz"),
 R("stories260k-gguf","tinyllamas","1 MiB GGUF LLM for a real inference test","MIT","any",url="https://huggingface.co/ggml-org/models/resolve/main/tinyllamas/stories260K.gguf"),
 R("whisper-cpp-src","1.7.6","whisper.cpp source: speech inference","MIT","source",url="https://github.com/ggerganov/whisper.cpp/archive/refs/tags/v1.7.6.tar.gz",filename="whisper.cpp-1.7.6.tar.gz"),
 R("ggml-tiny-en-q5","q5_1","Quantized speech model","MIT","any",url="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.en-q5_1.bin"),
 R("python37-standalone","3.7.9","Legacy Python for TF 2.0 / MindSpore 1.0 / Paddle Lite 2.12 / MXNet 1.9","PSF","linux-x64",url="https://github.com/indygreg/python-build-standalone/releases/download/20200822/cpython-3.7.9-x86_64-unknown-linux-gnu-pgo-20200823T0036.tar.zst"),
 R("libprotobuf32-deb","3.21.12","Runtime dependency of ncnn's onnx2ncnn and caffe2ncnn on non-24.04 hosts, unpacked locally","BSD-3-Clause","linux-x64",url="http://archive.ubuntu.com/ubuntu/pool/main/p/protobuf/libprotobuf32t64_3.21.12-8.2ubuntu0.4_amd64.deb"),
 R("libssl1.1-deb","1.1.1f","Runtime dependency of MindSpore 1.0.0, unpacked locally; OpenSSL 1.1.1 is EOL","OpenSSL","linux-x64",url="http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb"),
 R("iree-src","3.5.0","IREE source: C runtime headers missing from iree-dist 3.5.0","Apache-2.0 WITH LLVM-exception","source",url="https://codeload.github.com/iree-org/iree/tar.gz/refs/tags/v3.5.0",filename="iree-3.5.0.tar.gz"),
 R("onnxruntime-android","1.22.0","ONNX Runtime official Android AAR","MIT","android",url="https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime-android/1.22.0/onnxruntime-android-1.22.0.aar",sha256="04a4617a9c797cf49225595e45b5546081cb34c86ac817581141577d3b7dbfe2"),
 # ---- over 100 MiB, downloaded with the user's approval of 2026-11-05 ----
 R("android-ndk","r27d","Android C++ cross-compilation","Android SDK license (no redistribution)","linux-x64",url="https://dl.google.com/android/repository/android-ndk-r27d-linux.zip",expected_size=663956036,sha1="22105e410cf29afcf163760cc95522b9fb981121",approved_oversize=True),
 R("android-emulator","37 (16696583)","Android Emulator, KVM-accelerated","Android SDK license (no redistribution)","linux-x64",url="https://dl.google.com/android/repository/emulator-linux_x64-16696583.zip",expected_size=354166476,sha1="4296551c0fce5928710bf29bd1ce6d4888372051",approved_oversize=True),
 R("android-sysimg-34-x86_64","34 r04","Android 14 x86_64 system image for the emulator","Android SDK license (no redistribution)","linux-x64",url="https://dl.google.com/android/repository/sys-img/android/x86_64-34_r04.zip",expected_size=720747116,sha1="5f6a249f9bc3b1b4c459b13ce2eb646c9680bed1",approved_oversize=True),
 R("android-platform-tools","37.0.2","adb","Android SDK license (no redistribution)","linux-x64",url="https://dl.google.com/android/repository/platform-tools_r37.0.2-linux.zip",expected_size=9541228,sha1="736a08af10515674e40d8b754fe87390d698da2b"),
 R("arm-none-eabi-gcc","15.2.1-1.1","GCC for Cortex-M: TFLite Micro build","GPL-3.0","linux-x64",approved_oversize=True,**gh_asset("xpack-dev-tools/arm-none-eabi-gcc-xpack","v15.2.1-1.1","xpack-arm-none-eabi-gcc-15.2.1-1.1-linux-x64.tar.gz")),
 R("debian-12-arm64","bookworm","Clean ARM64 OS image for the QEMU device simulation","Debian mixed free licenses","qemu-system-aarch64",url="https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-nocloud-arm64.qcow2",expected_size=410451968,approved_oversize=True,sha512=DEB),
 # ---- deliberately never downloaded: over 100 MiB, or gated behind a login ----


 R("mnn-linux-prebuilt","3.2.0","MNN prebuilt desktop libs; built from source here instead","Apache-2.0","linux-x64",**gh_asset("alibaba/MNN","3.2.0","mnn_3.2.0_linux_x64_cpu_opencl.zip")),
 R("tensorrt-sdk","10.x","TensorRT C++ SDK, needs an NVIDIA GPU","NVIDIA proprietary","linux-x64/aarch64 NVIDIA GPU",url="https://developer.nvidia.com/tensorrt/download",filename="TensorRT-Linux-x86_64.tar.gz",placeholder=True,instructions="NVIDIA Developer login; choose TensorRT 10 tarball for your CUDA"),
 R("qairt-sdk","2.x","Qualcomm AI Runtime SDK (QNN, SNPE)","Qualcomm proprietary","linux-x64 host, Snapdragon target",url="https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk",filename="qairt-sdk.zip",placeholder=True,instructions="Qualcomm ID login"),
 R("hailo-dfc","3.x","Hailo Dataflow Compiler and HailoRT","Hailo proprietary","linux-x64 host, Hailo device",url="https://hailo.ai/developer-zone/software-downloads/",filename="hailo_dataflow_compiler.whl",placeholder=True,instructions="Hailo Developer Zone login"),
 R("x-cube-ai","10.x","STM32Cube.AI","ST SLA","win/linux host, STM32 target",url="https://www.st.com/en/embedded-software/x-cube-ai.html",filename="x-cube-ai.zip",placeholder=True,instructions="my.st.com login"),
 R("cann-toolkit","8.x","Huawei Ascend CANN and ATC compiler","Huawei proprietary","Ascend host",url="https://www.hiascend.com/software/cann",filename="Ascend-cann-toolkit.run",placeholder=True,instructions="Huawei account; pick the build matching your NPU driver"),
 R("xcode","16+","Xcode: Core ML / Swift build and on-device test","Apple EULA","macOS only",url="https://developer.apple.com/xcode/",filename="Xcode.xip",placeholder=True,instructions="Mac App Store; cannot run on Linux"),
]
json.dump(res, open(os.path.join(ROOT, "manifests/resources.json"), "w"), indent=1)
print(len(res), "resources")
