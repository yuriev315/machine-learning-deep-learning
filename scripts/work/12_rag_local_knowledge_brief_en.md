# Brief for annotation: 12 检索增强与本地知识

## 12-001 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- arXiv: 2005.11401  first public: 2020-05-22  latest: 2021-04-12  primary cat: cs.CL
- authors (12): Patrick Lewis; Ethan Perez; Aleksandra Piktus; Fabio Petroni; Vladimir Karpukhin; Naman Goyal ...
- seed subtopic: RAG 方法基础; type: 原始研究; cross: []
- arXiv comment: Accepted at NeurIPS 2020
- URLs on first pages of PDF: https://github.com/huggingface/transformers/blob/master/ https://huggingface.co/rag/
- pages: 19

ABSTRACT: Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

## 12-002 | Making a MIRACL: Multilingual Information Retrieval Across a Continuum of Languages
- arXiv: 2210.09984  first public: 2022-10-18  latest: 2022-10-18  primary cat: cs.IR
- authors (9): Xinyu Zhang; Nandan Thakur; Odunayo Ogundepo; Ehsan Kamalloo; David Alfonso-Hermelo; Xiaoguang Li ...
- seed subtopic: 多语言检索基准; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/attardi/wikiextractor
- pages: 6

ABSTRACT: MIRACL (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual dataset we have built for the WSDM 2023 Cup challenge that focuses on ad hoc retrieval across 18 different languages, which collectively encompass over three billion native speakers around the world. These languages have diverse typologies, originate from many different language families, and are associated with varying amounts of available resources -- including what researchers typically characterize as high-resource as well as low-resource languages. Our dataset is designed to support the creation and evaluation of models for monolingual retrieval, where the queries and the corpora are in the same language. In total, we have gathered over 700k high-quality relevance judgments for around 77k queries over Wikipedia in these 18 languages, where all assessments have been performed by native speakers hired by our team. Our goal is to spur research that will improve retrieval across a continuum of languages, thus enhancing information access capabilities for diverse populations around the world, particularly those that have been traditionally underserved. This overview paper describes the dataset and baselines that we share with the community. The MIRACL website is live at http://miracl.ai/.

## 12-003 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- arXiv: 2310.11511  first public: 2023-10-17  latest: 2023-10-17  primary cat: cs.CL
- authors (5): Akari Asai; Zeqiu Wu; Yizhong Wang; Avirup Sil; Hannaneh Hajishirzi
- seed subtopic: 自反思检索增强; type: 原始研究; cross: []
- arXiv comment: 30 pages, 2 figures, 12 tables
- URLs on first pages of PDF: https://selfrag.github.io/
- pages: 30

ABSTRACT: Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation. We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (Self-RAG) that enhances an LM's quality and factuality through retrieval and self-reflection. Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks. Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models.

## 12-004 | Multilingual E5 Text Embeddings: A Technical Report
- arXiv: 2402.05672  first public: 2024-02-08  latest: 2024-02-08  primary cat: cs.CL
- authors (6): Liang Wang; Nan Yang; Xiaolong Huang; Linjun Yang; Rangan Majumder; Furu Wei
- seed subtopic: 多语言嵌入模型; type: 技术报告; cross: []
- arXiv comment: 6 pages
- URLs on first pages of PDF: https://github.com/microsoft/unilm/
- pages: 6

ABSTRACT: This technical report presents the training methodology and evaluation results of the open-source multilingual E5 text embedding models, released in mid-2023. Three embedding models of different sizes (small / base / large) are provided, offering a balance between the inference efficiency and embedding quality. The training procedure adheres to the English E5 model recipe, involving contrastive pre-training on 1 billion multilingual text pairs, followed by fine-tuning on a combination of labeled datasets. Additionally, we introduce a new instruction-tuned embedding model, whose performance is on par with state-of-the-art, English-only models of similar sizes. Information regarding the model release can be found at https://github.com/microsoft/unilm/tree/master/e5 .

## 12-005 | M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation
- arXiv: 2402.03216  first public: 2024-02-05  latest: 2025-12-12  primary cat: cs.CL
- authors (6): Jianlv Chen; Shitao Xiao; Peitian Zhang; Kun Luo; Defu Lian; Zheng Liu
- seed subtopic: 多语言嵌入模型; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/FlagOpen/FlagEmbedding https://huggingface.co/datasets/shibing624/nli-zh-all
- pages: 18

ABSTRACT: In this paper, we introduce a new embedding model called M3-Embedding, which is distinguished for its versatility in \textit{Multi-Linguality}, \textit{Multi-Functionality}, and \textit{Multi-Granularity}. It provides a uniform support for the semantic retrieval of more than 100 working languages. It can simultaneously accomplish the three common retrieval functionalities: dense retrieval, multi-vector retrieval, and sparse retrieval. Besides, it is also capable of processing inputs of different granularities, spanning from short sentences to long documents of up to 8,192 tokens. The effective training of M3-Embedding presents a series of technical contributions. Notably, we propose a novel self-knowledge distillation approach, where the relevance scores from different retrieval functionalities can be integrated as the teacher signal to enhance the training quality. We also optimize the batching strategy, which enables a large batch size and high training throughput to improve the discriminativeness of embeddings. M3-Embedding exhibits a superior performance in our experiment, leading to new state-of-the-art results on multilingual, cross-lingual, and long-document retrieval benchmarks.

## 12-006 | mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval
- arXiv: 2407.19669  first public: 2024-07-29  latest: 2024-10-14  primary cat: cs.CL
- authors (13): Xin Zhang; Yanzhao Zhang; Dingkun Long; Wen Xie; Ziqi Dai; Jialong Tang ...
- seed subtopic: 多语言嵌入与重排序; type: 原始研究; cross: []
- arXiv comment: Camera-ready version of EMNLP 2024: Industry Track
- pages: 20

ABSTRACT: We present systematic efforts in building long-context multilingual text representation model (TRM) and reranker from scratch for text retrieval. We first introduce a text encoder (base size) enhanced with RoPE and unpadding, pre-trained in a native 8192-token context (longer than 512 of previous multilingual encoders). Then we construct a hybrid TRM and a cross-encoder reranker by contrastive learning. Evaluations show that our text encoder outperforms the same-sized previous state-of-the-art XLM-R. Meanwhile, our TRM and reranker match the performance of large-sized state-of-the-art BGE-M3 models and achieve better results on long-context retrieval benchmarks. Further analysis demonstrate that our proposed models exhibit higher efficiency during both training and inference. We believe their efficiency and effectiveness could benefit various researches and industrial applications.

## 12-007 | jina-embeddings-v3: Multilingual Embeddings With Task LoRA
- arXiv: 2409.10173  first public: 2024-09-16  latest: 2024-09-19  primary cat: cs.CL
- authors (11): Saba Sturua; Isabelle Mohr; Mohammad Kalim Akram; Michael Günther; Bo Wang; Markus Krimmel ...
- seed subtopic: 多语言嵌入模型; type: 技术报告; cross: []
- arXiv comment: 20 pages, pp11-13 references, pp14-20 appendix and experiment tables
- pages: 20

ABSTRACT: We introduce jina-embeddings-v3, a novel text embedding model with 570 million parameters, achieves state-of-the-art performance on multilingual data and long-context retrieval tasks, supporting context lengths of up to 8192 tokens. The model includes a set of task-specific Low-Rank Adaptation (LoRA) adapters to generate high-quality embeddings for query-document retrieval, clustering, classification, and text matching. Evaluation on the MTEB benchmark shows that jina-embeddings-v3 outperforms the latest proprietary embeddings from OpenAI and Cohere on English tasks, while achieving superior performance compared to multilingual-e5-large-instruct across all multilingual tasks. With a default output dimension of 1024, users can flexibly reduce the embedding dimensions to as low as 32 without compromising performance, enabled by Matryoshka Representation Learning.

## 12-008 | Arctic-Embed 2.0: Multilingual Retrieval Without Compromise
- arXiv: 2412.04506  first public: 2024-12-03  latest: 2024-12-14  primary cat: cs.CL
- authors (4): Puxuan Yu; Luke Merrick; Gaurav Nuti; Daniel Campos
- seed subtopic: 多语言嵌入模型; type: 技术报告; cross: []
- arXiv comment: 10 pages, 5 figures, 3 tables
- URLs on first pages of PDF: https://huggingface.co/dunzhang/stella_en_1.5B_v5
- pages: 10

ABSTRACT: This paper presents the training methodology of Arctic-Embed 2.0, a set of open-source text embedding models built for accurate and efficient multilingual retrieval. While prior works have suffered from degraded English retrieval quality, Arctic-Embed 2.0 delivers competitive retrieval quality on multilingual and English-only benchmarks, and supports Matryoshka Representation Learning (MRL) for efficient embedding storage with significantly lower compressed quality degradation compared to alternatives. We detail the design and implementation, presenting several important open research questions that arose during model development. We conduct experiments exploring these research questions and include extensive discussion aimed at fostering further discussion in this field.

## 12-009 | Gemini Embedding: Generalizable Embeddings from Gemini
- arXiv: 2503.07891  first public: 2025-03-10  latest: 2025-03-10  primary cat: cs.CL
- authors (47): Jinhyuk Lee; Feiyang Chen; Sahil Dua; Daniel Cer; Madhuri Shanbhogue; Iftekhar Naim ...
- seed subtopic: LLM 初始化嵌入; type: 技术报告; cross: []
- arXiv comment: 19 pages
- URLs on first pages of PDF: https://huggingface.co/spaces/mteb/leaderboard
- pages: 19

ABSTRACT: In this report, we introduce Gemini Embedding, a state-of-the-art embedding model leveraging the power of Gemini, Google's most capable large language model. Capitalizing on Gemini's inherent multilingual and code understanding capabilities, Gemini Embedding produces highly generalizable embeddings for text spanning numerous languages and textual modalities. The representations generated by Gemini Embedding can be precomputed and applied to a variety of downstream tasks including classification, similarity, clustering, ranking, and retrieval. Evaluated on the Massive Multilingual Text Embedding Benchmark (MMTEB), which includes over one hundred tasks across 250+ languages, Gemini Embedding substantially outperforms prior state-of-the-art models, demonstrating considerable improvements in embedding quality. Achieving state-of-the-art performance across MMTEB's multilingual, English, and code benchmarks, our unified model demonstrates strong capabilities across a broad selection of tasks and surpasses specialized domain-specific models.

## 12-010 | Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- arXiv: 2506.05176  first public: 2025-06-05  latest: 2025-06-11  primary cat: cs.CL
- authors (12): Yanzhao Zhang; Mingxin Li; Dingkun Long; Xin Zhang; Huan Lin; Baosong Yang ...
- seed subtopic: LLM 嵌入与重排序; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen3-Embedding https://huggingface.co/Qwen
- pages: 14

ABSTRACT: In this work, we introduce the Qwen3 Embedding series, a significant advancement over its predecessor, the GTE-Qwen series, in text embedding and reranking capabilities, built upon the Qwen3 foundation models. Leveraging the Qwen3 LLMs' robust capabilities in multilingual text understanding and generation, our innovative multi-stage training pipeline combines large-scale unsupervised pre-training with supervised fine-tuning on high-quality datasets. Effective model merging strategies further ensure the robustness and adaptability of the Qwen3 Embedding series. During the training process, the Qwen3 LLMs serve not only as backbone models but also play a crucial role in synthesizing high-quality, rich, and diverse training data across multiple domains and languages, thus enhancing the training pipeline. The Qwen3 Embedding series offers a spectrum of model sizes (0.6B, 4B, 8B) for both embedding and reranking tasks, addressing diverse deployment scenarios where users can optimize for either efficiency or effectiveness. Empirical evaluations demonstrate that the Qwen3 Embedding series achieves state-of-the-art results across diverse benchmarks. Notably, it excels on the multilingual evaluation benchmark MTEB for text embedding, as well as in various retrieval tasks, including code retrieval, cross-lingual retrieval and multilingual retrieval. To facilitate reproducibility and promote community-driven research and development, the Qwen3 Embedding models are publicly available under the Apache 2.0 license.

## 12-011 | EmbeddingGemma: Powerful and Lightweight Text Representations
- arXiv: 2509.20354  first public: 2025-09-24  latest: 2025-11-01  primary cat: cs.CL
- authors (89): Henrique Schechter Vera; Sahil Dua; Biao Zhang; Daniel Salz; Ryan Mullins; Sindhu Raghuram Panyam ...
- seed subtopic: 轻量多语言嵌入; type: 技术报告; cross: ['16']
- arXiv comment: 18 pages. Models are available in HuggingFace (at https://huggingface.co/collections/google/embeddinggemma-68b9ae3a72a82f0562a80dc4), Kaggle (at https://www.kaggle.com/models/google/embeddinggemma/), and Vertex AI (at https://pantheon.corp.google.com/vertex-ai/publishers/google/model-garden/embeddinggemma)
- URLs on first pages of PDF: https://huggingface.co/spaces/mteb/leaderboard
- pages: 18

ABSTRACT: We introduce EmbeddingGemma, a new lightweight, open text embedding model based on the Gemma 3 language model family. Our innovative training recipe strategically captures knowledge from larger models via encoder-decoder initialization and geometric embedding distillation. We improve model robustness and expressiveness with a spread-out regularizer, and ensure generalizability by merging checkpoints from varied, optimized mixtures. Evaluated on the Massive Text Embedding Benchmark (MTEB) across multilingual, English, and code domains, EmbeddingGemma (300M) achieves state-of-the-art results. Notably, it outperforms prior top models, both proprietary and open, with fewer than 500M parameters, and provides performance comparable to models double its size, offering an exceptional performance-to-cost ratio. Remarkably, this lead persists when quantizing model weights or truncating embedding outputs. This makes EmbeddingGemma particularly well-suited for low-latency and high-throughput use cases such as on-device applications. We provide ablation studies exploring our key design choices. We release EmbeddingGemma to the community to promote further research.

## 12-012 | Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks
- arXiv: 2511.07025  first public: 2025-11-10  latest: 2025-11-10  primary cat: cs.CL
- authors (8): Yauhen Babakhin; Radek Osmulski; Ronay Ak; Gabriel Moreira; Mengyao Xu; Benedikt Schifferer ...
- seed subtopic: 多语言与跨语言嵌入; type: 技术报告; cross: []
- URLs on first pages of PDF: https://huggingface.co/nvidia/llama-embed-nemotron-8b
- pages: 20

ABSTRACT: We introduce llama-embed-nemotron-8b, an open-weights text embedding model that achieves state-of-the-art performance on the Multilingual Massive Text Embedding Benchmark (MMTEB) leaderboard as of October 21, 2025. While recent models show strong performance, their training data or methodologies are often not fully disclosed. We aim to address this by developing a fully open-source model, publicly releasing its weights and detailed ablation studies, and planning to share the curated training datasets. Our model demonstrates superior performance across all major embedding tasks -- including retrieval, classification and semantic textual similarity (STS) -- and excels in challenging multilingual scenarios, such as low-resource languages and cross-lingual setups. This state-of-the-art performance is driven by a novel data mix of 16.1 million query-document pairs, split between 7.7 million samples from public datasets and 8.4 million synthetically generated examples from various open-weight LLMs. One of our key contributions is a detailed ablation study analyzing core design choices, including a comparison of contrastive loss implementations, an evaluation of synthetic data generation (SDG) strategies, and the impact of model merging. The llama-embed-nemotron-8b is an instruction-aware model, supporting user-defined instructions to enhance performance for specific use-cases. This combination of top-tier performance, broad applicability, and user-driven flexibility enables it to serve as a universal text embedding solution.

## 12-013 | LUSIFER: Language Universal Space Integration for Enhanced Multilingual Embeddings with Large Language Models
- arXiv: 2501.00874  first public: 2025-01-01  latest: 2025-05-07  primary cat: cs.CL
- authors (6): Hieu Man; Nghia Trung Ngo; Viet Dac Lai; Ryan A. Rossi; Franck Dernoncourt; Thien Huu Nguyen
- seed subtopic: 零样本多语言嵌入迁移; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/hieum98/lusifer
- pages: 15

ABSTRACT: Recent advancements in large language models (LLMs) based embedding models have established new state-of-the-art benchmarks for text embedding tasks, particularly in dense vector-based retrieval. However, these models predominantly focus on English, leaving multilingual embedding capabilities largely unexplored. To address this limitation, we present LUSIFER, a novel zero-shot approach that adapts LLM-based embedding models for multilingual tasks without requiring multilingual supervision. LUSIFER's architecture combines a multilingual encoder, serving as a language-universal learner, with an LLM-based embedding model optimized for embedding-specific tasks. These components are seamlessly integrated through a minimal set of trainable parameters that act as a connector, effectively transferring the multilingual encoder's language understanding capabilities to the specialized embedding model. Additionally, to comprehensively evaluate multilingual embedding performance, we introduce a new benchmark encompassing 5 primary embedding tasks, 123 diverse datasets, and coverage across 14 languages. Extensive experimental results demonstrate that LUSIFER significantly enhances the multilingual performance across various embedding tasks, particularly for medium and low-resource languages, without requiring explicit multilingual training data.

## 12-014 | MMTEB: Massive Multilingual Text Embedding Benchmark
- arXiv: 2502.13595  first public: 2025-02-19  latest: 2025-11-13  primary cat: cs.CL
- authors (86): Kenneth Enevoldsen; Isaac Chung; Imene Kerboua; Márton Kardos; Ashwin Mathur; David Stap ...
- seed subtopic: 多语言嵌入评测; type: 基准与数据集; cross: ['15']
- arXiv comment: Accepted for ICLR: https://openreview.net/forum?id=zl3pfz4VCV
- URLs on first pages of PDF: https://github.com/embeddings-benchmark/mteb https://huggingface.co/spaces/mteb/leaderboard
- pages: 57

ABSTRACT: Text embeddings are typically evaluated on a limited set of tasks, which are constrained by language, domain, and task diversity. To address these limitations and provide a more comprehensive evaluation, we introduce the Massive Multilingual Text Embedding Benchmark (MMTEB) - a large-scale, community-driven expansion of MTEB, covering over 500 quality-controlled evaluation tasks across 250+ languages. MMTEB includes a diverse set of challenging, novel tasks such as instruction following, long-document retrieval, and code retrieval, representing the largest multilingual collection of evaluation tasks for embedding models to date. Using this collection, we develop several highly multilingual benchmarks, which we use to evaluate a representative set of models. We find that while large language models (LLMs) with billions of parameters can achieve state-of-the-art performance on certain language subsets and task categories, the best-performing publicly available model is multilingual-e5-large-instruct with only 560 million parameters. To facilitate accessibility and reduce computational cost, we introduce a novel downsampling method based on inter-task correlation, ensuring a diverse selection while preserving relative model rankings. Furthermore, we optimize tasks such as retrieval by sampling hard negatives, creating smaller but effective splits. These optimizations allow us to introduce benchmarks that drastically reduce computational demands. For instance, our newly introduced zero-shot English benchmark maintains a ranking order similar to the full-scale version but at a fraction of the computational cost.

## 12-015 | Improving Text Embeddings with Large Language Models
- arXiv: 2401.00368  first public: 2023-12-31  latest: 2024-05-31  primary cat: cs.CL
- authors (6): Liang Wang; Nan Yang; Xiaolong Huang; Linjun Yang; Rangan Majumder; Furu Wei
- seed subtopic: LLM 合成数据训练嵌入; type: 原始研究; cross: ['09']
- arXiv comment: Accepted by ACL 2024
- pages: 20

ABSTRACT: In this paper, we introduce a novel and simple method for obtaining high-quality text embeddings using only synthetic data and less than 1k training steps. Unlike existing methods that often depend on multi-stage intermediate pre-training with billions of weakly-supervised text pairs, followed by fine-tuning with a few labeled datasets, our method does not require building complex training pipelines or relying on manually collected datasets that are often constrained by task diversity and language coverage. We leverage proprietary LLMs to generate diverse synthetic data for hundreds of thousands of text embedding tasks across 93 languages. We then fine-tune open-source decoder-only LLMs on the synthetic data using standard contrastive loss. Experiments demonstrate that our method achieves strong performance on highly competitive text embedding benchmarks without using any labeled data. Furthermore, when fine-tuned with a mixture of synthetic and labeled data, our model sets new state-of-the-art results on the BEIR and MTEB benchmarks.

## 12-016 | Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever
- arXiv: 2408.16672  first public: 2024-08-29  latest: 2024-09-14  primary cat: cs.IR
- authors (10): Rohan Jha; Bo Wang; Michael Günther; Georgios Mastrapas; Saba Sturua; Isabelle Mohr ...
- seed subtopic: 多语言多向量检索; type: 原始研究; cross: []
- arXiv comment: 8 pages, references at pp7,8; EMNLP workshop submission
- pages: 8

ABSTRACT: Multi-vector dense models, such as ColBERT, have proven highly effective in information retrieval. ColBERT's late interaction scoring approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval models, thanks to its bi-encoder architecture and recent optimizations in indexing and search. In this work we propose a number of incremental improvements to the ColBERT model architecture and training pipeline, using methods shown to work in the more mature single-vector embedding model training paradigm, particularly those that apply to heterogeneous multilingual data or boost efficiency with little tradeoff. Our new model, Jina-ColBERT-v2, demonstrates strong performance across a range of English and multilingual retrieval tasks.

## 12-017 | ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval
- arXiv: 2402.15059  first public: 2024-02-23  latest: 2024-02-23  primary cat: cs.CL
- authors (4): Antoine Louis; Vageesh Saxena; Gijs van Dijck; Gerasimos Spanakis
- seed subtopic: 模块化零样本多语言检索; type: 原始研究; cross: []
- arXiv comment: Under review. Code is available at https://github.com/ant-louis/xm-retrievers
- pages: 13

ABSTRACT: State-of-the-art neural retrievers predominantly focus on high-resource languages like English, which impedes their adoption in retrieval scenarios involving other languages. Current approaches circumvent the lack of high-quality labeled data in non-English languages by leveraging multilingual pretrained language models capable of cross-lingual transfer. However, these models require substantial task-specific fine-tuning across multiple languages, often perform poorly in languages with minimal representation in the pretraining corpus, and struggle to incorporate new languages after the pretraining phase. In this work, we present a novel modular dense retrieval model that learns from the rich data of a single high-resource language and effectively zero-shot transfers to a wide array of languages, thereby eliminating the need for language-specific labeled data. Our model, ColBERT-XM, demonstrates competitive performance against existing state-of-the-art multilingual retrievers trained on more extensive datasets in various languages. Further analysis reveals that our modular approach is highly data-efficient, effectively adapts to out-of-distribution data, and significantly reduces energy consumption and carbon emissions. By demonstrating its proficiency in zero-shot scenarios, ColBERT-XM marks a shift towards more sustainable and inclusive retrieval systems, enabling effective information accessibility in numerous languages. We publicly release our code and models for the community.

## 12-018 | Training Sparse Mixture Of Experts Text Embedding Models
- arXiv: 2502.07972  first public: 2025-02-11  latest: 2025-03-09  primary cat: cs.CL
- authors (2): Zach Nussbaum; Brandon Duderstadt
- seed subtopic: MoE 多语言嵌入; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/nomic-ai/contrastors
- pages: 12

ABSTRACT: Transformer-based text embedding models have improved their performance on benchmarks like MIRACL and BEIR by increasing their parameter counts. However, this scaling approach introduces significant deployment challenges, including increased inference latency and memory usage. These challenges are particularly severe in retrieval-augmented generation (RAG) applications, where large models' increased memory requirements constrain dataset ingestion capacity, and their higher latency directly impacts query-time performance. While causal language models have addressed similar efficiency challenges using Mixture of Experts (MoE) architectures, this approach hasn't been successfully adapted to the general text embedding setting. In this paper, we introduce Nomic Embed v2, the first general purpose MoE text embedding model. Our model outperforms models in the same parameter class on both monolingual and multilingual benchmarks while also maintaining competitive performance with models twice its size. We open-source all code, models, and evaluation data to ensure full reproducibility of our training pipeline at \href{https://github.com/nomic-ai/contrastors}{https://github.com/nomic-ai/contrastors}.

## 12-019 | Optimized Text Embedding Models and Benchmarks for Amharic Passage Retrieval
- arXiv: 2505.19356  first public: 2025-05-25  latest: 2025-06-10  primary cat: cs.IR
- authors (3): Kidist Amde Mekonnen; Yosef Worku Alemneh; Maarten de Rijke
- seed subtopic: 阿姆哈拉语检索嵌入; type: 原始研究; cross: []
- arXiv comment: 10 pages (excl. refs/appendix), 10 figures. Accepted to ACL 2025 Findings. Kidist and Yosef contributed equally to this work. Public resources: https://github.com/kidist-amde/amharic-ir-benchmarks
- URLs on first pages of PDF: https://github.com/kidist-amde/ https://huggingface.co/datasets/rasyosef/ https://huggingface.co/spaces/mteb/
- pages: 18

ABSTRACT: Neural retrieval methods using transformer-based pre-trained language models have advanced multilingual and cross-lingual retrieval. However, their effectiveness for low-resource, morphologically rich languages such as Amharic remains underexplored due to data scarcity and suboptimal tokenization. We address this gap by introducing Amharic-specific dense retrieval models based on pre-trained Amharic BERT and RoBERTa backbones. Our proposed RoBERTa-Base-Amharic-Embed model (110M parameters) achieves a 17.6% relative improvement in MRR@10 and a 9.86% gain in Recall@10 over the strongest multilingual baseline, Arctic Embed 2.0 (568M parameters). More compact variants, such as RoBERTa-Medium-Amharic-Embed (42M), remain competitive while being over 13x smaller. Additionally, we train a ColBERT-based late interaction retrieval model that achieves the highest MRR@10 score (0.843) among all evaluated models. We benchmark our proposed models against both sparse and dense retrieval baselines to systematically assess retrieval effectiveness in Amharic. Our analysis highlights key challenges in low-resource settings and underscores the importance of language-specific adaptation. To foster future research in low-resource IR, we publicly release our dataset, codebase, and trained models at https://github.com/kidist-amde/amharic-ir-benchmarks.

## 12-020 | MINERS: Multilingual Language Models as Semantic Retrievers
- arXiv: 2406.07424  first public: 2024-06-11  latest: 2024-09-24  primary cat: cs.CL
- authors (3): Genta Indra Winata; Ruochen Zhang; David Ifeoluwa Adelani
- seed subtopic: 多语言语义检索评测; type: 基准与数据集; cross: []
- arXiv comment: Accepted by EMNLP 2024 Findings
- URLs on first pages of PDF: https://github.com/gentaiscool/miners
- pages: 25

ABSTRACT: Words have been represented in a high-dimensional vector space that encodes their semantic similarities, enabling downstream applications such as retrieving synonyms, antonyms, and relevant contexts. However, despite recent advances in multilingual language models (LMs), the effectiveness of these models' representations in semantic retrieval contexts has not been comprehensively explored. To fill this gap, this paper introduces the MINERS, a benchmark designed to evaluate the ability of multilingual LMs in semantic retrieval tasks, including bitext mining and classification via retrieval-augmented contexts. We create a comprehensive framework to assess the robustness of LMs in retrieving samples across over 200 diverse languages, including extremely low-resource languages in challenging cross-lingual and code-switching settings. Our results demonstrate that by solely retrieving semantically similar embeddings yields performance competitive with state-of-the-art approaches, without requiring any fine-tuning.

## 12-021 | Zero-Shot Cross-Lingual Reranking with Large Language Models for Low-Resource Languages
- arXiv: 2312.16159  first public: 2023-12-26  latest: 2023-12-26  primary cat: cs.IR
- authors (4): Mofetoluwa Adeyemi; Akintunde Oladipo; Ronak Pradeep; Jimmy Lin
- seed subtopic: 低资源语言 LLM 重排序; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/CIRAL/ https://huggingface.co/facebook/nllb-200-1.3B
- pages: 6

ABSTRACT: Large language models (LLMs) have shown impressive zero-shot capabilities in various document reranking tasks. Despite their successful implementations, there is still a gap in existing literature on their effectiveness in low-resource languages. To address this gap, we investigate how LLMs function as rerankers in cross-lingual information retrieval (CLIR) systems for African languages. Our implementation covers English and four African languages (Hausa, Somali, Swahili, and Yoruba) and we examine cross-lingual reranking with queries in English and passages in the African languages. Additionally, we analyze and compare the effectiveness of monolingual reranking using both query and document translations. We also evaluate the effectiveness of LLMs when leveraging their own generated translations. To get a grasp of the effectiveness of multiple LLMs, our study focuses on the proprietary models RankGPT-4 and RankGPT-3.5, along with the open-source model, RankZephyr. While reranking remains most effective in English, our results reveal that cross-lingual reranking may be competitive with reranking in African languages depending on the multilingual capability of the LLM.

## 12-022 | Translate-Distill: Learning Cross-Language Dense Retrieval by Translation and Distillation
- arXiv: 2401.04810  first public: 2024-01-09  latest: 2024-01-09  primary cat: cs.IR
- authors (5): Eugene Yang; Dawn Lawrie; James Mayfield; Douglas W. Oard; Scott Miller
- seed subtopic: 翻译蒸馏跨语言检索; type: 原始研究; cross: []
- arXiv comment: 17 pages, 1 figure, accepted at ECIR 2024
- URLs on first pages of PDF: https://github.com/hltcoe/ColBERT-X/tree/plaid-x https://huggingface.co/collections/hltcoe/
- pages: 17

ABSTRACT: Prior work on English monolingual retrieval has shown that a cross-encoder trained using a large number of relevance judgments for query-document pairs can be used as a teacher to train more efficient, but similarly effective, dual-encoder student models. Applying a similar knowledge distillation approach to training an efficient dual-encoder model for Cross-Language Information Retrieval (CLIR), where queries and documents are in different languages, is challenging due to the lack of a sufficiently large training collection when the query and document languages differ. The state of the art for CLIR thus relies on translating queries, documents, or both from the large English MS MARCO training set, an approach called Translate-Train. This paper proposes an alternative, Translate-Distill, in which knowledge distillation from either a monolingual cross-encoder or a CLIR cross-encoder is used to train a dual-encoder CLIR student model. This richer design space enables the teacher model to perform inference in an optimized setting, while training the student model directly for CLIR. Trained models and artifacts are publicly available on Huggingface.

## 12-023 | Leveraging LLMs for Synthesizing Training Data Across Many Languages in Multilingual Dense Retrieval
- arXiv: 2311.05800  first public: 2023-11-10  latest: 2024-04-15  primary cat: cs.IR
- authors (6): Nandan Thakur; Jianmo Ni; Gustavo Hernández Ábrego; John Wieting; Jimmy Lin; Daniel Cer
- seed subtopic: 合成多语言检索数据; type: 原始研究; cross: ['09']
- arXiv comment: Accepted at NAACL 2024. Data released at https://github.com/google-research-datasets/swim-ir
- pages: 26

ABSTRACT: There has been limited success for dense retrieval models in multilingual retrieval, due to uneven and scarce training data available across multiple languages. Synthetic training data generation is promising (e.g., InPars or Promptagator), but has been investigated only for English. Therefore, to study model capabilities across both cross-lingual and monolingual retrieval tasks, we develop SWIM-IR, a synthetic retrieval training dataset containing 33 (high to very-low resource) languages for fine-tuning multilingual dense retrievers without requiring any human supervision. To construct SWIM-IR, we propose SAP (summarize-then-ask prompting), where the large language model (LLM) generates a textual summary prior to the query generation step. SAP assists the LLM in generating informative queries in the target language. Using SWIM-IR, we explore synthetic fine-tuning of multilingual dense retrieval models and evaluate them robustly on three retrieval benchmarks: XOR-Retrieve (cross-lingual), MIRACL (monolingual) and XTREME-UP (cross-lingual). Our models, called SWIM-X, are competitive with human-supervised dense retrieval models, e.g., mContriever-X, finding that SWIM-IR can cheaply substitute for expensive human-labeled retrieval training data. SWIM-IR dataset and SWIM-X models are available at https://github.com/google-research-datasets/SWIM-IR.

## 12-024 | What are the limits of cross-lingual dense passage retrieval for low-resource languages?
- arXiv: 2408.11942  first public: 2024-08-21  latest: 2024-08-21  primary cat: cs.IR
- authors (3): Jie Wu; Zhaochun Ren; Suzan Verberne
- seed subtopic: 低资源语言跨语言稠密检索; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/Susheel-1999/Sentence_ https://github.com/google-deepmind/xquad https://github.com/iapp-technology/ https://github.com/xhluca/dl-translate
- pages: 14

ABSTRACT: In this paper, we analyze the capabilities of the multi-lingual Dense Passage Retriever (mDPR) for extremely low-resource languages. In the Cross-lingual Open-Retrieval Answer Generation (CORA) pipeline, mDPR achieves success on multilingual open QA benchmarks across 26 languages, of which 9 were unseen during training. These results are promising for Question Answering (QA) for low-resource languages. We focus on two extremely low-resource languages for which mDPR performs poorly: Amharic and Khmer. We collect and curate datasets to train mDPR models using Translation Language Modeling (TLM) and question--passage alignment. We also investigate the effect of our extension on the language distribution in the retrieval results. Our results on the MKQA and AmQA datasets show that language alignment brings improvements to mDPR for the low-resource languages, but the improvements are modest and the results remain low. We conclude that fulfilling CORA's promise to enable multilingual open QA in extremely low-resource settings is challenging because the model, the data, and the evaluation approach are intertwined. Hence, all three need attention in follow-up work. We release our code for reproducibility and future work: https://anonymous.4open.science/r/Question-Answering-for-Low-Resource-Languages-B13C/

## 12-025 | NeuCLIRBench: A Modern Evaluation Collection for Monolingual, Cross-Language, and Multilingual Information Retrieval
- arXiv: 2511.14758  first public: 2025-11-18  latest: 2025-11-18  primary cat: cs.IR
- authors (9): Dawn Lawrie; James Mayfield; Eugene Yang; Andrew Yates; Sean MacAvaney; Ronak Pradeep ...
- seed subtopic: 跨语言检索评测集; type: 基准与数据集; cross: []
- arXiv comment: 14 pages, 1 figure
- URLs on first pages of PDF: https://github.com/codelucas/ https://huggingface.co/datasets/
- pages: 14

ABSTRACT: To measure advances in retrieval, test collections with relevance judgments that can faithfully distinguish systems are required. This paper presents NeuCLIRBench, an evaluation collection for cross-language and multilingual retrieval. The collection consists of documents written natively in Chinese, Persian, and Russian, as well as those same documents machine translated into English. The collection supports several retrieval scenarios including: monolingual retrieval in English, Chinese, Persian, or Russian; cross-language retrieval with English as the query language and one of the other three languages as the document language; and multilingual retrieval, again with English as the query language and relevant documents in all three languages. NeuCLIRBench combines the TREC NeuCLIR track topics of 2022, 2023, and 2024. The 250,128 judgments across approximately 150 queries for the monolingual and cross-language tasks and 100 queries for multilingual retrieval provide strong statistical discriminatory power to distinguish retrieval approaches. A fusion baseline of strong neural retrieval systems is included with the collection so that developers of reranking algorithms are no longer reliant on BM25 as their first-stage retriever. NeuCLIRBench is publicly available.

## 12-026 | Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs
- arXiv: 2510.00908  first public: 2025-10-01  latest: 2025-10-01  primary cat: cs.IR
- authors (3): Roksana Goworek; Olivia Macmillan-Scott; Eda B. Özyiğit
- seed subtopic: 跨语言检索综述; type: 综述; cross: []
- pages: 57

ABSTRACT: Cross-lingual information retrieval (CLIR) addresses the challenge of retrieving relevant documents written in languages different from that of the original query. Research in this area has typically framed the task as monolingual retrieval augmented by translation, treating retrieval methods and cross-lingual capabilities in isolation. Both monolingual and cross-lingual retrieval usually follow a pipeline of query expansion, ranking, re-ranking and, increasingly, question answering. Recent advances, however, have shifted from translation-based methods toward embedding-based approaches and leverage multilingual large language models (LLMs), for which aligning representations across languages remains a central challenge. The emergence of cross-lingual embeddings and multilingual LLMs has introduced a new paradigm, offering improved retrieval performance and enabling answer generation. This survey provides a comprehensive overview of developments from early translation-based methods to state-of-the-art embedding-driven and generative techniques. It presents a structured account of core CLIR components, evaluation practices, and available resources. Persistent challenges such as data imbalance and linguistic variation are identified, while promising directions are suggested for advancing equitable and effective cross-lingual information retrieval. By situating CLIR within the broader landscape of information retrieval and multilingual language processing, this work not only reviews current capabilities but also outlines future directions for building retrieval systems that are robust, inclusive, and adaptable.

## 12-027 | The Multilingual Curse at the Retrieval Layer: Evidence from Amharic
- arXiv: 2605.24556  first public: 2026-05-23  latest: 2026-05-23  primary cat: cs.IR
- authors (3): Yosef Worku Alemneh; Kidist Amde Mekonnen; Maarten de Rijke
- seed subtopic: 低资源语言检索层诅咒; type: 原始研究; cross: []
- arXiv comment: 10 pages, 4 tables. Accepted to the 1st Workshop on Multilinguality in the Era of Large Language Models (MeLLM) at ACL 2026
- URLs on first pages of PDF: https://github.com/rasyosef/
- pages: 10

ABSTRACT: Multilingual retrieval increasingly underpins cross-lingual question answering and retrieval-augmented generation. Strong zero-shot scores on multilingual benchmarks are often taken as evidence that current encoders transfer reliably across many languages. We argue that this assumption breaks down for underrepresented, morphologically rich languages, and use Amharic as a diagnostic case. Under a shared passage retrieval protocol covering dense, late-interaction, learned sparse, and cross-encoder paradigms, we compare zero-shot multilingual retrievers, Amharic-fine-tuned multilingual retrievers, and monolingual Amharic retrievers. The strongest zero-shot multilingual retriever underperforms the strongest monolingual Amharic first-stage retriever by 23% relative MRR@10. Fine-tuning two recent multilingual embedding models on the same Amharic supervision yields 32-60% relative MRR@10 gains over zero-shot, but the best Amharic-fine-tuned multilingual model remains below the strongest monolingual Amharic retriever. These findings indicate that zero-shot multilingual retrieval is not a sufficient proxy for equitable information access in the LLM era: for underrepresented languages, retrieval must be evaluated and adapted in-language rather than inferred from aggregate multilingual benchmarks. To foster future research, we publicly release the dataset, codebase, and trained models at https://github.com/rasyosef/amharic-neural-ir.

## 12-028 | "Knowing When You Don't Know": A Multilingual Relevance Assessment Dataset for Robust Retrieval-Augmented Generation
- arXiv: 2312.11361  first public: 2023-12-18  latest: 2024-11-10  primary cat: cs.CL
- authors (11): Nandan Thakur; Luiz Bonifacio; Xinyu Zhang; Odunayo Ogundepo; Ehsan Kamalloo; David Alfonso-Hermelo ...
- seed subtopic: 多语言 RAG 鲁棒性评测; type: 基准与数据集; cross: []
- arXiv comment: EMNLP 2024 (Findings)
- URLs on first pages of PDF: https://github.com/project-miracl/nomiracl
- pages: 19

ABSTRACT: Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) output by leveraging external knowledge sources to reduce factual hallucinations. However, prior work lacks a comprehensive evaluation of different language families, making it challenging to evaluate LLM robustness against errors in external retrieved knowledge. To overcome this, we establish NoMIRACL, a human-annotated dataset for evaluating LLM robustness in RAG across 18 typologically diverse languages. NoMIRACL includes both a non-relevant and a relevant subset. Queries in the non-relevant subset contain passages judged as non-relevant, whereas queries in the relevant subset include at least a single judged relevant passage. We measure relevance assessment using: (i) hallucination rate, measuring model tendency to hallucinate, when the answer is not present in passages in the non-relevant subset, and (ii) error rate, measuring model inaccuracy to recognize relevant passages in the relevant subset.In our work, we observe that most models struggle to balance the two capacities. Models such as LLAMA-2 and Orca-2 achieve over 88% hallucination rate on the non-relevant subset. Mistral and LLAMA-3 hallucinate less but can achieve up to a 74.9% error rate on the relevant subset. Overall, GPT-4 is observed to provide the best tradeoff on both subsets, highlighting future work necessary to improve LLM robustness. NoMIRACL dataset and evaluation code are available at: https://github.com/project-miracl/nomiracl.

## 12-029 | Retrieval-augmented generation in multilingual settings
- arXiv: 2407.01463  first public: 2024-07-01  latest: 2024-07-01  primary cat: cs.CL
- authors (6): Nadezhda Chirkova; David Rau; Hervé Déjean; Thibault Formal; Stéphane Clinchant; Vassilina Nikoulina
- seed subtopic: 多语言 RAG 基线; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/naver/bergen https://github.com/naver/bergen/blob/main/documentations/multilingual.md https://github.com/naver/bergen1
- pages: 12

ABSTRACT: Retrieval-augmented generation (RAG) has recently emerged as a promising solution for incorporating up-to-date or domain-specific knowledge into large language models (LLMs) and improving LLM factuality, but is predominantly studied in English-only settings. In this work, we consider RAG in the multilingual setting (mRAG), i.e. with user queries and the datastore in 13 languages, and investigate which components and with which adjustments are needed to build a well-performing mRAG pipeline, that can be used as a strong baseline in future works. Our findings highlight that despite the availability of high-quality off-the-shelf multilingual retrievers and generators, task-specific prompt engineering is needed to enable generation in user languages. Moreover, current evaluation metrics need adjustments for multilingual setting, to account for variations in spelling named entities. The main limitations to be addressed in future works include frequent code-switching in non-Latin alphabet languages, occasional fluency errors, wrong reading of the provided documents, or irrelevant retrieval. We release the code for the resulting mRAG baseline pipeline at https://github.com/naver/bergen.

## 12-030 | Not All Languages are Equal: Insights into Multilingual Retrieval-Augmented Generation
- arXiv: 2410.21970  first public: 2024-10-29  latest: 2024-10-29  primary cat: cs.CL
- authors (8): Suhang Wu; Jialong Tang; Baosong Yang; Ante Wang; Kaidi Jia; Jiawei Yu ...
- seed subtopic: 多语言 RAG 评测; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/H-shw/
- pages: 15

ABSTRACT: RALMs (Retrieval-Augmented Language Models) broaden their knowledge scope by incorporating external textual resources. However, the multilingual nature of global knowledge necessitates RALMs to handle diverse languages, a topic that has received limited research focus. In this work, we propose \textit{Futurepedia}, a carefully crafted benchmark containing parallel texts across eight representative languages. We evaluate six multilingual RALMs using our benchmark to explore the challenges of multilingual RALMs. Experimental results reveal linguistic inequalities: 1) high-resource languages stand out in Monolingual Knowledge Extraction; 2) Indo-European languages lead RALMs to provide answers directly from documents, alleviating the challenge of expressing answers across languages; 3) English benefits from RALMs' selection bias and speaks louder in multilingual knowledge selection. Based on these findings, we offer advice for improving multilingual Retrieval Augmented Generation. For monolingual knowledge extraction, careful attention must be paid to cascading errors from translating low-resource languages into high-resource ones. In cross-lingual knowledge transfer, encouraging RALMs to provide answers within documents in different languages can improve transfer performance. For multilingual knowledge selection, incorporating more non-English documents and repositioning English documents can help mitigate RALMs' selection bias. Through comprehensive experiments, we underscore the complexities inherent in multilingual RALMs and offer valuable insights for future research.

