// ONNX Runtime with the QNN execution provider, targeting the Hexagon NPU through libQnnHtp.so.
// Compiles against the standard SDK, but only a QNN-enabled ORT build on a Snapdragon device can run it. It has never been run.
#include <onnxruntime_cxx_api.h>
#include <array>
#include <cstdio>
#include <string>
#include <unordered_map>
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model_int8_qdq.onnx digits_test.bin [libQnnHtp.so]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "qnn"); Ort::SessionOptions so;
  std::unordered_map<std::string, std::string> opts{{"backend_path", argc > 3 ? argv[3] : "libQnnHtp.so"}, {"htp_performance_mode", "burst"}};
  so.AppendExecutionProvider("QNN", opts);
  so.AddConfigEntry("session.disable_cpu_ep_fallback", "1");   // fail rather than silently run on the CPU
  Ort::Session s(env, argv[1], so);
  Ort::AllocatorWithDefaultOptions al; auto i = s.GetInputNameAllocated(0, al); auto o = s.GetOutputNameAllocated(0, al);
  const char* in[] = {i.get()}; const char* out[] = {o.get()};
  std::array<int64_t, 4> shape{1, 1, 8, 8}; std::vector<float> x(64);
  auto mem = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
  Ort::Value t = Ort::Value::CreateTensor<float>(mem, x.data(), x.size(), shape.data(), shape.size());
  digits::Stats st;
  for (uint32_t n = 0; n < test.n; ++n) {
    std::copy_n(test.image(n), 64, x.begin());
    auto t0 = digits::Clock::now(); auto r = s.Run(Ort::RunOptions{nullptr}, in, &t, 1, out, 1); double us = digits::us_since(t0);
    st.add(us, digits::argmax(r[0].GetTensorData<float>(), 10) == test.labels[n]);
  }
  st.report("pytorch_onnx_qnn_htp", argv[1]);
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
