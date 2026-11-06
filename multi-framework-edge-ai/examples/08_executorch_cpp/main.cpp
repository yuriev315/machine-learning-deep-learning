// ExecuTorch C++ Module API + XNNPACK. usage: et_digits model.pte digits_test.bin [route]
#include <cstdio>
#include <executorch/extension/module/module.h>
#include <executorch/extension/tensor/tensor.h>
#include <executorch/extension/threadpool/threadpool.h>
#include "digits.h"
using executorch::extension::Module;
using executorch::extension::from_blob;
using executorch::runtime::Error;
int main(int argc, char** argv) try {
  if (argc < 3) { fprintf(stderr, "usage: %s model.pte digits_test.bin [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  // The default pool has one thread per core. Under a CPU quota those threads spin and get throttled, which inflated
  // latency by 200x in one run here. Size it explicitly, as the other runtimes in this project do.
  executorch::extension::threadpool::get_threadpool()->_unsafe_reset_threadpool(1);
  Module module(argv[1]);
  if (module.load_forward() != Error::Ok) { fprintf(stderr, "load_forward failed\n"); return 1; }
  std::vector<float> input(test.h * test.w);
  auto tensor = from_blob(input.data(), {1, 1, int(test.h), int(test.w)});
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    std::copy_n(test.image(i), input.size(), input.begin());
    auto t0 = digits::Clock::now();
    auto r = module.forward(tensor);
    double us = digits::us_since(t0);
    if (!r.ok()) { fprintf(stderr, "forward failed: 0x%x\n", int(r.error())); return 1; }
    st.add(us, digits::argmax(r->at(0).toTensor().const_data_ptr<float>(), 10) == test.labels[i]);
  }
  st.report(argc > 3 ? argv[3] : "executorch_cpp", argv[1]);
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