## 12-031 | Investigating Language Preference of Multilingual RAG Systems
- arXiv: 2502.11175  first public: 2025-02-16  latest: 2025-06-01  primary cat: cs.CL
- authors (2): Jeonghyun Park; Hwanhee Lee
- seed subtopic: 多语言 RAG 语言偏好; type: 原始研究; cross: []
- arXiv comment: ACL 2025 Findings
- URLs on first pages of PDF: https://github.com/jeonghyunpark2002/ https://huggingface.co/datasets/facebook/
- pages: 31

ABSTRACT: Multilingual Retrieval-Augmented Generation (mRAG) systems enhance language models by integrating external multilingual information to produce context-aware responses. However, mRAG systems struggle with retrieving relevant information due to linguistic variations between queries and documents, generating inconsistent responses when multilingual sources conflict. In this work, we systematically investigate language preferences in both retrieval and generation of mRAG through a series of experiments. Our analysis indicates that retrievers tend to prefer high-resource and query languages, yet this preference does not consistently improve generation performance. Moreover, we observe that generators prefer the query language or Latin scripts, leading to inconsistent outputs. To overcome these issues, we propose Dual Knowledge Multilingual RAG (DKM-RAG), a simple yet effective framework that fuses translated multilingual passages with complementary model knowledge. Empirical results demonstrate that DKM-RAG mitigates language preference in generation and enhances performance across diverse linguistic settings. Code is available at https://github.com/jeonghyunpark2002/LanguagePreference.git

