// ONNX Runtime C++: load model, allocate tensor, run, read output. usage: ort_digits model.onnx digits_test.bin [threads]
#include <onnxruntime_cxx_api.h>
#include <array>
#include <cstdio>
#include <cstdlib>
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.onnx digits_test.bin [threads]\n", argv[0]); return 2; }
  const int threads = argc > 3 ? atoi(argv[3]) : 1;
  auto test = digits::load(argv[2]);
  Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "digits");
  Ort::SessionOptions so;
  so.SetIntraOpNumThreads(threads);
  so.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_ALL);
  Ort::Session session(env, argv[1], so);
  Ort::AllocatorWithDefaultOptions alloc;
  auto in_name = session.GetInputNameAllocated(0, alloc);
  auto out_name = session.GetOutputNameAllocated(0, alloc);
  const char* in_names[] = {in_name.get()};
  const char* out_names[] = {out_name.get()};
  std::array<int64_t, 4> shape{1, 1, test.h, test.w};  // NCHW
  std::vector<float> input(test.h * test.w);
  auto mem = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
  Ort::Value in = Ort::Value::CreateTensor<float>(mem, input.data(), input.size(), shape.data(), shape.size());
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::copy_n(test.image(i), input.size(), input.begin());
    auto t0 = digits::Clock::now();
    auto out = session.Run(Ort::RunOptions{nullptr}, in_names, &in, 1, out_names, 1);
    double us = digits::us_since(t0);
    st.add(us, digits::argmax(out[0].GetTensorData<float>(), 10) == test.labels[i]);
  }
  st.report(argc > 4 ? argv[4] : "onnxruntime_cpp", argv[1]);
  return 0;
} catch (const std::exception& e) {
  fprintf(stderr, "error: %s\n", e.what());
  return 1;
}
