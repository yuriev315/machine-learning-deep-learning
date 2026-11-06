# 运行方式：embedded_linux

ARM64 和 ARM32 用 QEMU 用户态运行，入口是 [examples/19_arm64_cross](../../examples/19_arm64_cross)。此外还在 QEMU 系统模拟的干净 Debian 12 上完整部署过，见 [examples/23_clean_device_vm](../../examples/23_clean_device_vm)。这证明指令集、库和部署包正确，但延迟数字没有参考意义，也不算设备部署。
