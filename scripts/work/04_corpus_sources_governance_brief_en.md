# Brief for annotation: 04 语料来源、治理与许可

## 04-001 | FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language
- arXiv: 2506.20920  first public: 2025-06-26  latest: 2025-06-26  primary cat: cs.CL
- authors (10): Guilherme Penedo; Hynek Kydlíček; Vinko Sabolčec; Bettina Messmer; Negar Foroutan; Amir Hossein Kargaran ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['05']
- URLs on first pages of PDF: https://github.com/huggingface/fineweb-2
- pages: 59

ABSTRACT: Pre-training state-of-the-art large language models (LLMs) requires vast amounts of clean and diverse text data. While the open development of large high-quality English pre-training datasets has seen substantial recent progress, training performant multilingual LLMs remains a challenge, in large part due to the inherent difficulty of tailoring filtering and deduplication pipelines to a large number of languages. In this work, we introduce a new pre-training dataset curation pipeline based on FineWeb that can be automatically adapted to support any language. We extensively ablate our pipeline design choices on a set of nine diverse languages, guided by a set of meaningful and informative evaluation tasks that were chosen through a novel selection process based on measurable criteria. Ultimately, we show that our pipeline can be used to create non-English corpora that produce more performant models than prior datasets. We additionally introduce a straightforward and principled approach to rebalance datasets that takes into consideration both duplication count and quality, providing an additional performance uplift. Finally, we scale our pipeline to over 1000 languages using almost 100 Common Crawl snapshots to produce FineWeb2, a new 20 terabyte (5 billion document) multilingual dataset which we release along with our pipeline, training, and evaluation codebases.

## 04-002 | An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)
- arXiv: 2503.10267  first public: 2025-03-13  latest: 2025-06-04  primary cat: cs.CL
- authors (35): Laurie Burchell; Ona de Gibert; Nikolay Arefyev; Mikko Aulamo; Marta Bañón; Pinzhen Chen ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['05']
- arXiv comment: ACL'2025 Main Proceedings
- URLs on first pages of PDF: https://github.com/hplt-project/
- pages: 35

ABSTRACT: Training state-of-the-art large language models requires vast amounts of clean and diverse textual data. However, building suitable multilingual datasets remains a challenge. In this work, we present HPLT v2, a collection of high-quality multilingual monolingual and parallel corpora, extending prior work of the HPLT project. The monolingual portion of the data contains 8T tokens covering 193 languages, while the parallel data contains 380M sentence pairs covering 51 languages. We document the entire data pipeline and release the code to reproduce it. We provide extensive analysis of the quality and characteristics of our data. Finally, we evaluate the performance of language models and machine translation systems trained on HPLT v2, demonstrating its value.

## 04-003 | A New Massive Multilingual Dataset for High-Performance Language Technologies
- arXiv: 2403.14009  first public: 2024-03-20  latest: 2024-03-20  primary cat: cs.CL
- authors (13): Ona de Gibert; Graeme Nail; Nikolay Arefyev; Marta Bañón; Jelmer van der Linde; Shaoxiong Ji ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: []
- arXiv comment: LREC-COLING 2024
- URLs on first pages of PDF: https://github.com/CLD2Owners/cld2 https://github.com/bitextor/ https://github.com/bitextor/warc2text https://github.com/hplt-project https://github.com/hplt-project/ https://github.com/mbanon/fastspell
- pages: 13

ABSTRACT: We present the HPLT (High Performance Language Technologies) language resources, a new massive multilingual dataset including both monolingual and bilingual corpora extracted from CommonCrawl and previously unused web crawls from the Internet Archive. We describe our methods for data acquisition, management and processing of large corpora, which rely on open-source software tools and high-performance computing. Our monolingual collection focuses on low- to medium-resourced languages and covers 75 languages and a total of ~5.6 trillion word tokens de-duplicated on the document level. Our English-centric parallel corpus is derived from its monolingual counterpart and covers 18 language pairs and more than 96 million aligned sentence pairs with roughly 1.4 billion English tokens. The HPLT language resources are one of the largest open text corpora ever released, providing a great resource for language modeling and machine translation training. We publicly release the corpora, the software, and the tools used in this work.

## 04-004 | HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models
- arXiv: 2511.01066  first public: 2025-11-02  latest: 2026-04-19  primary cat: cs.CL
- authors (32): Stephan Oepen; Nikolay Arefev; Mikko Aulamo; Marta Bañón; Maja Buljan; Laurie Burchell ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['15']
- URLs on first pages of PDF: https://github.com/hplt-project/ https://github.com/pablop16n/
- pages: 26

ABSTRACT: We present an ongoing initiative to provide open, very large, high-quality, and richly annotated textual datasets for almost 200 languages. At 30 trillion tokens, this is likely the largest generally available multilingual collection of LLM pre-training data. These datasets are derived from web crawls from different sources and accompanied with a complete, open-source pipeline for document selection from web archives, text extraction from HTML, language identification for noisy texts, exact and near-deduplication, annotation with, among others, register labels, text quality estimates, and personally identifiable information; and final selection and filtering. We report on data quality probes through contrastive and analytical statistics, through manual inspection of samples for 24 languages, and through end-to-end evaluation of various language model architectures trained on this data. For multilingual LLM evaluation, we provide a comprehensive collection of benchmarks for nine European languages, with special emphasis on natively created tasks, mechanisms to mitigate prompt sensitivity, and refined normalization and aggregation of scores. Additionally, we train and evaluate a family of 57 monolingual encoder-decoder models, as well as a handful of monolingual GPT-like reference models. Besides the monolingual data and models, we also present a very large collection of parallel texts automatically mined from this data, together with a novel parallel corpus synthesized via machine translation.

## 04-005 | GlotCC: An Open Broad-Coverage CommonCrawl Corpus and Pipeline for Minority Languages
- arXiv: 2410.23825  first public: 2024-10-31  latest: 2025-03-03  primary cat: cs.CL
- authors (3): Amir Hossein Kargaran; François Yvon; Hinrich Schütze
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['05']
- arXiv comment: NeurIPS 2024
- pages: 23

ABSTRACT: The need for large text corpora has increased with the advent of pretrained language models and, in particular, the discovery of scaling laws for these models. Most available corpora have sufficient data only for languages with large dominant communities. However, there is no corpus available that (i) covers a wide range of minority languages; (ii) is generated by an open-source reproducible pipeline; and (iii) is rigorously cleaned from noise, making it trustworthy to use. We present GlotCC, a clean, document-level, 2TB general domain corpus derived from CommonCrawl, covering more than 1000 languages. We make GlotCC and the system used to generate it - including the pipeline, language identification model, and filters - available to the research community. Corpus v. 1.0 https://huggingface.co/datasets/cis-lmu/GlotCC-v1, Pipeline v. 3.0 https://github.com/cisnlp/GlotCC.

## 04-006 | MC$^2$: Towards Transparent and Culturally-Aware NLP for Minority Languages in China
- arXiv: 2311.08348  first public: 2023-11-14  latest: 2024-06-13  primary cat: cs.CL
- authors (6): Chen Zhang; Mingxu Tao; Quzhe Huang; Jiuheng Lin; Zhibin Chen; Yansong Feng
- seed subtopic: 少数民族语言语料构建; type: 基准与数据集; cross: []
- arXiv comment: ACL 2024 https://github.com/luciusssss/mc2_corpus
- URLs on first pages of PDF: https://github.com/luciusssss/mc2_corpus
- pages: 19

ABSTRACT: Current large language models demonstrate deficiencies in understanding low-resource languages, particularly the minority languages in China. This limitation stems from the scarcity of available pre-training data. To address this accessibility challenge, we present MC$^2$, a Multilingual Corpus of Minority Languages in China, which is the largest open-source corpus of its kind so far. MC$^2$ includes four underrepresented languages: Tibetan, Uyghur, Kazakh, and Mongolian. Notably, we focus on the less common writing systems of Kazakh and Mongolian, i.e., Kazakh Arabic script and traditional Mongolian script, respectively, which have been long neglected in previous corpus construction efforts. Recognizing the prevalence of language contamination within existing corpora, we adopt a quality-centric solution for collecting MC$^2$, prioritizing accuracy while enhancing diversity. Furthermore, we underscore the importance of attending to the multiplicity of writing systems, which is closely related to the cultural awareness of the resulting models. The MC$^2$ corpus and related models are made public to the community.

## 04-007 | SEACrowd: A Multilingual Multimodal Data Hub and Benchmark Suite for Southeast Asian Languages
- arXiv: 2406.10118  first public: 2024-06-14  latest: 2025-03-11  primary cat: cs.CL
- authors (61): Holy Lovenia; Rahmad Mahendra; Salsabil Maulana Akbar; Lester James V. Miranda; Jennifer Santoso; Elyanah Aco ...
- seed subtopic: 区域语料汇集与社区参与; type: 基准与数据集; cross: ['15']
- arXiv comment: https://seacrowd.github.io/ Published in EMNLP 2024
- URLs on first pages of PDF: https://commoncrawl.github.io/cc-crawl-statistics/plots/languages https://github.com/SEACrowd/seacrowd-datahub/ https://github.com/SEACrowd/seacrowd-experiments https://seacrowd.github.io/seacrowd-catalogue/
- pages: 49

ABSTRACT: Southeast Asia (SEA) is a region rich in linguistic diversity and cultural variety, with over 1,300 indigenous languages and a population of 671 million people. However, prevailing AI models suffer from a significant lack of representation of texts, images, and audio datasets from SEA, compromising the quality of AI models for SEA languages. Evaluating models for SEA languages is challenging due to the scarcity of high-quality datasets, compounded by the dominance of English training data, raising concerns about potential cultural misrepresentation. To address these challenges, we introduce SEACrowd, a collaborative initiative that consolidates a comprehensive resource hub that fills the resource gap by providing standardized corpora in nearly 1,000 SEA languages across three modalities. Through our SEACrowd benchmarks, we assess the quality of AI models on 36 indigenous languages across 13 tasks, offering valuable insights into the current AI landscape in SEA. Furthermore, we propose strategies to facilitate greater AI advancements, maximizing potential utility and resource equity for the future of AI in SEA.

## 04-008 | IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages
- arXiv: 2403.06350  first public: 2024-03-11  latest: 2024-11-29  primary cat: cs.CL
- authors (12): Mohammed Safi Ur Rahman Khan; Priyam Mehta; Ananth Sankar; Umashankar Kumaravelan; Sumanth Doddapaneni; Suriyaprasaad B ...
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: ['05', '08']
- arXiv comment: ACL-2024 Outstanding Paper
- doi: 10.18653/v1/2024.acl-long.843
- URLs on first pages of PDF: https://github.com/AI4Bharat/IndicLLMSuite
- pages: 59

