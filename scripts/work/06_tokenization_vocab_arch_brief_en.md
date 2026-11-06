# Brief for annotation: 06 分词、词表与模型架构

## 06-054 | Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Robust, Adaptable Language Models
- arXiv: 2501.10322  first public: 2025-01-17  latest: 2025-01-20  primary cat: cs.CL
- authors (4): Pit Neitemeier; Björn Deiseroth; Constantin Eichenberg; Lukas Balles
- seed subtopic: 字节-词层次模型; type: 原始研究; cross: []
- pages: 24

ABSTRACT: Tokenization is a fundamental step in natural language processing, breaking text into units that computational models can process. While learned subword tokenizers have become the de-facto standard, they present challenges such as large vocabularies, limited adaptability to new domains or languages, and sensitivity to spelling errors and variations. To overcome these limitations, we investigate a hierarchical architecture for autoregressive language modelling that combines character-level and word-level processing. It employs a lightweight character-level encoder to convert character sequences into word embeddings, which are then processed by a word-level backbone model and decoded back into characters via a compact character-level decoder. This method retains the sequence compression benefits of word-level tokenization without relying on a rigid, predefined vocabulary. We demonstrate, at scales up to 7 billion parameters, that hierarchical transformers match the downstream task performance of subword-tokenizer-based models while exhibiting significantly greater robustness to input perturbations. Additionally, during continued pretraining on an out-of-domain language, our model trains almost twice as fast, achieves superior performance on the target language, and retains more of its previously learned knowledge. Hierarchical transformers pave the way for NLP systems that are more robust, flexible, and generalizable across languages and domains.

## 06-055 | Dynamic Chunking for End-to-End Hierarchical Sequence Modeling
- arXiv: 2507.07955  first public: 2025-07-10  latest: 2025-07-15  primary cat: cs.LG
- authors (3): Sukjun Hwang; Brandon Wang; Albert Gu
- seed subtopic: 动态分块（H-Net）; type: 原始研究; cross: []
- pages: 39

ABSTRACT: Major progress on language models (LMs) in recent years has largely resulted from moving away from specialized models designed for specific tasks, to general models based on powerful architectures (e.g. the Transformer) that learn everything from raw data. Despite this trend, pre-processing steps such as tokenization remain a barrier to true end-to-end foundation models. We introduce a collection of new techniques that enable a dynamic chunking mechanism which automatically learns content- and context- dependent segmentation strategies learned jointly with the rest of the model. Incorporating this into an explicit hierarchical network (H-Net) allows replacing the (implicitly hierarchical) tokenization-LM-detokenization pipeline with a single model learned fully end-to-end. When compute- and data- matched, an H-Net with one stage of hierarchy operating at the byte level outperforms a strong Transformer language model operating over BPE tokens. Iterating the hierarchy to multiple stages further increases its performance by modeling multiple levels of abstraction, demonstrating significantly better scaling with data and matching the token-based Transformer of twice its size. H-Nets pretrained on English show significantly increased character-level robustness, and qualitatively learn meaningful data-dependent chunking strategies without any heuristics or explicit supervision. Finally, the H-Net's improvement over tokenized pipelines is further increased in languages and modalities with weaker tokenization heuristics, such as Chinese and code, or DNA sequences (nearly 4x improvement in data efficiency over baselines), showing the potential of true end-to-end models that learn and scale better from unprocessed data.

## 06-056 | H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich Languages
- arXiv: 2508.05628  first public: 2025-08-07  latest: 2025-08-07  primary cat: cs.CL
- authors (2): Mehrdad Zakershahrak; Samira Ghodratnama
- seed subtopic: 形态丰富语言的无分词模型; type: 原始研究; cross: []
- pages: 11

