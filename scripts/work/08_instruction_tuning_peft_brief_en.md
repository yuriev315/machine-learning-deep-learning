# Brief for annotation: 08 指令微调与参数高效适配

## 08-001 | Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning
- arXiv: 2402.06619  first public: 2024-02-09  latest: 2024-02-09  primary cat: cs.CL
- authors (33): Shivalika Singh; Freddie Vargus; Daniel Dsouza; Börje F. Karlsson; Abinaya Mahendiran; Wei-Yin Ko ...
- seed subtopic: 本地语言指令数据; type: 基准与数据集; cross: ['04']
- pages: 124

ABSTRACT: Datasets are foundational to many breakthroughs in modern artificial intelligence. Many recent achievements in the space of natural language processing (NLP) can be attributed to the finetuning of pre-trained models on a diverse set of tasks that enables a large language model (LLM) to respond to instructions. Instruction fine-tuning (IFT) requires specifically constructed and annotated datasets. However, existing datasets are almost all in the English language. In this work, our primary goal is to bridge the language gap by building a human-curated instruction-following dataset spanning 65 languages. We worked with fluent speakers of languages from around the world to collect natural instances of instructions and completions. Furthermore, we create the most extensive multilingual collection to date, comprising 513 million instances through templating and translating existing datasets across 114 languages. In total, we contribute four key resources: we develop and open-source the Aya Annotation Platform, the Aya Dataset, the Aya Collection, and the Aya Evaluation Suite. The Aya initiative also serves as a valuable case study in participatory research, involving collaborators from 119 countries. We see this as a valuable framework for future research collaborations that aim to bridge gaps in resources.

## 08-002 | Multilingual Instruction Tuning With Just a Pinch of Multilinguality
- arXiv: 2401.01854  first public: 2024-01-03  latest: 2024-05-21  primary cat: cs.CL
- authors (6): Uri Shaham; Jonathan Herzig; Roee Aharoni; Idan Szpektor; Reut Tsarfaty; Matan Eyal
- seed subtopic: 多语指令迁移; type: 原始研究; cross: []
- arXiv comment: Findings of ACL 2024
- pages: 14

ABSTRACT: As instruction-tuned large language models (LLMs) gain global adoption, their ability to follow instructions in multiple languages becomes increasingly crucial. In this work, we investigate how multilinguality during instruction tuning of a multilingual LLM affects instruction-following across languages from the pre-training corpus. We first show that many languages transfer some instruction-following capabilities to other languages from even monolingual tuning. Furthermore, we find that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, both in seen and unseen languages during tuning. In general, we observe that models tuned on multilingual mixtures exhibit comparable or superior performance in multiple languages compared to monolingually tuned models, despite training on 10x fewer examples in those languages. Finally, we find that diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization. Our results suggest that building massively multilingual instruction-tuned models can be done with only a very small set of multilingual instruction-responses.

## 08-003 | Turning English-centric LLMs Into Polyglots: How Much Multilinguality Is Needed?
- arXiv: 2312.12683  first public: 2023-12-20  latest: 2024-10-03  primary cat: cs.CL
- authors (3): Tannon Kew; Florian Schottmann; Rico Sennrich
- seed subtopic: 多语指令迁移; type: 原始研究; cross: []
- arXiv comment: Accepted at Findings of EMNLP 2024
- URLs on first pages of PDF: https://github.com/huggingface/trl https://github.com/openai/gpt-3/blob/master/
- pages: 28

ABSTRACT: The vast majority of today's large language models (LLMs) are English-centric, having been pretrained predominantly on English text. Yet, in order to meet user expectations, models need to be able to respond appropriately in multiple languages once deployed in downstream applications. This requires strong cross-lingual transfer abilities. In this work, we investigate the minimal amount of multilinguality required during finetuning to elicit cross-lingual generalisation in English-centric LLMs. In experiments across four LLMs, we find that multilingual instruction tuning with as few as two to three languages is both necessary and sufficient to elicit effective cross-lingual generalisation, with the limiting factor being the degree to which a target language is seen during pretraining. Evaluations on five different tasks further reveal that multilingual instruction tuning is most beneficial for generative tasks that assume input/output language agreement, such as in chat settings, while being of less importance for highly structured classification-style tasks. Our code and data is available at https://github.com/ZurichNLP/multilingual-instruction-tuning.

## 08-004 | Zero-shot cross-lingual transfer in instruction tuning of large language models
- arXiv: 2402.14778  first public: 2024-02-22  latest: 2024-04-22  primary cat: cs.CL
- authors (2): Nadezhda Chirkova; Vassilina Nikoulina
- seed subtopic: 仅英文指令的跨语言迁移; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Instruction tuning (IT) is widely used to teach pretrained large language models (LLMs) to follow arbitrary instructions, but is under-studied in multilingual settings. In this work, we conduct a systematic study of zero-shot cross-lingual transfer in IT, when an LLM is instruction-tuned on English-only data and then tested on user prompts in other languages. We advocate for the importance of evaluating various aspects of model responses in multilingual instruction following and investigate the influence of different model configuration choices. We find that cross-lingual transfer does happen successfully in IT even if all stages of model training are English-centric, but only if multiliguality is taken into account in hyperparameter tuning and with large enough IT data. English-trained LLMs are capable of generating correct-language, comprehensive and helpful responses in other languages, but suffer from low factuality and may occasionally have fluency errors.

## 08-005 | How Many Languages Make Good Multilingual Instruction Tuning? A Case Study on BLOOM
- arXiv: 2404.04850  first public: 2024-04-07  latest: 2024-12-09  primary cat: cs.CL
- authors (2): Shaoxiong Ji; Pinzhen Chen
- seed subtopic: 指令语言数量; type: 原始研究; cross: []
- arXiv comment: COLING 2025
- pages: 7

ABSTRACT: Instruction tuning a large language model with multiple languages can prepare it for multilingual downstream tasks. Nonetheless, it is yet to be determined whether having a handful of languages is sufficient, or whether the benefits increase with the inclusion of more. By fine-tuning large multilingual models on 1 to 52 languages, we present a case study on BLOOM to understand three pertinent factors affecting performance: the number of languages, language exposure, and similarity between training and test languages. Overall we found that 1) expanding language coverage in multilingual instruction tuning proves to be beneficial; 2) accuracy often significantly boots if the test language appears in the instruction mixture; 3) languages' genetic features correlate with cross-lingual transfer more than merely the number of language but different languages benefit to various degrees.

## 08-006 | Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?
- arXiv: 2402.13703  first public: 2024-02-21  latest: 2024-10-10  primary cat: cs.CL
- authors (7): Alexander Arno Weber; Klaudia Thellmann; Jan Ebert; Nicolas Flores-Herr; Jens Lehmann; Michael Fromm ...
- seed subtopic: 多语指令迁移; type: 原始研究; cross: []
- arXiv comment: Accepted for EMNLP 2024 (Main), 27 pages, 8 figures
- URLs on first pages of PDF: https://github.com/Modalities/MT-Bench-X
- pages: 27

ABSTRACT: The adaption of multilingual pre-trained LLMs into eloquent and helpful assistants is essential to facilitate their use across different language regions. In that spirit, we are the first to conduct an extensive study of the performance of multilingual models instruction-tuned on different language compositions on parallel instruction-tuning benchmarks across a selection of the most spoken Indo-European languages. We systematically examine the effects of language and instruction dataset size on a mid-sized and a large, multilingual LLMs by instruction-tuning them on parallel instruction-tuning datasets. Our results demonstrate that instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%. Furthermore, we show that the Superficial Alignment Hypothesis does not hold in general, as the investigated multilingual 7B parameter model presents a counter-example requiring large-scale instruction-tuning datasets. Finally, we conduct a human annotation study to understand the alignment between human-based and GPT-4-based evaluation within multilingual chat scenarios.

## 08-007 | A Post-trainer's Guide to Multilingual Training Data: Uncovering Cross-lingual Transfer Dynamics
- arXiv: 2504.16677  first public: 2025-04-23  latest: 2025-04-23  primary cat: cs.CL
- authors (4): Luisa Shimabucoro; Ahmet Ustun; Marzieh Fadaee; Sebastian Ruder
- seed subtopic: 后训练多语数据; type: 原始研究; cross: []
- pages: 18

ABSTRACT: In order for large language models to be useful across the globe, they are fine-tuned to follow instructions on multilingual data. Despite the ubiquity of such post-training, a clear understanding of the dynamics that enable cross-lingual transfer remains elusive. This study examines cross-lingual transfer (CLT) dynamics in realistic post-training settings. We study two model families of up to 35B parameters in size trained on carefully controlled mixtures of multilingual data on three generative tasks with varying levels of complexity (summarization, instruction following, and mathematical reasoning) in both single-task and multi-task instruction tuning settings. Overall, we find that the dynamics of cross-lingual transfer and multilingual performance cannot be explained by isolated variables, varying depending on the combination of post-training settings. Finally, we identify the conditions that lead to effective cross-lingual transfer in practice.

## 08-008 | Monolingual or Multilingual Instruction Tuning: Which Makes a Better Alpaca
- arXiv: 2309.08958  first public: 2023-09-16  latest: 2024-01-31  primary cat: cs.CL
- authors (6): Pinzhen Chen; Shaoxiong Ji; Nikolay Bogoychev; Andrey Kutuzov; Barry Haddow; Kenneth Heafield
- seed subtopic: 单语 vs 多语指令微调; type: 原始研究; cross: []
- arXiv comment: Accepted to Findings of ACL: EACL 2024. Added human evaluation and shortened writing
- URLs on first pages of PDF: https://github.com/browsermt/ https://github.com/gururise/alpacadatacleaned https://github.com/hplt-project/
- pages: 10