ABSTRACT: Despite the considerable advancements in English LLMs, the progress in building comparable models for other languages has been hindered due to the scarcity of tailored resources. Our work aims to bridge this divide by introducing an expansive suite of resources specifically designed for the development of Indic LLMs, covering 22 languages, containing a total of 251B tokens and 74.8M instruction-response pairs. Recognizing the importance of both data quality and quantity, our approach combines highly curated manually verified data, unverified yet valuable data, and synthetic data. We build a clean, open-source pipeline for curating pre-training data from diverse sources, including websites, PDFs, and videos, incorporating best practices for crawling, cleaning, flagging, and deduplication. For instruction-fine tuning, we amalgamate existing Indic datasets, translate/transliterate English datasets into Indian languages, and utilize LLaMa2 and Mixtral models to create conversations grounded in articles from Indian Wikipedia and Wikihow. Additionally, we address toxicity alignment by generating toxic prompts for multiple scenarios and then generate non-toxic responses by feeding these toxic prompts to an aligned LLaMa2 model. We hope that the datasets, tools, and resources released as a part of this work will not only propel the research and development of Indic LLMs but also establish an open-source blueprint for extending such efforts to other languages. The data and other artifacts created as part of this work are released with permissive licenses.

## 04-009 | 101 Billion Arabic Words Dataset
- arXiv: 2405.01590  first public: 2024-04-29  latest: 2024-04-29  primary cat: cs.CL
- authors (5): Manel Aloui; Hasna Chouikhi; Ghaith Chaabane; Haithem Kchaou; Chehir Dhaouadi
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: []
- pages: 15

ABSTRACT: In recent years, Large Language Models have revolutionized the field of natural language processing, showcasing an impressive rise predominantly in English-centric domains. These advancements have set a global benchmark, inspiring significant efforts toward developing Arabic LLMs capable of understanding and generating the Arabic language with remarkable accuracy. Despite these advancements, a critical challenge persists: the potential bias in Arabic LLMs, primarily attributed to their reliance on datasets comprising English data that has been translated into Arabic. This reliance not only compromises the authenticity of the generated content but also reflects a broader issue -the scarcity of original quality Arabic linguistic data. This study aims to address the data scarcity in the Arab world and to encourage the development of Arabic Language Models that are true to both the linguistic and nuances of the region. We undertook a large-scale data mining project, extracting a substantial volume of text from the Common Crawl WET files, specifically targeting Arabic content. The extracted data underwent a rigorous cleaning and deduplication process, using innovative techniques to ensure the integrity and uniqueness of the dataset. The result is the 101 Billion Arabic Words Dataset, the largest Arabic dataset available to date, which can significantly contribute to the development of authentic Arabic LLMs. This study not only highlights the potential for creating linguistically and culturally accurate Arabic LLMs but also sets a precedent for future research in enhancing the authenticity of Arabic language models.

## 04-010 | Building a Large Japanese Web Corpus for Large Language Models
- arXiv: 2404.17733  first public: 2024-04-27  latest: 2024-04-27  primary cat: cs.CL
- authors (10): Naoaki Okazaki; Kakeru Hattori; Hirai Shota; Hiroki Iida; Masanari Ohi; Kazuki Fujii ...
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: []
- arXiv comment: 17 pages
- URLs on first pages of PDF: https://commoncrawl.github.io/cc-crawl-statistics/ https://github.com/CLD2Owners/cld2 https://github.com/facebookresearch/cc https://huggingface.co/datasets/cc100 https://huggingface.co/tokyotech-llm https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/
- pages: 17

ABSTRACT: Open Japanese large language models (LLMs) have been trained on the Japanese portions of corpora such as CC-100, mC4, and OSCAR. However, these corpora were not created for the quality of Japanese texts. This study builds a large Japanese web corpus by extracting and refining text from the Common Crawl archive (21 snapshots of approximately 63.4 billion pages crawled between 2020 and 2023). This corpus consists of approximately 312.1 billion characters (approximately 173 million pages), which is the largest of all available training corpora for Japanese LLMs, surpassing CC-100 (approximately 25.8 billion characters), mC4 (approximately 239.7 billion characters) and OSCAR 23.10 (approximately 74 billion characters). To confirm the quality of the corpus, we performed continual pre-training on Llama 2 7B, 13B, 70B, Mistral 7B v0.1, and Mixtral 8x7B Instruct as base LLMs and gained consistent (6.6-8.1 points) improvements on Japanese benchmark datasets. We also demonstrate that the improvement on Llama 2 13B brought from the presented corpus was the largest among those from other existing corpora.

## 04-011 | GPT-NL Public Corpus: A Permissively Licensed, Dutch-First Dataset for LLM Pre-training
- arXiv: 2604.00920  first public: 2026-04-01  latest: 2026-04-01  primary cat: cs.CL
- authors (5): Jesse van Oort; Frank Brinkkemper; Erik de Graaf; Bram Vanroy; Saskia Lensink
- seed subtopic: 许可友好的语料; type: 基准与数据集; cross: []
- arXiv comment: Accepted at LREC 2026
- URLs on first pages of PDF: https://huggingface.co/datasets/
- pages: 13

ABSTRACT: We present the GPT-NL Public Corpus, the biggest permissively licensed corpus of Dutch language resources. The GPT-NL Public Corpus contains 21 Dutch-only collections totalling 36B preprocessed Dutch tokens not present in any other LLM pretraining corpus. Additionally, the corpus includes roughly 207B English, 232B Code, and 48B German/Danish tokens taken from existing sets which we further curated for compliance. This corpus includes curated data from large existing corpora like Common Corpus and Common Crawl, as well as newly created Dutch-specific collections. Most newly created Dutch collections consist of content collected in collaboration with organisations or synthetically augmented content. All data is collected and evaluated with the aim of facilitating the creation of (commercial) language models that are lawful, useful and non-harmful. All data included in the GPT-NL Public Corpus is sourced from datasets with permissive licensing and is curated and redistributed under a CC-BY license. The full dataset is publicly available on the Hugging Face Hub.

## 04-012 | Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training
- arXiv: 2506.01732  first public: 2025-06-02  latest: 2026-10-05  primary cat: cs.CL
- authors (10): Pierre-Carl Langlais; Pavel Chizhov; Catherine Arnett; Carlos Rosas-Hinostroza; Mattia Nee; Eliot Krzystof Jones ...
- seed subtopic: 许可友好的语料; type: 基准与数据集; cross: ['05']
- journal_ref: ICLR 2026 (Oral)
- pages: 34

ABSTRACT: Large Language Models (LLMs) are pre-trained on large amounts of data from different sources and domains. Such datasets often contain trillions of tokens, including large portions of copyrighted or proprietary content, which raises questions about the legal use of such models. This underscores the need for truly open pre-training data that complies with data security regulations. In this paper, we introduce Common Corpus, the largest open dataset for LLM pre-training. The data assembled in Common Corpus are either uncopyrighted or under open licenses, totaling about two trillion tokens. The dataset contains a wide variety of languages, ranging from the high-resource European languages to some low-resource languages rarely represented in pre-training datasets. In addition, it includes a large amount of code data. The diversity of data sources in terms of covered domains and time periods opens up the paths for both research and entrepreneurial needs across diverse areas of knowledge. In this paper, we present the detailed provenance of data assembling and the details of dataset filtering and curation. We train two small language models on Common Corpus and find that they perform comparably to other models of their size, indicating that our dataset is suitable for multilingual pretraining. Common Corpus represents a key contribution to the ecosystem for open science research on Large Language Models.

## 04-013 | The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text
- arXiv: 2506.05209  first public: 2025-06-05  latest: 2025-06-05  primary cat: cs.CL
- authors (27): Nikhil Kandpal; Brian Lester; Colin Raffel; Sebastian Majstorovic; Stella Biderman; Baber Abbasi ...
- seed subtopic: 许可友好的语料; type: 基准与数据集; cross: []
- pages: 55

ABSTRACT: Large language models (LLMs) are typically trained on enormous quantities of unlicensed text, a practice that has led to scrutiny due to possible intellectual property infringement and ethical concerns. Training LLMs on openly licensed text presents a first step towards addressing these issues, but prior data collection efforts have yielded datasets too small or low-quality to produce performant LLMs. To address this gap, we collect, curate, and release the Common Pile v0.1, an eight terabyte collection of openly licensed text designed for LLM pretraining. The Common Pile comprises content from 30 sources that span diverse domains including research papers, code, books, encyclopedias, educational materials, audio transcripts, and more. Crucially, we validate our efforts by training two 7 billion parameter LLMs on text from the Common Pile: Comma v0.1-1T and Comma v0.1-2T, trained on 1 and 2 trillion tokens respectively. Both models attain competitive performance to LLMs trained on unlicensed text with similar computational budgets, such as Llama 1 and 2 7B. In addition to releasing the Common Pile v0.1 itself, we also release the code used in its creation as well as the training mixture and checkpoints for the Comma v0.1 models.

## 04-014 | Institutional Books 1.0: A 242B token dataset from Harvard Library's collections, refined for accuracy and usability
- arXiv: 2506.08300  first public: 2025-06-10  latest: 2025-06-10  primary cat: cs.CL
- authors (11): Matteo Cargnelutti; Catherine Brobston; John Hess; Jack Cushman; Kristi Mukk; Aristana Scourtas ...
- seed subtopic: OCR 文献数字化来源; type: 基准与数据集; cross: ['05']
- pages: 51

ABSTRACT: Large language models (LLMs) use data to learn about the world in order to produce meaningful correlations and predictions. As such, the nature, scale, quality, and diversity of the datasets used to train these models, or to support their work at inference time, have a direct impact on their quality. The rapid development and adoption of LLMs of varying quality has brought into focus the scarcity of publicly available, high-quality training data and revealed an urgent need to ground the stewardship of these datasets in sustainable practices with clear provenance chains. To that end, this technical report introduces Institutional Books 1.0, a large collection of public domain books originally digitized through Harvard Library's participation in the Google Books project, beginning in 2006. Working with Harvard Library, we extracted, analyzed, and processed these volumes into an extensively-documented dataset of historic texts. This analysis covers the entirety of Harvard Library's collection scanned as part of that project, originally spanning 1,075,899 volumes written in over 250 different languages for a total of approximately 250 billion tokens. As part of this initial release, the OCR-extracted text (original and post-processed) as well as the metadata (bibliographic, source, and generated) of the 983,004 volumes, or 242B tokens, identified as being in the public domain have been made available. This report describes this project's goals and methods as well as the results of the analyses we performed, all in service of making this historical collection more accessible and easier for humans and machines alike to filter, read and use.

## 04-015 | Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research
- arXiv: 2402.00159  first public: 2024-01-31  latest: 2024-06-06  primary cat: cs.CL
- authors (36): Luca Soldaini; Rodney Kinney; Akshita Bhagia; Dustin Schwenk; David Atkinson; Russell Authur ...
- seed subtopic: 语料文档化; type: 基准与数据集; cross: []
- arXiv comment: Accepted at ACL 2024; Dataset: https://hf.co/datasets/allenai/dolma; Code: https://github.com/allenai/dolma
- pages: 64

