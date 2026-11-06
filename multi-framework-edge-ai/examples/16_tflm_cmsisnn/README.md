# Project 16: TFLite Micro + CMSIS-NN on Cortex-M

The host build (commands in the final report) does two things:

1. Builds TFLite Micro for x86-64 and runs the INT8 model through the Micro interpreter (`tflm_digits`).
2. Generates the C array of the same `.tflite`, which is what gets flashed to a microcontroller.

The Cortex-M route is in [cortex_m/](cortex_m/): CMSIS-NN only, no interpreter, run on QEMU `mps2-an386` through `cortex_m/build_run.sh`. TFLM itself was not built for Cortex-M, because the Arm GCC toolchain is over the 100 MiB download limit.
