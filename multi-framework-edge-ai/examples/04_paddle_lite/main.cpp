// Paddle Lite 2.12 light API. usage: paddle_mobilenet model.nb
// Input is a fixed gradient image, because there is no labelled ImageNet set here: this proves the .nb loads
// and runs on ARMv8, and prints top-1; it does not measure accuracy.
#include <paddle_api.h>
#include <algorithm>
#include <chrono>
#include <cstdio>
#include <iostream>
#include <memory>
using namespace paddle::lite_api;
int main(int argc, char** argv) {
  if (argc < 2) { std::cerr << "usage: " << argv[0] << " model.nb\n"; return 2; }
  MobileConfig cfg;
  cfg.set_model_from_file(argv[1]);
  cfg.set_threads(1);
  cfg.set_power_mode(LITE_POWER_HIGH);
  auto net = CreatePaddlePredictor<MobileConfig>(cfg);
  auto in = net->GetInput(0);
  in->Resize({1, 3, 224, 224});
  auto* d = in->mutable_data<float>();
  for (int i = 0; i < 3 * 224 * 224; ++i) d[i] = float(i % 224) / 224.0f - 0.5f;
  auto t0 = std::chrono::steady_clock::now();
  net->Run();
  double ms = std::chrono::duration<double, std::milli>(std::chrono::steady_clock::now() - t0).count();
  auto out = net->GetOutput(0);
  const float* o = out->data<float>();
  int64_t n = out->shape()[1];
  int top = int(std::max_element(o, o + n) - o);
  float sum = 0; for (int64_t i = 0; i < n; ++i) sum += o[i];
  printf("classes=%ld top1=%d score=%.4f sum=%.4f run_ms=%.1f\n", long(n), top, o[top], sum, ms);
  return (n == 1000 && sum > 0.99f && sum < 1.01f) ? 0 : 1;   // softmax output must sum to 1
}