ABSTRACT: Information about pretraining corpora used to train the current best-performing language models is seldom discussed: commercial models rarely detail their data, and even open models are often released without accompanying training data or recipes to reproduce them. As a result, it is challenging to conduct and advance scientific research on language modeling, such as understanding how training data impacts model capabilities and limitations. To facilitate scientific research on language model pretraining, we curate and release Dolma, a three-trillion-token English corpus, built from a diverse mixture of web content, scientific papers, code, public-domain books, social media, and encyclopedic materials. We extensively document Dolma, including its design principles, details about its construction, and a summary of its contents. We present analyses and experimental results on intermediate states of Dolma to share what we have learned about important data curation practices. Finally, we open-source our data curation toolkit to enable reproduction of our work as well as support further research in large-scale data curation.

## 04-016 | What's In My Big Data?
- arXiv: 2310.20707  first public: 2023-10-31  latest: 2024-03-05  primary cat: cs.CL
- authors (13): Yanai Elazar; Akshita Bhagia; Ian Magnusson; Abhilasha Ravichander; Dustin Schwenk; Alane Suhr ...
- seed subtopic: 语料文档化与审计; type: 原始研究; cross: ['05']
- arXiv comment: Published at ICLR 2024 spotlight
- URLs on first pages of PDF: https://github.com/allenai/wimbd
- pages: 56

ABSTRACT: Large text corpora are the backbone of language models. However, we have a limited understanding of the content of these corpora, including general statistics, quality, social factors, and inclusion of evaluation data (contamination). In this work, we propose What's In My Big Data? (WIMBD), a platform and a set of sixteen analyses that allow us to reveal and compare the contents of large text corpora. WIMBD builds on two basic capabilities -- count and search -- at scale, which allows us to analyze more than 35 terabytes on a standard compute node. We apply WIMBD to ten different corpora used to train popular language models, including C4, The Pile, and RedPajama. Our analysis uncovers several surprising and previously undocumented findings about these corpora, including the high prevalence of duplicate, synthetic, and low-quality content, personally identifiable information, toxic language, and benchmark contamination. For instance, we find that about 50% of the documents in RedPajama and LAION-2B-en are duplicates. In addition, several datasets used for benchmarking models trained on such corpora are contaminated with respect to important benchmarks, including the Winograd Schema Challenge and parts of GLUE and SuperGLUE. We open-source WIMBD's code and artifacts to provide a standard set of evaluations for new text-based corpora and to encourage more analyses and transparency around them.

## 04-017 | Consent in Crisis: The Rapid Decline of the AI Data Commons
- arXiv: 2407.14933  first public: 2024-07-20  latest: 2024-07-24  primary cat: cs.CL
- authors (49): Shayne Longpre; Robert Mahari; Ariel Lee; Campbell Lund; Hamidah Oderinwale; William Brannon ...
- seed subtopic: 数据授权与同意; type: 原始研究; cross: []
- arXiv comment: 41 pages (13 main), 5 figures, 9 tables
- pages: 41

ABSTRACT: General-purpose artificial intelligence (AI) systems are built on massive swathes of public web data, assembled into corpora such as C4, RefinedWeb, and Dolma. To our knowledge, we conduct the first, large-scale, longitudinal audit of the consent protocols for the web domains underlying AI training corpora. Our audit of 14,000 web domains provides an expansive view of crawlable web data and how codified data use preferences are changing over time. We observe a proliferation of AI-specific clauses to limit use, acute differences in restrictions on AI developers, as well as general inconsistencies between websites' expressed intentions in their Terms of Service and their robots.txt. We diagnose these as symptoms of ineffective web protocols, not designed to cope with the widespread re-purposing of the internet for AI. Our longitudinal analyses show that in a single year (2023-2024) there has been a rapid crescendo of data restrictions from web sources, rendering ~5%+ of all tokens in C4, or 28%+ of the most actively maintained, critical sources in C4, fully restricted from use. For Terms of Service crawling restrictions, a full 45% of C4 is now restricted. If respected or enforced, these restrictions are rapidly biasing the diversity, freshness, and scaling laws for general-purpose AI systems. We hope to illustrate the emerging crises in data consent, for both developers and creators. The foreclosure of much of the open web will impact not only commercial AI, but also non-commercial AI and academic research.

## 04-018 | Data Authenticity, Consent, & Provenance for AI are all broken: what will it take to fix them?
- arXiv: 2404.12691  first public: 2024-04-19  latest: 2024-08-30  primary cat: cs.AI
- authors (8): Shayne Longpre; Robert Mahari; Naana Obeng-Marnu; William Brannon; Tobin South; Katy Gero ...
- seed subtopic: 数据来源追踪; type: 原始研究; cross: []
- arXiv comment: ICML 2024 camera-ready version (Spotlight paper). 9 pages, 2 tables
- journal_ref: Proceedings of ICML 2024, in PMLR 235:32711-32725. URL: https://proceedings.mlr.press/v235/longpre24b.html
- URLs on first pages of PDF: https://huggingface.co/datasets/librarian-bots/
- pages: 15

ABSTRACT: New capabilities in foundation models are owed in large part to massive, widely-sourced, and under-documented training data collections. Existing practices in data collection have led to challenges in tracing authenticity, verifying consent, preserving privacy, addressing representation and bias, respecting copyright, and overall developing ethical and trustworthy foundation models. In response, regulation is emphasizing the need for training data transparency to understand foundation models' limitations. Based on a large-scale analysis of the foundation model training data landscape and existing solutions, we identify the missing infrastructure to facilitate responsible foundation model development practices. We examine the current shortcomings of common tools for tracing data authenticity, consent, and documentation, and outline how policymakers, developers, and data creators can facilitate responsible foundation model development by adopting universal data provenance standards.

## 04-019 | Bridging the Data Provenance Gap Across Text, Speech and Video
- arXiv: 2412.17847  first public: 2024-12-19  latest: 2025-02-19  primary cat: cs.AI
- authors (43): Shayne Longpre; Nikhil Singh; Manuel Cherep; Kushagra Tiwary; Joanna Materzynska; William Brannon ...
- seed subtopic: 数据来源追踪; type: 原始研究; cross: []
- arXiv comment: ICLR 2025. 10 pages, 5 figures (main paper)
- pages: 70

ABSTRACT: Progress in AI is driven largely by the scale and quality of training data. Despite this, there is a deficit of empirical analysis examining the attributes of well-established datasets beyond text. In this work we conduct the largest and first-of-its-kind longitudinal audit across modalities--popular text, speech, and video datasets--from their detailed sourcing trends and use restrictions to their geographical and linguistic representation. Our manual analysis covers nearly 4000 public datasets between 1990-2024, spanning 608 languages, 798 sources, 659 organizations, and 67 countries. We find that multimodal machine learning applications have overwhelmingly turned to web-crawled, synthetic, and social media platforms, such as YouTube, for their training sets, eclipsing all other sources since 2019. Secondly, tracing the chain of dataset derivations we find that while less than 33% of datasets are restrictively licensed, over 80% of the source content in widely-used text, speech, and video datasets, carry non-commercial restrictions. Finally, counter to the rising number of languages and geographies represented in public AI training datasets, our audit demonstrates measures of relative geographical and multilingual representation have failed to significantly improve their coverage since 2013. We believe the breadth of our audit enables us to empirically examine trends in data sourcing, restrictions, and Western-centricity at an ecosystem-level, and that visibility into these questions are essential to progress in responsible AI. As a contribution to ongoing improvements in dataset transparency and responsible use, we release our entire multimodal audit, allowing practitioners to trace data provenance across text, speech, and video.

## 04-020 | Do Not Trust Licenses You See: Dataset Compliance Requires Massive-Scale AI-Powered Lifecycle Tracing
- arXiv: 2503.02784  first public: 2025-03-04  latest: 2025-03-14  primary cat: cs.CY
- authors (8): Jaekyeom Kim; Sungryull Sohn; Gerrard Jeongwon Jo; Jihoon Choi; Kyunghoon Bae; Hwayoung Lee ...
- seed subtopic: 数据授权与许可; type: 原始研究; cross: []
- pages: 37

ABSTRACT: This paper argues that a dataset's legal risk cannot be accurately assessed by its license terms alone; instead, tracking dataset redistribution and its full lifecycle is essential. However, this process is too complex for legal experts to handle manually at scale. Tracking dataset provenance, verifying redistribution rights, and assessing evolving legal risks across multiple stages require a level of precision and efficiency that exceeds human capabilities. Addressing this challenge effectively demands AI agents that can systematically trace dataset redistribution, analyze compliance, and identify legal risks. We develop an automated data compliance system called NEXUS and show that AI can perform these tasks with higher accuracy, efficiency, and cost-effectiveness than human experts. Our massive legal analysis of 17,429 unique entities and 8,072 license terms using this approach reveals the discrepancies in legal rights between the original datasets before redistribution and their redistributed subsets, underscoring the necessity of the data lifecycle-aware compliance. For instance, we find that out of 2,852 datasets with commercially viable individual license terms, only 605 (21%) are legally permissible for commercialization. This work sets a new standard for AI data governance, advocating for a framework that systematically examines the entire lifecycle of dataset redistribution to ensure transparent, legal, and responsible dataset management.

## 04-021 | An Empirical Analysis of Machine Learning Model and Dataset Documentation, Supply Chain, and Licensing Challenges on Hugging Face
- arXiv: 2502.04484  first public: 2025-02-06  latest: 2025-09-29  primary cat: cs.SE
- authors (7): Trevor Stalnaker; Nathan Wintersgill; Oscar Chaparro; Laura A. Heymann; Massimiliano Di Penta; Daniel M German ...
- seed subtopic: 数据授权与许可; type: 原始研究; cross: []
- pages: 48

ABSTRACT: The last decade has seen widespread adoption of Machine Learning (ML) components in software systems. This has occurred in nearly every domain, from natural language processing to computer vision. These ML components range from relatively simple neural networks to complex and resource-intensive large language models. However, despite this widespread adoption, little is known about the supply chain relationships that produce these models, which can have implications for compliance and security. In this work, we conducted an extensive analysis of 760,460 models and 175,000 datasets extracted from the popular model-sharing site Hugging Face. First, we evaluate the current state of documentation in the Hugging Face supply chain, report real-world examples of shortcomings, and offer actionable suggestions for improvement. Next, we analyze the underlying structure of the existing supply chain. Finally, we explore the current licensing landscape against what was reported in previous work and discuss the unique challenges posed in this domain. Our results motivate multiple research avenues, including the need for better license management for ML models/datasets, better support for model documentation, and automated inconsistency checking and validation. We make our research infrastructure and dataset available to facilitate future research.

## 04-022 | Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs
- arXiv: 2601.14311  first public: 2026-01-19  latest: 2026-01-19  primary cat: cs.CR
- authors (6): Richard Hohensinner; Belgin Mutlu; Inti Gabriel Mendoza Estrada; Matej Vukovic; Simone Kopeinik; Roman Kern
- seed subtopic: 数据来源追踪; type: 综述; cross: []
- arXiv comment: 35 pages, 6 figures. Manuscript submitted to ACM Computing Surveys (CSUR) on the 12th of December 2025
- pages: 35

