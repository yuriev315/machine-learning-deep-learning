# 评测学习与设计指南

目标：为小语种模型或应用建立可信的评测体系。

先厘清五组容易混淆的概念：
1. 原生语言测试与翻译测试：基准是用目标语言原生编写的，还是从英语翻译来的。
2. 用小语种回答与用该语言正确推理/执行工具：前者只说明输出语言对，后者才说明推理与操作正确。
3. 机器翻译文本与自然产生的本地语言文本。
4. 作者自报结果与独立复现结果。
5. 通用方法证据与特定语言案例证据。

每篇论文的这几项属性，见 `catalog_cn.csv` 中“基准来源（原生/翻译）”“结果来源”“证据范围”“关键区分说明”几列。

## 1. 原生构建与翻译基准

原生或本地知识基准：
- [LRL-P-15-002｜INCLUDE: Evaluating Multilingual Language Understanding with Regional](../papers/2024_Romanou_INCLUDE_en.pdf)INCLUDE：区域知识，44 种语言。
- [LRL-P-15-011｜MultiLoKo: a multilingual local knowledge benchmark for LLMs spanning](../papers/2025_Hupkes_MultiLoKo_en.pdf)MultiLoKo：本地知识。
- [LRL-P-15-023｜TUMLU: A Unified and Native Language Understanding Benchmark for Turki](../papers/2025_Isbarov_TUMLU_en.pdf)TUMLU：突厥语族原生基准。
- [LRL-P-15-024｜BertaQA: How Much Do Language Models Know About Local Culture?](../papers/2024_Etxaniz_BertaQA_en.pdf)BertaQA：巴斯克本地文化。
- [LRL-P-15-034｜ProverbEval: Exploring LLM Evaluation Challenges for Low-resource Lang](../papers/2024_Azime_ProverbEval_en.pdf)ProverbEval：埃塞俄比亚语言谚语理解。
- [LRL-P-15-004｜IrokoBench: A New Benchmark for African Languages in the Age of Large](../papers/2024_Adelani_IrokoBench_en.pdf)IrokoBench：非洲语言。

翻译基准的问题与改进：
- [LRL-P-15-001｜Global MMLU: Understanding and Addressing Cultural and Linguistic Bias](../papers/2024_Singh_GlobalMMLU_en.pdf)Global MMLU：标注翻译基准中的文化偏差。
- [LRL-P-15-007｜The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks](../papers/2025_Wu_BitterLessonLearned2000Multilingual_en.pdf)The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks。
- [LRL-P-15-013｜Global PIQA: Evaluating Commonsense Reasoning Across 100+ Languages an](../papers/2025_Chang_GlobalPIQA_en.pdf)Global PIQA。

文化知识：[LRL-P-15-003｜BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures](../papers/2024_Myung_BLEnD_en.pdf)BLEnD。

构建原则（来自上述文献的共同建议）：
- 优先母语者编写或改写。
- 翻译题须经母语者审校，并标注文化不适用的题目。
- 公开题目时说明来源与许可。

## 2. 生成与翻译评测

- 指标在低资源语言上的有效性：[LRL-P-15-051｜Evaluating the Evaluator: Summarization Metrics and LLM-Judges beyond](../papers/2025_Barnes_EvaluatingTheEvaluator_en.pdf)英语以外的摘要指标与 LLM 评判。
- 机器翻译评测污染：[LRL-P-05-064｜When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Tra](../papers/2026_Tan_WhenFloresBloomzWrong_en.pdf)FLORES 跨方向污染。
- 翻译腔对评判的影响：[LRL-P-09-059｜Mitigating Translationese Bias in Multilingual LLM-as-a-Judge via Dise](../papers/2026_Zhang_MitigatingTranslationese_en.pdf)。
- 工程：
  - [LRL-E-20｜sacrebleu](../reference_code/sacrebleu_2277cac_original_en.tar.gz)sacrebleu（BLEU/chrF）。
  - [LRL-E-21｜COMET](../reference_code/COMET_49c348d_original_en.tar.gz)COMET。

## 3. LLM 作为评判者与人工评价

LLM 评判的多语言可靠性：
- [LRL-P-15-047｜How Reliable is Multilingual LLM-as-a-Judge?](../papers/2025_Fu_HowReliableMultilingualLLM_en.pdf)How Reliable is Multilingual LLM-as-a-Judge?
- [LRL-P-15-048｜MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge a](../papers/2024_Son_MMEval_en.pdf)MM-Eval 元评测。
- [LRL-P-15-050｜M-Prometheus: A Suite of Open Multilingual LLM Judges](../papers/2025_Pombal_MPrometheus_en.pdf)M-Prometheus。
- [LRL-P-15-053｜Challenges and Recommendations for LLM-as-a-Judge in Multilingual Sett](../papers/2026_Dogruoz_ChallengesRecommendations_en.pdf)多语言与低资源场景下的挑战与建议。

