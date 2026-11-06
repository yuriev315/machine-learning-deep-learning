# Brief for annotation: 11 推理、长上下文与工具调用

## 11-001 | Language Models are Multilingual Chain-of-Thought Reasoners
- arXiv: 2210.03057  first public: 2022-10-06  latest: 2022-10-06  primary cat: cs.CL
- authors (12): Freda Shi; Mirac Suzgun; Markus Freitag; Xuezhi Wang; Suraj Srivats; Soroush Vosoughi ...
- seed subtopic: 多语言数学推理基准; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://github.com/google-research/url-nlp
- pages: 20

ABSTRACT: We evaluate the reasoning abilities of large language models in multilingual settings. We introduce the Multilingual Grade School Math (MGSM) benchmark, by manually translating 250 grade-school math problems from the GSM8K dataset (Cobbe et al., 2021) into ten typologically diverse languages. We find that the ability to solve MGSM problems via chain-of-thought prompting emerges with increasing model scale, and that models have strikingly strong multilingual reasoning abilities, even in underrepresented languages such as Bengali and Swahili. Finally, we show that the multilingual reasoning abilities of language models extend to other tasks such as commonsense reasoning and word-in-context semantic judgment. The MGSM benchmark is publicly available at https://github.com/google-research/url-nlp.

## 11-002 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- arXiv: 2201.11903  first public: 2022-01-28  latest: 2023-01-10  primary cat: cs.CL
- authors (9): Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia ...
- seed subtopic: 思维链方法基础; type: 原始研究; cross: []
- pages: 43

ABSTRACT: We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

## 11-003 | Not All Languages Are Created Equal in LLMs: Improving Multilingual Capability by Cross-Lingual-Thought Prompting
- arXiv: 2305.07004  first public: 2023-05-11  latest: 2023-10-22  primary cat: cs.CL
- authors (7): Haoyang Huang; Tianyi Tang; Dongdong Zhang; Wayne Xin Zhao; Ting Song; Yan Xia ...
- seed subtopic: 跨语言思维提示; type: 原始研究; cross: []
- arXiv comment: Accepted by EMNLP 2023 Findings
- URLs on first pages of PDF: https://github.com/microsoft/unilm https://github.com/openai/openai-cookbook
- pages: 30

ABSTRACT: Large language models (LLMs) demonstrate impressive multilingual capability, but their performance varies substantially across different languages. In this work, we introduce a simple yet effective method, called cross-lingual-thought prompting (XLT), to systematically improve the multilingual capability of LLMs. Specifically, XLT is a generic template prompt that stimulates cross-lingual and logical reasoning skills to enhance task performance across languages. We conduct comprehensive evaluations on 7 typical benchmarks related to reasoning, understanding, and generation tasks, covering both high-resource and low-resource languages. Experimental results show that XLT not only remarkably enhances the performance of various multilingual tasks but also significantly reduces the gap between the average performance and the best performance of each task in different languages. Notably, XLT brings over 10 points of average improvement in arithmetic reasoning and open-domain question-answering tasks.

## 11-004 | Do Multilingual Language Models Think Better in English?
- arXiv: 2308.01223  first public: 2023-08-02  latest: 2023-08-02  primary cat: cs.CL
- authors (5): Julen Etxaniz; Gorka Azkune; Aitor Soroa; Oier Lopez de Lacalle; Mikel Artetxe
- seed subtopic: 推理语言选择; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/juletx/
- pages: 15

ABSTRACT: Translate-test is a popular technique to improve the performance of multilingual language models. This approach works by translating the input into English using an external machine translation system, and running inference over the translated input. However, these improvements can be attributed to the use of a separate translation system, which is typically trained on large amounts of parallel data not seen by the language model. In this work, we introduce a new approach called self-translate, which overcomes the need of an external translation system by leveraging the few-shot translation capabilities of multilingual language models. Experiments over 5 tasks show that self-translate consistently outperforms direct inference, demonstrating that language models are unable to leverage their full multilingual potential when prompted in non-English languages. Our code is available at https://github.com/juletx/self-translate.

## 11-005 | Breaking Language Barriers in Multilingual Mathematical Reasoning: Insights and Observations
- arXiv: 2310.20246  first public: 2023-10-31  latest: 2024-10-16  primary cat: cs.CL
- authors (6): Nuo Chen; Zinan Zheng; Ning Wu; Ming Gong; Dongmei Zhang; Jia Li
- seed subtopic: 多语言数学推理训练; type: 原始研究; cross: ['08']
- arXiv comment: Work in Progress
- pages: 16

ABSTRACT: Existing research predominantly focuses on developing powerful language learning models (LLMs) for mathematical reasoning within monolingual languages, with few explorations in preserving efficacy in a multilingual context. To bridge this gap, this paper pioneers exploring and training powerful Multilingual Math Reasoning (xMR) LLMs. Firstly, by utilizing translation, we construct the first multilingual math reasoning instruction dataset, MGSM8KInstruct, encompassing ten distinct languages, thus addressing the issue of training data scarcity in xMR tasks. Based on the collected dataset, we propose different training strategies to build powerful xMR LLMs, named MathOctopus, notably outperform conventional open-source LLMs and exhibit superiority over ChatGPT in few-shot scenarios. Notably, MathOctopus-13B reaches 47.6% accuracy which exceeds ChatGPT 46.3% on MGSM testset. Beyond remarkable results, we unearth several pivotal observations and insights from extensive experiments: (1) When extending the rejection sampling strategy to the multilingual context, it proves effective for model performances, albeit limited. (2) Employing parallel corpora for math Supervised Fine-Tuning (SFT) across multiple languages not only significantly enhances model performance multilingually but also elevates their monolingual performance. This indicates that crafting multilingual corpora can be regarded as a vital strategy for enhancing model performance in a specific language, especially in mathematical reasoning tasks. For instance, MathOctopus-7B improves its counterparts that trained on English from 42.2% to 50.8% on GSM8K testset. Codes are available at https://github.com/microsoft/MathOctopus.

## 11-006 | xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning
- arXiv: 2401.07037  first public: 2024-01-13  latest: 2024-01-13  primary cat: cs.CL
- authors (11): Linzheng Chai; Jian Yang; Tao Sun; Hongcheng Guo; Jiaheng Liu; Bing Wang ...
- seed subtopic: 跨语言思维链微调; type: 原始研究; cross: []
- arXiv comment: 11 pages
- URLs on first pages of PDF: https://github.com/openai/grade-school-math
- pages: 11

ABSTRACT: Chain-of-thought (CoT) has emerged as a powerful technique to elicit reasoning in large language models and improve a variety of downstream tasks. CoT mainly demonstrates excellent performance in English, but its usage in low-resource languages is constrained due to poor language generalization. To bridge the gap among different languages, we propose a cross-lingual instruction fine-tuning framework (xCOT) to transfer knowledge from high-resource languages to low-resource languages. Specifically, the multilingual instruction training data (xCOT-INSTRUCT) is created to encourage the semantic alignment of multiple languages. We introduce cross-lingual in-context few-shot learning (xICL)) to accelerate multilingual agreement in instruction tuning, where some fragments of source languages in examples are randomly substituted by their counterpart translations of target languages. During multilingual instruction tuning, we adopt the randomly online CoT strategy to enhance the multilingual reasoning ability of the large language model by first translating the query to another language and then answering in English. To further facilitate the language transfer, we leverage the high-resource CoT to supervise the training of low-resource languages with cross-lingual distillation. Experimental results on previous benchmarks demonstrate the superior performance of xCoT in reducing the gap among different languages, highlighting its potential to reduce the cross-lingual gap.

## 11-007 | MindMerger: Efficient Boosting LLM Reasoning in non-English Languages
- arXiv: 2405.17386  first public: 2024-05-27  latest: 2024-05-27  primary cat: cs.CL
- authors (5): Zixian Huang; Wenhao Zhu; Gong Cheng; Lei Li; Fei Yuan
- seed subtopic: 外部多语言编码器融合; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/CONE-MT/MindMerger
- pages: 19

ABSTRACT: Reasoning capabilities are crucial for Large Language Models (LLMs), yet a notable gap exists between English and non-English languages. To bridge this disparity, some works fine-tune LLMs to relearn reasoning capabilities in non-English languages, while others replace non-English inputs with an external model's outputs such as English translation text to circumvent the challenge of LLM understanding non-English. Unfortunately, these methods often underutilize the built-in skilled reasoning and useful language understanding capabilities of LLMs. In order to better utilize the minds of reasoning and language understanding in LLMs, we propose a new method, namely MindMerger, which merges LLMs with the external language understanding capabilities from multilingual models to boost the multilingual reasoning performance. Furthermore, a two-step training scheme is introduced to first train to embeded the external capabilities into LLMs and then train the collaborative utilization of the external capabilities and the built-in capabilities in LLMs. Experiments on three multilingual reasoning datasets and a language understanding dataset demonstrate that MindMerger consistently outperforms all baselines, especially in low-resource languages. Without updating the parameters of LLMs, the average accuracy improved by 6.7% and 8.0% across all languages and low-resource languages on the MGSM dataset, respectively.

## 11-008 | LangBridge: Multilingual Reasoning Without Multilingual Supervision
- arXiv: 2401.10695  first public: 2024-01-19  latest: 2024-06-03  primary cat: cs.CL
- authors (6): Dongkeun Yoon; Joel Jang; Sungdong Kim; Seungone Kim; Sheikh Shafayat; Minjoon Seo
- seed subtopic: 多语言编码器桥接; type: 原始研究; cross: []
- arXiv comment: ACL 2024 Main
- pages: 21

ABSTRACT: We introduce LangBridge, a zero-shot approach to adapt language models for multilingual reasoning tasks without multilingual supervision. LangBridge operates by bridging two models, each specialized in different aspects: (1) one specialized in understanding multiple languages (e.g., mT5 encoder) and (2) one specialized in reasoning (e.g., MetaMath). LangBridge connects the two models by introducing minimal trainable parameters between them. Despite utilizing only English data for training, LangBridge considerably enhances the performance of language models on low-resource languages across mathematical reasoning, code completion, logical reasoning, and commonsense reasoning. Our analysis suggests that the efficacy of LangBridge stems from the language-agnostic characteristics of multilingual representations. We publicly release our code and models.

## 11-010 | The Power of Question Translation Training in Multilingual Reasoning: Broadened Scope and Deepened Insights
- arXiv: 2405.01345  first public: 2024-05-02  latest: 2024-11-06  primary cat: cs.CL
- authors (6): Wenhao Zhu; Shujian Huang; Fei Yuan; Cheng Chen; Jiajun Chen; Alexandra Birch
- seed subtopic: 问题翻译对齐训练; type: 原始研究; cross: []
- pages: 12

ABSTRACT: Bridging the significant gap between large language model's English and non-English performance presents a great challenge. While some previous studies attempt to mitigate this gap with translated training data, the recently proposed question alignment framework leverages the model's English expertise to improve multilingual performance with minimum usage of expensive, error-prone translation. In this paper, we explore how broadly this method can be applied by examining its effects in reasoning with and without chain-of-thought, as well as with program-of-thought. We also explore applying this framework to extremely large language models in an efficient manner, such as through proxy-tuning. Experiment results on multilingual reasoning benchmarks mGSM, mSVAMP, xCSQA and xNLI demonstrate that we can extend question alignment framework to boost multilingual performance across diverse reasoning scenarios, model families, and sizes. For instance, when applied to the LLaMA2 models, it brings an average accuracy improvements of 12.2% on mGSM even with the 70B model. To understand the mechanism of its success, we analyze representation space, generated response and data scales, and reveal how question translation training strengthens language alignment within LLMs and shapes their working patterns.

