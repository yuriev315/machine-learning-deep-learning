# 部署学习与设计指南

流程：模型导出与量化 → 推理服务 → API → 容器与环境 → 并发和延迟测试 → 日志与监控 → 灰度与回滚。

本指南不提供具体配置、硬件预算或性能承诺。文献中的速度、显存与成本数字，都依附于各自的模型、硬件与负载，引用时须同时说明实验条件。

小语种部署有两个特有问题，每一步都要单独检查：
- 压缩后目标语言能力是否保持；
- 分词膨胀带来的成本与延迟差异。

## 1. 模型导出与量化（输入：适配后的模型；产出：量化模型 + 目标语言回归报告）

- 量化对多语言能力的影响（直接相关，优先阅读）：
  - [LRL-P-16-001｜How Does Quantization Affect Multilingual LLMs?](../papers/2024_Marchisio_HowDoesQuantizationAffect_en.pdf)How Does Quantization Affect Multilingual LLMs?
  - [LRL-P-16-003｜The Uneven Impact of Post-Training Quantization in Machine Translation](../papers/2025_Marie_UnevenImpactPostTraining_en.pdf)训练后量化对机器翻译的不均衡影响。
  - [LRL-P-16-002｜Calibrating Beyond English: Language Diversity for Better Quantized Mu](../papers/2026_Chimoto_CalibratingBeyondEnglish_en.pdf)用多语言校准数据改进量化。
- 剪枝与蒸馏：
  - [LRL-P-16-009｜On the Limitations of Language Targeted Pruning: Investigating the Cal](../papers/2024_Kurz_LimitationsLanguageTargeted_en.pdf)面向特定语言剪枝的局限。
  - [LRL-P-16-011｜Multilingual Brain Surgeon: Large Language Models Can be Compressed Le](../papers/2024_Zeng_MultilingualBrainSurgeon_en.pdf)Multilingual Brain Surgeon。
  - [LRL-P-16-020｜Bielik-Minitron-7B: Compressing Large Language Models via Structured P](../papers/2026_Kinas_BielikMinitron7B_en.pdf)Bielik-Minitron（波兰语）。
  - [LRL-P-16-019｜The Hidden Costs of Translation Accuracy: Distillation, Quantization,](../papers/2025_Vijay_HiddenCostsTranslationAccuracy_en.pdf)蒸馏与量化的隐藏成本（翻译）。
- 通用量化方法（通用支撑，经典补充）：
  - [LRL-P-16-060｜GPTQ: Accurate Post-Training Quantization for Generative Pre-trained T](../papers/2022_Frantar_GPTQ_en.pdf)GPTQ。
  - [LRL-P-16-061｜AWQ: Activation-aware Weight Quantization for LLM Compression and Acce](../papers/2023_Lin_AWQ_en.pdf)AWQ。
- 工程：
  - [LRL-E-31｜llm-compressor](../reference_code/llm-compressor_04546e0_original_en.tar.gz)llm-compressor。
  - [LRL-E-29｜llama.cpp](../reference_code/llamacpp_8642541_original_en.tar.gz)llama.cpp（GGUF 量化与本地推理）。

检查项：
- 量化校准数据是否包含目标语言。
- 量化前后，在目标语言与原有语言上的回归评测（见 evaluation_cn.md 第 8 节）。

## 2. 推理服务、批处理与 KV 缓存

- 通用服务系统（通用支撑）：
  - [LRL-P-16-059｜Efficient Memory Management for Large Language Model Serving with Page](../papers/2023_Kwon_EfficientMemoryManagement_en.pdf)PagedAttention/vLLM（经典补充）。
  - [LRL-P-16-038｜SGLang: Efficient Execution of Structured Language Model Programs](../papers/2023_Zheng_SGLang_en.pdf)SGLang。