人工评价与母语者：
- [LRL-P-02-070｜Assessing Thai Dialect Performance in LLMs with Automatic Benchmarks a](../papers/2025_Limkonchotiwat_AssessingThaiDialectPerformance_en.pdf)泰语方言的自动与人工评价对比。
- [LRL-P-10-017｜MENLO: From Preferences to Proficiency -- Evaluating and Modeling Nati](../papers/2025_Whitehouse_MENLO_en.pdf)MENLO：类母语质量的偏好评价。

工程（人工标注平台）：[LRL-E-22｜argilla](../reference_code/argilla_78cb518_original_en.tar.gz)Argilla。

建议：
- LLM 评判须与母语者评分做一致性检验，并报告一致性指标。
- 评判模型对目标语言不流利时，评判结果不可靠（见[LRL-P-10-009｜Fluent Alignment with Disfluent Judges: Post-training for Lower-resour](../papers/2025_Samuel_FluentAlignmentDisfluent_en.pdf)）。

## 4. 推理、长上下文与工具评测

- 多语言推理综述：[LRL-P-11-023｜A Survey of Multilingual Reasoning in Language Models](../papers/2025_Ghosh_SurveyMultilingualReasoning_en.pdf)。
- 推理语言控制：
  - [LRL-P-11-016｜When Models Reason in Your Language: Controlling Thinking Language Com](../papers/2025_Qi_WhenModelsReasonYourLanguage_en.pdf)控制思考语言的代价。
  - [LRL-P-11-034｜Beg to Differ: Understanding Reasoning-Answer Misalignment Across Lang](../papers/2025_Ovalle_BegToDiffer_en.pdf)推理与答案在不同语言间不一致。
- 测试时扩展的跨语言推理：[LRL-P-11-014｜Crosslingual Reasoning through Test-Time Scaling](../papers/2025_Yong_CrosslingualReasoningThrough_en.pdf)。
- 长上下文：[LRL-P-11-045｜One ruler to measure them all: Benchmarking multilingual long-context](../papers/2025_Kim_OneRulerMeasureThemAllBenchmarking_en.pdf)ONERULER，26 种语言。
- 工具调用的多语言鲁棒性：
  - [LRL-P-11-051｜Lost in Execution: On the Multilingual Robustness of Tool Calling in L](../papers/2026_Luo_LostInExecution_en.pdf)Lost in Execution。
  - [LRL-P-11-052｜Enhancing Tool Calling in LLMs with the International Tool Calling Dat](../papers/2026_Zhang_EnhancingToolCallingLLMs_en.pdf)国际化工具调用数据集。
- 结构化输出：[LRL-P-11-049｜JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Langua](../papers/2025_Geng_JSONSchemaBench_en.pdf)JSONSchemaBench（通用支撑；多语言 JSON 合规专门研究是库内缺口）。

关键区分：
- 判定“用目标语言执行工具成功”，要检查参数抽取与执行结果。
- 只检查回答语言不够。

## 5. 代码评测（用非英语提出编程需求）

- 多自然语言代码生成基准：
  - [LRL-P-14-001｜mHumanEval -- A Multilingual Benchmark to Evaluate Large Language Mode](../papers/2024_Raihan_MHumanEvalMultilingualBenchmark_en.pdf)mHumanEval，204 种自然语言。
  - [LRL-P-14-002｜HumanEval-XL: A Multilingual Code Generation Benchmark for Cross-lingu](../papers/2024_Peng_HumanEvalXL_en.pdf)HumanEval-XL。
- 偏差分析：
  - [LRL-P-14-003｜Exploring Multi-Lingual Bias of Large Code Models in Code Generation](../papers/2024_Wang_ExploringMultiLingualBias_en.pdf)代码模型的多语言偏差。
  - [LRL-P-14-004｜Bridging the Language Gap: Enhancing Multilingual Prompt-Based Code Ge](../papers/2024_Li_BridgingTheLanguageGap_en.pdf)多语言提示代码生成。
- 语码混合提示：[LRL-P-14-006｜CodeMixBench: Evaluating Large Language Models on Code Generation with](../papers/2025_Sheokand_CodeMixBench_en.pdf)CodeMixBench。
- 无污染代码评测：[LRL-P-14-045｜LiveCodeBench: Holistic and Contamination Free Evaluation of Large Lan](../papers/2024_Jain_LiveCodeBench_en.pdf)LiveCodeBench（通用支撑）。
- 仓库级任务：
  - [LRL-P-14-056｜SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](../papers/2023_Jimenez_SWEBench_en.pdf)SWE-bench（经典补充）。
  - [LRL-P-14-044｜Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving](../papers/2025_Zan_MultiSWEBench_en.pdf)Multi-SWE-bench（多编程语言）。

