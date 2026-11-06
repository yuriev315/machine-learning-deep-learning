#!/usr/bin/env bash
# TFLite Micro for Cortex-M4 with CMSIS-NN optimized kernels, using the project-local Arm GCC.
cd "$(dirname "$0")/.." && source scripts/env.sh; G=$PWD/third_party/arm-gcc/bin; cd third_party/tflite-micro
make -f tensorflow/lite/micro/tools/make/Makefile -j3 TARGET=cortex_m_generic TARGET_ARCH=cortex-m4 OPTIMIZED_KERNEL_DIR=cmsis_nn BUILD_TYPE=release TARGET_TOOLCHAIN_ROOT=$G/ microlite
