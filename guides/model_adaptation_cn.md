# 模型适配学习与设计指南（路线 A：在现有多语言基座上增强小语种）

流程：基座评估 → 分词检查 → 持续预训练 → 指令微调（含合成/翻译数据）→ 偏好对齐与安全 → 遗忘与能力回归检查。

使用前请注意：
- 所有结论均为论文作者在其模型、语言与数据条件下的报告；“作者自报”与“独立复现”的区分，见 `catalog_cn.csv` 的“结果来源”列。
- 每个案例的语言与文字见“涉及语言”“文字系统”列。
- 本指南不给出超参数、算力预算或效果承诺。

## 1. 基座评估（输入：候选基座、目标语言评测集；产出：基座选择记录）

做什么：
- 用原生构建的目标语言评测（见 evaluation_cn.md）比较候选基座。
- 同时记录三项内容：分词效率、目标语言生成的流畅度与正确性、原有语言与代码能力的基线。

可参考的文献：
- 多语言基座的覆盖与能力不均衡：
  - [LRL-P-03-002｜Aya Model: An Instruction Finetuned Open-Access Multilingual Language](../papers/2024_Ustun_AyaModel_en.pdf)Aya Model。
  - [LRL-P-03-023｜Sailor2: Sailing in South-East Asia with Inclusive Multilingual LLMs](../papers/2025_Dou_Sailor2_en.pdf)Sailor2（东南亚语言）。
  - [LRL-P-03-043｜Poro 34B and the Blessing of Multilinguality](../papers/2024_Luukkonen_Poro34BBlessingMultilinguality_en.pdf)Poro 34B（芬兰语加英语加代码）。
- 大规模语言覆盖：
  - [LRL-P-03-005｜EMMA-500: Enhancing Massively Multilingual Adaptation of Large Languag](../papers/2024_Ji_EMMA500_en.pdf)EMMA-500。
  - [LRL-P-03-001｜MaLA-500: Massive Language Adaptation of Large Language Models](../papers/2024_Lin_MaLA500_en.pdf)MaLA-500。
  - [LRL-P-03-008｜Goldfish: Monolingual Language Models for 350 Languages](../papers/2024_Chang_Goldfish_en.pdf)Goldfish：为 350 种语言提供单语小模型，可作为对照基线。
- 多语言是否成为“诅咒”：[LRL-P-03-009｜When Is Multilinguality a Curse? Language Modeling for 250 High- and L](../papers/2023_Chang_WhenMultilingualityCurse_en.pdf)。
- 迁移规模规律：[LRL-P-03-011｜ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Fi](../papers/2025_Longpre_ATLAS_en.pdf)ATLAS。

## 2. 分词检查与词表适配（产出：分词效率报告、是否扩表的决定）

先测量目标语言文本在基座分词器下的 token 数，与英语或同义平行文本对比，判断是否需要扩表或换分词器。

文献：
- 分词公平性：
  - [LRL-P-06-022｜Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in T](../papers/2025_Foroutan_ParityAwareBytePairEncoding_en.pdf)Parity-aware BPE。
  - [LRL-P-06-014｜Equity with Efficiency: An Empirical Study of Tokenizers for Multiling](../papers/2026_Lee_EquityWithEfficiency_en.pdf)东南亚语言分词器实证。
  - [LRL-P-06-005｜Why do language models perform worse for morphologically complex langu](../papers/2024_Arnett_WhyDoLanguageModelsPerform_en.pdf)形态复杂语言为何更难。
- 成本视角，与部署相关：
  - [LRL-P-16-033｜The Script Tax: Measuring Tokenization-Driven Efficiency and Latency D](../papers/2026_Dixit_TheScriptTax_en.pdf)The Script Tax。
  - [LRL-P-16-034｜Measuring the Tokenization Premium: A Cost Audit for Underserved Langu](../papers/2026_Roy_MeasuringTokenizationPremium_en.pdf)分词溢价的成本审计。