## 12-032 | MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems
- arXiv: 2410.13716  first public: 2024-10-17  latest: 2025-03-29  primary cat: cs.CL
- authors (5): Nandan Thakur; Suleman Kazi; Ge Luo; Jimmy Lin; Amin Ahmad
- seed subtopic: 多语言 RAG 评测; type: 基准与数据集; cross: ['15']
- arXiv comment: Accepted at NAACL 2025 (Main Conference)
- pages: 25

ABSTRACT: Traditional retrieval-augmented generation (RAG) benchmarks evaluate systems using heuristic-based metrics, but these require human preferences as the ground truth for reference. In contrast, arena-based benchmarks, where systems compete against each other, require an expensive large language model (LLM) as a judge for a reliable evaluation. We present a simple efficient technique to combine the best of both worlds. The idea is to train a surrogate judge using heuristic metrics as input, to output the LLM as a judge prediction. In our work, we develop MIRAGE-Bench, a synthetic arena-based RAG benchmark for 18 diverse languages on Wikipedia focused on multilingual answer generation evaluation. It extensively couples both heuristic features and LLM as a judge for evaluation. We benchmark 19 multilingual LLMs, and observe a high correlation (Kendall Tau ($τ$) = 0.909) using our surrogate judge and between GPT-4o as a teacher using the Bradley-Terry framework. Our results show proprietary and large open-source LLMs currently dominate on MIRAGE-Bench. Our code and datasets are made publicly available here: https://github.com/vectara/mirage-bench.

