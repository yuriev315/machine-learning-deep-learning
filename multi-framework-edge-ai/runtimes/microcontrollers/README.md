# 运行方式：microcontrollers

CMSIS-NN 在 QEMU Cortex-M4 和 Cortex-M55（Helium）上、TFLite Micro 在 Cortex-M4 上，都跑完 450 张测试图，预测与桌面 LiteRT 完全一致。入口：[examples/16_tflm_cmsisnn/cortex_m](../../examples/16_tflm_cmsisnn/cortex_m)。QEMU 不精确模拟周期，只有估算的指令数，不是时序数据。