ABSTRACT: Large language models (LLMs) are deployed at scale, yet their training data life cycle remains opaque. This survey synthesizes research from the past ten years on three tightly coupled axes: (1) data provenance, (2) transparency, and (3) traceability, and three supporting pillars: (4) bias \& uncertainty, (5) data privacy, and (6) tools and techniques that operationalize them. A central contribution is a proposed taxonomy defining the field's domains and listing corresponding artifacts. Through analysis of 95 publications, this work identifies key methodologies concerning data generation, watermarking, bias measurement, data curation, data privacy, and the inherent trade-off between transparency and opacity.

## 04-023 | Compliance Rating Scheme: A Data Provenance Framework for Generative AI Datasets
- arXiv: 2512.21775  first public: 2025-12-25  latest: 2025-12-25  primary cat: cs.AI
- authors (2): Matyas Bohacek; Ignacio Vilanova Echavarri
- seed subtopic: 数据来源追踪; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/
- pages: 14

ABSTRACT: Generative Artificial Intelligence (GAI) has experienced exponential growth in recent years, partly facilitated by the abundance of large-scale open-source datasets. These datasets are often built using unrestricted and opaque data collection practices. While most literature focuses on the development and applications of GAI models, the ethical and legal considerations surrounding the creation of these datasets are often neglected. In addition, as datasets are shared, edited, and further reproduced online, information about their origin, legitimacy, and safety often gets lost. To address this gap, we introduce the Compliance Rating Scheme (CRS), a framework designed to evaluate dataset compliance with critical transparency, accountability, and security principles. We also release an open-source Python library built around data provenance technology to implement this framework, allowing for seamless integration into existing dataset-processing and AI training pipelines. The library is simultaneously reactive and proactive, as in addition to evaluating the CRS of existing datasets, it equally informs responsible scraping and construction of new datasets.

## 04-024 | The Responsible Foundation Model Development Cheatsheet: A Review of Tools & Resources
- arXiv: 2406.16746  first public: 2024-06-24  latest: 2025-02-17  primary cat: cs.LG
- authors (23): Shayne Longpre; Stella Biderman; Alon Albalak; Hailey Schoelkopf; Daniel McDuff; Sayash Kapoor ...
- seed subtopic: 数据治理工具; type: 综述; cross: []
- pages: 41

ABSTRACT: Foundation model development attracts a rapidly expanding body of contributors, scientists, and applications. To help shape responsible development practices, we introduce the Foundation Model Development Cheatsheet: a growing collection of 250+ tools and resources spanning text, vision, and speech modalities. We draw on a large body of prior work to survey resources (e.g. software, documentation, frameworks, guides, and practical tools) that support informed data selection, processing, and understanding, precise and limitation-aware artifact documentation, efficient model training, advance awareness of the environmental impact from training, careful model evaluation of capabilities, risks, and claims, as well as responsible model release, licensing and deployment practices. We hope this curated collection of resources helps guide more responsible development. The process of curating this list, enabled us to review the AI development ecosystem, revealing what tools are critically missing, misused, or over-used in existing practices. We find that (i) tools for data sourcing, model evaluation, and monitoring are critically under-serving ethical and real-world needs, (ii) evaluations for model safety, capabilities, and environmental impact all lack reproducibility and transparency, (iii) text and particularly English-centric analyses continue to dominate over multilingual and multi-modal analyses, and (iv) evaluation of systems, rather than just models, is needed so that capabilities and impact are assessed in context.

## 04-025 | A Survey of Web Content Control for Generative AI
- arXiv: 2404.02309  first public: 2024-04-02  latest: 2024-04-02  primary cat: cs.IR
- authors (3): Michael Dinzinger; Florian Heß; Michael Granitzer
- seed subtopic: 数据授权与同意; type: 综述; cross: []
- pages: 12

ABSTRACT: The groundbreaking advancements around generative AI have recently caused a wave of concern culminating in a row of lawsuits, including high-profile actions against Stability AI and OpenAI. This situation of legal uncertainty has sparked a broad discussion on the rights of content creators and publishers to protect their intellectual property on the web. European as well as US law already provides rough guidelines, setting a direction for technical solutions to regulate web data use. In this course, researchers and practitioners have worked on numerous web standards and opt-out formats that empower publishers to keep their data out of the development of generative AI models. The emerging AI/ML opt-out protocols are valuable in regards to data sovereignty, but again, it creates an adverse situation for a site owners who are overwhelmed by the multitude of recent ad hoc standards to consider. In our work, we want to survey the different proposals, ideas and initiatives, and provide a comprehensive legal and technical background in the context of the current discussion on web publishers control.

## 04-026 | Socially Responsible Data for Large Multilingual Language Models
- arXiv: 2409.05247  first public: 2024-09-08  latest: 2024-09-08  primary cat: cs.CL
- authors (15): Andrew Smart; Ben Hutchinson; Lameck Mbangula Amugongo; Suzanne Dikker; Alex Zito; Amber Ebinama ...
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- journal_ref: ACM conference on Equity and Access in Algorithms, Mechanisms, and Optimization, 2024
- pages: 22

ABSTRACT: Large Language Models (LLMs) have rapidly increased in size and apparent capabilities in the last three years, but their training data is largely English text. There is growing interest in multilingual LLMs, and various efforts are striving for models to accommodate languages of communities outside of the Global North, which include many languages that have been historically underrepresented in digital realms. These languages have been coined as "low resource languages" or "long-tail languages", and LLMs performance on these languages is generally poor. While expanding the use of LLMs to more languages may bring many potential benefits, such as assisting cross-community communication and language preservation, great care must be taken to ensure that data collection on these languages is not extractive and that it does not reproduce exploitative practices of the past. Collecting data from languages spoken by previously colonized people, indigenous people, and non-Western languages raises many complex sociopolitical and ethical questions, e.g., around consent, cultural safety, and data sovereignty. Furthermore, linguistic complexity and cultural nuances are often lost in LLMs. This position paper builds on recent scholarship, and our own work, and outlines several relevant social, cultural, and ethical considerations and potential ways to mitigate them through qualitative research, community partnerships, and participatory design approaches. We provide twelve recommendations for consideration when collecting language data on underrepresented language communities outside of the Global North.

## 04-027 | Māori algorithmic sovereignty: idea, principles, and use
- arXiv: 2311.15473  first public: 2023-11-27  latest: 2023-11-27  primary cat: cs.CY
- authors (10): Paul T. Brown; Daniel Wilson; Kiri West; Kirita-Rose Escott; Kiya Basabas; Ben Ritchie ...
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- pages: 18

ABSTRACT: Due to the emergence of data-driven technologies in Aotearoa New Zealand that use Māori data, there is a need for values-based frameworks to guide thinking around balancing the tension between the opportunities these create, and the inherent risks that these technologies can impose. Algorithms can be framed as a particular use of data, therefore data frameworks that currently exist can be extended to include algorithms. Māori data sovereignty principles are well-known and are used by researchers and government agencies to guide the culturally appropriate use of Māori data. Extending these principles to fit the context of algorithms, and re-working the underlying sub-principles to address issues related to responsible algorithms from a Māori perspective leads to the Māori algorithmic sovereignty principles. We define this idea, present the updated principles and subprinciples, and highlight how these can be used to decolonise algorithms currently in use, and argue that these ideas could potentially be used to developed Indigenised algorithms.

## 04-028 | Data Findability, Governance, and Community Engagement for Māori Research Data Sovereignty
- arXiv: 2608.08905  first public: 2026-08-09  latest: 2026-08-09  primary cat: cs.CY
- authors (5): Paul T. Brown; Kiri West; Maree Sheehan; Hana Rapata; Te Taka Keegan
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- pages: 17

ABSTRACT: Māori data sovereignty (MDSov) has established important principles for recognising Māori rights and interests in data. Relatively little attention has been given to how these principles can be operationalised within research institutions who, as a function of their operations, collect and use Māori data. This paper introduces the concept of Māori Research Data Sovereignty (MRDSov), extending existing understandings of MDSov into the specific context of research data and the research data lifecycle. Drawing on Indigenous Data Sovereignty scholarship and research data management literature, we define Māori research data and position MRDSov as the application of MDSov principles to research data produced by, about, or for Māori. We argue that operationalising MRDSov requires three interdependent elements: data findability, data governance, and community engagement. Data findability enables Māori research data to be identified and contextualised; governance provides mechanisms through which Māori authority over research data can be exercised; and community engagement grounds both in enduring relationships with Māori communities. We further demonstrate how these elements collectively enact the principles of MDSov within institutional research settings, providing a practical pathway for aligning research data practices with Te Tiriti o Waitangi obligations and Indigenous data governance expectations. The paper contributes a conceptual framework for universities and other research organisations seeking to embed Māori authority, accountability, and relationships throughout the research data lifecycle.

## 04-029 | Modeling the Sacred: Considerations when Using Religious Texts in Natural Language Processing
- arXiv: 2404.14740  first public: 2024-04-23  latest: 2025-07-22  primary cat: cs.CL
- authors (1): Ben Hutchinson
- seed subtopic: 语料来源伦理; type: 原始研究; cross: []
- arXiv comment: Findings of NAACL2024
- pages: 15

ABSTRACT: This position paper concerns the use of religious texts in Natural Language Processing (NLP), which is of special interest to the Ethics of NLP. Religious texts are expressions of culturally important values, and machine learned models have a propensity to reproduce cultural values encoded in their training data. Furthermore, translations of religious texts are frequently used by NLP researchers when language data is scarce. This repurposes the translations from their original uses and motivations, which often involve attracting new followers. This paper argues that NLP's use of such texts raises considerations that go beyond model biases, including data provenance, cultural contexts, and their use in proselytism. We argue for more consideration of researcher positionality, and of the perspectives of marginalized linguistic and religious communities.

## 04-030 | Harnessing the Power of Artificial Intelligence to Vitalize Endangered Indigenous Languages: Technologies and Experiences
- arXiv: 2407.12620  first public: 2024-07-17  latest: 2024-07-29  primary cat: cs.CL
- authors (12): Claudio Pinhanez; Paulo Cavalin; Luciana Storto; Thomas Finbow; Alexander Cobbinah; Julio Nogima ...
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- pages: 31

ABSTRACT: Since 2022 we have been exploring application areas and technologies in which Artificial Intelligence (AI) and modern Natural Language Processing (NLP), such as Large Language Models (LLMs), can be employed to foster the usage and facilitate the documentation of Indigenous languages which are in danger of disappearing. We start by discussing the decreasing diversity of languages in the world and how working with Indigenous languages poses unique ethical challenges for AI and NLP. To address those challenges, we propose an alternative development AI cycle based on community engagement and usage. Then, we report encouraging results in the development of high-quality machine learning translators for Indigenous languages by fine-tuning state-of-the-art (SOTA) translators with tiny amounts of data and discuss how to avoid some common pitfalls in the process. We also present prototypes we have built in projects done in 2023 and 2024 with Indigenous communities in Brazil, aimed at facilitating writing, and discuss the development of Indigenous Language Models (ILMs) as a replicable and scalable way to create spell-checkers, next-word predictors, and similar tools. Finally, we discuss how we envision a future for language documentation where dying languages are preserved as interactive language models.