## 12-033 | MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation
- arXiv: 2502.17163  first public: 2025-02-24  latest: 2025-07-19  primary cat: cs.CL
- authors (6): María Andrea Cruz Blandón; Jayasimha Talur; Bruno Charron; Dong Liu; Saab Mansour; Marcello Federico
- seed subtopic: 多语言 RAG 元评测; type: 基准与数据集; cross: ['15']
- arXiv comment: ACL 2025
- URLs on first pages of PDF: https://github.com/amazon-science/ https://huggingface.co/datasets/miracl/miracl
- pages: 19

ABSTRACT: Automatic evaluation of retrieval augmented generation (RAG) systems relies on fine-grained dimensions like faithfulness and relevance, as judged by expert human annotators. Meta-evaluation benchmarks support the development of automatic evaluators that correlate well with human judgement. However, existing benchmarks predominantly focus on English or use translated data, which fails to capture cultural nuances. A native approach provides a better representation of the end user experience. In this work, we develop a Multilingual End-to-end Meta-Evaluation RAG benchmark (MEMERAG). Our benchmark builds on the popular MIRACL dataset, using native-language questions and generating responses with diverse large language models (LLMs), which are then assessed by expert annotators for faithfulness and relevance. We describe our annotation process and show that it achieves high inter-annotator agreement. We then analyse the performance of the answer-generating LLMs across languages as per the human evaluators. Finally we apply the dataset to our main use-case which is to benchmark multilingual automatic evaluators (LLM-as-a-judge). We show that our benchmark can reliably identify improvements offered by advanced prompting techniques and LLMs. Our dataset is available at https://github.com/amazon-science/MEMERAG

