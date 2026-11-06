// MindSpore Lite 2.6 C++. usage: msl_digits model.ms digits_test.bin [threads] [route]
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include "include/api/context.h"
#include "include/api/model.h"
#include "include/api/status.h"
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.ms digits_test.bin [threads] [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  auto ctx = std::make_shared<mindspore::Context>();
  ctx->SetThreadNum(argc > 3 ? atoi(argv[3]) : 1);
  ctx->MutableDeviceInfo().push_back(std::make_shared<mindspore::CPUDeviceInfo>());
  mindspore::Model model;
  auto st0 = model.Build(argv[1], mindspore::kMindIR, ctx);
  if (st0 != mindspore::kSuccess) { fprintf(stderr, "Build failed: %s\n", st0.ToString().c_str()); return 1; }
  auto inputs = model.GetInputs();
  auto shape = inputs[0].Shape();
  bool dynamic = false;
  for (auto& d : shape) if (d < 0) { d = 1; dynamic = true; }
  if (dynamic && model.Resize(inputs, {shape}) != mindspore::kSuccess) { fprintf(stderr, "Resize failed\n"); return 1; }
  inputs = model.GetInputs();
  fprintf(stderr, "input shape:"); for (auto d : shape) fprintf(stderr, " %ld", long(d)); fprintf(stderr, "\n");
  const size_t bytes = test.h * test.w * sizeof(float);
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::memcpy(inputs[0].MutableData(), test.image(i), bytes);
    std::vector<mindspore::MSTensor> out;
    auto t0 = digits::Clock::now();
    auto s = model.Predict(inputs, &out);
    double us = digits::us_since(t0);
    if (s != mindspore::kSuccess) { fprintf(stderr, "Predict failed\n"); return 1; }
    st.add(us, digits::argmax(reinterpret_cast<const float*>(out[0].Data().get()), 10) == test.labels[i]);
  }
  st.report(argc > 4 ? argv[4] : "mindspore_lite_cpp", argv[1]);
  return 0;
} catch (const std::exception& e) {
  fprintf(stderr, "error: %s\n", e.what());
  return 1;
}