ABSTRACT: Byte-level language models eliminate fragile tokenizers but face computational challenges in morphologically-rich languages (MRLs), where words span many bytes. We propose H-NET++, a hierarchical dynamic-chunking model that learns linguistically-informed segmentation through end-to-end training. Key innovations include: (1) a lightweight Transformer context-mixer (1.9M parameters) for cross-chunk attention, (2) a two-level latent hyper-prior for document-level consistency, (3) specialized handling of orthographic artifacts (e.g. Persian ZWNJ), and (4) curriculum-based training with staged sequence lengths. On a 1.4B-token Persian corpus, H-NET++ achieves state-of-the-art results: 0.159 BPB reduction versus BPE-based GPT-2-fa (12% better compression), 5.4pp gain on ParsGLUE, 53% improved robustness to ZWNJ corruption, and 73.8% F1 on gold morphological boundaries. Our learned chunks align with Persian morphology without explicit supervision, demonstrating that hierarchical dynamic chunking provides an effective tokenizer-free solution for MRLs while maintaining computational efficiency.

## 06-058 | BanglaByT5: Byte-Level Modelling for Bangla
- arXiv: 2505.17102  first public: 2025-05-21  latest: 2025-05-21  primary cat: cs.CL
- authors (2): Pramit Bhattacharyya; Arnab Bhattacharya
- seed subtopic: 字节级模型（孟加拉文）; type: 原始研究; cross: []
- pages: 9

ABSTRACT: Large language models (LLMs) have achieved remarkable success across various natural language processing tasks. However, most LLM models use traditional tokenizers like BPE and SentencePiece, which fail to capture the finer nuances of a morphologically rich language like Bangla (Bengali). In this work, we introduce BanglaByT5, the first byte-level encoder-decoder model explicitly tailored for Bangla. Built upon a small variant of Googles ByT5 architecture, BanglaByT5 is pre-trained on a 14GB curated corpus combining high-quality literary and newspaper articles. Through zeroshot and supervised evaluations across generative and classification tasks, BanglaByT5 demonstrates competitive performance, surpassing several multilingual and larger models. Our findings highlight the efficacy of byte-level modelling for morphologically rich languages and highlight BanglaByT5 potential as a lightweight yet powerful tool for Bangla NLP, particularly in both resource-constrained and scalable environments.

## 06-059 | Bit-level BPE: Below the byte boundary
- arXiv: 2506.07541  first public: 2025-06-09  latest: 2025-06-09  primary cat: cs.CL
- authors (3): Sangwhan Moon; Tatsuya Hiraoka; Naoaki Okazaki
- seed subtopic: 低于字节的编码（CJK）; type: 原始研究; cross: []
- pages: 12

ABSTRACT: Byte-level fallbacks for subword tokenization have become a common practice in large language models. In particular, it has been demonstrated to be incredibly effective as a pragmatic solution for preventing OOV, especially in the context of larger models. However, breaking a character down to individual bytes significantly increases the sequence length for long-tail tokens in languages such as Chinese, Japanese, and Korean (CJK) and other character-diverse contexts such as emoji. The increased sequence length results in longer computation during both training and inference. In this work, we propose a simple compression technique that reduces the sequence length losslessly.

## 06-060 | Measuring Cross-lingual Transfer in Bytes
- arXiv: 2404.08191  first public: 2024-04-12  latest: 2024-04-12  primary cat: cs.CL
- authors (4): Leandro Rodrigues de Souza; Thales Sales Almeida; Roberto Lotufo; Rodrigo Nogueira
- seed subtopic: 字节模型跨语言迁移; type: 原始研究; cross: []
- arXiv comment: NAACL 2024
- URLs on first pages of PDF: https://github.com/lersouza/language-transfer https://huggingface.co/datasets/mc4
- pages: 12

ABSTRACT: Multilingual pretraining has been a successful solution to the challenges posed by the lack of resources for languages. These models can transfer knowledge to target languages with minimal or no examples. Recent research suggests that monolingual models also have a similar capability, but the mechanisms behind this transfer remain unclear. Some studies have explored factors like language contamination and syntactic similarity. An emerging line of research suggests that the representations learned by language models contain two components: a language-specific and a language-agnostic component. The latter is responsible for transferring a more universal knowledge. However, there is a lack of comprehensive exploration of these properties across diverse target languages. To investigate this hypothesis, we conducted an experiment inspired by the work on the Scaling Laws for Transfer. We measured the amount of data transferred from a source language to a target language and found that models initialized from diverse languages perform similarly to a target language in a cross-lingual setting. This was surprising because the amount of data transferred to 10 diverse target languages, such as Spanish, Korean, and Finnish, was quite similar. We also found evidence that this transfer is not related to language contamination or language proximity, which strengthens the hypothesis that the model also relies on language-agnostic knowledge. Our experiments have opened up new possibilities for measuring how much data represents the language-agnostic representations learned during pretraining.