## 12-034 | Multilingual Retrieval Augmented Generation for Culturally-Sensitive Tasks: A Benchmark for Cross-lingual Robustness
- arXiv: 2410.01171  first public: 2024-10-02  latest: 2025-06-22  primary cat: cs.CL
- authors (10): Bryan Li; Fiona Luo; Samar Haider; Adwait Agashe; Tammy Li; Runqi Liu ...
- seed subtopic: 跨语言 RAG 文化敏感问题; type: 基准与数据集; cross: []
- arXiv comment: ACL 2025 (Findings)
- pages: 28

ABSTRACT: The paradigm of retrieval-augmented generated (RAG) helps mitigate hallucinations of large language models (LLMs). However, RAG also introduces biases contained within the retrieved documents. These biases can be amplified in scenarios which are multilingual and culturally-sensitive, such as territorial disputes. We thus introduce BordIRLines, a dataset of territorial disputes paired with retrieved Wikipedia documents, across 49 languages. We evaluate the cross-lingual robustness of this RAG setting by formalizing several modes for multilingual retrieval. Our experiments on several LLMs show that incorporating perspectives from diverse languages can in fact improve robustness; retrieving multilingual documents best improves response consistency and decreases geopolitical bias over RAG with purely in-language documents. We also consider how RAG responses utilize presented documents, finding a much wider variance in the linguistic distribution of response citations, when querying in low-resource languages. Our further analyses investigate the various aspects of a cross-lingual RAG pipeline, from retrieval to document contents. We release our benchmark and code to support continued research towards equitable information access across languages at https://huggingface.co/datasets/borderlines/bordirlines.

## 12-035 | XRAG: Cross-lingual Retrieval-Augmented Generation
- arXiv: 2505.10089  first public: 2025-05-15  latest: 2025-05-15  primary cat: cs.CL
- authors (5): Wei Liu; Sony Trenous; Leonardo F. R. Ribeiro; Bill Byrne; Felix Hieber
- seed subtopic: 跨语言 RAG 基准; type: 基准与数据集; cross: []
- pages: 20

ABSTRACT: We propose XRAG, a novel benchmark designed to evaluate the generation abilities of LLMs in cross-lingual Retrieval-Augmented Generation (RAG) settings where the user language does not match the retrieval results. XRAG is constructed from recent news articles to ensure that its questions require external knowledge to be answered. It covers the real-world scenarios of monolingual and multilingual retrieval, and provides relevancy annotations for each retrieved document. Our novel dataset construction pipeline results in questions that require complex reasoning, as evidenced by the significant gap between human and LLM performance. Consequently, XRAG serves as a valuable benchmark for studying LLM reasoning abilities, even before considering the additional cross-lingual complexity. Experimental results on five LLMs uncover two previously unreported challenges in cross-lingual RAG: 1) in the monolingual retrieval setting, all evaluated models struggle with response language correctness; 2) in the multilingual retrieval setting, the main challenge lies in reasoning over retrieved information across languages rather than generation of non-English text.

## 12-036 | Multilingual Retrieval-Augmented Generation for Knowledge-Intensive Task
- arXiv: 2504.03616  first public: 2025-04-04  latest: 2025-10-03  primary cat: cs.CL
- authors (3): Leonardo Ranaldi; Barry Haddow; Alexandra Birch
- seed subtopic: 多语言 RAG 策略; type: 原始研究; cross: []
- journal_ref: 2026.findings-eacl.35
- doi: 10.18653/v1/2026.findings-eacl.35
- URLs on first pages of PDF: https://huggingface.co/Cohere/Cohere-embed-
- pages: 16

ABSTRACT: Retrieval-augmented generation (RAG) has become a cornerstone of contemporary NLP, enhancing large language models (LLMs) by allowing them to access richer factual contexts through in-context retrieval. While effective in monolingual settings, especially in English, its use in multilingual tasks remains unexplored. This paper investigates the effectiveness of RAG across multiple languages by proposing novel approaches for multilingual open-domain question-answering. We evaluate the performance of various multilingual RAG strategies, including question-translation (tRAG), which translates questions into English before retrieval, and Multilingual RAG (MultiRAG), where retrieval occurs directly across multiple languages. Our findings reveal that tRAG, while useful, suffers from limited coverage. In contrast, MultiRAG improves efficiency by enabling multilingual retrieval but introduces inconsistencies due to cross-lingual variations in the retrieved content. To address these issues, we propose Crosslingual RAG (CrossRAG), a method that translates retrieved documents into a common language (e.g., English) before generating the response. Our experiments show that CrossRAG significantly enhances performance on knowledge-intensive tasks, benefiting both high-resource and low-resource languages.

## 12-037 | On the Consistency of Multilingual Context Utilization in Retrieval-Augmented Generation
- arXiv: 2504.00597  first public: 2025-04-01  latest: 2025-11-10  primary cat: cs.CL
- authors (3): Jirui Qi; Raquel Fernández; Arianna Bisazza
- seed subtopic: 多语言上下文利用; type: 原始研究; cross: []
- arXiv comment: Best Paper Award at MRL Workshop 2025, colocated with EMNLP 2025. All codes and data are released at https://github.com/Betswish/mRAG-Context-Consistency
- doi: 10.18653/v1/2025.mrl-main.15
- URLs on first pages of PDF: https://github.com/B https://huggingface.co/Cohere/Cohere-embed-m https://huggingface.co/datasets/wikimedia/wi
- pages: 27

ABSTRACT: Retrieval-augmented generation (RAG) with large language models (LLMs) has demonstrated strong performance in multilingual question-answering (QA) tasks by leveraging relevant passages retrieved from corpora. In multilingual RAG (mRAG), the retrieved passages can be written in languages other than that of the query entered by the user, making it challenging for LLMs to effectively utilize the provided information. Recent research suggests that retrieving passages from multilingual corpora can improve RAG performance, particularly for low-resource languages. However, the extent to which LLMs can leverage different kinds of multilingual contexts to generate accurate answers, *independently from retrieval quality*, remains understudied. In this paper, we conduct an extensive assessment of LLMs' ability to (i) make consistent use of a relevant passage regardless of its language, (ii) respond in the expected language, and (iii) focus on the relevant passage even when multiple `distracting' passages in different languages are provided in the context. Our experiments with four LLMs across three QA datasets covering a total of 48 languages reveal a surprising ability of LLMs to extract the relevant information from passages in a different language than the query, but a much weaker ability to formulate a full answer in the correct language. Our analysis, based on both accuracy and feature attribution techniques, further shows that distracting passages negatively impact answer quality regardless of their language. However, distractors in the query language exert a slightly stronger influence. Taken together, our findings deepen the understanding of how LLMs utilize context in mRAG systems, providing directions for future improvements.

## 12-038 | Language Drift in Multilingual Retrieval-Augmented Generation: Characterization and Decoding-Time Mitigation
- arXiv: 2511.09984  first public: 2025-11-13  latest: 2025-11-13  primary cat: cs.CL
- authors (3): Bo Li; Zhenghua Xu; Rui Xie
- seed subtopic: 多语言 RAG 语言漂移; type: 原始研究; cross: []
- arXiv comment: AAAI'26, Oral Paper
- URLs on first pages of PDF: https://github.com/baidu/DuReader https://github.com/pkuserc/SCD
- pages: 14

ABSTRACT: Multilingual Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to perform knowledge-intensive tasks in multilingual settings by leveraging retrieved documents as external evidence. However, when the retrieved evidence differs in language from the user query and in-context exemplars, the model often exhibits language drift by generating responses in an unintended language. This phenomenon is especially pronounced during reasoning-intensive decoding, such as Chain-of-Thought (CoT) generation, where intermediate steps introduce further language instability. In this paper, we systematically study output language drift in multilingual RAG across multiple datasets, languages, and LLM backbones. Our controlled experiments reveal that the drift results not from comprehension failure but from decoder-level collapse, where dominant token distributions and high-frequency English patterns dominate the intended generation language. We further observe that English serves as a semantic attractor under cross-lingual conditions, emerging as both the strongest interference source and the most frequent fallback language. To mitigate this, we propose Soft Constrained Decoding (SCD), a lightweight, training-free decoding strategy that gently steers generation toward the target language by penalizing non-target-language tokens. SCD is model-agnostic and can be applied to any generation algorithm without modifying the architecture or requiring additional data. Experiments across three multilingual datasets and multiple typologically diverse languages show that SCD consistently improves language alignment and task performance, providing an effective and generalizable solution in multilingual RAG.

## 12-039 | The Cross-Lingual Cost: Retrieval Biases in RAG over Arabic-English Corpora
- arXiv: 2507.07543  first public: 2025-07-10  latest: 2025-10-27  primary cat: cs.CL
- authors (5): Chen Amiraz; Yaroslav Fyodorov; Elad Haramaty; Zohar Karnin; Liane Lewin-Eytan
- seed subtopic: 跨语言检索偏差; type: 原始研究; cross: []
- arXiv comment: Accepted to ArabicNLP 2025
- URLs on first pages of PDF: https://huggingface.co/BAAI/ https://huggingface.co/BAAI/bge-m3 https://huggingface.co/Qwen/Qwen2 https://huggingface.co/intfloat/
- pages: 15

