# Brief for annotation: 07 预训练与持续预训练

## 07-001 | Simple and Scalable Strategies to Continually Pre-train Large Language Models
- arXiv: 2403.08763  first public: 2024-03-13  latest: 2024-09-04  primary cat: cs.LG
- authors (8): Adam Ibrahim; Benjamin Thérien; Kshitij Gupta; Mats L. Richter; Quentin Anthony; Timothée Lesort ...
- seed subtopic: 学习率重热与重放; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/EleutherAI/gpt-neox
- pages: 45

ABSTRACT: Large language models (LLMs) are routinely pre-trained on billions of tokens, only to start the process over again once new data becomes available. A much more efficient solution is to continually pre-train these models, saving significant compute compared to re-training. However, the distribution shift induced by new data typically results in degraded performance on previous data or poor adaptation to the new data. In this work, we show that a simple and scalable combination of learning rate (LR) re-warming, LR re-decaying, and replay of previous data is sufficient to match the performance of fully re-training from scratch on all available data, as measured by the final loss and the average score on several language model (LM) evaluation benchmarks. Specifically, we show this for a weak but realistic distribution shift between two commonly used LLM pre-training datasets (English$\rightarrow$English) and a stronger distribution shift (English$\rightarrow$German) at the $405$M parameter model scale with large dataset sizes (hundreds of billions of tokens). Selecting the weak but realistic shift for larger-scale experiments, we also find that our continual learning strategies match the re-training baseline for a 10B parameter LLM. Our results demonstrate that LLMs can be successfully updated via simple and scalable continual learning strategies, matching the re-training baseline using only a fraction of the compute. Finally, inspired by previous work, we propose alternatives to the cosine learning rate schedule that help circumvent forgetting induced by LR re-warming and that are not bound to a fixed token budget.

## 07-002 | Continual Pre-Training of Large Language Models: How to (re)warm your model?
- arXiv: 2308.04014  first public: 2023-08-08  latest: 2023-09-06  primary cat: cs.CL
- authors (8): Kshitij Gupta; Benjamin Thérien; Adam Ibrahim; Mats L. Richter; Quentin Anthony; Eugene Belilovsky ...
- seed subtopic: 学习率重热; type: 原始研究; cross: []
- pages: 11

ABSTRACT: Large language models (LLMs) are routinely pre-trained on billions of tokens, only to restart the process over again once new data becomes available. A much cheaper and more efficient solution would be to enable the continual pre-training of these models, i.e. updating pre-trained models with new data instead of re-training them from scratch. However, the distribution shift induced by novel data typically results in degraded performance on past data. Taking a step towards efficient continual pre-training, in this work, we examine the effect of different warm-up strategies. Our hypothesis is that the learning rate must be re-increased to improve compute efficiency when training on a new dataset. We study the warmup phase of models pre-trained on the Pile (upstream data, 300B tokens) as we continue to pre-train on SlimPajama (downstream data, 297B tokens), following a linear warmup and cosine decay schedule. We conduct all experiments on the Pythia 410M language model architecture and evaluate performance through validation perplexity. We experiment with different pre-training checkpoints, various maximum learning rates, and various warmup lengths. Our results show that while rewarming models first increases the loss on upstream and downstream data, in the longer run it improves the downstream performance, outperforming models trained from scratch$\unicode{x2013}$even for a large downstream dataset.

## 07-003 | Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language Capabilities
- arXiv: 2404.17790  first public: 2024-04-27  latest: 2024-04-27  primary cat: cs.CL
- authors (10): Kazuki Fujii; Taishi Nakamura; Mengsay Loem; Hiroki Iida; Masanari Ohi; Kakeru Hattori ...
- seed subtopic: 向新语言持续预训练; type: 原始研究; cross: ['06']
- URLs on first pages of PDF: https://commoncrawl.github.io/cc-crawl-statistics
- pages: 23

ABSTRACT: Cross-lingual continual pre-training of large language models (LLMs) initially trained on English corpus allows us to leverage the vast amount of English language resources and reduce the pre-training cost. In this study, we constructed Swallow, an LLM with enhanced Japanese capability, by extending the vocabulary of Llama 2 to include Japanese characters and conducting continual pre-training on a large Japanese web corpus. Experimental results confirmed that the performance on Japanese tasks drastically improved through continual pre-training, and the performance monotonically increased with the amount of training data up to 100B tokens. Consequently, Swallow achieved superior performance compared to other LLMs that were trained from scratch in English and Japanese. An analysis of the effects of continual pre-training revealed that it was particularly effective for Japanese question answering tasks. Furthermore, to elucidate effective methodologies for cross-lingual continual pre-training from English to Japanese, we investigated the impact of vocabulary expansion and the effectiveness of incorporating parallel corpora. The results showed that the efficiency gained through vocabulary expansion had no negative impact on performance, except for the summarization task, and that the combined use of parallel corpora enhanced translation ability.

## 07-004 | LLaMA Beyond English: An Empirical Study on Language Capability Transfer
- arXiv: 2401.01055  first public: 2024-01-02  latest: 2024-01-12  primary cat: cs.CL
- authors (6): Jun Zhao; Zhihao Zhang; Luhui Gao; Qi Zhang; Tao Gui; Xuanjing Huang
- seed subtopic: 向新语言持续预训练; type: 原始研究; cross: ['08']
- pages: 10

ABSTRACT: In recent times, substantial advancements have been witnessed in large language models (LLMs), exemplified by ChatGPT, showcasing remarkable proficiency across a range of complex tasks. However, many mainstream LLMs (e.g. LLaMA) are pretrained on English-dominant corpus, which limits their performance in other non-English languages. In this paper, we focus on how to effectively transfer the capabilities of language generation and following instructions to a non-English language. To answer this question, we conduct an extensive empirical investigation based on LLaMA, accumulating over 1440 GPU hours. We analyze the impact of key factors such as vocabulary extension, further pretraining, and instruction tuning on transfer. To accurately assess the model's level of knowledge, we employ four widely used standardized testing benchmarks: C-Eval, MMLU, AGI-Eval, and GAOKAO-Bench. Furthermore, a comprehensive evaluation of the model's response quality is conducted, considering aspects such as accuracy, fluency, informativeness, logical coherence, and harmlessness, based on LLM-Eval, a benchmarks consisting instruction tasks from 17 diverse categories. Our evaluation results demonstrate that comparable performance to state-of-the-art transfer models can be achieved with less than 1% of the pretraining data, both in terms of knowledge alignment and response quality. Furthermore, the experimental outcomes across the thirteen low-resource languages also exhibit similar trends. We anticipate that the conclusions revealed by the experiments will aid the community in developing non-English LLMs.

## 07-005 | Efficiently Adapting Pretrained Language Models To New Languages
- arXiv: 2311.05741  first public: 2023-11-09  latest: 2023-12-14  primary cat: cs.CL
- authors (4): Zoltan Csaki; Pian Pawakapan; Urmish Thakker; Qiantong Xu
- seed subtopic: 向新语言持续预训练; type: 原始研究; cross: ['06']
- arXiv comment: Accepted to "The third Neurips Workshop on Efficient Natural Language and Speech Processing 2023" (ENLSP-III)
- pages: 13

ABSTRACT: Recent large language models (LLM) exhibit sub-optimal performance on low-resource languages, as the training data of these models is usually dominated by English and other high-resource languages. Furthermore, it is challenging to train models for low-resource languages, especially from scratch, due to a lack of high quality training data. Adapting pretrained LLMs reduces the need for data in the new language while also providing cross lingual transfer capabilities. However, naively adapting to new languages leads to catastrophic forgetting and poor tokenizer efficiency. In this work, we study how to efficiently adapt any existing pretrained LLM to a new language without running into these issues. In particular, we improve the encoding efficiency of the tokenizer by adding new tokens from the target language and study the data mixing recipe to mitigate forgetting. Our experiments on adapting an English LLM to Hungarian and Thai show that our recipe can reach better performance than open source models on the target language, with minimal regressions on English.

## 07-006 | Mitigating Catastrophic Forgetting in Language Transfer via Model Merging
- arXiv: 2407.08699  first public: 2024-07-11  latest: 2024-07-16  primary cat: cs.LG
- authors (6): Anton Alexandrov; Veselin Raychev; Mark Niklas Müller; Ce Zhang; Martin Vechev; Kristina Toutanova
- seed subtopic: 遗忘缓解与模型合并; type: 原始研究; cross: []
- pages: 20

ABSTRACT: As open-weight large language models (LLMs) achieve ever more impressive performances across a wide range of tasks in English, practitioners aim to adapt these models to different languages. However, such language adaptation is often accompanied by catastrophic forgetting of the base model's capabilities, severely limiting the usefulness of the resulting model. We address this issue by proposing Branch-and-Merge (BaM), a new adaptation method based on iteratively merging multiple models, fine-tuned on a subset of the available training data. BaM is based on the insight that this yields lower magnitude but higher quality weight changes, reducing forgetting of the source domain while maintaining learning on the target domain. We demonstrate in an extensive empirical study on Bulgarian and German that BaM can significantly reduce forgetting while matching or even improving target domain performance compared to both standard continued pretraining and instruction finetuning across different model architectures.

## 07-007 | Unlocking the Potential of Model Merging for Low-Resource Languages
- arXiv: 2407.03994  first public: 2024-07-04  latest: 2024-10-06  primary cat: cs.CL
- authors (7): Mingxu Tao; Chen Zhang; Quzhe Huang; Tianyao Ma; Songfang Huang; Dongyan Zhao ...
- seed subtopic: 模型合并; type: 原始研究; cross: ['08']
- arXiv comment: To appear in EMNLP2024 Findings
- doi: 10.18653/v1/2024.findings-emnlp.508
- pages: 16

ABSTRACT: Adapting large language models (LLMs) to new languages typically involves continual pre-training (CT) followed by supervised fine-tuning (SFT). However, this CT-then-SFT approach struggles with limited data in the context of low-resource languages, failing to balance language modeling and task-solving capabilities. We thus propose model merging as an alternative for low-resource languages, combining models with distinct capabilities into a single model without additional training. We use model merging to develop task-solving LLMs for low-resource languages without SFT data in the target languages. Our experiments based on Llama-2-7B demonstrate that model merging effectively endows LLMs for low-resource languages with task-solving abilities, outperforming CT-then-SFT in scenarios with extremely scarce data. Observing performance saturation in model merging with more training tokens, we further analyze the merging process and introduce a slack variable to the model merging algorithm to mitigate the loss of important parameters, thereby enhancing performance. We hope that model merging can benefit more human languages suffering from data scarcity with its higher data efficiency.

