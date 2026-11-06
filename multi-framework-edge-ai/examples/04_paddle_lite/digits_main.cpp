// Paddle Lite 2.12 light API on the shared test set. usage: paddle_digits model.nb digits_test.bin [route]
#include <paddle_api.h>
#include <cstdio>
#include "digits.h"
using namespace paddle::lite_api;
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.nb digits_test.bin [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  MobileConfig cfg; cfg.set_model_from_file(argv[1]); cfg.set_threads(1); cfg.set_power_mode(LITE_POWER_HIGH);
  auto net = CreatePaddlePredictor<MobileConfig>(cfg);
  auto in = net->GetInput(0); in->Resize({1, 1, 8, 8});
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::copy_n(test.image(i), 64, in->mutable_data<float>());
    auto t0 = digits::Clock::now(); net->Run(); double us = digits::us_since(t0);
    st.add(us, digits::argmax(net->GetOutput(0)->data<float>(), 10) == test.labels[i]);
  }
  st.report(argc > 3 ? argv[3] : "paddle_lite_cpp", argv[1]);
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
