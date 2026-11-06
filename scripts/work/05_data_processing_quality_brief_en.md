# Brief for annotation: 05 数据处理与质量

## 05-001 | MaskLID: Code-Switching Language Identification through Iterative Masking
- arXiv: 2406.06263  first public: 2024-06-10  latest: 2024-06-10  primary cat: cs.CL
- authors (3): Amir Hossein Kargaran; François Yvon; Hinrich Schütze
- seed subtopic: 语言识别; type: 原始研究; cross: []
- arXiv comment: ACL 2024
- pages: 11

ABSTRACT: We present MaskLID, a simple, yet effective, code-switching (CS) language identification (LID) method. MaskLID does not require any training and is designed to complement current high-performance sentence-level LIDs. Sentence-level LIDs are classifiers trained on monolingual texts to provide single labels, typically using a softmax layer to turn scores into probabilities. However, in cases where a sentence is composed in both L1 and L2 languages, the LID classifier often only returns the dominant label L1. To address this limitation, MaskLID employs a strategy to mask text features associated with L1, allowing the LID to classify the text as L2 in the next round. This method uses the LID itself to identify the features that require masking and does not rely on any external resource. In this work, we explore the use of MaskLID for two open-source LIDs (GlotLID and OpenLID), that are both based on the FastText architecture. Code and demo are available at https://github.com/cisnlp/MaskLID.

## 05-002 | ConLID: Supervised Contrastive Learning for Low-Resource Language Identification
- arXiv: 2506.15304  first public: 2025-06-18  latest: 2026-03-09  primary cat: cs.CL
- authors (4): Negar Foroutan; Jakhongir Saydaliev; Ye Eun Kim; Antoine Bosselut
- seed subtopic: 语言识别; type: 原始研究; cross: []
- arXiv comment: EACL 2026 - Main Conference
- URLs on first pages of PDF: https://github.com/epfl-nlp/ConLID https://huggingface.co/datasets/cis-lmu/
- pages: 16

ABSTRACT: Language identification (LID) is a critical step in curating multilingual LLM pretraining corpora from web crawls. While many studies on LID model training focus on collecting diverse training data to improve performance, low-resource languages -- often limited to single-domain data, such as the Bible -- continue to perform poorly. To resolve these imbalance and bias issues, we propose a novel supervised contrastive learning (SCL) approach to learn domain-invariant representations for low-resource languages. We show that our approach improves LID performance on out-of-domain data for low-resource languages by 3.2 percentage points, while maintaining its performance for the high-resource languages.

## 05-003 | Code-Switched Language Identification is Harder Than You Think
- arXiv: 2402.01505  first public: 2024-02-02  latest: 2024-02-02  primary cat: cs.CL
- authors (4): Laurie Burchell; Alexandra Birch; Robert P. Thompson; Kenneth Heafield
- seed subtopic: 语言识别; type: 原始研究; cross: []
- arXiv comment: EACL 2024
- URLs on first pages of PDF: https://github.com/cyb3rk0tik/pyfranc https://github.com/laurieburchell/ https://github.com/wooorm/franc
- pages: 13

ABSTRACT: Code switching (CS) is a very common phenomenon in written and spoken communication but one that is handled poorly by many natural language processing applications. Looking to the application of building CS corpora, we explore CS language identification (LID) for corpus building. We make the task more realistic by scaling it to more languages and considering models with simpler architectures for faster inference. We also reformulate the task as a sentence-level multi-label tagging problem to make it more tractable. Having defined the task, we investigate three reasonable models for this task and define metrics which better reflect desired performance. We present empirical evidence that no current approach is adequate and finally provide recommendations for future work in this area.

## 05-004 | A Shocking Amount of the Web is Machine Translated: Insights from Multi-Way Parallelism
- arXiv: 2401.05749  first public: 2024-01-11  latest: 2024-06-05  primary cat: cs.CL
- authors (5): Brian Thompson; Mehak Preet Dhaliwal; Peter Frisch; Tobias Domhan; Marcello Federico
- seed subtopic: 低资源语料审计; type: 原始研究; cross: ['04']
- arXiv comment: Accepted at ACL Findings 2024
- URLs on first pages of PDF: https://github.com/amazon-science/
- pages: 13

ABSTRACT: We show that content on the web is often translated into many languages, and the low quality of these multi-way translations indicates they were likely created using Machine Translation (MT). Multi-way parallel, machine generated content not only dominates the translations in lower resource languages; it also constitutes a large fraction of the total web content in those languages. We also find evidence of a selection bias in the type of content which is translated into many languages, consistent with low quality English content being translated en masse into many lower resource languages, via MT. Our work raises serious concerns about training models such as multilingual large language models on both monolingual and bilingual data scraped from the web.

## 05-005 | Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2
- arXiv: 2610.31636  first public: 2026-10-22  latest: 2026-10-22  primary cat: cs.CL
- authors (3): Marek Šuppa; Ivan Vykopal; Jaroslav Kopčan
- seed subtopic: 低资源语料审计; type: 原始研究; cross: []
- arXiv comment: Accepted to WaC Workshop at EMNLP 2026
- pages: 18

ABSTRACT: Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four phenomena. The largest is a machine-generated content farm of 1,408,437 documents (5.32%) that passed the pipeline's filters, 86.6% of it passing even stricter thresholds. Blinded labels support 6 of the 7 findings (defect rates .53-1.00 against .08 in a random control) and do not support one. The compiled suite scans the full corpus in 0.7 s of wall-clock time without a GPU, against \$12k-\$90k per LLM classification pass. The best static sampling baseline validates more selectors than any agent run, at under half the cost. The agent contributes exact prevalence, a precision estimate checked against sampled documents, an account of why the pipeline missed each slice, and a reusable test. We release the framework, Slovak test suite, validation data and agent trajectories.

## 05-006 | Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models
- arXiv: 2505.22232  first public: 2025-05-28  latest: 2025-05-31  primary cat: cs.CL
- authors (18): Mehdi Ali; Manuel Brack; Max Lübbering; Elias Wendt; Abbas Goher Khan; Richard Rutmann ...
- seed subtopic: 质量筛选（模型分类器）; type: 原始研究; cross: []
- arXiv comment: Project page available at https://huggingface.co/spaces/Jackal-AI/JQL
- URLs on first pages of PDF: https://huggingface.co/datasets/JQL-AI/jql_human_edu_ https://huggingface.co/spaces/JQL-AI/JQL
- pages: 38

ABSTRACT: High-quality multilingual training data is essential for effectively pretraining large language models (LLMs). Yet, the availability of suitable open-source multilingual datasets remains limited. Existing state-of-the-art datasets mostly rely on heuristic filtering methods, restricting both their cross-lingual transferability and scalability. Here, we introduce JQL, a systematic approach that efficiently curates diverse and high-quality multilingual data at scale while significantly reducing computational demands. JQL distills LLMs' annotation capabilities into lightweight annotators based on pretrained multilingual embeddings. These models exhibit robust multilingual and cross-lingual performance, even for languages and scripts unseen during training. Evaluated empirically across 35 languages, the resulting annotation pipeline substantially outperforms current heuristic filtering methods like Fineweb2. JQL notably enhances downstream model training quality and increases data retention rates. Our research provides practical insights and valuable resources for multilingual data curation, raising the standards of multilingual dataset development.

## 05-007 | Enhancing Multilingual LLM Pretraining with Model-Based Data Selection
- arXiv: 2502.10361  first public: 2025-02-14  latest: 2026-02-19  primary cat: cs.CL
- authors (3): Bettina Messmer; Vinko Sabolčec; Martin Jaggi
- seed subtopic: 质量筛选（模型分类器）; type: 原始研究; cross: ['07']
- arXiv comment: NeurIPS 2025 Track on Datasets and Benchmarks
- pages: 37

