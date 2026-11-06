// TFLite Micro with CMSIS-NN kernels on Cortex-M4: flatbuffer in flash, static arena, no heap. Reports over semihosting.
#include <stdint.h>
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "model_data.h"
extern const unsigned char g_model[];
static void put(const char* s) { register int r0 __asm("r0") = 4; register const char* r1 __asm("r1") = s; __asm volatile("bkpt 0xAB" : "+r"(r0) : "r"(r1) : "memory"); }
static void put_int(int32_t v) { char b[12]; int i = 11; b[11] = 0; if (v == 0) b[--i] = '0'; while (v > 0) { b[--i] = char('0' + v % 10); v /= 10; } put(&b[i]); }
#define SYST_CSR (*(volatile uint32_t*)0xE000E010)
#define SYST_RVR (*(volatile uint32_t*)0xE000E014)
#define SYST_CVR (*(volatile uint32_t*)0xE000E018)
alignas(16) static uint8_t arena[8 * 1024];
extern "C" int main(void) {
  const tflite::Model* model = tflite::GetModel(g_model);
  tflite::MicroMutableOpResolver<4> ops; ops.AddConv2D(); ops.AddMaxPool2D(); ops.AddFullyConnected(); ops.AddReshape();
  tflite::MicroInterpreter ip(model, ops, arena, sizeof(arena));
  if (ip.AllocateTensors() != kTfLiteOk) { put("AllocateTensors failed\n"); return 1; }
  TfLiteTensor* in = ip.input(0); TfLiteTensor* out = ip.output(0);
  int32_t hit = 0, hash = 0; uint64_t ticks = 0;
  SYST_RVR = 0xFFFFFF; SYST_CVR = 0; SYST_CSR = 5;
  for (int32_t i = 0; i < N_TEST; ++i) {
    for (int p = 0; p < 64; ++p) in->data.int8[p] = test_x[i * 64 + p];
    uint32_t a = SYST_CVR;
    if (ip.Invoke() != kTfLiteOk) { put("Invoke failed\n"); return 1; }
    ticks += (a - SYST_CVR) & 0xFFFFFF;
    int best = 0; for (int k = 1; k < 10; ++k) if (out->data.int8[k] > out->data.int8[best]) best = k;
    hit += best == test_y[i]; hash += (i + 1) * best;
  }
  put("MCU_RESULT n="); put_int(N_TEST); put(" correct="); put_int(hit); put(" preds_hash="); put_int(hash); put(" systick_per_inference="); put_int(int32_t(ticks / N_TEST));
  put(" arena_used="); put_int(int32_t(ip.arena_used_bytes())); put("\n");
  return 0;
}