## 07-009 | Massively Multilingual Adaptation of Large Language Models Using Bilingual Translation Data
- arXiv: 2506.00469  first public: 2025-05-31  latest: 2025-12-04  primary cat: cs.CL
- authors (5): Shaoxiong Ji; Zihao Li; Jaakko Paavola; Hengyu Luo; Jörg Tiedemann
- seed subtopic: 双语数据持续预训练; type: 原始研究; cross: ['09']
- arXiv comment: EMMA-500 Gen 2; refer to Gen 1 in arXiv:2409.17892
- URLs on first pages of PDF: https://github.com/Helsinki-NLP/OPUS
- pages: 39

ABSTRACT: This paper investigates a critical design decision in the practice of massively multilingual continual pre-training -- the inclusion of parallel data. Specifically, we study the impact of bilingual translation data for massively multilingual language adaptation of the Llama3 family of models to 500 languages. To this end, we construct the MaLA bilingual translation corpus, containing data from more than 2,500 language pairs. Subsequently, we develop the EMMA-500 Llama 3 suite of four massively multilingual models -- continually pre-trained from the Llama 3 family of base models extensively on diverse data mixes up to 671B tokens -- and explore the effect of continual pre-training with or without bilingual translation data. Comprehensive evaluation across 7 tasks and 12 benchmarks demonstrates that bilingual data tends to enhance language transfer and performance, particularly for low-resource languages. We open-source the MaLA corpus, EMMA-500 Llama 3 suite artefacts, code, and model generations.

## 07-010 | Targeted Multilingual Adaptation for Low-resource Language Families
- arXiv: 2405.12413  first public: 2024-05-20  latest: 2024-05-20  primary cat: cs.CL
- authors (5): C. M. Downey; Terra Blevins; Dhwani Serai; Dwija Parikh; Shane Steinert-Threlkeld
- seed subtopic: 语言族定向适配; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/CLMBRs/targeted-xlms
- pages: 19

ABSTRACT: The "massively-multilingual" training of multilingual models is known to limit their utility in any one language, and they perform particularly poorly on low-resource languages. However, there is evidence that low-resource languages can benefit from targeted multilinguality, where the model is trained on closely related languages. To test this approach more rigorously, we systematically study best practices for adapting a pre-trained model to a language family. Focusing on the Uralic family as a test case, we adapt XLM-R under various configurations to model 15 languages; we then evaluate the performance of each experimental setting on two downstream tasks and 11 evaluation languages. Our adapted models significantly outperform mono- and multilingual baselines. Furthermore, a regression analysis of hyperparameter effects reveals that adapted vocabulary size is relatively unimportant for low-resource languages, and that low-resource languages can be aggressively up-sampled during training at little detriment to performance in high-resource languages. These results introduce new best practices for performing language adaptation in a targeted setting.

## 07-013 | Code-Switching Curriculum Learning for Multilingual Transfer in LLMs
- arXiv: 2411.02460  first public: 2024-11-04  latest: 2025-06-11  primary cat: cs.CL
- authors (5): Haneul Yoo; Cheonbok Park; Sangdoo Yun; Alice Oh; Hwaran Lee
- seed subtopic: 课程学习; type: 原始研究; cross: []
- arXiv comment: To appear in Findings of ACL 2025
- pages: 21

ABSTRACT: Large language models (LLMs) now exhibit near human-level performance in various tasks, but their performance drops drastically after a handful of high-resource languages due to the imbalance in pre-training data. Inspired by the human process of second language acquisition, particularly code-switching$\unicode{x2014}$the practice of language alternation in a conversation$\unicode{x2014}$we propose code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs. CSCL mimics the stages of human language learning by progressively training models with a curriculum consisting of 1) token-level code-switching, 2) sentence-level code-switching, and 3) monolingual corpora. Using Qwen 2 as our underlying model, we demonstrate the efficacy of the CSCL in improving language transfer to Korean, achieving significant performance gains compared to monolingual continual pre-training methods. Ablation studies reveal that both token- and sentence-level code-switching significantly enhance cross-lingual transfer and that curriculum learning amplifies these effects. We also extend our findings into various languages, including Japanese (high-resource) and Indonesian (low-resource), and using two additional models (Gemma 2 and Phi 3.5). We further show that CSCL mitigates spurious correlations between language resources and safety alignment, presenting a robust, efficient framework for more equitable language transfer in LLMs. We observe that CSCL is effective for low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.

## 07-014 | Efficient Continual Pre-training of LLMs for Low-resource Languages
- arXiv: 2412.10244  first public: 2024-12-13  latest: 2024-12-13  primary cat: cs.CL
- authors (4): Arijit Nag; Soumen Chakrabarti; Animesh Mukherjee; Niloy Ganguly
- seed subtopic: 低资源持续预训练效率; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Open-source Large Language models (OsLLMs) propel the democratization of natural language research by giving the flexibility to augment or update model parameters for performance improvement. Nevertheless, like proprietary LLMs, Os-LLMs offer poorer performance on low-resource languages (LRLs) than high-resource languages (HRLs), owing to smaller amounts of training data and underrepresented vocabulary. On the other hand, continual pre-training (CPT) with large amounts of language-specific data is a costly proposition in terms of data acquisition and computational resources. Our goal is to drastically reduce CPT cost. To that end, we first develop a new algorithm to select a subset of texts from a larger corpus. We show the effectiveness of our technique using very little CPT data. In search of further improvement, we design a new algorithm to select tokens to include in the LLM vocabulary. We experiment with the recent Llama-3 model and nine Indian languages with diverse scripts and extent of resource availability. For evaluation, we use IndicGenBench, a generation task benchmark dataset for Indic languages. We experiment with various CPT corpora and augmented vocabulary size and offer insights across language families.

## 07-015 | Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus
- arXiv: 2410.14815  first public: 2024-10-18  latest: 2025-04-21  primary cat: cs.CL
- authors (9): Raviraj Joshi; Kanishk Singla; Anusha Kamath; Raunak Kalani; Rakesh Paul; Utkarsh Vaidya ...
- seed subtopic: 持续预训练+合成语料; type: 原始研究; cross: ['09']
- URLs on first pages of PDF: https://github.com/AI4Bharat/IndicInstruct https://github.com/NVIDIA/NeMo-Curator https://huggingface.co/Telugu-LLM-Labs/Indic-gemma- https://huggingface.co/nvidia/
- pages: 8

ABSTRACT: Multilingual LLMs support a variety of languages; however, their performance is suboptimal for low-resource languages. In this work, we emphasize the importance of continued pre-training of multilingual LLMs and the use of translation-based synthetic pre-training corpora for improving LLMs in low-resource languages. We conduct our study in the context of the low-resource Indic language Hindi. We introduce Nemotron-Mini-Hindi 4B, a bilingual SLM supporting both Hindi and English, based on Nemotron-Mini 4B. The model is trained using a mix of real and synthetic Hindi + English tokens, with continuous pre-training performed on 400B tokens. We demonstrate that both the base and instruct models achieve state-of-the-art results on Hindi benchmarks while remaining competitive on English tasks. Additionally, we observe that the continued pre-training approach enhances the model's overall factual accuracy. We perform an ablation study to highlight the impact of Hindi pre-training, showing significant improvements in Hindi chat capabilities and factual accuracy, which cannot be achieved through Hindi alignment alone.

## 07-016 | Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation
- arXiv: 2506.00288  first public: 2025-05-30  latest: 2025-09-19  primary cat: cs.CL
- authors (3): Ahmed Elhady; Eneko Agirre; Mikel Artetxe
- seed subtopic: 持续预训练中的英语数据作用; type: 原始研究; cross: []
- arXiv comment: Published as a Conference Paper at the main track of ACL 2025
- pages: 14

ABSTRACT: Continued pretraining (CPT) is a popular approach to adapt existing large language models (LLMs) to new languages. When doing so, it is common practice to include a portion of English data in the mixture, but its role has not been carefully studied to date. In this work, we show that including English does not impact validation perplexity, yet it is critical for the emergence of downstream capabilities in the target language. We introduce a language-agnostic benchmark for in-context learning (ICL), which reveals catastrophic forgetting early on CPT when English is not included. This in turn damages the ability of the model to generalize to downstream prompts in the target language as measured by perplexity, even if it does not manifest in terms of accuracy until later in training, and can be tied to a big shift in the model parameters. Based on these insights, we introduce curriculum learning and exponential moving average (EMA) of weights as effective alternatives to mitigate the need for English. All in all, our work sheds light into the dynamics by which emergent abilities arise when doing CPT for language adaptation, and can serve as a foundation to design more effective methods in the future.

## 07-017 | Continually Adding New Languages to Multilingual Language Models
- arXiv: 2509.11414  first public: 2025-09-14  latest: 2025-09-14  primary cat: cs.CL
- authors (2): Abraham Toluwase Owodunni; Sachin Kumar
- seed subtopic: 持续增加新语言; type: 原始研究; cross: []
- pages: 22

ABSTRACT: Multilingual language models are trained on a fixed set of languages, and to support new languages, the models need to be retrained from scratch. This is an expensive endeavor and is often infeasible, as model developers tend not to release their pre-training data. Naive approaches, such as continued pretraining, suffer from catastrophic forgetting; however, mitigation strategies like experience replay cannot be applied due to the lack of original pretraining data. In this work, we investigate the problem of continually adding new languages to a multilingual model, assuming access to pretraining data in only the target languages. We explore multiple approaches to address this problem and propose Layer-Selective LoRA (LayRA), which adds Low-Rank Adapters (LoRA) to selected initial and final layers while keeping the rest of the model frozen. LayRA builds on two insights: (1) LoRA reduces forgetting, and (2) multilingual models encode inputs in the source language in the initial layers, reason in English in intermediate layers, and translate back to the source language in final layers. We experiment with adding multiple combinations of Galician, Swahili, and Urdu to pretrained language models and evaluate each method on diverse multilingual tasks. We find that LayRA provides the overall best tradeoff between preserving models' capabilities in previously supported languages, while being competitive with existing approaches such as LoRA in learning new languages. We also demonstrate that using model arithmetic, the adapted models can be equipped with strong instruction following abilities without access to any instruction tuning data in the target languages.

## 07-018 | Breaking Language Barriers: Cross-Lingual Continual Pre-Training at Scale
- arXiv: 2407.02118  first public: 2024-07-02  latest: 2024-10-02  primary cat: cs.CL
- authors (6): Wenzhen Zheng; Wenbo Pan; Xu Xu; Libo Qin; Li Yue; Ming Zhou
- seed subtopic: 跨语言持续预训练规模律; type: 原始研究; cross: []
- arXiv comment: 8 pages. Accepted at EMNLP 2024
- pages: 14