## 11-011 | MAPO: Advancing Multilingual Reasoning through Multilingual Alignment-as-Preference Optimization
- arXiv: 2401.06838  first public: 2024-01-12  latest: 2024-04-13  primary cat: cs.CL
- authors (7): Shuaijie She; Wei Zou; Shujian Huang; Wenhao Zhu; Xiang Liu; Xiang Geng ...
- seed subtopic: 推理一致性偏好优化; type: 原始研究; cross: ['10']
- arXiv comment: The project is available at https://github.com/NJUNLP/MAPO
- pages: 13

ABSTRACT: Though reasoning abilities are considered language-agnostic, existing LLMs exhibit inconsistent reasoning abilities across different languages, e.g., reasoning in the dominant language like English is superior to other languages due to the imbalance of multilingual training data. To enhance reasoning abilities in non-dominant languages, we propose a Multilingual-Alignment-as-Preference Optimization framework (MAPO), aiming to align the reasoning processes in other languages with the dominant language. Specifically, we harness an off-the-shelf translation model for the consistency between answers in non-dominant and dominant languages, which we adopt as the preference for optimization, e.g., Direct Preference Optimization (DPO) or Proximal Policy Optimization (PPO). Experiments show that MAPO stably achieves significant improvements in the multilingual reasoning of various models on all three benchmarks (MSVAMP +16.2%, MGSM +6.1%, and MNumGLUESub +13.3%), with improved reasoning consistency across languages.

## 11-012 | mCoT: Multilingual Instruction Tuning for Reasoning Consistency in Language Models
- arXiv: 2406.02301  first public: 2024-06-04  latest: 2024-07-10  primary cat: cs.CL
- authors (2): Huiyuan Lai; Malvina Nissim
- seed subtopic: 多语言推理一致性; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2024 main (Corrected Figure 2 (a))
- pages: 15

ABSTRACT: Large language models (LLMs) with Chain-of-thought (CoT) have recently emerged as a powerful technique for eliciting reasoning to improve various downstream tasks. As most research mainly focuses on English, with few explorations in a multilingual context, the question of how reliable this reasoning capability is in different languages is still open. To address it directly, we study multilingual reasoning consistency across multiple languages, using popular open-source LLMs. First, we compile the first large-scale multilingual math reasoning dataset, mCoT-MATH, covering eleven diverse languages. Then, we introduce multilingual CoT instruction tuning to boost reasoning capability across languages, thereby improving model consistency. While existing LLMs show substantial variation across the languages we consider, and especially low performance for lesser resourced languages, our 7B parameter model mCoT achieves impressive consistency across languages, and superior or comparable performance to close- and open-source models even of much larger sizes.

## 11-013 | AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Multilingual Chain-of-Thought
- arXiv: 2501.16154  first public: 2025-01-27  latest: 2026-04-14  primary cat: cs.CL
- authors (10): Weihua Zheng; Xin Huang; Zhengyuan Liu; Tarun Kumar Vangani; Bowei Zou; Xiyan Tao ...
- seed subtopic: 自适应思考语言; type: 原始研究; cross: []
- arXiv comment: AAAI 2026
- URLs on first pages of PDF: https://github.com/Social-AI-Studio/AdaMCoT
- pages: 19

ABSTRACT: Large language models (LLMs) have shown impressive multilingual capabilities through pretraining on diverse corpora. Although these models show strong reasoning abilities, their performance varies significantly between languages due to the imbalanced distribution of training data. Existing approaches using sample-level translation for extensive multilingual pretraining and cross-lingual tuning face scalability challenges and often fail to capture nuanced reasoning processes across languages. In this paper, we introduce AdaMCOT (Adaptive Multilingual Chain-of-Thought), a framework that enhances multilingual factual reasoning by dynamically routing thought processes in intermediary "thinking languages" before generating target-language responses. AdaMCOT leverages a language-agnostic core and incorporates an adaptive, reward-based mechanism for selecting optimal reasoning pathways without requiring additional pretraining. Our comprehensive evaluation across multiple benchmarks demonstrates substantial improvements in both factual reasoning quality and cross-lingual consistency, with particularly strong performance gains in low-resource language settings. An in-depth analysis of the model's hidden states and semantic space further elucidates the underlying mechanism of our method. The results suggest that adaptive reasoning paths can effectively bridge the performance gap between high and low-resource languages while maintaining cultural and linguistic nuances.

## 11-014 | Crosslingual Reasoning through Test-Time Scaling
- arXiv: 2505.05408  first public: 2025-05-08  latest: 2025-05-08  primary cat: cs.CL
- authors (10): Zheng-Xin Yong; M. Farid Adilazuarda; Jonibek Mansurov; Ruochen Zhang; Niklas Muennighoff; Carsten Eickhoff ...
- seed subtopic: 推理模型测试时扩展; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/BatsResearch/crosslingual-test-
- pages: 29

ABSTRACT: Reasoning capabilities of large language models are primarily studied for English, even when pretrained models are multilingual. In this work, we investigate to what extent English reasoning finetuning with long chain-of-thoughts (CoTs) can generalize across languages. First, we find that scaling up inference compute for English-centric reasoning language models (RLMs) improves multilingual mathematical reasoning across many languages including low-resource languages, to an extent where they outperform models twice their size. Second, we reveal that while English-centric RLM's CoTs are naturally predominantly English, they consistently follow a quote-and-think pattern to reason about quoted non-English inputs. Third, we discover an effective strategy to control the language of long CoT reasoning, and we observe that models reason better and more efficiently in high-resource languages. Finally, we observe poor out-of-domain reasoning generalization, in particular from STEM to cultural commonsense knowledge, even for English. Overall, we demonstrate the potentials, study the mechanisms and outline the limitations of crosslingual generalization of English reasoning test-time scaling. We conclude that practitioners should let English-centric RLMs reason in high-resource languages, while further work is needed to improve reasoning in low-resource languages and out-of-domain contexts.

## 11-015 | Language Matters: How Do Multilingual Input and Reasoning Paths Affect Large Reasoning Models?
- arXiv: 2505.17407  first public: 2025-05-23  latest: 2025-05-23  primary cat: cs.CL
- authors (6): Zhi Rui Tam; Cheng-Kuang Wu; Yu Ying Chiu; Chieh-Yen Lin; Yun-Nung Chen; Hung-yi Lee
- seed subtopic: 推理模型思考语言; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/openai/MMMLU
- pages: 35

ABSTRACT: Large reasoning models (LRMs) have demonstrated impressive performance across a range of reasoning tasks, yet little is known about their internal reasoning processes in multilingual settings. We begin with a critical question: {\it In which language do these models reason when solving problems presented in different languages?} Our findings reveal that, despite multilingual training, LRMs tend to default to reasoning in high-resource languages (e.g., English) at test time, regardless of the input language. When constrained to reason in the same language as the input, model performance declines, especially for low-resource languages. In contrast, reasoning in high-resource languages generally preserves performance. We conduct extensive evaluations across reasoning-intensive tasks (MMMLU, MATH-500) and non-reasoning benchmarks (CulturalBench, LMSYS-toxic), showing that the effect of language choice varies by task type: input-language reasoning degrades performance on reasoning tasks but benefits cultural tasks, while safety evaluations exhibit language-specific behavior. By exposing these linguistic biases in LRMs, our work highlights a critical step toward developing more equitable models that serve users across diverse linguistic backgrounds.

## 11-016 | When Models Reason in Your Language: Controlling Thinking Language Comes at the Cost of Accuracy
- arXiv: 2505.22888  first public: 2025-05-28  latest: 2025-10-01  primary cat: cs.CL
- authors (6): Jirui Qi; Shan Chen; Zidi Xiong; Raquel Fernández; Danielle S. Bitterman; Arianna Bisazza
- seed subtopic: 思考语言控制与准确率; type: 基准与数据集; cross: []
- arXiv comment: Accepted at EMNLP 2025 Findings
- doi: 10.18653/v1/2025.findings-emnlp.1103
- pages: 18

ABSTRACT: Recent Large Reasoning Models (LRMs) with thinking traces have shown strong performance on English reasoning tasks. However, their ability to think in other languages is less studied. This capability is as important as answer accuracy for real world applications because users may find the reasoning trace useful for oversight only when it is expressed in their own language. We comprehensively evaluate two leading families of LRMs on our XReasoning benchmark and find that even the most advanced models often revert to English or produce fragmented reasoning in other languages, revealing a substantial gap in multilingual reasoning. Prompt based interventions that force models to reason in the users language improve readability and oversight but reduce answer accuracy, exposing an important trade off. We further show that targeted post training on just 100 examples mitigates this mismatch, though some accuracy loss remains. Our results highlight the limited multilingual reasoning capabilities of current LRMs and outline directions for future work. Code and data are available at https://github.com/Betswish/mCoT-XReasoning.

## 11-017 | Long Chain-of-Thought Reasoning Across Languages
- arXiv: 2508.14828  first public: 2025-08-20  latest: 2026-03-20  primary cat: cs.CL
- authors (4): Josh Barua; Seun Eisape; Kayo Yin; Alane Suhr
- seed subtopic: 长思维链跨语言迁移; type: 原始研究; cross: []
- arXiv comment: Accepted to ICLR 2026. v1 is a workshop version accepted to SCALR @ COLM 2025
- URLs on first pages of PDF: https://github.com/Berkeley-NLP/Multilingual-Long-CoT
- pages: 24

ABSTRACT: While large reasoning models have shown remarkable ability to generate long chains-of-thought (CoTs) in English, we still lack understanding of how these long-form reasoning abilities transfer to the vast majority of the world's languages. In this work, we systematically investigate four key stages of model development--scaling, pretraining, post-training, and inference--to understand how long CoT capabilities extend beyond English. We compare two reasoning settings across nine non-English target languages: En-CoT, where models process target-language inputs, but reason in English; and Target-CoT, where models both process inputs and generate long CoTs in the target language. We find that scaling reasoning model size improves multilingual task performance in En-CoT, but Target-CoT performance lags behind. This gap widens for tasks requiring long, multi-step CoTs such as mathematical reasoning. Shifting to pretraining, we find that adding a specialized reasoning stage enhances En-CoT performance but degrades Target-CoT, whereas broad multilingual pretraining improves both modes simultaneously. Given the scarcity of high-quality reasoning traces in languages other than English, we explore synthetic data curation approaches for post-training. We demonstrate that fine-tuning on reasoning traces automatically translated from gold English traces outperforms fine-tuning on target-language traces distilled from large reasoning models. Finally, we report disparities in inference efficiency between languages and uncover language-specific failure modes in CoTs. We release models, datasets, and code to foster further research.

## 11-018 | Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning
- arXiv: 2510.07300  first public: 2025-10-08  latest: 2026-01-08  primary cat: cs.CL
- authors (8): Xue Zhang; Yunlong Liang; Fandong Meng; Songming Zhang; Kaiyu Huang; Yufeng Chen ...
- seed subtopic: 母语思考强化学习; type: 原始研究; cross: []
- arXiv comment: 17 pages, 14 tables, 4 figures. Code is available at: https://github.com/XZhang00/M-Thinker
- URLs on first pages of PDF: https://github.com/XZhang00/M-Thinker
- pages: 17

