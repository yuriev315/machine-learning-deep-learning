# Brief for annotation: 09 合成数据、翻译与蒸馏

## 09-015 | Syntax as a Rosetta Stone: Universal Dependencies for In-Context Coptic Translation
- arXiv: 2604.18758  first public: 2026-04-20  latest: 2026-05-26  primary cat: cs.CL
- authors (4): Abhishek Purushothama; Emma Thronson; Alexia Guo; Amir Zeldes
- seed subtopic: LLM 低资源机器翻译（语法书/词典/上下文）; type: 原始研究; cross: []
- arXiv comment: ACL 2026 Findings camera-ready, with fixes
- pages: 20

ABSTRACT: Low-resource machine translation requires methods that differ from those used for high-resource languages. This paper proposes a novel in-context learning approach to support low-resource machine translation of the Coptic language to English, with syntactic augmentation from Universal Dependencies parses of input sentences. Building on existing work using bilingual dictionaries to support inference for vocabulary items, we add several representations of syntactic analyses to our inputs , specifically exploring the inclusion of raw parser outputs, verbalizations of parses in plain English, and targeted instructions of difficult constructions identified in sub-trees and how they can be translated. Our results show that while syntactic information alone is not as useful as dictionary-based glosses, combining retrieved dictionary items with syntactic information achieves significant gains across model sizes, achieving new state-of-the-art translation results for Coptic.

## 09-016 | Beyond Many-Shot Translation: Scaling In-Context Demonstrations For Low-Resource Machine Translation
- arXiv: 2602.04764  first public: 2026-02-04  latest: 2026-02-04  primary cat: cs.CL
- authors (5): Luis Frentzen Salim; Esteban Carlin; Alexandre Morinvil; Xi Ai; Lun-Wei Ku
- seed subtopic: LLM 低资源机器翻译（语法书/词典/上下文）; type: 原始研究; cross: ['11']
- arXiv comment: 8 pages, 18 figures, EACL 2026 Conference - LoResMT workshop
- pages: 20

ABSTRACT: Building machine translation (MT) systems for low-resource languages is notably difficult due to the scarcity of high-quality data. Although Large Language Models (LLMs) have improved MT system performance, adapting them to lesser-represented languages remains challenging. In-context learning (ICL) may offer novel ways to adapt LLMs for low-resource MT by conditioning models on demonstration at inference time. In this study, we explore scaling low-resource machine translation ICL beyond the few-shot setting to thousands of examples with long-context models. We scale in-context token budget to 1M tokens and compare three types of training corpora used as in-context supervision: monolingual unsupervised data, instruction-style data, and parallel data (English--target and Indonesian--target). Our experiments on Javanese and Sundanese show that gains from additional context saturate quickly and can degrade near the maximum context window, with scaling behavior strongly dependent on corpus type. Notably, some forms of monolingual supervision can be competitive with parallel data, despite the latter offering additional supervision. Overall, our results characterize the effective limits and corpus-type sensitivity of long-context ICL for low-resource MT, highlighting that larger context windows do not necessarily yield proportional quality gains.

## 09-064 | SMOL: Professionally translated parallel data for 115 under-represented languages
- arXiv: 2502.12301  first public: 2025-02-17  latest: 2025-10-31  primary cat: cs.CL
- authors (26): Isaac Caswell; Elizabeth Nielsen; Jiaming Luo; Colin Cherry; Geza Kovacs; Hadar Shemtov ...
- seed subtopic: 综述与数据资源; type: 基准与数据集; cross: ['04']
- arXiv comment: ~10 pages with appendices
- URLs on first pages of PDF: https://huggingface.co/datasets?multilinguality=
- pages: 21

ABSTRACT: We open-source SMOL (Set of Maximal Overall Leverage), a suite of training data to unlock machine translation for low-resource languages. SMOL has been translated into 124 (and growing) under-resourced languages (125 language pairs), including many for which there exist no previous public resources, for a total of 6.1M translated tokens. SMOL comprises two sub-datasets, each carefully chosen for maximum impact given its size: SMOLSENT, a set of sentences chosen for broad unique token coverage, and SMOLDOC, a document-level resource focusing on a broad topic coverage. They join the already released GATITOS for a trifecta of paragraph, sentence, and token-level content. We demonstrate that using SMOL to prompt or fine-tune Large Language Models yields robust chrF improvements. In addition to translation, we provide factuality ratings and rationales for all documents in SMOLDOC, yielding the first factuality datasets for most of these languages.

