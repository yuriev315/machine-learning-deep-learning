// ncnn C++. usage: ncnn_digits model.param model.bin digits_test.bin in_blob out_blob [threads] [route]
#include <cstdio>
#include <cstdlib>
#include <net.h>
#if NCNN_VULKAN
#include <gpu.h>
#endif
#include "digits.h"
int main(int argc, char** argv) try {
  if (argc < 6) { fprintf(stderr, "usage: %s model.param model.bin digits_test.bin in_blob out_blob [threads] [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[3]);
  ncnn::Net net;
  net.opt.num_threads = argc > 6 ? atoi(argv[6]) : 1;
  // MFEA_NCNN_VULKAN=1 runs the GPU compute path. Here that means Mesa lavapipe, a software Vulkan driver: it exercises the shaders, not a real GPU.
  const char* vk = getenv("MFEA_NCNN_VULKAN");
#if NCNN_VULKAN
  net.opt.use_vulkan_compute = vk && vk[0] == '1';
  if (net.opt.use_vulkan_compute) { if (ncnn::get_gpu_count() == 0) { fprintf(stderr, "no Vulkan device\n"); return 1; } fprintf(stderr, "Vulkan device: %s\n", ncnn::get_gpu_info(ncnn::get_default_gpu_index()).device_name()); }
#else
  if (vk && vk[0] == '1') { fprintf(stderr, "built without Vulkan\n"); return 1; }
#endif
  if (net.load_param(argv[1]) != 0) { fprintf(stderr, "load_param failed\n"); return 1; }
  if (net.load_model(argv[2]) != 0) { fprintf(stderr, "load_model failed\n"); return 1; }
  digits::Stats st;
  for (uint32_t i = 0; i < test.n; ++i) {
    // ncnn::Mat(w, h, c, data) wraps the buffer without copying; clone so the network owns its input.
    ncnn::Mat in = ncnn::Mat(int(test.w), int(test.h), 1, (void*)test.image(i), 4u).clone();  // 3-dim: w, h, channels
    auto t0 = digits::Clock::now();
    ncnn::Extractor ex = net.create_extractor();
    if (ex.input(argv[4], in) != 0) { fprintf(stderr, "bad input blob %s\n", argv[4]); return 1; }
    ncnn::Mat out;
    if (ex.extract(argv[5], out) != 0) { fprintf(stderr, "bad output blob %s\n", argv[5]); return 1; }
    double us = digits::us_since(t0);
    st.add(us, digits::argmax((const float*)out, out.w) == test.labels[i]);
  }
  st.report(argc > 7 ? argv[7] : "ncnn_cpp", argv[2]);
  return 0;
} catch (const std::exception& e) {
  fprintf(stderr, "error: %s\n", e.what());
  return 1;
}
