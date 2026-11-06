# 基础先修路线：数学、深度学习、NLP、语言学与多语言学习

本路线按“教材打底 → 课程串讲 → 论文接到前沿”组织。课程与书的先修要求、难度、学期或版本，见 `catalog_cn.csv` 的“先修要求”“难度或阶段”“学期或书籍版本”列。

阶段分档：
- 入门：本科低年级可读。
- 进阶：需要前一阶段基础。
- 高阶：研究方向，可按需选读。

## 第 1 阶段：数学与概率统计（入门 → 进阶）

线性代数：
- [LRL-B-18-003｜Introduction to Applied Linear Algebra: Vectors, Matrices, and Least S](../books/Boyd_IntroductionAppliedLinearAlgebra_2018_en.pdf)Boyd & Vandenberghe：Introduction to Applied Linear Algebra（入门）。
- [LRL-B-18-007｜Linear Algebra Done Right](../books/Axler_LinearAlgebraDoneRight_4thEd_en.pdf)Axler：Linear Algebra Done Right（偏证明）。

面向机器学习的数学总览：[LRL-B-18-001｜Mathematics for Machine Learning](../books/Deisenroth_MathematicsForMachineLearning_2020_en.pdf)Mathematics for Machine Learning。

概率与离散数学：[LRL-C-17-026｜Discrete Mathematics and Probability Theory](../university_materials/Berkeley_CS70_2026Spring_LectureMaterials_en)Berkeley CS70。

统计理论（高阶）：[LRL-C-17-029｜Theoretical Statistics](../university_materials/Berkeley_Stat210A_2025Fall_LectureMaterials_en)Berkeley Stat 210A。注意这套讲义是手写扫描件，可读性有限。

信息论：
- [LRL-B-18-004｜Information Theory, Inference, and Learning Algorithms](../books/MacKay_InformationTheoryInferenceLearning_2003_en.pdf)MacKay。
- [LRL-B-18-006｜Information Theory: From Coding to Learning](../books/Polyanskiy_InformationTheoryCodingToLearning_2025_en.pdf)Polyanskiy & Wu（高阶）。

优化：
- [LRL-B-18-002｜Convex Optimization](../books/Boyd_ConvexOptimization_2004_en.pdf)Boyd：Convex Optimization。
- [LRL-C-17-027｜Convex Optimization I](../university_materials/Stanford_EE364a_2026Summer_LectureMaterials_en)Stanford EE364a。
- [LRL-C-17-028｜Optimization for Machine Learning](../university_materials/EPFL_CS-439_OptML_2026Spring_LectureMaterials_en)EPFL Optimization for ML。
- [LRL-B-18-008｜Algorithms for Optimization](../books/Kochenderfer_AlgorithmsForOptimization_2ndEd_en.pdf)Algorithms for Optimization。

高维概率与随机算法（高阶）：
- [LRL-B-18-005｜High-Dimensional Probability: An Introduction with Applications in Dat](../books/Vershynin_HighDimensionalProbability_2ndEd_en.pdf)Vershynin。
- [LRL-C-17-037｜The Modern Algorithmic Toolbox](../university_materials/Stanford_CS168_ModernAlgorithmicToolbox_2024Spring_LectureNotes_en)Stanford CS168。

## 第 2 阶段：机器学习与深度学习（入门 → 进阶）

课程（任选一门入门课，再选一门深度学习课）：
- 入门：
  - [LRL-C-17-031｜Introduction to Machine Learning](../university_materials/CMU_10-601_IntroML_2026Spring_LectureMaterials_en)CMU 10-601。
  - [LRL-C-17-034｜Introduction to Machine Learning](../university_materials/Berkeley_CS189_IntroML_2025Fall_LectureMaterials_en)Berkeley CS189。
  - [LRL-C-17-035｜Introduction to Machine Learning](../university_materials/Cornell_CS4780_IntroML_2024Spring_LectureMaterials_en)Cornell CS4780。
- 深度学习：
  - [LRL-C-17-032｜Introduction to Deep Learning](../university_materials/CMU_11-785_IntroDL_2025Spring_LectureMaterials_en)CMU 11-785。
  - [LRL-C-17-033｜Deep Learning](../university_materials/MIT_6.7960_DeepLearning_2025Fall_LectureMaterials_en)MIT 6.7960。
- 进阶：[LRL-C-17-036｜Advanced Machine Learning](../university_materials/UBC_CPSC440_AdvancedML_2025W2_LectureMaterials_en)UBC CPSC 440。