ABSTRACT: Dataset curation has become a basis for strong large language model (LLM) performance. While various rule-based filtering heuristics exist for English and multilingual datasets, model-based filtering techniques have primarily focused on English. To address the disparity stemming from limited research on non-English languages, we develop a model-based filtering framework for multilingual datasets that aims to identify a diverse set of structured and knowledge-rich samples. Our approach emphasizes transparency, simplicity, and efficiency, leveraging Transformer- and FastText-based classifiers to ensure the broad accessibility of our technique and data. We conduct comprehensive ablation studies on the FineWeb-2 web crawl dataset across diverse language families, scripts, and resource availability to demonstrate the effectiveness of our method. Training a 1B-parameter Llama model for 70B and 119B tokens, our approach can match the baseline MMLU score with as little as 15% of the training tokens, while also improving across other benchmarks and mitigating the curse of multilinguality. These findings provide strong evidence for the generalizability of our approach to other languages. As a result, we extend our framework to 20 languages for which we release the refined pretraining datasets.

## 05-008 | FinerWeb-10BT: Refining Web Data with LLM-Based Line-Level Filtering
- arXiv: 2501.07314  first public: 2025-01-13  latest: 2025-01-13  primary cat: cs.CL
- authors (3): Erik Henriksson; Otto Tarkka; Filip Ginter
- seed subtopic: 质量筛选（模型分类器）; type: 原始研究; cross: []
- arXiv comment: 11 pages, 4 figures, 4 tables. To be published in NoDaLiDa/Baltic-HLT 2025 proceedings
- URLs on first pages of PDF: https://github.com/TurkuNLP/finerweb-10bt https://huggingface.co/datasets/HuggingFaceFW/fineweb/ https://huggingface.co/datasets/TurkuNLP/finerweb-
- pages: 11

ABSTRACT: Data quality is crucial for training Large Language Models (LLMs). Traditional heuristic filters often miss low-quality text or mistakenly remove valuable content. In this paper, we introduce an LLM-based line-level filtering method to enhance training data quality. We use GPT-4o mini to label a 20,000-document sample from FineWeb at the line level, allowing the model to create descriptive labels for low-quality lines. These labels are grouped into nine main categories, and we train a DeBERTa-v3 classifier to scale the filtering to a 10B-token subset of FineWeb. To test the impact of our filtering, we train GPT-2 models on both the original and the filtered datasets. The results show that models trained on the filtered data achieve higher accuracy on the HellaSwag benchmark and reach their performance targets faster, even with up to 25\% less data. This demonstrates that LLM-based line-level filtering can significantly improve data quality and training efficiency for LLMs. We release our quality-annotated dataset, FinerWeb-10BT, and the codebase to support further work in this area.

## 05-009 | ÜberWeb: Insights from Multilingual Curation for a 20-Trillion-Token Dataset
- arXiv: 2602.15210  first public: 2026-02-16  latest: 2026-02-25  primary cat: cs.LG
- authors (35): DatologyAI; :; Aldo Gael Carranza; Kaleigh Mentzer; Ricardo Pio Monti; Alex Fang ...
- seed subtopic: 多语言数据整理; type: 技术报告; cross: ['07']
- pages: 31

ABSTRACT: Multilinguality is a core capability for modern foundation models, yet training high-quality multilingual models remains challenging due to uneven data availability across languages. A further challenge is the performance interference that can arise from joint multilingual training, commonly referred to as the "curse of multilinguality". We study multilingual data curation across thirteen languages and find that many reported regressions are not inherent to multilingual scaling but instead stem from correctable deficiencies in data quality and composition rather than fundamental capacity limits. In controlled bilingual experiments, improving data quality for any single language benefits others: curating English improves non-English performance in 12 of 13 languages, while curating non-English yields reciprocal improvements in English. Bespoke per-language curation produces substantially larger within-language improvements. Extending these findings to large-scale general-purpose training mixtures, we show that curated multilingual allocations comprising under 8% of total tokens remain remarkably effective. We operationalize this approach within an effort that produced a 20T-token pretraining corpus derived entirely from public sources. Models with 3B and 8B parameters trained on a 1T-token random subset achieve competitive multilingual accuracy with 4-10x fewer training FLOPs than strong public baselines, establishing a new Pareto frontier in multilingual performance versus compute. Moreover, these benefits extend to frontier model scale: the 20T-token corpus served as part of the pretraining dataset for Trinity Large (400B/A13B), which exhibits strong multilingual performance relative to its training FLOPs. These results show that targeted, per-language data curation mitigates multilingual interference and enables compute-efficient multilingual scaling.

## 05-010 | Mix, MinHash, and Match: Cross-Source Agreement for Multilingual Pretraining Datasets
- arXiv: 2512.18834  first public: 2025-12-21  latest: 2026-01-29  primary cat: cs.CL
- authors (2): Sultan Alrashed; Francesco Orabona
- seed subtopic: 去重与跨源一致性; type: 原始研究; cross: []
- arXiv comment: Multilingual LLM pretraining dataset curation
- URLs on first pages of PDF: https://huggingface.co/collections/AdaMLLab/mixminmatch
- pages: 26

ABSTRACT: Multilingual data from the web is essential for LLM pretraining. Yet, scraping it is expensive, and research groups repeatedly crawl the same content. For example, we found that over 40\% of tokens across major Arabic web corpora are duplicated between sources. In this work, we propose to use this wasteful redundancy as a quality signal to create high-quality pretraining datasets. Our key insight is that cross-source agreement functions as a free, model-free quality filter: content retained by multiple independent pipelines is more likely to represent high-quality text. Crucially, this signal requires no additional computation beyond standard deduplication, which is already performed at scale when pretraining language models. So, we propose MixMinMatch, a method that combines multiple existing web corpora, performs cross-dataset MinHash deduplication, and identifies documents independently recovered by multiple sources. We apply MixMinMatch to Arabic, Turkish, and Hindi, producing corpora that match or exceed the quality of the best single-source baselines, while providing up to 4$\times$ more unique tokens. On Arabic, our matched subset achieves a 4.5\% relative improvement over ArabicWeb24, while on Turkish, we improve over FineWeb-2 by 5.5\%. We release the datasets at: https://huggingface.co/collections/AdaMLLab/mixminmatch

## 05-011 | The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale
- arXiv: 2406.17557  first public: 2024-06-25  latest: 2024-10-31  primary cat: cs.CL
- authors (8): Guilherme Penedo; Hynek Kydlíček; Loubna Ben allal; Anton Lozhkov; Margaret Mitchell; Colin Raffel ...
- seed subtopic: 质量筛选（启发式）; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/HuggingFaceFW/fineweb https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
- pages: 38

ABSTRACT: The performance of a large language model (LLM) depends heavily on the quality and size of its pretraining dataset. However, the pretraining datasets for state-of-the-art open LLMs like Llama 3 and Mixtral are not publicly available and very little is known about how they were created. In this work, we introduce FineWeb, a 15-trillion token dataset derived from 96 Common Crawl snapshots that produces better-performing LLMs than other open pretraining datasets. To advance the understanding of how best to curate high-quality pretraining datasets, we carefully document and ablate all of the design choices used in FineWeb, including in-depth investigations of deduplication and filtering strategies. In addition, we introduce FineWeb-Edu, a 1.3-trillion token collection of educational text filtered from FineWeb. LLMs pretrained on FineWeb-Edu exhibit dramatically better performance on knowledge- and reasoning-intensive benchmarks like MMLU and ARC. Along with our datasets, we publicly release our data curation codebase and all of the models trained during our ablation experiments.

## 05-012 | DataComp-LM: In search of the next generation of training sets for language models
- arXiv: 2406.11794  first public: 2024-06-17  latest: 2025-04-21  primary cat: cs.LG
- authors (59): Jeffrey Li; Alex Fang; Georgios Smyrnis; Maor Ivgi; Matt Jordan; Samir Gadre ...
- seed subtopic: 质量筛选（模型分类器）; type: 基准与数据集; cross: []
- arXiv comment: Project page: https://www.datacomp.ai/dclm/
- pages: 89