## 04-032 | Kreyòl-MT: Building MT for Latin American, Caribbean and Colonial African Creole Languages
- arXiv: 2405.05376  first public: 2024-05-08  latest: 2024-05-13  primary cat: cs.CL
- authors (17): Nathaniel R. Robinson; Raj Dabre; Ammon Shurtz; Rasul Dent; Onenamiyi Onesi; Claire Bizon Monroc ...
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- arXiv comment: NAACL 2024
- URLs on first pages of PDF: https://github.com/JHU-CLSP/
- pages: 28

ABSTRACT: A majority of language technologies are tailored for a small number of high-resource languages, while relatively many low-resource languages are neglected. One such group, Creole languages, have long been marginalized in academic study, though their speakers could benefit from machine translation (MT). These languages are predominantly used in much of Latin America, Africa and the Caribbean. We present the largest cumulative dataset to date for Creole language MT, including 14.5M unique Creole sentences with parallel translations -- 11.6M of which we release publicly, and the largest bitexts gathered to date for 41 languages -- the first ever for 21. In addition, we provide MT models supporting all 41 Creole languages in 172 translation directions. Given our diverse dataset, we produce a model for Creole language MT exposed to more genre diversity than ever before, which outperforms a genre-specific Creole MT model on its own benchmark for 26 of 34 translation directions.

## 04-033 | Building low-resource African language corpora: A case study of Kidawida, Kalenjin and Dholuo
- arXiv: 2501.11003  first public: 2025-01-19  latest: 2025-01-19  primary cat: cs.CL
- authors (5): Audrey Mbogho; Quin Awuor; Andrew Kipkebut; Lilian Wanzare; Vivian Oloo
- seed subtopic: 低资源语料构建案例; type: 原始研究; cross: []
- arXiv comment: 13 pages, 1 figure, intend to submit to a Springer Nature journal
- pages: 13

ABSTRACT: Natural Language Processing is a crucial frontier in artificial intelligence, with broad applications in many areas, including public health, agriculture, education, and commerce. However, due to the lack of substantial linguistic resources, many African languages remain underrepresented in this digital transformation. This paper presents a case study on the development of linguistic corpora for three under-resourced Kenyan languages, Kidaw'ida, Kalenjin, and Dholuo, with the aim of advancing natural language processing and linguistic research in African communities. Our project, which lasted one year, employed a selective crowd-sourcing methodology to collect text and speech data from native speakers of these languages. Data collection involved (1) recording conversations and translation of the resulting text into Kiswahili, thereby creating parallel corpora, and (2) reading and recording written texts to generate speech corpora. We made these resources freely accessible via open-research platforms, namely Zenodo for the parallel text corpora and Mozilla Common Voice for the speech datasets, thus facilitating ongoing contributions and access for developers to train models and develop Natural Language Processing applications. The project demonstrates how grassroots efforts in corpus building can support the inclusion of African languages in artificial intelligence innovations. In addition to filling resource gaps, these corpora are vital in promoting linguistic diversity and empowering local communities by enabling Natural Language Processing applications tailored to their needs. As African countries like Kenya increasingly embrace digital transformation, developing indigenous language resources becomes essential for inclusive growth. We encourage continued collaboration from native speakers and developers to expand and utilize these corpora.

## 04-034 | Echoes Across Vietnam's Highlands, Delta, and Coast: A Multilingual Corpus for Cham, Khmer, and Tay-Nung
- arXiv: 2607.08362  first public: 2026-07-09  latest: 2026-07-27  primary cat: cs.CL
- authors (5): Anh Trac Duc Dinh; Khang Nhat Hoang Vo; Vinh Cong Doan; Tai Tien Ta; Khoa Duc Anh Lam
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: []
- pages: 18

ABSTRACT: Vietnam's ethnic minority languages are almost absent from the field of Natural Language Processing (NLP), and the challenge goes beyond data scarcity: Cham, Khmer, and Tay-Nung differ sharply in script, Vietnamese contact, and standardization, conditions under which standard multilingual adaptation can learn the wrong signals. We introduce CKTN, the first corpus and benchmark for these languages (44,367 documents, 24M subword tokens), spanning continued pretraining, category classification, and summary-document retrieval. We show that existing multilingual encoders severely fragment these languages, and that common adaptation metrics can mislead: models may lower language-modeling loss or excel at lexical-overlap retrieval while still failing at semantic generalization across documents. We address this with a script-aware adaptation recipe - vocabulary augmentation combined with calibrated replaced-token pretraining - that prevents the discriminator from exploiting trivial script mismatches. The result is an encoder with substantially less fragmentation and the strongest classification performance among evaluated models, exposing the limits of lexical-overlap retrieval as an evaluation signal.

## 04-035 | Developing an English-Efik Corpus and Machine Translation System for Digitization Inclusion
- arXiv: 2603.14873  first public: 2026-03-16  latest: 2026-03-16  primary cat: cs.CL
- authors (5): Offiong Bassey Edet; Mbuotidem Sunday Awak; Emmanuel Oyo-Ita; Benjamin Okon Nyong; Ita Etim Bassey
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- arXiv comment: 8 pages, 1 figure, accepted at AfricaNLP 2026 (co-located with EACL)
- pages: 8

ABSTRACT: Low-resource languages serve as invaluable repositories of human history, preserving cultural and intellectual diversity. Despite their significance, they remain largely absent from modern natural language processing systems. While progress has been made for widely spoken African languages such as Swahili, Yoruba, and Amharic, smaller indigenous languages like Efik continue to be underrepresented in machine translation research. This study evaluates the effectiveness of state-of-the-art multilingual neural machine translation models for English-Efik translation, leveraging a small-scale, community-curated parallel corpus of 13,865 sentence pairs. We fine-tuned both the mT5 multilingual model and the NLLB200 model on this dataset. NLLB-200 outperformed mT5, achieving BLEU scores of 26.64 for English-Efik and 31.21 for Efik-English, with corresponding chrF scores of 51.04 and 47.92, indicating improved fluency and semantic fidelity. Our findings demonstrate the feasibility of developing practical machine translation tools for low-resource languages and highlight the importance of inclusive data practices and culturally grounded evaluation in advancing equitable NLP.

## 04-036 | Design Considerations in Low-Resource Archival OCR: A Case Study in Lakota
- arXiv: 2610.25440  first public: 2026-10-18  latest: 2026-10-18  primary cat: cs.CL
- authors (8): Téa Wright; Laura X. Ma; Claudia Iron Hawk; Hannah J. Haynie; Alexis Palmer; Alane Suhr ...
- seed subtopic: OCR 文献数字化来源; type: 原始研究; cross: ['05']
- pages: 17

ABSTRACT: Building and expanding access to digital archives supports language reclamation and creates lasting resources for community revitalization. Designing effective tools to support these efforts requires taking into account the community-, language-, and document-specific context. We investigate how small ($\leq$3B) vision-language models (VLMs) can be adapted as optical character recognition (OCR) tools for Lakota, a North American Indigenous language. In addition to benchmarking modeling approaches, we inspect four practical facets of low-resource archival OCR that arise in previous work and conversations with community members: constrained training budgets, segmentation noise, scan degradation, and orthographic variance. We demonstrate that fine-tuning VLMs for OCR post-correction on 35 pages of transcribed data decreases character error rate (CER) from 17.1 to 3.9\% on a bilingual corpus, and find that training only with nine pages increases CER by only 1.1\% over this. However, evaluating under realistic automatic segmentation nearly doubles the CER of the best-performing models, stressing the importance of taking realistic use cases into account. We hope this work encourages future research on developing language technologies grounded in the workflows and constraints of ongoing revitalization efforts.

## 04-037 | WildChat: 1M ChatGPT Interaction Logs in the Wild
- arXiv: 2405.01470  first public: 2024-05-02  latest: 2024-05-02  primary cat: cs.CL
- authors (6): Wenting Zhao; Xiang Ren; Jack Hessel; Claire Cardie; Yejin Choi; Yuntian Deng
- seed subtopic: 对话语料与隐私; type: 基准与数据集; cross: ['13']
- arXiv comment: accepted by ICLR 2024
- URLs on first pages of PDF: https://huggingface.co/spaces/yuntian-deng/ChatGPT https://huggingface.co/spaces/yuntian-deng/ChatGPT4 https://microsoft.github.io/presidio/
- pages: 16

ABSTRACT: Chatbots such as GPT-4 and ChatGPT are now serving millions of users. Despite their widespread use, there remains a lack of public datasets showcasing how these tools are used by a population of users in practice. To bridge this gap, we offered free access to ChatGPT for online users in exchange for their affirmative, consensual opt-in to anonymously collect their chat transcripts and request headers. From this, we compiled WildChat, a corpus of 1 million user-ChatGPT conversations, which consists of over 2.5 million interaction turns. We compare WildChat with other popular user-chatbot interaction datasets, and find that our dataset offers the most diverse user prompts, contains the largest number of languages, and presents the richest variety of potentially toxic use-cases for researchers to study. In addition to timestamped chat transcripts, we enrich the dataset with demographic data, including state, country, and hashed IP addresses, alongside request headers. This augmentation allows for more detailed analysis of user behaviors across different geographical regions and temporal dimensions. Finally, because it captures a broad range of use cases, we demonstrate the dataset's potential utility in fine-tuning instruction-following models. WildChat is released at https://wildchat.allen.ai under AI2 ImpACT Licenses.

## 04-038 | The Esethu Framework: Reimagining Sustainable Dataset Governance and Curation for Low-Resource Languages
- arXiv: 2502.15916  first public: 2025-02-21  latest: 2025-06-12  primary cat: cs.CL
- authors (15): Jenalea Rajab; Anuoluwapo Aremu; Everlyn Asiko Chimoto; Dale Dunbar; Graham Morrissey; Fadel Thior ...
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- pages: 14

ABSTRACT: This paper presents the Esethu Framework, a sustainable data curation framework specifically designed to empower local communities and ensure equitable benefit-sharing from their linguistic resource. This framework is supported by the Esethu license, a novel community-centric data license. As a proof of concept, we introduce the Vuk'uzenzele isiXhosa Speech Dataset (ViXSD), an open-source corpus developed under the Esethu Framework and License. The dataset, containing read speech from native isiXhosa speakers enriched with demographic and linguistic metadata, demonstrates how community-driven licensing and curation principles can bridge resource gaps in automatic speech recognition (ASR) for African languages while safeguarding the interests of data creators. We describe the framework guiding dataset development, outline the Esethu license provisions, present the methodology for ViXSD, and present ASR experiments validating ViXSD's usability in building and refining voice-driven applications for isiXhosa.

## 04-039 | Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages
- arXiv: 2606.28867  first public: 2026-06-27  latest: 2026-06-27  primary cat: cs.CL
- authors (1): Ernst van Gassen
- seed subtopic: 数据授权与许可; type: 原始研究; cross: []
- arXiv comment: 12 pages. Published in Proceedings of Resources for African Indigenous Languages (RAIL) 2026 @ LREC-COLING 2026, pages 128-139
- journal_ref: Proceedings of Resources for African Indigenous Languages (RAIL) 2026, pages 128-139. ELRA, 2026
- pages: 11