ABSTRACT: Foundational large language models (LLMs) can be instruction-tuned to perform open-domain question answering, facilitating applications like chat assistants. While such efforts are often carried out in a single language, we empirically analyze cost-efficient strategies for multilingual scenarios. Our study employs the Alpaca dataset and machine translations of it to form multilingual data, which is then used to tune LLMs through either low-rank adaptation or full-parameter training. Under a controlled computation budget, comparisons show that multilingual tuning is on par or better than tuning a model for each language. Furthermore, multilingual tuning with downsampled data can be as powerful and more robust. Our findings serve as a guide for expanding language support through instruction tuning.

## 08-009 | Crosslingual Generalization through Multitask Finetuning
- arXiv: 2211.01786  first public: 2022-11-03  latest: 2023-05-29  primary cat: cs.CL
- authors (19): Niklas Muennighoff; Thomas Wang; Lintang Sutawika; Adam Roberts; Stella Biderman; Teven Le Scao ...
- seed subtopic: 多语多任务微调; type: 原始研究; cross: []
- arXiv comment: 9 main pages (119 with appendix), 16 figures and 11 tables
- pages: 119

ABSTRACT: Multitask prompted finetuning (MTF) has been shown to help large language models generalize to new tasks in a zero-shot setting, but so far explorations of MTF have focused on English data and models. We apply MTF to the pretrained multilingual BLOOM and mT5 model families to produce finetuned variants called BLOOMZ and mT0. We find finetuning large multilingual language models on English tasks with English prompts allows for task generalization to non-English languages that appear only in the pretraining corpus. Finetuning on multilingual tasks with English prompts further improves performance on English and non-English tasks leading to various state-of-the-art zero-shot results. We also investigate finetuning on multilingual tasks with prompts that have been machine-translated from English to match the language of each dataset. We find training on these machine-translated prompts leads to better performance on human-written prompts in the respective languages. Surprisingly, we find models are capable of zero-shot generalization to tasks in languages they have never intentionally seen. We conjecture that the models are learning higher-level capabilities that are both task- and language-agnostic. In addition, we introduce xP3, a composite of supervised datasets in 46 languages with English and machine-translated prompts. Our code, datasets and models are freely available at https://github.com/bigscience-workshop/xmtf.

## 08-010 | LoRA: Low-Rank Adaptation of Large Language Models
- arXiv: 2106.09685  first public: 2021-06-17  latest: 2021-10-16  primary cat: cs.CL
- authors (8): Edward J. Hu; Yelong Shen; Phillip Wallis; Zeyuan Allen-Zhu; Yuanzhi Li; Shean Wang ...
- seed subtopic: 低秩适配; type: 原始研究; cross: []
- arXiv comment: Draft V2 includes better baselines, experiments on GLUE, and more on adapter latency
- URLs on first pages of PDF: https://github.com/microsoft/LoRA
- pages: 26

ABSTRACT: An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at https://github.com/microsoft/LoRA.

## 08-011 | QLoRA: Efficient Finetuning of Quantized LLMs
- arXiv: 2305.14314  first public: 2023-05-23  latest: 2023-05-23  primary cat: cs.LG
- authors (4): Tim Dettmers; Artidoro Pagnoni; Ari Holtzman; Luke Zettlemoyer
- seed subtopic: 量化低秩适配; type: 原始研究; cross: ['16']
- arXiv comment: Extended NeurIPS submission
- URLs on first pages of PDF: https://github.com/TimDettmers/bitsandbytes https://github.com/artidoro/qlora
- pages: 26

ABSTRACT: We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters~(LoRA). Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) double quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) paged optimziers to manage memory spikes. We use QLoRA to finetune more than 1,000 models, providing a detailed analysis of instruction following and chatbot performance across 8 instruction datasets, multiple model types (LLaMA, T5), and model scales that would be infeasible to run with regular finetuning (e.g. 33B and 65B parameter models). Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when using smaller models than the previous SoTA. We provide a detailed analysis of chatbot performance based on both human and GPT-4 evaluations showing that GPT-4 evaluations are a cheap and reasonable alternative to human evaluation. Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots. A lemon-picked analysis demonstrates where Guanaco fails compared to ChatGPT. We release all of our models and code, including CUDA kernels for 4-bit training.

## 08-012 | DoRA: Weight-Decomposed Low-Rank Adaptation
- arXiv: 2402.09353  first public: 2024-02-14  latest: 2024-07-09  primary cat: cs.CL
- authors (7): Shih-Yang Liu; Chien-Yi Wang; Hongxu Yin; Pavlo Molchanov; Yu-Chiang Frank Wang; Kwang-Ting Cheng ...
- seed subtopic: LoRA 变体; type: 原始研究; cross: []
- arXiv comment: ICML2024(Oral)
- pages: 23

ABSTRACT: Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs. However, there still often exists an accuracy gap between these methods and full fine-tuning (FT). In this work, we first introduce a novel weight decomposition analysis to investigate the inherent differences between FT and LoRA. Aiming to resemble the learning capacity of FT from the findings, we propose Weight-Decomposed Low-Rank Adaptation (DoRA). DoRA decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning, specifically employing LoRA for directional updates to efficiently minimize the number of trainable parameters. By employing \ours, we enhance both the learning capacity and training stability of LoRA while avoiding any additional inference overhead. \ours~consistently outperforms LoRA on fine-tuning LLaMA, LLaVA, and VL-BART on various downstream tasks, such as commonsense reasoning, visual instruction tuning, and image/video-text understanding. Code is available at https://github.com/NVlabs/DoRA.

## 08-013 | LoRA Learns Less and Forgets Less
- arXiv: 2405.09673  first public: 2024-05-15  latest: 2024-09-20  primary cat: cs.LG
- authors (12): Dan Biderman; Jacob Portes; Jose Javier Gonzalez Ortiz; Mansheej Paul; Philip Greengard; Connor Jennings ...
- seed subtopic: LoRA 与遗忘; type: 原始研究; cross: []
- arXiv comment: Final version with new experiments and analyses, as accepted to Transactions on Machine Learning Research, August 2024 (Featured Certification). https://openreview.net/forum?id=aloEru2qCG&noteId=Jb3PQNQDI2
- URLs on first pages of PDF: https://github.com/danbider/lora-tradeoffs https://github.com/mosaicml/composer https://github.com/mosaicml/llm-foundry https://github.com/mosaicml/streaming https://huggingface.co/datasets/open-web-math/open-web-math
- pages: 39

ABSTRACT: Low-Rank Adaptation (LoRA) is a widely-used parameter-efficient finetuning method for large language models. LoRA saves memory by training only low rank perturbations to selected weight matrices. In this work, we compare the performance of LoRA and full finetuning on two target domains, programming and mathematics. We consider both the instruction finetuning (approximately 100K prompt-response pairs) and continued pretraining (20B unstructured tokens) data regimes. Our results show that, in the standard low-rank settings, LoRA substantially underperforms full finetuning. Nevertheless, LoRA better maintains the base model's performance on tasks outside the target domain. We show that LoRA mitigates forgetting more than common regularization techniques such as weight decay and dropout; it also helps maintain more diverse generations. Finally, we show that full finetuning learns perturbations with a rank that is 10-100X greater than typical LoRA configurations, possibly explaining some of the reported gaps. We conclude by proposing best practices for finetuning with LoRA.

## 08-014 | Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey
- arXiv: 2403.14608  first public: 2024-03-21  latest: 2024-09-16  primary cat: cs.LG
- authors (5): Zeyu Han; Chao Gao; Jinyang Liu; Jeff Zhang; Sai Qian Zhang
- seed subtopic: PEFT 综述; type: 综述; cross: []
- arXiv comment: 25 pages, 12 figures. Due to word limit, the abstract here is truncated. The full abstract is available in the PDF
- pages: 25

ABSTRACT: Large models represent a groundbreaking advancement in multiple application fields, enabling remarkable achievements across various tasks. However, their unprecedented scale comes with significant computational costs. These models, often consisting of billions of parameters, require vast amounts of computational resources for execution. Especially, the expansive scale and computational demands pose considerable challenges when customizing them for particular downstream tasks, particularly over the hardware platforms constrained by computational capabilities. Parameter Efficient Fine-Tuning (PEFT) provides a practical solution by efficiently adjusting the large models over the various downstream tasks. In particular, PEFT refers to the process of adjusting the parameters of a pre-trained large model to adapt it to a specific task or domain while minimizing the number of additional parameters introduced or computational resources required. This approach is particularly important when dealing with large-scale language models with high parameter counts, as fine-tuning these models from scratch can be computationally expensive and resource-intensive, posing considerable challenges in the supporting system platform design. In this survey, we present comprehensive studies of various PEFT algorithms, examining their performance and computational overhead. Moreover, we provide an overview of applications developed using different PEFT algorithms and discuss common techniques employed to mitigate computation costs for PEFT. In addition to providing an extensive survey from an algorithmic standpoint, we also examine various real-world system designs to investigate the implementation costs associated with different PEFT approaches. This survey serves as a valuable resource for researchers aiming to understand both the PEFT algorithm and its system implementation, offering detailed ......

## 08-015 | Instructing Large Language Models for Low-Resource Languages: A Systematic Study for Basque
- arXiv: 2506.07597  first public: 2025-06-09  latest: 2026-03-13  primary cat: cs.CL
- authors (12): Oscar Sainz; Naiara Perez; Julen Etxaniz; Joseba Fernandez de Landa; Itziar Aldabe; Iker García-Ferrero ...
- seed subtopic: 低资源语言指令化; type: 原始研究; cross: ['09']
- arXiv comment: Accepted at EMNLP 2025 Main Conference
- pages: 25