## 09-067 | TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation
- arXiv: 2608.18655  first public: 2026-08-19  latest: 2026-08-26  primary cat: cs.CL
- authors (4): Milan Gritta; Patrik Lambert; Jihye Back; Amril Nazir
- seed subtopic: LLM 合成数据与回译用于低资源 MT; type: 原始研究; cross: []
- arXiv comment: EMNLP 2026 (main conference)
- URLs on first pages of PDF: https://huggingface.co/Masakhane/africomet-qe-stl-1.1 https://huggingface.co/McGill-NLP/ssa-comet-mtl https://huggingface.co/collections/qvac/ https://huggingface.co/datasets/AfriNLP/AfriNLLB-train https://huggingface.co/google/
- pages: 27

ABSTRACT: The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent. Recent open-source LLMs systematically underperform on African language machine translation, while the lack of large-scale, high-quality, open-source parallel data has constrained the development of competitive small language models (SLMs). We introduce TranslatePsy-AfriSLM, a collection of open-source machine translation resources for 19 Sub-Saharan African languages, including curated parallel data, African-specialized synthetic data, and a family of fine-tuned SLMs. Our empirical study shows that unified quality-estimation filtering removes up to 96% of training tokens without degrading quality, and that filtered synthetic data dominates the quality-efficiency Pareto frontier. Fine-tuned on the resulting data mixture, TranslatePsy-AfriSLMs outperform substantially larger systems, including TranslateGemma-27B and Qwen3.5-122B-A10B, with as few as 0.8B parameters.

## 09-068 | Tower: An Open Multilingual Large Language Model for Translation-Related Tasks
- arXiv: 2402.17733  first public: 2024-02-27  latest: 2024-02-27  primary cat: cs.CL
- authors (13): Duarte M. Alves; José Pombal; Nuno M. Guerreiro; Pedro H. Martins; João Alves; Amin Farajian ...
- seed subtopic: LLM 合成数据与回译用于低资源 MT; type: 技术报告; cross: ['07']
- pages: 34

ABSTRACT: While general-purpose large language models (LLMs) demonstrate proficiency on multiple tasks within the domain of translation, approaches based on open LLMs are competitive only when specializing on a single task. In this paper, we propose a recipe for tailoring LLMs to multiple tasks present in translation workflows. We perform continued pretraining on a multilingual mixture of monolingual and parallel data, creating TowerBase, followed by finetuning on instructions relevant for translation processes, creating TowerInstruct. Our final model surpasses open alternatives on several tasks relevant to translation workflows and is competitive with general-purpose closed LLMs. To facilitate future research, we release the Tower models, our specialization dataset, an evaluation framework for LLMs focusing on the translation ecosystem, and a collection of model generations, including ours, on our benchmark.

## 09-069 | Exploring In-context Example Generation for Machine Translation
- arXiv: 2506.00507  first public: 2025-05-31  latest: 2025-05-31  primary cat: cs.CL
- authors (5): Dohyun Lee; Seungil Chad Lee; Chanwoo Yang; Yujin Baek; Jaegul Choo
- seed subtopic: LLM 低资源机器翻译（语法书/词典/上下文）; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2025 Findings
- URLs on first pages of PDF: https://github.com/aiclaudev/DAT
- pages: 15

ABSTRACT: Large language models (LLMs) have demonstrated strong performance across various tasks, leveraging their exceptional in-context learning ability with only a few examples. Accordingly, the selection of optimal in-context examples has been actively studied in the field of machine translation. However, these studies presuppose the presence of a demonstration pool with human-annotated pairs, making them less applicable to low-resource languages where such an assumption is challenging to meet. To overcome this limitation, this paper explores the research direction of in-context example generation for machine translation. Specifically, we propose Demonstration Augmentation for Translation (DAT), a simple yet effective approach that generates example pairs without relying on any external resources. This method builds upon two prior criteria, relevance and diversity, which have been highlighted in previous work as key factors for in-context example selection. Through experiments and analysis on low-resource languages where human-annotated pairs are scarce, we show that DAT achieves superior translation quality compared to the baselines. Furthermore, we investigate the potential of progressively accumulating generated pairs during test time to build and reuse a demonstration pool. Our implementation is publicly available at https://github.com/aiclaudev/DAT.