ABSTRACT: Creative Commons licenses dominate African NLP corpus releases, but their compatibility rules are rarely applied. CC-BY-SA and CC-BY-NC cannot be combined in a single published dataset; a NoDerivs clause silently prohibits tokenisation and annotation. This paper audits the license provenance of over twenty corpus families used in African NLP, constructs a six-tier compatibility matrix, and applies it to three case-study languages: Kituba/Munukutuba, Zarma, and Moore. Four failure modes are documented with primary-source evidence: outright prohibition (JW300, removed from OPUS after a legal audit confirmed Terms of Service violation); composite license misrepresentation (WAXAL, whose CC-BY 4.0 claim is contradicted by its own HuggingFace dataset card); a NoDerivs clause hidden behind a CC-BY label (Tanzil); and data persistence failure (the Congolese Radio Corpus, where 402 of 405 source URLs are now dead). A pre-annotation due diligence checklist and a survey of legally clean enrichment opportunities close the paper.

## 04-040 | "It's how you do things that matters": Attending to Process to Better Serve Indigenous Communities with Language Technologies
- arXiv: 2402.02639  first public: 2024-02-04  latest: 2024-02-06  primary cat: cs.CL
- authors (3): Ned Cooper; Courtney Heldreth; Ben Hutchinson
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- journal_ref: Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2024)
- pages: 8

ABSTRACT: Indigenous languages are historically under-served by Natural Language Processing (NLP) technologies, but this is changing for some languages with the recent scaling of large multilingual models and an increased focus by the NLP community on endangered languages. This position paper explores ethical considerations in building NLP technologies for Indigenous languages, based on the premise that such projects should primarily serve Indigenous communities. We report on interviews with 17 researchers working in or with Aboriginal and/or Torres Strait Islander communities on language technology projects in Australia. Drawing on insights from the interviews, we recommend practices for NLP researchers to increase attention to the process of engagements with Indigenous communities, rather than focusing only on decontextualised artefacts.

## 04-041 | PashtoCorp: A 1.25-Billion-Word Corpus, Evaluation Suite, and Reproducible Pipeline for Low-Resource Language Development
- arXiv: 2603.16354  first public: 2026-03-17  latest: 2026-03-17  primary cat: cs.CL
- authors (1): Hanif Rahman
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://huggingface.co/ihanif/
- pages: 8

ABSTRACT: We present PashtoCorp, a 1.25-billion-word corpus for Pashto, a language spoken by 60 million people that remains severely underrepresented in NLP. The corpus is assembled from 39 sources spanning seven HuggingFace datasets and 32 purpose-built web scrapers, processed through a reproducible pipeline with Arabic-script tokenization, SHA-256 deduplication, and quality filtering. At 1.25B words across 2.81 million documents, PashtoCorp is 40x larger than the OSCAR Pashto subset and 83x larger than the previously largest dedicated Pashto corpus. Continued MLM pretraining of XLM-R-base on PashtoCorp reduces held-out perplexity by 25.1% (8.08->6.06). On WikiANN Pashto NER, the pretrained model improves entity F1 by 10% relative (19.0%->21.0%) and reduces training variance nearly 7x; the largest gain appears at 50 training sentences (+27%), with PashtoCorp covering 97.9% of WikiANN entity vocabulary. On Belebele Pashto reading comprehension, Gemma-3n achieves 64.6% accuracy, the first published LLM baseline for Pashto on this benchmark. A leave-one-out source ablation shows that Wikipedia (0.7% of documents) is the most critical source for NER: removing it alone reduces entity F1 by 47%. Corpus data, trained model, and code are available at https://huggingface.co/datasets/ihanif/pashto-corpus, https://huggingface.co/ihanif/xlmr-pashto, and https://github.com/ihanif/pashto-corpus.

## 04-042 | Fine PT-PT Web: A High-Quality 41 Billion Tokens Data Collection of the European Portuguese Web
- arXiv: 2609.07699  first public: 2026-09-07  latest: 2026-09-18  primary cat: cs.CL
- authors (10): Gonçalo Vinagre; Rui Pedro Guerra; Pedro Gomes; Miguel Moura Ramos; Duarte Miguel Alves; Afonso Simplício ...
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: ['05']
- arXiv comment: 16 pages, 9 figures, EMNLP 2026 Main
- URLs on first pages of PDF: https://github.com/huggingface/fineweb-2/
- pages: 16

ABSTRACT: Curating Web corpora for regional language variants like European Portuguese (PT-PT) is heavily bottlenecked by dialectal overlap (mainly with PT-BR) and data processing scale. This paper presents an efficient pipeline to curate a production-ready PT-PT corpus from the Portuguese Web, spanning 411 TB of raw data from Arquivo.pt. We introduce a novel post-scraping block that removes boilerplate and line duplicates prior to filtering. This early-stage intervention increases final document yield by 19.04% by rescuing valid text that standard heuristic filters prematurely discard. Integrated with rigorous language identification, weighted fuzzy deduplication, and neural quality classification, our pipeline offers a scalable framework and a clean, representative corpus optimized for LLM pre-training.

## 04-043 | Why Low-Resource NLP Needs More Than Cross-Lingual Transfer: Lessons Learned from Luxembourgish
- arXiv: 2605.10714  first public: 2026-05-11  latest: 2026-05-11  primary cat: cs.CL
- authors (4): Fred Philippy; Siwen Guo; Jacques Klein; Tegawendé F. Bissyandé
- seed subtopic: 低资源语料构建案例; type: 原始研究; cross: []
- arXiv comment: Accepted at BigPicture Workshop 2026 (co-located with ACL 2026)
- pages: 12

ABSTRACT: Cross-lingual transfer has become a central paradigm for extending natural language processing (NLP) technologies to low-resource languages. By leveraging supervision from high-resource languages, multilingual language models can achieve strong task performance with little or no labeled target-language data. However, it remains unclear to what extent cross-lingual transfer can substitute for language-specific efforts. In this paper, we synthesize prior research findings and data collection results on Luxembourgish, which, despite its typological proximity to high-resource languages and its presence in a multilingual context, remains insufficiently represented in modern NLP technologies. Across findings, we observe a fundamental interdependence between cross-lingual transfer and language-specific efforts. Cross-lingual transfer can substantially improve target-language performance, but its success depends critically on the availability of sufficiently high-quality, task-aligned target-language data. At the same time, such resources, particularly in low-resource settings, are typically too limited in scale to drive strong performance on their own. Instead, such resources reach their full potential only when leveraged within a cross-lingual framework. We therefore argue that cross-lingual transfer and language-specific efforts should not be viewed as competing alternatives. Instead, they function as complementary components of a sustainable low-resource NLP pipeline. Based on these insights, we provide practical guidelines for integrating and balancing cross-lingual transfer with language-specific development in sustainable low-resource NLP pipelines.

## 04-044 | Beyond Catalogue Counts: the Dataset Visibility Asymmetry in Low-Resource Multilingual NLP
- arXiv: 2605.17442  first public: 2026-05-17  latest: 2026-05-17  primary cat: cs.CL
- authors (2): Zhiyin Tan; Changxu Duan
- seed subtopic: 语料文档化与资源可见性; type: 原始研究; cross: []
- arXiv comment: Accepted at the 15th edition of the Language Resources and Evaluation Conference (LREC 2026)
- doi: 10.63317/3bep4yiomtp2
- URLs on first pages of PDF: https://github.com/zhiyintan/dataset-visibility-asymmetry
- pages: 12

