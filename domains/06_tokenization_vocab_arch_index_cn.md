# 06 分词、词表与模型架构：资料索引

由 `scripts/build_catalog_en.py` 自动生成；字段详见 `catalog_cn.csv`。本类主分类 57 条，交叉标签 56 条。

已核验完整资料 57 / 目标约 50；待核验 0；下载失败 0。近三年 53/57（93.0%）；直接相关 50，通用支撑 7；已有复用 4。

| 编号 | 优先 | 首次公开 | 相关性 | 标题 | 本地路径 |
|---|---|---|---|---|---|
| LRL-P-06-022 | 1 | 2025-08-06 | 直接相关 | Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization | [2025_Foroutan_ParityAwareBytePairEncoding_en.pdf](../papers/2025_Foroutan_ParityAwareBytePairEncoding_en.pdf) |
| LRL-P-06-015 | 2 | 2025-06-12 | 直接相关 | One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers | [2025_Abagyan_OneTokenizerRuleThemAllEmergent_en.pdf](../papers/2025_Abagyan_OneTokenizerRuleThemAllEmergent_en.pdf) |
| LRL-P-06-014 | 3 | 2026-06-13 | 直接相关 | Equity with Efficiency: An Empirical Study of Tokenizers for Multilingual Large Language M | [2026_Lee_EquityWithEfficiency_en.pdf](../papers/2026_Lee_EquityWithEfficiency_en.pdf) |
| LRL-P-06-005 | 4 | 2024-11-21 | 直接相关 | Why do language models perform worse for morphologically complex languages? | [2024_Arnett_WhyDoLanguageModelsPerform_en.pdf](../papers/2024_Arnett_WhyDoLanguageModelsPerform_en.pdf) |
| LRL-P-06-021 | 5 | 2024-03-15 | 直接相关 | MYTE: Morphology-Driven Byte Encoding for Better and Fairer Multilingual Language Modeling | [2024_Limisiewicz_MYTE_en.pdf](../papers/2024_Limisiewicz_MYTE_en.pdf) |
| LRL-P-06-020 | 6 | 2024-07-11 | 直接相关 | MAGNET: Improving the Multilingual Fairness of Language Models with Adaptive Gradient-Base | [2024_Ahia_MAGNET_en.pdf](../papers/2024_Ahia_MAGNET_en.pdf) |
| LRL-P-06-027 | 7 | 2024-06-17 | 直接相关 | How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text? | [2024_Yamaguchi_HowCanEffectivelyExpandVocabulary_en.pdf](../papers/2024_Yamaguchi_HowCanEffectivelyExpandVocabulary_en.pdf) |
| LRL-P-06-032 | 8 | 2024-05-13 | 直接相关 | Zero-Shot Tokenizer Transfer | [2024_Minixhofer_ZeroShotTokenizerTransfer_en.pdf](../papers/2024_Minixhofer_ZeroShotTokenizerTransfer_en.pdf) |
| LRL-P-06-051 | 9 | 2024-12-13 | 通用支撑 | Byte Latent Transformer: Patches Scale Better Than Tokens | [2024_Pagnoni_ByteLatentTransformer_en.pdf](../papers/2024_Pagnoni_ByteLatentTransformer_en.pdf) |
| LRL-P-06-064 | 10 | 2024-01-25 | 直接相关 | RomanSetu: Efficiently unlocking multilingual capabilities of Large Language Models via Ro | [2024_Husain_RomanSetu_en.pdf](../papers/2024_Husain_RomanSetu_en.pdf) |
| LRL-P-06-001 |  | 2025-09-05 | 直接相关 | The Token Tax: Systematic Bias in Multilingual Tokenization | [2025_Lundin_TheTokenTax_en.pdf](../papers/2025_Lundin_TheTokenTax_en.pdf) |
| LRL-P-06-002 |  | 2026-06-23 | 直接相关 | The African Language Tax: Quantifying the Cost, Latency, and Context Penalty of Tokenizing | [2026_Somide_TheAfricanLanguageTax_en.pdf](../papers/2026_Somide_TheAfricanLanguageTax_en.pdf) |
| LRL-P-06-004 |  | 2026-07-27 | 直接相关 | The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenizati | [2026_Srivastava_TheTokenizerTax_en.pdf](../papers/2026_Srivastava_TheTokenizerTax_en.pdf) |
| LRL-P-06-006 |  | 2025-07-08 | 直接相关 | Evaluating Morphological Alignment of Tokenizers in 70 Languages | [2025_Arnett_EvaluatingMorphologicalAlignment_en.pdf](../papers/2025_Arnett_EvaluatingMorphologicalAlignment_en.pdf) |
| LRL-P-06-007 |  | 2025-03-18 | 直接相关 | Splintering Nonconcatenative Languages for Better Tokenization | [2025_Gazit_SplinteringNonconcatenative_en.pdf](../papers/2025_Gazit_SplinteringNonconcatenative_en.pdf) |
| LRL-P-06-008 |  | 2024-10-15 | 直接相关 | Tokenization and Morphology in Multilingual Language Models: A Comparative Analysis of mT5 | [2024_Dang_TokenizationMorphologyMultilingual_en.pdf](../papers/2024_Dang_TokenizationMorphologyMultilingual_en.pdf) |
| LRL-P-06-010 |  | 2024-11-19 | 直接相关 | Evaluating Tokenizer Performance of Large Language Models Across Official Indian Languages | [2024_Tamang_EvaluatingTokenizerPerformance_en.pdf](../papers/2024_Tamang_EvaluatingTokenizerPerformance_en.pdf) |
| LRL-P-06-012 |  | 2024-03-26 | 直接相关 | Introducing Syllable Tokenization for Low-resource Languages: A Case Study with Swahili | [2024_Atuhurra_IntroducingSyllableTokenization_en.pdf](../papers/2024_Atuhurra_IntroducingSyllableTokenization_en.pdf) |
| LRL-P-06-013 |  | 2024-02-28 | 通用支撑 | Tokenization Is More Than Compression | [2024_Schmidt_TokenizationMoreThanCompression_en.pdf](../papers/2024_Schmidt_TokenizationMoreThanCompression_en.pdf) |
| LRL-P-06-016 |  | 2025-11-05 | 直接相关 | MUTANT: A Recipe for Multilingual Tokenizer Design | [2025_Rana_MUTANT_en.pdf](../papers/2025_Rana_MUTANT_en.pdf) |
| LRL-P-06-018 |  | 2025-10-07 | 直接相关 | Parallel Tokenizers: Rethinking Vocabulary Design in Cross-Lingual Transfer of Low-Resourc | [2025_Kautsar_ParallelTokenizers_en.pdf](../papers/2025_Kautsar_ParallelTokenizers_en.pdf) |
| LRL-P-06-024 |  | 2024-02-22 | 直接相关 | Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models | [2024_Kim_EfficientEffectiveVocabulary_en.pdf](../papers/2024_Kim_EfficientEffectiveVocabulary_en.pdf) |
| LRL-P-06-026 |  | 2024-02-16 | 直接相关 | An Empirical Study on Cross-lingual Vocabulary Adaptation for Efficient Language Model Inf | [2024_Yamaguchi_EmpiricalStudyCrossLingual_en.pdf](../papers/2024_Yamaguchi_EmpiricalStudyCrossLingual_en.pdf) |
| LRL-P-06-030 |  | 2024-10-12 | 直接相关 | Adapters for Altering LLM Vocabularies: What Languages Benefit the Most? | [2024_Han_AdaptersAlteringLLMVocabularies_en.pdf](../papers/2024_Han_AdaptersAlteringLLMVocabularies_en.pdf) |
| LRL-P-06-031 |  | 2024-08-08 | 直接相关 | Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for | [2024_Remy_TransTokenizationCrossLingual_en.pdf](../papers/2024_Remy_TransTokenizationCrossLingual_en.pdf) |
| LRL-P-06-033 |  | 2023-11-15 | 直接相关 | OFA: A Framework of Initializing Unseen Subword Embeddings for Efficient Large-scale Multi | [2023_Liu_OFA_en.pdf](../papers/2023_Liu_OFA_en.pdf) |
| LRL-P-06-035 |  | 2024-04-03 | 直接相关 | ANGOFA: Leveraging OFA Embedding Initialization and Synthetic Data for Angolan Language Mo | [2024_Quinjica_ANGOFA_en.pdf](../papers/2024_Quinjica_ANGOFA_en.pdf) |
| LRL-P-06-036 |  | 2025-06-02 | 直接相关 | Dictionaries to the Rescue: Cross-Lingual Vocabulary Transfer for Low-Resource Languages U | [2025_Sakajo_DictionariesToTheRescue_en.pdf](../papers/2025_Sakajo_DictionariesToTheRescue_en.pdf) |
| LRL-P-06-038 |  | 2023-12-05 | 直接相关 | Impact of Tokenization on LLaMa Russian Adaptation | [2023_Tikhomirov_ImpactTokenizationLLaMaRussian_en.pdf](../papers/2023_Tikhomirov_ImpactTokenizationLLaMaRussian_en.pdf) |
| LRL-P-06-039 |  | 2024-12-16 | 直接相关 | Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion | [2024_Zhu_SecondLanguageArabicAcquisition_en.pdf](../papers/2024_Zhu_SecondLanguageArabicAcquisition_en.pdf) |
| LRL-P-06-043 |  | 2026-07-16 | 直接相关 | Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and | [2026_Teklehaymanot_ExpandingLexiconGeEzBased_en.pdf](../papers/2026_Teklehaymanot_ExpandingLexiconGeEzBased_en.pdf) |
| LRL-P-06-046 |  | 2024-01-19 | 直接相关 | Accelerating Multilingual Language Model for Excessively Tokenized Languages | [2024_Hong_AcceleratingMultilingual_en.pdf](../papers/2024_Hong_AcceleratingMultilingual_en.pdf) |
| LRL-P-06-047 |  | 2024-07-18 | 通用支撑 | Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies | [2024_Tao_ScalingLawsWithVocabulary_en.pdf](../papers/2024_Tao_ScalingLawsWithVocabulary_en.pdf) |
| LRL-P-06-048 |  | 2024-07-09 | 直接相关 | Adapting LLMs to Hebrew: Unveiling DictaLM 2.0 with Enhanced Vocabulary and Instruction Ca | [2024_Shmidman_AdaptingLLMsToHebrew_en.pdf](../papers/2024_Shmidman_AdaptingLLMsToHebrew_en.pdf) |
| LRL-P-06-049 |  | 2025-06-04 | 直接相关 | TokAlign: Efficient Vocabulary Adaptation via Token Alignment | [2025_Li_TokAlign_en.pdf](../papers/2025_Li_TokAlign_en.pdf) |
| LRL-P-06-050 |  | 2024-01-24 | 通用支撑 | MambaByte: Token-free Selective State Space Model | [2024_Wang_MambaByte_en.pdf](../papers/2024_Wang_MambaByte_en.pdf) |
| LRL-P-06-052 |  | 2024-04-22 | 通用支撑 | SpaceByte: Towards Deleting Tokenization from Large Language Modeling | [2024_Slagle_SpaceByte_en.pdf](../papers/2024_Slagle_SpaceByte_en.pdf) |
| LRL-P-06-053 |  | 2024-10-28 | 直接相关 | MrT5: Dynamic Token Merging for Efficient Byte-level Language Models | [2024_Kallini_MrT5_en.pdf](../papers/2024_Kallini_MrT5_en.pdf) |
| LRL-P-06-054 |  | 2025-01-17 | 通用支撑 | Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Ro | [2025_Neitemeier_HierarchicalAutoregressive_en.pdf](../papers/2025_Neitemeier_HierarchicalAutoregressive_en.pdf) |
| LRL-P-06-055 |  | 2025-07-10 | 通用支撑 | Dynamic Chunking for End-to-End Hierarchical Sequence Modeling | [2025_Hwang_DynamicChunkingEndEndHierarchical_en.pdf](../papers/2025_Hwang_DynamicChunkingEndEndHierarchical_en.pdf) |
| LRL-P-06-056 |  | 2025-08-07 | 直接相关 | H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologi | [2025_Zakershahrak_HNet_en.pdf](../papers/2025_Zakershahrak_HNet_en.pdf) |
| LRL-P-06-058 |  | 2025-05-21 | 直接相关 | BanglaByT5: Byte-Level Modelling for Bangla | [2025_Bhattacharyya_BanglaByT5_en.pdf](../papers/2025_Bhattacharyya_BanglaByT5_en.pdf) |
| LRL-P-06-059 |  | 2025-06-09 | 直接相关 | Bit-level BPE: Below the byte boundary | [2025_Moon_BitLevelBPE_en.pdf](../papers/2025_Moon_BitLevelBPE_en.pdf) |
| LRL-P-06-060 |  | 2024-04-12 | 直接相关 | Measuring Cross-lingual Transfer in Bytes | [2024_Souza_MeasuringCrossLingualTransfer_en.pdf](../papers/2024_Souza_MeasuringCrossLingualTransfer_en.pdf) |
| LRL-P-06-061 |  | 2025-05-27 | 直接相关 | Multilingual Pretraining for Pixel Language Models | [2025_Kesen_MultilingualPretrainingPixel_en.pdf](../papers/2025_Kesen_MultilingualPretrainingPixel_en.pdf) |
| LRL-P-06-062 |  | 2025-04-02 | 直接相关 | Overcoming Vocabulary Constraints with Pixel-level Fallback | [2025_Lotz_OvercomingVocabularyConstraints_en.pdf](../papers/2025_Lotz_OvercomingVocabularyConstraints_en.pdf) |
| LRL-P-06-063 |  | 2026-03-29 | 直接相关 | KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter | [2026_Akylzhanov_KazByte_en.pdf](../papers/2026_Akylzhanov_KazByte_en.pdf) |
| LRL-P-06-065 |  | 2024-01-12 | 直接相关 | TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual  | [2024_Liu_TransliCo_en.pdf](../papers/2024_Liu_TransliCo_en.pdf) |
| LRL-P-06-067 |  | 2024-06-28 | 直接相关 | Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliterati | [2024_Xhelili_BreakingScriptBarrierMultilingual_en.pdf](../papers/2024_Xhelili_BreakingScriptBarrierMultilingual_en.pdf) |
| LRL-P-06-068 |  | 2025-09-22 | 直接相关 | Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Appro | [2025_Zhuang_EnhancingCrossLingualTransfer_en.pdf](../papers/2025_Zhuang_EnhancingCrossLingualTransfer_en.pdf) |
| LRL-P-06-070 |  | 2024-09-26 | 直接相关 | LangSAMP: Language-Script Aware Multilingual Pretraining | [2024_Liu_LangSAMP_en.pdf](../papers/2024_Liu_LangSAMP_en.pdf) |
| LRL-P-06-072 |  | 2025-06-14 | 直接相关 | Group then Scale: Dynamic Mixture-of-Experts Multilingual Language Model | [2025_Li_GroupThenScale_en.pdf](../papers/2025_Li_GroupThenScale_en.pdf) |
| LRL-P-06-073 |  | 2025-10-06 | 直接相关 | Multilingual Routing in Mixture-of-Experts | [2025_Bandarkar_MultilingualRoutingMixture_en.pdf](../papers/2025_Bandarkar_MultilingualRoutingMixture_en.pdf) |
| LRL-P-06-075 |  | 2023-05-17 | 直接相关 | Language Model Tokenizers Introduce Unfairness Between Languages | [2023_Petrov_LanguageModelTokenizersIntroduce_en.pdf](../papers/2023_Petrov_LanguageModelTokenizersIntroduce_en.pdf) |
| LRL-P-06-076 |  | 2023-05-23 | 直接相关 | Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models | [2023_Ahia_DoAllLanguagesCostSameTokenization_en.pdf](../papers/2023_Ahia_DoAllLanguagesCostSameTokenization_en.pdf) |
| LRL-P-06-077 |  | 2023-05-23 | 直接相关 | FOCUS: Effective Embedding Initialization for Monolingual Specialization of Multilingual M | [2023_Dobler_FOCUS_en.pdf](../papers/2023_Dobler_FOCUS_en.pdf) |
| LRL-P-06-078 |  | 2021-12-13 | 直接相关 | WECHSEL: Effective initialization of subword embeddings for cross-lingual transfer of mono | [2021_Minixhofer_WECHSEL_en.pdf](../papers/2021_Minixhofer_WECHSEL_en.pdf) |