ABSTRACT: In recent years, Large Language Models (LLMs) have made significant strides towards Artificial General Intelligence. However, training these models from scratch requires substantial computational resources and vast amounts of text data. In this paper, we explore an alternative approach to constructing an LLM for a new language by continually pretraining (CPT) from existing pretrained LLMs, instead of using randomly initialized parameters. Based on parallel experiments on 40 model sizes ranging from 40M to 5B parameters, we find that 1) CPT converges faster and saves significant resources in a scalable manner; 2) CPT adheres to an extended scaling law derived from Hoffmann et al. (2022) with a joint data-parameter scaling term; 3) The compute-optimal data-parameter allocation for CPT markedly differs based on our estimated scaling factors; 4) The effectiveness of transfer at scale is influenced by training duration and linguistic properties, while robust to data replaying, a method that effectively mitigates catastrophic forgetting in CPT. We hope our findings provide deeper insights into the transferability of LLMs at scale for the research community.

## 07-019 | AfriqueLLM: How Data Mixing and Model Architecture Impact Continued Pre-training for African Languages
- arXiv: 2601.06395  first public: 2026-01-10  latest: 2026-06-23  primary cat: cs.CL
- authors (6): Hao Yu; Tianyi Xu; Michael A. Hedderich; Wassim Hamidouche; Syed Waqas Zamir; David Ifeoluwa Adelani
- seed subtopic: 数据混合（非洲语言）; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2026 (Main Conference)
- pages: 21

ABSTRACT: Large language models (LLMs) are increasingly multilingual, yet open models continue to underperform relative to proprietary systems, with the gap most pronounced for African languages. Continued pre-training (CPT) offers a practical route to language adaptation, but improvements on demanding capabilities such as mathematical reasoning often remain limited. This limitation is driven in part by the uneven domain coverage and missing task-relevant knowledge that characterize many low-resource language corpora. We present \texttt{AfriqueLLM}, a suite of open LLMs adapted to 20 African languages through CPT on 26B tokens. We perform a comprehensive empirical study across five base models spanning sizes and architectures, including Llama 3.1, Gemma 3, and Qwen 3, and systematically analyze how CPT data composition shapes downstream performance. In particular, we vary mixtures that include math, code, and synthetic translated data, and evaluate the resulting models on a range of multilingual benchmarks. Our results identify data composition as the primary driver of CPT gains. Adding math, code, and synthetic translated data yields consistent improvements, including on reasoning-oriented evaluations. Within a fixed architecture, larger models typically improve performance, but architectural choices dominate scale when comparing across model families. Moreover, strong multilingual performance in the base model does not reliably predict post-CPT outcomes; robust architectures coupled with task-aligned data provide a more dependable recipe. Finally, our best models improve long-context performance, including document-level translation. Models and code have been released on [Huggingface](https://huggingface.co/collections/McGill-NLP/afriquellm) and [Github](https://github.com/McGill-NLP/AfriqueLLM).

## 07-022 | Small Languages, Big Models: A Study of Continual Training on Languages of Norway
- arXiv: 2412.06484  first public: 2024-12-09  latest: 2025-02-02  primary cat: cs.CL
- authors (7): David Samuel; Vladislav Mikhailov; Erik Velldal; Lilja Øvrelid; Lucas Georges Gabriel Charpentier; Andrey Kutuzov ...
- seed subtopic: 挪威语/萨米语持续训练; type: 原始研究; cross: []
- arXiv comment: Published at NoDaLiDa 2025
- journal_ref: Proceedings of the 25th Nordic Conference on Computational Linguistics (NoDaLiDa 2025). Tallinn, Estonia
- pages: 36

ABSTRACT: Training large language models requires vast amounts of data, posing a challenge for less widely spoken languages like Norwegian and even more so for truly low-resource languages like Northern Sámi. To address this issue, we present a novel three-stage continual training approach that substantially improves the downstream performance together with the inference efficiency for the target languages. Based on our findings, we train, evaluate, and openly release a new generative language model for Norwegian Bokmål, Nynorsk, and Northern Sámi with 11.4 billion parameters: NorMistral-11B.

## 07-023 | SnakModel: Lessons Learned from Training an Open Danish Large Language Model
- arXiv: 2412.12956  first public: 2024-12-17  latest: 2024-12-17  primary cat: cs.CL
- authors (4): Mike Zhang; Max Müller-Eberstein; Elisa Bassignana; Rob van der Goot
- seed subtopic: 丹麦语适配经验; type: 原始研究; cross: []
- arXiv comment: Accepted at NoDaLiDa 2025 (oral)
- URLs on first pages of PDF: https://github.com/nlpnorth/snakmodel/
- pages: 14

ABSTRACT: We present SnakModel, a Danish large language model (LLM) based on Llama2-7B, which we continuously pre-train on 13.6B Danish words, and further tune on 3.7M Danish instructions. As best practices for creating LLMs for smaller language communities have yet to be established, we examine the effects of early modeling and training decisions on downstream performance throughout the entire training pipeline, including (1) the creation of a strictly curated corpus of Danish text from diverse sources; (2) the language modeling and instruction-tuning training process itself, including the analysis of intermediate training dynamics, and ablations across different hyperparameters; (3) an evaluation on eight language and culturally-specific tasks. Across these experiments SnakModel achieves the highest overall performance, outperforming multiple contemporary Llama2-7B-based models. By making SnakModel, the majority of our pre-training corpus, and the associated code available under open licenses, we hope to foster further research and development in Danish Natural Language Processing, and establish training guidelines for languages with similar resource constraints.

## 07-024 | ChocoLlama: Lessons Learned From Teaching Llamas Dutch
- arXiv: 2412.07633  first public: 2024-12-10  latest: 2024-12-10  primary cat: cs.CL
- authors (6): Matthieu Meeus; Anthony Rathé; François Remy; Pieter Delobelle; Jens-Joris Decorte; Thomas Demeester
- seed subtopic: 荷兰语适配经验; type: 原始研究; cross: ['08']
- URLs on first pages of PDF: https://github.com/ChocoLlamaModel/ChocoLlama https://huggingface.co/ChocoLlama
- pages: 18

ABSTRACT: While Large Language Models (LLMs) have shown remarkable capabilities in natural language understanding and generation, their performance often lags in lower-resource, non-English languages due to biases in the training data. In this work, we explore strategies for adapting the primarily English LLMs (Llama-2 and Llama-3) to Dutch, a language spoken by 30 million people worldwide yet often underrepresented in LLM development. We collect 104GB of Dutch text ($32$B tokens) from various sources to first apply continued pretraining using low-rank adaptation (LoRA), complemented with Dutch posttraining strategies provided by prior work. For Llama-2, we consider using (i) the tokenizer of the original model, and (ii) training a new, Dutch-specific tokenizer combined with embedding reinitialization. We evaluate our adapted models, ChocoLlama-2, both on standard benchmarks and a novel Dutch benchmark, ChocoLlama-Bench. Our results demonstrate that LoRA can effectively scale for language adaptation, and that tokenizer modification with careful weight reinitialization can improve performance. Notably, Llama-3 was released during the course of this project and, upon evaluation, demonstrated superior Dutch capabilities compared to our Dutch-adapted versions of Llama-2. We hence apply the same adaptation technique to Llama-3, using its original tokenizer. While our adaptation methods enhanced Llama-2's Dutch capabilities, we found limited gains when applying the same techniques to Llama-3. This suggests that for ever improving, multilingual foundation models, language adaptation techniques may benefit more from focusing on language-specific posttraining rather than on continued pretraining. We hope this work contributes to the broader understanding of adapting LLMs to lower-resource languages, and to the development of Dutch LLMs in particular.

## 07-026 | FinGPT: Large Generative Models for a Small Language
- arXiv: 2311.05640  first public: 2023-11-03  latest: 2023-11-03  primary cat: cs.CL
- authors (21): Risto Luukkonen; Ville Komulainen; Jouni Luoma; Anni Eskelinen; Jenna Kanerva; Hanna-Mari Kupari ...
- seed subtopic: 小语种从零预训练; type: 原始研究; cross: []
- arXiv comment: 17 pages (10 main), 7 figures, 5 tables
- URLs on first pages of PDF: https://github.com/TurkuNLP/CC-Fi https://github.com/google/cld3 https://github.com/miso-belica/jusText https://huggingface.co/Finnish-NLP https://huggingface.co/bigscience-data https://huggingface.co/datasets/mc4
- pages: 17

ABSTRACT: Large language models (LLMs) excel in many tasks in NLP and beyond, but most open models have very limited coverage of smaller languages and LLM work tends to focus on languages where nearly unlimited data is available for pretraining. In this work, we study the challenges of creating LLMs for Finnish, a language spoken by less than 0.1% of the world population. We compile an extensive dataset of Finnish combining web crawls, news, social media and eBooks. We pursue two approaches to pretrain models: 1) we train seven monolingual models from scratch (186M to 13B parameters) dubbed FinGPT, 2) we continue the pretraining of the multilingual BLOOM model on a mix of its original training data and Finnish, resulting in a 176 billion parameter model we call BLUUMI. For model evaluation, we introduce FIN-bench, a version of BIG-bench with Finnish tasks. We also assess other model qualities such as toxicity and bias. Our models and tools are openly available at https://turkunlp.org/gpt3-finnish.

## 07-029 | Bilingual Adaptation of Monolingual Foundation Models
- arXiv: 2407.12869  first public: 2024-07-13  latest: 2024-07-25  primary cat: cs.CL
- authors (22): Gurpreet Gosal; Yishi Xu; Gokul Ramakrishnan; Rituraj Joshi; Avraham Sheinin; Zhiming ...
- seed subtopic: 双语持续预训练（阿拉伯语）; type: 原始研究; cross: []
- pages: 12

ABSTRACT: We present an efficient method for adapting a monolingual Large Language Model (LLM) to another language, addressing challenges of catastrophic forgetting and tokenizer limitations. We focus this study on adapting Llama 2 to Arabic. Our two-stage approach begins with expanding the vocabulary and training only the embeddings matrix, followed by full model continual pre-training on a bilingual corpus. By continually pre-training on a mix of Arabic and English corpora, the model retains its proficiency in English while acquiring capabilities in Arabic. Our approach results in significant improvements in Arabic and slight enhancements in English, demonstrating cost-effective cross-lingual transfer. We perform ablations on embedding initialization techniques, data mix ratios, and learning rates and release a detailed training recipe. To demonstrate generalizability of this approach we also adapted Llama 3 8B to Arabic and Llama 2 13B to Hindi.

