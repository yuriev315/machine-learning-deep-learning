// OpenVINO 2025.2 C++. usage: ov_digits model.xml digits_test.bin [device=CPU] [threads=1] [route]
#include <cstdio>
#include <cstdlib>
#include <openvino/openvino.hpp>
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.xml digits_test.bin [device] [threads] [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  const std::string device = argc > 3 ? argv[3] : "CPU";
  ov::Core core;
  auto model = core.read_model(argv[1]);
  if (model->is_dynamic()) model->reshape({1, 1, 8, 8});
  ov::AnyMap cfg;
  if (device == "CPU") { cfg[ov::inference_num_threads.name()] = argc > 4 ? atoi(argv[4]) : 1; cfg[ov::hint::performance_mode.name()] = ov::hint::PerformanceMode::LATENCY; }
  auto compiled = core.compile_model(model, device, cfg);
  auto req = compiled.create_infer_request();
  auto input = req.get_input_tensor();
  const size_t pixels = test.h * test.w;
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::copy_n(test.image(i), pixels, input.data<float>());
    auto t0 = digits::Clock::now();
    req.infer();
    double us = digits::us_since(t0);
    st.add(us, digits::argmax(req.get_output_tensor().data<const float>(), 10) == test.labels[i]);
  }
  st.report(argc > 5 ? argv[5] : "openvino_cpp", std::string(argv[1]).substr(0, std::string(argv[1]).size() - 3) + "bin");
  return 0;
} catch (const std::exception& e) {
  fprintf(stderr, "error: %s\n", e.what());
  return 1;
}