书：
- 概率机器学习：[LRL-B-18-009｜Probabilistic Machine Learning: An Introduction](../books/Murphy_ProbabilisticMLIntroduction_2022_en.pdf)Murphy PML1，[LRL-B-18-010｜Probabilistic Machine Learning: Advanced Topics](../books/Murphy_ProbabilisticMLAdvancedTopics_2023_en.pdf)PML2。
- 深度学习主教材：[LRL-B-18-011｜Understanding Deep Learning](../books/Prince_UnderstandingDeepLearning_v5.0.3_en.pdf)Prince：Understanding Deep Learning。
- 动手实践：[LRL-B-18-012｜Dive into Deep Learning](../books/Zhang_DiveIntoDeepLearning_2023_en.pdf)Dive into Deep Learning。
- 速览：[LRL-B-18-014｜The Little Book of Deep Learning](../books/Fleuret_LittleBookOfDeepLearning_2023_en.pdf)The Little Book of Deep Learning。
- 可微编程视角：
  - [LRL-B-18-015｜Alice's Adventures in a Differentiable Wonderland](../books/Scardapane_AlicesAdventuresDifferentiableWonderland_v3_en.pdf)。
  - [LRL-B-18-016｜The Elements of Differentiable Programming](../books/Blondel_ElementsOfDifferentiableProgramming_v4_en.pdf)。
- 学习理论（高阶）：[LRL-B-18-013｜Learning Theory from First Principles](../books/Bach_LearningTheoryFirstPrinciples_2024_en.pdf)Bach。
- 经典参考：[LRL-B-18-017｜Deep Learning](../books/Goodfellow_DeepLearning_2016_html_en)Goodfellow（离线 HTML 包）。

## 第 3 阶段：NLP 与大语言模型

课程：
- 入门：
  - [LRL-C-17-001｜Natural Language Processing with Deep Learning](../university_materials/Stanford_CS224N_2026Winter_LectureMaterials_en)Stanford CS224N 2026。
  - [LRL-C-17-011｜Natural Language Processing](../university_materials/Princeton_COS484_2026Spring_LectureMaterials_en)Princeton COS484。
  - [LRL-C-17-017｜Natural Language Processing (LM-class)](../university_materials/Cornell_CS5740_LMClass_2025Spring_LectureMaterials_en)Cornell LM-class。
- 进阶：
  - [LRL-C-17-007｜Advanced Natural Language Processing](../university_materials/CMU_11-711_ANLP_2025Fall_LectureMaterials_en)CMU 11-711。
  - [LRL-C-17-012｜NLP: Self-supervised Models](../university_materials/JHU_CS601-471_SelfSupervisedModels_2025Spring_LectureMaterials_en)JHU 自监督模型。
- LLM 专门课：
  - [LRL-C-17-002｜Language Modeling from Scratch](../university_materials/Stanford_CS336_2026Spring_LectureMaterials_en)CS336 从零构建语言模型。
  - [LRL-C-17-003｜Transformers & Large Language Models](../university_materials/Stanford_CME295_2025Autumn_LectureMaterials_en)CME295。
  - [LRL-C-17-008｜Large Language Models: Methods and Applications](../university_materials/CMU_11-667_LLMMethodsApplications_2024Fall_LectureMaterials_en)CMU 11-667。
  - [LRL-C-17-019｜Deep Dive into Large Language Models](../university_materials/Princeton_COS597R_DeepDiveLLMs_2024Fall_LectureMaterials_en)Princeton COS597R。
  - [LRL-C-17-021｜Large Language Models](../university_materials/Stanford_CS324_LLMs_2022Winter_LectureNotes_en)CS324（2022，经典）。

书：
- [LRL-B-18-018｜Speech and Language Processing](../books/Jurafsky_SpeechAndLanguageProcessing_3rdEdDraft_2026_en.pdf)Jurafsky & Martin SLP3。
- [LRL-B-18-019｜Natural Language Processing](../books/Eisenstein_NaturalLanguageProcessing_2018_en.pdf)Eisenstein。
- [LRL-B-18-023｜Natural Language Processing: Neural Networks and Large Language Models](../books/Xiao_NLPNeuralNetworksAndLLMs_2026_en.pdf)Xiao：NLP 神经网络与 LLM。
- [LRL-B-18-037｜Foundations of Large Language Models](../books/Xiao_FoundationsOfLargeLanguageModels_v4_en.pdf)Foundations of Large Language Models。
- 中文资料：
  - [LRL-B-18-040｜大语言模型](../books/Zhao_DaYuYanMoXing_2025_cn.pdf)《大语言模型》。注意这份 PDF 的中文文本抽取质量差，全文检索时会漏检。
  - [LRL-B-18-039｜大规模语言模型：从理论到实践](../books/Zhang_DaGuiMoYuYanMoXing_2ndEd_cn.pdf)《大规模语言模型：从理论到实践》。
  - 课程课件：[LRL-C-17-018｜大语言模型（课程 PDF 课件）](../university_materials/RUC_LLMBook_DaYuYanMoXing_2025_CourseSlides_cn)人大《大语言模型》。

## 第 4 阶段：语言学基础（小语种开发必需）

形态、句法与语义：
- [LRL-B-18-025｜Grammatical theory: From transformational grammar to constraint-based](../books/Mueller_GrammaticalTheory_5thEd_en.pdf)Müller：Grammatical Theory。
- [LRL-B-18-027｜Analyzing meaning: An introduction to semantics and pragmatics](../books/Kroeger_AnalyzingMeaning_3rdEd_en.pdf)Kroeger：Analyzing Meaning。
- [LRL-C-17-047｜Morphological and Syntactic Analysis](../university_materials/CUNI_NPFL094_MorphSyntaxAnalysis_2025-26Winter_LectureMaterials_en)Charles NPFL094 形态与句法分析。

语料与方法：[LRL-B-18-026｜Corpus linguistics: A guide to the methodology](../books/Stefanowitsch_CorpusLinguistics_2020_en.pdf)Corpus Linguistics。

文字系统与 Unicode：[LRL-B-18-033｜The Unicode Cookbook for Linguists: Managing writing systems using ort](../books/Moran_UnicodeCookbookForLinguists_2018_en.pdf)The Unicode Cookbook for Linguists。

语言类型与多样性：
- [LRL-B-18-034｜Indigenous languages of the Americas and their structures: Sounds](../books/Saguaro_IndigenousLanguagesAmericasSounds_2026_en.pdf)美洲原住民语言的结构。
- [LRL-B-18-035｜Multilingualism: Learning and using multiple languages and varieties](../books/Berthele_Multilingualism_2026_en.pdf)Multilingualism。
- [LRL-B-18-036｜Linguistics Olympiad: Training guide](../books/Neacsu_LinguisticsOlympiadTrainingGuide_2024_en.pdf)语言学奥赛训练指南：适合训练分析陌生语言。

入门读物：[LRL-B-18-024｜Language and Computers](../books/Glass_LanguageAndComputers_2024_en.pdf)Language and Computers。

论文，接到 LLM 时代的语言学问题：
- 形态与 LLM：
  - [LRL-P-02-001｜Evaluating Morphological Compositional Generalization in Large Languag](../papers/2024_Ismayilzada_EvaluatingMorphologicalCompositional_en.pdf)形态组合泛化。
  - [LRL-P-02-003｜Counting the Bugs in ChatGPT's Wugs: A Multilingual Investigation into](../papers/2023_Weissweiler_CountingBugsChatGPTSWugs_en.pdf)多语言形态测试（经典补充）。
  - [LRL-P-02-045｜Improving Low-Resource Morphological Inflection via Self-Supervised Ob](../papers/2025_Wiemerslage_ImprovingLowResourceMorphological_en.pdf)。
- 类型学：
  - [LRL-P-02-018｜What is "Typological Diversity" in NLP?](../papers/2024_Ploeger_WhatTypologicalDiversity_en.pdf)NLP 中的“类型多样性”是什么。
  - [LRL-P-02-019｜A Principled Framework for Evaluating on Typologically Diverse Languag](../papers/2024_Ploeger_PrincipledFrameworkEvaluating_en.pdf)。
  - [LRL-P-02-016｜URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological](../papers/2024_Khan_URIEL_en.pdf)URIEL+。
  - [LRL-P-02-009｜Large Language Models Share Representations of Latent Grammatical Conc](../papers/2025_Brinkmann_LargeLanguageModelsShare_en.pdf)跨类型共享语法概念表示。
  - [LRL-P-02-051｜LLM Agents as Computational Typologists](../papers/2026_Yang_LLMAgentsComputationalTypologists_en.pdf)LLM 智能体作为计算类型学家。
- 文字：
  - [LRL-P-02-054｜Unknown Script: Impact of Script on Cross-Lingual Transfer](../papers/2024_Tufa_UnknownScript_en.pdf)。
  - [LRL-P-02-055｜Multilingual Language Models Encode Script Over Linguistic Structure](../papers/2026_Verma_MultilingualLanguageModels_en.pdf)模型编码文字多于语言结构。
  - [LRL-P-02-025｜Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin](../papers/2024_Nguyen_PromptingWithPhonemes_en.pdf)。
- 方言与语码转换：
  - [LRL-P-02-026｜Natural Language Processing for Dialects of a Language: A Survey](../papers/2024_Joshi_NaturalLanguageProcessing_en.pdf)方言 NLP 综述。
  - [LRL-P-02-027｜DIALECTBENCH: A NLP Benchmark for Dialects, Varieties, and Closely-Rel](../papers/2024_Faisal_DIALECTBENCH_en.pdf)DIALECTBENCH。
  - [LRL-P-02-059｜Beyond Monolingual Assumptions: A Survey of Code-Switched NLP in the E](../papers/2025_Sheth_BeyondMonolingualAssumptions_en.pdf)语码转换综述。
  - [LRL-P-02-032｜Lost in the Mix: Evaluating LLM Understanding of Code-Switched Text](../papers/2025_Mohamed_LostInTheMix_en.pdf)。
- 语言态度与偏见：
  - [LRL-P-02-028｜Dialect prejudice predicts AI decisions about people's character, empl](../papers/2024_Hofmann_DialectPrejudicePredicts_en.pdf)方言偏见。
  - [LRL-P-02-029｜Standard Language Ideology in AI-Generated Language](../papers/2024_Smith_StandardLanguageIdeology_en.pdf)标准语意识形态。

## 第 5 阶段：多语言学习、机器翻译与低资源 NLP

课程：
- [LRL-C-17-041｜Multilingual Natural Language Processing](../university_materials/CMU_11-737_MultilingualNLP_2023Fall_LectureMaterials_en)CMU 11-737 多语言 NLP（2023 秋，核心）。
- [LRL-C-17-043｜Multilingual Natural Language Processing](../university_materials/CUNI_NPFL120_MultilingualNLP_2026Summer_LectureMaterials_en)Charles NPFL120 多语言 NLP。
- [LRL-C-17-052｜NLP for Low-Resource and Marginalized Language Varieties](../university_materials/UZH_LowResourceMarginalizedVarietiesNLP_2026Spring_LectureMaterials_en)UZH 低资源与边缘语言变体 NLP（2026）。
- [LRL-C-17-046｜Subword Modeling](../university_materials/CMU_11-824_SubwordModeling_2026Spring_LectureMaterials_en)CMU 子词建模。
- 机器翻译：
  - [LRL-C-17-042｜Machine Translation](../university_materials/JHU_601-468_MachineTranslation_2026Fall_LectureMaterials_en)JHU 601.468。
  - [LRL-C-17-044｜Statistical Machine Translation](../university_materials/CUNI_NPFL087_StatisticalMT_2026Summer_LectureMaterials_en)Charles NPFL087。
  - [LRL-C-17-045｜Machine Translation (Vorlesung + Übung)](../university_materials/LMU_MachineTranslation_2023Summer_LectureMaterials_en)LMU。

书：
- [LRL-B-18-028｜机器翻译：基础与模型](../books/Xiao_JiQiFanYiJiChuYuMoXing_2024_cn.pdf)《机器翻译：基础与模型》。
- [LRL-B-18-029｜Machine translation for everyone: Empowering users in the age of artif](../books/Kenny_MachineTranslationForEveryone_2022_en.pdf)Machine Translation for Everyone。
- [LRL-B-18-030｜European Language Equality: A Strategic Agenda for Digital Language Eq](../books/Rehm_EuropeanLanguageEquality_2023_en.pdf)European Language Equality。

论文（第 01 类中与跨语言相关的基础）：
- [LRL-P-01-044｜Understanding Cross-Lingual Alignment -- A Survey](../papers/2024_Hammerl_UnderstandingCrossLingual_en.pdf)跨语言对齐综述。
- [LRL-P-01-040｜The Semantic Hub Hypothesis: Language Models Share Semantic Representa](../papers/2024_Wu_TheSemanticHubHypothesis_en.pdf)Semantic Hub 假说。
- [LRL-P-01-033｜LLMs Are Few-Shot In-Context Low-Resource Language Learners](../papers/2024_Cahyawijaya_LLMsFewShotContextLowResource_en.pdf)LLM 作为低资源语言的少样本学习者。
- [LRL-P-01-066｜On the Calibration of Multilingual Question Answering LLMs](../papers/2023_Yang_CalibrationMultilingualQuestion_en.pdf)多语言问答的校准。

## 第 6 阶段：接入专题

学完以上内容后，可按目标进入以下指南：
- data_pipeline_cn.md
- model_adaptation_cn.md
- evaluation_cn.md
- application_development_cn.md
- deployment_cn.md

规模规律与数据受限训练，是理解“小语种数据少”这一问题的理论入口：
- [LRL-P-01-007｜Scaling Laws for Mixture Pretraining Under Data Constraints](../papers/2026_Sedova_ScalingLawsMixturePretraining_en.pdf)。
- [LRL-P-01-014｜Scaling Data-Constrained Language Models](../papers/2023_Muennighoff_ScalingDataConstrainedLanguage_en.pdf)。
- [LRL-P-01-005｜Scaling Laws for Downstream Task Performance of Large Language Models](../papers/2024_Isik_ScalingLawsDownstreamTask_en.pdf)。
