# 端到端路线图：四种开发路线

四种路线：
- 路线 0：从零学习。
- 路线 A：适配现有基座。
- 路线 B：构建应用。
- 路线 C：从头预训练。

本图整合五份专题指南，每个阶段列出输入、产出、依赖和学习资料。

关于资源与效果：
- 本图不给出硬件预算、训练时长或效果承诺。
- 需要估计资源时，引用对应论文的模型规模、数据量与硬件条件，并注明不可外推。

## 路线 0：从零学习（无 ML 背景 → 能读懂并复现论文）

| 阶段 | 输入 | 产出 | 依赖 | 资料 |
|---|---|---|---|---|
| 0.1 数学 | 高中数学 | 线性代数、概率、优化基础 | — | foundations_cn.md 第 1 阶段：[LRL-B-18-001｜Mathematics for Machine Learning](../books/Deisenroth_MathematicsForMachineLearning_2020_en.pdf)[LRL-C-17-026｜Discrete Mathematics and Probability Theory](../university_materials/Berkeley_CS70_2026Spring_LectureMaterials_en) |
| 0.2 机器学习与深度学习 | 0.1 | 能训练与调试小型神经网络 | 0.1 | [LRL-C-17-031｜Introduction to Machine Learning](../university_materials/CMU_10-601_IntroML_2026Spring_LectureMaterials_en)[LRL-B-18-011｜Understanding Deep Learning](../books/Prince_UnderstandingDeepLearning_v5.0.3_en.pdf)[LRL-B-18-012｜Dive into Deep Learning](../books/Zhang_DiveIntoDeepLearning_2023_en.pdf) |
| 0.3 NLP 与 LLM | 0.2 | 理解 Transformer、预训练、后训练 | 0.2 | [LRL-C-17-001｜Natural Language Processing with Deep Learning](../university_materials/Stanford_CS224N_2026Winter_LectureMaterials_en)[LRL-C-17-002｜Language Modeling from Scratch](../university_materials/Stanford_CS336_2026Spring_LectureMaterials_en)[LRL-B-18-018｜Speech and Language Processing](../books/Jurafsky_SpeechAndLanguageProcessing_3rdEdDraft_2026_en.pdf)[LRL-B-18-037｜Foundations of Large Language Models](../books/Xiao_FoundationsOfLargeLanguageModels_v4_en.pdf) |
| 0.4 语言学与多语言 | 0.3（可并行） | 能分析目标语言的形态、文字、方言问题 | — | [LRL-B-18-033｜The Unicode Cookbook for Linguists: Managing writing systems using ort](../books/Moran_UnicodeCookbookForLinguists_2018_en.pdf)[LRL-C-17-041｜Multilingual Natural Language Processing](../university_materials/CMU_11-737_MultilingualNLP_2023Fall_LectureMaterials_en)[LRL-C-17-052｜NLP for Low-Resource and Marginalized Language Varieties](../university_materials/UZH_LowResourceMarginalizedVarietiesNLP_2026Spring_LectureMaterials_en)[LRL-P-02-018｜What is "Typological Diversity" in NLP?](../papers/2024_Ploeger_WhatTypologicalDiversity_en.pdf) |

## 路线 A：在现有多语言基座上增强小语种