## 07-030 | Rethinking LLM Language Adaptation: A Case Study on Chinese Mixtral
- arXiv: 2403.01851  first public: 2024-03-04  latest: 2024-03-04  primary cat: cs.CL
- authors (2): Yiming Cui; Xin Yao
- seed subtopic: 语言适配（MoE）; type: 原始研究; cross: []
- arXiv comment: 13 pages
- URLs on first pages of PDF: https://github.com/huggingface/peft https://github.com/huggingface/transformers https://github.com/huggingface/transformers/blob/main/src/ https://github.com/ymcui/Chinese-Mixtral
- pages: 13

ABSTRACT: Mixtral, a representative sparse mixture of experts (SMoE) language model, has received significant attention due to its unique model design and superior performance. Based on Mixtral-8x7B-v0.1, in this paper, we propose Chinese-Mixtral and Chinese-Mixtral-Instruct with improved Chinese language abilities by adopting further pre-training and instruction fine-tuning. Experimental results show that our Chinese-Mixtral and Chinese-Mixtral-Instruct successfully improve Chinese understanding and generation performance while retaining the original English abilities. Then, we discuss several key questions when performing language adaptation on large language models, including the necessity of extending the language-specific vocabulary and the choice of the initialization model (foundation model v.s. instruction model), by providing empirical results and analysis. We also present the visualizations of each expert to examine their importance on downstream tasks. Our resources are publicly available through \url{https://github.com/ymcui/Chinese-Mixtral}.

## 07-031 | Aurora-M: Open Source Continual Pre-training for Multilingual Language and Code
- arXiv: 2404.00399  first public: 2024-03-30  latest: 2024-12-27  primary cat: cs.CL
- authors (45): Taishi Nakamura; Mayank Mishra; Simone Tedeschi; Yekun Chai; Jason T Stillerman; Felix Friedrich ...
- seed subtopic: 多语+代码持续预训练; type: 原始研究; cross: ['14']
- arXiv comment: Preprint
- pages: 23

ABSTRACT: Pretrained language models are an integral part of AI applications, but their high computational cost for training limits accessibility. Initiatives such as Bloom and StarCoder aim to democratize access to pretrained models for collaborative community development. Despite these efforts, such models encounter challenges such as limited multilingual capabilities, risks of catastrophic forgetting during continual pretraining, and the high costs of training models from scratch, alongside the need to align with AI safety standards and regulatory frameworks. This paper presents Aurora-M, a 15B parameter multilingual open-source model trained on English, Finnish, Hindi, Japanese, Vietnamese, and code. Continually pretrained from StarCoderPlus on 435B additional tokens, Aurora-M surpasses 2T tokens in total training token count. It is the first open-source multilingual model fine-tuned on human-reviewed safety instructions, thus aligning its development not only with conventional red-teaming considerations, but also with the specific concerns articulated in the Biden-Harris Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence. We evaluate Aurora-M across a wide range of tasks and languages, showcasing its robustness against catastrophic forgetting and its superior performance in multilingual settings, particularly in safety evaluations. We open-source Aurora-M and its variants to encourage responsible open-source development of large language models at https://huggingface.co/aurora-m.

## 07-032 | Investigating Continual Pretraining in Large Language Models: Insights and Implications
- arXiv: 2402.17400  first public: 2024-02-27  latest: 2025-02-12  primary cat: cs.CL
- authors (5): Çağatay Yıldız; Nishaanth Kanna Ravichandran; Nitin Sharma; Matthias Bethge; Beyza Ermis
- seed subtopic: 持续预训练基准; type: 原始研究; cross: []
- pages: 23

ABSTRACT: Continual learning (CL) in large language models (LLMs) is an evolving domain that focuses on developing efficient and sustainable training strategies to adapt models to emerging knowledge and achieve robustness in dynamic environments. Our primary emphasis is on continual domain-adaptive pretraining, a process designed to equip LLMs with the ability to integrate new information from various domains while retaining previously learned knowledge. Since existing works concentrate mostly on continual fine-tuning for a limited selection of downstream tasks or training domains, we introduce a new benchmark designed to measure the adaptability of LLMs to changing pretraining data landscapes. We further examine the impact of model size on learning efficacy and forgetting, as well as how the progression and similarity of emerging domains affect the knowledge transfer within these models. Our findings uncover several key insights: (i) continual pretraining consistently improves <1.5B models studied in this work and is also superior to domain adaptation, (ii) larger models always achieve better perplexity than smaller ones when continually pretrained on the same corpus, (iii) smaller models are particularly sensitive to continual pretraining, showing the most significant rates of both learning and forgetting, (iv) continual pretraining boosts downstream task performance of GPT-2 family, (v) continual pretraining enables LLMs to specialize better when the sequence of domains shows semantic similarity while randomizing training domains leads to better transfer and final performance otherwise. We posit that our research establishes a new benchmark for CL in LLMs, providing a more realistic evaluation of knowledge retention and transfer across diverse domains.

## 07-033 | Examining Forgetting in Continual Pre-training of Aligned Large Language Models
- arXiv: 2401.03129  first public: 2024-01-06  latest: 2024-01-06  primary cat: cs.CL
- authors (2): Chen-An Li; Hung-Yi Lee
- seed subtopic: 对齐模型持续预训练遗忘; type: 原始研究; cross: ['10']
- arXiv comment: Work in progress
- pages: 10

ABSTRACT: Recent advances in Large Language Models (LLMs) have exhibited remarkable proficiency across various tasks. Given the potent applications of LLMs in numerous fields, there has been a surge in LLM development. In developing LLMs, a common practice involves continual pre-training on previously fine-tuned models. However, this can lead to catastrophic forgetting. In our work, we investigate the phenomenon of forgetting that occurs during continual pre-training on an existing fine-tuned LLM. We evaluate the impact of continuous pre-training on the fine-tuned LLM across various dimensions, including output format, knowledge, and reliability. Experiment results highlight the non-trivial challenge of addressing catastrophic forgetting during continual pre-training, especially the repetition issue.

## 07-034 | Continual Learning for Large Language Models: A Survey
- arXiv: 2402.01364  first public: 2024-02-02  latest: 2024-02-07  primary cat: cs.CL
- authors (6): Tongtong Wu; Linhao Luo; Yuan-Fang Li; Shirui Pan; Thuy-Trang Vu; Gholamreza Haffari
- seed subtopic: 持续学习综述; type: 综述; cross: []
- pages: 9

ABSTRACT: Large language models (LLMs) are not amenable to frequent re-training, due to high training costs arising from their massive scale. However, updates are necessary to endow LLMs with new skills and keep them up-to-date with rapidly evolving human knowledge. This paper surveys recent works on continual learning for LLMs. Due to the unique nature of LLMs, we catalog continue learning techniques in a novel multi-staged categorization scheme, involving continual pretraining, instruction tuning, and alignment. We contrast continual learning for LLMs with simpler adaptation methods used in smaller models, as well as with other enhancement strategies like retrieval-augmented generation and model editing. Moreover, informed by a discussion of benchmarks and evaluation, we identify several challenges and future work directions for this crucial task.

## 07-036 | CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models
- arXiv: 2407.17467  first public: 2024-07-24  latest: 2024-10-07  primary cat: cs.CL
- authors (5): Jiawei Gu; Zacc Yang; Chuanghao Ding; Rui Zhao; Fei Tan
- seed subtopic: 重放/混合比例规模律; type: 原始研究; cross: []
- arXiv comment: EMNLP 2024 main conference
- pages: 20

ABSTRACT: Large Language Models (LLMs) excel in diverse tasks but often underperform in specialized fields due to limited domain-specific or proprietary corpus. Continual pre-training (CPT) enhances LLM capabilities by imbuing new domain-specific or proprietary knowledge while replaying general corpus to prevent catastrophic forgetting. The data mixture ratio of general corpus and domain-specific corpus, however, has been chosen heuristically, leading to sub-optimal training efficiency in practice. In this context, we attempt to re-visit the scaling behavior of LLMs under the hood of CPT, and discover a power-law relationship between loss, mixture ratio, and training tokens scale. We formalize the trade-off between general and domain-specific capabilities, leading to a well-defined Critical Mixture Ratio (CMR) of general and domain data. By striking the balance, CMR maintains the model's general ability and achieves the desired domain transfer, ensuring the highest utilization of available resources. Considering the balance between efficiency and effectiveness, CMR can be regarded as the optimal mixture ratio. Through extensive experiments, we ascertain the predictability of CMR, propose CMR scaling law and have substantiated its generalization. These findings offer practical guidelines for optimizing LLM training in specialized domains, ensuring both general and domain-specific performance while efficiently managing training resources.

## 07-037 | Efficient Continual Pre-training by Mitigating the Stability Gap
- arXiv: 2406.14833  first public: 2024-06-21  latest: 2024-06-27  primary cat: cs.CL
- authors (5): Yiduo Guo; Jie Fu; Huishuai Zhang; Dongyan Zhao; Yikang Shen
- seed subtopic: 训练稳定性; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/YiDuo1999/
- pages: 28

ABSTRACT: Continual pre-training has increasingly become the predominant approach for adapting Large Language Models (LLMs) to new domains. This process involves updating the pre-trained LLM with a corpus from a new domain, resulting in a shift in the training distribution. To study the behavior of LLMs during this shift, we measured the model's performance throughout the continual pre-training process. we observed a temporary performance drop at the beginning, followed by a recovery phase, a phenomenon known as the "stability gap," previously noted in vision models classifying new classes. To address this issue and enhance LLM performance within a fixed compute budget, we propose three effective strategies: (1) Continually pre-training the LLM on a subset with a proper size for multiple epochs, resulting in faster performance recovery than pre-training the LLM on a large corpus in a single epoch; (2) Pre-training the LLM only on high-quality sub-corpus, which rapidly boosts domain performance; and (3) Using a data mixture similar to the pre-training data to reduce distribution gap. We conduct various experiments on Llama-family models to validate the effectiveness of our strategies in both medical continual pre-training and instruction tuning. For example, our strategies improve the average medical task performance of the OpenLlama-3B model from 36.2% to 40.7% with only 40% of the original training budget and enhance the average general task performance without causing forgetting. Furthermore, we apply our strategies to the Llama-3-8B model. The resulting model, Llama-3-Physician, achieves the best medical performance among current open-source models, and performs comparably to or even better than GPT-4 on several medical benchmarks. We release our models at \url{https://huggingface.co/YiDuo1999/Llama-3-Physician-8B-Instruct}.

## 07-038 | Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models
- arXiv: 2407.07263  first public: 2024-07-09  latest: 2024-07-09  primary cat: cs.CL
- authors (5): Jupinder Parmar; Sanjev Satheesh; Mostofa Patwary; Mohammad Shoeybi; Bryan Catanzaro
- seed subtopic: 持续预训练配方; type: 原始研究; cross: []
- arXiv comment: Preprint. Under review
- pages: 15

ABSTRACT: As language models have scaled both their number of parameters and pretraining dataset sizes, the computational cost for pretraining has become intractable except for the most well-resourced teams. This increasing cost makes it ever more important to be able to reuse a model after it has completed pretraining; allowing for a model's abilities to further improve without needing to train from scratch. In this work, we detail a set of guidelines that cover how to design efficacious data distributions and learning rate schedules for continued pretraining of language models. When applying these findings within a continued pretraining run on top of a well-trained 15B parameter model, we show an improvement of 9\% in average model accuracy compared to the baseline of continued training on the pretraining set. The resulting recipe provides a practical starting point with which to begin developing language models through reuse rather than retraining.

## 07-040 | Revisiting Multilingual Data Mixtures in Language Model Pretraining
- arXiv: 2510.25947  first public: 2025-10-29  latest: 2025-10-29  primary cat: cs.CL
- authors (4): Negar Foroutan; Paul Teiletche; Ayush Kumar Tarun; Antoine Bosselut
- seed subtopic: 多语数据混合; type: 原始研究; cross: []
- arXiv comment: Under Review
- URLs on first pages of PDF: https://huggingface.co/datasets/allenai/c4 https://huggingface.co/mistralai/Mistral-Nemo-Base-2407
- pages: 29

ABSTRACT: The impact of different multilingual data mixtures in pretraining large language models (LLMs) has been a topic of ongoing debate, often raising concerns about potential trade-offs between language coverage and model performance (i.e., the curse of multilinguality). In this work, we investigate these assumptions by training 1.1B and 3B parameter LLMs on diverse multilingual corpora, varying the number of languages from 25 to 400. Our study challenges common beliefs surrounding multilingual training. First, we find that combining English and multilingual data does not necessarily degrade the in-language performance of either group, provided that languages have a sufficient number of tokens included in the pretraining corpus. Second, we observe that using English as a pivot language (i.e., a high-resource language that serves as a catalyst for multilingual generalization) yields benefits across language families, and contrary to expectations, selecting a pivot language from within a specific family does not consistently improve performance for languages within that family. Lastly, we do not observe a significant "curse of multilinguality" as the number of training languages increases in models at this scale. Our findings suggest that multilingual data, when balanced appropriately, can enhance language model capabilities without compromising performance, even in low-resource settings

## 07-041 | XDoGE: Multilingual Data Reweighting to Enhance Language Inclusivity in LLMs
- arXiv: 2512.10545  first public: 2025-12-11  latest: 2025-12-11  primary cat: cs.CL
- authors (5): Iñaki Lacunza; José Javier Saiz; Alexander Shvets; Aitor Gonzalez-Agirre; Marta Villegas
- seed subtopic: 数据重加权; type: 原始研究; cross: []
- arXiv comment: Accepted and presented at the LLMs4All workshop at the IEEE BigData 2025 Conference, Macau - December 8-11, 2025
- URLs on first pages of PDF: https://huggingface.co/datasets/ https://huggingface.co/langtech-languagemodeling/
- pages: 10

ABSTRACT: Current large language models (LLMs) are trained on massive amounts of text data, primarily from a few dominant languages. Studies suggest that this over-reliance on high-resource languages, such as English, hampers LLM performance in mid- and low-resource languages. To mitigate this problem, we propose to (i) optimize the language distribution by training a small proxy model within a domain-reweighing DoGE algorithm that we extend to XDoGE for a multilingual setup, and (ii) rescale the data and train a full-size model with the established language weights either from scratch or within a continual pre-training phase (CPT). We target six languages possessing a variety of geographic and intra- and inter-language-family relations, namely, English and Spanish (high-resource), Portuguese and Catalan (mid-resource), Galician and Basque (low-resource). We experiment with Salamandra-2b, which is a promising model for these languages. We investigate the effects of substantial data repetition on minor languages and under-sampling on dominant languages using the IberoBench framework for quantitative evaluation. Finally, we release a new promising IberianLLM-7B-Instruct model centering on Iberian languages and English that we pretrained from scratch and further improved using CPT with the XDoGE weights.

## 07-044 | MoE-LPR: Multilingual Extension of Large Language Models through Mixture-of-Experts with Language Priors Routing
- arXiv: 2408.11396  first public: 2024-08-21  latest: 2024-08-21  primary cat: cs.CL
- authors (9): Hao Zhou; Zhijun Wang; Shujian Huang; Xin Huang; Xue Han; Junlan Feng ...
- seed subtopic: MoE 扩展与遗忘缓解; type: 原始研究; cross: ['06']
- URLs on first pages of PDF: https://github.com/zjwang21/MoE-LPR.git
- pages: 12

ABSTRACT: Large Language Models (LLMs) are often English-centric due to the disproportionate distribution of languages in their pre-training data. Enhancing non-English language capabilities through post-pretraining often results in catastrophic forgetting of the ability of original languages. Previous methods either achieve good expansion with severe forgetting or slight forgetting with poor expansion, indicating the challenge of balancing language expansion while preventing forgetting. In this paper, we propose a method called MoE-LPR (Mixture-of-Experts with Language Priors Routing) to alleviate this problem. MoE-LPR employs a two-stage training approach to enhance the multilingual capability. First, the model is post-pretrained into a Mixture-of-Experts (MoE) architecture by upcycling, where all the original parameters are frozen and new experts are added. In this stage, we focus improving the ability on expanded languages, without using any original language data. Then, the model reviews the knowledge of the original languages with replay data amounting to less than 1% of post-pretraining, where we incorporate language priors routing to better recover the abilities of the original languages. Evaluations on multiple benchmarks show that MoE-LPR outperforms other post-pretraining methods. Freezing original parameters preserves original language knowledge while adding new experts preserves the learning ability. Reviewing with LPR enables effective utilization of multilingual knowledge within the parameters. Additionally, the MoE architecture maintains the same inference overhead while increasing total model parameters. Extensive experiments demonstrate MoE-LPR's effectiveness in improving expanded languages and preserving original language proficiency with superior scalability. Code and scripts are freely available at https://github.com/zjwang21/MoE-LPR.git.

## 07-045 | Adapting Language-Specific LLMs to a Reasoning Model in One Day via Model Merging -- An Open Recipe
- arXiv: 2502.09056  first public: 2025-02-13  latest: 2025-03-27  primary cat: cs.CL
- authors (4): Kunat Pipatanakul; Pittawat Taveekitworachai; Potsawee Manakul; Kasima Tharnpipitchai
- seed subtopic: 模型合并（泰语）; type: 原始研究; cross: ['11']
- arXiv comment: 9 pages
- URLs on first pages of PDF: https://huggingface.co/collections/scb10x/
- pages: 18

ABSTRACT: This paper investigates data selection and model merging methodologies aimed at incorporating advanced reasoning capabilities such as those of DeepSeek R1 into language-specific large language models (LLMs), with a particular focus on the Thai LLM. Our goal is to enhance the reasoning capabilities of language-specific LLMs while maintaining their target language abilities. DeepSeek R1 excels in reasoning but primarily benefits high-resource languages such as English and Chinese. However, low-resource languages remain underserved due to the dominance of English-centric training data and model optimizations, which limit performance in these languages. This limitation results in unreliable code-switching and diminished effectiveness on tasks in low-resource languages. Meanwhile, local and regional LLM initiatives have attempted to bridge this gap by developing language-specific LLMs that focus on improving local linguistic fidelity. We demonstrate that, with only publicly available datasets and a computational budget of $120, it is possible to enhance the reasoning capabilities of language-specific LLMs to match the level of DeepSeek R1, without compromising their performance on target language tasks.

## 07-046 | Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models
- arXiv: 2410.01335  first public: 2024-10-02  latest: 2025-03-04  primary cat: cs.CL
- authors (7): Lucas Bandarkar; Benjamin Muller; Pritish Yuvraj; Rui Hou; Nayan Singhal; Hongjiang Lv ...
- seed subtopic: 层交换合并; type: 原始研究; cross: ['11']
- arXiv comment: ICLR 2025, Spotlight Paper, In The Thirteenth International Conference on Learning Representations, 2025
- journal_ref: The Thirteenth International Conference on Learning Representations (2025)
- pages: 24

ABSTRACT: Model merging, such as model souping, is the practice of combining different models with the same architecture together without further training. In this work, we present a model merging methodology that addresses the difficulty of fine-tuning Large Language Models (LLMs) for target tasks in non-English languages, where task-specific data is often unavailable. We focus on mathematical reasoning and without in-language math data, facilitate cross-lingual transfer by composing language and math capabilities. Starting from the same pretrained model, we fine-tune separate "experts" on math instruction data in English and on generic instruction data in the target language. We then replace the top and bottom transformer layers of the math expert directly with layers from the language expert, which consequently enhances math performance in the target language. The resulting merged models outperform the individual experts and other merging methods on the math benchmark, MGSM, by 10% across four major languages where math instruction data is scarce. In addition, this layer swapping is simple, inexpensive, and intuitive, as it is based on an interpretative analysis of the most important parameter changes during the fine-tuning of each expert. The ability to successfully re-compose LLMs for cross-lingual transfer in this manner opens up future possibilities to combine model expertise, create modular solutions, and transfer reasoning capabilities across languages all post hoc.

## 07-047 | Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese
- arXiv: 2510.00810  first public: 2025-10-01  latest: 2026-03-26  primary cat: cs.CL
- authors (3): Jenny Kunz; Iben Nyholm Debess; Annika Simonsen
- seed subtopic: 法罗语迁移与合并; type: 原始研究; cross: []
- pages: 22

ABSTRACT: We investigate strategies for adapting small, efficient language models to Faroese, a low-resource North Germanic language. Starting from English-pretrained models, we apply continued pre-training on related Scandinavian languages -- individually or combined via model merging -- before fine-tuning on Faroese. We compare full fine-tuning with parameter-efficient adaptation via LoRA, assessing their effects on general language modeling performance, linguistic accuracy, and text comprehension. To address the lack of existing Faroese evaluation resources, we construct two new minimal-pair probing benchmarks, one for linguistic acceptability and one for text comprehension, and complement them with human evaluations conducted by native Faroese linguists. Our results show that transfer from related languages is essential, but the optimal source language is task-dependent: Icelandic improves linguistic accuracy, while Danish boosts reading comprehension. The choice of adaptation method likewise depends on the target task: LoRA yields stronger linguistic acceptability and marginally higher human evaluation scores, whereas full fine-tuning produces better comprehension performance and more robust downstream fine-tuning. Merging multiple related languages under full fine-tuning (but not LoRA) improves general language modeling, though its benefits in the linguistic acceptability and comprehension probes are less consistent.

## 07-048 | Racka: Efficient Hungarian LLM Adaptation on Academic Infrastructure
- arXiv: 2601.01244  first public: 2026-01-03  latest: 2026-02-12  primary cat: cs.CL
- authors (9): Zsolt Csibi; Bence György Gortka; Natabara Gyöngyössy; Kornél Nagy; Dávid Márk Nemeskey; Martin Sallai ...
- seed subtopic: 匈牙利语低成本适配; type: 原始研究; cross: []
- arXiv comment: 22 pages, 1 figures. Appeared, and received best paper award, at the XXII. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2026)
- URLs on first pages of PDF: https://huggingface.co/elte-nlp/Racka-4B
- pages: 22

