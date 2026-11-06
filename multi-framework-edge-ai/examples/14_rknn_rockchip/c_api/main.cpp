// RKNN C API for RK3588. Cross-compiles and links here. Execution needs the NPU driver and a Rockchip board: never run on hardware.
// usage: rknn_digits model.rknn digits_test.bin
#include <rknn_api.h>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <vector>
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.rknn digits_test.bin\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  std::ifstream f(argv[1], std::ios::binary | std::ios::ate); if (!f) { fprintf(stderr, "cannot open model\n"); return 1; }
  std::vector<char> blob(size_t(f.tellg())); f.seekg(0); f.read(blob.data(), std::streamsize(blob.size()));
  rknn_context ctx = 0;
  int ret = rknn_init(&ctx, blob.data(), uint32_t(blob.size()), 0, nullptr);
  if (ret != RKNN_SUCC) { fprintf(stderr, "rknn_init failed: %d (needs an RKNPU driver on a Rockchip board)\n", ret); return 1; }
  rknn_core_mask mask = RKNN_NPU_CORE_0; rknn_set_core_mask(ctx, mask);
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    rknn_input in{}; in.index = 0; in.buf = const_cast<float*>(test.image(i)); in.size = 64 * sizeof(float); in.pass_through = 0; in.type = RKNN_TENSOR_FLOAT32; in.fmt = RKNN_TENSOR_NHWC;
    if ((ret = rknn_inputs_set(ctx, 1, &in)) != RKNN_SUCC) { fprintf(stderr, "rknn_inputs_set: %d\n", ret); return 1; }
    auto t0 = digits::Clock::now();
    if ((ret = rknn_run(ctx, nullptr)) != RKNN_SUCC) { fprintf(stderr, "rknn_run: %d\n", ret); return 1; }
    rknn_output out{}; out.want_float = 1;
    if ((ret = rknn_outputs_get(ctx, 1, &out, nullptr)) != RKNN_SUCC) { fprintf(stderr, "rknn_outputs_get: %d\n", ret); return 1; }
    double us = digits::us_since(t0);
    st.add(us, digits::argmax(static_cast<float*>(out.buf), 10) == test.labels[i]);
    rknn_outputs_release(ctx, 1, &out);
  }
  st.report("pytorch_onnx_rknn_rk3588_npu", argv[1]);
  rknn_destroy(ctx);
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
