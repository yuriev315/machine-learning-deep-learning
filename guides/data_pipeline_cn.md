# 数据流水线学习与设计指南

适用路线：A（现有基座持续预训练/指令微调）、C（从头预训练）。路线 B（检索与工具）的知识库构建也复用其中的“来源—授权—清洗—版本”环节。

阅读说明：
- 本指南只依据库内已下载并核验的资料，链接均指向本地文件。
- 论文结论均为作者在其实验条件下的报告。不同语言、文字、语料规模之间不能直接外推。
- 每篇论文涉及的语言、文字、资源条件，见 `catalog_cn.csv` 中的“涉及语言”“文字系统”“资源条件”列。
- 本指南不给出配置参数或硬件预算。

流程总览：

```
语料来源 → 授权与合规 → 语言识别 → 规范化/OCR 修复 → 去重 → 质量筛选 → 语言配比 → 数据版本与评测隔离
   04          04            05           05             05        05          05/07/01         05/15 + 工程
```

## 1. 语料来源（输入：目标语言清单；产出：候选来源表）

先回答三个问题：
- 目标语言在公开网页里有多少文本？
- 是否有高质量的非网页来源，如书籍、档案、政府出版物、广播转写？
- 有没有平行语料？

大规模多语言网页语料的构建方法与覆盖情况：
- [LRL-P-04-001｜FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data](../papers/2025_Penedo_FineWeb2_en.pdf)FineWeb2：按语言调整处理流水线、覆盖上千语言。
- [LRL-P-04-002｜An Expanded Massive Multilingual Dataset for High-Performance Language](../papers/2025_Burchell_ExpandedMassiveMultilingual_en.pdf)HPLT 扩展数据集：单语加平行语料。
- [LRL-P-04-005｜GlotCC: An Open Broad-Coverage CommonCrawl Corpus and Pipeline for Min](../papers/2024_Kargaran_GlotCC_en.pdf)GlotCC：面向少数语言的 CommonCrawl 语料。
- [LRL-P-04-008｜IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning D](../papers/2024_Khan_IndicLLMSuite_en.pdf)IndicLLMSuite：一个语区从预训练到指令数据的完整蓝图。

非网页来源与数字化：
- [LRL-P-04-036｜Design Considerations in Low-Resource Archival OCR: A Case Study in La](../papers/2026_Wright_DesignConsiderationsLowResource_en.pdf)拉科塔语档案 OCR 案例。
- [LRL-P-04-035｜Developing an English-Efik Corpus and Machine Translation System for D](../papers/2026_Edet_DevelopingEnglishEfikCorpus_en.pdf)Efik 语数字化语料。
- [LRL-P-05-016｜olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Mod](../papers/2025_Poznanski_OlmOCR_en.pdf)olmOCR：从 PDF 抽取训练文本。
- [LRL-P-05-037｜Institutional Books - Enriched Text: A customizable multilingual open-](../papers/2026_LowryDuda_InstitutionalBooksEnriched_en.pdf)机构藏书语料流水线。

特定社区或语种的语料案例：
- [LRL-P-04-006｜MC$^2$: Towards Transparent and Culturally-Aware NLP for Minority Lang](../papers/2023_Zhang_MC2_en.pdf)MC²：中国少数民族语言。
- [LRL-P-04-038｜The Esethu Framework: Reimagining Sustainable Dataset Governance and C](../papers/2025_Rajab_TheEsethuFramework_en.pdf)Esethu：科萨语的数据治理框架。

注意：
- “小语种”不等于“低资源”。有的语言使用人口少，但数字文本丰富；有的语言使用人口多，但网页文本稀少。
- 记录来源时，同时写明语言变体、文字（同一语言可能有多种文字）和文本是否自然产生。

## 2. 授权、隐私与社区参与（产出：许可清单、数据卡、排除规则）

许可与来源追踪：
- [LRL-P-04-019｜Bridging the Data Provenance Gap Across Text, Speech and Video](../papers/2024_Longpre_BridgingDataProvenanceGap_en.pdf)跨模态数据来源缺口。
- [LRL-P-04-017｜Consent in Crisis: The Rapid Decline of the AI Data Commons](../papers/2024_Longpre_ConsentInCrisis_en.pdf)网页数据授权收缩（Consent in Crisis）。
- [LRL-P-04-020｜Do Not Trust Licenses You See: Dataset Compliance Requires Massive-Sca](../papers/2025_Kim_DoNotTrustLicensesYouSee_en.pdf)不要只信数据集声明的许可证。
- [LRL-P-04-022｜Tracing the Data Trail: A Survey of Data Provenance, Transparency and](../papers/2026_Hohensinner_TracingTheDataTrail_en.pdf)数据来源追踪综述。
- [LRL-P-04-023｜Compliance Rating Scheme: A Data Provenance Framework for Generative A](../papers/2025_Bohacek_ComplianceRatingScheme_en.pdf)合规评级框架。
- [LRL-P-04-039｜Open but Incompatible: A License Compatibility Analysis of Corpora for](../papers/2026_Gassen_OpenButIncompatible_en.pdf)低资源语料的许可证兼容性分析：以非洲语言为例。