ABSTRACT: Large Reasoning Models (LRMs) have achieved remarkable performance on complex reasoning tasks by adopting the ``think-then-answer'' paradigm, which enhances both accuracy and interpretability. However, current LRMs exhibit two critical limitations when processing non-English languages: (1) They often struggle to maintain input-output language consistency; (2) They generally perform poorly with wrong reasoning paths and lower answer accuracy compared to English. These limitations significantly compromise the interpretability of reasoning processes and degrade the user experience for non-English speakers, hindering the global deployment of LRMs. To address these limitations, we propose M-Thinker, which is trained by the GRPO algorithm that involves a Language Consistency (LC) reward and a novel Cross-lingual Thinking Alignment (CTA) reward. Specifically, the LC reward defines a strict constraint on the language consistency between the input, thought, and answer. Besides, the CTA reward compares the model's non-English reasoning paths with its English reasoning path to transfer its own reasoning capability from English to non-English languages. Through an iterative RL procedure, our M-Thinker-1.5B/4B/7B models not only achieve nearly 100% language consistency and superior performance on two multilingual benchmarks (MMATH and PolyMath), but also exhibit excellent generalization on out-of-domain languages.

## 11-019 | The Reasoning Lingua Franca: A Double-Edged Sword for Multilingual AI
- arXiv: 2510.20647  first public: 2025-10-23  latest: 2026-02-08  primary cat: cs.CL
- authors (4): Alan Saji; Raj Dabre; Anoop Kunchukuttan; Ratish Puduppully
- seed subtopic: 英语作推理通用语; type: 原始研究; cross: []
- arXiv comment: 14 pages, 13 figures, 5 tables
- URLs on first pages of PDF: https://github.com/AI4Bharat/m
- pages: 16

ABSTRACT: Large Reasoning Models (LRMs) achieve strong performance on mathematical, scientific, and other question-answering tasks, but their multilingual reasoning abilities remain underexplored. When presented with non-English questions, LRMs often default to reasoning in English, raising concerns about interpretability and the handling of linguistic and cultural nuances. We systematically compare an LRM's reasoning in English versus the language of the question. Our evaluation spans two tasks: MGSM and GPQA Diamond. Beyond measuring answer accuracy, we also analyze cognitive attributes in the reasoning traces. We find that English reasoning traces exhibit a substantially higher presence of these cognitive behaviors, and that reasoning in English generally yields higher final-answer accuracy, with the performance gap increasing as tasks become more complex. However, this English-centric strategy is susceptible to a key failure mode - getting "Lost in Translation," where translation steps lead to errors that would have been avoided by reasoning in the language of the question.

## 11-020 | Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning
- arXiv: 2502.17407  first public: 2025-02-24  latest: 2025-08-01  primary cat: cs.CL
- authors (4): Guijin Son; Jiwoo Hong; Hyunwoo Ko; James Thorne
- seed subtopic: 测试时扩展的语言泛化; type: 基准与数据集; cross: ['15']
- arXiv comment: ACL 2025 (ORAL)
- URLs on first pages of PDF: https://github.com/gauss5930/MCLM
- pages: 36

ABSTRACT: Scaling pre-training compute has proven effective for achieving mulitlinguality, but does the same hold for test-time scaling? In this work, we introduce MCLM, a multilingual math benchmark featuring competition-level problems in 55 languages. We test three test-time scaling methods-Outcome Reward Modeling (ORM), Process Reward Modeling (ORM), and Budget Forcing (BF)-on both Qwen2.5-1.5B Math and MR1-1.5B, a multilingual LLM we trained for extended reasoning. Our experiments show that using Qwen2.5-1.5B Math with ORM achieves a score of 35.8 on MCLM, while BF on MR1-1.5B attains 35.2. Although "thinking LLMs" have recently garnered significant attention, we find that their performance is comparable to traditional scaling methods like best-of-N once constrained to similar levels of inference FLOPs. Moreover, while BF yields a 20-point improvement on English AIME, it provides only a 1.94-point average gain across other languages-a pattern consistent across the other test-time scaling methods we studied-higlighting that test-time scaling may not generalize as effectively to multilingual tasks. To foster further research, we release MCLM, MR1-1.5B, and evaluation results.

## 11-021 | PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts
- arXiv: 2504.18428  first public: 2025-04-25  latest: 2025-11-02  primary cat: cs.CL
- authors (16): Yiming Wang; Pei Zhang; Jialong Tang; Haoran Wei; Baosong Yang; Rui Wang ...
- seed subtopic: 多语言数学推理评测; type: 基准与数据集; cross: ['15']
- arXiv comment: Accepted by NeurIPS 2025
- URLs on first pages of PDF: https://github.com/QwenLM/PolyMath
- pages: 50

ABSTRACT: In this paper, we introduce PolyMath, a multilingual mathematical reasoning benchmark covering 18 languages and 4 easy-to-hard difficulty levels. Our benchmark ensures difficulty comprehensiveness, language diversity, and high-quality translation, making it a highly discriminative multilingual mathematical benchmark in the era of reasoning LLMs. We conduct a comprehensive evaluation for advanced LLMs and find that even Qwen-3-235B-A22B-Thinking and Gemini-2.5-pro, achieve only 54.6 and 52.2 benchmark scores, with about 40% accuracy under the highest level From a language perspective, our benchmark reveals several key challenges of LLMs in multilingual reasoning: (1) Reasoning performance varies widely across languages for current LLMs; (2) Input-output language consistency is low in reasoning LLMs and may be correlated with performance; (3) The thinking length differs significantly by language for current LLMs. Additionally, we demonstrate that controlling the output language in the instructions has the potential to affect reasoning performance, especially for some low-resource languages, suggesting a promising direction for improving multilingual capabilities in LLMs.

## 11-022 | MMATH: A Multilingual Benchmark for Mathematical Reasoning
- arXiv: 2505.19126  first public: 2025-05-25  latest: 2025-05-25  primary cat: cs.CL
- authors (5): Wenyang Luo; Wayne Xin Zhao; Jing Sha; Shijin Wang; Ji-Rong Wen
- seed subtopic: 多语言数学推理评测; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://github.com/RUCAIBox/MMATH https://github.com/huggingface/Math-Verify
- pages: 16

ABSTRACT: The advent of large reasoning models, such as OpenAI o1 and DeepSeek R1, has significantly advanced complex reasoning tasks. However, their capabilities in multilingual complex reasoning remain underexplored, with existing efforts largely focused on simpler tasks like MGSM. To address this gap, we introduce MMATH, a benchmark for multilingual complex reasoning spanning 374 high-quality math problems across 10 typologically diverse languages. Using MMATH, we observe that even advanced models like DeepSeek R1 exhibit substantial performance disparities across languages and suffer from a critical off-target issue-generating responses in unintended languages. To address this, we explore strategies including prompting and training, demonstrating that reasoning in English and answering in target languages can simultaneously enhance performance and preserve target-language consistency. Our findings offer new insights and practical strategies for advancing the multilingual reasoning capabilities of large language models. Our code and data could be found at https://github.com/RUCAIBox/MMATH.

## 11-023 | A Survey of Multilingual Reasoning in Language Models
- arXiv: 2502.09457  first public: 2025-02-13  latest: 2025-10-14  primary cat: cs.CL
- authors (4): Akash Ghosh; Debayan Datta; Sriparna Saha; Chirag Agarwal
- seed subtopic: 多语言推理综述; type: 综述; cross: []
- arXiv comment: EMNLP Findings 2025
- URLs on first pages of PDF: https://github.com/AkashGhosh/Survey
- pages: 17

