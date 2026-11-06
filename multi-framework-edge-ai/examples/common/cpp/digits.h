// Shared evaluation helpers for every C++ route: test-set loading, timing, peak memory, result line.
#pragma once
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>
#if defined(__linux__)
#include <sys/resource.h>
#endif
namespace digits {
struct TestSet {
  uint32_t n = 0, h = 0, w = 0;
  std::vector<float> images;     // n * h * w, single channel, range [-1, 1]
  std::vector<uint8_t> labels;   // n
  const float* image(size_t i) const { return images.data() + i * h * w; }
};
inline TestSet load(const std::string& path) {
  std::ifstream f(path, std::ios::binary);
  if (!f) throw std::runtime_error("cannot open test set: " + path);
  TestSet t;
  f.read(reinterpret_cast<char*>(&t.n), 4);
  f.read(reinterpret_cast<char*>(&t.h), 4);
  f.read(reinterpret_cast<char*>(&t.w), 4);
  t.images.resize(size_t(t.n) * t.h * t.w);
  t.labels.resize(t.n);
  f.read(reinterpret_cast<char*>(t.images.data()), std::streamsize(t.images.size() * sizeof(float)));
  f.read(reinterpret_cast<char*>(t.labels.data()), t.n);
  if (!f) throw std::runtime_error("truncated test set: " + path);
  return t;
}
inline size_t file_size(const std::string& p) {
  std::ifstream f(p, std::ios::binary | std::ios::ate);
  return f ? size_t(f.tellg()) : 0;
}
inline long peak_rss_kb() {
#if defined(__linux__)
  rusage r{};
  getrusage(RUSAGE_SELF, &r);
  return r.ru_maxrss;
#else
  return -1;
#endif
}
template <class T> inline int argmax(const T* v, int n) { return int(std::max_element(v, v + n) - v); }
class Stats {
 public:
  void add(double us, bool hit) { lat_.push_back(us); hits_ += hit; }
  // One machine-readable line; scripts/record_result.py collects it into runtime_test_results.csv.
  void report(const char* route, const std::string& model) {
    std::sort(lat_.begin(), lat_.end());
    double sum = 0; for (double v : lat_) sum += v;
    printf("RESULT {\"route\":\"%s\",\"n\":%zu,\"accuracy\":%.4f,\"latency_mean_us\":%.2f,\"latency_p95_us\":%.2f,"
           "\"peak_rss_kb\":%ld,\"model_bytes\":%zu}\n", route, lat_.size(), double(hits_) / double(lat_.size()),
           sum / double(lat_.size()), lat_[size_t(double(lat_.size()) * 0.95)], peak_rss_kb(), file_size(model));
  }
 private:
  std::vector<double> lat_; size_t hits_ = 0;
};
using Clock = std::chrono::steady_clock;
inline double us_since(Clock::time_point t0) { return std::chrono::duration<double, std::micro>(Clock::now() - t0).count(); }
}  // namespace digits
