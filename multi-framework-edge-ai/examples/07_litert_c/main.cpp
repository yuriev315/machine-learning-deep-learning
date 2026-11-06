// LiteRT / TFLite through the stable C API. Handles float and uint8/int8 quantized models.
// usage: litert_digits model.tflite digits_test.bin [threads] [route-name]
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include "digits.h"
#include "tensorflow/lite/c/c_api.h"
#define CHECK_TFL(x) do { if ((x) != kTfLiteOk) { fprintf(stderr, "TFLite call failed: %s\n", #x); return 1; } } while (0)
int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "usage: %s model.tflite digits_test.bin [threads] [route]\n", argv[0]); return 2; }
  digits::TestSet test;
  try { test = digits::load(argv[2]); } catch (const std::exception& e) { fprintf(stderr, "%s\n", e.what()); return 1; }
  TfLiteModel* model = TfLiteModelCreateFromFile(argv[1]);
  if (!model) { fprintf(stderr, "cannot load model %s\n", argv[1]); return 1; }
  TfLiteInterpreterOptions* opt = TfLiteInterpreterOptionsCreate();
  TfLiteInterpreterOptionsSetNumThreads(opt, argc > 3 ? atoi(argv[3]) : 1);
  TfLiteInterpreter* ip = TfLiteInterpreterCreate(model, opt);
  if (!ip) { fprintf(stderr, "cannot create interpreter\n"); return 1; }
  CHECK_TFL(TfLiteInterpreterAllocateTensors(ip));
  TfLiteTensor* in = TfLiteInterpreterGetInputTensor(ip, 0);
  const TfLiteTensor* out = TfLiteInterpreterGetOutputTensor(ip, 0);
  const TfLiteType it = TfLiteTensorType(in), ot = TfLiteTensorType(out);
  const TfLiteQuantizationParams iq = TfLiteTensorQuantizationParams(in);
  const size_t pixels = test.h * test.w;   // NHWC with one channel: same memory order as the source image
  std::vector<float> fbuf(10); std::vector<uint8_t> ibuf(pixels), obuf(10);
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    const float* x = test.image(i);
    if (it == kTfLiteFloat32) {
      CHECK_TFL(TfLiteTensorCopyFromBuffer(in, x, pixels * sizeof(float)));
    } else {
      for (size_t p = 0; p < pixels; ++p) {
        int v = int(std::lround(x[p] / iq.scale)) + iq.zero_point;
        ibuf[p] = (it == kTfLiteUInt8) ? uint8_t(std::min(255, std::max(0, v))) : uint8_t(int8_t(std::min(127, std::max(-128, v))));
      }
      CHECK_TFL(TfLiteTensorCopyFromBuffer(in, ibuf.data(), pixels));
    }
    auto t0 = digits::Clock::now();
    CHECK_TFL(TfLiteInterpreterInvoke(ip));
    double us = digits::us_since(t0);
    int pred;
    if (ot == kTfLiteFloat32) { CHECK_TFL(TfLiteTensorCopyToBuffer(out, fbuf.data(), 10 * sizeof(float))); pred = digits::argmax(fbuf.data(), 10); }
    else if (ot == kTfLiteUInt8) { CHECK_TFL(TfLiteTensorCopyToBuffer(out, obuf.data(), 10)); pred = digits::argmax(obuf.data(), 10); }
    else { CHECK_TFL(TfLiteTensorCopyToBuffer(out, obuf.data(), 10)); pred = digits::argmax(reinterpret_cast<int8_t*>(obuf.data()), 10); }
    st.add(us, pred == test.labels[i]);
  }
  st.report(argc > 4 ? argv[4] : "litert_c_api", argv[1]);
  TfLiteInterpreterDelete(ip); TfLiteInterpreterOptionsDelete(opt); TfLiteModelDelete(model);
  return 0;
}