ABSTRACT: Instructing language models with user intent requires large instruction datasets, which are only available for a limited set of languages. In this paper, we explore alternatives to conventional instruction adaptation pipelines in low-resource scenarios. We assume a realistic scenario for low-resource languages, where only the following are available: corpora in the target language, existing open-weight multilingual base and instructed backbone LLMs, and synthetically generated instructions sampled from the instructed backbone. We present a comprehensive set of experiments for Basque that systematically study different combinations of these components evaluated on benchmarks and human preferences from 1,680 participants. Our conclusions show that target language corpora are essential, with synthetic instructions yielding robust models, and, most importantly, that using as backbone an instruction-tuned model outperforms using a base non-instructed model. Scaling up to Llama 3.1 Instruct 70B as backbone, our model comes near frontier models of much larger sizes for Basque, without using any Basque instructions. We release code, models, instruction datasets, and human preferences to support full reproducibility in future research on low-resource language adaptation. https://github.com/hitz-zentroa/latxa-instruct

## 08-016 | Pipeline Analysis for Developing Instruct LLMs in Low-Resource Languages: A Case Study on Basque
- arXiv: 2412.13922  first public: 2024-12-18  latest: 2024-12-18  primary cat: cs.CL
- authors (3): Ander Corral; Ixak Sarasua; Xabier Saralegi
- seed subtopic: 低资源指令模型流水线; type: 原始研究; cross: ['07']
- pages: 19

ABSTRACT: Large language models (LLMs) are typically optimized for resource-rich languages like English, exacerbating the gap between high-resource and underrepresented languages. This work presents a detailed analysis of strategies for developing a model capable of following instructions in a low-resource language, specifically Basque, by focusing on three key stages: pre-training, instruction tuning, and alignment with human preferences. Our findings demonstrate that continual pre-training with a high-quality Basque corpus of around 600 million words improves natural language understanding (NLU) of the foundational model by over 12 points. Moreover, instruction tuning and human preference alignment using automatically translated datasets proved highly effective, resulting in a 24-point improvement in instruction-following performance. The resulting models, Llama-eus-8B and Llama-eus-8B-instruct, establish a new state-of-the-art for Basque in the sub-10B parameter category.

## 08-017 | Airavata: Introducing Hindi Instruction-tuned LLM
- arXiv: 2401.15006  first public: 2024-01-26  latest: 2024-02-26  primary cat: cs.CL
- authors (11): Jay Gala; Thanmay Jayakumar; Jaavid Aktar Husain; Aswanth Kumar M; Mohammed Safi Ur Rahman Khan; Diptesh Kanojia ...
- seed subtopic: 印地语指令微调; type: 技术报告; cross: []
- arXiv comment: Work in progress
- URLs on first pages of PDF: https://ai4bharat.github.io/airavata https://huggingface.co/collections/ai4bharat/airavata-evaluation-suite https://huggingface.co/datasets/ai4bharat/indic-instruct-data-v0.1 https://huggingface.co/datasets/lmsys/lmsys-chat-1m#lmsys-chat-1m-dat
- pages: 20

ABSTRACT: We announce the initial release of "Airavata," an instruction-tuned LLM for Hindi. Airavata was created by fine-tuning OpenHathi with diverse, instruction-tuning Hindi datasets to make it better suited for assistive tasks. Along with the model, we also share the IndicInstruct dataset, which is a collection of diverse instruction-tuning datasets to enable further research for Indic LLMs. Additionally, we present evaluation benchmarks and a framework for assessing LLM performance across tasks in Hindi. Currently, Airavata supports Hindi, but we plan to expand this to all 22 scheduled Indic languages. You can access all artifacts at https://ai4bharat.github.io/airavata.

## 08-018 | Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh
- arXiv: 2502.13647  first public: 2025-02-19  latest: 2026-03-15  primary cat: cs.CL
- authors (7): Nurkhan Laiyk; Daniil Orel; Rituraj Joshi; Maiya Goloburda; Yuxia Wang; Preslav Nakov ...
- seed subtopic: 哈萨克语指令数据; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/nurkhan5l/
- pages: 30

ABSTRACT: Instruction tuning in low-resource languages remains underexplored due to limited text data, particularly in government and cultural domains. To address this, we introduce and open-source a large-scale (10,600 samples) instruction-following (IFT) dataset, covering key institutional and cultural knowledge relevant to Kazakhstan. Our dataset enhances LLMs' understanding of procedural, legal, and structural governance topics. We employ LLM-assisted data generation, comparing open-weight and closed-weight models for dataset construction, and select GPT-4o as the backbone. Each entity of our dataset undergoes full manual verification to ensure high quality. We also show that fine-tuning Qwen, Falcon, and Gemma on our dataset leads to consistent performance improvements in both multiple-choice and generative tasks, demonstrating the potential of LLM-assisted instruction tuning for low-resource languages.

## 08-019 | LuxIT: A Luxembourgish Instruction Tuning Dataset from Monolingual Seed Data
- arXiv: 2510.24434  first public: 2025-10-28  latest: 2026-08-22  primary cat: cs.CL
- authors (4): Julian Valline; Cedric Lothritz; Siwen Guo; Jordi Cabot
- seed subtopic: 卢森堡语指令数据; type: 基准与数据集; cross: ['09']
- arXiv comment: To appear in proceedings of LaTeLL 2026
- pages: 19

ABSTRACT: The effectiveness of instruction-tuned Large Language Models (LLMs) is often limited in low-resource linguistic settings due to a lack of high-quality training data. We introduce LuxIT, a monolingual instruction tuning dataset for Luxembourgish developed to mitigate this challenge. We synthesize the dataset from a corpus of native Luxembourgish texts, utilizing DeepSeek-R1-0528, chosen for its shown proficiency in Luxembourgish. Following generation, we apply a quality assurance process, employing an LLM-as-a-judge approach, retaining 227,507 high-quality instruction-answer pairs. To investigate the practical utility of the dataset, we fine-tune 14 smaller-scale LLMs ($\leq$15B parameters) on LuxIT and evaluate them on standardized Luxembourgish proficiency exams and five downstream NLP tasks. Training on LuxIT yields a mean accuracy change of +5.37 percentage points on language exams across all 14 models, with 12 of 14 showing improvement. On NLP downstream tasks, 9 of 14 models improve in macro-averaged F1, though gains on the two benchmarks do not systematically correlate. These results underscore the feasibility of leveraging monolingual synthetic data to improve LLM capabilities in low-resource languages, while highlighting the multi-faceted nature of language proficiency.

## 08-020 | Empowering Persian LLMs for Instruction Following: A Novel Dataset and Training Approach
- arXiv: 2407.11186  first public: 2024-07-15  latest: 2025-01-14  primary cat: cs.CL
- authors (4): Hojjat Mokhtarabadi; Ziba Zamani; Abbas Maazallahi; Mohammad Hossein Manshaei
- seed subtopic: 波斯语指令数据; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/Hojjat-Mokhtarabadi/ https://huggingface.co/datasets/PNLPhub/
- pages: 37

ABSTRACT: Instruction-tuned large language models have demonstrated remarkable capabilities in following human instructions across various domains. However, their proficiency remains notably deficient in many low-resource languages. To address this challenge, we begin by introducing FarsInstruct a comprehensive instruction dataset designed to enhance the instruction following ability of large language models specifically for the Persian language a significant yet underrepresented language globally. FarsInstruct encompasses a wide range of task types and datasets, each containing a mix of straightforward to complex manual written instructions, as well as translations from the Public Pool of Prompts, ensuring a rich linguistic and cultural representation. Furthermore, we introduce Co-CoLA, a framework designed to enhance the multi-task adaptability of LoRA-tuned models. Through extensive experimental analyses, our study showcases the effectiveness of the FarsInstruct dataset coupled with training by the Co-CoLA framework, in improving the performance of large language models within the Persian context. As of the current writing, FarsInstruct comprises 197 templates across 21 distinct datasets, and we intend to update it consistently, thus augmenting its applicability.

## 08-021 | WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation in Thai
- arXiv: 2508.15239  first public: 2025-08-21  latest: 2025-09-19  primary cat: cs.CL
- authors (8): Peerat Limkonchotiwat; Pume Tuchinda; Lalita Lowphansirikul; Surapon Nonesung; Panuthep Tasawong; Alham Fikri Aji ...
- seed subtopic: 泰语人工指令数据; type: 基准与数据集; cross: ['15']
- arXiv comment: Accepted to EMNLP 2025 (Main). Model and Dataset: https://huggingface.co/collections/airesearch/wangchan-thai-instruction-6835722a30b98e01598984fd
- URLs on first pages of PDF: https://huggingface.co/datasets/ https://huggingface.co/spaces/
- pages: 24

ABSTRACT: Large language models excel at instruction-following in English, but their performance in low-resource languages like Thai remains underexplored. Existing benchmarks often rely on translations, missing cultural and domain-specific nuances needed for real-world use. We present WangchanThaiInstruct, a human-authored Thai dataset for evaluation and instruction tuning, covering four professional domains and seven task types. Created through a multi-stage quality control process with annotators, domain experts, and AI researchers, WangchanThaiInstruct supports two studies: (1) a zero-shot evaluation showing performance gaps on culturally and professionally specific tasks, and (2) an instruction tuning study with ablations isolating the effect of native supervision. Models fine-tuned on WangchanThaiInstruct outperform those using translated data in both in-domain and out-of-domain benchmarks. These findings underscore the need for culturally and professionally grounded instruction data to improve LLM alignment in low-resource, linguistically diverse settings.