## 交叉标签（主分类在别类）

- LRL-P-03-001（主类 03 多语言及低资源语言大模型）MaLA-500: Massive Language Adaptation of Large Language Models — 依据：方法核心为词表扩展（06）与持续预训练（07）
- LRL-P-03-006（主类 03 多语言及低资源语言大模型）LOLA -- An Open-Source Massively Multilingual Large Language Model — 依据：采用 MoE 架构
- LRL-P-03-010（主类 03 多语言及低资源语言大模型）Breaking the Curse of Multilinguality with Cross-lingual Expert Language Models — 依据：语言专家模块化结构；07类：主分类由 03 类先行列入；本类仅作交叉标签：其核心内容涉及持续预训练/语言适配（07）
- LRL-P-03-020（主类 03 多语言及低资源语言大模型）SeaLLMs -- Large Language Models for Southeast Asia — 依据：含词表扩展
- LRL-P-03-025（主类 03 多语言及低资源语言大模型）Typhoon: Thai Large Language Models — 依据：含泰文词表扩展
- LRL-P-03-032（主类 03 多语言及低资源语言大模型）Tamil-Llama: A New Tamil Language Model Based on Llama 2 — 依据：含词表扩展
- LRL-P-03-033（主类 03 多语言及低资源语言大模型）Paramanu: Compact and Competitive Monolingual Language Models for Low-Resource Morphologic — 依据：专用分词器；07类：主分类由 03 类先行列入；本类仅作交叉标签：其核心内容涉及持续预训练/语言适配（07）
- LRL-P-03-039（主类 03 多语言及低资源语言大模型）PersianMind: A Cross-Lingual Persian-English Large Language Model — 依据：词表扩展
- LRL-P-03-049（主类 03 多语言及低资源语言大模型）LlamaTurk: Adapting Open-Source Generative Large Language Models for Low-Resource Language — 依据：含词表扩展比较
- LRL-P-03-060（主类 03 多语言及低资源语言大模型）Nile-Chat: Egyptian Language Models for Arabic and Latin Scripts — 依据：双文字与 MoE 合并
- LRL-P-03-072（主类 03 多语言及低资源语言大模型）SinLlama -- A Large Language Model for Sinhala — 依据：含词表扩展；07类：主分类已由 03 类认领（03-072）；本类仅作交叉标签：方法为词表扩展+持续预训练（07）
- LRL-P-04-059（主类 04 语料来源、治理与许可）SomaliWeb v1: A Quality-Filtered Somali Web Corpus with a Matched Tokenizer and a Public L — 依据：含质量过滤与 LID 基准（05）及配套分词器（06）
- LRL-P-05-022（主类 05 数据处理与质量）What Language is This? Ask Your Tokenizer — 依据：基于分词器
- LRL-P-05-033（主类 05 数据处理与质量）Don't Touch My Diacritics — 依据：影响分词
- LRL-P-05-067（主类 05 数据处理与质量）Yorùbá in Unicode: An Overview of a Problem — 依据：影响分词与文本表示
- LRL-P-07-003（主类 07 预训练与持续预训练）Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language Capab — 依据：含日语词表扩展（06）
- LRL-P-07-005（主类 07 预训练与持续预训练）Efficiently Adapting Pretrained Language Models To New Languages — 依据：涉及词表扩展（06）
- LRL-P-07-029（主类 07 预训练与持续预训练）Bilingual Adaptation of Monolingual Foundation Models — 依据：06类：主分类已由 07 认领（07-029）；本类仅作交叉标签：阿拉伯语适配中的词表扩展与嵌入初始化，与 06 的分词/词表/架构主题直接相关。
- LRL-P-07-044（主类 07 预训练与持续预训练）MoE-LPR: Multilingual Extension of Large Language Models through Mixture-of-Experts with L — 依据：架构扩展（06）
- LRL-P-07-056（主类 07 预训练与持续预训练）Exploring Design Choices for Building Language-Specific LLMs — 依据：词表扩展（06）
- LRL-P-07-065（主类 07 预训练与持续预训练）SambaLingo: Teaching Large Language Models New Languages — 依据：词表扩展与嵌入初始化（06）
- LRL-P-07-066（主类 07 预训练与持续预训练）Adapting Chat Language Models Using Only Target Unlabeled Language Data — 依据：保持指令/对话能力（08）；06类：主分类已由 07 认领（07-066）；本类仅作交叉标签：对话模型在只有目标语言无标注数据时的词表扩展，与 06 的分词/词表/架构主题直接相关。
- LRL-P-08-027（主类 08 指令微调与参数高效适配）Franken-Adapter: Cross-Lingual Adaptation of LLMs by Embedding Surgery — 依据：嵌入/词表替换（06）
- LRL-P-08-032（主类 08 指令微调与参数高效适配）Exploring the Role of Transliteration in In-Context Learning for Low-resource Languages Wr — 依据：文字系统（02）；06类：主分类已由 08 认领（08-032）；本类仅作交叉标签：非拉丁文字低资源语言的转写（文字处理）研究，与 06 的分词/词表/架构主题直接相关。
- LRL-P-16-025（主类 16 高效训练、推理与部署）The Ups and Downs of Large Language Model Inference with Vocabulary Trimming by Language H — 依据：涉及词表
- LRL-P-16-032（主类 16 高效训练、推理与部署）Double Jeopardy and Climate Impact in the Use of Large Language Models: Socio-economic Dis — 依据：以分词长度差异为成因
- LRL-P-16-033（主类 16 高效训练、推理与部署）The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multil — 依据：以分词长度差异为成因
- LRL-P-16-034（主类 16 高效训练、推理与部署）Measuring the Tokenization Premium: A Cost Audit for Underserved Language Communities — 依据：以分词长度差异为成因
- LRL-P-16-035（主类 16 高效训练、推理与部署）Removable and Irreducible: A Token-Cost Ledger for the Multilingual Tokenization Tax — 依据：以分词长度差异为成因
- LRL-P-16-067（主类 16 高效训练、推理与部署）Optimizing Korean-Centric LLMs via Token Pruning — 依据：词表
- LRL-C-17-002（主类 17 大学官方教材与完整课程讲义）Language Modeling from Scratch — 依据：
- LRL-C-17-003（主类 17 大学官方教材与完整课程讲义）Transformers & Large Language Models — 依据：
- LRL-C-17-011（主类 17 大学官方教材与完整课程讲义）Natural Language Processing — 依据：
- LRL-C-17-016（主类 17 大学官方教材与完整课程讲义）Advanced Natural Language Processing — 依据：
- LRL-C-17-017（主类 17 大学官方教材与完整课程讲义）Natural Language Processing (LM-class) — 依据：
- LRL-C-17-031（主类 17 大学官方教材与完整课程讲义）Introduction to Machine Learning — 依据：
- LRL-C-17-032（主类 17 大学官方教材与完整课程讲义）Introduction to Deep Learning — 依据：
- LRL-C-17-033（主类 17 大学官方教材与完整课程讲义）Deep Learning — 依据：
- LRL-C-17-034（主类 17 大学官方教材与完整课程讲义）Introduction to Machine Learning — 依据：
- LRL-C-17-036（主类 17 大学官方教材与完整课程讲义）Advanced Machine Learning — 依据：
- LRL-C-17-041（主类 17 大学官方教材与完整课程讲义）Multilingual Natural Language Processing — 依据：
- LRL-C-17-043（主类 17 大学官方教材与完整课程讲义）Multilingual Natural Language Processing — 依据：
- LRL-C-17-045（主类 17 大学官方教材与完整课程讲义）Machine Translation (Vorlesung + Übung) — 依据：
- LRL-C-17-046（主类 17 大学官方教材与完整课程讲义）Subword Modeling — 依据：
- LRL-C-17-047（主类 17 大学官方教材与完整课程讲义）Morphological and Syntactic Analysis — 依据：
- LRL-C-17-065（主类 17 大学官方教材与完整课程讲义）Systems for Machine Learning — 依据：
- LRL-B-18-004（主类 18 完整教科书、专著与参考书）Information Theory, Inference, and Learning Algorithms — 依据：
- LRL-B-18-011（主类 18 完整教科书、专著与参考书）Understanding Deep Learning — 依据：
- LRL-B-18-012（主类 18 完整教科书、专著与参考书）Dive into Deep Learning — 依据：
- LRL-B-18-014（主类 18 完整教科书、专著与参考书）The Little Book of Deep Learning — 依据：
- LRL-B-18-015（主类 18 完整教科书、专著与参考书）Alice's Adventures in a Differentiable Wonderland — 依据：
- LRL-B-18-018（主类 18 完整教科书、专著与参考书）Speech and Language Processing — 依据：
- LRL-B-18-022（主类 18 完整教科书、专著与参考书）Representation Learning for Natural Language Processing — 依据：
- LRL-B-18-023（主类 18 完整教科书、专著与参考书）Natural Language Processing: Neural Networks and Large Language Models — 依据：
- LRL-B-18-033（主类 18 完整教科书、专著与参考书）The Unicode Cookbook for Linguists: Managing writing systems using orthography profiles — 依据：
- LRL-B-18-040（主类 18 完整教科书、专著与参考书）大语言模型 — 依据：