## 6. 安全与文化评测

- 安全：
  - [LRL-P-10-034｜Low-Resource Languages Jailbreak GPT-4](../papers/2023_Yong_LowResourceLanguagesJailbreak_en.pdf)低资源语言可绕过安全限制。
  - [LRL-P-10-037｜The Language Barrier: Dissecting Safety Challenges of LLMs in Multilin](../papers/2024_Shen_TheLanguageBarrier_en.pdf)多语言安全挑战剖析。
  - [LRL-P-10-052｜PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages](../papers/2025_Kumar_PolyGuard_en.pdf)PolyGuard。
- 奖励模型与偏好：[LRL-P-10-005｜M-RewardBench: Evaluating Reward Models in Multilingual Settings](../papers/2024_Gureja_MRewardBench_en.pdf)M-RewardBench。

## 7. 污染控制与统计不确定性

- 污染：
  - [LRL-P-05-017｜Data Contamination Can Cross Language Barriers](../papers/2024_Yao_DataContaminationCanCross_en.pdf)污染可以跨语言。
  - [LRL-P-05-063｜Contamination Report for Multilingual Benchmarks](../papers/2024_Ahuja_ContaminationReportMultilingual_en.pdf)多语言基准污染报告。
  - [LRL-P-05-038｜Obscuring Data Contamination Through Translation: Evidence from Arabic](../papers/2026_Abbas_ObscuringDataContamination_en.pdf)通过翻译掩盖污染。
- 统计不确定性：
  - [LRL-P-15-064｜Adding Error Bars to Evals: A Statistical Approach to Language Model E](../papers/2024_Miller_AddingErrorBarsEvalsStatistical_en.pdf)给评测加误差条。
  - [LRL-P-15-065｜Quantifying Variance in Evaluation Benchmarks](../papers/2024_Madaan_QuantifyingVarianceEvaluation_en.pdf)量化基准方差。
  - [LRL-P-15-066｜Signal and Noise: A Framework for Reducing Uncertainty in Language Mod](../papers/2025_Heineman_SignalAndNoise_en.pdf)Signal and Noise。

建议：
- 小语种测试集通常规模小，应报告置信区间或多次运行的方差。
- 不同语言之间的分数差，若在误差范围内，不应解读为能力差异。

## 8. 回归测试工程

- [LRL-E-18｜lm-evaluation-harness](../reference_code/lm-evaluation-harness_ddd6722_original_en.tar.gz)lm-evaluation-harness：支持多语言任务配置。
- [LRL-E-19｜lighteval](../reference_code/lighteval_7c1cd62_original_en.tar.gz)lighteval。
- 建议把以下几类评测固定为版本化的回归集，在每次训练或部署前运行：
  - 目标语言评测；
  - 原有语言评测；
  - 代码评测；
  - 工具调用评测；
  - 安全评测。

## 推荐学习顺序

[LRL-P-15-007｜The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks](../papers/2025_Wu_BitterLessonLearned2000Multilingual_en.pdf)→[LRL-P-15-001｜Global MMLU: Understanding and Addressing Cultural and Linguistic Bias](../papers/2024_Singh_GlobalMMLU_en.pdf)→[LRL-P-15-002｜INCLUDE: Evaluating Multilingual Language Understanding with Regional](../papers/2024_Romanou_INCLUDE_en.pdf)→[LRL-P-15-047｜How Reliable is Multilingual LLM-as-a-Judge?](../papers/2025_Fu_HowReliableMultilingualLLM_en.pdf)→[LRL-P-15-064｜Adding Error Bars to Evals: A Statistical Approach to Language Model E](../papers/2024_Miller_AddingErrorBarsEvalsStatistical_en.pdf)→[LRL-P-11-051｜Lost in Execution: On the Multilingual Robustness of Tool Calling in L](../papers/2026_Luo_LostInExecution_en.pdf)→[LRL-P-14-001｜mHumanEval -- A Multilingual Benchmark to Evaluate Large Language Mode](../papers/2024_Raihan_MHumanEvalMultilingualBenchmark_en.pdf)。

课程：
- [LRL-C-17-007｜Advanced Natural Language Processing](../university_materials/CMU_11-711_ANLP_2025Fall_LectureMaterials_en)CMU 11-711：评测与基准相关讲次。
- [LRL-C-17-001｜Natural Language Processing with Deep Learning](../university_materials/Stanford_CS224N_2026Winter_LectureMaterials_en)CS224N：评测讲次。