ABSTRACT: Cross-lingual retrieval-augmented generation (RAG) is a critical capability for retrieving and generating answers across languages. Prior work in this context has mostly focused on generation and relied on benchmarks derived from open-domain sources, most notably Wikipedia. In such settings, retrieval challenges often remain hidden due to language imbalances, overlap with pretraining data, and memorized content. To address this gap, we study Arabic-English RAG in a domain-specific setting using benchmarks derived from real-world corporate datasets. Our benchmarks include all combinations of languages for the user query and the supporting document, drawn independently and uniformly at random. This enables a systematic study of multilingual retrieval behavior. Our findings reveal that retrieval is a critical bottleneck in cross-lingual domain-specific scenarios, with substantial performance drops occurring when the user query and supporting document languages differ. A key insight is that these failures stem primarily from the retriever's difficulty in ranking documents across languages. Finally, we propose two simple retrieval strategies that address this source of failure by enforcing equal retrieval from both languages or by translating the query, resulting in substantial improvements in cross-lingual and overall performance. These results highlight meaningful opportunities for improving multilingual retrieval, particularly in practical, real-world RAG applications.

## 12-040 | Crosslingual Retrieval Augmented In-context Learning for Bangla
- arXiv: 2311.00587  first public: 2023-11-01  latest: 2023-12-02  primary cat: cs.CL
- authors (3): Xiaoqian Li; Ercong Nie; Sheng Liang
- seed subtopic: 孟加拉语跨语言检索增强; type: 原始研究; cross: []
- arXiv comment: In The 1st Bangla Language Processing (BLP) Workshop, held in conjunction with The Conference on Empirical Methods in Natural Language Processing (EMNLP), December 2023
- pages: 15

ABSTRACT: The promise of Large Language Models (LLMs) in Natural Language Processing has often been overshadowed by their limited performance in low-resource languages such as Bangla. To address this, our paper presents a pioneering approach that utilizes cross-lingual retrieval augmented in-context learning. By strategically sourcing semantically similar prompts from high-resource language, we enable multilingual pretrained language models (MPLMs), especially the generative model BLOOMZ, to successfully boost performance on Bangla tasks. Our extensive evaluation highlights that the cross-lingual retrieval augmented prompts bring steady improvements to MPLMs over the zero-shot performance.

## 12-041 | Faux Polyglot: A Study on Information Disparity in Multilingual Large Language Models
- arXiv: 2407.05502  first public: 2024-07-07  latest: 2025-02-11  primary cat: cs.CL
- authors (3): Nikhil Sharma; Kenton Murray; Ziang Xiao
- seed subtopic: 多语言信息偏好; type: 原始研究; cross: []
- arXiv comment: NAACL 2025
- doi: 10.18653/v1/2025.naacl-long.411
- pages: 18

ABSTRACT: Although the multilingual capability of LLMs offers new opportunities to overcome the language barrier, do these capabilities translate into real-life scenarios where linguistic divide and knowledge conflicts between multilingual sources are known occurrences? In this paper, we studied LLM's linguistic preference in a cross-language RAG-based information search setting. We found that LLMs displayed systemic bias towards information in the same language as the query language in both document retrieval and answer generation. Furthermore, in scenarios where no information is in the language of the query, LLMs prefer documents in high-resource languages during generation, potentially reinforcing the dominant views. Such bias exists for both factual and opinion-based queries. Our results highlight the linguistic divide within multilingual LLMs in information search systems. The seemingly beneficial multilingual capability of LLMs may backfire on information parity by reinforcing language-specific information cocoons or filter bubbles further marginalizing low-resource views.

## 12-042 | CroSearch-R1: Better Leveraging Cross-lingual Knowledge for Retrieval-Augmented Generation
- arXiv: 2604.25182  first public: 2026-04-28  latest: 2026-04-28  primary cat: cs.CL
- authors (6): Rui Qi; Fengran Mo; Sijin Lu; Yufeng Chen; Jian-Yun Nie; Kaiyu Huang
- seed subtopic: 跨语言搜索智能体; type: 原始研究; cross: []
- arXiv comment: Accepted to SIGIR 2026 (Short Paper)
- URLs on first pages of PDF: https://huggingface.co/datasets/wikimedia/wikipedia
- pages: 7

ABSTRACT: A multilingual collection may contain useful knowledge in other languages to supplement and correct the facts in the original language for Retrieval-Augmented Generation (RAG). However, the vanilla approach that simply concatenates multiple pieces of knowledge from different languages into the context may fail to improve effectiveness due to the potential disparities across languages. To better leverage multilingual knowledge, we propose CroSearch-R1, a search-augmented reinforcement learning framework to integrate multilingual knowledge into the Group Relative Policy Optimization (GRPO) process. In particular, the approach adopts a multi-turn retrieval strategy with cross-lingual knowledge integration to dynamically align the knowledge from other languages as supplementary evidence into a unified representation space. Furthermore, we introduce a multilingual rollout mechanism to optimize reasoning transferability across languages. Experimental results demonstrate that our framework effectively leverages cross-lingual complementarity and improves the effectiveness of RAG with multilingual collections.

## 12-043 | XProvence: Zero-Cost Multilingual Context Pruning for Retrieval-Augmented Generation
- arXiv: 2601.18886  first public: 2026-01-26  latest: 2026-01-26  primary cat: cs.IR
- authors (4): Youssef Mohamed; Mohamed Elhoseiny; Thibault Formal; Nadezhda Chirkova
- seed subtopic: 多语言上下文剪枝; type: 原始研究; cross: []
- arXiv comment: Accepted to ECIR 2026
- URLs on first pages of PDF: https://github.com/naver/bergen/tree/ https://github.com/naver/bergen/tree/main/ https://github.com/naver/bergen/tree/main/scripts/xprovence https://huggingface.co/naver/xprovence-reranker-bgem3-v2
- pages: 7

ABSTRACT: This paper introduces XProvence, a multilingual zero-cost context pruning model for retrieval-augmented generation (RAG), trained on 16 languages and supporting 100+ languages through effective cross-lingual transfer. Motivated by the growing use of RAG systems across diverse languages, we explore several strategies to generalize the Provence framework-which first integrated efficient zero-cost context pruning directly into the re-ranking model-beyond English. Across four multilingual question answering benchmarks, we show how XProvence can prune RAG contexts with minimal-to-no performance degradation and outperforms strong baselines. Our model is available at https://huggingface.co/naver/xprovence-reranker-bgem3-v2.

## 12-044 | Quality-Aware Translation Tagging in Multilingual RAG system
- arXiv: 2510.23070  first public: 2025-10-27  latest: 2025-10-27  primary cat: cs.CL
- authors (3): Hoyeon Moon; Byeolhee Kim; Nikhil Verma
- seed subtopic: 翻译质量标注 RAG; type: 原始研究; cross: []
- arXiv comment: EMNLP 2025 MRL Workshop
- pages: 17

ABSTRACT: Multilingual Retrieval-Augmented Generation (mRAG) often retrieves English documents and translates them into the query language for low-resource settings. However, poor translation quality degrades response generation performance. Existing approaches either assume sufficient translation quality or utilize the rewriting method, which introduces factual distortion and hallucinations. To mitigate these problems, we propose Quality-Aware Translation Tagging in mRAG (QTT-RAG), which explicitly evaluates translation quality along three dimensions-semantic equivalence, grammatical accuracy, and naturalness&fluency-and attach these scores as metadata without altering the original content. We evaluate QTT-RAG against CrossRAG and DKM-RAG as baselines in two open-domain QA benchmarks (XORQA, MKQA) using six instruction-tuned LLMs ranging from 2.4B to 14B parameters, covering two low-resource languages (Korean and Finnish) and one high-resource language (Chinese). QTT-RAG outperforms the baselines by preserving factual integrity while enabling generator models to make informed decisions based on translation reliability. This approach allows for effective usage of cross-lingual documents in low-resource settings with limited native language documents, offering a practical and robust solution across multilingual domains.

## 12-045 | mRAKL: Multilingual Retrieval-Augmented Knowledge Graph Construction for Low-Resourced Languages
- arXiv: 2507.16011  first public: 2025-07-21  latest: 2025-07-21  primary cat: cs.CL
- authors (5): Hellina Hailu Nigatu; Min Li; Maartje ter Hoeve; Saloni Potdar; Sarah Chasins
- seed subtopic: 低资源语言知识图谱构建; type: 原始研究; cross: []
- arXiv comment: Accepted to Findings of ACL 2025
- pages: 18

ABSTRACT: Knowledge Graphs represent real-world entities and the relationships between them. Multilingual Knowledge Graph Construction (mKGC) refers to the task of automatically constructing or predicting missing entities and links for knowledge graphs in a multilingual setting. In this work, we reformulate the mKGC task as a Question Answering (QA) task and introduce mRAKL: a Retrieval-Augmented Generation (RAG) based system to perform mKGC. We achieve this by using the head entity and linking relation in a question, and having our model predict the tail entity as an answer. Our experiments focus primarily on two low-resourced languages: Tigrinya and Amharic. We experiment with using higher-resourced languages Arabic and English for cross-lingual transfer. With a BM25 retriever, we find that the RAG-based approach improves performance over a no-context setting. Further, our ablation studies show that with an idealized retrieval system, mRAKL improves accuracy by 4.92 and 8.79 percentage points for Tigrinya and Amharic, respectively.

## 12-046 | Pre-training Cross-lingual Open Domain Question Answering with Large-scale Synthetic Supervision
- arXiv: 2402.16508  first public: 2024-02-26  latest: 2024-10-02  primary cat: cs.CL
- authors (3): Fan Jiang; Tom Drummond; Trevor Cohn
- seed subtopic: 跨语言开放域问答预训练; type: 原始研究; cross: []
- arXiv comment: EMNLP 2024 Main
- pages: 28

ABSTRACT: Cross-lingual open domain question answering (CLQA) is a complex problem, comprising cross-lingual retrieval from a multilingual knowledge base, followed by answer generation in the query language. Both steps are usually tackled by separate models, requiring substantial annotated datasets, and typically auxiliary resources, like machine translation systems to bridge between languages. In this paper, we show that CLQA can be addressed using a single encoder-decoder model. To effectively train this model, we propose a self-supervised method based on exploiting the cross-lingual link structure within Wikipedia. We demonstrate how linked Wikipedia pages can be used to synthesise supervisory signals for cross-lingual retrieval, through a form of cloze query, and generate more natural questions to supervise answer generation. Together, we show our approach, \texttt{CLASS}, outperforms comparable methods on both supervised and zero-shot language adaptation settings, including those using machine translation.

## 12-047 | Even Small Reasoners Should Quote Their Sources: Introducing the Pleias-RAG Model Family
- arXiv: 2504.18225  first public: 2025-04-25  latest: 2026-10-05  primary cat: cs.CL
- authors (9): Pierre-Carl Langlais; Pavel Chizhov; Mattia Nee; Carlos Rosas-Hinostroza; Matthieu Delsart; Irène Girard ...
- seed subtopic: 带引用的小模型 RAG; type: 技术报告; cross: []
- pages: 19

ABSTRACT: We introduce a new generation of small reasoning models for RAG, search, and source summarization. Pleias-RAG-350m and Pleias-RAG-1B are mid-trained on a large synthetic dataset emulating the retrieval of a wide variety of multilingual open sources from the Common Corpus. They provide native support for citation and grounding with literal quotes and reintegrate multiple features associated with RAG workflows, such as query routing, query reformulation, and source reranking. Pleias-RAG-350m and Pleias-RAG-1B outperform SLMs below 4 billion parameters on standardized RAG benchmarks (HotPotQA, 2wiki) and are competitive with popular larger models, including Qwen-2.5-7B, Llama-3.1-8B, and Gemma-3-4B. They are the only SLMs to date maintaining consistent RAG performance across leading European languages and ensuring systematic reference grounding for statements. Due to their size and ease of deployment on constrained infrastructure and higher factuality by design, the models unlock a range of new use cases for generative AI.