## 08-022 | Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning
- arXiv: 2411.18571  first public: 2024-11-27  latest: 2024-11-27  primary cat: cs.CL
- authors (5): Omkar Khade; Shruti Jagdale; Abhishek Phaltankar; Gauri Takalikar; Raviraj Joshi
- seed subtopic: LoRA 小语种适配; type: 原始研究; cross: []
- pages: 6

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable multilingual capabilities, yet challenges persist in adapting these models for low-resource languages. In this study, we investigate the effects of Low-Rank Adaptation (LoRA) Parameter-Efficient Fine-Tuning (PEFT) on multilingual Gemma models for Marathi, a language with limited resources. Using a translated Alpaca dataset with 52,000 instruction-response pairs, our findings reveal that while evaluation metrics often show a performance decline post-fine-tuning, manual assessments frequently suggest that the fine-tuned models outperform their original counterparts. The observations indicate improvements in target language generation capabilities but a reduction in reasoning abilities following language adaptation. These results underscore the need for improved evaluation methodologies and the creation of high-quality native datasets to accurately assess language-specific model performance in low-resource settings.

## 08-023 | Train More Parameters But Mind Their Placement: Insights into Language Adaptation with PEFT
- arXiv: 2412.12674  first public: 2024-12-17  latest: 2024-12-17  primary cat: cs.CL
- authors (1): Jenny Kunz
- seed subtopic: PEFT 语言适配; type: 原始研究; cross: []
- arXiv comment: To appear at NoDaLiDa 2025
- pages: 8

ABSTRACT: Smaller LLMs still face significant challenges even in medium-resourced languages, particularly when it comes to language-specific knowledge -- a problem not easily resolved with machine-translated data. In this case study on Icelandic, we aim to enhance the generation performance of an LLM by specialising it using unstructured text corpora. A key focus is on preventing interference with the models' capabilities of handling longer context during this adaptation. Through ablation studies using various parameter-efficient fine-tuning (PEFT) methods and setups, we find that increasing the number of trainable parameters leads to better and more robust language adaptation. LoRAs placed in the feed-forward layers and bottleneck adapters show promising results with sufficient parameters, while prefix tuning and (IA)3 are not suitable. Although improvements are consistent in 0-shot summarisation, some adapted models struggle with longer context lengths, an issue that can be mitigated by adapting only the final layers.

## 08-024 | MAPLE: Multilingual Evaluation of Parameter Efficient Finetuning of Large Language Models
- arXiv: 2401.07598  first public: 2024-01-15  latest: 2024-07-22  primary cat: cs.CL
- authors (4): Divyanshu Aggarwal; Ashutosh Sathe; Ishaan Watts; Sunayana Sitaram
- seed subtopic: 多语 PEFT 评估; type: 原始研究; cross: []
- arXiv comment: 46 pages, 23 figures, 45 tables. Accepted in ACL 2024 findings
- pages: 44

ABSTRACT: Parameter Efficient Finetuning (PEFT) has emerged as a viable solution for improving the performance of Large Language Models (LLMs) without requiring massive resources and compute. Prior work on multilingual evaluation has shown that there is a large gap between the performance of LLMs on English and other languages. Further, there is also a large gap between the performance of smaller open-source models and larger LLMs. Finetuning can be an effective way to bridge this gap and make language models more equitable. In this work, we finetune the LLama-2-7B and Mistral-7B models on two synthetic multilingual instruction tuning datasets to determine its effect on model performance on six downstream tasks covering forty languages in all. Additionally, we experiment with various parameters, such as rank for low-rank adaptation and values of quantisation to determine their effects on downstream performance and find that higher rank and higher quantisation values benefit low-resource languages. We find that PEFT of smaller open-source models sometimes bridges the gap between the performance of these models and the larger ones, however, English performance can take a hit. We also find that finetuning sometimes improves performance on low-resource languages, while degrading performance on high-resource languages.

## 08-025 | Adapting Multilingual LLMs to Low-Resource Languages with Knowledge Graphs via Adapters
- arXiv: 2407.01406  first public: 2024-07-01  latest: 2024-12-18  primary cat: cs.CL
- authors (3): Daniil Gurgurov; Mareike Hartmann; Simon Ostermann
- seed subtopic: 语言适配器; type: 原始研究; cross: []
- arXiv comment: 9 pages, KaLLM workshop
- journal_ref: 2024.kallm-1.7
- doi: 10.18653/v1/2024.kallm-1.7
- URLs on first pages of PDF: https://github.com/d-gurgurov/
- pages: 12

ABSTRACT: This paper explores the integration of graph knowledge from linguistic ontologies into multilingual Large Language Models (LLMs) using adapters to improve performance for low-resource languages (LRLs) in sentiment analysis (SA) and named entity recognition (NER). Building upon successful parameter-efficient fine-tuning techniques, such as K-ADAPTER and MAD-X, we propose a similar approach for incorporating knowledge from multilingual graphs, connecting concepts in various languages with each other through linguistic relationships, into multilingual LLMs for LRLs. Specifically, we focus on eight LRLs -- Maltese, Bulgarian, Indonesian, Nepali, Javanese, Uyghur, Tibetan, and Sinhala -- and employ language-specific adapters fine-tuned on data extracted from the language-specific section of ConceptNet, aiming to enable knowledge transfer across the languages covered by the knowledge graph. We compare various fine-tuning objectives, including standard Masked Language Modeling (MLM), MLM with full-word masking, and MLM with targeted masking, to analyse their effectiveness in learning and integrating the extracted graph data. Through empirical evaluation on language-specific tasks, we assess how structured graph knowledge affects the performance of multilingual LLMs for LRLs in SA and NER, providing insights into the potential benefits of adapting language models for low-resource scenarios.

## 08-026 | Small Models, Big Impact: Efficient Corpus and Graph-Based Adaptation of Small Multilingual Language Models for Low-Resource Languages
- arXiv: 2502.10140  first public: 2025-02-14  latest: 2025-02-14  primary cat: cs.CL
- authors (4): Daniil Gurgurov; Ivan Vykopal; Josef van Genabith; Simon Ostermann
- seed subtopic: 适配器（小模型）; type: 原始研究; cross: []
- arXiv comment: Pre-print
- pages: 41

ABSTRACT: Low-resource languages (LRLs) face significant challenges in natural language processing (NLP) due to limited data. While current state-of-the-art large language models (LLMs) still struggle with LRLs, smaller multilingual models (mLMs) such as mBERT and XLM-R offer greater promise due to a better fit of their capacity to low training data sizes. This study systematically investigates parameter-efficient adapter-based methods for adapting mLMs to LRLs, evaluating three architectures: Sequential Bottleneck, Invertible Bottleneck, and Low-Rank Adaptation. Using unstructured text from GlotCC and structured knowledge from ConceptNet, we show that small adaptation datasets (e.g., up to 1 GB of free-text or a few MB of knowledge graph data) yield gains in intrinsic (masked language modeling) and extrinsic tasks (topic classification, sentiment analysis, and named entity recognition). We find that Sequential Bottleneck adapters excel in language modeling, while Invertible Bottleneck adapters slightly outperform other methods on downstream tasks due to better embedding alignment and larger parameter counts. Adapter-based methods match or outperform full fine-tuning while using far fewer parameters, and smaller mLMs prove more effective for LRLs than massive LLMs like LLaMA-3, GPT-4, and DeepSeek-R1-based distilled models. While adaptation improves performance, pre-training data size remains the dominant factor, especially for languages with extensive pre-training coverage.

## 08-027 | Franken-Adapter: Cross-Lingual Adaptation of LLMs by Embedding Surgery
- arXiv: 2502.08037  first public: 2025-02-12  latest: 2025-02-12  primary cat: cs.CL
- authors (4): Fan Jiang; Honglin Yu; Grace Chung; Trevor Cohn
- seed subtopic: 模块化跨语言适配; type: 原始研究; cross: ['06']
- arXiv comment: 33 pages
- pages: 33

ABSTRACT: The capabilities of Large Language Models (LLMs) in low-resource languages lag far behind those in English, making their universal accessibility a significant challenge. To alleviate this, we present $\textit{Franken-Adapter}$, a modular language adaptation approach for decoder-only LLMs with embedding surgery. Our method begins by creating customized vocabularies for target languages and performing language adaptation through embedding tuning on multilingual data. These pre-trained embeddings are subsequently integrated with LLMs that have been instruction-tuned on English alignment data to enable zero-shot cross-lingual transfer. Our experiments on $\texttt{Gemma2}$ models with up to 27B parameters demonstrate improvements of up to 20% across 96 languages, spanning both discriminative and generative tasks, with minimal regressions ($<$1%) in English. Further in-depth analysis reveals the critical role of customizing tokenizers in enhancing language adaptation, while boosting inference efficiency. Additionally, we show the versatility of our method by achieving a 14% improvement over a math-optimized LLM across 20 languages, offering a modular solution to transfer reasoning abilities across languages post hoc.

## 08-028 | Exploring Continual Fine-Tuning for Enhancing Language Ability in Large Language Model
- arXiv: 2410.16006  first public: 2024-10-21  latest: 2026-04-22  primary cat: cs.CL
- authors (5): Divyanshu Aggarwal; Sankarshan Damle; Navin Goyal; Satya Lokam; Sunayana Sitaram
- seed subtopic: 持续微调与语言能力; type: 原始研究; cross: []
- arXiv comment: 19 pages, 6 tables, 4 figures, Accepted to ACL 2026 Findings
- pages: 23

