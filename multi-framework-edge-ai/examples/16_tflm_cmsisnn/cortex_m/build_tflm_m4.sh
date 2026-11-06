#!/usr/bin/env bash
# TFLite Micro + CMSIS-NN kernels on an emulated Cortex-M4. Needs scripts/build_tflm_m.sh and a prior build_run.sh m4 (for the embedded test data).
cd "$(dirname "$0")/../../.." && source scripts/env.sh
H=examples/16_tflm_cmsisnn/cortex_m; O=build/tflm_m4; mkdir -p $O; TM=third_party/tflite-micro; G=third_party/arm-gcc/bin
python3 -c "
b=open('examples/artifacts/tensorflow/tinycnn_int8.tflite','rb').read()
f=open('$O/model.cc','w');f.write('#include <cstdint>\nalignas(16) extern const unsigned char g_model[] = {'+','.join(str(x) for x in b)+'};\n')"
sed -e 's/LENGTH = 512K/LENGTH = 1024K/' $H/link.ld | sed -e 's/\*(.text\*) \*(.rodata\*)/*(.text*) *(.rodata*) KEEP(*(.init)) KEEP(*(.fini)) . = ALIGN(4); __preinit_array_start = .; KEEP(*(.preinit_array)) __preinit_array_end = .; __init_array_start = .; KEEP(*(.init_array*)) __init_array_end = .; __fini_array_start = .; KEEP(*(.fini_array*)) __fini_array_end = .;/' -e 's/\*(.bss\*) \*(COMMON)/*(.bss*) *(COMMON) __bss_end__ = .; end = .;/' > $O/link.ld
F="-mcpu=cortex-m4 -mfloat-abi=soft -mthumb -O2 -ffunction-sections -fdata-sections -fno-exceptions -DUSE_LIBC -DTF_LITE_STATIC_MEMORY -DTF_LITE_STRIP_ERROR_STRINGS -DCMSIS_NN"
$G/arm-none-eabi-gcc $F -c $H/startup.c -o $O/startup.o || exit 1
$G/arm-none-eabi-g++ $F -std=c++17 -fno-rtti -fno-threadsafe-statics -I$TM -I$TM/tensorflow/lite/micro/tools/make/downloads/flatbuffers/include -I$TM/tensorflow/lite/micro/tools/make/downloads/gemmlowp -Ibuild/cortex_m_m4 -nostartfiles --specs=nano.specs --specs=nosys.specs -Wl,-T,$O/link.ld -Wl,--gc-sections $H/tflm_m4.cc $O/model.cc $O/startup.o $TM/gen/cortex_m_generic_cortex-m4_release_cmsis_nn_gcc/lib/libtensorflow-microlite.a -lm -o $O/tflm.elf || exit 1
timeout 280 third_party/qemu-arm/bin/qemu-system-arm -M mps2-an386 -cpu cortex-m4 -icount shift=0 -nographic -semihosting -kernel $O/tflm.elf > $O/mcu.txt 2>&1; cat $O/mcu.txt; $G/arm-none-eabi-size $O/tflm.elf | tail -1
python3 - "$O" <<'P'
import json, re, subprocess, sys
o = sys.argv[1]; m = re.search(r"n=(\d+) correct=(\d+) preds_hash=(\d+) systick_per_inference=(\d+) arena_used=(\d+)", open(o + "/mcu.txt").read())
ref = open("build/cortex_m_m4/ref.txt").read(); h = int(re.search(r"preds_hash (\d+)", ref)[1])
sz = subprocess.check_output(["third_party/arm-gcc/bin/arm-none-eabi-size", o + "/tflm.elf"], text=True).splitlines()[-1].split()
ins = int(m[4]) * 40; print(f"flash_bytes={int(sz[0]) + int(sz[1])} ram_bytes={int(sz[1]) + int(sz[2])} arena_used={m[5]} identical_predictions={int(m[3]) == h} est_instructions_per_inference={ins}")
print("RESULT " + json.dumps(dict(route="tf_tflm_cmsisnn_int8_cortex_m4", n=int(m[1]), accuracy=round(int(m[2]) / int(m[1]), 4), latency_mean_us="", latency_p95_us="", peak_rss_kb=round((int(sz[1]) + int(sz[2])) / 1024, 1), model_bytes=int(sz[0]) + int(sz[1])), separators=(",", ":")))
open(o + "/est.txt", "w").write(f"tf_tflm_cmsisnn_int8_cortex_m4,{ins},{int(sz[0]) + int(sz[1])},{int(sz[1]) + int(sz[2])},{int(m[3]) == h}\n")
P