ABSTRACT: We introduce DataComp for Language Models (DCLM), a testbed for controlled dataset experiments with the goal of improving language models. As part of DCLM, we provide a standardized corpus of 240T tokens extracted from Common Crawl, effective pretraining recipes based on the OpenLM framework, and a broad suite of 53 downstream evaluations. Participants in the DCLM benchmark can experiment with data curation strategies such as deduplication, filtering, and data mixing at model scales ranging from 412M to 7B parameters. As a baseline for DCLM, we conduct extensive experiments and find that model-based filtering is key to assembling a high-quality training set. The resulting dataset, DCLM-Baseline enables training a 7B parameter language model from scratch to 64% 5-shot accuracy on MMLU with 2.6T training tokens. Compared to MAP-Neo, the previous state-of-the-art in open-data language models, DCLM-Baseline represents a 6.6 percentage point improvement on MMLU while being trained with 40% less compute. Our baseline model is also comparable to Mistral-7B-v0.3 and Llama 3 8B on MMLU (63% & 66%), and performs similarly on an average of 53 natural language understanding tasks while being trained with 6.6x less compute than Llama 3 8B. Our results highlight the importance of dataset design for training language models and offer a starting point for further research on data curation.

## 05-013 | Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset
- arXiv: 2412.02595  first public: 2024-12-03  latest: 2025-05-30  primary cat: cs.CL
- authors (9): Dan Su; Kezhi Kong; Ying Lin; Joseph Jennings; Brandon Norick; Markus Kliegl ...
- seed subtopic: 质量筛选（模型分类器）; type: 基准与数据集; cross: []
- arXiv comment: ACL 2025
- URLs on first pages of PDF: https://github.com/NVIDIA/NeMo-Curator https://github.com/google-research/ https://huggingface.co/nvidia/nemocurator-
- pages: 17

ABSTRACT: Recent English Common Crawl datasets like FineWeb-Edu and DCLM achieved significant benchmark gains via aggressive model-based filtering, but at the cost of removing 90% of data. This limits their suitability for long token horizon training, such as 15T tokens for Llama 3.1. In this paper, we show how to achieve better trade-offs between accuracy and data quantity by a combination of classifier ensembling, synthetic data rephrasing, and reduced reliance on heuristic filters. When training 8B parameter models for 1T tokens, using a high-quality subset of our data improves MMLU by 5.6 over DCLM, demonstrating the efficacy of our methods for boosting accuracies over a relatively short token horizon. Furthermore, our full 6.3T token dataset matches DCLM on MMLU, but contains four times more unique real tokens than DCLM. This unlocks state-of-the-art training over a long token horizon: an 8B parameter model trained for 15T tokens, of which 7.2T came from our dataset, is better than the Llama 3.1 8B model: +5 on MMLU, +3.1 on ARC-Challenge, and +0.5 on average across ten diverse tasks. The dataset is available at https://data.commoncrawl.org/contrib/Nemotron/Nemotron-CC/index.html

## 05-014 | AICC: Parse HTML Finer, Make Models Better -- A 7.3T AI-Ready Corpus Built by a Model-Based HTML Parser
- arXiv: 2511.16397  first public: 2025-11-20  latest: 2025-11-26  primary cat: cs.CL
- authors (29): Ren Ma; Jiantao Qiu; Chao Xu; Pei Chu; Kaiwen Liu; Pengli Ren ...
- seed subtopic: 正文抽取; type: 基准与数据集; cross: []
- pages: 34

ABSTRACT: While web data quality is crucial for large language models, most curation efforts focus on filtering and deduplication,treating HTML-to-text extraction as a fixed pre-processing step. Existing web corpora rely on heuristic-based extractors like Trafilatura, which struggle to preserve document structure and frequently corrupt structured elements such as formulas, codes, and tables. We hypothesize that improving extraction quality can be as impactful as aggressive filtering strategies for downstream performance. We introduce MinerU-HTML, a novel extraction pipeline that reformulates content extraction as a sequence labeling problem solved by a 0.6B-parameter language model. Unlike text-density heuristics, MinerU-HTML leverages semantic understanding and employs a two-stage formatting pipeline that explicitly categorizes semantic elements before converting to Markdown. Crucially, its model-based approach is inherently scalable, whereas heuristic methods offer limited improvement pathways. On MainWebBench, our benchmark of 7,887 annotated web pages, MinerU-HTML achieves 81.8\% ROUGE-N F1 compared to Trafilatura's 63.6\%, with exceptional structured element preservation (90.9\% for code blocks, 94.0\% for formulas). Using MinerU-HTML, we construct AICC (AI-ready Common Crawl), a 7.3-trillion token multilingual corpus from two Common Crawl snapshots. In controlled pretraining experiments where AICC and Trafilatura-extracted TfCC undergo identical filtering, models trained on AICC (62B tokens) achieve 50.8\% average accuracy across 13 benchmarks, outperforming TfCC by 1.08pp-providing direct evidence that extraction quality significantly impacts model capabilities. AICC also surpasses RefinedWeb and FineWeb on key benchmarks. We publicly release MainWebBench, MinerU-HTML, and AICC, demonstrating that HTML extraction is a critical, often underestimated component of web corpus construction.

## 05-015 | LSHBloom: Memory-efficient, Extreme-scale Document Deduplication
- arXiv: 2411.04257  first public: 2024-11-06  latest: 2026-01-27  primary cat: cs.LG
- authors (10): Arham Khan; Robert Underwood; Carlo Siebenschuh; Yadu Babuji; Aswathy Ajith; Kyle Hippe ...
- seed subtopic: 去重; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Contemporary large language model (LLM) training pipelines require the assembly of internet-scale databases full of text data from a variety of sources (e.g., web, academic, and publishers). Preprocessing these datasets via deduplication -- detecting and eliminating additional instances of the same content -- is a major focus for assembling and curating training datasets for LLMs. Unrestrained, duplicates in the training dataset increase training costs and lead to undesirable properties such as memorization in trained models or cheating on evaluation. Unfortunately, contemporary approaches to document-level deduplication are either unreliable at accurately identifying duplicate documents or extremely expensive in terms of both runtime and memory. We propose LSHBloom, an extension to MinhashLSH, which replaces the expensive LSHIndex with lightweight Bloom filters. LSHBloom demonstrates the same state-of-the-art deduplication performance as MinhashLSH, with only a marginal increase in false positives (near zero in our experiments), while boasting competitive runtime (12$\times$ faster than MinhashLSH on peS2o) and, crucially, using 18$\times$ less disk space than MinhashLSH (as measured on peS2o). Based on extrapolation, we show that this advantage in space and runtime remains even at the extreme scale of several billion documents. LSHBloom allows practitioners to access the deduplication quality of MinHashLSH at scales that are normally only tractable for less sophisticated, heuristic solutions. As a result, LSHBloom promises to enable scaling high-quality document deduplication to internet-scale text datasets.

## 05-016 | olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models
- arXiv: 2502.18443  first public: 2025-02-25  latest: 2025-07-02  primary cat: cs.CL
- authors (10): Jake Poznanski; Aman Rangapur; Jon Borchardt; Jason Dunkelberger; Regan Huff; Daniel Lin ...
- seed subtopic: OCR 与文档转换; type: 原始研究; cross: []
- pages: 33

ABSTRACT: PDF documents have the potential to provide trillions of novel, high-quality tokens for training language models. However, these documents come in a diversity of types with differing formats and visual layouts that pose a challenge when attempting to extract and faithfully represent the underlying content for language model use. Traditional open source tools often produce lower quality extractions compared to vision language models (VLMs), but reliance on the best VLMs can be prohibitively costly (e.g., over 6,240 USD per million PDF pages for GPT-4o) or infeasible if the PDFs cannot be sent to proprietary APIs. We present olmOCR, an open-source toolkit for processing PDFs into clean, linearized plain text in natural reading order while preserving structured content like sections, tables, lists, equations, and more. Our toolkit runs a fine-tuned 7B vision language model (VLM) trained on olmOCR-mix-0225, a sample of 260,000 pages from over 100,000 crawled PDFs with diverse properties, including graphics, handwritten text and poor quality scans. olmOCR is optimized for large-scale batch processing, able to scale flexibly to different hardware setups and can convert a million PDF pages for only 176 USD. To aid comparison with existing systems, we also introduce olmOCR-Bench, a curated set of 1,400 PDFs capturing many content types that remain challenging even for the best tools and VLMs, including formulas, tables, tiny fonts, old scans, and more. We find olmOCR outperforms even top VLMs including GPT-4o, Gemini Flash 2 and Qwen-2.5-VL. We openly release all components of olmOCR: our fine-tuned VLM model, training code and data, an efficient inference pipeline that supports vLLM and SGLang backends, and benchmark olmOCR-Bench.

