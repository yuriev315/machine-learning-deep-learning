// MNN session API. usage: mnn_digits model.mnn digits_test.bin [threads] [route]
#include <MNN/Interpreter.hpp>
#include <MNN/Tensor.hpp>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.mnn digits_test.bin [threads] [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  std::shared_ptr<MNN::Interpreter> net(MNN::Interpreter::createFromFile(argv[1]));
  if (!net) { fprintf(stderr, "cannot load model\n"); return 1; }
  MNN::ScheduleConfig cfg; cfg.type = MNN_FORWARD_CPU; cfg.numThread = argc > 3 ? atoi(argv[3]) : 1;
  auto* session = net->createSession(cfg);
  if (!session) { fprintf(stderr, "cannot create session\n"); return 1; }
  auto* in = net->getSessionInput(session, nullptr);
  // Models from TensorFlow keep NHWC, models from ONNX use NCHW. Ask the model instead of assuming.
  const bool nhwc = in->getDimensionType() == MNN::Tensor::TENSORFLOW;
  if (nhwc) net->resizeTensor(in, {1, int(test.h), int(test.w), 1}); else net->resizeTensor(in, {1, 1, int(test.h), int(test.w)});
  net->resizeSession(session);
  // Host-side tensor in the model's own layout; MNN converts to its internal NC4HW4.
  std::unique_ptr<MNN::Tensor> host(new MNN::Tensor(in, nhwc ? MNN::Tensor::TENSORFLOW : MNN::Tensor::CAFFE));
  auto* out = net->getSessionOutput(session, nullptr);
  std::unique_ptr<MNN::Tensor> ohost(new MNN::Tensor(out, nhwc ? MNN::Tensor::TENSORFLOW : MNN::Tensor::CAFFE));
  const size_t bytes = test.h * test.w * sizeof(float);
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::memcpy(host->host<float>(), test.image(i), bytes);
    auto t0 = digits::Clock::now();
    in->copyFromHostTensor(host.get());
    if (net->runSession(session) != MNN::NO_ERROR) { fprintf(stderr, "runSession failed\n"); return 1; }
    out->copyToHostTensor(ohost.get());
    double us = digits::us_since(t0);
    st.add(us, digits::argmax(ohost->host<float>(), 10) == test.labels[i]);
  }
  st.report(argc > 4 ? argv[4] : "mnn_cpp", argv[1]);
  return 0;
} catch (const std::exception& e) {
  fprintf(stderr, "error: %s\n", e.what());
  return 1;
}