ABSTRACT: A common challenge towards the adaptability of Large Language Models (LLMs) is their ability to learn new languages over time without hampering the model's performance on languages in which the model is already proficient (usually English). Continual fine-tuning (CFT) is the process of sequentially fine-tuning an LLM to enable the model to adapt to downstream tasks with varying data distributions and time shifts. This paper focuses on the language adaptability of LLMs through CFT. We study a two-phase CFT process in which an English-only end-to-end fine-tuned LLM from Phase 1 (predominantly Task Ability) is sequentially fine-tuned on a multilingual dataset -- comprising task data in new languages -- in Phase 2 (predominantly Language Ability). We observe that the ``similarity'' of Phase 2 tasks with Phase 1 determines the LLM's adaptability. For similar phase-wise datasets, the LLM after Phase 2 does not show deterioration in task ability. In contrast, when the phase-wise datasets are not similar, the LLM's task ability deteriorates. We test our hypothesis on the open-source \mis\ and \llm\ models with multiple phase-wise dataset pairs. To address the deterioration, we analyze tailored variants of two CFT methods: layer freezing and generative replay. Our findings demonstrate their effectiveness in enhancing the language ability of LLMs while preserving task performance, in comparison to relevant baselines.

## 08-029 | It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs
- arXiv: 2508.19089  first public: 2025-08-26  latest: 2025-08-26  primary cat: cs.CL
- authors (3): Yue Li; Zhixue Zhao; Carolina Scarton
- seed subtopic: 上下文学习教新语言; type: 原始研究; cross: []
- arXiv comment: Accepted by EMNLP 2025
- URLs on first pages of PDF: https://huggingface.co/facebook/nllb-200-3
- pages: 15

ABSTRACT: Extremely low-resource languages, especially those written in rare scripts, as shown in Figure 1, remain largely unsupported by large language models (LLMs). This is due in part to compounding factors such as the lack of training data. This paper delivers the first comprehensive analysis of whether LLMs can acquire such languages purely via in-context learning (ICL), with or without auxiliary alignment signals, and how these methods compare to parameter-efficient fine-tuning (PEFT). We systematically evaluate 20 under-represented languages across three state-of-the-art multilingual LLMs. Our findings highlight the limitation of PEFT when both language and its script are extremely under-represented by the LLM. In contrast, zero-shot ICL with language alignment is impressively effective on extremely low-resource languages, while few-shot ICL or PEFT is more beneficial for languages relatively better represented by LLMs. For LLM practitioners working on extremely low-resource languages, we summarise guidelines grounded by our results on adapting LLMs to low-resource languages, e.g., avoiding fine-tuning a multilingual model on languages of unseen scripts.

## 08-030 | Prompt, Translate, Fine-Tune, Re-Initialize, or Instruction-Tune? Adapting LLMs for In-Context Learning in Low-Resource Languages
- arXiv: 2506.19187  first public: 2025-06-23  latest: 2025-06-23  primary cat: cs.CL
- authors (2): Christopher Toukmaji; Jeffrey Flanigan
- seed subtopic: 少样本适配策略比较; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL GEM 2025
- URLs on first pages of PDF: https://huggingface.co/collections/ChrisToukmaji/toukmaji-
- pages: 36

ABSTRACT: LLMs are typically trained in high-resource languages, and tasks in lower-resourced languages tend to underperform the higher-resource language counterparts for in-context learning. Despite the large body of work on prompting settings, it is still unclear how LLMs should be adapted cross-lingually specifically for in-context learning in the low-resource target languages. We perform a comprehensive study spanning five diverse target languages, three base LLMs, and seven downstream tasks spanning over 4,100 GPU training hours (9,900+ TFLOPs) across various adaptation techniques: few-shot prompting, translate-test, fine-tuning, embedding re-initialization, and instruction fine-tuning. Our results show that the few-shot prompting and translate-test settings tend to heavily outperform the gradient-based adaptation methods. To better understand this discrepancy, we design a novel metric, Valid Output Recall (VOR), and analyze model outputs to empirically attribute the degradation of these trained models to catastrophic forgetting. To the extent of our knowledge, this is the largest study done on in-context learning for low-resource languages with respect to train compute and number of adaptation techniques considered. We make all our datasets and trained models available for public use.

## 08-032 | Exploring the Role of Transliteration in In-Context Learning for Low-resource Languages Written in Non-Latin Scripts
- arXiv: 2407.02320  first public: 2024-07-02  latest: 2024-07-02  primary cat: cs.CL
- authors (4): Chunlan Ma; Yihong Liu; Haotian Ye; Hinrich Schütze
- seed subtopic: 转写与上下文学习; type: 原始研究; cross: ['02']
- pages: 13

ABSTRACT: Decoder-only large language models (LLMs) excel in high-resource languages across various tasks through few-shot or even zero-shot in-context learning (ICL). However, their performance often does not transfer well to low-resource languages, especially those written in non-Latin scripts. Inspired by recent work that leverages transliteration in encoder-only models, we investigate whether transliteration is also effective in improving LLMs' performance for low-resource languages written in non-Latin scripts. To this end, we propose three prompt templates, where the target-language text is represented in (1) its original script, (2) Latin script, or (3) both. We apply these methods to several representative LLMs of different sizes on various tasks including text classification and sequential labeling. Our findings show that the effectiveness of transliteration varies by task type and model size. For instance, all models benefit from transliterations for sequential labeling (with increases of up to 25%).

## 08-034 | Analyzing and Adapting Large Language Models for Few-Shot Multilingual NLU: Are We There Yet?
- arXiv: 2403.01929  first public: 2024-03-04  latest: 2024-03-04  primary cat: cs.CL
- authors (3): Evgeniia Razumovskaia; Ivan Vulić; Anna Korhonen
- seed subtopic: 少样本多语 NLU; type: 原始研究; cross: []
- pages: 21

ABSTRACT: Supervised fine-tuning (SFT), supervised instruction tuning (SIT) and in-context learning (ICL) are three alternative, de facto standard approaches to few-shot learning. ICL has gained popularity recently with the advent of LLMs due to its simplicity and sample efficiency. Prior research has conducted only limited investigation into how these approaches work for multilingual few-shot learning, and the focus so far has been mostly on their performance. In this work, we present an extensive and systematic comparison of the three approaches, testing them on 6 high- and low-resource languages, three different NLU tasks, and a myriad of language and domain setups. Importantly, performance is only one aspect of the comparison, where we also analyse the approaches through the optics of their computational, inference and financial costs. Our observations show that supervised instruction tuning has the best trade-off between performance and resource requirements. As another contribution, we analyse the impact of target language adaptation of pretrained LLMs and find that the standard adaptation approaches can (superficially) improve target language generation capabilities, but language understanding elicited through ICL does not improve and remains limited, with low scores especially for low-resource languages.

## 08-035 | PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning
- arXiv: 2311.08711  first public: 2023-11-15  latest: 2024-02-12  primary cat: cs.CL
- authors (7): Zhihan Zhang; Dong-Ho Lee; Yuwei Fang; Wenhao Yu; Mengzhao Jia; Meng Jiang ...
- seed subtopic: 枢轴语言指令微调; type: 原始研究; cross: []
- pages: 22

ABSTRACT: Instruction tuning has remarkably advanced large language models (LLMs) in understanding and responding to diverse human instructions. Despite the success in high-resource languages, its application in lower-resource ones faces challenges due to the imbalanced foundational abilities of LLMs across different languages, stemming from the uneven language distribution in their pre-training data. To tackle this issue, we propose pivot language guided generation (PLUG), an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages. It trains the model to first process instructions in the pivot language, and then produce responses in the target language. To evaluate our approach, we introduce a benchmark, X-AlpacaEval, of instructions in 4 languages (Chinese, Korean, Italian, and Spanish), each annotated by professional translators. Our approach demonstrates a significant improvement in the instruction-following abilities of LLMs by 29% on average, compared to directly responding in the target language alone. Further experiments validate the versatility of our approach by employing alternative pivot languages beyond English to assist languages where LLMs exhibit lower proficiency. Our code and data are available at https://github.com/ytyz1307zzh/PLUG.

## 08-036 | Getting More from Less: Large Language Models are Good Spontaneous Multilingual Learners
- arXiv: 2405.13816  first public: 2024-05-22  latest: 2024-06-18  primary cat: cs.CL
- authors (9): Shimao Zhang; Changjiang Gao; Wenhao Zhu; Jiajun Chen; Xin Huang; Xue Han ...
- seed subtopic: 问题翻译数据微调; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Recently, Large Language Models (LLMs) have shown impressive language capabilities. While most of the existing LLMs have very unbalanced performance across different languages, multilingual alignment based on translation parallel data is an effective method to enhance the LLMs' multilingual capabilities. In this work, we discover and comprehensively investigate the spontaneous multilingual alignment improvement of LLMs. We find that LLMs instruction-tuned on the question translation data (i.e. without annotated answers) are able to encourage the alignment between English and a wide range of languages, even including those unseen during instruction-tuning. Additionally, we utilize different settings and mechanistic interpretability methods to analyze the LLM's performance in the multilingual scenario comprehensively. Our work suggests that LLMs have enormous potential for improving multilingual alignment efficiently with great language and task generalization.

## 08-037 | Which LoRA? An Empirical Study on the Effectiveness of LoRA Techniques During Multilingual Instruction Tuning
- arXiv: 2606.10428  first public: 2026-06-09  latest: 2026-06-09  primary cat: cs.CL
- authors (3): Thamali Wijewardhana; Napoleon H. Reyes; Surangika Ranathunga
- seed subtopic: LoRA 变体比较; type: 原始研究; cross: []
- pages: 10

