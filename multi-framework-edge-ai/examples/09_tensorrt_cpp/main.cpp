// SOURCE_ONLY: written against the TensorRT 10 API; never compiled or run here (no SDK, no NVIDIA GPU).
// Engine first: trtexec --onnx=tinycnn.onnx --saveEngine=tinycnn.engine --fp16
#include <NvInfer.h>
#include <cstdio>
#include <fstream>
#include <memory>
#include <vector>
#include "digits.h"
class Logger : public nvinfer1::ILogger {
  void log(Severity s, const char* m) noexcept override { if (s <= Severity::kWARNING) fprintf(stderr, "[TRT] %s\n", m); }
};
int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "usage: %s tinycnn.engine digits_test.bin\n", argv[0]); return 2; }
  auto test = digits::load(argv[2]);
  std::ifstream f(argv[1], std::ios::binary | std::ios::ate);
  std::vector<char> blob(size_t(f.tellg())); f.seekg(0); f.read(blob.data(), std::streamsize(blob.size()));
  Logger logger;
  std::unique_ptr<nvinfer1::IRuntime> rt(nvinfer1::createInferRuntime(logger));
  std::unique_ptr<nvinfer1::ICudaEngine> engine(rt->deserializeCudaEngine(blob.data(), blob.size()));
  if (!engine) { fprintf(stderr, "cannot load engine\n"); return 1; }
  std::unique_ptr<nvinfer1::IExecutionContext> ctx(engine->createExecutionContext());
  // Real code allocates these with cudaMalloc and copies with cudaMemcpy; see the official samples under official_examples/.
  fprintf(stderr, "engine loaded, %d tensors\n", engine->getNbIOTensors());
  return 0;
}