- 推测解码与多语言：
  - [LRL-P-16-029｜Towards Fast Multilingual LLM Inference: Speculative Decoding and Spec](../papers/2024_Yi_FastMultilingualLLMInference_en.pdf)多语言推测解码与专用草稿模型。
  - [LRL-P-16-030｜Speculative Decoding and the Curse of Multilinguality](../papers/2026_Paudel_SpeculativeDecodingCurse_en.pdf)推测解码中的“多语言诅咒”。
  - [LRL-P-16-031｜Cross-Family Speculative Decoding for Polish Language Models on Apple~](../papers/2026_Fonal_CrossFamilySpeculativeDecoding_en.pdf)波兰语模型的跨家族推测解码。
  - [LRL-P-16-037｜EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](../papers/2024_Li_EAGLE_en.pdf)EAGLE（通用支撑）。
- 工程：
  - [LRL-E-28｜vllm](../reference_code/vllm_5df63a7_original_en.tar.gz)vLLM。
  - [LRL-E-30｜sglang](../reference_code/sglang_baa9bef_original_en.tar.gz)SGLang。
  - [LRL-E-29｜llama.cpp](../reference_code/llamacpp_8642541_original_en.tar.gz)llama.cpp。

库内缺口：
- KV 缓存与服务调度方面缺少针对多语言的专门研究，现只能用通用论文支撑。

## 3. API、流式输出与容器环境

- vLLM、SGLang 的 OpenAI 兼容服务器与流式输出实现，见其文档集：
  - [LRL-E-28｜vllm](../reference_code/vllm_5df63a7_original_en.tar.gz)。
  - [LRL-E-30｜sglang](../reference_code/sglang_baa9bef_original_en.tar.gz)。
  - 两者的文档集都已完整保存，路径见 catalog 的“本地路径”列。
- 系统课程：
  - [LRL-C-17-010｜Large Language Model Systems](../university_materials/CMU_11-868_LLMSystems_2026Spring_LectureMaterials_en)CMU 11-868 LLM Systems。
  - [LRL-C-17-013｜Machine Learning Systems](../university_materials/CMU_15-442_MLSystems_2026Spring_LectureMaterials_en)CMU 15-442 ML Systems。
  - [LRL-C-17-062｜Advanced Topics in Machine Learning Systems (LLM Edition)](../university_materials/CMU_15-779_MLSysLLM_2025Fall_LectureMaterials_en)CMU 15-779。

## 4. 并发、延迟与成本测试

- 分词带来的成本与延迟差异，是小语种特有的问题：
  - [LRL-P-16-033｜The Script Tax: Measuring Tokenization-Driven Efficiency and Latency D](../papers/2026_Dixit_TheScriptTax_en.pdf)The Script Tax。
  - [LRL-P-16-034｜Measuring the Tokenization Premium: A Cost Audit for Underserved Langu](../papers/2026_Roy_MeasuringTokenizationPremium_en.pdf)分词溢价成本审计。
  - [LRL-P-16-035｜Removable and Irreducible: A Token-Cost Ledger for the Multilingual To](../papers/2026_Mandarapu_RemovableAndIrreducible_en.pdf)Token 成本账本。
  - [LRL-P-06-002｜The African Language Tax: Quantifying the Cost, Latency, and Context P](../papers/2026_Somide_TheAfricanLanguageTax_en.pdf)非洲语言税。
- 韩语场景的 token 剪枝：[LRL-P-16-067｜Optimizing Korean-Centric LLMs via Token Pruning](../papers/2026_Kim_OptimizingKoreanCentricLLMs_en.pdf)。

建议：
- 压测负载使用真实的目标语言请求分布。
- 分语言报告每请求 token 数、首 token 延迟与吞吐。

## 5. 日志、监控与成本统计

- 工程：
  - [LRL-E-36｜prometheus](../reference_code/prometheus_bae3ece_original_en.tar.gz)Prometheus。
  - [LRL-E-37｜opentelemetry-python](../reference_code/opentelemetry-python_14971ce_original_en.tar.gz)OpenTelemetry Python。
  - [LRL-E-38｜langfuse](../reference_code/langfuse_d89f49b_original_en.tar.gz)Langfuse：LLM 调用追踪与成本统计。注意其 ee/ 目录为商业许可。
- 建议：
  - 监控指标按语言分组。
  - 记录检索命中、工具调用成功率，以及安全过滤的触发情况。

