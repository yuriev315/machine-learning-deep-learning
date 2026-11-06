// Project 17: frame source -> preprocessing -> inference -> postprocessing, as separate threads with a bounded "latest frame" queue.
// usage: realtime_camera model.onnx digits_test.bin --source=synthetic [--frames=N] [--fps=30]
//        realtime_camera model.onnx digits_test.bin --source=/dev/video0 [--frames=N]
// No real camera has ever been used. The V4L2 path is exercised by fake_v4l2.c, a user-space driver simulation. The synthetic source renders
// real digit images into 640x480 YUYV frames, so preprocessing and accuracy can be checked end to end.
#include <fcntl.h>
#include <linux/videodev2.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <onnxruntime_cxx_api.h>
#include <algorithm>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <mutex>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>
using Clock = std::chrono::steady_clock;
constexpr int kW = 640, kH = 480;
struct Frame { std::vector<uint8_t> yuyv; int label = -1; Clock::time_point captured; };
// Keep only the newest frame: a real-time pipeline drops frames instead of letting latency grow.
class LatestSlot {
 public:
  void put(Frame&& f) { std::lock_guard<std::mutex> l(m_); if (has_) ++dropped_; f_ = std::move(f); has_ = true; cv_.notify_one(); }
  bool take(Frame& f, std::atomic<bool>& done) {
    std::unique_lock<std::mutex> l(m_);
    cv_.wait_for(l, std::chrono::milliseconds(200), [&] { return has_ || done.load(); });
    if (!has_) return false;
    f = std::move(f_); has_ = false; return true;
  }
  long dropped() const { return dropped_; }
 private:
  std::mutex m_; std::condition_variable cv_; Frame f_; bool has_ = false; long dropped_ = 0;
};
struct TestSet { uint32_t n, h, w; std::vector<float> x; std::vector<uint8_t> y; };
static TestSet load(const std::string& p) {
  std::ifstream f(p, std::ios::binary); if (!f) throw std::runtime_error("cannot open " + p);
  TestSet t; f.read((char*)&t.n, 4); f.read((char*)&t.h, 4); f.read((char*)&t.w, 4);
  t.x.resize(size_t(t.n) * t.h * t.w); t.y.resize(t.n);
  f.read((char*)t.x.data(), std::streamsize(t.x.size() * 4)); f.read((char*)t.y.data(), t.n); return t;
}
// Draw one 8x8 digit, scaled up to the full frame height and centered, as luminance in a YUYV buffer.
static void render(const TestSet& t, size_t i, std::vector<uint8_t>& yuyv) {
  yuyv.assign(size_t(kW) * kH * 2, 128);
  const int cell = kH / 8, x0 = (kW - kH) / 2;
  for (int y = 0; y < kH; ++y) for (int x = 0; x < kW; ++x) {
    uint8_t lum = uint8_t(0.5f * 255);
    int gx = x - x0, r = y / cell, c = gx / cell;
    if (gx >= 0 && c < 8 && r < 8) lum = uint8_t(std::clamp((t.x[i * 64 + size_t(r) * 8 + size_t(c)] + 1.f) * 127.5f, 0.f, 255.f));
    yuyv[(size_t(y) * kW + size_t(x)) * 2] = lum;
  }
}
// Preprocess: center-crop a square from Y, area-average down to 8x8, normalize to [-1, 1].
static void preprocess(const std::vector<uint8_t>& yuyv, float* out) {
  const int cell = kH / 8, x0 = (kW - kH) / 2;
  for (int r = 0; r < 8; ++r) for (int c = 0; c < 8; ++c) {
    uint32_t sum = 0;
    for (int y = r * cell; y < (r + 1) * cell; ++y) for (int x = x0 + c * cell; x < x0 + (c + 1) * cell; ++x) sum += yuyv[(size_t(y) * kW + size_t(x)) * 2];
    out[r * 8 + c] = float(sum) / float(cell * cell) / 127.5f - 1.f;
  }
}
// Camera capture with V4L2 memory-mapped streaming. Tested only against the fake_v4l2.c simulation.
static void v4l2_loop(const std::string& dev, LatestSlot& slot, std::atomic<bool>& done, int max_frames, bool label_in_chroma) {
  int fd = open(dev.c_str(), O_RDWR); if (fd < 0) throw std::runtime_error("cannot open " + dev);
  v4l2_format fmt{}; fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE; fmt.fmt.pix.width = kW; fmt.fmt.pix.height = kH; fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_YUYV; fmt.fmt.pix.field = V4L2_FIELD_NONE;
  if (ioctl(fd, VIDIOC_S_FMT, &fmt) < 0) throw std::runtime_error("VIDIOC_S_FMT failed");
  if (fmt.fmt.pix.width != kW || fmt.fmt.pix.height != kH || fmt.fmt.pix.pixelformat != V4L2_PIX_FMT_YUYV) throw std::runtime_error("camera does not offer 640x480 YUYV");
  v4l2_requestbuffers rq{}; rq.count = 4; rq.type = V4L2_BUF_TYPE_VIDEO_CAPTURE; rq.memory = V4L2_MEMORY_MMAP;
  if (ioctl(fd, VIDIOC_REQBUFS, &rq) < 0) throw std::runtime_error("VIDIOC_REQBUFS failed");
  std::vector<void*> maps(rq.count); std::vector<size_t> lens(rq.count);
  for (uint32_t i = 0; i < rq.count; ++i) {
    v4l2_buffer b{}; b.type = rq.type; b.memory = rq.memory; b.index = i;
    if (ioctl(fd, VIDIOC_QUERYBUF, &b) < 0) throw std::runtime_error("VIDIOC_QUERYBUF failed");
    lens[i] = b.length; maps[i] = mmap(nullptr, b.length, PROT_READ | PROT_WRITE, MAP_SHARED, fd, b.m.offset);
    if (maps[i] == MAP_FAILED) throw std::runtime_error("mmap failed");
    if (ioctl(fd, VIDIOC_QBUF, &b) < 0) throw std::runtime_error("VIDIOC_QBUF failed");
  }
  int type = V4L2_BUF_TYPE_VIDEO_CAPTURE; if (ioctl(fd, VIDIOC_STREAMON, &type) < 0) throw std::runtime_error("VIDIOC_STREAMON failed");
  int captured = 0;
  while (!done) {
    v4l2_buffer b{}; b.type = V4L2_BUF_TYPE_VIDEO_CAPTURE; b.memory = V4L2_MEMORY_MMAP;
    if (ioctl(fd, VIDIOC_DQBUF, &b) < 0) throw std::runtime_error("VIDIOC_DQBUF failed");
    Frame f; f.captured = Clock::now(); auto* p = static_cast<uint8_t*>(maps[b.index]); f.yuyv.assign(p, p + b.bytesused);
    if (label_in_chroma) f.label = p[1];   // test hook: the simulated driver stores the ground truth in the first U byte
    slot.put(std::move(f));
    if (ioctl(fd, VIDIOC_QBUF, &b) < 0) throw std::runtime_error("VIDIOC_QBUF failed");
    if (max_frames > 0 && ++captured >= max_frames) break;
  }
  ioctl(fd, VIDIOC_STREAMOFF, &type);
  for (uint32_t i = 0; i < rq.count; ++i) munmap(maps[i], lens[i]);
  close(fd);
}
int main(int argc, char** argv) try {
  if (argc < 4) { fprintf(stderr, "usage: %s model.onnx digits_test.bin --source=synthetic|/dev/videoN [--frames=N] [--fps=N]\n", argv[0]); return 2; }
  std::string source = "synthetic"; int frames = 450, fps = 30; bool label_in_chroma = false;
  for (int i = 3; i < argc; ++i) { std::string a = argv[i]; if (a.rfind("--source=", 0) == 0) source = a.substr(9); else if (a.rfind("--frames=", 0) == 0) frames = std::stoi(a.substr(9)); else if (a.rfind("--fps=", 0) == 0) fps = std::stoi(a.substr(6)); else if (a == "--label-in-chroma") label_in_chroma = true; }
  auto test = load(argv[2]);
  Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "camera"); Ort::SessionOptions so; so.SetIntraOpNumThreads(1);
  Ort::Session sess(env, argv[1], so); Ort::AllocatorWithDefaultOptions al;
  auto in_n = sess.GetInputNameAllocated(0, al); auto out_n = sess.GetOutputNameAllocated(0, al);
  const char* inn[] = {in_n.get()}; const char* outn[] = {out_n.get()};
  LatestSlot slot; std::atomic<bool> done{false};
  std::thread cap([&] {
    if (source == "synthetic") {
      auto period = std::chrono::microseconds(1000000 / fps); auto next = Clock::now();
      for (int i = 0; i < frames; ++i) {
        Frame f; size_t k = size_t(i) % test.n; render(test, k, f.yuyv); f.label = test.y[k]; f.captured = Clock::now(); slot.put(std::move(f));
        next += period; std::this_thread::sleep_until(next);
      }
    } else {
      try { v4l2_loop(source, slot, done, frames, label_in_chroma); } catch (const std::exception& e) { fprintf(stderr, "camera error: %s\n", e.what()); }  // exceptions must not escape a thread
    }
    done = true;
  });
  std::array<int64_t, 4> shape{1, 1, 8, 8}; std::vector<float> in(64);
  auto mem = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
  Ort::Value tensor = Ort::Value::CreateTensor<float>(mem, in.data(), in.size(), shape.data(), shape.size());
  long n = 0, hit = 0, labeled = 0; std::vector<double> e2e, pre, inf;
  auto t0 = Clock::now();
  Frame f;
  while (slot.take(f, done) || !done) {
    if (f.yuyv.empty()) continue;
    auto a = Clock::now(); preprocess(f.yuyv, in.data()); auto b = Clock::now();
    auto out = sess.Run(Ort::RunOptions{nullptr}, inn, &tensor, 1, outn, 1); auto c = Clock::now();
    const float* o = out[0].GetTensorData<float>(); int pred = int(std::max_element(o, o + 10) - o);     // postprocess: top-1
    if (f.label >= 0) { ++labeled; hit += pred == f.label; }
    pre.push_back(std::chrono::duration<double, std::micro>(b - a).count()); inf.push_back(std::chrono::duration<double, std::micro>(c - b).count());
    e2e.push_back(std::chrono::duration<double, std::micro>(c - f.captured).count()); ++n; f.yuyv.clear();
  }
  cap.join();
  auto p95 = [](std::vector<double> v) { if (v.empty()) return 0.0; std::sort(v.begin(), v.end()); return v[size_t(double(v.size()) * .95)]; };
  double wall = std::chrono::duration<double>(Clock::now() - t0).count();
  printf("CAMERA source=%s processed=%ld dropped=%ld fps=%.1f preprocess_p95_us=%.0f infer_p95_us=%.0f end_to_end_p95_us=%.0f accuracy=%.4f\n", source.c_str(), n, slot.dropped(), double(n) / wall, p95(pre), p95(inf), p95(e2e), labeled ? double(hit) / double(labeled) : -1.0);
  return n > 0 ? 0 : 1;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