ABSTRACT: We present Racka, a lightweight, continually pretrained large language model designed to bridge the resource gap between Hungarian and high-resource languages such as English and German. Racka employs parameter-efficient continual pretraining via Low-Rank Adaptation (LoRA) on a Qwen-3 4B backbone, making the recipe practical on A100 (40GB)-based HPC clusters with low inter-node bandwidth. To better match the training distribution, we replace and adapt the tokenizer, achieving substantially improved tokenization fertility for Hungarian while maintaining competitive performance in English and German. The model is trained on 160B subword tokens drawn from a mixture of internet and high-quality curated sources, with a composition of 44% Hungarian, 24% English, 21% German, and 11% code. This data mix is chosen to mitigate catastrophic forgetting and preserve high-resource language capabilities during continual pretraining. Our preliminary results indicate modest but stable results in language adaptation.

## 07-051 | Open Llama2 Model for the Lithuanian Language
- arXiv: 2408.12963  first public: 2024-08-23  latest: 2024-08-23  primary cat: cs.CL
- authors (3): Artūras Nakvosas; Povilas Daniušis; Vytas Mulevičius
- seed subtopic: 立陶宛语持续预训练; type: 原始研究; cross: []
- arXiv comment: 12 pages, 8 figures, 5 tables
- journal_ref: Informatica, 2025
- doi: 10.15388/25-INFOR592
- URLs on first pages of PDF: https://huggingface.co/meta-llama/Llama-2-13b https://huggingface.co/meta-llama/Llama-2-7b https://huggingface.co/neurotechnology
- pages: 12