## 06-061 | Multilingual Pretraining for Pixel Language Models
- arXiv: 2505.21265  first public: 2025-05-27  latest: 2025-12-02  primary cat: cs.CL
- authors (5): Ilker Kesen; Jonas F. Lotz; Ingo Ziegler; Phillip Rust; Desmond Elliott
- seed subtopic: 像素语言模型; type: 原始研究; cross: []
- arXiv comment: EMNLP 2025
- pages: 18

ABSTRACT: Pixel language models operate directly on images of rendered text, eliminating the need for a fixed vocabulary. While these models have demonstrated strong capabilities for downstream cross-lingual transfer, multilingual pretraining remains underexplored. We introduce PIXEL-M4, a model pretrained on four visually and linguistically diverse languages: English, Hindi, Ukrainian, and Simplified Chinese. Multilingual evaluations on semantic and syntactic tasks show that PIXEL-M4 outperforms an English-only counterpart on non-Latin scripts. Word-level probing analyses confirm that PIXEL-M4 captures rich linguistic features, even in languages not seen during pretraining. Furthermore, an analysis of its hidden representations shows that multilingual pretraining yields a semantic embedding space closely aligned across the languages used for pretraining. This work demonstrates that multilingual pretraining substantially enhances the capability of pixel language models to effectively support a diverse set of languages.

## 06-062 | Overcoming Vocabulary Constraints with Pixel-level Fallback
- arXiv: 2504.02122  first public: 2025-04-02  latest: 2025-08-10  primary cat: cs.CL
- authors (4): Jonas F. Lotz; Hendra Setiawan; Stephan Peitz; Yova Kementchedjhieva
- seed subtopic: 像素级回退编码; type: 原始研究; cross: []
- arXiv comment: COLM 2025
- pages: 27

ABSTRACT: Subword tokenization requires balancing computational efficiency and vocabulary coverage, which often leads to suboptimal performance on languages and scripts not prioritized during training. We propose to augment pretrained language models with a vocabulary-free encoder that generates input embeddings from text rendered as pixels. Through experiments on English-centric language models, we demonstrate that our approach substantially improves machine translation performance and facilitates effective cross-lingual transfer, outperforming tokenizer-based methods. Furthermore, we find that pixel-based representations outperform byte-level approaches and standard vocabulary expansion. Our approach enhances the multilingual capabilities of monolingual language models without extensive retraining and reduces decoding latency via input compression.

## 06-063 | KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter
- arXiv: 2603.27859  first public: 2026-03-29  latest: 2026-03-29  primary cat: cs.CL
- authors (1): Rauan Akylzhanov
- seed subtopic: 字节级适配器（哈萨克语）; type: 原始研究; cross: []
- arXiv comment: Technical announcement
- pages: 12

ABSTRACT: Large language models fragment Kazakh text into many more tokens than equivalent English text, because their tokenizers were built for high-resource languages. This tokenizer tax inflates compute, shortens the effective context window, and weakens the model's grip on Kazakh morphology. We propose to bypass the tokenizer entirely by feeding raw bytes through a small adapter that learns to speak the internal language of a frozen Qwen2.5-7B. Once the adapter is trained, we freeze it and fine-tune only the attention layers of Qwen on Kazakh text. Our central hypothesis is that this two-stage process -- first teach the interface, then adapt the model -- should match or exceed the accuracy of the original Qwen2.5-7B on standard Kazakh benchmarks. This report describes the ByteKaz architecture and training protocol. Empirical validation is ongoing; this version stakes the design and hypotheses for the record.