ABSTRACT: Multilingual NLP often relies on dataset counts from centralized catalogues to characterize which languages are resource-rich or resource-poor. However, these catalogues record only one layer of dataset visibility: what has been registered or institutionally distributed. They do not necessarily reflect which datasets are created, cited, or reused in the research literature. To examine this gap, we combine a catalogue-based baseline with literature-backed evidence of dataset circulation. We introduce the Resource Density Index (RDI), defined as the number of catalogued datasets per one million speakers, and compute it for the 200 most widely spoken languages in Ethnologue. Among them, 118 languages (59%) have an average RDI of zero across the LRE Map and the Linguistic Data Consortium (LDC), and another 23 fall below 0.1, corresponding to at most one catalogued dataset per ten million speakers. We then apply an LLM-assisted citation-mining pipeline over the Semantic Scholar corpus to these 141 low-visibility languages. After manual validation and consolidation, we identify 609 unique datasets across 53 languages, of which 356 remain openly accessible through working public links. These results reveal a substantial visibility gap: many large-speaker languages appear data-poor in catalogue records yet show clear evidence of dataset activity in the research literature. Our findings suggest that multilingual data scarcity should be understood not only as a production problem, but also as a question of documentation, discoverability, and long-term accessibility. Code and data are publicly available at (https://github.com/zhiyintan/dataset-visibility-asymmetry).

## 04-045 | Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on Hugging Face
- arXiv: 2401.13822  first public: 2024-01-24  latest: 2024-01-24  primary cat: cs.LG
- authors (3): Xinyu Yang; Weixin Liang; James Zou
- seed subtopic: 语料文档化; type: 原始研究; cross: []
- arXiv comment: Accepted to the main conference of ICLR 2024
- URLs on first pages of PDF: https://github.com/huggingface/datasets/
- pages: 18

ABSTRACT: Advances in machine learning are closely tied to the creation of datasets. While data documentation is widely recognized as essential to the reliability, reproducibility, and transparency of ML, we lack a systematic empirical understanding of current dataset documentation practices. To shed light on this question, here we take Hugging Face -- one of the largest platforms for sharing and collaborating on ML models and datasets -- as a prominent case study. By analyzing all 7,433 dataset documentation on Hugging Face, our investigation provides an overview of the Hugging Face dataset ecosystem and insights into dataset documentation practices, yielding 5 main findings: (1) The dataset card completion rate shows marked heterogeneity correlated with dataset popularity. (2) A granular examination of each section within the dataset card reveals that the practitioners seem to prioritize Dataset Description and Dataset Structure sections, while the Considerations for Using the Data section receives the lowest proportion of content. (3) By analyzing the subsections within each section and utilizing topic modeling to identify key topics, we uncover what is discussed in each section, and underscore significant themes encompassing both technical and social impacts, as well as limitations within the Considerations for Using the Data section. (4) Our findings also highlight the need for improved accessibility and reproducibility of datasets in the Usage sections. (5) In addition, our human annotation evaluation emphasizes the pivotal role of comprehensive dataset content in shaping individuals' perceptions of a dataset card's overall quality. Overall, our study offers a unique perspective on analyzing dataset documentation through large-scale data science analysis and underlines the need for more thorough dataset documentation in machine learning research.

## 04-046 | SEADialogues: A Multilingual Culturally Grounded Multi-turn Dialogue Dataset on Southeast Asian Languages
- arXiv: 2508.07069  first public: 2025-08-09  latest: 2025-08-09  primary cat: cs.CL
- authors (9): Muhammad Dehan Al Kautsar; Aswin Candra; Muhammad Alif Al Hakim; Maxalmina Satria Kahfi; Fajri Koto; Alham Fikri Aji ...
- seed subtopic: 对话语料; type: 基准与数据集; cross: ['13']
- arXiv comment: Preprint
- pages: 28

ABSTRACT: Although numerous datasets have been developed to support dialogue systems, most existing chit-chat datasets overlook the cultural nuances inherent in natural human conversations. To address this gap, we introduce SEADialogues, a culturally grounded dialogue dataset centered on Southeast Asia, a region with over 700 million people and immense cultural diversity. Our dataset features dialogues in eight languages from six Southeast Asian countries, many of which are low-resource despite having sizable speaker populations. To enhance cultural relevance and personalization, each dialogue includes persona attributes and two culturally grounded topics that reflect everyday life in the respective communities. Furthermore, we release a multi-turn dialogue dataset to advance research on culturally aware and human-centric large language models, including conversational dialogue agents.

## 04-047 | An Evaluation Study of Hybrid Methods for Multilingual PII Detection
- arXiv: 2510.07551  first public: 2025-10-08  latest: 2025-10-08  primary cat: cs.AI
- authors (7): Harshit Rajgarhia; Suryam Gupta; Asif Shaik; Gulipalli Praveen Kumar; Y Santhoshraj; Sanka Nithya Tanvy Nishitha ...
- seed subtopic: 隐私与个人信息; type: 原始研究; cross: []
- pages: 10

ABSTRACT: The detection of Personally Identifiable Information (PII) is critical for privacy compliance but remains challenging in low-resource languages due to linguistic diversity and limited annotated data. We present RECAP, a hybrid framework that combines deterministic regular expressions with context-aware large language models (LLMs) for scalable PII detection across 13 low-resource locales. RECAP's modular design supports over 300 entity types without retraining, using a three-phase refinement pipeline for disambiguation and filtering. Benchmarked with nervaluate, our system outperforms fine-tuned NER models by 82% and zero-shot LLMs by 17% in weighted F1-score. This work offers a scalable and adaptable solution for efficient PII detection in compliance-focused applications.

## 04-048 | ks-pret-5m: a 5 million word, 12 million token kashmiri pretraining dataset
- arXiv: 2604.11066  first public: 2026-04-13  latest: 2026-04-13  primary cat: cs.CL
- authors (2): Haq Nawaz Malik; Nahfid Nissar
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: ['05']
- pages: 5

ABSTRACT: We present KS-PRET-5M, the largest publicly available pretraining dataset for the Kashmiri language, comprising 5,090,244 (5.09M) words, 27,692,959 (27.6M) characters, and a vocabulary of 295,433 (295.4K) unique word types. We assembled the dataset from two source classes: digitized archival and literary material, encompassing literature, news, biographies, novels, poetry, religious scholarship, and academic writing, recovered from the proprietary InPage desktop-publishing format using the converter of Malik~\cite{malik2024inpage}, and Unicode-native text collected from Kashmiri-language web sources. All text was processed through an eleven-stage cleaning pipeline that achieves a mean Kashmiri script ratio of 0.9965, reducing Devanagari contamination to 146 characters across the full dataset. We tokenized the dataset empirically using google/muril-base-cased, yielding a subword ratio of 2.383 tokens per word and a total of approximately 12.13 million subword tokens, substantially higher than prior estimates derived from non-Kashmiri Perso-Arabic analogues. KS-PRET-5M is released as a single continuous text stream under CC~BY~4.0 to support language model pretraining, tokenizer training, and computational linguistic research for Kashmiri.

## 04-049 | Better Quality Pre-training Data and T5 Models for African Languages
- arXiv: -  first public: 2023-12  latest:   primary cat: 
- authors (7): Akintunde Oladipo; Mofetoluwa Adeyemi; Orevaoghene Ahia; Abraham Owodunni; Odunayo Ogundepo; David Adelani ...
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: ['05']
- pages: 11

ABSTRACT: (non-arXiv; see seed)

## 04-050 | MADLAD-400: A Multilingual And Document-Level Large Audited Dataset
- arXiv: 2309.04662  first public: 2023-09-09  latest: 2023-09-09  primary cat: cs.CL
- authors (11): Sneha Kudugunta; Isaac Caswell; Biao Zhang; Xavier Garcia; Christopher A. Choquette-Choo; Katherine Lee ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['05']
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/google-research/google-research/tree/master/madlad_400
- pages: 60

ABSTRACT: We introduce MADLAD-400, a manually audited, general domain 3T token monolingual dataset based on CommonCrawl, spanning 419 languages. We discuss the limitations revealed by self-auditing MADLAD-400, and the role data auditing had in the dataset creation process. We then train and release a 10.7B-parameter multilingual machine translation model on 250 billion tokens covering over 450 languages using publicly available data, and find that it is competitive with models that are significantly larger, and report the results on different domains. In addition, we train a 8B-parameter language model, and assess the results on few-shot translation. We make the baseline models available to the research community.

## 04-051 | The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing & Attribution in AI
- arXiv: 2310.16787  first public: 2023-10-25  latest: 2023-11-04  primary cat: cs.CL
- authors (17): Shayne Longpre; Robert Mahari; Anthony Chen; Naana Obeng-Marnu; Damien Sileo; William Brannon ...
- seed subtopic: 数据来源追踪; type: 原始研究; cross: []
- arXiv comment: 30 pages (18 main), 6 figures, 5 tables
- pages: 30

ABSTRACT: The race to train language models on vast, diverse, and inconsistently documented datasets has raised pressing concerns about the legal and ethical risks for practitioners. To remedy these practices threatening data transparency and understanding, we convene a multi-disciplinary effort between legal and machine learning experts to systematically audit and trace 1800+ text datasets. We develop tools and standards to trace the lineage of these datasets, from their source, creators, series of license conditions, properties, and subsequent use. Our landscape analysis highlights the sharp divides in composition and focus of commercially open vs closed datasets, with closed datasets monopolizing important categories: lower resource languages, more creative tasks, richer topic variety, newer and more synthetic training data. This points to a deepening divide in the types of data that are made available under different license conditions, and heightened implications for jurisdictional legal interpretations of copyright and fair use. We also observe frequent miscategorization of licenses on widely used dataset hosting sites, with license omission of 70%+ and error rates of 50%+. This points to a crisis in misattribution and informed use of the most popular datasets driving many recent breakthroughs. As a contribution to ongoing improvements in dataset transparency and responsible use, we release our entire audit, with an interactive UI, the Data Provenance Explorer, which allows practitioners to trace and filter on data provenance for the most popular open source finetuning data collections: www.dataprovenance.org.

## 04-052 | CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages
- arXiv: 2309.09400  first public: 2023-09-17  latest: 2023-09-17  primary cat: cs.CL
- authors (8): Thuat Nguyen; Chien Van Nguyen; Viet Dac Lai; Hieu Man; Nghia Trung Ngo; Franck Dernoncourt ...
- seed subtopic: 多语言网络语料; type: 基准与数据集; cross: ['05']
- arXiv comment: Ongoing Work
- URLs on first pages of PDF: https://github.com/google/cld3 https://huggingface.co/datasets/mc4
- pages: 11

ABSTRACT: The driving factors behind the development of large language models (LLMs) with impressive learning capabilities are their colossal model sizes and extensive training datasets. Along with the progress in natural language processing, LLMs have been frequently made accessible to the public to foster deeper investigation and applications. However, when it comes to training datasets for these LLMs, especially the recent state-of-the-art models, they are often not fully disclosed. Creating training data for high-performing LLMs involves extensive cleaning and deduplication to ensure the necessary level of quality. The lack of transparency for training data has thus hampered research on attributing and addressing hallucination and bias issues in LLMs, hindering replication efforts and further advancements in the community. These challenges become even more pronounced in multilingual learning scenarios, where the available multilingual text datasets are often inadequately collected and cleaned. Consequently, there is a lack of open-source and readily usable dataset to effectively train LLMs in multiple languages. To overcome this issue, we present CulturaX, a substantial multilingual dataset with 6.3 trillion tokens in 167 languages, tailored for LLM development. Our dataset undergoes meticulous cleaning and deduplication through a rigorous pipeline of multiple stages to accomplish the best quality for model training, including language identification, URL-based filtering, metric-based cleaning, document refinement, and data deduplication. CulturaX is fully released to the public in HuggingFace to facilitate research and advancements in multilingual LLMs: https://huggingface.co/datasets/uonlp/CulturaX.

## 04-053 | Participatory Research for Low-resourced Machine Translation: A Case Study in African Languages
- arXiv: 2010.02353  first public: 2020-10-05  latest: 2020-11-06  primary cat: cs.CL
- authors (48): Wilhelmina Nekoto; Vukosi Marivate; Tshinondiwa Matsila; Timi Fasubaa; Tajudeen Kolawole; Taiwo Fagbohungbe ...
- seed subtopic: 语言社区参与与数据主权; type: 原始研究; cross: []
- arXiv comment: Findings of EMNLP 2020; updated benchmarks
- pages: 17

ABSTRACT: Research in NLP lacks geographic diversity, and the question of how NLP can be scaled to low-resourced languages has not yet been adequately solved. "Low-resourced"-ness is a complex problem going beyond data availability and reflects systemic problems in society. In this paper, we focus on the task of Machine Translation (MT), that plays a crucial role for information accessibility and communication worldwide. Despite immense improvements in MT over the past decade, MT is centered around a few high-resourced languages. As MT researchers cannot solve the problem of low-resourcedness alone, we propose participatory research as a means to involve all necessary agents required in the MT development process. We demonstrate the feasibility and scalability of participatory research with a case study on MT for African languages. Its implementation leads to a collection of novel translation datasets, MT benchmarks for over 30 languages, with human evaluations for a third of them, and enables participants without formal training to make a unique scientific contribution. Benchmarks, models, data, code, and evaluation results are released under https://github.com/masakhane-io/masakhane-mt.

## 04-054 | Quechua Speech Datasets in Common Voice: The Case of Puno Quechua
- arXiv: 2510.13871  first public: 2025-10-13  latest: 2025-10-13  primary cat: cs.CL
- authors (4): Elwin Huaman; Wendi Huaman; Jorge Luis Huaman; Ninfa Quispe
- seed subtopic: 语言社区参与与数据主权; type: 基准与数据集; cross: []
- arXiv comment: to be published in the 9th Annual International Conference on Information Management and Big Data (SIMBig 2025)
- URLs on first pages of PDF: https://github.com/common-voice/common-voice https://github.com/common-voice/cv-dataset/blob/main/README.md
- pages: 10

ABSTRACT: Under-resourced languages, such as Quechuas, face data and resource scarcity, hindering their development in speech technology. To address this issue, Common Voice presents a crucial opportunity to foster an open and community-driven speech dataset creation. This paper examines the integration of Quechua languages into Common Voice. We detail the current 17 Quechua languages, presenting Puno Quechua (ISO 639-3: qxp) as a focused case study that includes language onboarding and corpus collection of both reading and spontaneous speech data. Our results demonstrate that Common Voice now hosts 191.1 hours of Quechua speech (86\% validated), with Puno Quechua contributing 12 hours (77\% validated), highlighting the Common Voice's potential. We further propose a research agenda addressing technical challenges, alongside ethical considerations for community engagement and indigenous data sovereignty. Our work contributes towards inclusive voice technology and digital empowerment of under-resourced language communities.

## 04-055 | Data Governance in the Age of Large-Scale Data-Driven Language Technology
- arXiv: 2206.03216  first public: 2022-05-04  latest: 2022-11-02  primary cat: cs.CY
- authors (21): Yacine Jernite; Huu Nguyen; Stella Biderman; Anna Rogers; Maraim Masoud; Valentin Danchev ...
- seed subtopic: 数据治理框架; type: 原始研究; cross: []
- arXiv comment: 32 pages: Full paper and Appendices; Association for Computing Machinery, New York, NY, USA, 2206-2222
- journal_ref: Proceedings of 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)
- doi: 10.1145/3531146.3534637
- pages: 26