ABSTRACT: We investigate whether commonly available LoRA variants have an advantage over basic LoRA in multilingual instruction tuning. Experiments involving LoRA and four other variants on two datasets across diverse target languages show that there is no significant advantage in using more complex LoRA variants instead of basic LoRA, with respect to balancing cross-lingual transfer and knowledge retention. An analysis of hidden embeddings reveal that layer-wise language representation remains largely similar across LLMs fine-tuned with different LoRA techniques, suggesting that architectural novelty of LoRA techniques may not translate into better cross-lingual adaptation.

## 08-038 | Beyond Bilingual Transfer: Multilingual Code-Switching in Instruction Tuning
- arXiv: 2605.29414  first public: 2026-05-28  latest: 2026-05-28  primary cat: cs.CL
- authors (3): Shunta Asano; Jeonghun Baek; Toshihiko Yamasaki
- seed subtopic: 语码转换指令微调; type: 原始研究; cross: []
- pages: 10

ABSTRACT: Recent studies have shown that code-switching data (CSD), in which multiple languages are mixed within the same context, can improve cross-lingual transfer and multilingual alignment in large language models (LLMs). However, existing studies primarily focus on bilingual transfer between English and a target language, leaving multilingual settings involving three or more languages largely unexplored. In this work, we investigate multilingual code-switching instruction tuning across four languages: English, Japanese, Korean, and Chinese. We evaluate multilingual understanding on Belebele. Our experiments show that simple sentence-level multilingual CSD consistently improves average multilingual performance across all four languages, indicating that multilingual code-switching can be effective beyond bilingual transfer settings.

## 08-039 | Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights
- arXiv: 2603.28263  first public: 2026-03-30  latest: 2026-03-30  primary cat: cs.CL
- authors (5): Eneko Valero; Maria Ribalta i Albado; Oscar Sainz; Naiara Perez; German Rigau
- seed subtopic: 合并式指令化; type: 原始研究; cross: ['07']
- arXiv comment: This paper was accepted at the 15th edition of the Language Resources and Evaluation Conference (LREC 2026)
- pages: 16

ABSTRACT: Large Language Models (LLMs) remain heavily centered on English, with limited performance in low-resource languages. Existing adaptation approaches, such as continual pre-training, demand significant computational resources. In the case of instructed models, high-quality instruction data is also required, both of which are often inaccessible for low-resource language communities. Under these constraints, model merging offers a lightweight alternative, but its potential in low-resource contexts has not been systematically explored. In this work, we explore whether it is possible to transfer language knowledge to an instruction-tuned LLM by merging it with a language-specific base model, thereby eliminating the need of language-specific instructions and repeated fine-tuning processes whenever stronger instructed variants become available. Through experiments covering four Iberian languages (Basque, Catalan, Galician, and Spanish) and two model families, we show that merging enables effective instruction following behavior in new languages and even supports multilingual capability through the combination of multiple language-specific models. Our results indicate that model merging is a viable and efficient alternative to traditional adaptation methods for low-resource languages, achieving competitive performance while greatly reducing computational cost.

## 08-040 | Scaling Sparse Fine-Tuning to Large Language Models
- arXiv: 2401.16405  first public: 2024-01-29  latest: 2024-02-02  primary cat: cs.CL
- authors (5): Alan Ansell; Ivan Vulić; Hannah Sterz; Anna Korhonen; Edoardo M. Ponti
- seed subtopic: 稀疏微调; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Large Language Models (LLMs) are difficult to fully fine-tune (e.g., with instructions or human feedback) due to their sheer number of parameters. A family of parameter-efficient sparse fine-tuning methods have proven promising in terms of performance but their memory requirements increase proportionally to the size of the LLMs. In this work, we scale sparse fine-tuning to state-of-the-art LLMs like LLaMA 2 7B and 13B. We propose SpIEL, a novel sparse fine-tuning method which, for a desired density level, maintains an array of parameter indices and the deltas of these parameters relative to their pretrained values. It iterates over: (a) updating the active deltas, (b) pruning indices (based on the change of magnitude of their deltas) and (c) regrowth of indices. For regrowth, we explore two criteria based on either the accumulated gradients of a few candidate parameters or their approximate momenta estimated using the efficient SM3 optimizer. We experiment with instruction-tuning of LLMs on standard dataset mixtures, finding that SpIEL is often superior to popular parameter-efficient fine-tuning methods like LoRA (low-rank adaptation) in terms of performance and comparable in terms of run time. We additionally show that SpIEL is compatible with both quantization and efficient optimizers, to facilitate scaling to ever-larger model sizes. We release the code for SpIEL at https://github.com/AlanAnsell/peft and for the instruction-tuning experiments at https://github.com/ducdauge/sft-llm.

## 08-041 | LoRA+: Efficient Low Rank Adaptation of Large Models
- arXiv: 2402.12354  first public: 2024-02-19  latest: 2024-07-04  primary cat: cs.LG
- authors (3): Soufiane Hayou; Nikhil Ghosh; Bin Yu
- seed subtopic: LoRA 变体; type: 原始研究; cross: []
- arXiv comment: 27 pages
- pages: 24

ABSTRACT: In this paper, we show that Low Rank Adaptation (LoRA) as originally introduced in Hu et al. (2021) leads to suboptimal finetuning of models with large width (embedding dimension). This is due to the fact that adapter matrices A and B in LoRA are updated with the same learning rate. Using scaling arguments for large width networks, we demonstrate that using the same learning rate for A and B does not allow efficient feature learning. We then show that this suboptimality of LoRA can be corrected simply by setting different learning rates for the LoRA adapter matrices A and B with a well-chosen ratio. We call this proposed algorithm LoRA$+$. In our extensive experiments, LoRA$+$ improves performance (1-2 $\%$ improvements) and finetuning speed (up to $\sim$ 2X SpeedUp), at the same computational cost as LoRA.

## 08-042 | PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models
- arXiv: 2404.02948  first public: 2024-04-03  latest: 2025-04-09  primary cat: cs.LG
- authors (3): Fanxu Meng; Zhaohui Wang; Muhan Zhang
- seed subtopic: LoRA 变体; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024 spotlight
- URLs on first pages of PDF: https://github.com/GraphPKU/PiSSA
- pages: 34

ABSTRACT: To parameter-efficiently fine-tune (PEFT) large language models (LLMs), the low-rank adaptation (LoRA) method approximates the model changes $ΔW \in \mathbb{R}^{m \times n}$ through the product of two matrices $A \in \mathbb{R}^{m \times r}$ and $B \in \mathbb{R}^{r \times n}$, where $r \ll \min(m, n)$, $A$ is initialized with Gaussian noise, and $B$ with zeros. LoRA freezes the original model $W$ and updates the "Noise & Zero" adapter, which may lead to slow convergence. To overcome this limitation, we introduce Principal Singular values and Singular vectors Adaptation (PiSSA). PiSSA shares the same architecture as LoRA, but initializes the adaptor matrices $A$ and $B$ with the principal components of the original matrix $W$, and put the remaining components into a residual matrix $W^{res} \in \mathbb{R}^{m \times n}$ which is frozen during fine-tuning. Compared to LoRA, PiSSA updates the principal components while freezing the "residual" parts, allowing faster convergence and enhanced performance. Comparative experiments of PiSSA and LoRA across 12 different models, ranging from 184M to 70B, encompassing 5 NLG and 8 NLU tasks, reveal that PiSSA consistently outperforms LoRA under identical experimental setups. On the GSM8K benchmark, Mistral-7B fine-tuned with PiSSA achieves an accuracy of 72.86%, surpassing LoRA's 67.7% by 5.16%. Due to the same architecture, PiSSA is also compatible with quantization to further reduce the memory requirement of fine-tuning. Compared to QLoRA, QPiSSA exhibits smaller quantization errors in the initial stages. Fine-tuning LLaMA-3-70B on GSM8K, QPiSSA attains an accuracy of 86.05%, exceeding the performances of QLoRA at 81.73%. Leveraging a fast SVD technique, PiSSA can be initialized in only a few seconds, presenting a negligible cost for transitioning from LoRA to PiSSA. Code is available at https://github.com/GraphPKU/PiSSA.

## 08-043 | A Rank Stabilization Scaling Factor for Fine-Tuning with LoRA
- arXiv: 2312.03732  first public: 2023-11-28  latest: 2023-11-28  primary cat: cs.CL
- authors (1): Damjan Kalajdzievski
- seed subtopic: LoRA 缩放; type: 原始研究; cross: []
- pages: 12

ABSTRACT: As large language models (LLMs) have become increasingly compute and memory intensive, parameter-efficient fine-tuning (PEFT) methods are now a common strategy to fine-tune LLMs. A popular PEFT method is Low-Rank Adapters (LoRA), which adds trainable low-rank "adapters" to selected layers. Each adapter consists of a low-rank matrix product, multiplicatively scaled by a rank-dependent factor. This scaling factor, which divides adapters by a factor of the rank, results in slowed learning and stunted performance for LoRA with higher-rank adapters. Consequently, the use of LoRA in practice has generally been limited to very low ranks. In this work, we study the impact of the scaling factor on the learning process and prove that LoRA adapters should be divided by a factor of the square root of the rank. Modifying LoRA with the appropriate scaling factor, which we call the rank-stabilized LoRA (rsLoRA) method, easily provides for a fine-tuning compute/performance trade-off, where larger ranks can be used to trade off increased computational resources during training for better fine-tuning performance, with no change in inference computing cost.

## 08-044 | Low-Rank Adaptation for Multilingual Summarization: An Empirical Study
- arXiv: 2311.08572  first public: 2023-11-14  latest: 2024-03-31  primary cat: cs.CL
- authors (6): Chenxi Whitehouse; Fantine Huot; Jasmijn Bastings; Mostafa Dehghani; Chu-Cheng Lin; Mirella Lapata
- seed subtopic: LoRA 多语摘要; type: 原始研究; cross: []
- arXiv comment: Findings of NAACL 2024
- pages: 27