公开许可语料的做法：
- [LRL-P-04-013｜The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licen](../papers/2025_Kandpal_TheCommonPileV01_en.pdf)Common Pile。
- [LRL-P-04-011｜GPT-NL Public Corpus: A Permissively Licensed, Dutch-First Dataset for](../papers/2026_Oort_GPTNLPublicCorpus_en.pdf)GPT-NL 公开语料。

社区与数据主权：
- [LRL-P-04-027｜Māori algorithmic sovereignty: idea, principles, and use](../papers/2023_Brown_MaoriAlgorithmicSovereignty_en.pdf)毛利算法主权。
- [LRL-P-04-026｜Socially Responsible Data for Large Multilingual Language Models](../papers/2024_Smart_SociallyResponsibleDataLarge_en.pdf)面向多语言 LLM 的社会责任数据。
- [LRL-P-04-029｜Modeling the Sacred: Considerations when Using Religious Texts in Natu](../papers/2024_Hutchinson_ModelingTheSacred_en.pdf)宗教文本使用的考量。

工具与清单：[LRL-P-04-024｜The Responsible Foundation Model Development Cheatsheet: A Review of T](../papers/2024_Longpre_ResponsibleFoundationModel_en.pdf)负责任基础模型开发速查表。

设计要点（来自上述文献的共性建议，非本库验证结论）：
- 逐来源记录许可证与获取方式。
- 区分“可训练”“仅可评测”“不可用”三类。
- 社区数据须明确使用边界与回馈方式。

## 3. 语言识别与近似语言区分（产出：带语言/文字标签的文档）

- [LRL-P-05-020｜CommonLID: Re-evaluating State-of-the-Art Language Identification Perf](../papers/2026_Suarez_CommonLID_en.pdf)CommonLID：在真实网页上重新评测语言识别系统。
- [LRL-P-05-019｜OpenLID-v3: Improving the Precision of Closely Related Language Identi](../papers/2026_Fedorova_OpenLIDV3_en.pdf)OpenLID-v3：提升近似语言区分精度。
- [LRL-P-05-047｜Multi-label Scandinavian Language Identification (SLIDE)](../papers/2025_Fedorova_MultiLabelScandinavianLanguage_en.pdf)斯堪的纳维亚多标签语言识别。
- [LRL-P-05-049｜ILID: Native Script Language Identification for Indian Languages](../papers/2025_Ingle_ILID_en.pdf)印度语言本文字识别。
- 罗马化与非正式书写：
  - [LRL-P-05-021｜Script-Agnostic Language Identification](../papers/2024_Agarwal_ScriptAgnosticLanguageIdentification_en.pdf)与文字无关的语言识别。
  - [LRL-P-05-045｜Improving Informally Romanized Language Identification](../papers/2025_Benton_ImprovingInformallyRomanized_en.pdf)非正式罗马化文本的语言识别。
- 语码转换文本：[LRL-P-05-001｜MaskLID: Code-Switching Language Identification through Iterative Mask](../papers/2024_Kargaran_MaskLID_en.pdf)MaskLID。
- 工程实现：
  - [LRL-E-02｜GlotLID](../reference_code/GlotLID_d63cc2f_original_en.tar.gz)GlotLID 仓库。
  - [LRL-E-01｜datatrove](../reference_code/datatrove_1977fbb_original_en.tar.gz)datatrove 中的语言过滤步骤。

检查项：
- 语言识别模型对目标语言及其“近邻语言”的混淆情况。
- 同一语言不同文字的处理方式。
- 低置信度文档是丢弃还是另存待审。

## 4. 规范化、文字与 OCR 噪声（产出：规范化后的文本与规则记录）