## 12-048 | OCR Hinders RAG: Evaluating the Cascading Impact of OCR on Retrieval-Augmented Generation
- arXiv: 2412.02592  first public: 2024-12-03  latest: 2025-08-30  primary cat: cs.CV
- authors (9): Junyuan Zhang; Qintong Zhang; Bin Wang; Linke Ouyang; Zichen Wen; Ying Li ...
- seed subtopic: OCR 对 RAG 的影响; type: 基准与数据集; cross: []
- arXiv comment: Accepted by ICCV 2025
- pages: 31

ABSTRACT: Retrieval-augmented Generation (RAG) enhances Large Language Models (LLMs) by integrating external knowledge to reduce hallucinations and incorporate up-to-date information without retraining. As an essential part of RAG, external knowledge bases are commonly built by extracting structured data from unstructured PDF documents using Optical Character Recognition (OCR). However, given the imperfect prediction of OCR and the inherent non-uniform representation of structured data, knowledge bases inevitably contain various OCR noises. In this paper, we introduce OHRBench, the first benchmark for understanding the cascading impact of OCR on RAG systems. OHRBench includes 8,561 carefully selected unstructured document images from seven real-world RAG application domains, along with 8,498 Q&A pairs derived from multimodal elements in documents, challenging existing OCR solutions used for RAG. To better understand OCR's impact on RAG systems, we identify two primary types of OCR noise: Semantic Noise and Formatting Noise and apply perturbation to generate a set of structured data with varying degrees of each OCR noise. Using OHRBench, we first conduct a comprehensive evaluation of current OCR solutions and reveal that none is competent for constructing high-quality knowledge bases for RAG systems. We then systematically evaluate the impact of these two noise types and demonstrate the trend relationship between the degree of OCR noise and RAG performance. Our OHRBench, including PDF documents, Q&As, and the ground truth structured data are released at: https://github.com/opendatalab/OHR-Bench

## 12-050 | PaddleOCR 3.0 Technical Report
- arXiv: 2507.05595  first public: 2025-07-08  latest: 2025-07-08  primary cat: cs.CV
- authors (19): Cheng Cui; Ting Sun; Manhui Lin; Tingquan Gao; Yubo Zhang; Jiaxuan Liu ...
- seed subtopic: 多语言 OCR 工具链; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/PaddlePaddle/PaddleOCR https://huggingface.co/PaddlePaddle https://paddlepaddle.github.io/PaddleOCR
- pages: 24

ABSTRACT: This technical report introduces PaddleOCR 3.0, an Apache-licensed open-source toolkit for OCR and document parsing. To address the growing demand for document understanding in the era of large language models, PaddleOCR 3.0 presents three major solutions: (1) PP-OCRv5 for multilingual text recognition, (2) PP-StructureV3 for hierarchical document parsing, and (3) PP-ChatOCRv4 for key information extraction. Compared to mainstream vision-language models (VLMs), these models with fewer than 100 million parameters achieve competitive accuracy and efficiency, rivaling billion-parameter VLMs. In addition to offering a high-quality OCR model library, PaddleOCR 3.0 provides efficient tools for training, inference, and deployment, supports heterogeneous hardware acceleration, and enables developers to easily build intelligent document applications.

## 12-051 | MDPBench: A Benchmark for Multilingual Document Parsing in Real-World Scenarios
- arXiv: 2603.28130  first public: 2026-03-30  latest: 2026-03-30  primary cat: cs.CV
- authors (10): Zhang Li; Zhibo Lin; Qiang Liu; Ziyang Zhang; Shuo Zhang; Zidun Guo ...
- seed subtopic: 多语言文档解析评测; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/Yuliang-Liu/MultimodalOCR
- pages: 17

ABSTRACT: We introduce Multilingual Document Parsing Benchmark, the first benchmark for multilingual digital and photographed document parsing. Document parsing has made remarkable strides, yet almost exclusively on clean, digital, well-formatted pages in a handful of dominant languages. No systematic benchmark exists to evaluate how models perform on digital and photographed documents across diverse scripts and low-resource languages. MDPBench comprises 3,400 document images spanning 17 languages, diverse scripts, and varied photographic conditions, with high-quality annotations produced through a rigorous pipeline of expert model labeling, manual correction, and human verification. To ensure fair comparison and prevent data leakage, we maintain separate public and private evaluation splits. Our comprehensive evaluation of both open-source and closed-source models uncovers a striking finding: while closed-source models (notably Gemini3-Pro) prove relatively robust, open-source alternatives suffer dramatic performance collapse, particularly on non-Latin scripts and real-world photographed documents, with an average drop of 17.8% on photographed documents and 14.0% on non-Latin scripts. These results reveal significant performance imbalances across languages and conditions, and point to concrete directions for building more inclusive, deployment-ready parsing systems. Source available at https://github.com/Yuliang-Liu/MultimodalOCR.

## 12-052 | Evaluating Robustness of LLMs in Question Answering on Multilingual Noisy OCR Data
- arXiv: 2502.16781  first public: 2025-02-24  latest: 2025-09-19  primary cat: cs.CL
- authors (5): Bhawna Piryani; Jamshid Mozafari; Abdelrahman Abdallah; Antoine Doucet; Adam Jatowt
- seed subtopic: 多语言 OCR 噪声问答; type: 基准与数据集; cross: []
- arXiv comment: Accepted at CIKM 2025
- URLs on first pages of PDF: https://github.com/DataScienceUIBK/MultiOCR-QA
- pages: 11

ABSTRACT: Optical Character Recognition (OCR) plays a crucial role in digitizing historical and multilingual documents, yet OCR errors - imperfect extraction of text, including character insertion, deletion, and substitution can significantly impact downstream tasks like question-answering (QA). In this work, we conduct a comprehensive analysis of how OCR-induced noise affects the performance of Multilingual QA Systems. To support this analysis, we introduce a multilingual QA dataset MultiOCR-QA, comprising 50K question-answer pairs across three languages, English, French, and German. The dataset is curated from OCR-ed historical documents, which include different levels and types of OCR noise. We then evaluate how different state-of-the-art Large Language Models (LLMs) perform under different error conditions, focusing on three major OCR error types. Our findings show that QA systems are highly prone to OCR-induced errors and perform poorly on noisy OCR text. By comparing model performance on clean versus noisy texts, we provide insights into the limitations of current approaches and emphasize the need for more noise-resilient QA systems in historical digitization contexts.

## 12-054 | Retrieval-augmented Multilingual Knowledge Editing
- arXiv: 2312.13040  first public: 2023-12-20  latest: 2023-12-20  primary cat: cs.CL
- authors (3): Weixuan Wang; Barry Haddow; Alexandra Birch
- seed subtopic: 检索增强多语言知识编辑; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/Vicky-Wil/ReMaKE
- pages: 20

ABSTRACT: Knowledge represented in Large Language Models (LLMs) is quite often incorrect and can also become obsolete over time. Updating knowledge via fine-tuning is computationally resource-hungry and not reliable, and so knowledge editing (KE) has developed as an effective and economical alternative to inject new knowledge or to fix factual errors in LLMs. Although there has been considerable interest in this area, current KE research exclusively focuses on the monolingual setting, typically in English. However, what happens if the new knowledge is supplied in one language, but we would like to query the LLM in a different language? To address the problem of multilingual knowledge editing, we propose Retrieval-augmented Multilingual Knowledge Editor (ReMaKE) to update new knowledge in LLMs. ReMaKE can perform model-agnostic knowledge editing in multilingual settings. ReMaKE concatenates the new knowledge retrieved from a multilingual knowledge base with prompts. Our experimental results show that ReMaKE outperforms baseline knowledge editing methods by a significant margin and is the first KE method to work in a multilingual setting. We provide our multilingual knowledge editing dataset (MzsRE) in 12 languages, which along with code, and additional project information is available at https://github.com/Vicky-Wil/ReMaKE.

## 12-055 | BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning
- arXiv: 2406.17764  first public: 2024-06-25  latest: 2025-05-31  primary cat: cs.CL
- authors (6): Ercong Nie; Bo Shao; Zifeng Ding; Mingyang Wang; Helmut Schmid; Hinrich Schütze
- seed subtopic: 跨语言知识编辑基准; type: 基准与数据集; cross: []
- arXiv comment: Accepted to ACL 2025
- pages: 18

ABSTRACT: This paper introduces BMIKE-53, a comprehensive benchmark for cross-lingual in-context knowledge editing (IKE) across 53 languages, unifying three knowledge editing (KE) datasets: zsRE, CounterFact, and WikiFactDiff. Cross-lingual KE, which requires knowledge edited in one language to generalize across others while preserving unrelated knowledge, remains underexplored. To address this gap, we systematically evaluate IKE under zero-shot, one-shot, and few-shot setups, incorporating tailored metric-specific demonstrations. Our findings reveal that model scale and demonstration alignment critically govern cross-lingual IKE efficacy, with larger models and tailored demonstrations significantly improving performance. Linguistic properties, particularly script type, strongly influence performance variation across languages, with non-Latin languages underperforming due to issues like language confusion. Code and data are publicly available at: https://github.com/ercong21/MultiKnow/.

## 12-056 | MLaKE: Multilingual Knowledge Editing Benchmark for Large Language Models
- arXiv: 2404.04990  first public: 2024-04-07  latest: 2025-02-19  primary cat: cs.CL
- authors (6): Zihao Wei; Jingcheng Deng; Liang Pang; Hanxing Ding; Huawei Shen; Xueqi Cheng
- seed subtopic: 多语言知识编辑基准; type: 基准与数据集; cross: []
- arXiv comment: Accepted as a full paper at COLING 2025
- pages: 17

ABSTRACT: The extensive utilization of large language models (LLMs) underscores the crucial necessity for precise and contemporary knowledge embedded within their intrinsic parameters. Existing research on knowledge editing primarily concentrates on monolingual scenarios, neglecting the complexities presented by multilingual contexts and multi-hop reasoning. To address these challenges, our study introduces MLaKE (Multilingual Language Knowledge Editing), a novel benchmark comprising 4072 multi-hop and 5360 single-hop questions designed to evaluate the adaptability of knowledge editing methods across five languages: English, Chinese, Japanese, French, and German. MLaKE aggregates fact chains from Wikipedia across languages and utilizes LLMs to generate questions in both free-form and multiple-choice. We evaluate the multilingual knowledge editing generalization capabilities of existing methods on MLaKE. Existing knowledge editing methods demonstrate higher success rates in English samples compared to other languages. However, their generalization capabilities are limited in multi-language experiments. Notably, existing knowledge editing methods often show relatively high generalization for languages within the same language family compared to languages from different language families. These results underscore the imperative need for advancements in multilingual knowledge editing and we hope MLaKE can serve as a valuable resource for benchmarking and solution development.

## 12-057 | Editing Across Languages: A Survey of Multilingual Knowledge Editing
- arXiv: 2505.14393  first public: 2025-05-20  latest: 2025-11-01  primary cat: cs.CL
- authors (3): Nadir Durrani; Basel Mousi; Fahim Dalvi
- seed subtopic: 多语言知识编辑综述; type: 综述; cross: []
- arXiv comment: Accepted at EMNLP 2025
- pages: 13