## 06-064 | RomanSetu: Efficiently unlocking multilingual capabilities of Large Language Models via Romanization
- arXiv: 2401.14280  first public: 2024-01-25  latest: 2024-06-23  primary cat: cs.CL
- authors (7): Jaavid Aktar Husain; Raj Dabre; Aswanth Kumar; Jay Gala; Thanmay Jayakumar; Ratish Puduppully ...
- seed subtopic: 罗马化作为桥梁; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2024
- pages: 23

ABSTRACT: This study addresses the challenge of extending Large Language Models (LLMs) to non-English languages that use non-Roman scripts. We propose an approach that utilizes the romanized form of text as an interface for LLMs, hypothesizing that its frequent informal use and shared tokens with English enhance cross-lingual alignment. Our approach involves the continual pretraining of an English LLM like Llama 2 on romanized text of non-English, non-Roman script languages, followed by instruction tuning on romanized data. The results indicate that romanized text not only reduces token fertility by 2x-4x but also matches or outperforms native script representation across various NLU, NLG, and MT tasks. Moreover, the embeddings computed on romanized text exhibit closer alignment with their English translations than those from the native script. Our approach presents a promising direction for leveraging the power of English LLMs in languages traditionally underrepresented in NLP. Our code is available on https://github.com/AI4Bharat/romansetu.

## 06-065 | TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models
- arXiv: 2401.06620  first public: 2024-01-12  latest: 2024-05-23  primary cat: cs.CL
- authors (4): Yihong Liu; Chunlan Ma; Haotian Ye; Hinrich Schütze
- seed subtopic: 文字障碍与转写; type: 原始研究; cross: []
- arXiv comment: ACL 2024
- URLs on first pages of PDF: https://github.com/cisnlp/TransliCo https://github.com/isi-nlp/uroman
- pages: 24

ABSTRACT: The world's more than 7000 languages are written in at least 293 scripts. Due to various reasons, many closely related languages use different scripts, which poses a difficulty for multilingual pretrained language models (mPLMs) in learning crosslingual knowledge through lexical overlap. As a consequence, mPLMs are faced with a script barrier: representations from different scripts are located in different subspaces, which can result in crosslingual transfer involving languages of different scripts performing suboptimally. To address this problem, we propose TransliCo, a framework that optimizes the Transliteration Contrastive Modeling (TCM) objective to fine-tune an mPLM by contrasting sentences in its training data and their transliterations in a unified script (in our case Latin), which enhances uniformity in the representation space for different scripts. Using Glot500-m, an mPLM pretrained on over 500 languages, as our source model, we fine-tune it on a small portion (5%) of its training data, and refer to the resulting model as Furina. We show that Furina not only better aligns representations from distinct scripts but also outperforms the original Glot500-m on various zero-shot crosslingual transfer tasks. Additionally, we achieve consistent improvement in a case study on the Indic group where the languages exhibit areal features but use different scripts. We make our code and models publicly available.

## 06-067 | Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment
- arXiv: 2406.19759  first public: 2024-06-28  latest: 2024-10-09  primary cat: cs.CL
- authors (3): Orgest Xhelili; Yihong Liu; Hinrich Schütze
- seed subtopic: 转写后训练对齐; type: 原始研究; cross: []
- arXiv comment: EMNLP 2024 Findings
- pages: 14

