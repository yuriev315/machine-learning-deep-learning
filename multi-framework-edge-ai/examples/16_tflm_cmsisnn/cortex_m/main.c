/* Bare-metal CMSIS-NN inference: no OS, no libc, no heap; all tensors are static. Same source for Cortex-M4 (DSP) and Cortex-M55 (Helium).
 * Results print over Arm semihosting, which QEMU forwards to stdout. Real boards would use a UART. */
#include <stdint.h>
#include "arm_nnfunctions.h"
#include "arm_nnsupportfunctions.h"
#include "model_data.h"
static int32_t semihost(int32_t op, const void* arg) {
  register int32_t r0 __asm("r0") = op; register const void* r1 __asm("r1") = arg;
  __asm volatile("bkpt 0xAB" : "+r"(r0) : "r"(r1) : "memory");
  return r0;
}
static void put(const char* s) { semihost(0x04, s); }
static void put_int(int32_t v) {
  char b[12]; int i = 11; b[11] = 0; if (v == 0) b[--i] = '0'; while (v > 0) { b[--i] = (char)('0' + v % 10); v /= 10; } put(&b[i]);
}
#define SYST_CSR (*(volatile uint32_t*)0xE000E010)
#define SYST_RVR (*(volatile uint32_t*)0xE000E014)
#define SYST_CVR (*(volatile uint32_t*)0xE000E018)
static int8_t scratch[2048] __attribute__((aligned(8))), t1[8 * 8 * 8], t2[4 * 4 * 8], t3[4 * 4 * 16], t4[2 * 2 * 16], out[10];
static int32_t fc_sum[10];   /* Helium FC kernel uses precomputed kernel sums */
#define OK(x) do { if ((x) != ARM_CMSIS_NN_SUCCESS) { put("CMSIS-NN error\n"); return -1; } } while (0)
static int infer(const int8_t* in) {
  cmsis_nn_context ctx = {scratch, sizeof(scratch)};
  const cmsis_nn_activation act = {-128, 127};
  const cmsis_nn_dims ud = {1, 1, 1, 1};  /* no up-scaling */
  { cmsis_nn_conv_params p = {-(C1_IN_ZP), C1_OUT_ZP, {1, 1}, {1, 1}, {1, 1}, act};
    cmsis_nn_per_channel_quant_params q = {(int32_t*)c1_m, (int32_t*)c1_s};
    cmsis_nn_dims id = {1, 8, 8, 1}, fd = {8, 3, 3, 1}, bd = {1, 1, 1, 8}, od = {1, 8, 8, 8};
    OK(arm_convolve_s8(&ctx, &p, &q, &id, in, &fd, c1_w, &bd, c1_b, &ud, &od, t1)); }
  { cmsis_nn_pool_params p = {{2, 2}, {0, 0}, act}; cmsis_nn_dims id = {1, 8, 8, 8}, fd = {1, 2, 2, 1}, od = {1, 4, 4, 8};
    OK(arm_max_pool_s8(&ctx, &p, &id, t1, &fd, &od, t2)); }
  { cmsis_nn_conv_params p = {-(C2_IN_ZP), C2_OUT_ZP, {1, 1}, {1, 1}, {1, 1}, act};
    cmsis_nn_per_channel_quant_params q = {(int32_t*)c2_m, (int32_t*)c2_s};
    cmsis_nn_dims id = {1, 4, 4, 8}, fd = {16, 3, 3, 8}, bd = {1, 1, 1, 16}, od = {1, 4, 4, 16};
    OK(arm_convolve_s8(&ctx, &p, &q, &id, t2, &fd, c2_w, &bd, c2_b, &ud, &od, t3)); }
  { cmsis_nn_pool_params p = {{2, 2}, {0, 0}, act}; cmsis_nn_dims id = {1, 4, 4, 16}, fd = {1, 2, 2, 1}, od = {1, 2, 2, 16};
    OK(arm_max_pool_s8(&ctx, &p, &id, t3, &fd, &od, t4)); }
  { cmsis_nn_fc_params p = {-(FC_IN_ZP), 0, FC_OUT_ZP, act};
    cmsis_nn_per_channel_quant_params q = {(int32_t*)fc_m, (int32_t*)fc_s};  /* TF 2.19 quantizes dense layers per output channel */
    cmsis_nn_dims id = {1, 1, 1, 64}, fd = {64, 1, 1, 10}, bd = {1, 1, 1, 10}, od = {1, 1, 1, 10};
    cmsis_nn_context fctx = {fc_sum, sizeof(fc_sum)};
    OK(arm_fully_connected_per_channel_s8(&fctx, &p, &q, &id, t4, &fd, fc_w, &bd, fc_b, &od, out)); }
  int best = 0; for (int k = 1; k < 10; ++k) if (out[k] > out[best]) best = k;
  return best;
}
int main(void) {
  int32_t hit = 0, hash = 0; uint64_t ticks = 0;
  OK(arm_vector_sum_s8(fc_sum, 64, 10, fc_w, -(FC_IN_ZP), 0, fc_b));
  SYST_RVR = 0xFFFFFF; SYST_CVR = 0; SYST_CSR = 5;   /* processor clock, no interrupt */
  for (int32_t i = 0; i < N_TEST; ++i) {
    uint32_t a = SYST_CVR;
    int p = infer(test_x + i * 64);
    ticks += (a - SYST_CVR) & 0xFFFFFF;
    if (p < 0) return 1;
    hit += p == test_y[i]; hash += (i + 1) * p;
  }
  put("MCU_RESULT n="); put_int(N_TEST); put(" correct="); put_int(hit); put(" preds_hash="); put_int(hash);
  put(" systick_per_inference="); put_int((int32_t)(ticks / N_TEST)); put("\n");
  return 0;
}