- 词表扩展与嵌入初始化：
  - [LRL-P-06-024｜Efficient and Effective Vocabulary Expansion Towards Multilingual Larg](../papers/2024_Kim_EfficientEffectiveVocabulary_en.pdf)。
  - [LRL-P-06-027｜How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Ta](../papers/2024_Yamaguchi_HowCanEffectivelyExpandVocabulary_en.pdf)用 0.01GB 目标语言数据扩表。
  - [LRL-P-06-077｜FOCUS: Effective Embedding Initialization for Monolingual Specializati](../papers/2023_Dobler_FOCUS_en.pdf)FOCUS（经典补充）。
  - [LRL-P-06-035｜ANGOFA: Leveraging OFA Embedding Initialization and Synthetic Data for](../papers/2024_Quinjica_ANGOFA_en.pdf)ANGOFA。
  - [LRL-P-06-039｜Second Language (Arabic) Acquisition of LLMs via Progressive Vocabular](../papers/2024_Zhu_SecondLanguageArabicAcquisition_en.pdf)渐进式词表扩展（阿拉伯语）。
  - [LRL-P-06-032｜Zero-Shot Tokenizer Transfer](../papers/2024_Minixhofer_ZeroShotTokenizerTransfer_en.pdf)零样本分词器迁移。
- 不扩表的替代：
  - [LRL-P-06-064｜RomanSetu: Efficiently unlocking multilingual capabilities of Large La](../papers/2024_Husain_RomanSetu_en.pdf)RomanSetu（罗马化）。
  - [LRL-P-06-021｜MYTE: Morphology-Driven Byte Encoding for Better and Fairer Multilingu](../papers/2024_Limisiewicz_MYTE_en.pdf)MYTE（形态驱动的字节编码）。
  - [LRL-P-06-051｜Byte Latent Transformer: Patches Scale Better Than Tokens](../papers/2024_Pagnoni_ByteLatentTransformer_en.pdf)Byte Latent Transformer（通用支撑）。
  - [LRL-P-06-015｜One Tokenizer To Rule Them All: Emergent Language Plasticity via Multi](../papers/2025_Abagyan_OneTokenizerRuleThemAllEmergent_en.pdf)通用多语言分词器带来的“语言可塑性”。

工程：
- [LRL-E-03｜sentencepiece](../reference_code/sentencepiece_e0cce7d_original_en.tar.gz)sentencepiece。
- [LRL-E-04｜tokenizers](../reference_code/tokenizers_3012770_original_en.tar.gz)tokenizers。

检查项：
- 扩表之后，新嵌入的初始化方式。
- 原有语言的分词是否被改变。
- 下游评测要同时覆盖目标语言与原有语言。

## 3. 持续预训练（产出：目标语言适配后的基座 + 训练与数据记录）

方法与经验：
- 教授新语言的系统研究：
  - [LRL-P-07-065｜SambaLingo: Teaching Large Language Models New Languages](../papers/2024_Csaki_SambaLingo_en.pdf)SambaLingo。
  - [LRL-P-07-004｜LLaMA Beyond English: An Empirical Study on Language Capability Transf](../papers/2024_Zhao_LLaMABeyondEnglish_en.pdf)LLaMA Beyond English。
  - [LRL-P-07-018｜Breaking Language Barriers: Cross-Lingual Continual Pre-Training at Sc](../papers/2024_Zheng_BreakingLanguageBarriers_en.pdf)大规模跨语言持续预训练。