ABSTRACT: Multilingual pre-trained models (mPLMs) have shown impressive performance on cross-lingual transfer tasks. However, the transfer performance is often hindered when a low-resource target language is written in a different script than the high-resource source language, even though the two languages may be related or share parts of their vocabularies. Inspired by recent work that uses transliteration to address this problem, our paper proposes a transliteration-based post-pretraining alignment (PPA) method aiming to improve the cross-lingual alignment between languages using diverse scripts. We select two areal language groups, $\textbf{Mediterranean-Amharic-Farsi}$ and $\textbf{South+East Asian Languages}$, wherein the languages are mutually influenced but use different scripts. We apply our method to these language groups and conduct extensive experiments on a spectrum of downstream tasks. The results show that after PPA, models consistently outperform the original model (up to 50% for some tasks) in English-centric transfer. In addition, when we use languages other than English as sources in transfer, our method obtains even larger improvements. We will make our code and models publicly available at \url{https://github.com/cisnlp/Transliteration-PPA}.

## 06-068 | Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages
- arXiv: 2509.17493  first public: 2025-09-22  latest: 2025-09-22  primary cat: cs.CL
- authors (3): Wenhao Zhuang; Yuan Sun; Xiaobing Zhao
- seed subtopic: 可逆转写（中国少数民族语言等）; type: 原始研究; cross: []
- doi: 10.18653/v1/2025.acl-long.795
- pages: 17

ABSTRACT: As large language models (LLMs) are trained on increasingly diverse and extensive multilingual corpora, they demonstrate cross-lingual transfer capabilities. However, these capabilities often fail to effectively extend to low-resource languages, particularly those utilizing non-Latin scripts. While transliterating low-resource languages into Latin script presents a natural solution, there currently lacks a comprehensive framework for integrating transliteration into LLMs training and deployment. Taking a pragmatic approach, this paper innovatively combines character transliteration with Huffman coding to design a complete transliteration framework. Our proposed framework offers the following advantages: 1) Compression: Reduces storage requirements for low-resource language content, achieving up to 50% reduction in file size and 50-80% reduction in token count. 2) Accuracy: Guarantees 100% lossless conversion from transliterated text back to the source language. 3) Efficiency: Eliminates the need for vocabulary expansion for low-resource languages, improving training and inference efficiency. 4) Scalability: The framework can be extended to other low-resource languages. We validate the effectiveness of our framework across multiple downstream tasks, including text classification, machine reading comprehension, and machine translation. Experimental results demonstrate that our method significantly enhances the model's capability to process low-resource languages while maintaining performance on high-resource languages. Our data and code are publicly available at https://github.com/CMLI-NLP/HuffmanTranslit.

## 06-070 | LangSAMP: Language-Script Aware Multilingual Pretraining
- arXiv: 2409.18199  first public: 2024-09-26  latest: 2025-05-21  primary cat: cs.CL
- authors (5): Yihong Liu; Haotian Ye; Chunlan Ma; Mingyang Wang; Hinrich Schütze
- seed subtopic: 语言/文字嵌入; type: 原始研究; cross: []
- arXiv comment: ACL 2025
- pages: 28

ABSTRACT: Recent multilingual pretrained language models (mPLMs) often avoid using language embeddings -- learnable vectors assigned to individual languages. However, this places a significant burden on token representations to encode all language-specific information, which may hinder language neutrality. To address this limitation, we propose Language-Script Aware Multilingual Pretraining (LangSAMP), a method that incorporates both language and script embeddings to enhance representation learning. Specifically, we integrate these embeddings into the output of the Transformer blocks before passing the final representations to the language modeling head for prediction. We apply LangSAMP to the continual pretraining of XLM-R on a highly multilingual corpus covering more than 500 languages. The resulting model consistently outperforms the baseline in zero-shot crosslingual transfer across diverse downstream tasks. Extensive analysis reveals that language and script embeddings capture language- and script-specific nuances, which benefits more language-neutral representations, proven by improved pairwise cosine similarity. In our case study, we also show that language and script embeddings can be used to select better source languages for crosslingual transfer. We make our code and models publicly available at https://github.com/cisnlp/LangSAMP.

## 06-072 | Group then Scale: Dynamic Mixture-of-Experts Multilingual Language Model
- arXiv: 2506.12388  first public: 2025-06-14  latest: 2025-06-14  primary cat: cs.CL
- authors (4): Chong Li; Yingzhuo Deng; Jiajun Zhang; Chengqing Zong
- seed subtopic: 多语言动态 MoE; type: 原始研究; cross: ['03']
- arXiv comment: ACL 2025, our codes and models are available at https://github.com/ZNLP/DMoE
- pages: 25