## 6. 灰度发布与回滚

- 工程：[LRL-E-39｜argo-rollouts](../reference_code/argo-rollouts_356117c_original_en.tar.gz)Argo Rollouts：金丝雀与蓝绿发布，文档集完整。
- 建议：
  - 新模型或量化版本先在小流量上，与旧版本对比目标语言质量指标与安全指标。
  - 保留可立即回滚的旧版本。

## 7. 训练侧的分布式与检查点（如需自行训练）

- 通用支撑（经典补充）：
  - [LRL-P-16-057｜ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](../papers/2019_Rajbhandari_ZeRO_en.pdf)ZeRO。
  - [LRL-P-16-058｜Efficient Large-Scale Language Model Training on GPU Clusters Using Me](../papers/2021_Narayanan_EfficientLargeScaleLanguage_en.pdf)Megatron-LM。
- 大规模训练经验：[LRL-P-16-027｜Training LLMs on HPC Systems: Best Practices from the OpenGPT-X Projec](../papers/2025_Penke_TrainingLLMsHPCSystemsBest_en.pdf)OpenGPT-X 在 HPC 上训练的最佳实践。
- 工程：
  - [LRL-E-14｜Megatron-LM](../reference_code/Megatron-LM_4b4acac_original_en.tar.gz)Megatron-LM。
  - [LRL-E-15｜DeepSpeed](../reference_code/DeepSpeed_0eb3a8b_original_en.tar.gz)DeepSpeed。
  - [LRL-E-16｜torchtitan](../reference_code/torchtitan_45e33cd_original_en.tar.gz)torchtitan。
  - [LRL-E-17｜accelerate](../reference_code/accelerate_6afc1e5_original_en.tar.gz)accelerate。
- 书：
  - [LRL-B-18-049｜How to Scale Your Model](../books/Austin_HowToScaleYourModel_2025_html_en)How to Scale Your Model。
  - [LRL-B-18-050｜The Ultra-Scale Playbook: Training LLMs on GPU Clusters](../books/Tazi_UltraScalePlaybook_2025_en.pdf)The Ultra-Scale Playbook。
  - [LRL-B-18-053｜Machine Learning Engineering Open Book](../books/Bekman_MachineLearningEngineeringOpenBook_2026_en.pdf)Machine Learning Engineering Open Book。

## 推荐学习顺序

1. 课程：
   - [LRL-C-17-061｜TinyML and Efficient Deep Learning Computing](../university_materials/MIT_6.5940_EfficientML_2024Fall_LectureMaterials_en)MIT 6.5940 EfficientML。
   - [LRL-C-17-010｜Large Language Model Systems](../university_materials/CMU_11-868_LLMSystems_2026Spring_LectureMaterials_en)CMU 11-868。
   - [LRL-C-17-064｜Principles of Large-Scale Machine Learning Systems](../university_materials/Cornell_CS4787_LargeScaleML_2025Fall_LectureMaterials_en)Cornell CS4787。
2. 书：
   - [LRL-B-18-051｜Introduction to Machine Learning Systems](../books/Reddi_IntroductionToMLSystems_Vol1_v0.8.0_en.pdf)Introduction to ML Systems。
   - [LRL-B-18-052｜Scaling Machine Learning Systems: From Nodes to Fleets](../books/Reddi_ScalingMLSystems_Vol2_v0.3.0_en.pdf)Scaling ML Systems。
3. 论文：[LRL-P-16-001｜How Does Quantization Affect Multilingual LLMs?](../papers/2024_Marchisio_HowDoesQuantizationAffect_en.pdf)→[LRL-P-16-033｜The Script Tax: Measuring Tokenization-Driven Efficiency and Latency D](../papers/2026_Dixit_TheScriptTax_en.pdf)→[LRL-P-16-059｜Efficient Memory Management for Large Language Model Serving with Page](../papers/2023_Kwon_EfficientMemoryManagement_en.pdf)→[LRL-P-16-030｜Speculative Decoding and the Curse of Multilinguality](../papers/2026_Paudel_SpeculativeDecodingCurse_en.pdf)。
