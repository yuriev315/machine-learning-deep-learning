// Minimal GGUF inference with the llama.cpp C API: tokenize, decode, greedy sample. usage: llm_gguf model.gguf "prompt" [n_predict]
#include <llama.h>
#include <chrono>
#include <cstdio>
#include <string>
#include <vector>
int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "usage: %s model.gguf prompt [n]\n", argv[0]); return 2; }
  const int n_predict = argc > 3 ? atoi(argv[3]) : 40;
  llama_log_set([](ggml_log_level, const char*, void*) {}, nullptr);
  llama_backend_init();
  auto mp = llama_model_default_params(); mp.n_gpu_layers = 0;
  llama_model* model = llama_model_load_from_file(argv[1], mp);
  if (!model) { fprintf(stderr, "cannot load model\n"); return 1; }
  const llama_vocab* vocab = llama_model_get_vocab(model);
  std::string prompt = argv[2];
  std::vector<llama_token> toks(prompt.size() + 8);
  int n = llama_tokenize(vocab, prompt.c_str(), int32_t(prompt.size()), toks.data(), int32_t(toks.size()), true, false);
  if (n < 0) { fprintf(stderr, "tokenize failed\n"); return 1; }
  toks.resize(n);
  auto cp = llama_context_default_params(); cp.n_ctx = n + n_predict + 4; cp.n_batch = cp.n_ctx; cp.n_threads = 2; cp.n_threads_batch = 2;
  llama_context* ctx = llama_init_from_model(model, cp);
  if (!ctx) { fprintf(stderr, "cannot create context\n"); return 1; }
  llama_sampler* smpl = llama_sampler_chain_init(llama_sampler_chain_default_params());
  llama_sampler_chain_add(smpl, llama_sampler_init_greedy());
  printf("%s", prompt.c_str());
  llama_batch batch = llama_batch_get_one(toks.data(), int32_t(toks.size()));
  int made = 0; auto t0 = std::chrono::steady_clock::now();
  llama_token tok;
  for (; made < n_predict; ++made) {
    if (llama_decode(ctx, batch) != 0) { fprintf(stderr, "decode failed\n"); return 1; }
    tok = llama_sampler_sample(smpl, ctx, -1);
    if (llama_vocab_is_eog(vocab, tok)) break;
    char buf[128]; int l = llama_token_to_piece(vocab, tok, buf, sizeof(buf), 0, true);
    if (l > 0) fwrite(buf, 1, size_t(l), stdout);
    batch = llama_batch_get_one(&tok, 1);
  }
  double s = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
  printf("\nLLM tokens=%d tok_per_s=%.1f\n", made, made / s);
  llama_sampler_free(smpl); llama_free(ctx); llama_model_free(model); llama_backend_free();
  return made > 0 ? 0 : 1;
}