## 05-017 | Data Contamination Can Cross Language Barriers
- arXiv: 2406.13236  first public: 2024-06-19  latest: 2024-10-30  primary cat: cs.CL
- authors (6): Feng Yao; Yufan Zhuang; Zihao Sun; Sunan Xu; Animesh Kumar; Jingbo Shang
- seed subtopic: 基准污染检测; type: 原始研究; cross: ['15']
- arXiv comment: EMNLP 2024 Main camera-ready version
- pages: 12

ABSTRACT: The opacity in developing large language models (LLMs) is raising growing concerns about the potential contamination of public benchmarks in the pre-training data. Existing contamination detection methods are typically based on the text overlap between training and evaluation data, which can be too superficial to reflect deeper forms of contamination. In this paper, we first present a cross-lingual form of contamination that inflates LLMs' performance while evading current detection methods, deliberately injected by overfitting LLMs on the translated versions of benchmark test sets. Then, we propose generalization-based approaches to unmask such deeply concealed contamination. Specifically, we examine the LLM's performance change after modifying the original benchmark by replacing the false answer choices with correct ones from other questions. Contaminated models can hardly generalize to such easier situations, where the false choices can be \emph{not even wrong}, as all choices are correct in their memorization. Experimental results demonstrate that cross-lingual contamination can easily fool existing detection methods, but not ours. In addition, we discuss the potential utilization of cross-lingual contamination in interpreting LLMs' working mechanisms and in post-training LLMs for enhanced multilingual capabilities. The code and dataset we use can be obtained from \url{https://github.com/ShangDataLab/Deep-Contam}.

## 05-018 | Investigating Data Contamination in Modern Benchmarks for Large Language Models
- arXiv: 2311.09783  first public: 2023-11-16  latest: 2024-04-03  primary cat: cs.CL
- authors (5): Chunyuan Deng; Yilun Zhao; Xiangru Tang; Mark Gerstein; Arman Cohan
- seed subtopic: 基准污染检测; type: 原始研究; cross: []
- arXiv comment: NAACL 2024 Version
- pages: 14

ABSTRACT: Recent observations have underscored a disparity between the inflated benchmark scores and the actual performance of LLMs, raising concerns about potential contamination of evaluation benchmarks. This issue is especially critical for closed-source models and certain open-source models where training data transparency is lacking. In this paper we study data contamination by proposing two methods tailored for both open-source and proprietary LLMs. We first introduce a retrieval-based system to explore potential overlaps between evaluation benchmarks and pretraining corpora. We further present a novel investigation protocol named \textbf{T}estset \textbf{S}lot Guessing (\textit{TS-Guessing}), applicable to both open and proprietary models. This approach entails masking a wrong answer in a multiple-choice question and prompting the model to fill in the gap. Additionally, it involves obscuring an unlikely word in an evaluation example and asking the model to produce it. We find that certain commercial LLMs could surprisingly guess the missing option in various test sets. Specifically, in the TruthfulQA benchmark, we find that LLMs exhibit notable performance improvement when provided with additional metadata in the benchmark. Further, in the MMLU benchmark, ChatGPT and GPT-4 demonstrated an exact match rate of 52\% and 57\%, respectively, in guessing the missing options in benchmark test data. We hope these results underscore the need for more robust evaluation methodologies and benchmarks in the field.

## 05-019 | OpenLID-v3: Improving the Precision of Closely Related Language Identification -- An Experience Report
- arXiv: 2602.13139  first public: 2026-02-13  latest: 2026-06-18  primary cat: cs.CL
- authors (7): Mariia Fedorova; Nikolay Arefyev; Maja Buljan; Jindřich Helcl; Stephan Oepen; Egil Rønningstad ...
- seed subtopic: 语言识别（近似语言）; type: 原始研究; cross: []
- arXiv comment: VarDial'26 workshop at the EACL 2026 conference
- doi: 10.18653/v1/2026.vardial-1.23
- URLs on first pages of PDF: https://github.com/hplt-project/ https://github.com/hplt-project/openlid https://github.com/hplt-project/release3_ https://github.com/ltgoslo/slide https://huggingface.co/datasets/ https://huggingface.co/datasets/cis-lmu/udhr-lid
- pages: 20

ABSTRACT: Language identification (LID) is an essential step in building high-quality multilingual datasets from web data. Existing LID tools (such as OpenLID or GlotLID) often struggle to identify closely related languages and to distinguish valid natural language from noise, which contaminates language-specific subsets, especially for low-resource languages. In this work we extend the OpenLID classifier by adding more training data, merging problematic language variant clusters, and introducing a special label for marking noise. We call this extended system OpenLID-v3 and evaluate it against GlotLID on multiple benchmarks. During development, we focus on three groups of closely related languages (Bosnian, Croatian, and Serbian; Romance varieties of Northern Italy and Southern France; and Scandinavian languages) and contribute new evaluation datasets where existing ones are inadequate. We find that ensemble approaches improve precision but also substantially reduce coverage for low-resource languages. OpenLID-v3 is available on https://huggingface.co/HPLT/OpenLID-v3.

## 05-020 | CommonLID: Re-evaluating State-of-the-Art Language Identification Performance on Web Data
- arXiv: 2601.18026  first public: 2026-01-25  latest: 2026-06-08  primary cat: cs.CL
- authors (97): Pedro Ortiz Suarez; Laurie Burchell; Catherine Arnett; Rafael Mosquera-Gómez; Sara Hincapie-Monsalve; Thom Vaughan ...
- seed subtopic: 语言识别（评测）; type: 基准与数据集; cross: ['15']
- arXiv comment: 18 pages, 8 tables, 5 figures
- URLs on first pages of PDF: https://huggingface.co/datasets/commoncrawl/
- pages: 18

ABSTRACT: Language identification (LID) is a fundamental step in curating multilingual corpora. However, LID models still perform poorly for many languages, especially on the noisy and heterogeneous web data often used to train multilingual language models. In this paper, we introduce CommonLID, a community-driven, human-annotated LID benchmark for the web domain, covering 109 languages. Many of the included languages have been previously under-served, making CommonLID a key resource for developing more representative high-quality text corpora. We show CommonLID's value by using it, alongside five other common evaluation sets, to test eight popular LID models. We analyse our results to situate our contribution and to provide an overview of the state of the art. In particular, we highlight that existing evaluations overestimate LID accuracy for many languages in the web domain. We make CommonLID and the code used to create it available under an open, permissive license.

## 05-021 | Script-Agnostic Language Identification
- arXiv: 2406.17901  first public: 2024-06-25  latest: 2024-06-25  primary cat: cs.CL
- authors (3): Milind Agarwal; Joshua Otten; Antonios Anastasopoulos
- seed subtopic: 语言识别（文字无关）; type: 原始研究; cross: []
- arXiv comment: Under Review in ACL Rolling Review
- URLs on first pages of PDF: https://github.com/Joshua-Otten/Script-Agnostic-Lang-ID
- pages: 20

ABSTRACT: Language identification is used as the first step in many data collection and crawling efforts because it allows us to sort online text into language-specific buckets. However, many modern languages, such as Konkani, Kashmiri, Punjabi etc., are synchronically written in several scripts. Moreover, languages with different writing systems do not share significant lexical, semantic, and syntactic properties in neural representation spaces, which is a disadvantage for closely related languages and low-resource languages, especially those from the Indian Subcontinent. To counter this, we propose learning script-agnostic representations using several different experimental strategies (upscaling, flattening, and script mixing) focusing on four major Dravidian languages (Tamil, Telugu, Kannada, and Malayalam). We find that word-level script randomization and exposure to a language written in multiple scripts is extremely valuable for downstream script-agnostic language identification, while also maintaining competitive performance on naturally occurring text.

## 05-022 | What Language is This? Ask Your Tokenizer
- arXiv: 2602.17655  first public: 2026-02-19  latest: 2026-09-10  primary cat: cs.CL
- authors (4): Clara Meister; Ahmetcan Yavuz; Pietro Lesci; Tiago Pimentel
- seed subtopic: 语言识别; type: 原始研究; cross: ['06']
- arXiv comment: In Proceedings of ICML 2026
- pages: 22