| 阶段 | 输入 | 产出 | 依赖 | 资料 |
|---|---|---|---|---|
| A1 明确目标语言与资源条件 | 语言、文字、变体、可得数据 | 语言档案（含资源条件依据） | 0.4 | [LRL-P-03-009｜When Is Multilinguality a Curse? Language Modeling for 250 High- and L](../papers/2023_Chang_WhenMultilingualityCurse_en.pdf)[LRL-P-15-007｜The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks](../papers/2025_Wu_BitterLessonLearned2000Multilingual_en.pdf) |
| A2 建立原生评测与回归集 | 母语者、现有基准 | 版本化评测集（目标语言 + 原有语言 + 代码/工具） | A1 | evaluation_cn.md：[LRL-P-15-002｜INCLUDE: Evaluating Multilingual Language Understanding with Regional](../papers/2024_Romanou_INCLUDE_en.pdf)[LRL-P-15-064｜Adding Error Bars to Evals: A Statistical Approach to Language Model E](../papers/2024_Miller_AddingErrorBarsEvalsStatistical_en.pdf) |
| A3 基座评估与分词检查 | 候选基座、A2 | 基座选择记录、分词效率报告 | A2 | model_adaptation_cn.md §1–2：[LRL-P-06-022｜Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in T](../papers/2025_Foroutan_ParityAwareBytePairEncoding_en.pdf)[LRL-P-16-033｜The Script Tax: Measuring Tokenization-Driven Efficiency and Latency D](../papers/2026_Dixit_TheScriptTax_en.pdf) |
| A4 语料构建 | 来源、许可 | 版本化语料与数据卡 | A1 | data_pipeline_cn.md：[LRL-P-04-001｜FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data](../papers/2025_Penedo_FineWeb2_en.pdf)[LRL-P-05-020｜CommonLID: Re-evaluating State-of-the-Art Language Identification Perf](../papers/2026_Suarez_CommonLID_en.pdf)[LRL-E-01｜datatrove](../reference_code/datatrove_1977fbb_original_en.tar.gz) |
| A5 持续预训练（可选） | A3、A4、算力 | 适配基座 | A3、A4 | [LRL-P-07-065｜SambaLingo: Teaching Large Language Models New Languages](../papers/2024_Csaki_SambaLingo_en.pdf)[LRL-P-07-001｜Simple and Scalable Strategies to Continually Pre-train Large Language](../papers/2024_Ibrahim_SimpleScalableStrategies_en.pdf)[LRL-P-07-006｜Mitigating Catastrophic Forgetting in Language Transfer via Model Merg](../papers/2024_Alexandrov_MitigatingCatastrophicForgetting_en.pdf)[LRL-E-14｜Megatron-LM](../reference_code/Megatron-LM_4b4acac_original_en.tar.gz) |
| A6 指令微调 | 本地/翻译/合成指令数据 | 指令模型 | A5 或 A3 | [LRL-P-08-001｜Aya Dataset: An Open-Access Collection for Multilingual Instruction Tu](../papers/2024_Singh_AyaDataset_en.pdf)[LRL-P-08-002｜Multilingual Instruction Tuning With Just a Pinch of Multilinguality](../papers/2024_Shaham_MultilingualInstructionTuning_en.pdf)[LRL-P-09-033｜Is It Good Data for Multilingual Instruction Tuning or Just Bad Multil](../papers/2024_Chen_ItGoodDataMultilingualInstruction_en.pdf)[LRL-E-10｜peft](../reference_code/peft_eaa35c7_original_en.tar.gz) |
| A7 偏好对齐与安全 | 偏好数据、安全评测 | 对齐模型 | A6 | [LRL-P-10-001｜RLHF Can Speak Many Languages: Unlocking Multilingual Preference Optim](../papers/2024_Dang_RLHFCanSpeakManyLanguages_en.pdf)[LRL-P-10-034｜Low-Resource Languages Jailbreak GPT-4](../papers/2023_Yong_LowResourceLanguagesJailbreak_en.pdf)[LRL-E-11｜trl](../reference_code/trl_1b5c75e_original_en.tar.gz) |
| A8 遗忘与能力回归 | A2 回归集 | 前后对比报告；不达标则回到 A5–A7 | A5–A7 | [LRL-P-01-060｜Scaling Laws for Forgetting When Fine-Tuning Large Language Models](../papers/2024_Kalajdzievski_ScalingLawsForgettingWhen_en.pdf)[LRL-P-11-034｜Beg to Differ: Understanding Reasoning-Answer Misalignment Across Lang](../papers/2025_Ovalle_BegToDiffer_en.pdf)[LRL-E-18｜lm-evaluation-harness](../reference_code/lm-evaluation-harness_ddd6722_original_en.tar.gz) |

## 路线 B：现有模型 + 本地知识库 + 检索与工具

