// TFLite Micro: arena-based, no dynamic allocation after setup. Accuracy over the shared test set.
#include <cmath>
#include <cstdio>
#include "digits.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
#include "tensorflow/lite/schema/schema_generated.h"
extern const unsigned char g_model[];
extern const unsigned int g_model_len;
int main(int argc, char** argv) try {
  if (argc < 2) { fprintf(stderr, "usage: %s digits_test.bin\n", argv[0]); return 2; }
  auto test = digits::load(argv[1]);
  const tflite::Model* model = tflite::GetModel(g_model);
  tflite::MicroMutableOpResolver<8> ops;
  ops.AddConv2D(); ops.AddDepthwiseConv2D(); ops.AddMaxPool2D(); ops.AddFullyConnected(); ops.AddReshape(); ops.AddQuantize(); ops.AddDequantize(); ops.AddSoftmax();
  alignas(16) static uint8_t arena[16 * 1024];
  tflite::MicroInterpreter ip(model, ops, arena, sizeof(arena));
  if (ip.AllocateTensors() != kTfLiteOk) { fprintf(stderr, "AllocateTensors failed\n"); return 1; }
  TfLiteTensor* in = ip.input(0); TfLiteTensor* out = ip.output(0);
  digits::Stats st;
  const size_t px = test.h * test.w;
  for (uint32_t i = 0; i < test.n; ++i) {
    const float* x = test.image(i);
    for (size_t p = 0; p < px; ++p) {
      int v = int(std::lround(x[p] / in->params.scale)) + in->params.zero_point;
      if (in->type == kTfLiteUInt8) in->data.uint8[p] = uint8_t(std::min(255, std::max(0, v)));
      else in->data.int8[p] = int8_t(std::min(127, std::max(-128, v)));
    }
    auto t0 = digits::Clock::now();
    if (ip.Invoke() != kTfLiteOk) { fprintf(stderr, "Invoke failed\n"); return 1; }
    double us = digits::us_since(t0);
    int pred = out->type == kTfLiteUInt8 ? digits::argmax(out->data.uint8, 10) : digits::argmax(out->data.int8, 10);
    st.add(us, pred == test.labels[i]);
  }
  fprintf(stderr, "arena used: %zu bytes\n", ip.arena_used_bytes());
  st.report(argc > 2 ? argv[2] : "tf_tflm_int8", "");
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "%s\n", e.what()); return 1; }