ABSTRACT: The curse of multilinguality phenomenon is a fundamental problem of multilingual Large Language Models (LLMs), where the competition between massive languages results in inferior performance. It mainly comes from limited capacity and negative transfer between dissimilar languages. To address this issue, we propose a method to dynamically group and scale up the parameters of multilingual LLM while boosting positive transfer among similar languages. Specifically, the model is first tuned on monolingual corpus to determine the parameter deviation in each layer and quantify the similarity between languages. Layers with more deviations are extended to mixture-of-experts layers to reduce competition between languages, where one expert module serves one group of similar languages. Experimental results on 18 to 128 languages show that our method reduces the negative transfer between languages and significantly boosts multilingual performance with fewer parameters. Such language group specialization on experts benefits the new language adaptation and reduces the inference on the previous multilingual knowledge learned.

## 06-073 | Multilingual Routing in Mixture-of-Experts
- arXiv: 2510.04694  first public: 2025-10-06  latest: 2026-02-17  primary cat: cs.CL
- authors (5): Lucas Bandarkar; Chenyuan Yang; Mohsen Fayyaz; Junlin Hu; Nanyun Peng
- seed subtopic: MoE 多语言路由分析; type: 原始研究; cross: []
- arXiv comment: ICLR 2026, In The Fourteenth International Conference on Learning Representations, 2025
- journal_ref: The Fourteenth International Conference on Learning Representations (2026)
- pages: 23

ABSTRACT: Mixture-of-Experts (MoE) architectures have become the key to scaling modern LLMs, yet little is understood about how their sparse routing dynamics respond to multilingual data. In this work, we analyze expert routing patterns using parallel multilingual datasets and present highly interpretable layer-wise phenomena. We find that MoE models route tokens in language-specific ways in the early and late decoder layers but exhibit significant cross-lingual routing alignment in middle layers, mirroring parameter-sharing trends observed in dense LLMs. In particular, we reveal a clear, strong correlation between a model's performance in a given language and how similarly its tokens are routed to English in these layers. Extending beyond correlation, we explore inference-time interventions that induce higher cross-lingual routing alignment. We introduce a method that steers the router by promoting middle-layer task experts frequently activated in English, and it successfully increases multilingual performance. These 1-2% gains are remarkably consistent across two evaluation tasks, three models, and 15+ languages, especially given that these simple interventions override routers of extensively trained, state-of-the-art LLMs. In comparison, interventions outside of the middle layers or targeting multilingual-specialized experts only yield performance degradation. Altogether, we present numerous findings that explain how MoEs process non-English text and demonstrate that generalization is limited by the model's ability to leverage language-universal experts in all languages.

## 06-075 | Language Model Tokenizers Introduce Unfairness Between Languages
- arXiv: 2305.15425  first public: 2023-05-17  latest: 2023-10-20  primary cat: cs.CL
- authors (4): Aleksandar Petrov; Emanuele La Malfa; Philip H. S. Torr; Adel Bibi
- seed subtopic: 分词公平性（经典）; type: 原始研究; cross: []
- arXiv comment: Published at NeurIPS 2023, Project webpage: https://aleksandarpetrov.github.io/tokenization-fairness, Code: https://github.com/AleksandarPetrov/tokenization-fairness
- pages: 28

ABSTRACT: Recent language models have shown impressive multilingual performance, even when not explicitly trained for it. Despite this, there are concerns about the quality of their outputs across different languages. In this paper, we show how disparity in the treatment of different languages arises at the tokenization stage, well before a model is even invoked. The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases. These disparities persist even for tokenizers that are intentionally trained for multilingual support. Character-level and byte-level models also exhibit over 4 times the difference in the encoding length for some language pairs. This induces unfair treatment for some language communities in regard to the cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context to the models. Therefore, we make the case that we should train future language models using multilingually fair subword tokenizers.

## 06-076 | Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models
- arXiv: 2305.13707  first public: 2023-05-23  latest: 2023-05-23  primary cat: cs.CL
- authors (7): Orevaoghene Ahia; Sachin Kumar; Hila Gonen; Jungo Kasai; David R. Mortensen; Noah A. Smith ...
- seed subtopic: 分词成本（经典）; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/opena https://huggingface.co/docs/api-inference/q
- pages: 20