ABSTRACT: While Knowledge Editing has been extensively studied in monolingual settings, it remains underexplored in multilingual contexts. This survey systematizes recent research on Multilingual Knowledge Editing (MKE), a growing subdomain of model editing focused on ensuring factual edits generalize reliably across languages. We present a comprehensive taxonomy of MKE methods, covering parameter-based, memory-based, fine-tuning, and hypernetwork approaches. We survey available benchmarks,summarize key findings on method effectiveness and transfer patterns, identify challenges in cross-lingual propagation, and highlight open problems related to language anisotropy, evaluation coverage, and edit scalability. Our analysis consolidates a rapidly evolving area and lays the groundwork for future progress in editable language-aware LLMs.

## 12-058 | Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs
- arXiv: 2502.14645  first public: 2025-02-20  latest: 2025-05-23  primary cat: cs.CL
- authors (4): Yuchen Wu; Liang Ding; Li Shen; Dacheng Tao
- seed subtopic: 跨语言知识同步; type: 原始研究; cross: []
- arXiv comment: ACL 2025 Findings
- pages: 21

ABSTRACT: Knowledge editing allows for efficient adaptation of large language models (LLMs) to new information or corrections without requiring full retraining. However, prior methods typically focus on either single-language editing or basic multilingual editing, failing to achieve true cross-linguistic knowledge synchronization. To address this, we present a simple and practical state-of-the-art (SOTA) recipe Cross-Lingual Knowledge Democracy Edit (X-KDE), designed to propagate knowledge from a dominant language to other languages effectively. Our X-KDE comprises two stages: (i) Cross-lingual Edition Instruction Tuning (XE-IT), which fine-tunes the model on a curated parallel dataset to modify in-scope knowledge while preserving unrelated information, and (ii) Target-language Preference Optimization (TL-PO), which applies advanced optimization techniques to ensure consistency across languages, fostering the transfer of updates. Additionally, we contribute a high-quality, cross-lingual dataset, specifically designed to enhance knowledge transfer across languages. Extensive experiments on the Bi-ZsRE and MzsRE benchmarks show that X-KDE significantly enhances cross-lingual performance, achieving an average improvement of +8.19%, while maintaining high accuracy in monolingual settings.

## 12-059 | SemEval-2025 Task 7: Multilingual and Crosslingual Fact-Checked Claim Retrieval
- arXiv: 2505.10740  first public: 2025-05-15  latest: 2025-05-15  primary cat: cs.CL
- authors (10): Qiwei Peng; Robert Moro; Michal Gregor; Ivan Srba; Simon Ostermann; Marian Simko ...
- seed subtopic: 多语言事实核查声明检索; type: 基准与数据集; cross: []
- pages: 14

ABSTRACT: The rapid spread of online disinformation presents a global challenge, and machine learning has been widely explored as a potential solution. However, multilingual settings and low-resource languages are often neglected in this field. To address this gap, we conducted a shared task on multilingual claim retrieval at SemEval 2025, aimed at identifying fact-checked claims that match newly encountered claims expressed in social media posts across different languages. The task includes two subtracks: (1) a monolingual track, where social posts and claims are in the same language, and (2) a crosslingual track, where social posts and claims might be in different languages. A total of 179 participants registered for the task contributing to 52 test submissions. 23 out of 31 teams have submitted their system papers. In this paper, we report the best-performing systems as well as the most common and the most effective approaches across both subtracks. This shared task, along with its dataset and participating systems, provides valuable insights into multilingual claim retrieval and automated fact-checking, supporting future research in this field.

## 12-060 | AfrIFact: Cultural Information Retrieval, Evidence Extraction and Fact Checking for African Languages
- arXiv: 2604.00706  first public: 2026-04-01  latest: 2026-10-21  primary cat: cs.CL
- authors (19): Israel Abebe Azime; Jesujoba Oluwadara Alabi; Crystina Zhang; Iffat Maab; Atnafu Lambebo Tonja; Tadesse Destaw Belay ...
- seed subtopic: 非洲语言事实核查; type: 基准与数据集; cross: []
- arXiv comment: Accepted at 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)
- URLs on first pages of PDF: https://github.com/IsraelAbebe/ https://huggingface.co/collections/
- pages: 23

ABSTRACT: Assessing the veracity of a claim made online is a complex and important task with real-world implications. When these claims are directed at communities with limited access to information and the content concerns issues such as healthcare and culture, the consequences intensify, especially in low-resource languages. In this work, we introduce AfrIFact, a dataset that covers the necessary steps for automatic fact-checking (i.e., information retrieval, evidence extraction, and fact checking), in ten African languages and English. Our evaluation results show that even the best embedding models lack cross-lingual retrieval capabilities, and that cultural and news documents are easier to retrieve than healthcare-domain documents, both in large corpora and in single documents. We show that LLMs lack robust multilingual fact-verification capabilities in African languages, while few-shot prompting improves performance by up to 43% in AfriqueQwen-14B, and task-specific fine-tuning further improves fact-checking accuracy by up to 26%. These findings, along with our release of the AfrIFact dataset, encourage work on low-resource information retrieval, evidence retrieval, and fact checking.

## 12-061 | SemEval-2025 Task 3: Mu-SHROOM, the Multilingual Shared Task on Hallucinations and Related Observable Overgeneration Mistakes
- arXiv: 2504.11975  first public: 2025-04-16  latest: 2025-04-28  primary cat: cs.CL
- authors (18): Raúl Vázquez; Timothee Mickus; Elaine Zosa; Teemu Vahtola; Jörg Tiedemann; Aman Sinha ...
- seed subtopic: 多语言幻觉片段检测; type: 基准与数据集; cross: []
- arXiv comment: Mu-SHROOM is part of SemEval-2025 (Task 3). TBP: Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025)
- URLs on first pages of PDF: https://github.com/Helsinki-NLP/mu-shroom https://helsinki-nlp.github.io/shroom/2025 https://huggingface.co/datasets/Helsinki-NLP/
- pages: 26

ABSTRACT: We present the Mu-SHROOM shared task which is focused on detecting hallucinations and other overgeneration mistakes in the output of instruction-tuned large language models (LLMs). Mu-SHROOM addresses general-purpose LLMs in 14 languages, and frames the hallucination detection problem as a span-labeling task. We received 2,618 submissions from 43 participating teams employing diverse methodologies. The large number of submissions underscores the interest of the community in hallucination detection. We present the results of the participating systems and conduct an empirical analysis to identify key factors contributing to strong performance in this task. We also emphasize relevant current challenges, notably the varying degree of hallucinations across languages and the high annotator disagreement when labeling hallucination spans.

## 12-062 | Poly-FEVER: A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models
- arXiv: 2503.16541  first public: 2025-03-19  latest: 2025-03-26  primary cat: cs.CL
- authors (6): Hanzhi Zhang; Sumera Anjum; Heng Fan; Weijian Zheng; Yan Huang; Yunhe Feng
- seed subtopic: 多语言事实核验基准; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER
- pages: 10

ABSTRACT: Hallucinations in generative AI, particularly in Large Language Models (LLMs), pose a significant challenge to the reliability of multilingual applications. Existing benchmarks for hallucination detection focus primarily on English and a few widely spoken languages, lacking the breadth to assess inconsistencies in model performance across diverse linguistic contexts. To address this gap, we introduce Poly-FEVER, a large-scale multilingual fact verification benchmark specifically designed for evaluating hallucination detection in LLMs. Poly-FEVER comprises 77,973 labeled factual claims spanning 11 languages, sourced from FEVER, Climate-FEVER, and SciFact. It provides the first large-scale dataset tailored for analyzing hallucination patterns across languages, enabling systematic evaluation of LLMs such as ChatGPT and the LLaMA series. Our analysis reveals how topic distribution and web resource availability influence hallucination frequency, uncovering language-specific biases that impact model accuracy. By offering a multilingual benchmark for fact verification, Poly-FEVER facilitates cross-linguistic comparisons of hallucination detection and contributes to the development of more reliable, language-inclusive AI systems. The dataset is publicly available to advance research in responsible AI, fact-checking methodologies, and multilingual NLP, promoting greater transparency and robustness in LLM performance. The proposed Poly-FEVER is available at: https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER.

## 12-063 | Investigating Language and Retrieval Bias in Multilingual Previously Fact-Checked Claim Detection
- arXiv: 2509.25138  first public: 2025-09-29  latest: 2025-09-29  primary cat: cs.CL
- authors (7): Ivan Vykopal; Antonia Karamolegkou; Jaroslav Kopčan; Qiwei Peng; Tomáš Javůrek; Michal Gregor ...
- seed subtopic: 多语言核查检索偏差; type: 原始研究; cross: []
- pages: 22

ABSTRACT: Multilingual Large Language Models (LLMs) offer powerful capabilities for cross-lingual fact-checking. However, these models often exhibit language bias, performing disproportionately better on high-resource languages such as English than on low-resource counterparts. We also present and inspect a novel concept - retrieval bias, when information retrieval systems tend to favor certain information over others, leaving the retrieval process skewed. In this paper, we study language and retrieval bias in the context of Previously Fact-Checked Claim Detection (PFCD). We evaluate six open-source multilingual LLMs across 20 languages using a fully multilingual prompting strategy, leveraging the AMC-16K dataset. By translating task prompts into each language, we uncover disparities in monolingual and cross-lingual performance and identify key trends based on model family, size, and prompting strategy. Our findings highlight persistent bias in LLM behavior and offer recommendations for improving equity in multilingual fact-checking. To investigate retrieval bias, we employed multilingual embedding models and look into the frequency of retrieved claims. Our analysis reveals that certain claims are retrieved disproportionately across different posts, leading to inflated retrieval performance for popular claims while under-representing less common ones.

## 12-064 | Retrieval-Augmented Generation for Large Language Models: A Survey
- arXiv: 2312.10997  first public: 2023-12-18  latest: 2024-03-27  primary cat: cs.CL
- authors (10): Yunfan Gao; Yun Xiong; Xinyu Gao; Kangxiang Jia; Jinliu Pan; Yuxi Bi ...
- seed subtopic: RAG 综述; type: 综述; cross: []
- arXiv comment: Ongoing Work
- URLs on first pages of PDF: https://github.com/Tongji-KGLLM/
- pages: 21

ABSTRACT: Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

## 12-065 | Developing PUGG for Polish: A Modern Approach to KBQA, MRC, and IR Dataset Construction
- arXiv: 2408.02337  first public: 2024-08-05  latest: 2024-08-05  primary cat: cs.AI
- authors (7): Albert Sawczyn; Katsiaryna Viarenich; Konrad Wojtasik; Aleksandra Domogała; Marcin Oleksy; Maciej Piasecki ...
- seed subtopic: 小语种知识库问答数据; type: 基准与数据集; cross: []
- arXiv comment: Accepted for ACL 2024 (findings)
- URLs on first pages of PDF: https://github.com/CLARIN-PL/PUGG https://huggingface.co/datasets/clarin-pl/
- pages: 19

ABSTRACT: Advancements in AI and natural language processing have revolutionized machine-human language interactions, with question answering (QA) systems playing a pivotal role. The knowledge base question answering (KBQA) task, utilizing structured knowledge graphs (KG), allows for handling extensive knowledge-intensive questions. However, a significant gap exists in KBQA datasets, especially for low-resource languages. Many existing construction pipelines for these datasets are outdated and inefficient in human labor, and modern assisting tools like Large Language Models (LLM) are not utilized to reduce the workload. To address this, we have designed and implemented a modern, semi-automated approach for creating datasets, encompassing tasks such as KBQA, Machine Reading Comprehension (MRC), and Information Retrieval (IR), tailored explicitly for low-resource environments. We executed this pipeline and introduced the PUGG dataset, the first Polish KBQA dataset, and novel datasets for MRC and IR. Additionally, we provide a comprehensive implementation, insightful findings, detailed statistics, and evaluation of baseline models.