ABSTRACT: Language Identification (LID) is an important component of many multilingual natural language processing pipelines, where it facilitates corpus curation, training data analysis, and cross-lingual evaluation of large language models. Despite near-perfect performance on high-resource languages, existing systems remain brittle in low-resource and closely related language settings. We introduce UniLID, a simple and efficient LID method based on the UnigramLM tokenization algorithm. In short, to predict a string's language label, we simply ask: under which language's unigram distribution is this string most likely? Our formulation is data- and compute-efficient, supports incremental addition of new languages without retraining existing models, and can naturally be integrated into existing language model tokenization pipelines. Empirical evaluations against widely used baselines, including fasttext, GlotLID-M, and CLD3, show that UniLID achieves competitive performance on standard benchmarks, reaches 69% accuracy with five labeled samples per language and 89% with 25, and delivers large gains on fine-grained dialect identification.

## 05-023 | Fumbling in Babel: An Investigation into ChatGPT's Language Identification Ability
- arXiv: 2311.09696  first public: 2023-11-16  latest: 2024-04-08  primary cat: cs.CL
- authors (5): Wei-Rui Chen; Ife Adebara; Khai Duy Doan; Qisheng Liao; Muhammad Abdul-Mageed
- seed subtopic: 语言识别（LLM）; type: 原始研究; cross: []
- arXiv comment: Accepted to NAACL 2024 Findings
- pages: 27