ABSTRACT: While reasoning and multilingual capabilities in language models (LMs) have achieved remarkable progress in recent years, their integration into a unified paradigm - multilingual reasoning - is at a nascent stage. Multilingual reasoning requires language models to handle logical reasoning across languages while addressing misalignment, biases, and challenges in low-resource settings. This survey provides the first in-depth review of multilingual reasoning in LMs. In this survey, we provide a systematic overview of existing methods that leverage LMs for multilingual reasoning, specifically outlining the challenges, motivations, and foundational aspects of applying language models to reason across diverse languages. We provide an overview of the standard data resources used for training multilingual reasoning in LMs and the evaluation benchmarks employed to assess their multilingual capabilities. Next, we analyze various state-of-the-art methods and their performance on these benchmarks. Finally, we explore future research opportunities to improve multilingual reasoning in LMs, focusing on enhancing their ability to handle diverse languages and complex reasoning tasks. Rapid growth of evolving developments in this field can be actively tracked on our project page: [https://github.com/AkashGhosh/Survey-of-Multilingual-Reasoning-in-Language-Models](https://github.com/AkashGhosh/Survey-of-Multilingual-Reasoning-in-Language-Models)

## 11-024 | Reasoning Transfer for an Extremely Low-Resource and Endangered Language: Bridging Languages Through Sample-Efficient Language Understanding
- arXiv: 2504.02890  first public: 2025-04-02  latest: 2025-11-26  primary cat: cs.CL
- authors (3): Khanh-Tung Tran; Barry O'Sullivan; Hoang D. Nguyen
- seed subtopic: 极低资源濒危语言推理迁移; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/ReML-AI/english-pivoted-cot
- pages: 9

ABSTRACT: Recent advances have enabled Large Language Models (LLMs) to tackle reasoning tasks by generating chain-of-thought (CoT) rationales, yet these gains have largely applied to high-resource languages, leaving low-resource languages behind. In this work, we first investigate CoT techniques in extremely low-resource scenarios through previous prompting, model-editing, and fine-tuning approaches. We introduce English-Pivoted CoT Training, leveraging the insight that LLMs internally operate in a latent space aligned toward the dominant language. Given input in a low-resource language, we perform supervised fine-tuning to generate CoT in English and output the final response in the target language. Across mathematical reasoning benchmarks, our approach outperforms other baselines with up to 28.33% improvement in low-resource scenarios. Our analysis and additional experiments, including Mixed-Language CoT and Two-Stage Training, show that explicitly separating language understanding from reasoning enhances cross-lingual reasoning abilities. To facilitate future work, we also release \emph{LC2024}, the first benchmark for mathematical tasks in Irish, an extremely low-resource and endangered language. Our results and resources highlight a practical pathway to multilingual reasoning without extensive retraining in every extremely low-resource language, despite data scarcity.

## 11-025 | Improving Multilingual Math Reasoning for African Languages
- arXiv: 2505.19848  first public: 2025-05-26  latest: 2025-05-26  primary cat: cs.CL
- authors (6): Odunayo Ogundepo; Akintunde Oladipo; Kelechi Ogueji; Esther Adenuga; David Ifeoluwa Adelani; Jimmy Lin
- seed subtopic: 非洲语言数学推理; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL- https://huggingface.co/datasets/nvidia/OpenMathInstruct-2
- pages: 18

ABSTRACT: Researchers working on low-resource languages face persistent challenges due to limited data availability and restricted access to computational resources. Although most large language models (LLMs) are predominantly trained in high-resource languages, adapting them to low-resource contexts, particularly African languages, requires specialized techniques. Several strategies have emerged for adapting models to low-resource languages in todays LLM landscape, defined by multi-stage pre-training and post-training paradigms. However, the most effective approaches remain uncertain. This work systematically investigates which adaptation strategies yield the best performance when extending existing LLMs to African languages. We conduct extensive experiments and ablation studies to evaluate different combinations of data types (translated versus synthetically generated), training stages (pre-training versus post-training), and other model adaptation configurations. Our experiments focuses on mathematical reasoning tasks, using the Llama 3.1 model family as our base model.

## 11-026 | MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs
- arXiv: 2507.17476  first public: 2025-07-23  latest: 2025-07-23  primary cat: cs.CL
- authors (8): Alexander R. Fabbri; Diego Mares; Jorge Flores; Meher Mankikar; Ernesto Hernandez; Dean Lee ...
- seed subtopic: 原生多语言推理基准; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://huggingface.co/datasets/ScaleAI/MultiNRC
- pages: 16

ABSTRACT: Although recent Large Language Models (LLMs) have shown rapid improvement on reasoning benchmarks in English, the evaluation of such LLMs' multilingual reasoning capability across diverse languages and cultural contexts remains limited. Existing multilingual reasoning benchmarks are typically constructed by translating existing English reasoning benchmarks, biasing these benchmarks towards reasoning problems with context in English language/cultures. In this work, we introduce the Multilingual Native Reasoning Challenge (MultiNRC), a benchmark designed to assess LLMs on more than 1,000 native, linguistic and culturally grounded reasoning questions written by native speakers in French, Spanish, and Chinese. MultiNRC covers four core reasoning categories: language-specific linguistic reasoning, wordplay & riddles, cultural/tradition reasoning, and math reasoning with cultural relevance. For cultural/tradition reasoning and math reasoning with cultural relevance, we also provide English equivalent translations of the multilingual questions by manual translation from native speakers fluent in English. This set of English equivalents can provide a direct comparison of LLM reasoning capacity in other languages vs. English on the same reasoning questions. We systematically evaluate current 14 leading LLMs covering most LLM families on MultiNRC and its English equivalent set. The results show that (1) current LLMs are still not good at native multilingual reasoning, with none scoring above 50% on MultiNRC; (2) LLMs exhibit distinct strengths and weaknesses in handling linguistic, cultural, and logical reasoning tasks; (3) Most models perform substantially better in math reasoning in English compared to in original languages (+10%), indicating persistent challenges with culturally grounded knowledge.

## 11-027 | A Comprehensive Evaluation of Multilingual Chain-of-Thought Reasoning: Performance, Consistency, and Faithfulness Across Languages
- arXiv: 2510.09555  first public: 2025-10-10  latest: 2025-10-10  primary cat: cs.CL
- authors (4): Raoyuan Zhao; Yihong Liu; Hinrich Schütze; Michael A. Hedderich
- seed subtopic: 多语言 CoT 忠实性; type: 原始研究; cross: []
- arXiv comment: preprint
- URLs on first pages of PDF: https://github.com/mainlp/Multilingual-CoT-Evaluation
- pages: 20

ABSTRACT: Large reasoning models (LRMs) increasingly rely on step-by-step Chain-of-Thought (CoT) reasoning to improve task performance, particularly in high-resource languages such as English. While recent work has examined final-answer accuracy in multilingual settings, the thinking traces themselves, i.e., the intermediate steps that lead to the final answer, remain underexplored. In this paper, we present the first comprehensive study of multilingual CoT reasoning, evaluating three key dimensions: performance, consistency, and faithfulness. We begin by measuring language compliance, answer accuracy, and answer consistency when LRMs are explicitly instructed or prompt-hacked to think in a target language, revealing strong language preferences and divergent performance across languages. Next, we assess crosslingual consistency of thinking traces by interchanging them between languages. We find that the quality and effectiveness of thinking traces vary substantially depending on the prompt language. Finally, we adapt perturbation-based techniques -- i.e., truncation and error injection -- to probe the faithfulness of thinking traces across languages, showing that models rely on traces to varying degrees. We release our code and data to support future research.

## 11-028 | Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes
- arXiv: 2505.14815  first public: 2025-05-20  latest: 2025-09-19  primary cat: cs.CL
- authors (6): Mingyang Wang; Lukas Lange; Heike Adel; Yunpu Ma; Jannik Strötgen; Hinrich Schütze
- seed subtopic: 推理中的语言混用; type: 原始研究; cross: []
- pages: 30

ABSTRACT: Reasoning language models (RLMs) excel at complex tasks by leveraging a chain-of-thought process to generate structured intermediate steps. However, language mixing, i.e., reasoning steps containing tokens from languages other than the prompt, has been observed in their outputs and shown to affect performance, though its impact remains debated. We present the first systematic study of language mixing in RLMs, examining its patterns, impact, and internal causes across 15 languages, 7 task difficulty levels, and 18 subject areas, and show how all three factors influence language mixing. Moreover, we demonstrate that the choice of reasoning language significantly affects performance: forcing models to reason in Latin or Han scripts via constrained decoding notably improves accuracy. Finally, we show that the script composition of reasoning traces closely aligns with that of the model's internal representations, indicating that language mixing reflects latent processing preferences in RLMs. Our findings provide actionable insights for optimizing multilingual reasoning and open new directions for controlling reasoning languages to build more interpretable and adaptable RLMs.

## 11-029 | Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners
- arXiv: 2601.02996  first public: 2026-01-06  latest: 2026-04-16  primary cat: cs.CL
- authors (4): Yihong Liu; Raoyuan Zhao; Hinrich Schütze; Michael A. Hedderich
- seed subtopic: 多语言潜在推理; type: 原始研究; cross: []
- arXiv comment: ACL 2026 Findings
- pages: 29

ABSTRACT: Large reasoning models (LRMs) achieve strong performance on mathematical reasoning tasks, often attributed to their capability to generate explicit chain-of-thought (CoT) explanations. However, recent work shows that LRMs often arrive at the correct answer before completing these textual reasoning steps, indicating the presence of latent reasoning -- internal, non-verbal computation encoded in hidden states. While this phenomenon has been explored in English, its multilingual behavior remains largely unknown. In this paper, we conduct a systematic investigation of multilingual latent reasoning in LRMs across 11 languages. Using a truncation-based strategy, we examine how the correct answer emerges as the model is given only partial reasoning traces, allowing us to measure stepwise latent prediction formation. Our results reveal clear evidence of multilingual latent reasoning, though unevenly: strong in resource-rich languages, weaker in low-resource ones, and broadly less observable on harder benchmarks. To understand whether these differences reflect distinct internal mechanisms, we further perform representational analyses. Despite surface-level disparities, we find that the internal evolution of predictions is highly consistent across languages and broadly aligns with English -- a pattern suggesting an English-centered latent reasoning pathway.

## 11-031 | Towards Better Understanding of Program-of-Thought Reasoning in Cross-Lingual and Multilingual Environments
- arXiv: 2502.17956  first public: 2025-02-25  latest: 2025-05-22  primary cat: cs.CL
- authors (9): Patomporn Payoungkhamdee; Pume Tuchinda; Jinheon Baek; Samuel Cahyawijaya; Can Udomcharoenchaikit; Potsawee Manakul ...
- seed subtopic: 程序化思维跨语言; type: 原始研究; cross: []
- journal_ref: Findings of the Association for Computational Linguistics: ACL 2025
- doi: 10.18653/v1/2025.findings-acl.817
- pages: 18

ABSTRACT: Multi-step reasoning is essential for large language models (LLMs), yet multilingual performance remains challenging. While Chain-of-Thought (CoT) prompting improves reasoning, it struggles with non-English languages due to the entanglement of reasoning and execution. Program-of-Thought (PoT) prompting separates reasoning from execution, offering a promising alternative but shifting the challenge to generating programs from non-English questions. We propose a framework to evaluate PoT by separating multilingual reasoning from code execution to examine (i) the impact of fine-tuning on question-reasoning alignment and (ii) how reasoning quality affects answer correctness. Our findings demonstrate that PoT fine-tuning substantially enhances multilingual reasoning, outperforming CoT fine-tuned models. We further demonstrate a strong correlation between reasoning quality (measured through code quality) and answer accuracy, highlighting its potential as a test-time performance improvement heuristic.

## 11-032 | EfficientXLang: Towards Improving Token Efficiency Through Cross-Lingual Reasoning
- arXiv: 2507.00246  first public: 2025-06-30  latest: 2025-06-30  primary cat: cs.CL
- authors (3): Sanchit Ahuja; Praneetha Vaddamanu; Barun Patra
- seed subtopic: 推理语言与 token 效率; type: 原始研究; cross: []
- arXiv comment: 15 pages, 5 figures, 9 tables
- pages: 15

ABSTRACT: Despite recent advances in Language Reasoning Models (LRMs), most research focuses solely on English, even though many models are pretrained on multilingual data. In this work, we investigate: Is English the most token-efficient language for reasoning? We evaluate three open-source RLMs: DeepSeek R1, Qwen 2.5 and Qwen 3, across four math datasets and seven typologically diverse languages. We find that reasoning in non-English languages not only reduces token usage, but also preserves accuracy. These gains persist even after translating the reasoning traces into English, suggesting genuine shifts in reasoning behavior rather than surface-level linguistic effects. The extent of improvement, however, depends on the models multilingual strength. Our findings motivate a broader view of reasoning in language models, highlighting the potential of multilingual reasoning and the importance of strong multilingual foundations. The code for our work can be found: https://github.com/microsoft/EfficientXLang.

## 11-033 | Could Thinking Multilingually Empower LLM Reasoning?
- arXiv: 2504.11833  first public: 2025-04-16  latest: 2025-04-16  primary cat: cs.CL
- authors (6): Changjiang Gao; Xu Huang; Wenhao Zhu; Shujian Huang; Lei Li; Fei Yuan
- seed subtopic: 多语言思考增益; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/meta-llama/Llama-3
- pages: 18

ABSTRACT: Previous work indicates that large language models exhibit a significant "English bias", i.e. they often perform better when tasks are presented in English. Interestingly, we have observed that using certain other languages in reasoning tasks can yield better performance than English. However, this phenomenon remains under-explored. In this paper, we explore the upper bound of harnessing multilingualism in reasoning tasks, suggesting that multilingual reasoning promises significantly (by nearly 10 Acc@$k$ points) and robustly (tolerance for variations in translation quality and language choice) higher upper bounds than English-only reasoning. Besides analyzing the reason behind the upper bound and challenges in reaching it, we also find that common answer selection methods cannot achieve this upper bound, due to their limitations and biases. These insights could pave the way for future research aimed at fully harnessing the potential of multilingual reasoning in LLMs.

## 11-034 | Beg to Differ: Understanding Reasoning-Answer Misalignment Across Languages
- arXiv: 2512.22712  first public: 2025-12-27  latest: 2026-03-30  primary cat: cs.CL
- authors (7): Anaelia Ovalle; Candace Ross; Sebastian Ruder; Adina Williams; Karen Ullrich; Mark Ibrahim ...
- seed subtopic: 推理与答案不一致; type: 原始研究; cross: []
- arXiv comment: Accepted to 2025 EMNLP Multilingual Representation Learning Workshop
- pages: 16

ABSTRACT: Large language models demonstrate strong reasoning capabilities through chain-of-thought prompting, but whether this reasoning quality transfers across languages remains underexplored. We introduce a human-validated framework to evaluate whether model-generated reasoning traces logically support their conclusions across languages. Analyzing 65k reasoning traces from GlobalMMLU questions across 6 languages and 6 frontier models, we uncover a critical blind spot: while models achieve high task accuracy, their reasoning can fail to support their conclusions. Reasoning traces in non-Latin scripts show at least twice as much misalignment between their reasoning and conclusions than those in Latin scripts. We develop an error taxonomy through human annotation to characterize these failures, finding they stem primarily from evidential errors (unsupported claims, ambiguous facts) followed by illogical reasoning steps. Our findings demonstrate that current multilingual evaluation practices provide an incomplete picture of model reasoning capabilities and highlight the need for reasoning-aware evaluation frameworks.

## 11-035 | Multilingual Reasoning Gym: Multilingual Scaling of Procedural Reasoning Environments
- arXiv: 2603.10793  first public: 2026-03-11  latest: 2026-03-11  primary cat: cs.CL
- authors (5): Konstantin Dobler; Simon Lehnerer; Federico Scozzafava; Jonathan Janke; Mohamed Ali
- seed subtopic: 多语言推理训练环境; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/apple/ml-multilingual-reasoning-gym
- pages: 14

ABSTRACT: We present the Multilingual Reasoning Gym, an extension of Reasoning Gym (Stojanovski et al., 2025), that procedurally generates verifiable reasoning problems across 14 languages. We translate templates for 94 tasks with native-speaker validation in 10 languages and targeted code or template adaptations to ensure linguistic naturalness. The Multilingual Reasoning Gym preserves the core benefits of the procedural generation approach used in the original Reasoning Gym, such as virtually unlimited problem instance generation and adjustable difficulty, and remains directly usable for Reinforcement Learning from Verifiable Rewards and evaluation settings. Problems in the Multilingual Reasoning Gym are parallel across languages, enabling crosslingually parallel data generation at massive scale due to the procedural nature of the environments. We release our implementation to support research into multilingual reasoning models.

## 11-036 | MathMist: A Parallel Multilingual Benchmark Dataset for Mathematical Problem Solving and Reasoning
- arXiv: 2510.14305  first public: 2025-10-16  latest: 2026-01-24  primary cat: cs.CL
- authors (5): Mahbub E Sobhani; Md. Faiyaz Abdullah Sayeedi; Tasnim Mohiuddin; Md Mofijul Islam; Swakkhar Shatabda
- seed subtopic: 多语言平行数学基准; type: 基准与数据集; cross: []
- arXiv comment: Accepted for publication in Findings of EACL 2026
- pages: 27

ABSTRACT: Mathematical reasoning remains one of the most challenging domains for large language models (LLMs), requiring not only linguistic understanding but also structured logical deduction and numerical precision. While recent LLMs demonstrate strong general-purpose reasoning abilities, their mathematical competence across diverse languages remains underexplored. Existing benchmarks primarily focus on English or a narrow subset of high-resource languages, leaving significant gaps in assessing multilingual and cross-lingual mathematical reasoning. To address this, we introduce MATHMIST, a parallel multilingual benchmark for mathematical problem solving and reasoning. MATHMIST encompasses 2,890 parallel Bangla-English gold standard artifacts, totaling approximately 30K aligned question--answer pairs across thirteen languages, representing an extensive coverage of high-, medium-, and low-resource linguistic settings. The dataset captures linguistic variety, multiple types of problem settings, and solution synthesizing capabilities. We systematically evaluate a diverse suite of models, including open-source small and medium LLMs, proprietary systems, and multilingual-reasoning-focused models under zero-shot, chain-of-thought (CoT), perturbated reasoning, and code-switched reasoning paradigms. Our results reveal persistent deficiencies in LLMs' ability to perform consistent and interpretable mathematical reasoning across languages, with pronounced degradation in low-resource settings. All the codes and data are available at GitHub: https://github.com/mahbubhimel/MathMist

## 11-037 | How Well Does Mathematical Reasoning Transfer Across Languages in English-Centric LLMs?
- arXiv: 2510.02272  first public: 2025-10-02  latest: 2026-10-22  primary cat: cs.CL
- authors (5): Wen Yang; Junhong Wu; Chong Li; Chengqing Zong; Jiajun Zhang
- seed subtopic: 英语中心模型推理迁移; type: 原始研究; cross: []
- arXiv comment: Camera ready version for EMNLP 2026 Main
- pages: 27

ABSTRACT: Recent advances in Reinforcement Post-Training (RPT) have substantially improved the mathematical reasoning capabilities of large language models (LLMs), but it remains unclear how well such gains transfer across languages. In this work, we study cross-lingual mathematical reasoning transfer in English-centric LLMs under controlled multilingual evaluation. We first evaluate a range of English-centric reasoning models on multilingual mathematical reasoning benchmarks and find that transfer is highly variable across initial model choice, target language, and training paradigm. Through controlled comparative experiments, we further find that stronger English-centric initialization does not necessarily lead to stronger relative transfer efficiency, even when it yields higher multilingual reasoning accuracy. Finally, we show that the largest improvement comes from moving beyond English-only supervision: adding a single parallel language yields a substantial gain, while further gains from additional languages are smaller but consistent. Overall, our results highlight the need to evaluate multilingual mathematical reasoning directly, using both absolute performance and relative transfer-efficiency metrics.

## 11-038 | Learn Globally, Speak Locally: Bridging the Gaps in Multilingual Reasoning
- arXiv: 2507.05418  first public: 2025-07-07  latest: 2025-09-26  primary cat: cs.CL
- authors (8): Jaedong Hwang; Kumar Tanmay; Seok-Jin Lee; Ayush Agrawal; Hamid Palangi; Kumar Ayush ...
- seed subtopic: 本地语言推理忠实性; type: 原始研究; cross: []
- URLs on first pages of PDF: https://jd730.github.io/projects/M2A_GeoFact-X
- pages: 23

ABSTRACT: Large Language Models (LLMs) have achieved strong performance in domains like mathematics, factual question answering, and code generation, yet their ability to reason on these tasks in different languages remains underdeveloped. Especially for low-resource languages such as Swahili or Thai, LLMs can often misinterpret prompts or default to reasoning in English. This implicit bias toward high-resource languages undermines factual accuracy, interpretability, and trust. We propose M2A, a novel method that combines multi-scale multilingual alignment with language-consistency rewards on machine-translated questions, training models to reason directly and accurately in the target language. Furthermore, existing multilingual benchmarks only evaluate on final answers, overlooking whether reasoning occurs in the intended language. To close this gap, we introduce GeoFact-X, a geography-based multilingual factual reasoning benchmark together with reasoning traces in five languages: English, Hindi, Japanese, Swahili, and Thai. Our results show that M2A significantly enhances multilingual reasoning fidelity in both mathematical and factual reasoning tasks, highlighting that reasoning-aware multilingual reinforcement learning is crucial for robust cross-lingual generalization. https://jd730.github.io/projects/M2A_GeoFact-X

## 11-039 | Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages
- arXiv: 2608.00533  first public: 2026-08-01  latest: 2026-08-01  primary cat: cs.CL
- authors (3): Sean Gip Lim; William Chandra Tjhi; Hai Leong Chieu
- seed subtopic: 东南亚低资源语言原生 CoT; type: 原始研究; cross: []
- arXiv comment: 22 pages, 16 figures, 12 tables
- URLs on first pages of PDF: https://github.com/SG-Lim/OSCD
- pages: 22

ABSTRACT: Large Language Models have achieved substantial progress in reasoning capabilities. Yet in low-resource native settings, many suffer from cross-lingual collapse, reverting to English during intermediate steps that require complex logical reasoning. This presents a cold-start bottleneck for policy optimization, whereas standard fine-tuning risks catastrophic forgetting due to cross-lingual representation drift. To address these challenges, we introduce the Onramp-Sequence Cross-Distillation (OSCD), a post-training algorithm that projects high-resource reasoning trajectories into low-resource vocabulary subspaces during generative training rollouts via an integrated translator agentic loop, ensuring the stable and efficient translation of dynamically generated reference samples for fine-tuning. This is coupled with joint-embedding semantic alignment of both reference and target-language reasoning traces, thereby bridging the pairwise cross-lingual representational gaps. Comprehensive evaluations using the AIME25 and HMMT25 benchmarks demonstrate that OSCD yields up to 3.2 times overall improvements in native Southeast Asian languages for mathematical reasoning, of which the joint-embedding semantic alignment component contributes up to 6.4% improvements in linguistic debiasing over translation-only baselines.

## 11-040 | PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource Languages
- arXiv: 2607.05992  first public: 2026-07-07  latest: 2026-07-07  primary cat: cs.CL
- authors (17): Daryna Dementieva; Nikolay Babakov; Kathy Hämmerl; Ilseyar Alimova; Jindřich Libovický; Shu Okabe ...
- seed subtopic: 低资源语言数学评测; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://huggingface.co/front/assets/huggingface
- pages: 51

ABSTRACT: Mathematical reasoning has become a central task for evaluating and tuning reasoning Large Language Models (LLMs), yet existing benchmarks remain heavily biased toward high-resource languages, with English and Chinese dominating both pre-training corpora and evaluation suites. The recently released PolyMath (Wang et al., 2025) dataset represents a significant step forward, yet its coverage is still limited to 18 only high-resource languages. To address this gap, we introduce PluraMath, an extension of PolyMath to 18 additional {underrepresented languages spanning 6 language families -- ranging from mid-resource to extreme low-resource settings. We constructed the dataset through a human-curated pipeline, where native speakers thoroughly validated pre-computed translations. Using PluraMath, we then benchmark 27 reasoning LLMs across four model scales -- small, mid-size, large, and closed-source ensembles -- probing the multilingual mathematical reasoning capabilities of state-of-the-art models under diverse linguistic conditions. Our fine-grained analysis confirms a persistent gap in mathematical reasoning performance between high-resource and underrepresented languages, with stronger results largely associated with better instruction-following ability. We fully open-source our dataset, data acquisition pipeline, and evaluation framework, with the goal of lowering the barrier to multilingual benchmark development for underrepresented communities.

## 11-041 | Crosslingual On-Policy Self-Distillation for Multilingual Reasoning
- arXiv: 2605.09548  first public: 2026-05-10  latest: 2026-05-10  primary cat: cs.CL
- authors (4): Yihong Liu; Raoyuan Zhao; Michael A. Hedderich; Hinrich Schütze
- seed subtopic: 跨语言自蒸馏; type: 原始研究; cross: ['09']
- arXiv comment: preprint
- URLs on first pages of PDF: https://github.com/cisnlp/COPSD
- pages: 24

ABSTRACT: Large language models (LLMs) have achieved remarkable progress in mathematical reasoning, but this ability is not equally accessible across languages. Especially low-resource languages exhibit much lower reasoning performance. To address this, we propose Crosslingual On-Policy Self-Distillation (COPSD), which transfers a model's own high-resource reasoning behavior to low-resource languages. COPSD uses the same model as student and teacher: the student sees only the low-resource problem, while the teacher receives privileged crosslingual context, including the problem translation and reference solution in English. Training minimizes full-distribution token-level divergence on the student's own rollouts, providing dense supervision while avoiding the sparsity and instability of outcome-only reinforcement learning (RL). Experiments on 17 low-resource African languages show that COPSD consistently improves low-resource mathematical reasoning across model sizes and substantially outperforms Group Relative Policy Optimization (GRPO). Further analyses show that COPSD improves answer-format adherence, strengthens test-time scaling, and generalizes to harder multilingual reasoning benchmarks, with especially large gains for lower-resource languages. We make our code and data available at: https://github.com/cisnlp/COPSD.

## 11-042 | Large Language Models Are Cross-Lingual Knowledge-Free Reasoners
- arXiv: 2406.16655  first public: 2024-06-24  latest: 2025-03-03  primary cat: cs.CL
- authors (8): Peng Hu; Sizhe Liu; Changjiang Gao; Xin Huang; Xue Han; Junlan Feng ...
- seed subtopic: 推理与知识解耦迁移; type: 原始研究; cross: []
- pages: 18

ABSTRACT: Large Language Models have demonstrated impressive reasoning capabilities across multiple languages. However, the relationship between capabilities in different languages is less explored. In this work, we decompose the process of reasoning tasks into two separated components: knowledge retrieval and knowledge-free reasoning, and analyze the relationship between cross-lingual transferability and these two components. With adapted commonsense reasoning datasets and constructed knowledge-free reasoning datasets, we show that the knowledge-free reasoning capability can be nearly perfectly transferred across various source-target language directions despite the secondary impact of resource in some specific target languages, while cross-lingual knowledge retrieval significantly hinders the transfer. Moreover, by analyzing the hidden states and feed-forward network neuron activation during the reasoning, we show that higher similarity of hidden representations and larger overlap of activated neurons could explain the better cross-lingual transferability of knowledge-free reasoning than knowledge retrieval. Thus, we hypothesize that knowledge-free reasoning shares similar neurons in different languages for reasoning, while knowledge is stored separately in different languages. Our code and data is available at: https://github.com/NJUNLP/Knowledge-Free-Reasoning.

## 11-043 | Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models
- arXiv: 2408.10151  first public: 2024-08-19  latest: 2024-08-19  primary cat: cs.CL
- authors (4): Amey Hengle; Prasoon Bajpai; Soham Dan; Tanmoy Chakraborty
- seed subtopic: 多语言长上下文检索; type: 基准与数据集; cross: []
- pages: 13

ABSTRACT: While recent large language models (LLMs) demonstrate remarkable abilities in responding to queries in diverse languages, their ability to handle long multilingual contexts is unexplored. As such, a systematic evaluation of the long-context capabilities of LLMs in multilingual settings is crucial, specifically in the context of information retrieval. To address this gap, we introduce the MultiLingual Needle-in-a-Haystack (MLNeedle) test, designed to assess a model's ability to retrieve relevant information (the needle) from a collection of multilingual distractor texts (the haystack). This test serves as an extension of the multilingual question-answering task, encompassing both monolingual and cross-lingual retrieval. We evaluate four state-of-the-art LLMs on MLNeedle. Our findings reveal that model performance can vary significantly with language and needle position. Specifically, we observe that model performance is the lowest when the needle is (i) in a language outside the English language family and (ii) located in the middle of the input context. Furthermore, although some models claim a context size of $8k$ tokens or greater, none demonstrate satisfactory cross-lingual retrieval performance as the context length increases. Our analysis provides key insights into the long-context behavior of LLMs in multilingual settings to guide future evaluation protocols. To our knowledge, this is the first study to investigate the multilingual long-context behavior of LLMs.

## 11-044 | Evaluating Multilingual Long-Context Models for Retrieval and Reasoning
- arXiv: 2409.18006  first public: 2024-09-26  latest: 2024-10-12  primary cat: cs.CL
- authors (5): Ameeta Agrawal; Andy Dang; Sina Bagheri Nezhad; Rhitabrat Pokharel; Russell Scheinberg
- seed subtopic: 多语言长上下文推理; type: 基准与数据集; cross: []
- arXiv comment: To appear at MRL 2024
- URLs on first pages of PDF: https://huggingface.co/NousResearch/ https://huggingface.co/meta-llama/
- pages: 16

ABSTRACT: Recent large language models (LLMs) demonstrate impressive capabilities in handling long contexts, some exhibiting near-perfect recall on synthetic retrieval tasks. However, these evaluations have mainly focused on English text and involved a single target sentence within lengthy contexts. Our work investigates how LLM performance generalizes to multilingual settings with multiple hidden target sentences. We create a new dataset -- mLongRR -- to comprehensively evaluate several multilingual long-context LLMs on retrieval and reasoning tasks across five languages: English, Vietnamese, Indonesian, Swahili, and Somali. These languages share the Latin script but belong to distinct language families and resource levels. Our analysis reveals a significant performance gap between languages. The best-performing models such as Gemini-1.5 and GPT-4o, achieve around 96% accuracy in English to around 36% in Somali with a single target sentence. However, this accuracy drops to 40% in English and 0% in Somali when dealing with three target sentences. Our findings highlight the challenges long-context LLMs face when processing longer contexts, an increase in the number of target sentences, or languages of lower resource levels.

## 11-045 | One ruler to measure them all: Benchmarking multilingual long-context language models
- arXiv: 2503.01996  first public: 2025-03-03  latest: 2025-09-30  primary cat: cs.CL
- authors (4): Yekyung Kim; Jenna Russell; Marzena Karpinska; Mohit Iyyer
- seed subtopic: 多语言长上下文基准; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/mungg/OneRuler
- pages: 29

ABSTRACT: We present ONERULER, a multilingual benchmark designed to evaluate long-context language models across 26 languages. ONERULER adapts the English-only RULER benchmark (Hsieh et al., 2024) by including seven synthetic tasks that test both retrieval and aggregation, including new variations of the "needle-in-a-haystack" task that allow for the possibility of a nonexistent needle. We create ONERULER through a two-step process, first writing English instructions for each task and then collaborating with native speakers to translate them into 25 additional languages. Experiments with both open-weight and closed LLMs reveal a widening performance gap between low- and high-resource languages as context length increases from 8K to 128K tokens. Surprisingly, English is not the top-performing language on long-context tasks (ranked 6th out of 26), with Polish emerging as the top language. Our experiments also show that many LLMs (particularly OpenAI's o3-mini-high) incorrectly predict the absence of an answer, even in high-resource languages. Finally, in cross-lingual scenarios where instructions and context appear in different languages, performance can fluctuate by up to 20% depending on the instruction language. We hope the release of ONERULER will facilitate future research into improving multilingual and cross-lingual long-context training pipelines.

## 11-046 | Can LLMs reason over extended multilingual contexts? Towards long-context evaluation beyond retrieval and haystacks
- arXiv: 2504.12845  first public: 2025-04-17  latest: 2025-04-17  primary cat: cs.CL
- authors (4): Amey Hengle; Prasoon Bajpai; Soham Dan; Tanmoy Chakraborty
- seed subtopic: 多语言长上下文推理; type: 基准与数据集; cross: []
- arXiv comment: 33 Pages in Total - 23 (Main Manuscript) + 10 (Appendix)
- URLs on first pages of PDF: https://github.com/AmeyHengle/multilingual-long-context-reasoning
- pages: 33

ABSTRACT: Existing multilingual long-context benchmarks, often based on the popular needle-in-a-haystack test, primarily evaluate a model's ability to locate specific information buried within irrelevant texts. However, such a retrieval-centric approach is myopic and inherently limited, as successful recall alone does not indicate a model's capacity to reason over extended contexts. Moreover, these benchmarks are susceptible to data leakage, short-circuiting, and risk making the evaluation a priori identifiable. To address these limitations, we introduce MLRBench, a new synthetic benchmark for multilingual long-context reasoning. Unlike existing benchmarks, MLRBench goes beyond surface-level retrieval by including tasks that assess multi-hop inference, aggregation, and epistemic reasoning. Spanning seven languages, MLRBench is designed to be parallel, resistant to leakage, and scalable to arbitrary context lengths. Our extensive experiments with an open-weight large language model (LLM) reveal a pronounced gap between high- and low-resource languages, particularly for tasks requiring the model to aggregate multiple facts or predict the absence of information. We also find that, in multilingual settings, LLMs effectively utilize less than 30% of their claimed context length. Although off-the-shelf Retrieval Augmented Generation helps alleviate this to a certain extent, it does not solve the long-context problem. We open-source MLRBench to enable future research in improved evaluation and training of multilingual LLMs.

## 11-047 | Long-context Non-factoid Question Answering in Indic Languages
- arXiv: 2504.13615  first public: 2025-04-18  latest: 2025-06-13  primary cat: cs.CL
- authors (3): Ritwik Mishra; Rajiv Ratn Shah; Ponnurangam Kumaraguru
- seed subtopic: 印度语言长文问答; type: 原始研究; cross: ['12']
- arXiv comment: Short version of this manuscript accepted at https://bda2025.iiitb.net/
- pages: 16

ABSTRACT: Question Answering (QA) tasks, which involve extracting answers from a given context, are relatively straightforward for modern Large Language Models (LLMs) when the context is short. However, long contexts pose challenges due to the quadratic complexity of the self-attention mechanism. This challenge is compounded in Indic languages, which are often low-resource. This study explores context-shortening techniques, including Open Information Extraction (OIE), coreference resolution, Answer Paragraph Selection (APS), and their combinations, to improve QA performance. Compared to the baseline of unshortened (long) contexts, our experiments on four Indic languages (Hindi, Tamil, Telugu, and Urdu) demonstrate that context-shortening techniques yield an average improvement of 4\% in semantic scores and 47\% in token-level scores when evaluated on three popular LLMs without fine-tuning. Furthermore, with fine-tuning, we achieve an average increase of 2\% in both semantic and token-level scores. Additionally, context-shortening reduces computational overhead. Explainability techniques like LIME and SHAP reveal that when the APS model confidently identifies the paragraph containing the answer, nearly all tokens within the selected text receive high relevance scores. However, the study also highlights the limitations of LLM-based QA systems in addressing non-factoid questions, particularly those requiring reasoning or debate. Moreover, verbalizing OIE-generated triples does not enhance system performance. These findings emphasize the potential of context-shortening techniques to improve the efficiency and effectiveness of LLM-based QA systems, especially for low-resource languages. The source code and resources are available at https://github.com/ritwikmishra/IndicGenQA.

## 11-048 | RULER: What's the Real Context Size of Your Long-Context Language Models?
- arXiv: 2404.06654  first public: 2024-04-09  latest: 2024-08-06  primary cat: cs.CL
- authors (8): Cheng-Ping Hsieh; Simeng Sun; Samuel Kriman; Shantanu Acharya; Dima Rekesh; Fei Jia ...
- seed subtopic: 长上下文评测方法; type: 基准与数据集; cross: []
- arXiv comment: COLM 2024; Code is available at https://github.com/hsiehjackson/RULER
- URLs on first pages of PDF: https://github.com/hsiehjackson/RULER
- pages: 27

ABSTRACT: The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the "needle") from long distractor texts (the "haystack"), has been widely adopted to evaluate long-context language models (LMs). However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding. To provide a more comprehensive evaluation of long-context LMs, we create a new synthetic benchmark RULER with flexible configurations for customized sequence length and task complexity. RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER. Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K. Our analysis of Yi-34B, which supports context length of 200K, reveals large room for improvement as we increase input length and task complexity. We open source RULER to spur comprehensive evaluation of long-context LMs.

## 11-049 | JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models
- arXiv: 2501.10868  first public: 2025-01-18  latest: 2025-02-27  primary cat: cs.CL
- authors (9): Saibo Geng; Hudson Cooper; Michał Moskal; Samuel Jenkins; Julian Berman; Nathan Ranchin ...
- seed subtopic: 结构化输出与约束解码; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/guidance-ai/jsonschemabench
- pages: 32

ABSTRACT: Reliably generating structured outputs has become a critical capability for modern language model (LM) applications. Constrained decoding has emerged as the dominant technology across sectors for enforcing structured outputs during generation. Despite its growing adoption, little has been done with the systematic evaluation of the behaviors and performance of constrained decoding. Constrained decoding frameworks have standardized around JSON Schema as a structured data format, with most uses guaranteeing constraint compliance given a schema. However, there is poor understanding of the effectiveness of the methods in practice. We present an evaluation framework to assess constrained decoding approaches across three critical dimensions: efficiency in generating constraint-compliant outputs, coverage of diverse constraint types, and quality of the generated outputs. To facilitate this evaluation, we introduce JSONSchemaBench, a benchmark for constrained decoding comprising 10K real-world JSON schemas that encompass a wide range of constraints with varying complexity. We pair the benchmark with the existing official JSON Schema Test Suite and evaluate six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini. Through extensive experiments, we gain insights into the capabilities and limitations of constrained decoding on structured generation with real-world JSON schemas. Our work provides actionable insights for improving constrained decoding frameworks and structured generation tasks, setting a new standard for evaluating constrained decoding and structured generation. We release JSONSchemaBench at https://github.com/guidance-ai/jsonschemabench

## 11-050 | Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models
- arXiv: 2408.02442  first public: 2024-08-05  latest: 2024-10-14  primary cat: cs.CL
- authors (6): Zhi Rui Tam; Cheng-Kuang Wu; Yi-Lin Tsai; Chieh-Yen Lin; Hung-yi Lee; Yun-Nung Chen
- seed subtopic: 格式约束对推理的影响; type: 原始研究; cross: []
- arXiv comment: 18 pages
- URLs on first pages of PDF: https://github.com/appier-research/ https://github.com/huggingface/
- pages: 19

ABSTRACT: Structured generation, the process of producing content in standardized formats like JSON and XML, is widely utilized in real-world applications to extract key output information from large language models (LLMs). This study investigates whether such constraints on generation space impact LLMs abilities, including reasoning and domain knowledge comprehension. Specifically, we evaluate LLMs performance when restricted to adhere to structured formats versus generating free-form responses across various common tasks. Surprisingly, we observe a significant decline in LLMs reasoning abilities under format restrictions. Furthermore, we find that stricter format constraints generally lead to greater performance degradation in reasoning tasks.

## 11-051 | Lost in Execution: On the Multilingual Robustness of Tool Calling in Large Language Models
- arXiv: 2601.05366  first public: 2026-01-08  latest: 2026-06-28  primary cat: cs.CL
- authors (6): Zheng Luo; T Pranav Kutralingam; Ogochukwu N Okoani; Wanpeng Xu; Hua Wei; Xiyang Hu
- seed subtopic: 多语言工具调用鲁棒性; type: 基准与数据集; cross: []
- arXiv comment: ACL 2026
- pages: 19

ABSTRACT: Large Language Models (LLMs) are increasingly deployed as agents that invoke external tools through structured function calls. While recent work reports strong tool-calling performance under standard English-centric evaluations, the robustness of tool calling under multilingual user interactions remains underexplored. In this work, we introduce MLCL, a diagnostic benchmark, and conduct a systematic evaluation of multilingual tool calling across Chinese, Hindi, and the low-resource language Igbo. Through fine-grained error analysis, we show that many failures occur despite correct intent understanding and tool selection. We identify parameter value language mismatch as a dominant failure mode, where models generate semantically appropriate parameter values in the user's language, violating language-invariant execution conventions. We further evaluate several inference-time system strategies and find that while these strategies substantially reduce language-induced execution errors, none of them can fully recover English-level performance.

## 11-052 | Enhancing Tool Calling in LLMs with the International Tool Calling Dataset
- arXiv: 2603.05515  first public: 2026-01-21  latest: 2026-01-21  primary cat: cs.HC
- authors (2): Zuoyu Zhang; Yancheng Zhu
- seed subtopic: 国际化工具调用数据; type: 基准与数据集; cross: []
- pages: 19

ABSTRACT: Tool calling allows large language models (LLMs) to interact with external systems like APIs, enabling applications in customer support, data analysis, and dynamic content generation. While recent benchmarks have advanced tool-use research, they suffer from key limitations, including reliance on simulated or restricted APIs, limited reproducibility, and a lack of cultural and geographic diversity. To address these gaps, we introduce International Tool Calling (ITC), a large-scale, multilingual benchmark designed for realistic, globally distributed tool-calling scenarios. ITC includes 3,571 real APIs and 17,540 tool calling tasks across 20 categories and 40 countries. Experiments reveal substantial performance gaps between open- and closed-source LLMs, while fine-tuning on ITC yields significant improvements, particularly for non-English queries, enhancing cross-lingual generalization, reasoning consistency, and robustness to out-of-domain tools. ITC provides a valuable benchmark for advancing LLM robustness and performance in complex, multi-tool, and international scenarios. Dataset: https://anonymous.4open.science/r/International-Tool-Calling-ITC-dataset-FAF4/.

## 11-053 | Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation
- arXiv: 2509.14477  first public: 2025-09-17  latest: 2025-09-17  primary cat: cs.CL
- authors (4): Thales Sales Almeida; João Guilherme Alves Santos; Thiago Laitz; Giovana Kerche Bonás
- seed subtopic: 多语言区域化智能体评测; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://github.com/TropicAI-Research/Ticket-Bench
- pages: 11

ABSTRACT: Large language models (LLMs) are increasingly deployed as task-oriented agents, where success depends on their ability to generate accurate function calls under realistic, multilingual conditions. However, existing agent evaluations largely overlook cultural and linguistic diversity, often relying on monolingual or naively translated benchmarks. We introduce Ticket-Bench, a benchmark for multilingual agent evaluation in task-oriented scenarios. Ticket-Bench simulates the domain of soccer ticket purchases across six major languages: Portuguese, English, Spanish, German, Italian, and French. Using localized teams, cities, and user profiles to provide a higher level of realism. We evaluate a wide range of commercial and open-source LLMs, measuring function-calling accuracy and consistency across languages. Results show that reasoning-oriented models (e.g., GPT-5, Qwen3-235B) dominate performance but still exhibit notable cross-lingual disparities. These findings underscore the need for culturally aware, multilingual benchmarks to guide the development of robust LLM agents.

## 11-054 | Tool Calling for Arabic LLMs: Data Strategies and Instruction Tuning
- arXiv: 2509.20957  first public: 2025-09-25  latest: 2025-09-25  primary cat: cs.CL
- authors (4): Asim Ersoy; Enes Altinisik; Husrev Taha Sencar; Kareem Darwish
- seed subtopic: 阿拉伯语工具调用; type: 原始研究; cross: ['08']
- journal_ref: ArabicNLP 2025
- URLs on first pages of PDF: https://huggingface.co/collections/QCRI/ https://huggingface.co/datasets/NousResearch/ https://huggingface.co/datasets/glaiveai/ https://huggingface.co/datasets/llamafactory/
- pages: 12

ABSTRACT: Tool calling is a critical capability that allows Large Language Models (LLMs) to interact with external systems, significantly expanding their utility. However, research and resources for tool calling are predominantly English-centric, leaving a gap in our understanding of how to enable this functionality for other languages, such as Arabic. This paper investigates three key research questions: (1) the necessity of in-language (Arabic) tool-calling data versus relying on cross-lingual transfer, (2) the effect of general-purpose instruction tuning on tool-calling performance, and (3) the value of fine-tuning on specific, high-priority tools. To address these questions, we conduct extensive experiments using base and post-trained variants of an open-weight Arabic LLM. To enable this study, we bridge the resource gap by translating and adapting two open-source tool-calling datasets into Arabic. Our findings provide crucial insights into the optimal strategies for developing robust tool-augmented agents for Arabic.

## 11-055 | Teaching a Language Model to Speak the Language of Tools
- arXiv: 2506.23394  first public: 2025-06-29  latest: 2025-06-29  primary cat: cs.IR
- authors (1): Simeon Emanuilov
- seed subtopic: 小语种模型函数调用适配; type: 原始研究; cross: ['08']
- URLs on first pages of PDF: https://github.com/insait-institute/lm-evaluation-harness-bg/
- pages: 20

ABSTRACT: External tool integration through function-calling is essential for practical language model applications, yet most multilingual models lack reliable tool-use capabilities in non-English languages. Even state-of-the-art multilingual models struggle with determining when to use tools and generating the structured outputs required for function calls, often exhibiting language confusion when prompted in lower-resource languages. This work presents a methodology for adapting existing language models to enable robust tool use in any target language, using Bulgarian as a case study. The approach involves continued training of the BgGPT model series (2.6B, 9B, 27B parameters) on a novel bilingual dataset of 10,035 function-calling examples designed to support standardized protocols like MCP (Model Context Protocol). The research introduces TUCAN (Tool-Using Capable Assistant Navigator), which achieves up to 28.75% improvement in function-calling accuracy over base models while preserving core language understanding, as verified on established Bulgarian benchmarks. Beyond accuracy gains, TUCAN models demonstrate production-ready response formatting with clean, parsable function calls, contrasting with the verbose and inconsistent outputs of base models. The models, evaluation framework, and dataset are released to enable replication for other languages. This work demonstrates a practical approach for extending tool-augmented capabilities beyond English-centric systems.

## 11-056 | Enhancing Function-Calling Capabilities in LLMs: Strategies for Prompt Formats, Data Integration, and Multilingual Translation
- arXiv: 2412.01130  first public: 2024-12-02  latest: 2024-12-04  primary cat: cs.CL
- authors (4): Yi-Chang Chen; Po-Chun Hsu; Chan-Jan Hsu; Da-shan Shiu
- seed subtopic: 函数调用多语言翻译数据; type: 原始研究; cross: []
- pages: 13

ABSTRACT: Large language models (LLMs) have significantly advanced autonomous agents, particularly in zero-shot tool usage, also known as function calling. This research delves into enhancing the function-calling capabilities of LLMs by exploring different approaches, including prompt formats for integrating function descriptions, blending function-calling and instruction-following data, introducing a novel Decision Token for conditional prompts, leveraging chain-of-thought reasoning, and overcoming multilingual challenges with a translation pipeline. Our key findings and contributions are as follows: (1) Instruction-following data improves both function-calling accuracy and relevance detection. (2) The use of the newly proposed Decision Token, combined with synthetic non-function-call data, enhances relevance detection. (3) A tailored translation pipeline effectively overcomes multilingual limitations, demonstrating significant improvements in Traditional Chinese. These insights highlight the potential for improved function-calling capabilities and multilingual applications in LLMs.

## 11-057 | PolyWorkBench: Benchmarking LLM Agents for Cross-Lingual Long-Horizon Workflows
- arXiv: 2607.06008  first public: 2026-07-07  latest: 2026-08-17  primary cat: cs.AI
- authors (8): Hongliang Li; Yijin Liu; Zhiwei Zhang; Zihe Liu; Xinyue Lou; Jinan Xu ...
- seed subtopic: 跨语言长程工作流智能体; type: 基准与数据集; cross: []
- arXiv comment: 17 Pages, 5 figures
- pages: 17

ABSTRACT: While Large Language Model (LLM) agents excel at monolingual long-horizon planning and tool use, enterprise workflows inherently require processing multilingual resources across extended trajectories. The interaction between multilinguality and long-horizon execution, however, remains underexplored. We introduce PolyWorkBench, a benchmark designed to evaluate LLM agents on multilingual, long-horizon workplace workflows. PolyWorkBench features 67 tasks across five core domains: commerce, knowledge work, legal analysis, localization, and manufacturing. Tasks are authored by the paper's authors from real-world data seeds and independently verified through a second-author audit. Agents must integrate heterogeneous multilingual inputs, execute iterative tool-use trajectories, and produce structured domain artifacts. To rigorously assess performance, we adopt Grade, a task-specific structural scoring rubric, as our primary ranking metric, and complement it with Pytest for executable state verification and LLM-as-Judge for semantic quality diagnostics. Benchmark evaluations reveal that agent performance varies substantially across languages and drops sharply on the harder cross-lingual tasks, and our analysis shows that multilingual execution exposes systematic failure modes across planning, tool interaction, and decision-making in long-horizon agents.

## 11-058 | Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents
- arXiv: 2606.31648  first public: 2026-06-30  latest: 2026-06-30  primary cat: cs.AI
- authors (9): Utsav Garg; Sungjin Hong; Jason Jung; Justin Lee; Shaan Desai; Joon Hee Kim ...
- seed subtopic: 工具智能体思考语言; type: 原始研究; cross: []
- pages: 7

ABSTRACT: We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multilingual supervised fine-tuning, reinforcement learning with verifiable rewards for multi-step tool-use tasks, language-consistency rewards for Korean user-facing responses, and 4-bit quantization for single-GPU serving. The adapted model improves mathematical reasoning, function calling, and agentic natural-language-to-SQL (NL2SQL) performance while preserving general Korean and English instruction-following quality. These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.

## 11-059 | BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents
- arXiv: 2609.23490  first public: 2026-09-20  latest: 2026-10-23  primary cat: cs.CL
- authors (10): Peng Kuang; Yuchun Fan; Jiangnan Li; Minghao Wu; Jialong Tang; Hao-Ran Wei ...
- seed subtopic: 多语言智能体基准; type: 基准与数据集; cross: ['15']
- arXiv comment: 20 pages, 11 tables, and 7 figures
- URLs on first pages of PDF: https://github.com/QwenLM/BabelArena
- pages: 20

ABSTRACT: Large language model (LLM) agents increasingly execute multi-step workflows through tool use and interaction with users and environments. However, current agent evaluations are largely English-centric, limiting our understanding of agent capabilities in multilingual settings. We introduce BabelFlow, a benchmark-general agentic workflow that adapts existing agent benchmarks to new languages by analyzing runtime dependencies, coordinating structure-preserving translation, and combining multi-layer verification with human review to preserve task and evaluation semantics. Using BabelFlow, we construct BabelArena, a task-aligned benchmark comprising 16,146 instances derived from 702 canonical tasks across four benchmark families, 13 domains, and 23 languages. Experiments with five frontier models show that no single model dominates across benchmark families and that cross-language disparities extend well beyond task success. Lower-resource languages exhibit distinct failure patterns, with larger shares of tool-use and control-flow errors rather than answer-quality errors alone, pointing to gaps in reliable task execution across the resource levels of these languages. On the same tasks, agents in low-resource languages also consume substantially more tokens than in English (up to roughly twice the input) without proportional increases in interaction length, and language consistency degrades further on tasks requiring structured output, where switches are directed overwhelmingly toward English. We believe BabelArena provides a foundation for advancing research on reliable and efficient multilingual agents.

## 11-060 | APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets
- arXiv: 2406.18518  first public: 2024-06-26  latest: 2024-06-26  primary cat: cs.CL
- authors (17): Zuxin Liu; Thai Hoang; Jianguo Zhang; Ming Zhu; Tian Lan; Shirley Kokane ...
- seed subtopic: 可验证函数调用数据合成; type: 原始研究; cross: ['09']
- URLs on first pages of PDF: https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k
- pages: 20

ABSTRACT: The advancement of function-calling agent models requires diverse, reliable, and high-quality datasets. This paper presents APIGen, an automated data generation pipeline designed to synthesize verifiable high-quality datasets for function-calling applications. We leverage APIGen and collect 3,673 executable APIs across 21 different categories to generate diverse function-calling datasets in a scalable and structured manner. Each data in our dataset is verified through three hierarchical stages: format checking, actual function executions, and semantic verification, ensuring its reliability and correctness. We demonstrate that models trained with our curated datasets, even with only 7B parameters, can achieve state-of-the-art performance on the Berkeley Function-Calling Benchmark, outperforming multiple GPT-4 models. Moreover, our 1B model achieves exceptional performance, surpassing GPT-3.5-Turbo and Claude-3 Haiku. We release a dataset containing 60,000 high-quality entries, aiming to advance the field of function-calling agent domains. The dataset is available on Huggingface: https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k and the project homepage: https://apigen-pipeline.github.io/

## 11-061 | ToolACE: Winning the Points of LLM Function Calling
- arXiv: 2409.00920  first public: 2024-09-02  latest: 2025-07-25  primary cat: cs.LG
- authors (27): Weiwen Liu; Xu Huang; Xingshan Zeng; Xinlong Hao; Shuai Yu; Dexun Li ...
- seed subtopic: 函数调用数据合成; type: 原始研究; cross: []
- arXiv comment: 21 pages, 22 figures
- URLs on first pages of PDF: https://huggingface.co/Team-ACE
- pages: 23

ABSTRACT: Function calling significantly extends the application boundary of large language models, where high-quality and diverse training data is critical for unlocking this capability. However, real function-calling data is quite challenging to collect and annotate, while synthetic data generated by existing pipelines tends to lack coverage and accuracy. In this paper, we present ToolACE, an automatic agentic pipeline designed to generate accurate, complex, and diverse tool-learning data. ToolACE leverages a novel self-evolution synthesis process to curate a comprehensive API pool of 26,507 diverse APIs. Dialogs are further generated through the interplay among multiple agents, guided by a formalized thinking process. To ensure data accuracy, we implement a dual-layer verification system combining rule-based and model-based checks. We demonstrate that models trained on our synthesized data, even with only 8B parameters, achieve state-of-the-art performance on the Berkeley Function-Calling Leaderboard, rivaling the latest GPT-4 models. Our model and a subset of the data are publicly available at https://huggingface.co/Team-ACE.

## 11-075 | Cross-Lingual Consistency: A Novel Inference Framework for Advancing Reasoning in Large Language Models
- arXiv: 2504.01857  first public: 2025-04-02  latest: 2025-04-02  primary cat: cs.CL
- authors (5): Zhiwei Yu; Tuo Li; Changhong Wang; Hui Chen; Lang Zhou
- seed subtopic: 跨语言一致性推理框架; type: 原始研究; cross: []
- pages: 23

ABSTRACT: Chain-of-thought (CoT) has emerged as a critical mechanism for enhancing reasoning capabilities in large language models (LLMs), with self-consistency demonstrating notable promise in boosting performance. However, inherent linguistic biases in multilingual training corpora frequently cause semantic drift and logical inconsistencies, especially in sub-10B parameter LLMs handling complex inference tasks. To overcome these constraints, we propose the Cross-Lingual Consistency (CLC) framework, an innovative inference paradigm that integrates multilingual reasoning paths through majority voting to elevate LLMs' reasoning capabilities. Empirical evaluations on the CMATH dataset reveal CLC's superiority over the conventional self-consistency method, delivering 9.5%, 6.5%, and 6.0% absolute accuracy gains for DeepSeek-Math-7B-Instruct, Qwen2.5-Math-7B-Instruct, and Gemma2-9B-Instruct respectively. Expanding CLC's linguistic scope to 11 diverse languages implies two synergistic benefits: 1) neutralizing linguistic biases in multilingual training corpora through multilingual ensemble voting, 2) escaping monolingual reasoning traps by exploring the broader multilingual solution space. This dual benefits empirically enables more globally optimal reasoning paths compared to monolingual self-consistency baselines, as evidenced by the 4.1%-18.5% accuracy gains using Gemma2-9B-Instruct on the MGSM dataset.

## 11-076 | What Makes Good Multilingual Reasoning? Disentangling Traces with Measurable Features
- arXiv: 2604.04720  first public: 2026-04-06  latest: 2026-09-20  primary cat: cs.CL
- authors (3): Dayeon Ki; Kevin Duh; Marine Carpuat
- seed subtopic: 多语言推理轨迹质量; type: 原始研究; cross: []
- arXiv comment: COLM 2026
- URLs on first pages of PDF: https://github.com/dayeonki/multilingual_reasoning
- pages: 32

ABSTRACT: Large Reasoning Models (LRMs) still exhibit large performance gaps between English and other languages, yet much current work assumes these gaps can be closed simply by making reasoning in every language resemble English reasoning. This work challenges this assumption by asking instead: what actually characterizes successful reasoning traces in multilingual settings, and to what extent do English-derived reasoning features genuinely help in other languages? We first define a suite of measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow aspects of reasoning traces, and use logistic regression to quantify how each feature associates with final answer accuracy. We further train sparse autoencoders over multilingual traces to automatically discover latent reasoning concepts that instantiate or extend these features. Finally, we use the features to re-rank traces and measure their impact on accuracy at test time. Across two mathematical reasoning benchmarks, four LRMs, and ten languages, we find that most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some. Our findings challenge English-centric reward designs and point toward adaptive objectives that accommodate language-specific reasoning patterns, with concrete implications for multilingual benchmark and reward design.

## 11-077 | CURE-Med: Curriculum-Informed Reinforcement Learning for Multilingual Medical Reasoning
- arXiv: 2601.13262  first public: 2026-01-19  latest: 2026-04-26  primary cat: cs.AI
- authors (6): Eric Onyame; Akash Ghosh; Subhadip Baidya; Sriparna Saha; Xiuying Chen; Chirag Agarwal
- seed subtopic: 多语言领域推理强化学习; type: 原始研究; cross: []
- arXiv comment: Accepted at ACL 2026, main conference, oral presentation
- pages: 22

ABSTRACT: While large language models (LLMs) have shown to perform well on monolingual mathematical and commonsense reasoning, they remain unreliable for multilingual medical reasoning applications, hindering their deployment in multilingual healthcare settings. We address this by first introducing CUREMED-BENCH, a high-quality multilingual medical reasoning dataset with open-ended reasoning queries with a single verifiable answer, spanning thirteen languages, including underrepresented languages such as Amharic, Yoruba, and Swahili. Building on this dataset, we propose CURE-MED, a curriculum-informed reinforcement learning framework that integrates code-switching-aware supervised fine-tuning and Group Relative Policy Optimization to jointly improve logical correctness and language stability. Across thirteen languages, our approach consistently outperforms strong baselines and scales effectively, achieving 85.21% language consistency and 54.35% logical correctness at 7B parameters, and 94.96% language consistency and 70.04% logical correctness at 32B parameters. These results support reliable and equitable multilingual medical reasoning in LLMs. The code and dataset are available at https://cure-med.github.io/