| 阶段 | 输入 | 产出 | 依赖 | 资料 |
|---|---|---|---|---|
| B1 场景与用户研究 | 目标用户、任务 | 需求与风险清单 | — | [LRL-P-13-001｜ASHABot: An LLM-Powered Chatbot to Support the Informational Needs of](../papers/2024_Ramjee_ASHABot_en.pdf)[LRL-P-13-003｜"Koyi Sawaal Nahi Hai": Reimagining Maternal Health Chatbots for Colle](../papers/2025_Hameed_KoyiSawaalNahiHai_en.pdf) |
| B2 模型能力评估 | 候选模型、A2 式评测 | 选型（含方言/罗马化/语码混合鲁棒性） | B1 | [LRL-P-13-002｜Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Rom](../papers/2025_Khullar_ScriptGap_en.pdf)[LRL-P-11-051｜Lost in Execution: On the Multilingual Robustness of Tool Calling in L](../papers/2026_Luo_LostInExecution_en.pdf) |
| B3 知识库构建 | 本地文档 | 解析后的文档库、更新流程 | B1 | [LRL-P-12-051｜MDPBench: A Benchmark for Multilingual Document Parsing in Real-World](../papers/2026_Li_MDPBench_en.pdf)[LRL-E-26｜docling](../reference_code/docling_a857fd2_original_en.tar.gz) |
| B4 检索与 RAG | B3、嵌入模型 | 检索评测报告、RAG 流水线 | B3 | [LRL-P-12-005｜M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity](../papers/2024_Chen_M3Embedding_en.pdf)[LRL-P-12-029｜Retrieval-augmented generation in multilingual settings](../papers/2024_Chirkova_RetrievalAugmentedGeneration_en.pdf)[LRL-P-12-028｜"Knowing When You Don't Know": A Multilingual Relevance Assessment Dat](../papers/2023_Thakur_KnowingWhenYouDonTKnowMultilingual_en.pdf)[LRL-E-24｜FlagEmbedding](../reference_code/FlagEmbedding_fd1a2bd_original_en.tar.gz) |
| B5 工具与智能体（含编程助手） | 工具接口 | 工具调用评测、执行隔离方案 | B2 | [LRL-P-14-001｜mHumanEval -- A Multilingual Benchmark to Evaluate Large Language Mode](../papers/2024_Raihan_MHumanEvalMultilingualBenchmark_en.pdf)[LRL-P-14-050｜Multi-Programming Language Sandbox for LLMs](../papers/2024_Dou_MultiProgrammingLanguage_en.pdf)[LRL-E-33｜continue](../reference_code/continue_b238c1f_original_en.tar.gz)[LRL-E-34｜OpenHands-software-agent-sdk](../reference_code/OpenHands-software-agent-sdk_ccae18c_original_en.tar.gz) |
| B6 部署与监控 | B4/B5 | 服务、按语言分组的监控、灰度方案 | B4、B5 | deployment_cn.md：[LRL-E-28｜vllm](../reference_code/vllm_5df63a7_original_en.tar.gz)[LRL-E-38｜langfuse](../reference_code/langfuse_d89f49b_original_en.tar.gz)[LRL-E-39｜argo-rollouts](../reference_code/argo-rollouts_356117c_original_en.tar.gz) |

## 路线 C：从头训练语言模型

