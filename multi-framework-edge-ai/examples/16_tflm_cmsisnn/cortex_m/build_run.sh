#!/usr/bin/env bash
# Generates the C model, compiles CMSIS-NN with clang (via zig) for two targets, runs each in QEMU with -icount for a deterministic instruction estimate.
# usage: build_run.sh m4|m55. With -icount shift=0, one instruction = 1 virtual ns, so SysTick ticks convert to instructions via the board's clock.
cd "$(dirname "$0")/../../.." && source scripts/env.sh
T=${1:-m4}; HERE=examples/16_tflm_cmsisnn/cortex_m; O=$PWD/build/cortex_m_$T; mkdir -p $O examples/artifacts/cmsis_nn
case $T in
  m4)  CPU=cortex_m4;  QM=mps2-an386; QC=cortex-m4;  HZ=25000000; ROUTE=tf_cmsisnn_int8_cortex_m4 ;;
  m55) CPU=cortex_m55; QM=mps3-an547; QC=cortex-m55; HZ=32000000; ROUTE=tf_cmsisnn_int8_cortex_m55_helium ;;
esac
python -W ignore $HERE/gen_cmsis_model.py $O/model_data.h 2>/dev/null | tee $O/ref.txt
cp $O/model_data.h examples/artifacts/cmsis_nn/tinycnn_int8_cmsis_model.h
C=third_party/cmsis-nn
SRC=$(find $C/Source/ConvolutionFunctions $C/Source/FullyConnectedFunctions $C/Source/PoolingFunctions $C/Source/NNSupportFunctions -name '*.c' | grep -v lstm)
# GCC for both targets so the comparison is fair. zig's clang does not define __ARM_FEATURE_MVE for cortex_m55 and would silently build scalar kernels.
G=third_party/arm-gcc/bin
if [ $T = m55 ]; then
  CC="$G/arm-none-eabi-gcc -mcpu=cortex-m55 -mfloat-abi=hard -nostartfiles"
  $G/arm-none-eabi-gcc -mcpu=cortex-m55 -mfloat-abi=hard -dM -E -x c /dev/null | grep -q '__ARM_FEATURE_MVE' || { echo "MVE not enabled"; exit 1; }
else
  CC="$G/arm-none-eabi-gcc -mcpu=cortex-m4 -mfloat-abi=soft -nostartfiles"
fi
$CC -O2 -ffreestanding -fno-builtin -nostdlib -static -I$C/Include -I$O -I$HERE/shim -Wl,-T,$HERE/link.ld -Wl,--gc-sections -ffunction-sections -fdata-sections \
  $HERE/main.c $HERE/startup.c $SRC -o $O/cmsis_digits.elf -lgcc 2>$O/cc.log || { grep -E 'error|undefined' $O/cc.log | head -5; exit 1; }
cp $O/cmsis_digits.elf examples/artifacts/cmsis_nn/cmsis_digits_cortex_$T.elf
timeout 300 third_party/qemu-arm/bin/qemu-system-arm -M $QM -cpu $QC -icount shift=0 -nographic -semihosting -kernel $O/cmsis_digits.elf > $O/mcu.txt 2>&1; cat $O/mcu.txt
python - "$O" "$HZ" "$ROUTE" <<'P'
import re, struct, sys, json
o, hz, route = sys.argv[1], int(sys.argv[2]), sys.argv[3]; b = open(o + "/cmsis_digits.elf", "rb").read()
shoff = struct.unpack_from("<I", b, 32)[0]; n = struct.unpack_from("<H", b, 48)[0]; es = struct.unpack_from("<H", b, 46)[0]; st = struct.unpack_from("<H", b, 50)[0]
sec = [struct.unpack_from("<10I", b, shoff + i * es) for i in range(n)]; nm = sec[st][4]
name = lambda s: b[nm + s[0]:b.index(b"\0", nm + s[0])].decode()
sz = {name(s): s[5] for s in sec if s[1] != 0}
flash = sum(v for k, v in sz.items() if k in (".isr_vector", ".text", ".ARM.exidx", ".data")); ram = sz.get(".data", 0) + sz.get(".bss", 0)
m = re.search(r"n=(\d+) correct=(\d+) preds_hash=(\d+) systick_per_inference=(\d+)", open(o + "/mcu.txt").read()); r = open(o + "/ref.txt").read()
acc = int(m[2]) / int(m[1]); ra = float(re.search(r"accuracy ([\d.]+)", r)[1]); h = int(re.search(r"preds_hash (\d+)", r)[1]); ins = int(m[4]) * 1e9 / hz
print(f"flash_bytes={flash} ram_bytes={ram} accuracy={acc:.4f} reference_accuracy={ra:.4f} identical_predictions={int(m[3]) == h} est_instructions_per_inference={ins:.0f}")
print("RESULT " + json.dumps(dict(route=route, n=int(m[1]), accuracy=round(acc, 4), latency_mean_us="", latency_p95_us="", peak_rss_kb=round(ram / 1024, 1), model_bytes=flash), separators=(",", ":")))
open(o + "/est.txt", "w").write(f"{route},{ins:.0f},{flash},{ram},{int(m[3]) == h}\n")
P