ABSTRACT: Although the advancements of pre-trained Large Language Models have significantly accelerated recent progress in NLP, their ever-increasing size poses significant challenges for conventional fine-tuning, especially in memory-intensive tasks. We investigate the potential of Parameter-Efficient Fine-Tuning, focusing on Low-Rank Adaptation (LoRA), in the domain of multilingual summarization, a task that is both challenging (due to typically long inputs), and relatively unexplored. We conduct an extensive study across different data availability scenarios, including high- and low-data settings, and cross-lingual transfer, leveraging models of different sizes. Our findings reveal that LoRA is competitive with full fine-tuning when trained with high quantities of data, and excels in low-data scenarios and cross-lingual transfer. We also study different strategies for few-shot cross-lingual transfer, finding that continued LoRA tuning outperforms full fine-tuning and the dynamic composition of language-specific LoRA modules.

## 08-045 | LLaMAntino: LLaMA 2 Models for Effective Text Generation in Italian Language
- arXiv: 2312.09993  first public: 2023-12-15  latest: 2023-12-15  primary cat: cs.CL
- authors (6): Pierpaolo Basile; Elio Musacchio; Marco Polignano; Lucia Siciliani; Giuseppe Fiameni; Giovanni Semeraro
- seed subtopic: 意大利语 QLoRA 适配; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Large Language Models represent state-of-the-art linguistic models designed to equip computers with the ability to comprehend natural language. With its exceptional capacity to capture complex contextual relationships, the LLaMA (Large Language Model Meta AI) family represents a novel advancement in the field of natural language processing by releasing foundational models designed to improve the natural language understanding abilities of the transformer architecture thanks to their large amount of trainable parameters (7, 13, and 70 billion parameters). In many natural language understanding tasks, these models obtain the same performances as private company models such as OpenAI Chat-GPT with the advantage to make publicly available weights and code for research and commercial uses. In this work, we investigate the possibility of Language Adaptation for LLaMA models, explicitly focusing on addressing the challenge of Italian Language coverage. Adopting an open science approach, we explore various tuning approaches to ensure a high-quality text generated in Italian suitable for common tasks in this underrepresented language in the original models' datasets. We aim to release effective text generation models with strong linguistic properties for many tasks that seem challenging using multilingual or general-purpose LLMs. By leveraging an open science philosophy, this study contributes to Language Adaptation strategies for the Italian language by introducing the novel LLaMAntino family of Italian LLMs.

## 08-047 | Advancing Generative AI for Portuguese with Open Decoder Gervásio PT*
- arXiv: 2402.18766  first public: 2024-02-29  latest: 2024-03-05  primary cat: cs.CL
- authors (5): Rodrigo Santos; João Silva; Luís Gomes; João Rodrigues; António Branco
- seed subtopic: 葡萄牙语指令微调; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/PORTULAN https://huggingface.co/spaces/
- pages: 11

ABSTRACT: To advance the neural decoding of Portuguese, in this paper we present a fully open Transformer-based, instruction-tuned decoder model that sets a new state of the art in this respect. To develop this decoder, which we named Gervásio PT*, a strong LLaMA~2 7B model was used as a starting point, and its further improvement through additional training was done over language resources that include new instruction data sets of Portuguese prepared for this purpose, which are also contributed in this paper. All versions of Gervásio are open source and distributed for free under an open license, including for either research or commercial usage, and can be run on consumer-grade hardware, thus seeking to contribute to the advancement of research and innovation in language technology for Portuguese.

## 08-048 | BanglaLlama: LLaMA for Bangla Language
- arXiv: 2410.21200  first public: 2024-10-28  latest: 2025-10-06  primary cat: cs.CL
- authors (5): Abdullah Khan Zehady; Shubhashis Roy Dipta; Naymul Islam; Safi Al Mamun; Santu Karmaker
- seed subtopic: 孟加拉语指令微调; type: 原始研究; cross: []
- pages: 17

ABSTRACT: Bangla is a language spoken by approximately 240 million native speakers and around 300 million people worldwide. Despite being the 5th largest spoken language in the world, Bangla is still a "low-resource" language, and existing pretrained language models often struggle to perform well on Bangla Language Processing (BLP) tasks. This paper addresses this gap by: (1) introducing two high-quality translated Bangla-instruction datasets totaling 224k samples - Bangla-Orca (172k) and Bangla-Alpaca (52k); and (2) leveraging these datasets to develop BanglaLlama, an open-source family of Bangla-specific LLMs, consisting of five base and instruct variants. We present our methodology, two large datasets, and comprehensive benchmarking results showcasing the effectiveness of our dataset and model on multiple benchmarks. We believe our proposed datasets and models will serve as the new standard baseline for future research focused on this widely spoken yet "low-resource" language.

## 08-049 | Persian-Phi: Efficient Cross-Lingual Adaptation of Compact LLMs via Curriculum Learning
- arXiv: 2512.07454  first public: 2025-12-08  latest: 2025-12-08  primary cat: cs.CL
- authors (4): Amir Mohammad Akhlaghi; Amirhossein Shabani; Mostafa Abdolmaleki; Saeed Reza Kheradpisheh
- seed subtopic: 小模型课程式适配; type: 原始研究; cross: ['07']
- pages: 14

ABSTRACT: The democratization of AI is currently hindered by the immense computational costs required to train Large Language Models (LLMs) for low-resource languages. This paper presents Persian-Phi, a 3.8B parameter model that challenges the assumption that robust multilingual capabilities require massive model sizes or multilingual baselines. We demonstrate how Microsoft Phi-3 Mini -- originally a monolingual English model -- can be effectively adapted to Persian through a novel, resource-efficient curriculum learning pipeline. Our approach employs a unique "warm-up" stage using bilingual narratives (Tiny Stories) to align embeddings prior to heavy training, followed by continual pretraining and instruction tuning via Parameter-Efficient Fine-Tuning (PEFT). Despite its compact size, Persian-Phi achieves competitive results on Open Persian LLM Leaderboard in HuggingFace. Our findings provide a validated, scalable framework for extending the reach of state-of-the-art LLMs to underrepresented languages with minimal hardware resources. The Persian-Phi model is publicly available at https://huggingface.co/amirakhlaghiqqq/PersianPhi.

## 08-050 | Zero-Shot Cross-Lingual Transfer using Prefix-Based Adaptation
- arXiv: 2510.24619  first public: 2025-10-28  latest: 2025-10-28  primary cat: cs.CL
- authors (5): Snegha A; Sayambhu Sen; Piyush Singh Pasi; Abhishek Singhania; Preethi Jyothi
- seed subtopic: 前缀式适配; type: 原始研究; cross: []
- arXiv comment: 12 Pages
- pages: 12

ABSTRACT: With the release of new large language models (LLMs) like Llama and Mistral, zero-shot cross-lingual transfer has become increasingly feasible due to their multilingual pretraining and strong generalization capabilities. However, adapting these decoder-only LLMs to new tasks across languages remains challenging. While parameter-efficient fine-tuning (PeFT) techniques like Low-Rank Adaptation (LoRA) are widely used, prefix-based techniques such as soft prompt tuning, prefix tuning, and Llama Adapter are less explored, especially for zero-shot transfer in decoder-only models. We present a comprehensive study of three prefix-based methods for zero-shot cross-lingual transfer from English to 35+ high- and low-resource languages. Our analysis further explores transfer across linguistic families and scripts, as well as the impact of scaling model sizes from 1B to 24B. With Llama 3.1 8B, prefix methods outperform LoRA-baselines by up to 6% on the Belebele benchmark. Similar improvements were observed with Mistral v0.3 7B as well. Despite using only 1.23M learning parameters with prefix tuning, we achieve consistent improvements across diverse benchmarks. These findings highlight the potential of prefix-based techniques as an effective and scalable alternative to LoRA, particularly in low-resource multilingual settings.

## 08-051 | A Three-Pronged Approach to Cross-Lingual Adaptation with Multilingual LLMs
- arXiv: 2406.17377  first public: 2024-06-25  latest: 2024-06-25  primary cat: cs.CL
- authors (4): Vaibhav Singh; Amrith Krishna; Karthika NJ; Ganesh Ramakrishnan
- seed subtopic: 跨语言适配策略; type: 原始研究; cross: []
- pages: 13

ABSTRACT: Low-resource languages, by its very definition, tend to be under represented in the pre-training corpora of Large Language Models. In this work, we investigate three low-resource cross-lingual approaches that enable an LLM adapt to tasks in previously unseen languages. Llama-2 is an LLM where Indic languages, among many other language families, contribute to less than $0.005\%$ of the total $2$ trillion token pre-training corpora. In this work, we experiment with the English-dominated Llama-2 for cross-lingual transfer to three Indic languages, Bengali, Hindi, and Tamil as target languages. We study three approaches for cross-lingual transfer, under ICL and fine-tuning. One, we find that adding additional supervisory signals via a dominant language in the LLM, leads to improvements, both under in-context learning and fine-tuning. Two, adapting the target languages to word reordering may be beneficial under ICL, but its impact diminishes with fine tuning. Finally, continued pre-training in one low-resource language can improve model performance for other related low-resource languages.

## 08-052 | LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Reasoning
- arXiv: 2412.12499  first public: 2024-12-17  latest: 2025-02-17  primary cat: cs.CL
- authors (5): Hongbin Zhang; Kehai Chen; Xuefeng Bai; Yang Xiang; Min Zhang
- seed subtopic: 两阶段指令微调; type: 原始研究; cross: ['11']
- pages: 32