ABSTRACT: The recent emergence and adoption of Machine Learning technology, and specifically of Large Language Models, has drawn attention to the need for systematic and transparent management of language data. This work proposes an approach to global language data governance that attempts to organize data management amongst stakeholders, values, and rights. Our proposal is informed by prior work on distributed governance that accounts for human values and grounded by an international research collaboration that brings together researchers and practitioners from 60 countries. The framework we present is a multi-party international governance structure focused on language data, and incorporating technical and organizational tools needed to support its work.

## 04-056 | The Zeno's Paradox of `Low-Resource' Languages
- arXiv: 2410.20817  first public: 2024-10-28  latest: 2024-10-28  primary cat: cs.CL
- authors (5): Hellina Hailu Nigatu; Atnafu Lambebo Tonja; Benjamin Rosman; Thamar Solorio; Monojit Choudhury
- seed subtopic: 资源条件界定; type: 综述; cross: []
- arXiv comment: Accepted at EMNLP 2024
- URLs on first pages of PDF: https://github.com/acl-org/acl-anthology
- pages: 22

ABSTRACT: The disparity in the languages commonly studied in Natural Language Processing (NLP) is typically reflected by referring to languages as low vs high-resourced. However, there is limited consensus on what exactly qualifies as a `low-resource language.' To understand how NLP papers define and study `low resource' languages, we qualitatively analyzed 150 papers from the ACL Anthology and popular speech-processing conferences that mention the keyword `low-resource.' Based on our analysis, we show how several interacting axes contribute to `low-resourcedness' of a language and why that makes it difficult to track progress for each individual language. We hope our work (1) elicits explicit definitions of the terminology when it is used in papers and (2) provides grounding for the different axes to consider when connoting a language as low-resource.

## 04-059 | SomaliWeb v1: A Quality-Filtered Somali Web Corpus with a Matched Tokenizer and a Public Language-Identification Benchmark
- arXiv: 2605.18232  first public: 2026-05-18  latest: 2026-05-18  primary cat: cs.CL
- authors (1): Khalid Yusuf Dahir
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: ['05', '06']
- arXiv comment: 16 pages, 6 figures, 6 tables. Code: https://github.com/khaledyusuf44/somali-corpus Dataset: https://huggingface.co/datasets/khaledyusuf44/somaliweb-v1
- URLs on first pages of PDF: https://github.com/khaledyusuf44/somali-corpus https://huggingface.co/datasets/khaledyusuf44/somaliweb-v1
- pages: 16

ABSTRACT: Somali is a Cushitic language of the Horn of Africa with ~25 million speakers, yet no documented dedicated Somali pretraining corpus with a companion tokenizer and language-identification benchmark has been publicly released. Existing Somali text appears either inside multilingual distributions (HPLT v2, CC100, MADLAD-400, OSCAR, mC4) or in small, undocumented Somali-only uploads on Hugging Face. We introduce SomaliWeb v1, a quality-filtered Somali corpus of 819,322 documents (~303M tokens) built from three upstream sources (HPLT v2, CC100, Somali Wikipedia) through a six-stage reproducible pipeline. We release (i) the corpus, (ii) a matched BPE-16K tokenizer, and (iii) the first public side-by-side Somali benchmark of three production language identifiers. Our measurements reveal concrete quality defects in existing distributions: HPLT v2's "cleaned" Somali release retains 17.3% byte-exact duplicates, 56.1% of its documents contain fixable mojibake, and 10.7% of its byte-unique documents are near-duplicates at Jaccard tau=0.80. Our BPE-16K tokenizer emits 40.2% fewer tokens than GPT-4's cl100k_base on FLORES-200 Somali devtest as a tokenizer-level measurement; downstream language-model perplexity comparisons are deferred to a follow-up release.

## 04-060 | OpenWHO: A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages
- arXiv: 2508.16048  first public: 2025-08-22  latest: 2025-10-06  primary cat: cs.CL
- authors (4): Raphaël Merx; Hanna Suominen; Trevor Cohn; Ekaterina Vylomova
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- arXiv comment: Accepted at WMT 2025
- pages: 19

ABSTRACT: In machine translation (MT), health is a high-stakes domain characterised by widespread deployment and domain-specific vocabulary. However, there is a lack of MT evaluation datasets for low-resource languages in this domain. To address this gap, we introduce OpenWHO, a document-level parallel corpus of 2,978 documents and 26,824 sentences from the World Health Organization's e-learning platform. Sourced from expert-authored, professionally translated materials shielded from web-crawling, OpenWHO spans a diverse range of over 20 languages, of which nine are low-resource. Leveraging this new resource, we evaluate modern large language models (LLMs) against traditional MT models. Our findings reveal that LLMs consistently outperform traditional MT models, with Gemini 2.5 Flash achieving a +4.79 ChrF point improvement over NLLB-54B on our low-resource test set. Further, we investigate how LLM context utilisation affects accuracy, finding that the benefits of document-level translation are most pronounced in specialised domains like health. We release the OpenWHO corpus to encourage further research into low-resource MT in the health domain.

## 04-061 | EthioMT: Parallel Corpus for Low-resource Ethiopian Languages
- arXiv: 2403.19365  first public: 2024-03-28  latest: 2024-03-28  primary cat: cs.CL
- authors (4): Atnafu Lambebo Tonja; Olga Kolesnikova; Alexander Gelbukh; Jugal Kalita
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- arXiv comment: Accepted at The Fifth workshop on Resources for African Indigenous Languages (RAIL) 2024 ( LREC-COLING 2024)
- pages: 8

ABSTRACT: Recent research in natural language processing (NLP) has achieved impressive performance in tasks such as machine translation (MT), news classification, and question-answering in high-resource languages. However, the performance of MT leaves much to be desired for low-resource languages. This is due to the smaller size of available parallel corpora in these languages, if such corpora are available at all. NLP in Ethiopian languages suffers from the same issues due to the unavailability of publicly accessible datasets for NLP tasks, including MT. To help the research community and foster research for Ethiopian languages, we introduce EthioMT -- a new parallel corpus for 15 languages. We also create a new benchmark by collecting a dataset for better-researched languages in Ethiopia. We evaluate the newly collected corpus and the benchmark dataset for 23 Ethiopian languages using transformer and fine-tuning approaches.

## 04-062 | NSINA: A News Corpus for Sinhala
- arXiv: 2403.16571  first public: 2024-03-25  latest: 2024-03-25  primary cat: cs.CL
- authors (4): Hansi Hettiarachchi; Damith Premasiri; Lasitha Uyangodage; Tharindu Ranasinghe
- seed subtopic: 低资源语料构建案例; type: 基准与数据集; cross: []
- arXiv comment: Accepted to LREC-COLING 2024 (The 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation)
- URLs on first pages of PDF: https://github.com/Sinhala-NLP/
- pages: 6

ABSTRACT: The introduction of large language models (LLMs) has advanced natural language processing (NLP), but their effectiveness is largely dependent on pre-training resources. This is especially evident in low-resource languages, such as Sinhala, which face two primary challenges: the lack of substantial training data and limited benchmarking datasets. In response, this study introduces NSINA, a comprehensive news corpus of over 500,000 articles from popular Sinhala news websites, along with three NLP tasks: news media identification, news category prediction, and news headline generation. The release of NSINA aims to provide a solution to challenges in adapting LLMs to Sinhala, offering valuable resources and benchmarks for improving NLP in the Sinhala language. NSINA is the largest news corpus for Sinhala, available up to date.

## 04-063 | Building a Functional Machine Translation Corpus for Kpelle
- arXiv: 2505.18905  first public: 2025-05-24  latest: 2025-05-24  primary cat: cs.CL
- authors (3): Kweku Andoh Yamoah; Jackson Weako; Emmanuel J. Dorley
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- journal_ref: Proceedings of the Sixth Workshop on African Natural Language Processing (AfricaNLP 2025)
- doi: 10.18653/v1/2025.africanlp-1.8
- pages: 12

ABSTRACT: In this paper, we introduce the first publicly available English-Kpelle dataset for machine translation, comprising over 2000 sentence pairs drawn from everyday communication, religious texts, and educational materials. By fine-tuning Meta's No Language Left Behind(NLLB) model on two versions of the dataset, we achieved BLEU scores of up to 30 in the Kpelle-to-English direction, demonstrating the benefits of data augmentation. Our findings align with NLLB-200 benchmarks on other African languages, underscoring Kpelle's potential for competitive performance despite its low-resource status. Beyond machine translation, this dataset enables broader NLP tasks, including speech recognition and language modelling. We conclude with a roadmap for future dataset expansion, emphasizing orthographic consistency, community-driven validation, and interdisciplinary collaboration to advance inclusive language technology development for Kpelle and other low-resourced Mande languages.

## 04-064 | A Komi-Yazva--Russian Parallel Corpus and Evaluation Protocol for Zero- and Few-Shot LLM Translation
- arXiv: 2606.06420  first public: 2026-06-04  latest: 2026-06-04  primary cat: cs.CL
- authors (1): Petr Parshakov
- seed subtopic: 平行语料; type: 基准与数据集; cross: ['09']
- arXiv comment: 18 pages, 6 tables, 3 figures
- pages: 18

ABSTRACT: We present the first Komi-Yazva--Russian parallel corpus together with an explicit evaluation protocol for studying LLM translation in an endangered, extremely low-resource setting. The dataset contains 457 aligned sentence pairs from 74 narrative texts and is accompanied by documented provenance, sentence-level alignment, and story identifiers that enable leakage-aware evaluation. We use this setup to compare modern large language models on Komi-Yazva-to-Russian translation under severe parallel-data scarcity in zero-shot and retrieval-based few-shot regimes. The protocol includes story-level cross-validation, deterministic retrieval for few-shot prompting, strict validation of generated outputs, complementary reference-based and judge-based metrics, and story-level uncertainty estimates. Across models, LLMs produce non-trivial translations, but performance varies strongly by model family and prompting regime. Retrieval-based few-shot prompting consistently improves over zero-shot prompting, while gains beyond a small retrieved context remain limited. The results show that evaluative conclusions in this setting depend materially on metric choice and failure handling, so the paper frames the corpus as both a dataset contribution and a reproducible evaluation testbed for endangered-language machine translation.