- Unicode 与正字法：
  - [LRL-B-18-033｜The Unicode Cookbook for Linguists: Managing writing systems using ort](../books/Moran_UnicodeCookbookForLinguists_2018_en.pdf)The Unicode Cookbook for Linguists。
  - [LRL-P-05-033｜Don't Touch My Diacritics](../papers/2024_Gorman_DonTTouchMyDiacritics_en.pdf)Don't Touch My Diacritics：讨论变音符处理不当对多语言模型的影响。
- OCR 后处理：
  - [LRL-P-05-035｜Reference-Based Post-OCR Processing with LLM for Precise Diacritic Tex](../papers/2024_Do_ReferenceBasedPostOCRProcessing_en.pdf)基于参考的历史文献变音符修复。
  - [LRL-P-05-036｜OCR Error Post-Correction with LLMs in Historical Documents: No Free L](../papers/2025_Kanerva_OCRErrorPostCorrectionLLMs_en.pdf)LLM 做 OCR 纠错的局限（No Free Lunches）。
  - [LRL-P-05-052｜KazakhOCR: A Synthetic Benchmark for Evaluating Multimodal Models in L](../papers/2026_Gagnier_KazakhOCR_en.pdf)哈萨克语 OCR 合成基准。
- 文字与跨语言迁移的关系（与第 6 类、第 2 类衔接）：
  - [LRL-P-02-054｜Unknown Script: Impact of Script on Cross-Lingual Transfer](../papers/2024_Tufa_UnknownScript_en.pdf)未知文字对跨语言迁移的影响。
  - [LRL-P-02-086｜One Script Instead of Hundreds? On Pretraining Romanized Encoder Langu](../papers/2026_Ebing_OneScriptInsteadHundreds_en.pdf)罗马化预训练。

注意：
- 规范化规则（如 NFC/NFKC、变音符、零宽字符）会改变分词与去重结果，须在数据版本中固定并记录。

## 5. 去重（产出：去重后的语料与去重报告）

- [LRL-P-05-056｜Deduplicating Training Data Makes Language Models Better](../papers/2021_Lee_DeduplicatingTrainingData_en.pdf)Deduplicating Training Data Makes Language Models Better（经典补充）。
- [LRL-P-05-015｜LSHBloom: Memory-efficient, Extreme-scale Document Deduplication](../papers/2024_Khan_LSHBloom_en.pdf)LSHBloom：大规模文档去重。
- [LRL-P-05-010｜Mix, MinHash, and Match: Cross-Source Agreement for Multilingual Pretr](../papers/2025_Alrashed_MixMinHashAndMatch_en.pdf)跨来源 MinHash 一致性。
- 工程实现：
  - [LRL-E-05｜text-dedup](../reference_code/text-dedup_7538f3e_original_en.tar.gz)text-dedup。
  - [LRL-E-01｜datatrove](../reference_code/datatrove_1977fbb_original_en.tar.gz)datatrove（MinHash/精确去重模块）。
  - [LRL-E-09｜dolma](../reference_code/dolma_fd22a34_original_en.tar.gz)dolma 工具链。

库内缺口：专门研究“多语言/低资源语言去重阈值差异”的论文较少，详见 README 缺口说明。

## 6. 质量筛选与机器翻译文本识别（产出：筛选后的语料与筛选器评估）

基于模型的多语言数据选择：
- [LRL-P-05-007｜Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](../papers/2025_Messmer_EnhancingMultilingualLLM_en.pdf)。
- [LRL-P-05-006｜Judging Quality Across Languages: A Multilingual Approach to Pretraini](../papers/2025_Ali_JudgingQualityAcrossLanguages_en.pdf)JQL：跨语言质量判断。

低资源语料审计：
- [LRL-P-05-026｜How Good is Your Wikipedia? Auditing Data Quality for Low-resource and](../papers/2024_Tatariya_HowGoodYourWikipediaAuditing_en.pdf)维基百科各语言版本质量审计。
- [LRL-P-05-005｜Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](../papers/2026_Suppa_CanAgentDebugWebCorpusAgentic_en.pdf)用智能体审计斯洛伐克语 FineWeb2。

机器翻译内容污染语料（区分自然文本与机器翻译文本的关键文献）：
- [LRL-P-05-004｜A Shocking Amount of the Web is Machine Translated: Insights from Mult](../papers/2024_Thompson_ShockingAmountWebMachine_en.pdf)A Shocking Amount of the Web is Machine Translated。
- [LRL-P-09-049｜Multilingual Language Model Pretraining using Machine-translated Data](../papers/2025_Wang_MultilingualLanguageModel_en.pdf)用机器翻译数据预训练的研究，对照阅读。

工程实现：
- [LRL-E-08｜data-juicer](../reference_code/data-juicer_abb9e49_original_en.tar.gz)data-juicer（算子化清洗与分析）。
- [LRL-E-01｜datatrove](../reference_code/datatrove_1977fbb_original_en.tar.gz)datatrove。

注意：
- 面向英语调好的启发式过滤规则（如停用词比例、标点规则）不能直接搬到其他文字或形态的语言上。
- 要按语言抽样，人工检查筛选结果。

## 7. 语言配比与数据混合（产出：配比方案与依据）

- 规模规律视角：
  - [LRL-P-01-007｜Scaling Laws for Mixture Pretraining Under Data Constraints](../papers/2026_Sedova_ScalingLawsMixturePretraining_en.pdf)数据受限下的混合预训练规模规律。
  - [LRL-P-01-014｜Scaling Data-Constrained Language Models](../papers/2023_Muennighoff_ScalingDataConstrainedLanguage_en.pdf)数据受限语言模型（经典补充，讨论重复训练轮次）。
  - [LRL-P-01-008｜Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Mode](../papers/2024_Ye_DataMixingLaws_en.pdf)Data Mixing Laws。
- 多语言视角：
  - [LRL-P-03-009｜When Is Multilinguality a Curse? Language Modeling for 250 High- and L](../papers/2023_Chang_WhenMultilingualityCurse_en.pdf)When Is Multilinguality a Curse?
  - [LRL-P-03-011｜ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Fi](../papers/2025_Longpre_ATLAS_en.pdf)ATLAS 多语言迁移规模规律。
- 持续预训练中的混合与重放见 model_adaptation_cn.md 第 3 节。

注意：
- 上述规模规律都在特定模型规模、语言集合与数据量下拟合，换语言或规模须重新验证。

## 8. 数据版本、审计与评测隔离（产出：可复现的数据版本、污染检查报告）

- 污染检测：
  - [LRL-P-05-017｜Data Contamination Can Cross Language Barriers](../papers/2024_Yao_DataContaminationCanCross_en.pdf)污染可以跨语言。
  - [LRL-P-05-038｜Obscuring Data Contamination Through Translation: Evidence from Arabic](../papers/2026_Abbas_ObscuringDataContamination_en.pdf)通过翻译掩盖污染（阿拉伯语语料）。
  - [LRL-P-05-063｜Contamination Report for Multilingual Benchmarks](../papers/2024_Ahuja_ContaminationReportMultilingual_en.pdf)多语言基准污染报告。
  - [LRL-P-05-064｜When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Tra](../papers/2026_Tan_WhenFloresBloomzWrong_en.pdf)FLORES 跨方向污染。
  - [LRL-P-05-043｜Benchmark Data Contamination of Large Language Models: A Survey](../papers/2024_Xu_BenchmarkDataContamination_en.pdf)污染综述。
- 版本与配比管理：
  - [LRL-E-06｜dvc](../reference_code/dvc_356dfa0_original_en.tar.gz)DVC。
  - [LRL-E-07｜datasets](../reference_code/datasets_efe6ea4_original_en.tar.gz)Hugging Face datasets。
  - [LRL-E-09｜dolma](../reference_code/dolma_fd22a34_original_en.tar.gz)dolma（数据混合配置）。

检查项：
- 评测集的原文与译文都要做 n-gram/近重复检测。注意翻译后的基准可能以另一种语言形式泄漏。
- 数据版本要固定：来源快照、过滤规则、规范化规则、配比。

## 推荐学习顺序

1. 课程：
   - [LRL-C-17-002｜Language Modeling from Scratch](../university_materials/Stanford_CS336_2026Spring_LectureMaterials_en)Stanford CS336：数据相关讲次，含过滤、去重、混合。
   - [LRL-C-17-052｜NLP for Low-Resource and Marginalized Language Varieties](../university_materials/UZH_LowResourceMarginalizedVarietiesNLP_2026Spring_LectureMaterials_en)UZH 低资源与边缘语言变体 NLP。
2. 必读论文：[LRL-P-04-001｜FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data](../papers/2025_Penedo_FineWeb2_en.pdf)→[LRL-P-05-020｜CommonLID: Re-evaluating State-of-the-Art Language Identification Perf](../papers/2026_Suarez_CommonLID_en.pdf)→[LRL-P-05-004｜A Shocking Amount of the Web is Machine Translated: Insights from Mult](../papers/2024_Thompson_ShockingAmountWebMachine_en.pdf)→[LRL-P-05-007｜Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](../papers/2025_Messmer_EnhancingMultilingualLLM_en.pdf)→[LRL-P-05-017｜Data Contamination Can Cross Language Barriers](../papers/2024_Yao_DataContaminationCanCross_en.pdf)。
3. 工程对照：[LRL-E-01｜datatrove](../reference_code/datatrove_1977fbb_original_en.tar.gz)→[LRL-E-08｜data-juicer](../reference_code/data-juicer_abb9e49_original_en.tar.gz)→[LRL-E-06｜dvc](../reference_code/dvc_356dfa0_original_en.tar.gz)。