ABSTRACT: Large language models (LLMs) have exhibited impressive multilingual reasoning capabilities, driven by extensive multilingual pre-training corpora and instruction fine-tuning data. However, a performance gap exists between high- and low-resource language reasoning tasks due to the language imbalance in the pre-training corpus, which is exacerbated by evaluation bias in existing reasoning benchmarks lacking low-resource language coverage. To alleviate this issue, we propose LinguaLIFT, a two-stage instruction tuning framework for advancing low-resource language reasoning. LinguaLIFT employs a language alignment layer to capture multilingual alignment in a code-switched tuning way without requiring multilingual instruction or parallel data, thereby transferring the cross-lingual reasoning capabilities to low-resource languages through English-only instruction tuning data. To comprehensively evaluate the multilingual reasoning capabilities, we introduce the Multilingual Math World Problem (MMWP) benchmark, which spans 21 low-resource, 17 medium-resource, and 10 high-resource languages. Experimental results show that LinguaLIFT outperforms several competitive baselines across MMWP and four widely used benchmarks.

## 08-053 | Language Fusion for Parameter-Efficient Cross-lingual Transfer
- arXiv: 2501.06892  first public: 2025-01-12  latest: 2025-05-25  primary cat: cs.CL
- authors (4): Philipp Borchert; Ivan Vulić; Marie-Francine Moens; Jochen De Weerdt
- seed subtopic: 参数高效跨语言迁移; type: 原始研究; cross: []
- arXiv comment: ACL 2025
- pages: 21

ABSTRACT: Limited availability of multilingual text corpora for training language models often leads to poor performance on downstream tasks due to undertrained representation spaces for languages other than English. This 'under-representation' has motivated recent cross-lingual transfer methods to leverage the English representation space by e.g. mixing English and 'non-English' tokens at the input level or extending model parameters to accommodate new languages. However, these approaches often come at the cost of increased computational complexity. We propose Fusion forLanguage Representations (FLARE) in adapters, a novel method that enhances representation quality and downstream performance for languages other than English while maintaining parameter efficiency. FLARE integrates source and target language representations within low-rank (LoRA) adapters using lightweight linear transformations, maintaining parameter efficiency while improving transfer performance. A series of experiments across representative cross-lingual natural language understanding tasks, including natural language inference, question-answering and sentiment analysis, demonstrate FLARE's effectiveness. FLARE achieves performance improvements of 4.9% for Llama 3.1 and 2.2% for Gemma~2 compared to standard LoRA fine-tuning on question-answering tasks, as measured by the exact match metric.

## 08-054 | AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging
- arXiv: 2402.18913  first public: 2024-02-29  latest: 2024-02-29  primary cat: cs.CL
- authors (5): Yiran Zhao; Wenxuan Zhang; Huiming Wang; Kenji Kawaguchi; Lidong Bing
- seed subtopic: 适配器合并; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/DAMO-NLP-SG/AdaMergeX
- pages: 15

ABSTRACT: As an effective alternative to the direct fine-tuning on target tasks in specific languages, cross-lingual transfer addresses the challenges of limited training data by decoupling ''task ability'' and ''language ability'' by fine-tuning on the target task in the source language and another selected task in the target language, respectively. However, they fail to fully separate the task ability from the source language or the language ability from the chosen task. In this paper, we acknowledge the mutual reliance between task ability and language ability and direct our attention toward the gap between the target language and the source language on tasks. As the gap removes the impact of tasks, we assume that it remains consistent across tasks. Based on this assumption, we propose a new cross-lingual transfer method called $\texttt{AdaMergeX}$ that utilizes adaptive adapter merging. By introducing a reference task, we can determine that the divergence of adapters fine-tuned on the reference task in both languages follows the same distribution as the divergence of adapters fine-tuned on the target task in both languages. Hence, we can obtain target adapters by combining the other three adapters. Furthermore, we propose a structure-adaptive adapter merging method. Our empirical results demonstrate that our approach yields new and effective cross-lingual transfer, outperforming existing methods across all settings.

## 08-055 | Language and Task Arithmetic with Parameter-Efficient Layers for Zero-Shot Summarization
- arXiv: 2311.09344  first public: 2023-11-15  latest: 2024-10-10  primary cat: cs.CL
- authors (6): Alexandra Chronopoulou; Jonas Pfeiffer; Joshua Maynez; Xinyi Wang; Sebastian Ruder; Priyanka Agrawal
- seed subtopic: 语言/任务算术; type: 原始研究; cross: []
- pages: 13

ABSTRACT: Parameter-efficient fine-tuning (PEFT) using labeled task data can significantly improve the performance of large language models (LLMs) on the downstream task. However, there are 7000 languages in the world and many of these languages lack labeled data for real-world language generation tasks. In this paper, we propose to improve zero-shot cross-lingual transfer by composing language or task specialized parameters. Our method composes language and task PEFT modules via element-wise arithmetic operations to leverage unlabeled data and English labeled data. We extend our approach to cases where labeled data from more languages is available and propose to arithmetically compose PEFT modules trained on languages related to the target. Empirical results on summarization demonstrate that our method is an effective strategy that obtains consistent gains using minimal training of PEFT modules.

## 08-056 | The Impact of Demonstrations on Multilingual In-Context Learning: A Multidimensional Analysis
- arXiv: 2402.12976  first public: 2024-02-20  latest: 2024-06-07  primary cat: cs.CL
- authors (7): Miaoran Zhang; Vagrant Gautam; Mingyang Wang; Jesujoba O. Alabi; Xiaoyu Shen; Dietrich Klakow ...
- seed subtopic: 多语上下文学习示例; type: 原始研究; cross: []
- arXiv comment: ACL 2024 findings
- pages: 30

ABSTRACT: In-context learning is a popular inference strategy where large language models solve a task using only a few labeled demonstrations without needing any parameter updates. Although there have been extensive studies on English in-context learning, multilingual in-context learning remains under-explored, and we lack an in-depth understanding of the role of demonstrations in this context. To address this gap, we conduct a multidimensional analysis of multilingual in-context learning, experimenting with 5 models from different model families, 9 datasets covering classification and generation tasks, and 56 typologically diverse languages. Our results reveal that the effectiveness of demonstrations varies significantly across models, tasks, and languages. We also find that strong instruction-following models including Llama 2-Chat, GPT-3.5, and GPT-4 are largely insensitive to the quality of demonstrations. Instead, a carefully crafted template often eliminates the benefits of demonstrations for some tasks and languages altogether. These findings show that the importance of demonstrations might be overestimated. Our work highlights the need for granular evaluation across multiple axes towards a better understanding of in-context learning.

## 08-057 | LoRA vs Full Fine-tuning: An Illusion of Equivalence
- arXiv: 2410.21228  first public: 2024-10-28  latest: 2025-10-22  primary cat: cs.LG
- authors (4): Reece Shuttleworth; Jacob Andreas; Antonio Torralba; Pratyusha Sharma
- seed subtopic: LoRA 与全参数比较; type: 原始研究; cross: []
- pages: 29

ABSTRACT: Fine-tuning is a crucial paradigm for adapting pre-trained large language models to downstream tasks. Recently, methods like Low-Rank Adaptation (LoRA) have been shown to effectively fine-tune LLMs with an extreme reduction in trainable parameters. But, \emph{are their learned solutions really equivalent?} We study how LoRA and full-finetuning change pre-trained models by analyzing the model's weight matrices through the lens of their spectral properties. We find that LoRA and full fine-tuning yield weight matrices whose singular value decompositions exhibit very different structure: weight matrices trained with LoRA have new, high-ranking singular vectors, which we call \emph{intruder dimensions}, while those trained with full fine-tuning do not. Further, we extend the finding that LoRA forgets less than full fine-tuning and find its forgetting is vastly localized to the intruder dimension -- by causally intervening on the intruder dimensions by changing their associated singular values post-fine-tuning, we show that they cause forgetting. Moreover, scaling them down significantly improves modeling of the pre-training distribution with a minimal drop in downstream task performance. Given this, we should expect accumulating intruder dimensions to be harmful and lead to more forgetting. This will be amplified during continual learning because of sequentially fine-tuning, and we show that LoRA models do accumulate intruder dimensions here tend to perform worse in this setting, emphasizing the practicality of our findings.

## 08-058 | Taiwan LLM: Bridging the Linguistic Divide with a Culturally Aligned Language Model
- arXiv: 2311.17487  first public: 2023-11-29  latest: 2023-11-29  primary cat: cs.CL
- authors (2): Yen-Ting Lin; Yun-Nung Chen
- seed subtopic: 繁体中文持续预训练+指令微调; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/MiuLab/Taiwan-LLM https://github.com/MiuLab/Taiwan-LLaMa
- pages: 10

ABSTRACT: In the realm of language models, the nuanced linguistic and cultural intricacies of Traditional Chinese, as spoken in Taiwan, have been largely overlooked. This paper introduces Taiwan LLM, a pioneering Large Language Model that specifically caters to the Traditional Chinese language, with a focus on the variant used in Taiwan. Leveraging a comprehensive pretraining corpus and instruction-finetuning datasets, we have developed a model that not only understands the complexities of Traditional Chinese but also embodies the cultural context of Taiwan. Taiwan LLM represents the first of its kind, a model that is not only linguistically accurate but also culturally resonant with its user base. Our evaluations demonstrate that Taiwan LLM achieves superior performance in understanding and generating Traditional Chinese text, outperforming existing models that are predominantly trained on Simplified Chinese or English. The open-source release of Taiwan LLM invites collaboration and further innovation, ensuring that the linguistic diversity of Chinese speakers is embraced and well-served. The model, datasets, and further resources are made publicly available to foster ongoing research and development in this field.