ABSTRACT: In this paper, we propose and describe the first open Llama2 large language models (LLMs) for the Lithuanian language, including an accompanying question/answer (Q/A) dataset and translations of popular LLM benchmarks. We provide a brief review of open regional LLMs and detailed information on the proposed LLMs and their training process. We also conduct an empirical evaluation, comparing the perplexities of the proposed LLMs with those of other modern open LLMs. In addition, benchmarking the proposed LLMs against language understanding tasks reveals that high-quality pretraining datasets may be essential for achieving models that perform efficiently on these benchmarks. The full realisations of the described LLMs are available in the accompanying open repository~\url{https://huggingface.co/neurotechnology}.

## 07-052 | LLäMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch
- arXiv: 2411.11171  first public: 2024-11-17  latest: 2025-06-18  primary cat: cs.CL
- authors (3): Jan Pfister; Julia Wunderle; Andreas Hotho
- seed subtopic: 从零预训练（德语）; type: 原始研究; cross: []
- arXiv comment: camera ready @ACL25; https://www.informatik.uni-wuerzburg.de/datascience/projects/nlp/llammlein/
- pages: 20

ABSTRACT: We create two German-only decoder models, LLäMmlein 120M and 1B, transparently from scratch and publish them, along with the training data, for the German NLP research community to use. The model training involved several key steps, including extensive data preprocessing, the creation of a custom German tokenizer, the training itself, as well as the evaluation of the final models on various benchmarks. Throughout the training process, multiple checkpoints were saved and analyzed using the SuperGLEBer benchmark to monitor the models' learning dynamics. Compared to state-of-the-art models on the SuperGLEBer benchmark, both LLäMmlein models performed competitively, consistently matching or surpassing models with similar parameter sizes. The results show that the models' quality scales with size as expected, but performance improvements on some tasks plateaued early, offering valuable insights into resource allocation for future model development.

## 07-053 | CroissantLLM: A Truly Bilingual French-English Language Model
- arXiv: 2402.00786  first public: 2024-02-01  latest: 2025-04-09  primary cat: cs.CL
- authors (16): Manuel Faysse; Patrick Fernandes; Nuno M. Guerreiro; António Loison; Duarte M. Alves; Caio Corro ...
- seed subtopic: 双语从零预训练; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/CoderPat/croissant-llm-training https://github.com/EleutherAI/lm-evaluation-harness https://github.com/ManuelFay/llm-data-hub https://huggingface.co/CroissantLLM
- pages: 48

ABSTRACT: We introduce CroissantLLM, a 1.3B language model pretrained on a set of 3T English and French tokens, to bring to the research and industrial community a high-performance, fully open-sourced bilingual model that runs swiftly on consumer-grade local hardware. To that end, we pioneer the approach of training an intrinsically bilingual model with a 1:1 English-to-French pretraining data ratio, a custom tokenizer, and bilingual finetuning datasets. We release the training dataset, notably containing a French split with manually curated, high-quality, and varied data sources. To assess performance outside of English, we craft a novel benchmark, FrenchBench, consisting of an array of classification and generation tasks, covering various orthogonal aspects of model performance in the French Language. Additionally, rooted in transparency and to foster further Large Language Model research, we release codebases, and dozens of checkpoints across various model sizes, training data distributions, and training steps, as well as fine-tuned Chat models, and strong translation models. We evaluate our model through the FMTI framework, and validate 81 % of the transparency criteria, far beyond the scores of even most open initiatives. This work enriches the NLP landscape, breaking away from previous English-centric work in order to strengthen our understanding of multilinguality in language models.

## 07-054 | MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies
- arXiv: 2404.06395  first public: 2024-04-09  latest: 2024-06-03  primary cat: cs.CL
- authors (25): Shengding Hu; Yuge Tu; Xu Han; Chaoqun He; Ganqu Cui; Xiang Long ...
- seed subtopic: WSD 学习率调度; type: 原始研究; cross: []
- arXiv comment: revise according to peer review
- URLs on first pages of PDF: https://github.com/OpenBMB/MiniCPM
- pages: 32

ABSTRACT: The burgeoning interest in developing Large Language Models (LLMs) with up to trillion parameters has been met with concerns regarding resource efficiency and practical expense, particularly given the immense cost of experimentation. This scenario underscores the importance of exploring the potential of Small Language Models (SLMs) as a resource-efficient alternative. In this context, we introduce MiniCPM, specifically the 1.2B and 2.4B non-embedding parameter variants, not only excel in their respective categories but also demonstrate capabilities on par with 7B-13B LLMs. While focusing on SLMs, our approach exhibits scalability in both model and data dimensions for future LLM research. Regarding model scaling, we employ extensive model wind tunnel experiments for stable and optimal scaling. For data scaling, we introduce a Warmup-Stable-Decay (WSD) learning rate scheduler (LRS), conducive to continuous training and domain adaptation. We present an in-depth analysis of the intriguing training dynamics that occurred in the WSD LRS. With WSD LRS, we are now able to efficiently study data-model scaling law without extensive retraining experiments on both axes of model and data, from which we derive the much higher compute optimal data-model ratio than Chinchilla Optimal. Additionally, we introduce MiniCPM family, including MiniCPM-DPO, MiniCPM-MoE and MiniCPM-128K, whose excellent performance further cementing MiniCPM's foundation in diverse SLM applications. MiniCPM models are available publicly at https://github.com/OpenBMB/MiniCPM .

## 07-056 | Exploring Design Choices for Building Language-Specific LLMs
- arXiv: 2406.14670  first public: 2024-06-20  latest: 2024-10-30  primary cat: cs.CL
- authors (3): Atula Tejaswi; Nilesh Gupta; Eunsol Choi
- seed subtopic: 语言专属模型设计; type: 原始研究; cross: ['06']
- arXiv comment: Accepted to EMNLP 2024 Findings
- URLs on first pages of PDF: https://github.com/atutej/ https://github.com/google/sentencepiece
- pages: 16

ABSTRACT: Despite rapid progress in large language models (LLMs), their performance on a vast majority of languages remains unsatisfactory. In this paper, we study building language-specific LLMs by adapting monolingual and multilingual LLMs. We conduct systematic experiments on how design choices (base model selection, vocabulary extension, and continued pretraining) impact the adapted LLM, both in terms of efficiency (how many tokens are needed to encode the same amount of information) and end task performance. We find that (1) the initial performance of LLM does not always correlate with the final performance after the adaptation. Adapting an English-centric models can yield better results than adapting multilingual models despite their worse initial performance on low-resource languages. (2) Efficiency can easily improved with simple vocabulary extension and continued pretraining in most LLMs we study, and (3) The optimal adaptation method (choice of the base model, new vocabulary size, training data, initialization strategy) is highly language-dependent, and the simplest embedding initialization works well across various experimental settings. Together, our work lays foundations on efficiently building language-specific LLMs by adapting existing LLMs.

## 07-057 | TituLLMs: A Family of Bangla LLMs with Comprehensive Benchmarking
- arXiv: 2502.11187  first public: 2025-02-16  latest: 2025-06-05  primary cat: cs.CL
- authors (10): Shahriar Kabir Nahin; Rabindra Nath Nandi; Sagor Sarker; Quazi Sarwar Muhtaseem; Md Kowsher; Apu Chandraw Shill ...
- seed subtopic: 孟加拉语持续预训练; type: 原始研究; cross: []
- arXiv comment: LLMs, Benchmarking, Large Language Models, Bangla, BanglaLLMs
- URLs on first pages of PDF: https://github.com/hishab-nlp/titulm https://github.com/tesseract-ocr/tesseract
- pages: 19

ABSTRACT: In this paper, we present TituLLMs, the first large pretrained Bangla LLMs, available in 1b and 3b parameter sizes. Due to computational constraints during both training and inference, we focused on smaller models. To train TituLLMs, we collected a pretraining dataset of approximately ~37 billion tokens. We extended the Llama-3.2 tokenizer to incorporate language- and culture-specific knowledge, which also enables faster training and inference. There was a lack of benchmarking datasets to benchmark LLMs for Bangla. To address this gap, we developed five benchmarking datasets. We benchmarked various LLMs, including TituLLMs, and demonstrated that TituLLMs outperforms its initial multilingual versions. However, this is not always the case, highlighting the complexities of language adaptation. Our work lays the groundwork for adapting existing multilingual open models to other low-resource languages. To facilitate broader adoption and further research, we have made the TituLLMs models and benchmarking datasets publicly available (https://huggingface.co/collections/hishab/titulm-llama-family-6718d31fc1b83529276f490a).

## 07-058 | Qalb: Largest State-of-the-Art Urdu Large Language Model for 230M Speakers with Systematic Continued Pre-training
- arXiv: 2601.08141  first public: 2026-01-13  latest: 2026-01-13  primary cat: cs.CL
- authors (3): Muhammad Taimoor Hassan; Jawad Ahmed; Muhammad Awais
- seed subtopic: 乌尔都语持续预训练; type: 原始研究; cross: []
- pages: 7

ABSTRACT: Despite remarkable progress in large language models, Urdu-a language spoken by over 230 million people-remains critically underrepresented in modern NLP systems. Existing multilingual models demonstrate poor performance on Urdu-specific tasks, struggling with the language's complex morphology, right-to-left Nastaliq script, and rich literary traditions. Even the base LLaMA-3.1 8B-Instruct model shows limited capability in generating fluent, contextually appropriate Urdu text. We introduce Qalb, an Urdu language model developed through a two-stage approach: continued pre-training followed by supervised fine-tuning. Starting from LLaMA 3.1 8B, we perform continued pre-training on a dataset of 1.97 billion tokens. This corpus comprises 1.84 billion tokens of diverse Urdu text-spanning news archives, classical and contemporary literature, government documents, and social media-combined with 140 million tokens of English Wikipedia data to prevent catastrophic forgetting. We then fine-tune the resulting model on the Alif Urdu-instruct dataset. Through extensive evaluation on Urdu-specific benchmarks, Qalb demonstrates substantial improvements, achieving a weighted average score of 90.34 and outperforming the previous state-of-the-art Alif-1.0-Instruct model (87.1) by 3.24 points, while also surpassing the base LLaMA-3.1 8B-Instruct model by 44.64 points. Qalb achieves state-of-the-art performance with comprehensive evaluation across seven diverse tasks including Classification, Sentiment Analysis, and Reasoning. Our results demonstrate that continued pre-training on diverse, high-quality language data, combined with targeted instruction fine-tuning, effectively adapts foundation models to low-resource languages.

## 07-060 | BYOL: Bring Your Own Language Into LLMs
- arXiv: 2601.10804  first public: 2026-01-15  latest: 2026-01-15  primary cat: cs.CL
- authors (6): Syed Waqas Zamir; Wassim Hamidouche; Boulbaba Ben Amor; Luana Marotti; Inbal Becker-Reshef; Juan Lavista Ferres
- seed subtopic: 新语言接入框架; type: 原始研究; cross: []
- URLs on first pages of PDF: https://commoncrawl.github.io/cc-crawl-statistics/plots/languages.html https://github.com/microsoft/byol
- pages: 42

ABSTRACT: Large Language Models (LLMs) exhibit strong multilingual capabilities, yet remain fundamentally constrained by the severe imbalance in global language resources. While over 7,000 languages are spoken worldwide, only a small subset (fewer than 100) has sufficient digital presence to meaningfully influence modern LLM training. This disparity leads to systematic underperformance, cultural misalignment, and limited accessibility for speakers of low-resource and extreme-low-resource languages. To address this gap, we introduce Bring Your Own Language (BYOL), a unified framework for scalable, language-aware LLM development tailored to each language's digital footprint. BYOL begins with a language resource classification that maps languages into four tiers (Extreme-Low, Low, Mid, High) using curated web-scale corpora, and uses this classification to select the appropriate integration pathway. For low-resource languages, we propose a full-stack data refinement and expansion pipeline that combines corpus cleaning, synthetic text generation, continual pretraining, and supervised finetuning. Applied to Chichewa and Maori, this pipeline yields language-specific LLMs that achieve approximately 12 percent average improvement over strong multilingual baselines across 12 benchmarks, while preserving English and multilingual capabilities via weight-space model merging. For extreme-low-resource languages, we introduce a translation-mediated inclusion pathway, and show on Inuktitut that a tailored machine translation system improves over a commercial baseline by 4 BLEU, enabling high-accuracy LLM access when direct language modeling is infeasible. Finally, we release human-translated versions of the Global MMLU-Lite benchmark in Chichewa, Maori, and Inuktitut, and make our codebase and models publicly available at https://github.com/microsoft/byol .

## 07-061 | Learning Dynamics in Continual Pre-Training for Large Language Models
- arXiv: 2505.07796  first public: 2025-05-12  latest: 2025-06-19  primary cat: cs.CL
- authors (5): Xingjin Wang; Howe Tissue; Lu Wang; Linjing Li; Daniel Dajun Zeng
- seed subtopic: 持续预训练动态; type: 原始研究; cross: []
- arXiv comment: Accepted to ICML2025 (Oral)
- pages: 24

ABSTRACT: Continual Pre-Training (CPT) has become a popular and effective method to apply strong foundation models to specific downstream tasks. In this work, we explore the learning dynamics throughout the CPT process for large language models. We specifically focus on how general and downstream domain performance evolves at each training step, with domain performance measured via validation losses. We have observed that the CPT loss curve fundamentally characterizes the transition from one curve to another hidden curve, and could be described by decoupling the effects of distribution shift and learning rate annealing. We derive a CPT scaling law that combines the two factors, enabling the prediction of loss at any (continual) training steps and across learning rate schedules (LRS) in CPT. Our formulation presents a comprehensive understanding of several critical factors in CPT, including loss potential, peak learning rate, training steps, replay ratio, etc. Moreover, our approach can be adapted to customize training hyper-parameters to different CPT goals such as balancing general and domain-specific performance. Extensive experiments demonstrate that our scaling law holds across various CPT datasets and training hyper-parameters.

## 07-062 | Revisiting Replay and Gradient Alignment for Continual Pre-Training of Large Language Models
- arXiv: 2508.01908  first public: 2025-08-03  latest: 2025-08-03  primary cat: cs.LG
- authors (9): Istabrak Abbes; Gopeshh Subbaraj; Matthew Riemer; Nizar Islah; Benjamin Therien; Tsuguchika Tabaru ...
- seed subtopic: 重放与梯度对齐; type: 原始研究; cross: []
- pages: 22

ABSTRACT: Training large language models (LLMs) typically involves pre-training on massive corpora, only to restart the process entirely when new data becomes available. A more efficient and resource-conserving approach would be continual pre-training, where models are updated with new data rather than retraining from scratch. However, the introduction of new data often causes distribution shifts, leading to performance degradation on previously learned tasks. In this paper, we take a deeper look at two popular proposals for addressing this distribution shift within the continual learning literature: experience replay and gradient alignment. We consider continual pre-training of models within the Llama family of architectures at a large scale across languages with 100 billion tokens of training data in each language, finding that both replay and gradient alignment lead to more stable learning without forgetting. This conclusion holds both as we vary the model scale and as we vary the number and diversity of tasks. Moreover, we are the first to demonstrate the effectiveness of gradient alignment techniques in the context of LLM pre-training and propose an efficient implementation of meta-experience replay (MER) that imbues experience replay with the benefits of gradient alignment despite negligible compute and memory overhead. Our scaling analysis across model sizes and replay rates indicates that small rates of replaying old examples are definitely a more valuable use of compute than investing in model size, but that it is more compute efficient to scale the size of the model than invest in high rates of replaying old examples.

## 07-063 | UniMax: Fairer and more Effective Language Sampling for Large-Scale Multilingual Pretraining
- arXiv: 2304.09151  first public: 2023-04-18  latest: 2023-04-18  primary cat: cs.CL
- authors (7): Hyung Won Chung; Noah Constant; Xavier Garcia; Adam Roberts; Yi Tay; Sharan Narang ...
- seed subtopic: 语言采样; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/google-research/t5x/blob/main/docs/models.md
- pages: 19

ABSTRACT: Pretrained multilingual large language models have typically used heuristic temperature-based sampling to balance between different languages. However previous work has not systematically evaluated the efficacy of different pretraining language distributions across model scales. In this paper, we propose a new sampling method, UniMax, that delivers more uniform coverage of head languages while mitigating overfitting on tail languages by explicitly capping the number of repeats over each language's corpus. We perform an extensive series of ablations testing a range of sampling strategies on a suite of multilingual benchmarks, while varying model scale. We find that UniMax outperforms standard temperature-based sampling, and the benefits persist as scale increases. As part of our contribution, we release: (i) an improved and refreshed mC4 multilingual corpus consisting of 29 trillion characters across 107 languages, and (ii) a suite of pretrained umT5 model checkpoints trained with UniMax sampling.

## 07-064 | Chat Vector: A Simple Approach to Equip LLMs with Instruction Following and Model Alignment in New Languages
- arXiv: 2310.04799  first public: 2023-10-07  latest: 2024-06-07  primary cat: cs.CL
- authors (8): Shih-Cheng Huang; Pin-Zu Li; Yu-Chi Hsu; Kuang-Ming Chen; Yu Tung Lin; Shih-Kai Hsiao ...
- seed subtopic: 任务向量合并; type: 原始研究; cross: ['08']
- arXiv comment: ACL 2024 camera-ready version
- pages: 17

ABSTRACT: Recently, the development of open-source large language models (LLMs) has advanced rapidly. Nevertheless, due to data constraints, the capabilities of most open-source LLMs are primarily focused on English. To address this issue, we introduce the concept of $\textit{chat vector}$ to equip pre-trained language models with instruction following and human value alignment via simple model arithmetic. The chat vector is derived by subtracting the weights of a pre-trained base model (e.g. LLaMA2) from those of its corresponding chat model (e.g. LLaMA2-chat). By simply adding the chat vector to a continual pre-trained model's weights, we can endow the model with chat capabilities in new languages without the need for further training. Our empirical studies demonstrate the superior efficacy of the chat vector from three different aspects: instruction following, toxicity mitigation, and multi-turn dialogue. Moreover, to showcase the adaptability of our approach, we extend our experiments to encompass various languages, base models, and chat vectors. The results underscore the chat vector's simplicity, effectiveness, and wide applicability, making it a compelling solution for efficiently enabling conversational capabilities in pre-trained language models. Our code is available at https://github.com/aqweteddy/ChatVector.

## 07-065 | SambaLingo: Teaching Large Language Models New Languages
- arXiv: 2404.05829  first public: 2024-04-08  latest: 2024-07-17  primary cat: cs.CL
- authors (10): Zoltan Csaki; Bo Li; Jonathan Li; Qiantong Xu; Pian Pawakapan; Leon Zhang ...
- seed subtopic: 向新语言持续预训练; type: 原始研究; cross: ['06']
- arXiv comment: 23 pages
- URLs on first pages of PDF: https://huggingface.co/collections/sambanovasystems/
- pages: 24

ABSTRACT: Despite the widespread availability of LLMs, there remains a substantial gap in their capabilities and availability across diverse languages. One approach to address these issues has been to take an existing pre-trained LLM and continue to train it on new languages. While prior works have experimented with language adaptation, many questions around best practices and methodology have not been covered. In this paper, we present a comprehensive investigation into the adaptation of LLMs to new languages. Our study covers the key components in this process, including vocabulary extension, direct preference optimization and the data scarcity problem for human alignment in low-resource languages. We scale these experiments across 9 languages and 2 parameter scales (7B and 70B). We compare our models against Llama 2, Aya-101, XGLM, BLOOM and existing language experts, outperforming all prior published baselines. Additionally, all evaluation code and checkpoints are made public to facilitate future research.

## 07-066 | Adapting Chat Language Models Using Only Target Unlabeled Language Data
- arXiv: 2412.11704  first public: 2024-12-16  latest: 2025-09-29  primary cat: cs.CL
- authors (4): Atsuki Yamaguchi; Terufumi Morishita; Aline Villavicencio; Nikolaos Aletras
- seed subtopic: 聊天模型的语言适配; type: 原始研究; cross: ['08']
- arXiv comment: Accepted to TMLR
- URLs on first pages of PDF: https://huggingface.co/Almawave/Velvet-14B https://huggingface.co/collections/LGAI-EXAONE/exaone-35-674d0e1bb3dcd2ab6f39dbb4 https://huggingface.co/microsoft/phi-4/discussions/4
- pages: 42

ABSTRACT: Vocabulary expansion (VE) is the de-facto approach to language adaptation of large language models (LLMs) by adding new tokens and continuing pre-training on target data. While this is effective for base models trained on unlabeled data, it poses challenges for chat models trained to follow instructions through labeled conversation data. Directly adapting the latter with VE on target unlabeled data may result in forgetting chat abilities. While ideal, target chat data is often unavailable or costly to create for low-resource languages, and machine-translated alternatives are not always effective. To address this issue, previous work proposed using a base and chat model from the same family. This method first adapts the base LLM with VE on target unlabeled data and then converts it to a chat model by adding a chat vector (CV) derived from the weight difference between the source base and chat models. We propose ElChat, a new language adaptation method for chat LLMs that adapts a chat model directly on target unlabeled data, without a base model. It elicits chat abilities by injecting information from the source chat model. ElChat offers more robust and competitive target language and safety performance while achieving superior English, chat, and instruction-following abilities compared to CV.

## 07-067 | Efficient Language Adaptive Pre-training: Extending State-of-the-Art Large Language Models for Polish
- arXiv: 2402.09759  first public: 2024-02-15  latest: 2024-02-15  primary cat: cs.CL
- authors (1): Szymon Ruciński
- seed subtopic: 波兰语适配预训练; type: 原始研究; cross: []
- arXiv comment: 10 pages
- pages: 10

ABSTRACT: This study explores the potential of fine-tuning foundational English Large Language Models (LLMs) for generating Polish text. The first step involves Language Adaptive Pre-training (LAPT) on a high-quality dataset of 3.11 GB, consisting of 276 million Polish tokens. The LAPT is followed by additional fine-tuning aimed at solving nine KLEJ challenges. Our trained model Curie-7B-v1 not only generates Polish text with the lowest perplexity of 3.02 among decoder-based Polish models but also closely rivals the performance of the best Polish encoder-decoder models with a less than 2% gap on 8 out of 9 tasks. Curie-7B-v1 used approximately 2-3% of a typical dataset size to learn Polish. The LAPT was completed in less than five days using a consumer GPU, highlighting the method's efficiency. The proficiency of the model in Polish was significantly enhanced, demonstrating the viability of this approach for adding new languages to existing LLMs by training just 1.2% of its parameters. To contribute to the community's collaborative progress, the model has been released as open-source.

## 07-068 | Arabic Stable LM: Adapting Stable LM 2 1.6B to Arabic
- arXiv: 2412.04277  first public: 2024-12-05  latest: 2024-12-05  primary cat: cs.CL
- authors (11): Zaid Alyafeai; Michael Pieler; Hannah Teufel; Jonathan Tow; Marco Bellagente; Duy Phung ...
- seed subtopic: 阿拉伯语小模型持续预训练; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/huggingface/datatrove https://huggingface.co/models https://huggingface.co/stabilityai/
- pages: 18

ABSTRACT: Large Language Models (LLMs) have shown impressive results in multiple domains of natural language processing (NLP) but are mainly focused on the English language. Recently, more LLMs have incorporated a larger proportion of multilingual text to represent low-resource languages. In Arabic NLP, several Arabic-centric LLMs have shown remarkable results on multiple benchmarks in the past two years. However, most Arabic LLMs have more than 7 billion parameters, which increases their hardware requirements and inference latency, when compared to smaller LLMs. This paper introduces Arabic Stable LM 1.6B in a base and chat version as a small but powerful Arabic-centric LLM. Our Arabic Stable LM 1.6B chat model achieves impressive results on several benchmarks beating multiple models with up to 8x the parameters. In addition, we show the benefit of mixing in synthetic instruction tuning data by augmenting our fine-tuning data with a large synthetic dialogue dataset.

## 07-069 | The Unreasonable Effectiveness of Model Merging for Cross-Lingual Transfer in LLMs
- arXiv: 2505.18356  first public: 2025-05-23  latest: 2025-10-07  primary cat: cs.CL
- authors (2): Lucas Bandarkar; Nanyun Peng
- seed subtopic: 模型合并跨语言迁移; type: 原始研究; cross: ['11']
- arXiv comment: MRL Workshop at EMNLP 2025
- pages: 18

ABSTRACT: Large language models (LLMs) still struggle across tasks outside of high-resource languages. In this work, we investigate cross-lingual transfer to lower-resource languages where task-specific post-training data is scarce. Building on prior work, we first validate that the subsets of model parameters that matter most for mathematical reasoning and multilingual capabilities are distinctly non-overlapping. To exploit this implicit separability between task and target language parameterization, we develop and analyze numerous modular frameworks to improve the composition of the two during fine-tuning. These methods generally employ freezing parameters or post hoc model merging to assign math and language improvement to different key parts of the LLM. In the absence of in-language math data, we demonstrate that the modular approaches successfully improve upon baselines across three languages, four models, and two fine-tuning paradigms (full and LoRA). Furthermore, we identify the most consistently successful modular method to be fine-tuning separate language and math experts and model merging via Layer-Swapping, somewhat surprisingly. We offer possible explanations for this result via recent works on the linearity of task vectors. We further explain this by empirically showing that reverting less useful fine-tuning updates after training often outperforms freezing them from the start.

## 07-070 | BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting
- arXiv: 2212.09535  first public: 2022-12-19  latest: 2023-05-27  primary cat: cs.CL
- authors (15): Zheng-Xin Yong; Hailey Schoelkopf; Niklas Muennighoff; Alham Fikri Aji; David Ifeoluwa Adelani; Khalid Almubarak ...
- seed subtopic: 新增语言支持; type: 原始研究; cross: ['08']
- arXiv comment: ACL 2023
- pages: 20

ABSTRACT: The BLOOM model is a large publicly available multilingual language model, but its pretraining was limited to 46 languages. To extend the benefits of BLOOM to other languages without incurring prohibitively large costs, it is desirable to adapt BLOOM to new languages not seen during pretraining. In this work, we apply existing language adaptation strategies to BLOOM and benchmark its zero-shot prompting performance on eight new languages in a resource-constrained setting. We find language adaptation to be effective at improving zero-shot performance in new languages. Surprisingly, we find that adapter-based finetuning is more effective than continued pretraining for large models. In addition, we discover that prompting performance is not significantly affected by language specifics, such as the writing system. It is primarily determined by the size of the language adaptation data. We also add new languages to BLOOMZ, which is a multitask finetuned version of BLOOM capable of following task instructions zero-shot. We find including a new language in the multitask fine-tuning mixture to be the most effective method to teach BLOOMZ a new language. We conclude that with sufficient training data language adaptation can generalize well to diverse languages. Our code is available at https://github.com/bigscience-workshop/multilingual-modeling.

## 07-071 | Different Perturbations, Different Mechanisms: Understanding Continued Pre-training for Zero-Shot Dialect Robustness
- arXiv: 2608.05510  first public: 2026-08-06  latest: 2026-08-06  primary cat: cs.CL
- authors (2): Aarohi Srivastava; David Chiang
- seed subtopic: 方言鲁棒性持续预训练; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/meta-llama/Llama-2-7b
- pages: 13

ABSTRACT: Dialectal variation remains a major challenge for multilingual language models. Perturbation-based continued pre-training (CPT) has emerged as a promising approach to improving robustness, yet existing work largely evaluates individual perturbation strategies in isolation and provides limited insight into why they work. We present a systematic study of perturbation-based CPT for multilingual dialect robustness in LLMs, comparing six training conditions across nine German, Italian, and Arabic dialect tasks. Perturbation-based CPT, especially character-noised CPT, consistently improves zero-shot dialect robustness while largely preserving standard variety performance. More importantly, we show that methods with similar downstream performance induce distinct mechanisms of robustness, exhibiting different patterns of language model adaptation, representational alignment, and prediction repair. Our results provide a more complete understanding of how synthetic surface variation improves robustness and offer practical guidance for selecting CPT strategies in multilingual and dialectal settings.

## 07-072 | Leveraging Routing Dynamics in Mixture-of-Experts Models for Efficient Language Adaptation
- arXiv: 2605.29714  first public: 2026-05-28  latest: 2026-05-28  primary cat: cs.CL
- authors (5): Aditi Khandelwal; Marius Mosbach; Verna Dankers; Siva Reddy; Golnoosh Farnadi
- seed subtopic: MoE 语言适配; type: 原始研究; cross: []
- pages: 15

ABSTRACT: Mixture-of-Experts (MoE) models are widely used to scale language models, yet their expert routing behavior and adaptation in a multilingual setting remain underexplored. In this work, we study multilingual routing dynamics during continual pre-training of an English-centric MoE model on a multilingual corpus, analyzing how expert usage varies across languages. We find that continual multilingual pre-training leads to diffused, language-agnostic routing in early and middle layers, with language specialization primarily emerging in the final layers. We also show that token-level vocabulary overlap between languages plays an important role in how languages are routed. Motivated by these findings, we propose a parameter-efficient adaptation strategy that updates language-specific and shared experts in the final MoE layers. Experiments on MultiBLiMP and Belebele show that our method achieves a strong performance-efficiency trade-off, attaining competitive performance relative to fine-tuning complete final layers, while updating less than 2% of the parameters. Overall, our findings provide insights into where and how language specialization emerges in MoEs during continual pre-training and provide practical insights for low-resource multilingual adaptation. Our code is available at https://github.com/aditi184/moe-routing-adaptation.