| 阶段 | 输入 | 产出 | 依赖 | 资料 |
|---|---|---|---|---|
| C1 可行性评估 | 可得 token 量、算力、目标规模 | 规模与数据决策（引用论文条件，不外推） | 0.3 | [LRL-P-01-014｜Scaling Data-Constrained Language Models](../papers/2023_Muennighoff_ScalingDataConstrainedLanguage_en.pdf)[LRL-P-01-007｜Scaling Laws for Mixture Pretraining Under Data Constraints](../papers/2026_Sedova_ScalingLawsMixturePretraining_en.pdf)[LRL-P-03-011｜ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Fi](../papers/2025_Longpre_ATLAS_en.pdf)[LRL-P-03-009｜When Is Multilinguality a Curse? Language Modeling for 250 High- and L](../papers/2023_Chang_WhenMultilingualityCurse_en.pdf) |
| C2 分词器训练 | 清洗后语料 | 分词器 + 效率报告 | A4 | [LRL-P-06-015｜One Tokenizer To Rule Them All: Emergent Language Plasticity via Multi](../papers/2025_Abagyan_OneTokenizerRuleThemAllEmergent_en.pdf)[LRL-P-06-021｜MYTE: Morphology-Driven Byte Encoding for Better and Fairer Multilingu](../papers/2024_Limisiewicz_MYTE_en.pdf)[LRL-E-03｜sentencepiece](../reference_code/sentencepiece_e0cce7d_original_en.tar.gz) |
| C3 架构与训练系统 | C1 | 训练配置与检查点策略 | C1 | [LRL-C-17-002｜Language Modeling from Scratch](../university_materials/Stanford_CS336_2026Spring_LectureMaterials_en)[LRL-B-18-049｜How to Scale Your Model](../books/Austin_HowToScaleYourModel_2025_html_en)[LRL-B-18-050｜The Ultra-Scale Playbook: Training LLMs on GPU Clusters](../books/Tazi_UltraScalePlaybook_2025_en.pdf)[LRL-E-16｜torchtitan](../reference_code/torchtitan_45e33cd_original_en.tar.gz)[LRL-E-15｜DeepSpeed](../reference_code/DeepSpeed_0eb3a8b_original_en.tar.gz) |
| C4 预训练与监控 | C2、C3 | 基座模型、训练日志 | C2、C3 | [LRL-P-16-027｜Training LLMs on HPC Systems: Best Practices from the OpenGPT-X Projec](../papers/2025_Penke_TrainingLLMsHPCSystemsBest_en.pdf)[LRL-P-07-054｜MiniCPM: Unveiling the Potential of Small Language Models with Scalabl](../papers/2024_Hu_MiniCPM_en.pdf) |
| C5 后训练与评测 | C4 | 同路线 A 的 A6–A8 | C4 | model_adaptation_cn.md、evaluation_cn.md |

小语种从零训练的案例（规模与条件各异，仅供对照）：
- [LRL-P-03-028｜InkubaLM: A small language model for low-resource African languages](../papers/2024_Tonja_InkubaLM_en.pdf)InkubaLM，非洲语言小模型。
- [LRL-P-03-074｜Agaram 2.5B: The First Tamil-First Language Model Trained from Scratch](../papers/2026_Kumaresan_Agaram25B_en.pdf)Agaram 2.5B，泰米尔语。
- [LRL-P-07-052｜LLäMmlein: Transparent, Compact and Competitive German-Only Language M](../papers/2024_Pfister_LLaMmlein_en.pdf)LLäMmlein，德语。
- [LRL-P-03-008｜Goldfish: Monolingual Language Models for 350 Languages](../papers/2024_Chang_Goldfish_en.pdf)Goldfish，350 种语言的单语小模型。

## 横向依赖与常见陷阱

- 评测先于训练：先建好 A2 回归集，否则无法判断适配是否带来遗忘。
- 自然文本优先：机器翻译文本既可能混在语料里，也可能混在评测集里，见[LRL-P-05-004｜A Shocking Amount of the Web is Machine Translated: Insights from Mult](../papers/2024_Thompson_ShockingAmountWebMachine_en.pdf)[LRL-P-09-057｜Lost in Literalism: How Supervised Training Shapes Translationese in L](../papers/2025_Li_LostInLiteralism_en.pdf)。
- 结果需复核：作者自报的结果须在自己的语言与数据上复核。
- 成本按语言计算：同样内容在不同语言下的 token 数可能差别很大，见[LRL-P-16-034｜Measuring the Tokenization Premium: A Cost Audit for Underserved Langu](../papers/2026_Roy_MeasuringTokenizationPremium_en.pdf)。

## 工程资料总表

工程资料按 9 个工程环节分组，每个项目的版本/提交号、许可证、核心模块和本地路径，见以下位置：
- catalog_cn.csv 中编号以 LRL-E- 开头的行；
- scripts/work/engineering_notes_cn.md。