- 学习率重热、重放等通用策略：[LRL-P-07-001｜Simple and Scalable Strategies to Continually Pre-train Large Language](../papers/2024_Ibrahim_SimpleScalableStrategies_en.pdf)Simple and Scalable Strategies to Continually Pre-train（通用支撑）。
- 语言适配中的能力涌现：[LRL-P-07-016｜Emergent Abilities of Large Language Models under Continued Pretrainin](../papers/2025_Elhady_EmergentAbilitiesLargeLanguage_en.pdf)，涉及巴斯克语、阿拉伯语、印尼语。
- 具体语言案例：
  - [LRL-P-07-003｜Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Jap](../papers/2024_Fujii_ContinualPreTrainingCross_en.pdf)日语。
  - [LRL-P-07-022｜Small Languages, Big Models: A Study of Continual Training on Language](../papers/2024_Samuel_SmallLanguagesBigModels_en.pdf)挪威语与北萨米语。
  - [LRL-P-07-019｜AfriqueLLM: How Data Mixing and Model Architecture Impact Continued Pr](../papers/2026_Yu_AfriqueLLM_en.pdf)AfriqueLLM，20 种非洲语言，研究数据混合与架构的影响。

灾难性遗忘与模型合并：
- [LRL-P-07-006｜Mitigating Catastrophic Forgetting in Language Transfer via Model Merg](../papers/2024_Alexandrov_MitigatingCatastrophicForgetting_en.pdf)通过模型合并缓解语言迁移中的遗忘。
- [LRL-P-07-007｜Unlocking the Potential of Model Merging for Low-Resource Languages](../papers/2024_Tao_UnlockingPotentialModelMerging_en.pdf)低资源语言的模型合并。
- 遗忘的规模规律与再审视（第 01 类）：
  - [LRL-P-01-060｜Scaling Laws for Forgetting When Fine-Tuning Large Language Models](../papers/2024_Kalajdzievski_ScalingLawsForgettingWhen_en.pdf)。
  - [LRL-P-01-064｜Revisiting Catastrophic Forgetting in Large Language Model Tuning](../papers/2024_Li_RevisitingCatastrophicForgetting_en.pdf)。
  - [LRL-P-01-061｜Spurious Forgetting in Continual Learning of Language Models](../papers/2025_Zheng_SpuriousForgettingContinual_en.pdf)Spurious Forgetting。
- 可塑性丧失：[LRL-P-01-063｜Can Scale Save Us From Plasticity Loss in Large Language Models?](../papers/2026_HernandezGarcia_CanScaleSaveUsPlasticity_en.pdf)。

工程：
- [LRL-E-14｜Megatron-LM](../reference_code/Megatron-LM_4b4acac_original_en.tar.gz)Megatron-LM。
- [LRL-E-15｜DeepSpeed](../reference_code/DeepSpeed_0eb3a8b_original_en.tar.gz)DeepSpeed。
- [LRL-E-16｜torchtitan](../reference_code/torchtitan_45e33cd_original_en.tar.gz)torchtitan。
- [LRL-E-17｜accelerate](../reference_code/accelerate_6afc1e5_original_en.tar.gz)accelerate。
- 训练框架入口：[LRL-E-12｜LLaMA-Factory](../reference_code/LLaMA-Factory_7af9095_original_en.tar.gz)LLaMA-Factory。

## 4. 指令微调与参数高效适配（产出：指令模型、指令数据卡）

指令数据来源分三类，必须区分记录：
- 本地原生编写：
  - [LRL-P-08-001｜Aya Dataset: An Open-Access Collection for Multilingual Instruction Tu](../papers/2024_Singh_AyaDataset_en.pdf)Aya Dataset。
  - [LRL-P-08-021｜WangchanThaiInstruct: An instruction-following Dataset for Culture-Awa](../papers/2025_Limkonchotiwat_WangchanThaiInstruct_en.pdf)WangchanThaiInstruct（泰语）。
- 机器翻译：见第 5 节。
- 教师模型合成：见第 5 节。

