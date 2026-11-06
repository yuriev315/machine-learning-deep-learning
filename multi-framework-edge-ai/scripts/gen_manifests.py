#!/usr/bin/env python3
"""Generates every manifest in manifests/ from one set of tables.

Honesty rule enforced below: a route may only claim RUNNABLE_VERIFIED if a measured row with its name exists in
manifests/runtime_test_results.csv, and a conversion may only claim CONVERSION_VERIFIED if its artifact exists on disk.
Nothing here can claim DEVICE_DEPLOYMENT_VERIFIED: emulators and simulators do not count, and no physical target device was available.
"""
import csv, hashlib, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = os.path.join(ROOT, "manifests")
A = "examples/artifacts"
ALLOWED = {"RUNNABLE_VERIFIED", "CONVERSION_VERIFIED", "CPP_BUILD_VERIFIED", "DEVICE_DEPLOYMENT_VERIFIED", "SOURCE_ONLY", "HARDWARE_REQUIRED",
           "SDK_REQUIRED", "DEPENDENCIES_INCOMPLETE", "UNSUPPORTED", "NOT_TESTED", "N/A"}


def write(name, fields, rows):
    with open(os.path.join(M, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="raise")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
    print(f"{name}: {len(rows)} rows")


results = {r["route"]: r for r in csv.DictReader(open(os.path.join(M, "runtime_test_results.csv")))}

# Versions used, one per tool
V = dict(torch="2.7.1+cpu", tf="2.19.0", keras="3.10.0", jax="0.6.2", flax="0.10.7", mx="1.9.1", ms="2.7.2", onnx="1.18.0", ort="1.22.0", ov="2025.2.0", ncnn="20250503",
         pnnx="20250725", mnn="3.2.0", iree="3.5.0", et="0.6.0", cml="9.0", rknn="2.3.2", msl="2.6.0", pl="2.12", paddle="3.0.0", tvm="0.25.0.post1", litert_py="1.4.0", litert_c="TF 2.19.0",
         tflm="3200ccd", cmsis="7.0.0", edgetpu="16.0")
X86 = "x86-64 AMD Ryzen 5 3600 CPU"
CM4 = "QEMU mps2-an386 Cortex-M4"
Q64 = "qemu-aarch64-user"
Q32 = "qemu-arm-user"
CM55 = "QEMU mps3-an547 Cortex-M55"
VM = "QEMU virt Cortex-A76, clean Debian 12"
AE = "Android-14-emulator-x86_64-KVM"
VK = "Mesa lavapipe software Vulkan on x86-64"
MIL = "Independent MIL interpreter on x86-64 (not Core ML)"


def route(i, fw, fv, sf, conv, cv, df, rt, rv, os_, arch, hw, api, conversion, build, run, device, ev="", art="", note=""):
    return dict(route_id=i, source_framework=fw, source_version=fv, source_format=sf, converter=conv, converter_version=cv, destination_format=df, runtime=rt, runtime_version=rv,
                target_os=os_, architecture=arch, hardware=hw, language_api=api, conversion_status=conversion, cpp_build_status=build, runtime_status=run, device_deployment_status=device,
                evidence_result=ev, artifact=art, note=note)


CV, CB, RV, HW, SDK, SO, NT, NA, UN, DI = "CONVERSION_VERIFIED", "CPP_BUILD_VERIFIED", "RUNNABLE_VERIFIED", "HARDWARE_REQUIRED", "SDK_REQUIRED", "SOURCE_ONLY", "NOT_TESTED", "N/A", "UNSUPPORTED", "DEPENDENCIES_INCOMPLETE"
LX = "Ubuntu 26.04 x64"
QL = "Linux (user-mode emulation)"
R = [
 # --- brief item 1
 route("R01a", "PyTorch", V["torch"], "nn.Module / .pth", "torch.onnx.export (TorchScript exporter)", V["torch"], "ONNX opset 17", "ONNX Runtime", V["ort"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_ort_cpp", f"{A}/pytorch/tinycnn.onnx"),
 route("R01b", "PyTorch", V["torch"], "nn.Module / .pth", "torch.onnx.export", V["torch"], "ONNX opset 17", "ONNX Runtime", V["ort"], "Windows x64", "x86-64", "Intel/AMD CPU", "C++17 (MSVC)", CV, NT, NT, NT, "", f"{A}/pytorch/tinycnn.onnx", "No Windows host or MSVC here. Official win-x64 SDK exists but was not tested."),
 route("R01c", "PyTorch", V["torch"], "nn.Module / .pth", "torch.onnx.export", V["torch"], "ONNX opset 17", "ONNX Runtime", V["ort"], QL, "aarch64", Q64, "C++17 (clang via zig)", CV, CB, RV, HW, "pytorch_onnx_ort_cpp_a64", f"{A}/pytorch/tinycnn.onnx", "Emulated. Latency is not meaningful."),
 route("R01d", "PyTorch", V["torch"], "nn.Module", "torch.jit.trace", V["torch"], "TorchScript", "PyTorch", V["torch"], LX, "x86-64", X86, "Python", CV, NA, RV, NT, "torchscript_py", f"{A}/pytorch/tinycnn.torchscript.pt"),
 route("R01e", "PyTorch", V["torch"], "nn.Module", "torch.export", V["torch"], ".pt2 ExportedProgram", "PyTorch", V["torch"], LX, "x86-64", X86, "Python", CV, NA, NT, NT, "", f"{A}/pytorch/tinycnn.pt2", "Reload output compared to eager: max diff 9.5e-06, printed by the script, no timed result."),
 # --- 2
 route("R02a", "PyTorch", V["torch"], "torch.export", "ExecuTorch to_edge_transform_and_lower + XNNPACK", V["et"], ".pte", "ExecuTorch", V["et"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_executorch_xnnpack_cpp", f"{A}/executorch/tinycnn_xnnpack.pte", "executorch 0.6.0 pins torch==2.7.0; run here with 2.7.1 via --no-deps."),
 route("R02b", "PyTorch", V["torch"], "PT2E INT8", "ExecuTorch XNNPACKQuantizer + XNNPACK", V["et"], ".pte INT8", "ExecuTorch", V["et"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_executorch_xnnpack_int8_cpp", f"{A}/executorch/tinycnn_xnnpack_int8.pte"),
 route("R02c", "PyTorch", V["torch"], "torch.export", "ExecuTorch", V["et"], ".pte", "ExecuTorch", V["et"], "Android 14 emulator (KVM)", "x86_64", AE, "C++ (NDK r27d)", CV, CB, RV, NT, "pytorch_executorch_android_x86_64", f"{A}/executorch/tinycnn_xnnpack.pte", "Real Android OS and bionic through adb. x86_64, not ARM. No APK."),
 route("R02d", "PyTorch", V["torch"], "torch.export", "ExecuTorch", V["et"], ".pte", "ExecuTorch", V["et"], "Android", "arm64-v8a", "Android phone", "C++ (NDK r27d)", CV, CB, HW, HW, "", f"{A}/executorch/tinycnn_xnnpack.pte", "Compiles and links. An arm64 phone was not available."),
 # --- 3
 route("R03", "PyTorch", V["torch"], "ONNX", "trtexec / TensorRT ONNX parser", "10.x", "TensorRT .engine", "TensorRT", "10.x", "Linux, JetPack", "x86-64, aarch64", "NVIDIA GPU, Jetson", "C++", SDK, SO, HW, HW, "", f"{A}/pytorch/tinycnn.onnx", "No SDK and no GPU. main.cpp compiles to an object file against the official headers with a stub CUDA header: a syntax check only, never linked."),
 # --- 4
 route("R04", "PyTorch", V["torch"], "TorchScript", "coremltools", V["cml"], ".mlpackage (mlprogram, FP16; INT8 weights)", "Core ML", "iOS16+", "iOS, iPadOS, macOS", "arm64", "Apple Neural Engine, GPU, CPU", "Swift", CV, SO, HW, HW, "", f"{A}/coreml/TinyCNN.mlpackage", "The Core ML runtime needs Apple hardware. See R04b for what was checked instead."),
 route("R04b", "PyTorch", V["torch"], "TorchScript", "coremltools", V["cml"], "MIL program in .mlpackage", "Own MIL interpreter", "n/a", LX, "x86-64", MIL, "Python", CV, NA, RV, NT, "pytorch_coreml_fp16_mil_interpreter_py", f"{A}/coreml/TinyCNN.mlpackage", "A simulation: checks converted graph and weights, not Core ML or the Neural Engine."),
 # --- 5
 route("R05a", "TensorFlow", V["tf"], "tf.keras / .h5", "TFLiteConverter", V["tf"], ".tflite FP32", "LiteRT C API", V["litert_c"], LX, "x86-64", X86, "C API", CV, CB, RV, NT, "tf_litert_float_c_api", f"{A}/tensorflow/tinycnn_float.tflite"),
 route("R05b", "TensorFlow", V["tf"], "tf.keras / .h5", "TFLiteConverter + representative dataset", V["tf"], ".tflite INT8 (uint8 I/O)", "LiteRT C API", V["litert_c"], LX, "x86-64", X86, "C API", CV, CB, RV, NT, "tf_litert_int8_c_api", f"{A}/tensorflow/tinycnn_int8.tflite"),
 route("R05c", "TensorFlow", V["tf"], "tf.keras / .h5", "TFLiteConverter", V["tf"], ".tflite FP32", "LiteRT C API", V["litert_c"], QL, "aarch64", Q64, "C API (GCC 15 cross)", CV, CB, RV, HW, "tf_litert_float_c_api_a64", f"{A}/tensorflow/tinycnn_float.tflite", "Emulated. Library built without KleidiAI, whose download failed."),
 route("R05d", "TensorFlow", V["tf"], "tf.keras / .h5", "TFLiteConverter", V["tf"], ".tflite INT8", "LiteRT C API", V["litert_c"], QL, "aarch64", Q64, "C API (GCC 15 cross)", CV, CB, RV, HW, "tf_litert_int8_c_api_a64", f"{A}/tensorflow/tinycnn_int8.tflite", "Emulated."),
 route("R05e", "TensorFlow", V["tf"], "tf.keras", "TFLiteConverter", V["tf"], ".tflite", "LiteRT C API", V["litert_c"], "Android 14 emulator (KVM)", "x86_64", AE, "C API (NDK r27d)", CV, CB, RV, NT, "tf_litert_float_android_x86_64", f"{A}/tensorflow/tinycnn_float.tflite", "Real Android OS through adb. arm64-v8a compiles and links, not run."),
 # --- 6
 route("R06a", "TensorFlow", V["tf"], "tf.function", "tf2onnx", "1.17.0", "ONNX", "ONNX Runtime", V["ort"], LX, "x86-64", X86, "Python", CV, NA, RV, NT, "tf_tf2onnx_ort_py", f"{A}/tensorflow/tinycnn_tf2onnx.onnx"),
 route("R06b", "TensorFlow", V["tf"], "ONNX from tf2onnx", "trtexec", "10.x", "TensorRT .engine", "TensorRT", "10.x", "Linux", "x86-64", "NVIDIA GPU", "C++", SDK, SO, HW, HW, "", f"{A}/tensorflow/tinycnn_tf2onnx.onnx", "TF-TRT is deprecated, so this goes through ONNX. No SDK or GPU."),
 # --- 7
 route("R07a", "TensorFlow", V["tf"], "SavedModel", "ovc", V["ov"], "OpenVINO IR", "OpenVINO", V["ov"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "tf_savedmodel_openvino_cpp", f"{A}/openvino/tinycnn_tf.xml", "Ran on an AMD CPU through the generic CPU plugin. Not an Intel CPU."),
 route("R07b", "TensorFlow", V["tf"], ".tflite", "ovc", V["ov"], "OpenVINO IR", "OpenVINO", V["ov"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "tf_tflite_openvino_cpp", f"{A}/openvino/tinycnn_tflite.xml"),
 route("R07c", "PyTorch", V["torch"], "ONNX", "ovc", V["ov"], "OpenVINO IR", "OpenVINO", V["ov"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_openvino_cpp", f"{A}/openvino/tinycnn_onnx.xml"),
 route("R07d", "PyTorch", V["torch"], "OpenVINO IR", "NNCF post-training", "2.17.0", "OpenVINO IR INT8", "OpenVINO", V["ov"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_openvino_nncf_int8_cpp", f"{A}/openvino/tinycnn_int8.xml"),
 route("R07e", "TensorFlow", V["tf"], "SavedModel", "ovc", V["ov"], "OpenVINO IR", "OpenVINO", V["ov"], "Linux, Windows", "x86-64", "Intel iGPU, Intel NPU", "C++", CV, CB, HW, HW, "", f"{A}/openvino/tinycnn_tf.xml", "No Intel GPU or NPU here."),
 # --- 8
 route("R08a", "JAX/Flax", V["jax"], "jax.export", "iree-compile llvm-cpu", V["iree"], "StableHLO, then VMFB", "IREE", V["iree"], LX, "x86-64", X86, "C API", CV, CB, RV, NT, "jax_stablehlo_iree_c_api", f"{A}/jax/tinycnn.vmfb"),
 route("R08b", "JAX/Flax", V["jax"], "StableHLO", "iree-compile llvm-cpu", V["iree"], "VMFB aarch64", "IREE", V["iree"], "Linux", "aarch64", "ARM64 Linux", "C API", CV, NT, HW, HW, "", f"{A}/jax/tinycnn_aarch64-linux-gnu.vmfb", "Compile only: no ARM64 IREE runtime was built."),
 route("R08c", "JAX/Flax", V["jax"], "StableHLO", "iree-compile llvm-cpu", V["iree"], "VMFB riscv64", "IREE", V["iree"], "Linux", "riscv64", "RISC-V Linux", "C API", CV, NT, HW, HW, "", f"{A}/jax/tinycnn_riscv64-linux-gnu.vmfb", "Needs --iree-llvmcpu-target-abi=lp64d and +f,+d: with the default ABI, iree-lld fails on __mulsf3 and others."),
 route("R08d", "Keras 3 (JAX backend)", V["keras"], ".keras", "jax.export + iree-compile", V["iree"], "StableHLO, then VMFB", "IREE Python", V["iree"], LX, "x86-64", X86, "Python", CV, NA, RV, NT, "keras3_jax_stablehlo_iree_py", f"{A}/keras/tinycnn.vmfb"),
 # --- 9
 route("R09a", "PaddlePaddle", "official fluid model", "__model__ + params", "paddle_lite_opt", V["pl"], ".nb", "Paddle Lite", V["pl"], QL, "aarch64", Q64, "C++14 (GCC 15 cross)", CV, CB, RV, HW, "", f"{A}/paddle/mobilenet_v1_arm.nb", "Official MobileNetV1. Softmax sums to 1. No labelled data, so accuracy is not measured."),
 route("R09b", "PaddlePaddle", V["paddle"], "Layer, legacy .pdmodel", "paddle.jit.save, paddle_lite_opt", V["pl"], ".nb", "Paddle Lite", V["pl"], QL, "aarch64", Q64, "C++14 (GCC 15 cross)", CV, CB, RV, HW, "paddle_lite_nb_cpp_a64", f"{A}/paddle/tinycnn_arm.nb", "Needs FLAGS_enable_pir_api=0: Lite 2.12 reads .pdmodel, not the PIR .json of Paddle 3. Emulated."),
 route("R09c", "PaddlePaddle", V["paddle"], "PIR .json", "paddle2onnx", "2.0.1", "ONNX", "ONNX Runtime", V["ort"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "paddle_onnx_ort_cpp", f"{A}/paddle/tinycnn.onnx"),
 route("R09d", "PaddlePaddle", V["paddle"], "PIR .json", "paddle.jit.save", V["paddle"], ".json + .pdiparams", "Paddle Inference", V["paddle"], LX, "x86-64", X86, "Python", CV, NA, RV, NT, "paddle_inference_py", f"{A}/paddle/pir/tinycnn.json"),
 # --- 10
 route("R10a", "MindSpore", V["ms"], "Cell / .ckpt", "mindspore.export ONNX, then converter_lite", V["msl"], ".ms", "MindSpore Lite", V["msl"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "mindspore_onnx_lite_cpp", f"{A}/mindspore_lite/tinycnn_ms_onnx.ms"),
 route("R10b", "MindSpore", V["ms"], "MINDIR", "converter_lite", V["msl"], ".ms", "MindSpore Lite", V["msl"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "mindspore_mindir_lite_cpp", f"{A}/mindspore_lite/tinycnn_ms_mindir.ms", "A 2.7.2 MINDIR loads in the 2.6.0 converter, unlike 1.0.0. Lite 2.7 tarballs returned 403, so versions differ by one minor."),
 route("R10c", "PyTorch", V["torch"], "ONNX", "converter_lite", V["msl"], ".ms", "MindSpore Lite", V["msl"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_mindspore_lite_cpp", f"{A}/mindspore_lite/tinycnn_onnx.ms"),
 route("R10d", "TensorFlow", V["tf"], ".tflite", "converter_lite", V["msl"], ".ms", "MindSpore Lite", V["msl"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "tf_tflite_mindspore_lite_cpp", f"{A}/mindspore_lite/tinycnn_tflite.ms"),
 # --- 11
 route("R11", "Caffe", "SqueezeNet 1.1 official", "prototxt + caffemodel", "caffe2ncnn", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], LX, "x86-64", X86, "Python (ncnn binding)", CV, NA, RV, NT, "", f"{A}/caffe/squeezenet.param", "Top-5 identical to OpenCV DNN on the original caffemodel, max diff 0.00000. Caffe itself not installed. No timed result row."),
 route("R11b", "Darknet", "YOLOv4-tiny official", "cfg + weights", "darknet2ncnn", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], LX, "x86-64", X86, "Python (ncnn binding)", CV, NA, RV, NT, "", f"{A}/darknet/yolov4tiny.param", "Same classes as Darknet and OpenCV on dog.jpg: truck, dog, bicycle. Darknet's own detector printed one extra car at 46%. No timed result row."),
 route("R11c", "MXNet", V["mx"], "Symbol JSON + params", "mxnet2ncnn", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "mxnet_ncnn_cpp", f"{A}/ncnn/mxnet.param"),
 route("R11d", "MXNet", V["mx"], "Symbol JSON + params", "mx.onnx.export_model", V["mx"], "ONNX", "ONNX Runtime", V["ort"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "mxnet_onnx_ort_cpp", f"{A}/mxnet/tinycnn.onnx"),
 route("R11e", "MindSpore", V["ms"], "Cell", "mindspore.export", V["ms"], "ONNX", "ONNX Runtime", V["ort"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "mindspore_onnx_ort_cpp", f"{A}/mindspore/tinycnn.onnx"),
 # --- 12
 route("R12a", "PyTorch", V["torch"], "ONNX", "onnx2ncnn + ncnnoptimize", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_ncnn_cpp", f"{A}/ncnn/tinycnn_opt.param"),
 route("R12b", "PyTorch", V["torch"], "ONNX", "onnx2ncnn + ncnnoptimize", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], QL, "aarch64", Q64, "C++17 (static)", CV, CB, RV, HW, "pytorch_onnx_ncnn_cpp_a64", f"{A}/ncnn/tinycnn_opt.param", "Emulated."),
 route("R12c", "PyTorch", V["torch"], "ONNX", "onnx2ncnn + ncnnoptimize", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], QL, "armv7", Q32, "C++17 (static musl)", CV, CB, RV, HW, "pytorch_onnx_ncnn_cpp_arm32", f"{A}/ncnn/tinycnn_opt.param", "Emulated, single-threaded build."),
 route("R12d", "PyTorch", V["torch"], "TorchScript", "pnnx", V["pnnx"], "ncnn .param/.bin", "ncnn", V["ncnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_pnnx_ncnn_cpp", f"{A}/ncnn/tinycnn_pnnx.ncnn.param"),
 route("R12e", "PyTorch", V["torch"], "ONNX", "onnx2ncnn", V["ncnn"], "ncnn .param/.bin", "ncnn", V["ncnn"], "Android 14 emulator (KVM)", "x86_64", AE, "C++ (NDK r27d)", CV, CB, RV, NT, "pytorch_onnx_ncnn_android_x86_64", f"{A}/ncnn/tinycnn_opt.param", "Real Android OS through adb. arm64-v8a CLI and JNI .so compile and link, not run. No APK."),
 # --- 13
 route("R13a", "PyTorch", V["torch"], "ONNX", "mnnconvert", V["mnn"], ".mnn", "MNN", V["mnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_mnn_cpp", f"{A}/mnn/tinycnn.mnn"),
 route("R13b", "PyTorch", V["torch"], "ONNX", "mnnconvert --weightQuantBits 8", V["mnn"], ".mnn weight INT8", "MNN", V["mnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "pytorch_onnx_mnn_weightq8_cpp", f"{A}/mnn/tinycnn_w8.mnn"),
 route("R13c", "PyTorch", V["torch"], "ONNX", "mnnconvert", V["mnn"], ".mnn", "MNN", V["mnn"], QL, "aarch64", Q64, "C++17", CV, CB, RV, HW, "pytorch_onnx_mnn_cpp_a64", f"{A}/mnn/tinycnn.mnn", "Emulated. MNN_ARM82=OFF, because zig rejects its -march flag."),
 route("R13d", "TensorFlow", V["tf"], ".tflite", "mnnconvert", V["mnn"], ".mnn", "MNN", V["mnn"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "tf_tflite_mnn_cpp", f"{A}/mnn/tinycnn_tflite.mnn"),
 route("R13e", "PyTorch", V["torch"], "ONNX", "mnnconvert", V["mnn"], ".mnn", "MNN", V["mnn"], "Android 14 emulator (KVM)", "x86_64", AE, "C++ (NDK r27d)", CV, CB, RV, NT, "pytorch_onnx_mnn_android_x86_64", f"{A}/mnn/tinycnn.mnn", "Real Android OS through adb. arm64-v8a compiles and links, not run."),
 # --- 14
 route("R14", "PyTorch", V["torch"], "ONNX", "rknn-toolkit2", V["rknn"], ".rknn INT8 for RK3588", "RKNN runtime", V["rknn"], "Linux", "aarch64", "Rockchip RK3588 NPU", "C API", CV, CB, HW, HW, "pytorch_onnx_rknn_int8_simulator_py", f"{A}/rknn/tinycnn_rk3588_int8.rknn", "Accuracy from the toolkit's x86 simulator, full test set, not an NPU. The C program links, starts under QEMU, then correctly fails: cannot open the rknn device."),
 # --- 15
 route("R15", "PyTorch or TensorFlow", V["torch"], "ONNX INT8 QDQ", "QNN EP or qnn-onnx-converter", "2.x", "QNN context binary / .dlc", "ONNX Runtime QNN EP / QNN", "2.x", "Android, Linux, Windows on Arm", "aarch64", "Qualcomm Hexagon NPU", "C++", SDK, CB, HW, HW, "", f"{A}/quant/static_qdq_perchannel.onnx", "C++ compiles against stock ORT. Runtime correctly reports QNN EP unavailable in this build. SDK needs a login."),
 # --- 16
 route("R16", "TensorFlow", V["tf"], ".tflite INT8", "edgetpu_compiler", V["edgetpu"], "_edgetpu.tflite", "libedgetpu", "n/a", "Linux", "x86-64, aarch64", "Google Coral Edge TPU", "C++ / Python", CV, NT, HW, HW, "", f"{A}/edgetpu/tinycnn_int8_edgetpu.tflite", "All operators mapped to the Edge TPU, one subgraph, per the compiler's log. No Coral device. The repo is archived."),
 # --- 17
 route("R17a", "TensorFlow", V["tf"], ".tflite INT8", "gen_cmsis_model.py + CMSIS-NN", V["cmsis"], "C arrays + kernels", "None (bare metal)", V["cmsis"], "Bare metal", "Cortex-M4 (Thumb-2, DSP)", CM4, "C (Arm GCC 15)", CV, CB, RV, HW, "tf_cmsisnn_int8_cortex_m4", f"{A}/cmsis_nn/cmsis_digits_cortex_m4.elf", "Emulated. All 450 predictions match desktop LiteRT. No real timing: QEMU is not cycle accurate."),
 route("R17a2", "TensorFlow", V["tf"], ".tflite INT8", "gen_cmsis_model.py + CMSIS-NN", V["cmsis"], "C arrays + Helium kernels", "None (bare metal)", V["cmsis"], "Bare metal", "Cortex-M55 (Helium/MVE)", CM55, "C (Arm GCC 15)", CV, CB, RV, HW, "tf_cmsisnn_int8_cortex_m55_helium", f"{A}/cmsis_nn/cmsis_digits_cortex_m55.elf", "Emulated. All 450 predictions match desktop LiteRT. GCC needed: zig's clang silently builds scalar kernels for this CPU."),
 route("R17b", "TensorFlow", V["tf"], ".tflite INT8", "C array of .tflite", V["tflm"], "C++ array", "TFLite Micro", V["tflm"], LX, "x86-64", X86, "C++17", CV, CB, RV, NT, "tf_tflm_int8_x86", f"{A}/cmsis_nn/tinycnn_int8_tflm_model.cc", "Host build."),
 route("R17e", "TensorFlow", V["tf"], ".tflite INT8", "C array of .tflite", V["tflm"], "C++ array + CMSIS-NN kernels", "TFLite Micro", V["tflm"], "Bare metal", "Cortex-M4", CM4, "C++ (Arm GCC 15)", CV, CB, RV, HW, "tf_tflm_cmsisnn_int8_cortex_m4", f"{A}/tensorflow/tinycnn_int8.tflite", "Emulated. All 450 predictions match desktop LiteRT."),
 route("R17c", "TensorFlow", V["tf"], ".tflite INT8", "X-CUBE-AI", "10.x", "STM32 C library", "X-CUBE-AI runtime", "10.x", "Bare metal", "Cortex-M", "STM32 board", "C", SDK, SDK, HW, HW, "", "", "Login required, no board."),
 route("R17d", "TensorFlow", V["tf"], ".tflite INT8", "esp-tflite-micro", "n/a", "C++ array", "TFLite Micro", "n/a", "FreeRTOS", "Xtensa, RISC-V", "ESP32", "C++", NT, NT, HW, HW, "", "", "Official example collected. ESP-IDF not installed, no board."),
 # --- 18
 route("R18a", "PyTorch", V["torch"], "ONNX", "TVM relax", V["tvm"], "compiled .so", "TVM Python runtime", V["tvm"], LX, "x86-64", X86, "Python", CV, NA, RV, NT, "pytorch_onnx_tvm_py", f"{A}/tvm/tinycnn_x86_64.so"),
 # --- others
 route("R19", "any", "n/a", "GGUF", "convert_hf_to_gguf (not run)", "b6000", "GGUF", "llama.cpp", "b6000", LX, "x86-64", X86, "C API", NA, CB, RV, NT, "", "deps/archives/stories260k-gguf/stories260K.gguf", "LLM only: not a general interchange format. Output printed by examples/22_llm_gguf, no timed result row."),
 route("R20", "whisper", "tiny.en q5_1", "ggml", "none", "1.7.6", "ggml bin", "whisper.cpp", "1.7.6", LX, "x86-64", X86, "C++ CLI", NA, CB, RV, NT, "", "deps/archives/ggml-tiny-en-q5/ggml-tiny.en-q5_1.bin", "jfk.wav transcribed correctly. No timed result row."),
 route("R21", "PyTorch", V["torch"], "ONNX", "n/a", "n/a", "ONNX + runtime tarball", "ONNX Runtime", V["ort"], "Isolated chroot, no network, empty env", "x86-64", "isolated chroot on x86-64 host", "C++17", CV, CB, RV, NT, "packaged_ort_cpp", "", "Packaging test. Same kernel and CPU as the host, so it is not a device deployment."),
 route("R22", "PyTorch", V["torch"], "ONNX", "n/a", "n/a", "ONNX", "ONNX Runtime", V["ort"], "Linux", "x86-64", "USB/CSI camera", "C++17 V4L2", CV, CB, HW, HW, "", "", "No camera. Capture code ran against fake_v4l2.c, a user-space driver simulation, and against synthetic frames: both about 0.9756 accuracy, printed by the program."),
 route("R23a", "PyTorch", V["torch"], "ONNX", "n/a", "n/a", "ONNX", "ONNX Runtime", V["ort"], "Clean Debian 12 arm64 in QEMU", "aarch64", VM, "C++17", CV, CB, RV, HW, "pytorch_onnx_ort_cpp_vm", f"{A}/pytorch/tinycnn.onnx", "Full OS with its own kernel and libc. Emulated, so no real timing."),
 route("R23b", "PyTorch", V["torch"], "ONNX", "onnx2ncnn", V["ncnn"], "ncnn", "ncnn", V["ncnn"], "Clean Debian 12 arm64 in QEMU", "aarch64", VM, "C++17", CV, CB, RV, HW, "pytorch_onnx_ncnn_cpp_vm", f"{A}/ncnn/tinycnn_opt.param"),
 route("R23c", "PyTorch", V["torch"], "ONNX", "mnnconvert", V["mnn"], ".mnn", "MNN", V["mnn"], "Clean Debian 12 arm64 in QEMU", "aarch64", VM, "C++17", CV, CB, RV, HW, "pytorch_onnx_mnn_cpp_vm", f"{A}/mnn/tinycnn.mnn"),
 route("R24", "PyTorch", V["torch"], "ONNX", "onnx2ncnn", V["ncnn"], "ncnn", "ncnn Vulkan compute", V["ncnn"], LX, "x86-64", VK, "C++17", CV, CB, RV, HW, "pytorch_onnx_ncnn_vulkan_lavapipe_cpp", f"{A}/ncnn/tinycnn_opt.param", "Runs the GPU shader path on a software driver. Says nothing about real GPU speed."),
 route("R25", "PyTorch", V["torch"], "ONNX", "torch.onnx.export", V["torch"], "ONNX", "ONNX Runtime Android AAR", V["ort"], "Android 14 emulator (KVM)", "x86_64", AE, "C++ (NDK r27d)", CV, CB, RV, NT, "pytorch_onnx_ort_android_x86_64", f"{A}/pytorch/tinycnn.onnx", "Real Android OS through adb. arm64-v8a compiles and links, not run."),
]
# Honesty checks
for r in R:
    for k in ("conversion_status", "cpp_build_status", "runtime_status", "device_deployment_status"):
        assert r[k] in ALLOWED, (r["route_id"], k, r[k])
    assert r["device_deployment_status"] != "DEVICE_DEPLOYMENT_VERIFIED", r["route_id"]
    if r["evidence_result"]:
        assert r["evidence_result"] in results, ("missing measured result", r["route_id"], r["evidence_result"])
    if r["conversion_status"] == CV and r["artifact"]:
        assert os.path.exists(os.path.join(ROOT, r["artifact"])), ("missing artifact", r["route_id"], r["artifact"])
    res = results.get(r["evidence_result"], {})
    r["measured_accuracy"], r["measured_latency_mean_us"], r["measured_on"] = res.get("accuracy", ""), res.get("latency_mean_us", ""), res.get("hardware", "")
F = ["route_id", "source_framework", "source_version", "source_format", "converter", "converter_version", "destination_format", "runtime", "runtime_version", "target_os", "architecture", "hardware", "language_api",
     "conversion_status", "cpp_build_status", "runtime_status", "device_deployment_status", "evidence_result", "measured_accuracy", "measured_latency_mean_us", "measured_on", "artifact", "note"]
write("conversion_compatibility_matrix.csv", F, R)

write("unsupported_conversion_routes.csv", ["source", "destination", "tool_or_version", "kind", "evidence", "alternative"], [
 dict(source="MindSpore 1.0.0 MINDIR (older version, no longer used)", destination="MindSpore Lite 2.6.0 .ms", tool_or_version="converter_lite 2.6.0", kind="UNSUPPORTED (tested)", evidence="load_model.cc: Parse model producer version from pb file failed", alternative="MindSpore 2.7.2 MINDIR, verified as R10b"),
  dict(source="pnnx .pnnx.onnx intermediate", destination="ONNX Runtime", tool_or_version="pnnx 20250725, ORT 1.22.0", kind="UNSUPPORTED (tested)", evidence="ORT fails to load the file: the intermediate is not a usable ONNX model", alternative="Use the pnnx ncnn output (R12d) or torch.onnx.export (R01a)"),
 dict(source="ONNX ConvInteger with int8 weights", destination="ONNX Runtime CPU", tool_or_version="ORT 1.22.0 quantize_dynamic(QInt8)", kind="UNSUPPORTED (tested)", evidence="NOT_IMPLEMENTED: Could not find an implementation for ConvInteger(10)", alternative="weight_type=QUInt8 or static QDQ INT8"),
 dict(source="StableHLO", destination="IREE VMFB riscv64 with default ABI", tool_or_version="iree-compile 3.5.0", kind="UNSUPPORTED configuration (tested)", evidence="iree-lld: undefined symbol __mulsf3", alternative="--iree-llvmcpu-target-abi=lp64d --iree-llvmcpu-target-cpu-features=+m,+a,+f,+d,+c"),
  dict(source="Paddle 3 PIR .json", destination="Paddle Lite 2.12 opt", tool_or_version="paddle_lite_opt 2.12", kind="UNSUPPORTED by version", evidence="Lite 2.12 predates PIR and takes .pdmodel", alternative="Save with FLAGS_enable_pir_api=0, verified as R09b"),
 dict(source="All of TF, Paddle, MindSpore", destination="One Python process", tool_or_version="tf 2.19.0, paddle 3.0.0, mindspore 2.7.2", kind="UNSUPPORTED (tested)", evidence="TypeError: Descriptors cannot be created directly, then a segmentation fault. Each imports fine alone", alternative="One framework per process"),
 dict(source="Android static executable", destination="NDK link", tool_or_version="NDK r27d", kind="UNSUPPORTED (tested)", evidence="ld.lld: unable to find library -landroid: no static form", alternative="Dynamic linking on the emulator"),
 dict(source="TensorFlow", destination="TensorRT directly", tool_or_version="TF-TRT", kind="NOT_TESTED, vendor deprecated", evidence="Not tested. No SDK or GPU", alternative="tf2onnx (verified R06a), then trtexec (not run)"),
 dict(source="Any model", destination="Core ML on Linux", tool_or_version="coremltools 9.0", kind="UNSUPPORTED", evidence="libcoremlpython is unavailable off macOS, so predict cannot run", alternative="Convert on Linux, test on macOS or iOS"),
 dict(source="GGUF", destination="General-purpose runtimes", tool_or_version="n/a", kind="UNSUPPORTED by design", evidence="GGUF targets ggml LLM and related runtimes", alternative="ONNX, ExecuTorch or LiteRT for other networks"),
 dict(source="Caffe, Darknet", destination="Native training on this host", tool_or_version="BVLC/caffe last commit 2020", kind="NOT_TESTED", evidence="Caffe not built. Official models were converted instead", alternative="Train in a maintained framework"),
])

write("framework_support_matrix.csv", ["framework", "tier", "maintenance_status", "version_used", "python_env", "training_status", "checkpoint_status", "export_formats_verified", "c_cpp_inference", "quantization_tried", "mobile_embedded_path", "project", "limitations"], [
 dict(framework="PyTorch", tier=1, maintenance_status="Active", version_used=V["torch"], python_env="main, py3.12", training_status=RV, checkpoint_status=RV, export_formats_verified=".pth; TorchScript; .pt2; ONNX", c_cpp_inference="ONNX Runtime, ExecuTorch, ncnn, MNN, OpenVINO, MindSpore Lite", quantization_tried="FX QAT, PT2E INT8", mobile_embedded_path="ExecuTorch, Core ML", project="examples/01_pytorch", limitations="None specific."),
 dict(framework="TensorFlow", tier=1, maintenance_status="Active", version_used=V["tf"], python_env="main, py3.12", training_status=RV, checkpoint_status=RV, export_formats_verified=".keras; .h5; SavedModel; frozen GraphDef; .tflite; ONNX via tf2onnx", c_cpp_inference="LiteRT C API, OpenVINO, MNN, MindSpore Lite", quantization_tried="Post-training INT8, dynamic range", mobile_embedded_path="LiteRT, TFLite Micro, CMSIS-NN, Edge TPU", project="examples/02_tensorflow_keras", limitations="Import TF, Paddle and MindSpore in separate processes: together they conflict over protobuf."),
 dict(framework="Keras", tier=1, maintenance_status="Active", version_used=V["keras"], python_env="main, py3.12 (JAX and TF backends)", training_status=RV, checkpoint_status=RV, export_formats_verified=".keras; .h5; StableHLO through JAX", c_cpp_inference="IREE", quantization_tried="None", mobile_embedded_path="LiteRT through the TF backend", project="examples/02_tensorflow_keras, examples/03_jax_flax", limitations="JAX backend export to SavedModel still needs TF installed."),
 dict(framework="JAX/Flax", tier=1, maintenance_status="Active", version_used=f"{V['jax']} / {V['flax']}", python_env="main, py3.12", training_status=RV, checkpoint_status=RV, export_formats_verified="Orbax; StableHLO; jax.export", c_cpp_inference="IREE C API", quantization_tried="None", mobile_embedded_path="IREE cross-compile (aarch64, riscv64), not run", project="examples/03_jax_flax", limitations="No official mobile path other than IREE or third-party converters."),
 dict(framework="PaddlePaddle", tier=1, maintenance_status="Active; Paddle Lite low activity, last commit 2025-05", version_used=f"{V['paddle']} / Lite {V['pl']}", python_env="main, py3.12; Lite tool in legacy37", training_status=RV, checkpoint_status=RV, export_formats_verified=".pdparams; PIR .json; legacy .pdmodel; .nb; ONNX", c_cpp_inference="Paddle Lite ARMv8 C++, ONNX Runtime", quantization_tried="None", mobile_embedded_path="Paddle Lite", project="examples/04_paddle_lite", limitations="Lite 2.12 needs the legacy format, FLAGS_enable_pir_api=0."),
 dict(framework="MindSpore", tier=1, maintenance_status="Active", version_used=f"{V['ms']} / Lite {V['msl']}", python_env="main, py3.12", training_status=RV, checkpoint_status=RV, export_formats_verified=".ckpt; MINDIR; ONNX", c_cpp_inference="MindSpore Lite C++, ONNX Runtime", quantization_tried="None", mobile_embedded_path="MindSpore Lite", project="examples/04b_mindspore_lite", limitations="2.6.0 is not on PyPI and 2.7.2 is the first cp312 wheel; Lite stays 2.6.0 because later tarballs return 403."),
 dict(framework="Apache MXNet", tier=2, maintenance_status="Retired: repo archived, moved to the Apache Attic", version_used=V["mx"], python_env="legacy37", training_status=RV, checkpoint_status=RV, export_formats_verified="Symbol JSON + params; ONNX", c_cpp_inference="ONNX Runtime and ncnn after conversion", quantization_tried="None", mobile_embedded_path="ncnn", project="examples/05_mxnet_legacy", limitations="Historical use only. Needs old NumPy. Do not expose to untrusted models."),
 dict(framework="Caffe", tier=2, maintenance_status="Unmaintained: BVLC/caffe last commit 2020-02, not formally archived", version_used="Not installed", python_env="main (via ncnn, OpenCV)", training_status=NT, checkpoint_status=NA, export_formats_verified="prototxt + caffemodel consumed", c_cpp_inference="ncnn after conversion", quantization_tried="None", mobile_embedded_path="ncnn", project="examples/21_legacy_caffe_darknet", limitations="Caffe never built. Official SqueezeNet 1.1 only."),
 dict(framework="Darknet", tier=2, maintenance_status="pjreddie stale since 2022; AlexeyAB slow; hank-ai fork active", version_used="AlexeyAB master snapshot", python_env="native", training_status=NT, checkpoint_status=NA, export_formats_verified="cfg + weights consumed", c_cpp_inference="Darknet CLI, ncnn", quantization_tried="None", mobile_embedded_path="ncnn", project="examples/21_legacy_caffe_darknet", limitations="Built from a moving branch: the archive hash is recorded, not a tag."),
 dict(framework="tinygrad, Burn, others", tier=2, maintenance_status="Not evaluated", version_used="", python_env="", training_status=NT, checkpoint_status=NA, export_formats_verified="", c_cpp_inference="", quantization_tried="", mobile_embedded_path="", project="", limitations="Left out to keep the environment small."),
])

write("model_format_matrix.csv", ["format", "extension", "category", "produced_by", "consumed_by", "weights_included", "portable_across_devices", "status_here", "artifact_or_placeholder"], [
 dict(format="PyTorch checkpoint", extension=".pt/.pth", category="framework", produced_by="torch.save", consumed_by="torch.load", weights_included="yes", portable_across_devices="Needs PyTorch and the Python class", status_here=RV, artifact_or_placeholder=f"{A}/pytorch/tinycnn.pth"),
 dict(format="TorchScript", extension=".pt", category="framework", produced_by="torch.jit", consumed_by="PyTorch, LibTorch, pnnx, coremltools", weights_included="yes", portable_across_devices="Where LibTorch runs", status_here=RV, artifact_or_placeholder=f"{A}/pytorch/tinycnn.torchscript.pt"),
 dict(format="ExportedProgram", extension=".pt2", category="framework", produced_by="torch.export", consumed_by="PyTorch, ExecuTorch flow", weights_included="yes", portable_across_devices="No, an intermediate", status_here=CV, artifact_or_placeholder=f"{A}/pytorch/tinycnn.pt2"),
 dict(format="SavedModel", extension="dir", category="framework", produced_by="tf.saved_model", consumed_by="TF, TFLite converter, ovc", weights_included="yes", portable_across_devices="Needs TF or a converter", status_here=CV, artifact_or_placeholder=f"{A}/tensorflow/saved_model"),
 dict(format="GraphDef (frozen)", extension=".pb", category="framework", produced_by="TF", consumed_by="Converters", weights_included="yes", portable_across_devices="Legacy", status_here=CV, artifact_or_placeholder=f"{A}/tensorflow/tinycnn_frozen.pb"),
 dict(format="Keras", extension=".keras/.h5", category="framework", produced_by="Keras", consumed_by="Keras", weights_included="yes", portable_across_devices="Needs Keras", status_here=RV, artifact_or_placeholder=f"{A}/keras/tinycnn.keras"),
 dict(format="ONNX", extension=".onnx", category="interchange", produced_by="torch, mxnet, mindspore", consumed_by="ORT, OpenVINO, ncnn, MNN, MSLite, RKNN, TVM, TensorRT", weights_included="yes", portable_across_devices="Interchange: operators vary by runtime", status_here=RV, artifact_or_placeholder=f"{A}/pytorch/tinycnn.onnx"),
 dict(format="Orbax checkpoint", extension="dir", category="framework", produced_by="orbax", consumed_by="JAX", weights_included="yes", portable_across_devices="No", status_here=RV, artifact_or_placeholder=f"{A}/jax/orbax_ckpt"),
 dict(format="StableHLO", extension=".mlir", category="interchange", produced_by="jax.export", consumed_by="IREE, XLA", weights_included="yes (constants)", portable_across_devices="Compiler input, not a deployable", status_here=CV, artifact_or_placeholder=f"{A}/jax/tinycnn.stablehlo.mlir"),
 dict(format="Paddle inference model", extension="__model__ + params", category="framework", produced_by="Paddle", consumed_by="Paddle Lite opt, Paddle2ONNX", weights_included="yes", portable_across_devices="No", status_here=CV, artifact_or_placeholder="third_party/paddle-mobilenet (from the release tarball)"),
 dict(format="MindIR", extension=".mindir", category="framework", produced_by="mindspore.export", consumed_by="MindSpore; Lite only for compatible versions", weights_included="yes", portable_across_devices="No: 1.0 to 2.6 failed", status_here=UN, artifact_or_placeholder=f"{A}/mindspore/tinycnn.mindir"),
 dict(format="Caffe", extension=".prototxt/.caffemodel", category="legacy", produced_by="Caffe", consumed_by="caffe2ncnn, OpenCV DNN", weights_included="caffemodel", portable_across_devices="No", status_here=CV, artifact_or_placeholder="deps/archives/squeezenet11-caffemodel"),
 dict(format="MXNet", extension="-symbol.json/.params", category="legacy", produced_by="MXNet", consumed_by="mxnet2ncnn, mx2onnx", weights_included="params", portable_across_devices="No", status_here=RV, artifact_or_placeholder=f"{A}/mxnet/tinycnn-symbol.json"),
 dict(format="Darknet", extension=".cfg/.weights", category="legacy", produced_by="Darknet", consumed_by="darknet2ncnn, OpenCV DNN", weights_included="weights", portable_across_devices="No", status_here=CV, artifact_or_placeholder="deps/archives/yolov4-tiny-weights"),
 dict(format="LiteRT / TFLite", extension=".tflite", category="mobile", produced_by="TFLiteConverter", consumed_by="LiteRT, TFLM (subset), ovc, mnnconvert, converter_lite", weights_included="yes", portable_across_devices="CPU-portable; delegates vary", status_here=RV, artifact_or_placeholder=f"{A}/tensorflow/tinycnn_float.tflite"),
 dict(format="ExecuTorch", extension=".pte", category="mobile", produced_by="ExecuTorch", consumed_by="ExecuTorch with matching backend and kernels", weights_included="yes", portable_across_devices="No: tied to lowering choices", status_here=RV, artifact_or_placeholder=f"{A}/executorch/tinycnn_xnnpack.pte"),
 dict(format="Core ML", extension=".mlpackage", category="mobile", produced_by="coremltools", consumed_by="Apple platforms only", weights_included="yes", portable_across_devices="Apple only", status_here=CV, artifact_or_placeholder=f"{A}/coreml/TinyCNN.mlpackage"),
 dict(format="Core ML legacy", extension=".mlmodel", category="mobile", produced_by="coremltools (neuralnetwork)", consumed_by="Apple platforms only", weights_included="yes", portable_across_devices="Apple only", status_here=NT, artifact_or_placeholder=""),
 dict(format="ncnn", extension=".param/.bin", category="mobile", produced_by="onnx2ncnn, pnnx, caffe2ncnn, darknet2ncnn, mxnet2ncnn", consumed_by="ncnn", weights_included="bin", portable_across_devices="All ncnn targets", status_here=RV, artifact_or_placeholder=f"{A}/ncnn/tinycnn_opt.param"),
 dict(format="MNN", extension=".mnn", category="mobile", produced_by="mnnconvert", consumed_by="MNN", weights_included="yes", portable_across_devices="All MNN targets", status_here=RV, artifact_or_placeholder=f"{A}/mnn/tinycnn.mnn"),
 dict(format="TNN", extension=".tnnproto/.tnnmodel", category="mobile", produced_by="TNN convert", consumed_by="TNN", weights_included="yes", portable_across_devices="TNN targets", status_here=NT, artifact_or_placeholder="Tencent/TNN last commit 2025-03; not installed"),
 dict(format="MindSpore Lite", extension=".ms", category="mobile", produced_by="converter_lite", consumed_by="MindSpore Lite", weights_included="yes", portable_across_devices="Lite targets", status_here=RV, artifact_or_placeholder=f"{A}/mindspore_lite/tinycnn_onnx.ms"),
 dict(format="Paddle Lite", extension=".nb", category="embedded", produced_by="paddle_lite_opt", consumed_by="Paddle Lite for the chosen valid_targets", weights_included="yes", portable_across_devices="No: the .nb here targets ARM", status_here=RV, artifact_or_placeholder=f"{A}/paddle/mobilenet_v1_arm.nb"),
 dict(format="TensorRT", extension=".engine/.plan", category="gpu", produced_by="trtexec", consumed_by="Same TensorRT version on the same GPU family", weights_included="yes", portable_across_devices="No", status_here=SDK, artifact_or_placeholder="placeholders/TensorRT-Linux-x86_64.tar.gz.url"),
 dict(format="OpenVINO IR", extension=".xml/.bin", category="gpu", produced_by="ovc, NNCF", consumed_by="OpenVINO", weights_included="bin", portable_across_devices="Across OpenVINO devices", status_here=RV, artifact_or_placeholder=f"{A}/openvino/tinycnn_onnx.xml"),
 dict(format="QNN / SNPE", extension=".dlc, context .bin", category="npu", produced_by="QAIRT tools", consumed_by="QNN runtime, SoC-specific", weights_included="yes", portable_across_devices="No", status_here=SDK, artifact_or_placeholder="placeholders/qairt-sdk.zip.url"),
 dict(format="RKNN", extension=".rknn", category="npu", produced_by="rknn-toolkit2", consumed_by="librknnrt on the matching SoC", weights_included="yes", portable_across_devices="No: RK3588 target here", status_here=CV, artifact_or_placeholder=f"{A}/rknn/tinycnn_rk3588_int8.rknn"),
 dict(format="Hailo", extension=".hef", category="npu", produced_by="Hailo Dataflow Compiler", consumed_by="HailoRT", weights_included="yes", portable_across_devices="No", status_here=SDK, artifact_or_placeholder="placeholders/hailo_dataflow_compiler.whl.url"),
 dict(format="Edge TPU", extension="_edgetpu.tflite", category="npu", produced_by="edgetpu_compiler", consumed_by="libedgetpu", weights_included="yes", portable_across_devices="Coral only", status_here=CV, artifact_or_placeholder=f"{A}/edgetpu/tinycnn_int8_edgetpu.tflite"),
 dict(format="Ascend", extension=".om", category="npu", produced_by="CANN ATC", consumed_by="Ascend ACL", weights_included="yes", portable_across_devices="No", status_here=SDK, artifact_or_placeholder="placeholders/Ascend-cann-toolkit.run.url"),
 dict(format="Micro C array", extension=".cc", category="embedded", produced_by="xxd-like generation", consumed_by="TFLM", weights_included="yes", portable_across_devices="MCU-portable with TFLM", status_here=RV, artifact_or_placeholder=f"{A}/cmsis_nn/tinycnn_int8_tflm_model.cc"),
 dict(format="CMSIS-NN C model", extension=".h", category="embedded", produced_by="gen_cmsis_model.py", consumed_by="CMSIS-NN", weights_included="yes", portable_across_devices="Arm Cortex-M", status_here=RV, artifact_or_placeholder=f"{A}/cmsis_nn/tinycnn_int8_cmsis_model.h"),
 dict(format="TVM module", extension=".so", category="embedded", produced_by="TVM", consumed_by="TVM runtime", weights_included="yes", portable_across_devices="No: tied to target", status_here=RV, artifact_or_placeholder=f"{A}/tvm/tinycnn_x86_64.so"),
 dict(format="IREE", extension=".vmfb", category="embedded", produced_by="iree-compile", consumed_by="IREE runtime", weights_included="yes", portable_across_devices="No: tied to compile target", status_here=RV, artifact_or_placeholder=f"{A}/jax/tinycnn.vmfb"),
 dict(format="GGUF", extension=".gguf", category="llm", produced_by="llama.cpp tools", consumed_by="llama.cpp and ggml-based runtimes", weights_included="yes", portable_across_devices="Across ggml runtimes; LLM-focused", status_here=RV, artifact_or_placeholder="deps/archives/stories260k-gguf/stories260K.gguf"),
 dict(format="ggml whisper", extension=".bin", category="audio", produced_by="whisper.cpp tools", consumed_by="whisper.cpp", weights_included="yes", portable_across_devices="Across whisper.cpp targets", status_here=RV, artifact_or_placeholder="deps/archives/ggml-tiny-en-q5/ggml-tiny.en-q5_1.bin"),
])

write("hardware_runtime_matrix.csv", ["target", "category", "runtimes_studied", "tested_here_as", "best_status_here", "real_hardware_available", "what_is_missing"], [
 dict(target="Ubuntu/Linux x64, AMD CPU", category="desktop", runtimes_studied="ORT, OpenVINO, LiteRT, ncnn, MNN, MSLite, ExecuTorch, IREE, TVM, llama.cpp, whisper.cpp", tested_here_as="Native on Ryzen 5 3600", best_status_here=RV, real_hardware_available="yes", what_is_missing=""),
 dict(target="Intel CPU", category="desktop", runtimes_studied="OpenVINO, ORT", tested_here_as="Not tested", best_status_here=HW, real_hardware_available="no", what_is_missing="Intel machine"),
 dict(target="Windows x64", category="desktop", runtimes_studied="ORT, OpenVINO", tested_here_as="Not tested", best_status_here=NT, real_hardware_available="no", what_is_missing="Windows and MSVC"),
 dict(target="NVIDIA GPU", category="desktop", runtimes_studied="TensorRT, ORT CUDA", tested_here_as="Source only", best_status_here=HW, real_hardware_available="no", what_is_missing="GPU, CUDA, TensorRT SDK"),
 dict(target="AMD GPU", category="desktop", runtimes_studied="ORT MIGraphX, ncnn Vulkan", tested_here_as="Vulkan path on software lavapipe only", best_status_here=HW, real_hardware_available="unknown card0 with no compute stack", what_is_missing="ROCm or Vulkan setup"),
 dict(target="Intel GPU/NPU", category="desktop", runtimes_studied="OpenVINO", tested_here_as="Not tested", best_status_here=HW, real_hardware_available="no", what_is_missing="Hardware and drivers"),
 dict(target="ARM64 Linux", category="embedded linux", runtimes_studied="ORT, ncnn, MNN, LiteRT, Paddle Lite", tested_here_as="QEMU user-mode; clean Debian 12 in QEMU system mode", best_status_here=RV, real_hardware_available="no", what_is_missing="Real board; real timing"),
 dict(target="ARM32 Linux", category="embedded linux", runtimes_studied="ncnn", tested_here_as="QEMU user-mode, static musl", best_status_here=RV, real_hardware_available="no", what_is_missing="Real board"),
 dict(target="Raspberry Pi", category="embedded linux", runtimes_studied="Same ARM64 builds", tested_here_as="Not tested", best_status_here=HW, real_hardware_available="no", what_is_missing="Board. zig builds target glibc 2.28"),
 dict(target="NVIDIA Jetson", category="embedded linux", runtimes_studied="TensorRT", tested_here_as="Source only", best_status_here=HW, real_hardware_available="no", what_is_missing="Board, JetPack"),
 dict(target="Rockchip RK3588", category="npu", runtimes_studied="RKNN", tested_here_as="Toolkit simulator; C app links", best_status_here=CV, real_hardware_available="no", what_is_missing="Board and NPU driver"),
 dict(target="Qualcomm Hexagon", category="npu", runtimes_studied="QNN, ORT QNN EP", tested_here_as="C++ compiles", best_status_here=CB, real_hardware_available="no", what_is_missing="QAIRT SDK, Snapdragon device"),
 dict(target="Android", category="mobile", runtimes_studied="ORT, ncnn, MNN, LiteRT, ExecuTorch", tested_here_as="Android 14 x86_64 emulator with KVM; arm64-v8a compile and link", best_status_here=RV, real_hardware_available="no", what_is_missing="ARM phone; APK flow not built"),
 dict(target="iOS, iPadOS, Apple Silicon", category="mobile", runtimes_studied="Core ML", tested_here_as="Conversion on Linux; own MIL interpreter", best_status_here=CV, real_hardware_available="no", what_is_missing="Mac, Xcode, device"),
 dict(target="Arm Cortex-M", category="mcu", runtimes_studied="CMSIS-NN, TFLM", tested_here_as="QEMU M4 and M55: CMSIS-NN, TFLM on M4", best_status_here=RV, real_hardware_available="no", what_is_missing="Real board, cycle counts"),
 dict(target="STM32", category="mcu", runtimes_studied="X-CUBE-AI, TFLM", tested_here_as="Not tested", best_status_here=SDK, real_hardware_available="no", what_is_missing="X-CUBE-AI, board"),
 dict(target="ESP32", category="mcu", runtimes_studied="esp-tflite-micro", tested_here_as="Example collected", best_status_here=SO, real_hardware_available="no", what_is_missing="ESP-IDF, board"),
 dict(target="Google Edge TPU", category="npu", runtimes_studied="libedgetpu", tested_here_as="Compiled the model; all ops mapped", best_status_here=CV, real_hardware_available="no", what_is_missing="Coral device"),
 dict(target="Hailo", category="npu", runtimes_studied="HailoRT", tested_here_as="Example collected", best_status_here=SDK, real_hardware_available="no", what_is_missing="DFC login, device"),
 dict(target="Huawei Ascend", category="npu", runtimes_studied="CANN, MindSpore Lite", tested_here_as="Not tested", best_status_here=SDK, real_hardware_available="no", what_is_missing="CANN, Ascend device"),
])

write("hardware_requirements.csv", ["project", "needs_for_full_validation", "available_here", "status"], [
 dict(project="08 ExecuTorch on Android", needs_for_full_validation="ARM Android phone", available_here="x86_64 emulator only", status=HW),
 dict(project="09 TensorRT", needs_for_full_validation="NVIDIA GPU or Jetson, TensorRT SDK", available_here="no", status=HW),
 dict(project="10 OpenVINO on Intel GPU/NPU", needs_for_full_validation="Intel Core Ultra or similar", available_here="no; AMD CPU only", status=HW),
 dict(project="11 Core ML", needs_for_full_validation="Mac, Xcode, iPhone or iPad", available_here="own MIL interpreter only", status=HW),
 dict(project="12 ncnn Android", needs_for_full_validation="ARM Android phone", available_here="x86_64 emulator only", status=HW),
 dict(project="13 MNN Android", needs_for_full_validation="ARM Android phone", available_here="x86_64 emulator only", status=HW),
 dict(project="14 RKNN", needs_for_full_validation="RK3588 board with NPU driver", available_here="no", status=HW),
 dict(project="15 QNN", needs_for_full_validation="Snapdragon device, QAIRT SDK", available_here="no", status=HW),
 dict(project="16 MCU", needs_for_full_validation="Cortex-M board such as an STM32 Nucleo, for timing and memory", available_here="QEMU only", status=HW),
 dict(project="17 Camera", needs_for_full_validation="UVC USB camera", available_here="user-space driver simulation only", status=HW),
 dict(project="19 ARM64", needs_for_full_validation="Raspberry Pi or similar, for real latency", available_here="QEMU only", status=HW),
 dict(project="20, 23 Clean device", needs_for_full_validation="A second physical Linux machine", available_here="chroot; clean Debian in QEMU", status=HW),
])

# dependency matrix: from installed envs
dep = []
for env, py in (("main", ".envs/main/bin/python"), ("legacy37", ".envs/legacy37/bin/python")):
    code = "import importlib.metadata as m;[print(d.metadata['Name'],d.version,sep='\\t') for d in m.distributions()]"
    out = subprocess.run([os.path.join(ROOT, py), "-c", code], capture_output=True, text=True).stdout
    for line in sorted(set(out.splitlines())):
        n, v = line.split("\t")
        dep.append(dict(environment=env, package=n, version=v, source=f"deps/wheels ({'py312' if env == 'main' else 'py37'})"))
write("dependency_matrix.csv", ["environment", "package", "version", "source"], dep)

write("platform_compatibility.csv", ["component", "version", "linux_x64_tested", "linux_arm64_tested", "linux_arm32_tested", "windows_tested", "macos_tested", "android_tested", "ios_tested", "mcu_tested", "compilers_verified", "notes"], [
 dict(component="ONNX Runtime SDK", version=V["ort"], linux_x64_tested="native", linux_arm64_tested="QEMU", linux_arm32_tested="no official SDK used", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a build", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15, clang (zig 0.14.1), NDK clang"),
 dict(component="LiteRT C API from TF source", version="2.19.0", linux_x64_tested="native", linux_arm64_tested="QEMU", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a build", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15, GCC 15 cross", notes="XNNPACK needs -Wno-incompatible-pointer-types on GCC 15. KleidiAI off."),
 dict(component="Android NDK", version="r27d", linux_x64_tested="n/a", linux_arm64_tested="n/a", linux_arm32_tested="n/a", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a compile and link", ios_tested="n/a", mcu_tested="n/a", compilers_verified="NDK clang 18", notes="ORT, ncnn, MNN, LiteRT, ExecuTorch."),
 dict(component="OpenVINO", version=V["ov"], linux_x64_tested="native (AMD CPU)", linux_arm64_tested="no", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="no", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15", notes="Ubuntu 24 archive on Ubuntu 26.04 works. Needs rpath-link to TBB."),
 dict(component="ncnn", version=V["ncnn"], linux_x64_tested="native", linux_arm64_tested="QEMU", linux_arm32_tested="QEMU", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a build", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15, clang (zig)", notes="Static linking verified."),
 dict(component="MNN", version=V["mnn"], linux_x64_tested="native", linux_arm64_tested="QEMU", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a build", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15, clang (zig)"),
 dict(component="MindSpore Lite", version=V["msl"], linux_x64_tested="native", linux_arm64_tested="no", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="no", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15", notes="Needs --disable-new-dtags so bundled glog resolves."),
 dict(component="ExecuTorch", version=V["et"], linux_x64_tested="native", linux_arm64_tested="no", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="x86_64 emulator; arm64-v8a build", ios_tested="no", mcu_tested="no", compilers_verified="GCC 15", notes="Needs buck2 for source lists, downloaded automatically. Size the threadpool explicitly."),
 dict(component="IREE", version=V["iree"], linux_x64_tested="native", linux_arm64_tested="compile only", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="no", ios_tested="no", mcu_tested="no", compilers_verified="GCC 15", notes="iree-dist 3.5.0 omits runtime headers; taken from the v3.5.0 source."),
 dict(component="Paddle Lite", version=V["pl"], linux_x64_tested="opt tool only", linux_arm64_tested="QEMU", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="no", ios_tested="no", mcu_tested="n/a", compilers_verified="GCC 15 cross", notes="Headers need -include cstdint; library needs -fopenmp. libstdc++ ABI only."),
 dict(component="CMSIS-NN", version=V["cmsis"], linux_x64_tested="debug build", linux_arm64_tested="n/a", linux_arm32_tested="n/a", windows_tested="no", macos_tested="no", android_tested="n/a", ios_tested="n/a", mcu_tested="QEMU Cortex-M4 and M55", compilers_verified="Arm GCC 15, clang (zig) for M4"),
 dict(component="TFLite Micro", version=V["tflm"], linux_x64_tested="native", linux_arm64_tested="no", linux_arm32_tested="no", windows_tested="no", macos_tested="no", android_tested="n/a", ios_tested="n/a", mcu_tested="QEMU Cortex-M4", compilers_verified="GCC 15, Arm GCC 15"),
 dict(component="MSVC", version="n/a", linux_x64_tested="n/a", linux_arm64_tested="n/a", linux_arm32_tested="n/a", windows_tested="no", macos_tested="n/a", android_tested="n/a", ios_tested="n/a", mcu_tested="n/a", compilers_verified="none", notes="No Windows host. Every C++ project is untested on MSVC."),
])

write("sdk_versions.csv", ["tool", "version", "why_this_version", "official_source", "local_path", "kind"], [
 dict(tool="Python", version="3.12.3", why_this_version="Reused local build. Matches the reused torch and every main-env wheel.", official_source="https://github.com/astral-sh/python-build-standalone", local_path="~/.local/share/uv/python", kind="reused"),
 dict(tool="Python (legacy)", version="3.7.9", why_this_version="Needed by Paddle Lite 2.12 wheels and retired MXNet 1.9.1.", official_source="https://github.com/indygreg/python-build-standalone", local_path="third_party/python37", kind="downloaded"),
 dict(tool="PyTorch", version=V["torch"], why_this_version="Baseline for the mid-2025 toolchain. Independent wheel, hash-checked against the official index.", official_source="https://download.pytorch.org/whl/cpu", local_path=".envs/main", kind="downloaded"),
 dict(tool="TensorFlow", version=V["tf"], why_this_version="Mature, supports Python 3.12, and matches the LiteRT C API source.", official_source="https://pypi.org/project/tensorflow-cpu/2.19.0/", local_path=".envs/main", kind="downloaded"),
 dict(tool="PaddlePaddle", version=V["paddle"], why_this_version="First major 3.x release with cp312 wheels.", official_source="https://pypi.org/project/paddlepaddle/3.0.0/", local_path=".envs/main", kind="downloaded"),
 dict(tool="MindSpore", version=V["ms"], why_this_version="Earliest final wheel for Python 3.12 on PyPI.", official_source="https://pypi.org/project/mindspore/2.7.2/", local_path=".envs/main", kind="downloaded"),
 dict(tool="Android NDK / Emulator / image", version="r27d / 37 / API 34 x86_64", why_this_version="NDK r27 is a long-term release. The x86_64 image runs on KVM.", official_source="https://dl.google.com/android/repository/", local_path="third_party/android", kind="downloaded, not redistributable"),
 dict(tool="Arm GNU GCC", version="15.2.1", why_this_version="Real Helium support for Cortex-M55; TFLM builds.", official_source="https://github.com/xpack-dev-tools/arm-none-eabi-gcc-xpack", local_path="third_party/arm-gcc", kind="downloaded"),
 dict(tool="Mesa lavapipe", version="26.0.8", why_this_version="Software Vulkan driver, for the GPU compute path.", official_source="Ubuntu 26.04 archive", local_path="third_party/lavapipe", kind="downloaded"),
 dict(tool="ONNX / ONNX Runtime", version=f"{V['onnx']} / {V['ort']}", why_this_version="onnx<=1.18 is required by rknn-toolkit2. 1.22.0 is the last ORT in that line with a Linux C++ SDK asset.", official_source="https://github.com/microsoft/onnxruntime/releases/tag/v1.22.0", local_path="third_party/onnxruntime-x64", kind="downloaded"),
 dict(tool="OpenVINO", version=V["ov"], why_this_version="Python wheel and C++ archive at the same version, mid-2025.", official_source="https://storage.openvinotoolkit.org/repositories/openvino/packages/2025.2/linux/", local_path="third_party/openvino", kind="downloaded"),
 dict(tool="ExecuTorch", version=V["et"], why_this_version="The release matching torch 2.7.", official_source="https://github.com/pytorch/executorch/tree/v0.6.0", local_path="third_party/executorch", kind="git shallow"),
 dict(tool="LiteRT C API", version="TensorFlow 2.19.0 source", why_this_version="Official CMake build, no third-party binary.", official_source="https://github.com/tensorflow/tensorflow/tree/v2.19.0/tensorflow/lite", local_path="third_party/_build/tflite_c", kind="built"),
 dict(tool="ncnn", version=V["ncnn"], why_this_version="Python binding and C++ SDK at the same date.", official_source="https://github.com/Tencent/ncnn/releases/tag/20250503", local_path="third_party/ncnn-ubuntu", kind="downloaded"),
 dict(tool="MNN", version=V["mnn"], why_this_version="Python converter and source at the same version. Linux prebuilt exceeds the limit, so built from source.", official_source="https://github.com/alibaba/MNN/releases/tag/3.2.0", local_path="third_party/_build/mnn_x64", kind="built"),
 dict(tool="IREE", version=V["iree"], why_this_version="Matches jax 0.6 era StableHLO. Python and dist at one version.", official_source="https://github.com/iree-org/iree/releases/tag/v3.5.0", local_path="third_party/iree-dist", kind="downloaded"),
 dict(tool="MindSpore Lite", version=V["msl"], why_this_version="Newest mid-2025 tarball under the limit.", official_source="https://www.mindspore.cn/lite", local_path="third_party/mindspore-lite", kind="downloaded"),
 dict(tool="RKNN Toolkit", version=V["rknn"], why_this_version="Mature cp312 release from 2025. Runtime at the same tag.", official_source="https://github.com/airockchip/rknn-toolkit2/tree/v2.3.2", local_path=".envs/main", kind="downloaded"),
 dict(tool="Paddle Lite", version=V["pl"], why_this_version="Last final release: later tags are rc. Pip tool and C++ library at one version.", official_source="https://github.com/PaddlePaddle/Paddle-Lite/releases/tag/v2.12", local_path="third_party/paddle-lite-armv8", kind="downloaded"),
 dict(tool="TVM", version=V["tvm"], why_this_version="Oldest wheel found with a Linux x86-64 build under the limit. Pair with apache-tvm-ffi 0.1.12.", official_source="https://pypi.org/project/apache-tvm/", local_path=".envs/main", kind="downloaded"),
 dict(tool="Edge TPU compiler", version=V["edgetpu"], why_this_version="Only version in the archived repo.", official_source="https://github.com/google-coral/edgetpu", local_path="third_party/edgetpu_compiler", kind="downloaded"),
 dict(tool="CMake / Ninja / Zig", version="3.31.6 / 1.11.1.4 / 0.14.1", why_this_version="Pip-installed into the project, no system change.", official_source="PyPI", local_path=".envs/main/bin", kind="downloaded"),
 dict(tool="GCC aarch64 cross", version="15.2.0", why_this_version="Unpacked Ubuntu debs. Needed for libstdc++ ABI (Paddle Lite, LiteRT).", official_source="Ubuntu 26.04 archive", local_path="third_party/gcc-aarch64", kind="downloaded"),
 dict(tool="QEMU user / system", version="7.2.0-1 / 9.2.4-1", why_this_version="Static user-mode binaries; xPack system build.", official_source="https://github.com/multiarch/qemu-user-static, https://github.com/xpack-dev-tools/qemu-arm-xpack", local_path="deps/archives, third_party/qemu-arm", kind="downloaded"),
])

# Resources from resources.json and the status of each
res = json.load(open(os.path.join(M, "resources.json")))
status = {r["name"]: r for r in csv.DictReader(open(os.path.join(M, "download_status.csv")))}
OPTIONAL = {"ncnn-android", "mnn-android", "android-emulator", "android-sysimg-34-x86_64", "debian-12-arm64", "whisper-cpp-src", "ggml-tiny-en-q5", "llama-cpp-src", "stories260k-gguf", "qemu-arm-static", "darknet-src"}
ess, opt, ph = [], [], []
for r in res:
    s = status.get(r["name"], {})
    row = dict(name=r["name"], version=r["version"], purpose=r.get("purpose", ""), license=r.get("license", ""), platform=r.get("platform", ""), url=r["url"], size_bytes=s.get("size", ""), status=s.get("status", ""))
    if s.get("status") == "URL_PLACEHOLDER":
        fname = s.get("filename", "")
        ph.append(dict(name=r["name"], filename=fname, url=r["url"], expected_size=s.get("size", ""), version=r["version"], purpose=r.get("purpose", ""), license=r.get("license", ""), hardware_platform=r.get("platform", ""), official_sha256=r.get("sha256", "") or "unavailable", download_instructions=r.get("instructions", "curl -LO <URL>"), url_file=f"placeholders/{fname}.url"))
    elif r["name"] in OPTIONAL:
        opt.append(row)
    else:
        ess.append(row)
write("essential_resources.csv", list(ess[0]), ess)
write("optional_resources.csv", list(opt[0]), opt)
write("url_placeholders.csv", list(ph[0]), ph)

write("cleanup_candidates.csv", ["path", "approx_size", "reason", "safe_to_delete", "rebuild_with"], [
 dict(path="build/", approx_size="172 MB", reason="Compiled example binaries", safe_to_delete="yes", rebuild_with="scripts/build_examples.sh, examples/19_arm64_cross/build_and_run.sh"),
 dict(path="third_party/_build/android/", approx_size="several GB", reason="Android SDK object files", safe_to_delete="yes, rebuild takes about 40 min", rebuild_with="scripts/build_android.sh, scripts/build_extra.sh et_android"),
 dict(path="build/release/", approx_size="about 3 GB", reason="Release tars that have been uploaded", safe_to_delete="yes", rebuild_with="tar commands in docs/ENVIRONMENT.md"),
 dict(path="third_party/_build/", approx_size="3.1 GB", reason="SDK object files. Keep libs if you do not want a rebuild", safe_to_delete="yes, costs about 30 min to rebuild", rebuild_with="scripts/build_sdks.sh, scripts/build_extra.sh"),
 dict(path="third_party/executorch/.git", approx_size="249 MB", reason="Shallow history of the clone", safe_to_delete="yes", rebuild_with="n/a"),
 dict(path="third_party/iree-dist/bin/clang-21, lib/libIREECompiler.so", approx_size="over 100 MB each, extracted", reason="Duplicates compiler in the iree-base-compiler wheel", safe_to_delete="yes, if no one uses iree-dist tools", rebuild_with="Re-extract from deps/archives/iree-dist"),
 dict(path="deps/archives/tensorflow-src", approx_size="84 MB", reason="Only needed to rebuild LiteRT", safe_to_delete="yes after building", rebuild_with="scripts/fetch.py tensorflow-src"),
])

# checksums over every kept download and every artifact
lines = []
for base in ("deps/archives", "deps/wheels", "examples/artifacts", "examples/data"):
    for d, _, fs in sorted(os.walk(os.path.join(ROOT, base))):
        if "calib" in d:
            continue
        for f in sorted(fs):
            p = os.path.join(d, f)
            if os.path.islink(p) or f == "dataset.txt":   # dataset.txt holds machine-specific calibration paths and is not committed
                continue
            h = hashlib.sha256()
            with open(p, "rb") as fh:
                for b in iter(lambda: fh.read(1 << 20), b""):
                    h.update(b)
            lines.append(f"{h.hexdigest()}  {os.path.relpath(p, ROOT)}")
open(os.path.join(M, "checksums.sha256"), "w").write("\n".join(lines) + "\n")
print("checksums.sha256:", len(lines))

over = [os.path.relpath(os.path.join(d, f), ROOT) for base in ("examples", "manifests", "docs") for d, _, fs in os.walk(os.path.join(ROOT, base)) for f in fs if not os.path.islink(os.path.join(d, f)) and os.path.getsize(os.path.join(d, f)) > 104857600]
assert not over, over   # Git-tracked trees only; deps/ may now hold approved files over 100 MiB
print("no Git-tracked file exceeds 100 MiB")