ABSTRACT: Language models have graduated from being research prototypes to commercialized products offered as web APIs, and recent works have highlighted the multilingual capabilities of these products. The API vendors charge their users based on usage, more specifically on the number of ``tokens'' processed or generated by the underlying language models. What constitutes a token, however, is training data and model dependent with a large variance in the number of tokens required to convey the same information in different languages. In this work, we analyze the effect of this non-uniformity on the fairness of an API's pricing policy across languages. We conduct a systematic analysis of the cost and utility of OpenAI's language model API on multilingual benchmarks in 22 typologically diverse languages. We show evidence that speakers of a large number of the supported languages are overcharged while obtaining poorer results. These speakers tend to also come from regions where the APIs are less affordable to begin with. Through these analyses, we aim to increase transparency around language model APIs' pricing policies and encourage the vendors to make them more equitable.

## 06-077 | FOCUS: Effective Embedding Initialization for Monolingual Specialization of Multilingual Models
- arXiv: 2305.14481  first public: 2023-05-23  latest: 2023-11-06  primary cat: cs.CL
- authors (2): Konstantin Dobler; Gerard de Melo
- seed subtopic: 嵌入初始化（经典）; type: 原始研究; cross: []
- arXiv comment: Accepted to EMNLP 2023 Main Conference (Long Paper). Code: https://github.com/konstantinjdobler/focus
- doi: 10.18653/v1/2023.emnlp-main.829
- URLs on first pages of PDF: https://github.com/konstantinjdobler/focus
- pages: 15

ABSTRACT: Using model weights pretrained on a high-resource language as a warm start can reduce the need for data and compute to obtain high-quality language models for other, especially low-resource, languages. However, if we want to use a new tokenizer specialized for the target language, we cannot transfer the source model's embedding matrix. In this paper, we propose FOCUS - Fast Overlapping Token Combinations Using Sparsemax, a novel embedding initialization method that initializes the embedding matrix effectively for a new tokenizer based on information in the source model's embedding matrix. FOCUS represents newly added tokens as combinations of tokens in the overlap of the source and target vocabularies. The overlapping tokens are selected based on semantic similarity in an auxiliary static token embedding space. We focus our study on using the multilingual XLM-R as a source model and empirically show that FOCUS outperforms random initialization and previous work in language modeling and on a range of downstream tasks (NLI, QA, and NER).

## 06-078 | WECHSEL: Effective initialization of subword embeddings for cross-lingual transfer of monolingual language models
- arXiv: 2112.06598  first public: 2021-12-13  latest: 2022-05-04  primary cat: cs.CL
- authors (3): Benjamin Minixhofer; Fabian Paischer; Navid Rekabsaz
- seed subtopic: 嵌入初始化（经典）; type: 原始研究; cross: []
- arXiv comment: NAACL 2022
- doi: 10.18653/v1/2022.naacl-main.293
- pages: 15

ABSTRACT: Large pretrained language models (LMs) have become the central building block of many NLP applications. Training these models requires ever more computational resources and most of the existing models are trained on English text only. It is exceedingly expensive to train these models in other languages. To alleviate this problem, we introduce a novel method -- called WECHSEL -- to efficiently and effectively transfer pretrained LMs to new languages. WECHSEL can be applied to any model which uses subword-based tokenization and learns an embedding for each subword. The tokenizer of the source model (in English) is replaced with a tokenizer in the target language and token embeddings are initialized such that they are semantically similar to the English tokens by utilizing multilingual static word embeddings covering English and the target language. We use WECHSEL to transfer the English RoBERTa and GPT-2 models to four languages (French, German, Chinese and Swahili). We also study the benefits of our method on very low-resource languages. WECHSEL improves over proposed methods for cross-lingual parameter transfer and outperforms models of comparable size trained from scratch with up to 64x less training effort. Our method makes training large language models for new languages more accessible and less damaging to the environment. We make our code and models publicly available.