多语言指令迁移，即“需要多少种语言的指令数据”：
- [LRL-P-08-002｜Multilingual Instruction Tuning With Just a Pinch of Multilinguality](../papers/2024_Shaham_MultilingualInstructionTuning_en.pdf)只需少量多语言数据。
- [LRL-P-08-003｜Turning English-centric LLMs Into Polyglots: How Much Multilinguality](../papers/2023_Kew_TurningEnglishCentricLLMs_en.pdf)把以英语为主的模型变成多语言模型需要多少多语言数据。
- [LRL-P-08-005｜How Many Languages Make Good Multilingual Instruction Tuning? A Case S](../papers/2024_Ji_HowManyLanguagesMakeGood_en.pdf)BLOOM 上的多语言数量研究。
- [LRL-P-08-004｜Zero-shot cross-lingual transfer in instruction tuning of large langua](../papers/2024_Chirkova_ZeroShotCrossLingualTransfer_en.pdf)零样本跨语言迁移。

低资源语言指令化的系统研究：
- [LRL-P-08-015｜Instructing Large Language Models for Low-Resource Languages: A System](../papers/2025_Sainz_InstructingLargeLanguage_en.pdf)巴斯克语。
- [LRL-P-08-029｜It's All About In-Context Learning! Teaching Extremely Low-Resource La](../papers/2025_Li_ItSAllAboutContextLearning_en.pdf)极低资源语言与上下文学习。

参数高效适配：
- [LRL-P-08-013｜LoRA Learns Less and Forgets Less](../papers/2024_Biderman_LoRALearnsLessForgetsLess_en.pdf)LoRA Learns Less and Forgets Less（通用支撑，作者结论限于其实验设置）。
- [LRL-P-08-023｜Train More Parameters But Mind Their Placement: Insights into Language](../papers/2024_Kunz_TrainMoreParametersButMind_en.pdf)冰岛语适配中参数的放置位置。
- [LRL-P-08-011｜QLoRA: Efficient Finetuning of Quantized LLMs](../papers/2023_Dettmers_QLoRA_en.pdf)QLoRA（经典补充）。

工程：
- [LRL-E-10｜peft](../reference_code/peft_eaa35c7_original_en.tar.gz)peft。
- [LRL-E-11｜trl](../reference_code/trl_1b5c75e_original_en.tar.gz)trl。
- [LRL-E-12｜LLaMA-Factory](../reference_code/LLaMA-Factory_7af9095_original_en.tar.gz)LLaMA-Factory。
- [LRL-E-13｜open-instruct](../reference_code/open-instruct_64beb76_original_en.tar.gz)open-instruct。

## 5. 合成数据、翻译与蒸馏（产出：合成/翻译数据及其验证记录）

翻译指令与合成数据：
- [LRL-P-09-034｜MURI: High-Quality Instruction Tuning Datasets for Low-Resource Langua](../papers/2024_Koksal_MURI_en.pdf)MURI：反向指令生成。
- [LRL-P-09-036｜UPDESH: Synthesizing Grounded Instruction Tuning Data for 13 Indic Lan](../papers/2025_Chitale_UPDESH_en.pdf)UPDESH：基于本地语境合成，覆盖 13 种印度语言。
- [LRL-P-09-045｜Multilingual Arbitrage: Optimizing Data Pools to Accelerate Multilingu](../papers/2024_Odumakinde_MultilingualArbitrage_en.pdf)多语言数据池套利。
- [LRL-P-09-043｜Enhancing Multilingual Capabilities of Large Language Models through S](../papers/2024_Zhang_EnhancingMultilingualCapabilities_en.pdf)自蒸馏增强多语言能力。

翻译数据的偏差：
- [LRL-P-09-033｜Is It Good Data for Multilingual Instruction Tuning or Just Bad Multil](../papers/2024_Chen_ItGoodDataMultilingualInstruction_en.pdf)区分“数据好”与“评测有问题”。
- 翻译腔：
  - [LRL-P-09-057｜Lost in Literalism: How Supervised Training Shapes Translationese in L](../papers/2025_Li_LostInLiteralism_en.pdf)。
  - [LRL-P-09-058｜An Investigation of Translationese in the Generations of Multilingual](../papers/2026_Valentini_InvestigationTranslationese_en.pdf)。

基于语法书/词典的低资源翻译（MTOB 系列）：
- [LRL-P-09-014｜A Benchmark for Learning to Translate a New Language from One Grammar](../papers/2023_Tanzer_BenchmarkLearningTranslate_en.pdf)（经典补充）。
- [LRL-P-09-001｜Can LLMs Really Learn to Translate a Low-Resource Language from One Gr](../papers/2024_Aycock_CanLLMsReallyLearnTranslate_en.pdf)质疑模型是否真的从语法书中学会翻译。

合成数据扩展低资源机器翻译：
- [LRL-P-09-019｜Scaling Low-Resource MT via Synthetic Data Generation with LLMs](../papers/2025_Gibert_ScalingLowResourceMTSynthetic_en.pdf)。
- [LRL-P-09-018｜From LLM to NMT: Advancing Low-Resource Machine Translation with Claud](../papers/2024_Enis_FromLLMToNMT_en.pdf)。

注意：
- 合成数据在库内缺少专门的“验证与过滤”研究，相关做法散在各论文的方法部分中。
- 使用合成数据时，必须用原生构建的测试集评测，避免用同一翻译系统的输出自我验证。

## 6. 偏好对齐与安全（产出：对齐后的模型、安全评测记录）

多语言偏好优化：
- [LRL-P-10-001｜RLHF Can Speak Many Languages: Unlocking Multilingual Preference Optim](../papers/2024_Dang_RLHFCanSpeakManyLanguages_en.pdf)RLHF Can Speak Many Languages。
- [LRL-P-10-002｜The Multilingual Alignment Prism: Aligning Global and Local Preference](../papers/2024_Aakanksha_MultilingualAlignmentPrism_en.pdf)全球与本地偏好。
- [LRL-P-10-003｜Reuse Your Rewards: Reward Model Transfer for Zero-Shot Cross-Lingual](../papers/2024_Wu_ReuseYourRewards_en.pdf)奖励模型跨语言迁移。

低资源后训练经验：
- [LRL-P-10-009｜Fluent Alignment with Disfluent Judges: Post-training for Lower-resour](../papers/2025_Samuel_FluentAlignmentDisfluent_en.pdf)挪威语，评判模型本身不流利时如何对齐。
- [LRL-P-10-019｜Got Compute, but No Data: Lessons From Post-training a Finnish LLM](../papers/2025_Zosa_GotComputeButNoDataLessons_en.pdf)芬兰语，有算力缺数据时的经验教训。

奖励模型评测：
- [LRL-P-10-005｜M-RewardBench: Evaluating Reward Models in Multilingual Settings](../papers/2024_Gureja_MRewardBench_en.pdf)M-RewardBench。
- [LRL-P-10-015｜Relic: Enhancing Reward Model Generalization for Low-Resource Indic La](../papers/2025_Ghosal_Relic_en.pdf)Relic（印度低资源语言）。

安全：
- [LRL-P-10-034｜Low-Resource Languages Jailbreak GPT-4](../papers/2023_Yong_LowResourceLanguagesJailbreak_en.pdf)低资源语言可绕过安全限制（经典补充，2023-10）。
- [LRL-P-10-037｜The Language Barrier: Dissecting Safety Challenges of LLMs in Multilin](../papers/2024_Shen_TheLanguageBarrier_en.pdf)多语言安全挑战剖析。
- [LRL-P-10-052｜PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages](../papers/2025_Kumar_PolyGuard_en.pdf)PolyGuard 多语言安全审核。

文化适切性：
- [LRL-P-10-017｜MENLO: From Preferences to Proficiency -- Evaluating and Modeling Nati](../papers/2025_Whitehouse_MENLO_en.pdf)MENLO。
- [LRL-P-15-003｜BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures](../papers/2024_Myung_BLEnD_en.pdf)BLEnD。

## 7. 遗忘与能力回归检查（产出：前后对比报告）

每个阶段结束后，至少比较三类能力：
1. 目标语言的理解、生成与推理（原生构建的基准）。
2. 原有高资源语言（通常是英语）的同类能力。
3. 代码与工具调用能力：如果产品需要，参见 evaluation_cn.md 的代码/工具评测。

文献依据：
- 遗忘相关：[LRL-P-01-060｜Scaling Laws for Forgetting When Fine-Tuning Large Language Models](../papers/2024_Kalajdzievski_ScalingLawsForgettingWhen_en.pdf)、[LRL-P-07-006｜Mitigating Catastrophic Forgetting in Language Transfer via Model Merg](../papers/2024_Alexandrov_MitigatingCatastrophicForgetting_en.pdf)、[LRL-P-08-013｜LoRA Learns Less and Forgets Less](../papers/2024_Biderman_LoRALearnsLessForgetsLess_en.pdf)。
- 推理与回答语言不一致：[LRL-P-11-034｜Beg to Differ: Understanding Reasoning-Answer Misalignment Across Lang](../papers/2025_Ovalle_BegToDiffer_en.pdf)。
- 控制思考语言的代价：[LRL-P-11-016｜When Models Reason in Your Language: Controlling Thinking Language Com](../papers/2025_Qi_WhenModelsReasonYourLanguage_en.pdf)。

工程：
- 回归评测：
  - [LRL-E-18｜lm-evaluation-harness](../reference_code/lm-evaluation-harness_ddd6722_original_en.tar.gz)lm-evaluation-harness。
  - [LRL-E-19｜lighteval](../reference_code/lighteval_7c1cd62_original_en.tar.gz)lighteval。

## 推荐学习顺序

1. 课程：
   - [LRL-C-17-002｜Language Modeling from Scratch](../university_materials/Stanford_CS336_2026Spring_LectureMaterials_en)CS336。
   - [LRL-C-17-008｜Large Language Models: Methods and Applications](../university_materials/CMU_11-667_LLMMethodsApplications_2024Fall_LectureMaterials_en)CMU 11-667。
   - [LRL-C-17-041｜Multilingual Natural Language Processing](../university_materials/CMU_11-737_MultilingualNLP_2023Fall_LectureMaterials_en)CMU 11-737 多语言 NLP。
   - [LRL-C-17-046｜Subword Modeling](../university_materials/CMU_11-824_SubwordModeling_2026Spring_LectureMaterials_en)CMU 子词建模。
2. 书：
   - [LRL-B-18-037｜Foundations of Large Language Models](../books/Xiao_FoundationsOfLargeLanguageModels_v4_en.pdf)Foundations of Large Language Models。
   - [LRL-B-18-038｜Reinforcement Learning from Human Feedback](../books/Lambert_ReinforcementLearningFromHumanFeedback_v12_en.pdf)RLHF。
3. 核心论文：
   - [LRL-P-07-065｜SambaLingo: Teaching Large Language Models New Languages](../papers/2024_Csaki_SambaLingo_en.pdf)→[LRL-P-06-027｜How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Ta](../papers/2024_Yamaguchi_HowCanEffectivelyExpandVocabulary_en.pdf)→[LRL-P-08-002｜Multilingual Instruction Tuning With Just a Pinch of Multilinguality](../papers/2024_Shaham_MultilingualInstructionTuning_en.pdf)→[LRL-P-09-033｜Is It Good Data for Multilingual Instruction Tuning or Just Bad Multil](../papers/2024_Chen_ItGoodDataMultilingualInstruction_en.pdf)→[LRL-P-10-001｜RLHF Can Speak Many Languages: Unlocking Multilingual Preference Optim](../papers/2024_Dang_RLHFCanSpeakManyLanguages_en.pdf)→[LRL-P-07-006｜Mitigating Catastrophic Forgetting in Language Transfer via Model Merg](../papers/2024_Alexandrov_MitigatingCatastrophicForgetting_en.pdf)。