ABSTRACT: ChatGPT has recently emerged as a powerful NLP tool that can carry out a variety of tasks. However, the range of languages ChatGPT can handle remains largely a mystery. To uncover which languages ChatGPT `knows', we investigate its language identification (LID) abilities. For this purpose, we compile Babel-670, a benchmark comprising 670 languages representing 24 language families spoken in five continents. Languages in Babel-670 run the gamut from the very high-resource to the very low-resource. We then study ChatGPT's (both GPT-3.5 and GPT-4) ability to (i) identify language names and language codes (ii) under zero- and few-shot conditions (iii) with and without provision of a label set. When compared to smaller finetuned LID tools, we find that ChatGPT lags behind. For example, it has poor performance on African languages. We conclude that current large language models would benefit from further development before they can sufficiently serve diverse communities.

## 05-024 | TurEngMix: A Text Corpus and Benchmark for Turkish-English Code-Mixed Language Identification and Named Entity Recognition
- arXiv: 2609.06963  first public: 2026-09-07  latest: 2026-09-07  primary cat: cs.CL
- authors (3): Ilayda Dogan; Phuong-Anh Nguyen-Le; Julia Mendelsohn
- seed subtopic: 语言识别（语码混用）; type: 基准与数据集; cross: []
- arXiv comment: Accepted to W-NUT 2026 (11th Workshop on Natural User-generated Text), co-located with EMNLP 2026. 15 pages, 4 figures, 12 tables
- URLs on first pages of PDF: https://github.com/kemnguyenle/TurEngMix https://huggingface.co/datasets/ilydoa/TurEngMix
- pages: 15

ABSTRACT: Natural language processing systems underperform on code-mixed text, particularly for low-resource language pairs. Turkish-English poses a further challenge: it lets English stems combine with Turkish suffixes to form single mixed-language tokens. We introduce TurEngMix, a corpus of 5.5K noisy, naturally occurring social media posts (486,974 tokens) rich in Turkish-English code-mixing. From this corpus, we construct a new Turkish-English benchmark for code-mixed language identification (LID) and named entity recognition (NER), comprising 15K expert-annotated tokens. Evaluating both decoder LLM and fine-tuned encoder baselines, we find that monolingual Turkish and English tokens are labeled reliably, but all models have high error rates on mixed-language tokens for both LID and NER. For morphologically integrated tokens, NER error rates were 5.2x and 6.3x higher for GPT-4o and Qwen, respectively. This highlights how morphological integration remains a challenge. We release the corpus, annotations, and code to support future computational and sociolinguistic research on Turkish-English code-mixing.

## 05-025 | Automatic Machine Translation Detection Using a Surrogate Multilingual Translation Model
- arXiv: 2511.02958  first public: 2025-11-04  latest: 2025-11-04  primary cat: cs.CL
- authors (3): Cristian García-Romero; Miquel Esplà-Gomis; Felipe Sánchez-Martínez
- seed subtopic: 机器翻译文本检测; type: 原始研究; cross: []
- arXiv comment: Pre-MIT Press publication version
- URLs on first pages of PDF: https://huggingface.co/Unbabel/
- pages: 18

ABSTRACT: Modern machine translation (MT) systems depend on large parallel corpora, often collected from the Internet. However, recent evidence indicates that (i) a substantial portion of these texts are machine-generated translations, and (ii) an overreliance on such synthetic content in training data can significantly degrade translation quality. As a result, filtering out non-human translations is becoming an essential pre-processing step in building high-quality MT systems. In this work, we propose a novel approach that directly exploits the internal representations of a surrogate multilingual MT model to distinguish between human and machine-translated sentences. Experimental results show that our method outperforms current state-of-the-art techniques, particularly for non-English language pairs, achieving gains of at least 5 percentage points of accuracy.

## 05-026 | How Good is Your Wikipedia? Auditing Data Quality for Low-resource and Multilingual NLP
- arXiv: 2411.05527  first public: 2024-11-08  latest: 2026-05-04  primary cat: cs.CL
- authors (9): Kushal Tatariya; Artur Kulmizev; Wessel Poelman; Esther Ploeger; Marcel Bollmann; Johannes Bjerva ...
- seed subtopic: 低资源语料审计; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL Main, 2026
- URLs on first pages of PDF: https://github.com/akulmizev/texieve
- pages: 21

ABSTRACT: Wikipedia's perceived high quality and broad language coverage have established it as a fundamental resource in NLP. However, in recent years, such assumptions of high quality have become the subject of scrutiny in low-resource and multilingual contexts. In this study, we subject the entirety of non-English Wikipedia to a data filtering procedure typically reserved for noisy web-text -- a process which removes a large percentage of the collection's data. In analysing the removed data, we reveal numerous systematic quality issues, such as script and language contamination, repeated template and placeholder articles, and a high concentration of bot-generated content. We consolidate these findings into a 4-level quality ranking of Wikipedia, which shows strong correspondence with alternative quality measures and heuristics. Lastly, we evaluate the downstream impact of quality filtering in three practical language modelling scenarios, showing that models trained on filtered data largely match or outperform those trained on raw Wikipedia, with the largest gains observed for lower-quality language editions. Ultimately, our experiments serve as a first step in establishing quality-aware best practices for Wikipedia utilization in NLP, laying groundwork that can inform future dataset creation and curation efforts.

## 05-027 | Quality Does Matter: A Detailed Look at the Quality and Utility of Web-Mined Parallel Corpora
- arXiv: 2402.07446  first public: 2024-02-12  latest: 2024-06-14  primary cat: cs.CL
- authors (5): Surangika Ranathunga; Nisansa de Silva; Menan Velayuthan; Aloka Fernando; Charitha Rathnayake
- seed subtopic: 低资源语料审计; type: 原始研究; cross: ['04']
- pages: 21

ABSTRACT: We conducted a detailed analysis on the quality of web-mined corpora for two low-resource languages (making three language pairs, English-Sinhala, English-Tamil and Sinhala-Tamil). We ranked each corpus according to a similarity measure and carried out an intrinsic and extrinsic evaluation on different portions of this ranked corpus. We show that there are significant quality differences between different portions of web-mined corpora and that the quality varies across languages and datasets. We also show that, for some web-mined datasets, Neural Machine Translation (NMT) models trained with their highest-ranked 25k portion can be on par with human-curated datasets.

## 05-028 | Evaluating Machine Translation Datasets for Low-Web Data Languages: A Gendered Lens
- arXiv: 2511.03880  first public: 2025-11-05  latest: 2025-11-05  primary cat: cs.CL
- authors (8): Hellina Hailu Nigatu; Bethelhem Yemane Mamo; Bontu Fufa Balcha; Debora Taye Tesfaye; Elbethel Daniel Zewdie; Ikram Behiru Nesiru ...
- seed subtopic: 低资源语料审计; type: 原始研究; cross: []
- arXiv comment: Paper Under Review
- pages: 24

ABSTRACT: As low-resourced languages are increasingly incorporated into NLP research, there is an emphasis on collecting large-scale datasets. But in prioritizing quantity over quality, we risk 1) building language technologies that perform poorly for these languages and 2) producing harmful content that perpetuates societal biases. In this paper, we investigate the quality of Machine Translation (MT) datasets for three low-resourced languages--Afan Oromo, Amharic, and Tigrinya, with a focus on the gender representation in the datasets. Our findings demonstrate that while training data has a large representation of political and religious domain text, benchmark datasets are focused on news, health, and sports. We also found a large skew towards the male gender--in names of persons, the grammatical gender of verbs, and in stereotypical depictions in the datasets. Further, we found harmful and toxic depictions against women, which were more prominent for the language with the largest amount of data, underscoring that quantity does not guarantee quality. We hope that our work inspires further inquiry into the datasets collected for low-resourced languages and prompts early mitigation of harmful content. WARNING: This paper contains discussion of NSFW content that some may find disturbing.

## 05-029 | MuRating: A High Quality Data Selecting Approach to Multilingual Large Language Model Pretraining
- arXiv: 2507.01785  first public: 2025-07-02  latest: 2026-03-05  primary cat: cs.CL
- authors (13): Zhixun Chen; Ping Guo; Wenhan Han; Yifan Zhang; Binbin Liu; Haobin Lin ...
- seed subtopic: 质量筛选（模型分类器）; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2025 poster
- URLs on first pages of PDF: https://github.com/aialt/MuRater
- pages: 26

ABSTRACT: Data quality is a critical driver of large language model performance, yet existing model-based selection methods focus almost exclusively on English. We introduce MuRating, a scalable framework that transfers high-quality English data-quality signals into a single rater for 17 target languages. MuRating aggregates multiple English "raters" via pairwise comparisons to learn unified document-quality scores,then projects these judgments through translation to train a multilingual evaluator on monolingual, cross-lingual, and parallel text pairs. Applied to web data, MuRating selects balanced subsets of English and multilingual content to pretrain a 1.2 B-parameter LLaMA model. Compared to strong baselines, including QuRater, AskLLM, DCLM and so on, our approach boosts average accuracy on both English benchmarks and multilingual evaluations, with especially large gains on knowledge-intensive tasks. We further analyze translation fidelity, selection biases, and underrepresentation of narrative material, outlining directions for future work.

## 05-030 | Toward Cross-Lingual Quality Classifiers for Multilingual Pretraining Data Selection
- arXiv: 2604.20549  first public: 2026-04-22  latest: 2026-04-22  primary cat: cs.CL
- authors (4): Yassine Turki; Vinko Sabolčec; Bettina Messmer; Martin Jaggi
- seed subtopic: 质量筛选（跨语言迁移）; type: 原始研究; cross: []
- arXiv comment: Accepted at the 3rd Workshop on Navigating and Addressing Data Problems for Foundation Models (DATA-FM @ ICLR 2026). 31 pages, 4 figures
- pages: 31

ABSTRACT: As Large Language Models (LLMs) scale, data curation has shifted from maximizing volume to optimizing the signal-to-noise ratio by performing quality filtering. However, for many languages, native high quality data is insufficient to train robust quality classifiers. This work investigates the idea that quality markers in embedding space may show cross-lingual consistency, which would allow high-resource languages to subsidize the filtering of low-resource ones. We evaluate various filtering strategies, including cross-lingual transfer, third quartile sampling (Q3), and retention rate tuning. Our results demonstrate that massive multilingual pooling frequently outperforms monolingual baselines in both rank stability and aggregate accuracy for a 1B model trained on 103B tokens, delivering gains for high resource languages (1.2% increase in aggregate normalized accuracy for French) and matching or exceeding monolingual baselines for low-resource languages. However, we find that scale alone does not guarantee stability. Furthermore, for high-resource languages like French, we show that refining the decision boundary through third quartile sampling (Q3) or tuning the retention rate is necessary to fully leverage the multilingual signal.

## 05-031 | Register Always Matters: Analysis of LLM Pretraining Data Through the Lens of Language Variation
- arXiv: 2504.01542  first public: 2025-04-02  latest: 2025-09-09  primary cat: cs.CL
- authors (4): Amanda Myntti; Erik Henriksson; Veronika Laippala; Sampo Pyysalo
- seed subtopic: 语域/体裁分类; type: 原始研究; cross: []
- pages: 24

ABSTRACT: Pretraining data curation is a cornerstone in Large Language Model (LLM) development, leading to growing research on quality filtering of large web corpora. From statistical quality flags to LLM-based labelling systems, datasets are divided into categories, frequently reducing to a binary: those passing the filters are deemed as valuable examples, others are discarded as useless or detrimental. However, a more detailed understanding of the contribution of different kinds of texts to model performance is still largely lacking. In this article, we present the first study utilising registers or genres - a widely used standard in corpus linguistics to model linguistic variation - to curate pretraining datasets and investigate the effect of register on the performance of LLMs. We train small generative models with register classified data and evaluate them using standard benchmarks, and show that the register of pretraining data substantially affects model performance. We uncover surprising relationships between the pretraining material and the resulting models: using the News register results in subpar performance, and on the contrary, including the Opinion class, covering texts such as reviews and opinion blogs, is highly beneficial. While a model trained on the entire unfiltered dataset outperforms those trained on datasets limited to a single register, combining well-performing registers like How-to-Instructions, Informational Description, and Opinion leads to major improvements. Furthermore, analysis of individual benchmark results reveals key differences in the strengths and drawbacks of specific register classes as pretraining data. These findings show that register is an important explainer of model variation and can facilitate more deliberate future data selection practices.

## 05-032 | Automatic register identification for the open web using multilingual deep learning
- arXiv: 2406.19892  first public: 2024-06-28  latest: 2026-10-02  primary cat: cs.CL
- authors (6): Erik Henriksson; Amanda Myntti; Saara Hellström; Anni Eskelinen; Selcen Erten-Johansson; Veronika Laippala
- seed subtopic: 语域/体裁分类; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/TurkuNLP/pytorch-registerlabeling
- pages: 41

ABSTRACT: This article presents multilingual deep learning models for identifying web registers -- text varieties such as news reports and discussion forums -- across 16 languages. We introduce the Multilingual CORE corpora, which contain over 72,000 documents annotated with a hierarchical taxonomy of 25 registers designed to cover the entire open web. Using multi-label classification, our best model achieves 79% F1 averaged across languages, matching or exceeding previous studies that used simpler classification schemes. This demonstrates that models can perform well even with a complex register scheme at multilingual scale. However, we observe a consistent performance ceiling across all models and configurations. When we remove documents with uncertain labels through data pruning, performance increases to over 90% F1, suggesting that this ceiling stems from inherent ambiguity in web registers rather than model limitations. Analysis of hybrid texts (those combining multiple registers) reveals that the main challenge lies not in classifying hybrids themselves, but in distinguishing hybrid from non-hybrid documents. Multilingual models consistently outperform monolingual ones, particularly for languages with limited training data. Zero-shot performance on unseen languages drops by an average of 7%, though this varies by language (3--8%), indicating that while registers share features across languages, they also retain language-specific characteristics.

## 05-033 | Don't Touch My Diacritics
- arXiv: 2410.24140  first public: 2024-10-31  latest: 2025-02-19  primary cat: cs.CL
- authors (2): Kyle Gorman; Yuval Pinter
- seed subtopic: Unicode 规范化与变音符; type: 原始研究; cross: ['06']
- arXiv comment: 6 pages
- pages: 7

ABSTRACT: The common practice of preprocessing text before feeding it into NLP models introduces many decision points which have unintended consequences on model performance. In this opinion piece, we focus on the handling of diacritics in texts originating in many languages and scripts. We demonstrate, through several case studies, the adverse effects of inconsistent encoding of diacritized characters and of removing diacritics altogether. We call on the community to adopt simple but necessary steps across all models and toolkits in order to improve handling of diacritized text and, by extension, increase equity in multilingual NLP.

## 05-034 | ks-lit-3m: A 3.1 million word kashmiri text dataset for large language model pretraining
- arXiv: 2601.01091  first public: 2026-01-03  latest: 2026-01-03  primary cat: cs.CL
- authors (1): Haq Nawaz Malik
- seed subtopic: Unicode 与旧编码转换; type: 基准与数据集; cross: ['04']
- pages: 9

ABSTRACT: Large Language Models (LLMs) demonstrate remarkable fluency across high-resource languages yet consistently fail to generate coherent text in Kashmiri, a language spoken by approximately seven million people. This performance disparity stems not from inherent model limitations but from a critical scarcity of high-quality training data. Decades of Kashmiri literature remain inaccessible to modern NLP pipelines due to their encoding in the proprietary InPage desktop publishing format. This paper introduces KS-LIT-3M, a curated corpus of 3.1 million words (16.4 million characters) specifically designed for pretraining language models on Kashmiri. The dataset is structured as a single continuous linear text stream, optimized for causal language model training where models learn to predict subsequent tokens from preceding context. The corpus was constructed through the development of a specialized InPage-to-Unicode converter, followed by rigorous preprocessing including English contamination removal, character normalization, and quality validation. Encompassing 131,607 unique words drawn from diverse genres including literary works, journalistic writing, academic texts, and religious scholarship, KS-LIT-3M addresses a fundamental resource gap for Kashmiri language technology. The dataset is released under the CC-BY-4.0 license to facilitate research in Kashmiri natural language processing.

## 05-035 | Reference-Based Post-OCR Processing with LLM for Precise Diacritic Text in Historical Document Recognition
- arXiv: 2410.13305  first public: 2024-10-17  latest: 2025-02-27  primary cat: cs.CL
- authors (4): Thao Do; Dinh Phu Tran; An Vo; Daeyoung Kim
- seed subtopic: OCR 噪声与后校正; type: 原始研究; cross: []
- arXiv comment: Accepted in the AAAI 2025 (39th) AISI track. Dataset and repo are in the paper
- URLs on first pages of PDF: https://github.com/thaodod/VieBookRead
- pages: 9

ABSTRACT: Extracting fine-grained OCR text from aged documents in diacritic languages remains challenging due to unexpected artifacts, time-induced degradation, and lack of datasets. While standalone spell correction approaches have been proposed, they show limited performance for historical documents due to numerous possible OCR error combinations and differences between modern and classical corpus distributions. We propose a method utilizing available content-focused ebooks as a reference base to correct imperfect OCR-generated text, supported by large language models. This technique generates high-precision pseudo-page-to-page labels for diacritic languages, where small strokes pose significant challenges in historical conditions. The pipeline eliminates various types of noise from aged documents and addresses issues such as missing characters, words, and disordered sequences. Our post-processing method, which generated a large OCR dataset of classical Vietnamese books, achieved a mean grading score of 8.72 on a 10-point scale. This outperformed the state-of-the-art transformer-based Vietnamese spell correction model, which scored 7.03 when evaluated on a sampled subset of the dataset. We also trained a baseline OCR model to assess and compare it with well-known engines. Experimental results demonstrate the strength of our baseline model compared to widely used open-source solutions. The resulting dataset will be released publicly to support future studies.

## 05-036 | OCR Error Post-Correction with LLMs in Historical Documents: No Free Lunches
- arXiv: 2502.01205  first public: 2025-02-03  latest: 2025-02-03  primary cat: cs.CL
- authors (4): Jenna Kanerva; Cassandra Ledins; Siiri Käpyaho; Filip Ginter
- seed subtopic: OCR 噪声与后校正; type: 原始研究; cross: []
- arXiv comment: To be published in RESOURCEFUL 2025
- URLs on first pages of PDF: https://github.com/COMHIS
- pages: 10

ABSTRACT: Optical Character Recognition (OCR) systems often introduce errors when transcribing historical documents, leaving room for post-correction to improve text quality. This study evaluates the use of open-weight LLMs for OCR error correction in historical English and Finnish datasets. We explore various strategies, including parameter optimization, quantization, segment length effects, and text continuation methods. Our results demonstrate that while modern LLMs show promise in reducing character error rates (CER) in English, a practically useful performance for Finnish was not reached. Our findings highlight the potential and limitations of LLMs in scaling OCR post-correction for large historical corpora.

## 05-037 | Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale
- arXiv: 2608.19026  first public: 2026-08-19  latest: 2026-08-19  primary cat: cs.CL
- authors (7): David Lowry-Duda; Matteo Cargnelutti; Catherine Brobston; Salwa Ismail; Greg Leppert; Amanda Watson ...
- seed subtopic: OCR 噪声与后校正; type: 原始研究; cross: ['04']
- URLs on first pages of PDF: https://huggingface.co/datasets/institutional/institutional-books-1.0 https://huggingface.co/talkie-lm/talkie-1930-13b-base https://huggingface.co/typewriter-ai/typewriter-1913-7B-base
- pages: 59

ABSTRACT: Released in 2025, Institutional Books: Harvard Library (IB-HL) is a collection of 983,004 volumes (242B o200k_base tokens), originally digitized through Harvard Library's participation in the Google Books Library project. As researchers and developers have begun to use IB-HL, a tension has emerged between standard large-scale preprocessing practices and the goals of careful information stewardship. Many existing pipelines optimize for web text: as a result, they tend to aggressively filter, deduplicate, restrict by language, and sometimes discard meaningful metadata. Meanwhile, researchers seeking to use IB-HL duplicate effort while performing similar processing and analysis. We describe an approach that we call Enriched Text. Instead of producing a single 'complete' stream of tokens, we normalize the text while preserving metadata through annotations. We separate endmatter, detect per-paragraph language, identify clusters of duplicate paragraphs, and compute per-paragraph bits-per-byte scores. We provide this information through HTML-like annotations layered on top of the text. By parsing these annotations, users can tailor the output to their own needs instead of accepting a global editorial decision on content. The pipeline applies to all $\approx$250 languages in the collection. This report describes this project's goals, implementation, and design rationale. The release includes IB-HL-ET (an enriched-text version of IB-HL containing 217B o200k_base tokens across 983,003 volumes, organized into 1.39B annotated subtopic paragraphs) and the pipeline that produced it. These serve to make the collection easier for machines to parse and for humans to study.

## 05-038 | Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora
- arXiv: 2601.14994  first public: 2026-01-21  latest: 2026-10-08  primary cat: cs.CL
- authors (3): Chaymaa Abbas; Nour Shammaa; Mariette Awad
- seed subtopic: 基准污染检测; type: 原始研究; cross: ['15']
- pages: 11

ABSTRACT: Data contamination can invalidate benchmark evaluation when a model benefits from memorized evaluation content rather than genuine generalization. Yet contamination is difficult to audit when the exposed content differs in language from the evaluation benchmark. We study this failure mode by deliberately exposing four open-weight instruction-tuned LLMs to Arabic translations of MMLU and XQuAD evaluation items at increasing exposure levels, then evaluating them on the original English tasks. This controlled setup is a proxy for contamination rather than a reconstruction of real-world pretraining leakage. We first test two English-centric post-hoc probes, TS-Guessing and Min-K%++, and find that their signals largely disappear under translated exposure: TS-Guessing remains weak except for model-specific positional recall on MMLU, while Min-K%++ stays at or below chance. At the same time, English MMLU performance increases with Arabic exposure, showing that the absence of an English contamination signal does not imply the absence of an exposure effect. We then introduce Translation-Aware Contamination Detection (TACD), a training-data-free diagnostic based on cross-lingual prediction consistency and choice reordering. Cross-lingual consistency is substantially higher than an independence baseline and generally increases relative to the clean condition, although its magnitude is model-dependent and not strictly monotonic. These results show that translation can conceal contamination-related effects from English-only probes and motivate multilingual diagnostics that are explicitly framed as evidence of contamination-consistent behavior rather than definitive membership tests.

## 05-039 | Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets
- arXiv: 2410.04579  first public: 2024-10-06  latest: 2025-03-09  primary cat: cs.CL
- authors (5): Tianjian Li; Haoran Xu; Weiting Tan; Kenton Murray; Daniel Khashabi
- seed subtopic: 语言配比与采样温度; type: 原始研究; cross: ['07']
- arXiv comment: 19 pages, 9 figures, accepted to NAACL 2025 main conference
- pages: 19

ABSTRACT: Data abundance across different domains exhibits a long-tailed distribution: few domains have abundant data, while most face data scarcity. Our work focuses on a multilingual setting, where available data is heavily skewed towards high-resource languages. Two common strategies to address this disparity are upsampling low-resource data (Temperature Sampling) and upweighting low-resource loss (Scalarization). These methods are often assumed to be equivalent, but this equivalence has not been rigorously established, prompting our investigation. Through theoretical and empirical analysis, we identify when these two methods are equivalent and when they diverge. We prove that they are equivalent under full gradient descent but differ under stochastic gradient descent due to differences in gradient variance. Specifically, Temperature Sampling exhibits lower variance in gradient estimation compared to Scalarization, leading to faster convergence but a higher risk of overfitting. Based on these insights, we propose Cooldown, a strategy that starts by heavily upsampling low-resource languages to accelerate convergence and gradually reduces the upsampling to prevent overfitting -- achieving the best of both worlds. Our method competes effectively with existing data re-weighting techniques while offering computational efficiency.

## 05-040 | Separating the Wheat from the Chaff with BREAD: An open-source benchmark and metrics to detect redundancy in text
- arXiv: 2311.06440  first public: 2023-11-11  latest: 2023-11-11  primary cat: cs.CL
- authors (3): Isaac Caswell; Lisa Wang; Isabel Papadimitriou
- seed subtopic: 去重与冗余检测; type: 基准与数据集; cross: []
- arXiv comment: Accepted to GEM workshop 2023; 6 pages
- URLs on first pages of PDF: https://github.com/toizzy/
- pages: 15

ABSTRACT: Data quality is a problem that perpetually resurfaces throughout the field of NLP, regardless of task, domain, or architecture, and remains especially severe for lower-resource languages. A typical and insidious issue, affecting both training data and model output, is data that is repetitive and dominated by linguistically uninteresting boilerplate, such as price catalogs or computer-generated log files. Though this problem permeates many web-scraped corpora, there has yet to be a benchmark to test against, or a systematic study to find simple metrics that generalize across languages and agree with human judgements of data quality. In the present work, we create and release BREAD, a human-labeled benchmark on repetitive boilerplate vs. plausible linguistic content, spanning 360 languages. We release several baseline CRED (Character REDundancy) scores along with it, and evaluate their effectiveness on BREAD. We hope that the community will use this resource to develop better filtering methods, and that our reference implementations of CRED scores can become standard corpus evaluation tools, driving the development of cleaner language modeling corpora, especially in low-resource languages.

## 05-041 | NADI 2024: The Fifth Nuanced Arabic Dialect Identification Shared Task
- arXiv: 2407.04910  first public: 2024-07-06  latest: 2024-07-06  primary cat: cs.CL
- authors (8): Muhammad Abdul-Mageed; Amr Keleg; AbdelRahim Elmadany; Chiyu Zhang; Injy Hamed; Walid Magdy ...
- seed subtopic: 方言识别; type: 基准与数据集; cross: []
- arXiv comment: Accepted by The Second Arabic Natural Language Processing Conference
- pages: 20

ABSTRACT: We describe the findings of the fifth Nuanced Arabic Dialect Identification Shared Task (NADI 2024). NADI's objective is to help advance SoTA Arabic NLP by providing guidance, datasets, modeling opportunities, and standardized evaluation conditions that allow researchers to collaboratively compete on pre-specified tasks. NADI 2024 targeted both dialect identification cast as a multi-label task (Subtask~1), identification of the Arabic level of dialectness (Subtask~2), and dialect-to-MSA machine translation (Subtask~3). A total of 51 unique teams registered for the shared task, of whom 12 teams have participated (with 76 valid submissions during the test phase). Among these, three teams participated in Subtask~1, three in Subtask~2, and eight in Subtask~3. The winning teams achieved 50.57 F\textsubscript{1} on Subtask~1, 0.1403 RMSE for Subtask~2, and 20.44 BLEU in Subtask~3, respectively. Results show that Arabic dialect processing tasks such as dialect identification and machine translation remain challenging. We describe the methods employed by the participating teams and briefly offer an outlook for NADI.

## 05-042 | A Survey on Data Selection for Language Models
- arXiv: 2402.16827  first public: 2024-02-26  latest: 2024-08-02  primary cat: cs.CL
- authors (14): Alon Albalak; Yanai Elazar; Sang Michael Xie; Shayne Longpre; Nathan Lambert; Xinyi Wang ...
- seed subtopic: 数据筛选综述; type: 综述; cross: []
- arXiv comment: Paper list available at https://github.com/alon-albalak/data-selection-survey
- pages: 81

ABSTRACT: A major factor in the recent success of large language models is the use of enormous and ever-growing text datasets for unsupervised pre-training. However, naively training a model on all available data may not be optimal (or feasible), as the quality of available text data can vary. Filtering out data can also decrease the carbon footprint and financial costs of training models by reducing the amount of training required. Data selection methods aim to determine which candidate data points to include in the training dataset and how to appropriately sample from the selected data points. The promise of improved data selection methods has caused the volume of research in the area to rapidly expand. However, because deep learning is mostly driven by empirical evidence and experimentation on large-scale data is expensive, few organizations have the resources for extensive data selection research. Consequently, knowledge of effective data selection practices has become concentrated within a few organizations, many of which do not openly share their findings and methodologies. To narrow this gap in knowledge, we present a comprehensive review of existing literature on data selection methods and related research areas, providing a taxonomy of existing approaches. By describing the current landscape of research, this work aims to accelerate progress in data selection by establishing an entry point for new and established researchers. Additionally, throughout this review we draw attention to noticeable holes in the literature and conclude the paper by proposing promising avenues for future research.

## 05-043 | Benchmark Data Contamination of Large Language Models: A Survey
- arXiv: 2406.04244  first public: 2024-06-06  latest: 2024-06-06  primary cat: cs.CL
- authors (4): Cheng Xu; Shuhao Guan; Derek Greene; M-Tahar Kechadi
- seed subtopic: 基准污染检测; type: 综述; cross: []
- arXiv comment: 31 pages, 7 figures, 3 tables
- pages: 31

ABSTRACT: The rapid development of Large Language Models (LLMs) like GPT-4, Claude-3, and Gemini has transformed the field of natural language processing. However, it has also resulted in a significant issue known as Benchmark Data Contamination (BDC). This occurs when language models inadvertently incorporate evaluation benchmark information from their training data, leading to inaccurate or unreliable performance during the evaluation phase of the process. This paper reviews the complex challenge of BDC in LLM evaluation and explores alternative assessment methods to mitigate the risks associated with traditional benchmarks. The paper also examines challenges and future directions in mitigating BDC risks, highlighting the complexity of the issue and the need for innovative solutions to ensure the reliability of LLM evaluation in real-world applications.

## 05-044 | Geographically-Informed Language Identification
- arXiv: 2403.09892  first public: 2024-03-14  latest: 2024-03-14  primary cat: cs.CL
- authors (2): Jonathan Dunn; Lane Edwards-Brown
- seed subtopic: 语言识别（地理先验）; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/glottolog/glottolog https://github.com/jonathandunn/geoLid
- pages: 11

ABSTRACT: This paper develops an approach to language identification in which the set of languages considered by the model depends on the geographic origin of the text in question. Given that many digital corpora can be geo-referenced at the country level, this paper formulates 16 region-specific models, each of which contains the languages expected to appear in countries within that region. These regional models also each include 31 widely-spoken international languages in order to ensure coverage of these linguae francae regardless of location. An upstream evaluation using traditional language identification testing data shows an improvement in f-score ranging from 1.7 points (Southeast Asia) to as much as 10.4 points (North Africa). A downstream evaluation on social media data shows that this improved performance has a significant impact on the language labels which are applied to large real-world corpora. The result is a highly-accurate model that covers 916 languages at a sample size of 50 characters, the performance improved by incorporating geographic information into the model.
