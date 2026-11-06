# 部署学习与设计指南

流程：模型导出与量化 → 推理服务 → API → 容器与环境 → 并发和延迟测试 → 日志与监控 → 灰度与回滚。

本指南不提供具体配置、硬件预算或性能承诺。文献中的速度、显存与成本数字，都依附于各自的模型、硬件与负载，引用时须同时说明实验条件。

小语种部署有两个特有问题，每一步都要单独检查：
- 压缩后目标语言能力是否保持；
- 分词膨胀带来的成本与延迟差异。

## 1. 模型导出与量化（输入：适配后的模型；产出：量化模型 + 目标语言回归报告）

- 量化对多语言能力的影响（直接相关，优先阅读）：
  - 〔LRL-P-16-001〕How Does Quantization Affect Multilingual LLMs?
  - 〔LRL-P-16-003〕训练后量化对机器翻译的不均衡影响。
  - 〔LRL-P-16-002〕用多语言校准数据改进量化。
- 剪枝与蒸馏：
  - 〔LRL-P-16-009〕面向特定语言剪枝的局限。
  - 〔LRL-P-16-011〕Multilingual Brain Surgeon。
  - 〔LRL-P-16-020〕Bielik-Minitron（波兰语）。
  - 〔LRL-P-16-019〕蒸馏与量化的隐藏成本（翻译）。
- 通用量化方法（通用支撑，经典补充）：
  - 〔LRL-P-16-060〕GPTQ。
  - 〔LRL-P-16-061〕AWQ。
- 工程：
  - 〔LRL-E-31〕llm-compressor。
  - 〔LRL-E-29〕llama.cpp（GGUF 量化与本地推理）。

检查项：
- 量化校准数据是否包含目标语言。
- 量化前后，在目标语言与原有语言上的回归评测（见 evaluation_cn.md 第 8 节）。

## 2. 推理服务、批处理与 KV 缓存

- 通用服务系统（通用支撑）：
  - 〔LRL-P-16-059〕PagedAttention/vLLM（经典补充）。
  - 〔LRL-P-16-038〕SGLang。
- 推测解码与多语言：
  - 〔LRL-P-16-029〕多语言推测解码与专用草稿模型。
  - 〔LRL-P-16-030〕推测解码中的“多语言诅咒”。
  - 〔LRL-P-16-031〕波兰语模型的跨家族推测解码。
  - 〔LRL-P-16-037〕EAGLE（通用支撑）。
- 工程：
  - 〔LRL-E-28〕vLLM。
  - 〔LRL-E-30〕SGLang。
  - 〔LRL-E-29〕llama.cpp。

库内缺口：
- KV 缓存与服务调度方面缺少针对多语言的专门研究，现只能用通用论文支撑。

## 3. API、流式输出与容器环境

- vLLM、SGLang 的 OpenAI 兼容服务器与流式输出实现，见其文档集：
  - 〔LRL-E-28〕。
  - 〔LRL-E-30〕。
  - 两者的文档集都已完整保存，路径见 catalog 的“本地路径”列。
- 系统课程：
  - 〔LRL-C-17-010〕CMU 11-868 LLM Systems。
  - 〔LRL-C-17-013〕CMU 15-442 ML Systems。
  - 〔LRL-C-17-062〕CMU 15-779。

## 4. 并发、延迟与成本测试

- 分词带来的成本与延迟差异，是小语种特有的问题：
  - 〔LRL-P-16-033〕The Script Tax。
  - 〔LRL-P-16-034〕分词溢价成本审计。
  - 〔LRL-P-16-035〕Token 成本账本。
  - 〔LRL-P-06-002〕非洲语言税。
- 韩语场景的 token 剪枝：〔LRL-P-16-067〕。

建议：
- 压测负载使用真实的目标语言请求分布。
- 分语言报告每请求 token 数、首 token 延迟与吞吐。

## 5. 日志、监控与成本统计

- 工程：
  - 〔LRL-E-36〕Prometheus。
  - 〔LRL-E-37〕OpenTelemetry Python。
  - 〔LRL-E-38〕Langfuse：LLM 调用追踪与成本统计。注意其 ee/ 目录为商业许可。
- 建议：
  - 监控指标按语言分组。
  - 记录检索命中、工具调用成功率，以及安全过滤的触发情况。

## 6. 灰度发布与回滚

- 工程：〔LRL-E-39〕Argo Rollouts：金丝雀与蓝绿发布，文档集完整。
- 建议：
  - 新模型或量化版本先在小流量上，与旧版本对比目标语言质量指标与安全指标。
  - 保留可立即回滚的旧版本。

## 7. 训练侧的分布式与检查点（如需自行训练）

- 通用支撑（经典补充）：
  - 〔LRL-P-16-057〕ZeRO。
  - 〔LRL-P-16-058〕Megatron-LM。
- 大规模训练经验：〔LRL-P-16-027〕OpenGPT-X 在 HPC 上训练的最佳实践。
- 工程：
  - 〔LRL-E-14〕Megatron-LM。
  - 〔LRL-E-15〕DeepSpeed。
  - 〔LRL-E-16〕torchtitan。
  - 〔LRL-E-17〕accelerate。
- 书：
  - 〔LRL-B-18-049〕How to Scale Your Model。
  - 〔LRL-B-18-050〕The Ultra-Scale Playbook。
  - 〔LRL-B-18-053〕Machine Learning Engineering Open Book。

## 推荐学习顺序

1. 课程：
   - 〔LRL-C-17-061〕MIT 6.5940 EfficientML。
   - 〔LRL-C-17-010〕CMU 11-868。
   - 〔LRL-C-17-064〕Cornell CS4787。
2. 书：
   - 〔LRL-B-18-051〕Introduction to ML Systems。
   - 〔LRL-B-18-052〕Scaling ML Systems。
3. 论文：〔LRL-P-16-001〕→〔LRL-P-16-033〕→〔LRL-P-16-059〕→〔LRL-P-16-030〕。
