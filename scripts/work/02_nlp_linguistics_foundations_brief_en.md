# Brief for annotation: 02 自然语言处理与语言学基础

## 02-001 | Evaluating Morphological Compositional Generalization in Large Language Models
- arXiv: 2410.12656  first public: 2024-10-16  latest: 2025-06-05  primary cat: cs.CL
- authors (9): Mete Ismayilzada; Defne Circi; Jonne Sälevä; Hale Sirin; Abdullatif Köksal; Bhuwan Dhingra ...
- seed subtopic: 形态学与大模型; type: 原始研究; cross: []
- arXiv comment: Accepted to NAACL 2025
- URLs on first pages of PDF: https://github.com/mismayil/morph-gen
- pages: 36

ABSTRACT: Large language models (LLMs) have demonstrated significant progress in various natural language generation and understanding tasks. However, their linguistic generalization capabilities remain questionable, raising doubts about whether these models learn language similarly to humans. While humans exhibit compositional generalization and linguistic creativity in language use, the extent to which LLMs replicate these abilities, particularly in morphology, is under-explored. In this work, we systematically investigate the morphological generalization abilities of LLMs through the lens of compositionality. We define morphemes as compositional primitives and design a novel suite of generative and discriminative tasks to assess morphological productivity and systematicity. Focusing on agglutinative languages such as Turkish and Finnish, we evaluate several state-of-the-art instruction-finetuned multilingual models, including GPT-4 and Gemini. Our analysis shows that LLMs struggle with morphological compositional generalization particularly when applied to novel word roots, with performance declining sharply as morphological complexity increases. While models can identify individual morphological combinations better than chance, their performance lacks systematicity, leading to significant accuracy gaps compared to humans.

## 02-003 | Counting the Bugs in ChatGPT's Wugs: A Multilingual Investigation into the Morphological Capabilities of a Large Language Model
- arXiv: 2310.15113  first public: 2023-10-23  latest: 2023-10-26  primary cat: cs.CL
- authors (13): Leonie Weissweiler; Valentin Hofmann; Anjali Kantharuban; Anna Cai; Ritam Dutt; Amey Hengle ...
- seed subtopic: 形态学与大模型; type: 原始研究; cross: []
- arXiv comment: EMNLP 2023
- pages: 17

ABSTRACT: Large language models (LLMs) have recently reached an impressive level of linguistic capability, prompting comparisons with human language skills. However, there have been relatively few systematic inquiries into the linguistic capabilities of the latest generation of LLMs, and those studies that do exist (i) ignore the remarkable ability of humans to generalize, (ii) focus only on English, and (iii) investigate syntax or semantics and overlook other capabilities that lie at the heart of human language, like morphology. Here, we close these gaps by conducting the first rigorous analysis of the morphological capabilities of ChatGPT in four typologically varied languages (specifically, English, German, Tamil, and Turkish). We apply a version of Berko's (1958) wug test to ChatGPT, using novel, uncontaminated datasets for the four examined languages. We find that ChatGPT massively underperforms purpose-built systems, particularly in English. Overall, our results -- through the lens of morphology -- cast a new light on the linguistic capabilities of ChatGPT, suggesting that claims of human-like language skills are premature and misleading.

## 02-004 | GlossLM: A Massively Multilingual Corpus and Pretrained Model for Interlinear Glossed Text
- arXiv: 2403.06399  first public: 2024-03-11  latest: 2024-11-12  primary cat: cs.CL
- authors (7): Michael Ginn; Lindia Tjuatja; Taiqi He; Enora Rice; Graham Neubig; Alexis Palmer ...
- seed subtopic: 形态学与大模型; type: 基准与数据集; cross: []
- arXiv comment: EMNLP 2024. First two authors are equal contribution
- URLs on first pages of PDF: https://huggingface.co/collections/lecslab/
- pages: 20

ABSTRACT: Language documentation projects often involve the creation of annotated text in a format such as interlinear glossed text (IGT), which captures fine-grained morphosyntactic analyses in a morpheme-by-morpheme format. However, there are few existing resources providing large amounts of standardized, easily accessible IGT data, limiting their applicability to linguistic research, and making it difficult to use such data in NLP modeling. We compile the largest existing corpus of IGT data from a variety of sources, covering over 450k examples across 1.8k languages, to enable research on crosslingual transfer and IGT generation. We normalize much of our data to follow a standard set of labels across languages. Furthermore, we explore the task of automatically generating IGT in order to aid documentation projects. As many languages lack sufficient monolingual data, we pretrain a large multilingual model on our corpus. We demonstrate the utility of this model by finetuning it on monolingual corpora, outperforming SOTA models by up to 6.6\%. Our pretrained model and dataset are available on Hugging Face.

## 02-005 | Can we teach language models to gloss endangered languages?
- arXiv: 2406.18895  first public: 2024-06-27  latest: 2024-10-03  primary cat: cs.CL
- authors (3): Michael Ginn; Mans Hulden; Alexis Palmer
- seed subtopic: 形态学与大模型; type: 原始研究; cross: []
- arXiv comment: Accepted to EMNLP 2024 Findings
- URLs on first pages of PDF: https://github.com/michaelpginn/igt-icl
- pages: 16

ABSTRACT: Interlinear glossed text (IGT) is a popular format in language documentation projects, where each morpheme is labeled with a descriptive annotation. Automating the creation of interlinear glossed text would be desirable to reduce annotator effort and maintain consistency across annotated corpora. Prior research has explored a number of statistical and neural methods for automatically producing IGT. As large language models (LLMs) have showed promising results across multilingual tasks, even for rare, endangered languages, it is natural to wonder whether they can be utilized for the task of generating IGT. We explore whether LLMs can be effective at the task of interlinear glossing with in-context learning, without any traditional training. We propose new approaches for selecting examples to provide in-context, observing that targeted selection can significantly improve performance. We find that LLM-based methods beat standard transformer baselines, despite requiring no training at all. These approaches still underperform state-of-the-art supervised systems for the task, but are highly practical for researchers outside of the NLP community, requiring minimal effort to use.

## 02-006 | Can LLMs Help Create Grammar?: Automating Grammar Creation for Endangered Languages with In-Context Learning
- arXiv: 2412.10960  first public: 2024-12-14  latest: 2024-12-14  primary cat: cs.CL
- authors (2): Piyapath T Spencer; Nanthipat Kongborrirak
- seed subtopic: 形态学与大模型; type: 原始研究; cross: []
- arXiv comment: Preprint manuscript. Under revision. Accepted to COLING 2025
- pages: 10

ABSTRACT: Yes! In the present-day documenting and preserving endangered languages, the application of Large Language Models (LLMs) presents a promising approach. This paper explores how LLMs, particularly through in-context learning, can assist in generating grammatical information for low-resource languages with limited amount of data. We takes Moklen as a case study to evaluate the efficacy of LLMs in producing coherent grammatical rules and lexical entries using only bilingual dictionaries and parallel sentences of the unknown language without building the model from scratch. Our methodology involves organising the existing linguistic data and prompting to efficiently enable to generate formal XLE grammar. Our results demonstrate that LLMs can successfully capture key grammatical structures and lexical information, although challenges such as the potential for English grammatical biases remain. This study highlights the potential of LLMs to enhance language documentation efforts, providing a cost-effective solution for generating linguistic data and contributing to the preservation of endangered languages.

## 02-007 | UniMorph 4.0: Universal Morphology
- arXiv: 2205.03608  first public: 2022-05-07  latest: 2022-06-19  primary cat: cs.CL
- authors (96): Khuyagbaatar Batsuren; Omer Goldman; Salam Khalifa; Nizar Habash; Witold Kieraś; Gábor Bella ...
- seed subtopic: 形态学与大模型; type: 基准与数据集; cross: []
- arXiv comment: LREC 2022; The first two authors made equal contributions
- pages: 16

ABSTRACT: The Universal Morphology (UniMorph) project is a collaborative effort providing broad-coverage instantiated normalized morphological inflection tables for hundreds of diverse world languages. The project comprises two major thrusts: a language-independent feature schema for rich morphological annotation and a type-level resource of annotated data in diverse languages realizing that schema. This paper presents the expansions and improvements made on several fronts over the last couple of years (since McCarthy et al. (2020)). Collaborative efforts by numerous linguists have added 67 new languages, including 30 endangered languages. We have implemented several improvements to the extraction pipeline to tackle some issues, e.g. missing gender and macron information. We have also amended the schema to use a hierarchical structure that is needed for morphological phenomena like multiple-argument agreement and case stacking, while adding some missing morphological features to make the schema more inclusive. In light of the last UniMorph release, we also augmented the database with morpheme segmentation for 16 languages. Lastly, this new release makes a push towards inclusion of derivational morphology in UniMorph by enriching the data and annotation schema with instances representing derivational processes from MorphyNet.

## 02-008 | Mission: Impossible Language Models
- arXiv: 2401.06416  first public: 2024-01-12  latest: 2024-08-02  primary cat: cs.CL
- authors (5): Julie Kallini; Isabel Papadimitriou; Richard Futrell; Kyle Mahowald; Christopher Potts
- seed subtopic: 句法与语言能力探测; type: 原始研究; cross: []
- pages: 24

ABSTRACT: Chomsky and others have very directly claimed that large language models (LLMs) are equally capable of learning languages that are possible and impossible for humans to learn. However, there is very little published experimental evidence to support such a claim. Here, we develop a set of synthetic impossible languages of differing complexity, each designed by systematically altering English data with unnatural word orders and grammar rules. These languages lie on an impossibility continuum: at one end are languages that are inherently impossible, such as random and irreversible shuffles of English words, and on the other, languages that may not be intuitively impossible but are often considered so in linguistics, particularly those with rules based on counting word positions. We report on a wide range of evaluations to assess the capacity of GPT-2 small models to learn these uncontroversially impossible languages, and crucially, we perform these assessments at various stages throughout training to compare the learning process for each language. Our core finding is that GPT-2 struggles to learn impossible languages when compared to English as a control, challenging the core claim. More importantly, we hope our approach opens up a productive line of inquiry in which different LLM architectures are tested on a variety of impossible languages in an effort to learn more about how LLMs can be used as tools for these cognitive and typological investigations.

## 02-009 | Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages
- arXiv: 2501.06346  first public: 2025-01-10  latest: 2025-05-23  primary cat: cs.CL
- authors (4): Jannik Brinkmann; Chris Wendler; Christian Bartelt; Aaron Mueller
- seed subtopic: 句法与语言能力探测; type: 原始研究; cross: []
- pages: 20

ABSTRACT: Human bilinguals often use similar brain regions to process multiple languages, depending on when they learned their second language and their proficiency. In large language models (LLMs), how are multiple languages learned and encoded? In this work, we explore the extent to which LLMs share representations of morphsyntactic concepts such as grammatical number, gender, and tense across languages. We train sparse autoencoders on Llama-3-8B and Aya-23-8B, and demonstrate that abstract grammatical concepts are often encoded in feature directions shared across many languages. We use causal interventions to verify the multilingual nature of these representations; specifically, we show that ablating only multilingual features decreases classifier performance to near-chance across languages. We then use these features to precisely modify model behavior in a machine translation task; this demonstrates both the generality and selectivity of these feature's roles in the network. Our findings suggest that even models trained predominantly on English data can develop robust, cross-lingual abstractions of morphosyntactic concepts.

## 02-010 | MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguistic Minimal Pairs
- arXiv: 2504.02768  first public: 2025-04-03  latest: 2026-04-30  primary cat: cs.CL
- authors (4): Jaap Jumelet; Leonie Weissweiler; Joakim Nivre; Arianna Bisazza
- seed subtopic: 句法与语言能力探测; type: 基准与数据集; cross: ['15']
- arXiv comment: Published in TACL, MIT Press
- pages: 24

ABSTRACT: We introduce MultiBLiMP 1.0, a massively multilingual benchmark of linguistic minimal pairs, covering 101 languages and 2 types of subject-verb agreement, containing more than 128,000 minimal pairs. Our minimal pairs are created using a fully automated pipeline, leveraging the large-scale linguistic resources of Universal Dependencies and UniMorph. MultiBLiMP 1.0 evaluates abilities of LLMs at an unprecedented multilingual scale, and highlights the shortcomings of the current state-of-the-art in modelling low-resource languages.

## 02-011 | The Same But Different: Structural Similarities and Differences in Multilingual Language Modeling
- arXiv: 2410.09223  first public: 2024-10-11  latest: 2024-10-11  primary cat: cs.CL
- authors (5): Ruochen Zhang; Qinan Yu; Matianyu Zang; Carsten Eickhoff; Ellie Pavlick
- seed subtopic: 句法与语言能力探测; type: 原始研究; cross: []
- pages: 21

ABSTRACT: We employ new tools from mechanistic interpretability in order to ask whether the internal structure of large language models (LLMs) shows correspondence to the linguistic structures which underlie the languages on which they are trained. In particular, we ask (1) when two languages employ the same morphosyntactic processes, do LLMs handle them using shared internal circuitry? and (2) when two languages require different morphosyntactic processes, do LLMs handle them using different internal circuitry? Using English and Chinese multilingual and monolingual models, we analyze the internal circuitry involved in two tasks. We find evidence that models employ the same circuit to handle the same syntactic process independently of the language in which it occurs, and that this is the case even for monolingual models trained completely independently. Moreover, we show that multilingual models employ language-specific components (attention heads and feed-forward networks) when needed to handle linguistic processes (e.g., morphological marking) that only exist in some languages. Together, our results provide new insights into how LLMs trade off between exploiting common structures and preserving linguistic differences when tasked with modeling multiple languages simultaneously.

## 02-012 | Linguistic Minimal Pairs Elicit Linguistic Similarity in Large Language Models
- arXiv: 2409.12435  first public: 2024-09-19  latest: 2024-12-13  primary cat: cs.CL
- authors (5): Xinyu Zhou; Delong Chen; Samuel Cahyawijaya; Xufeng Duan; Zhenguang G. Cai
- seed subtopic: 句法与语言能力探测; type: 原始研究; cross: []
- arXiv comment: COLING 2025
- pages: 23

ABSTRACT: We introduce a novel analysis that leverages linguistic minimal pairs to probe the internal linguistic representations of Large Language Models (LLMs). By measuring the similarity between LLM activation differences across minimal pairs, we quantify the and gain insight into the linguistic knowledge captured by LLMs. Our large-scale experiments, spanning 100+ LLMs and 150k minimal pairs in three languages, reveal properties of linguistic similarity from four key aspects: consistency across LLMs, relation to theoretical categorizations, dependency to semantic context, and cross-lingual alignment of relevant phenomena. Our findings suggest that 1) linguistic similarity is significantly influenced by training data exposure, leading to higher cross-LLM agreement in higher-resource languages. 2) Linguistic similarity strongly aligns with fine-grained theoretical linguistic categories but weakly with broader ones. 3) Linguistic similarity shows a weak correlation with semantic similarity, showing its context-dependent nature. 4) LLMs exhibit limited cross-lingual alignment in their understanding of relevant linguistic phenomena. This work demonstrates the potential of minimal pairs as a window into the neural representations of language in LLMs, shedding light on the relationship between LLMs and linguistic theory. Codes and data are available at https://github.com/ChenDelong1999/Linguistic-Similarity

## 02-013 | Language Models as Models of Language
- arXiv: 2408.07144  first public: 2024-08-13  latest: 2024-08-13  primary cat: cs.CL
- authors (1): Raphaël Millière
- seed subtopic: 句法与语言能力探测; type: 综述; cross: []
- arXiv comment: Forthcoming in Nefdt, R., Dupre, G., \& Stanton, K. (eds.), The Oxford Handbook of the Philosophy of Linguistics. Oxford University Press
- pages: 55

ABSTRACT: This chapter critically examines the potential contributions of modern language models to theoretical linguistics. Despite their focus on engineering goals, these models' ability to acquire sophisticated linguistic knowledge from mere exposure to data warrants a careful reassessment of their relevance to linguistic theory. I review a growing body of empirical evidence suggesting that language models can learn hierarchical syntactic structure and exhibit sensitivity to various linguistic phenomena, even when trained on developmentally plausible amounts of data. While the competence/performance distinction has been invoked to dismiss the relevance of such models to linguistic theory, I argue that this assessment may be premature. By carefully controlling learning conditions and making use of causal intervention methods, experiments with language models can potentially constrain hypotheses about language acquisition and competence. I conclude that closer collaboration between theoretical linguists and computational researchers could yield valuable insights, particularly in advancing debates about linguistic nativism.

## 02-014 | What Languages are Easy to Language-Model? A Perspective from Learning Probabilistic Regular Languages
- arXiv: 2406.04289  first public: 2024-06-06  latest: 2025-01-12  primary cat: cs.CL
- authors (8): Nadav Borenstein; Anej Svete; Robin Chan; Josef Valvoda; Franz Nowak; Isabelle Augenstein ...
- seed subtopic: 句法与语言能力探测; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2024
- pages: 20

ABSTRACT: What can large language models learn? By definition, language models (LM) are distributions over strings. Therefore, an intuitive way of addressing the above question is to formalize it as a matter of learnability of classes of distributions over strings. While prior work in this direction focused on assessing the theoretical limits, in contrast, we seek to understand the empirical learnability. Unlike prior empirical work, we evaluate neural LMs on their home turf-learning probabilistic languages-rather than as classifiers of formal languages. In particular, we investigate the learnability of regular LMs (RLMs) by RNN and Transformer LMs. We empirically test the learnability of RLMs as a function of various complexity parameters of the RLM and the hidden state size of the neural LM. We find that the RLM rank, which corresponds to the size of linear space spanned by the logits of its conditional distributions, and the expected length of sampled strings are strong and significant predictors of learnability for both RNNs and Transformers. Several other predictors also reach significance, but with differing patterns between RNNs and Transformers.

## 02-016 | URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base
- arXiv: 2409.18472  first public: 2024-09-27  latest: 2025-02-14  primary cat: cs.CL
- authors (8): Aditya Khan; Mason Shipton; David Anugraha; Kaiyao Duan; Phuong H. Hoang; Eric Khiu ...
- seed subtopic: 语言类型学与跨语言迁移; type: 基准与数据集; cross: []
- arXiv comment: Accepted to COLING 2025
- pages: 16

ABSTRACT: URIEL is a knowledge base offering geographical, phylogenetic, and typological vector representations for 7970 languages. It includes distance measures between these vectors for 4005 languages, which are accessible via the lang2vec tool. Despite being frequently cited, URIEL is limited in terms of linguistic inclusion and overall usability. To tackle these challenges, we introduce URIEL+, an enhanced version of URIEL and lang2vec that addresses these limitations. In addition to expanding typological feature coverage for 2898 languages, URIEL+ improves the user experience with robust, customizable distance calculations to better suit the needs of users. These upgrades also offer competitive performance on downstream tasks and provide distances that better align with linguistic distance studies.

## 02-017 | Analyzing the Effect of Linguistic Similarity on Cross-Lingual Transfer: Tasks and Experimental Setups Matter
- arXiv: 2501.14491  first public: 2025-01-24  latest: 2025-05-21  primary cat: cs.CL
- authors (3): Verena Blaschke; Masha Fedzechkina; Maartje ter Hoeve
- seed subtopic: 语言类型学与跨语言迁移; type: 原始研究; cross: []
- arXiv comment: ACL Findings 2025
- pages: 32

ABSTRACT: Cross-lingual transfer is a popular approach to increase the amount of training data for NLP tasks in a low-resource context. However, the best strategy to decide which cross-lingual data to include is unclear. Prior research often focuses on a small set of languages from a few language families and/or a single task. It is still an open question how these findings extend to a wider variety of languages and tasks. In this work, we analyze cross-lingual transfer for 263 languages from a wide variety of language families. Moreover, we include three popular NLP tasks: POS tagging, dependency parsing, and topic classification. Our findings indicate that the effect of linguistic similarity on transfer performance depends on a range of factors: the NLP task, the (mono- or multilingual) input representations, and the definition of linguistic similarity.

## 02-018 | What is "Typological Diversity" in NLP?
- arXiv: 2402.04222  first public: 2024-02-06  latest: 2024-10-02  primary cat: cs.CL
- authors (4): Esther Ploeger; Wessel Poelman; Miryam de Lhoneux; Johannes Bjerva
- seed subtopic: 语言类型学与跨语言迁移; type: 原始研究; cross: []
- arXiv comment: EMNLP 2024: Main Conference
- URLs on first pages of PDF: https://github.com/WPoelman/typ-div
- pages: 20

ABSTRACT: The NLP research community has devoted increased attention to languages beyond English, resulting in considerable improvements for multilingual NLP. However, these improvements only apply to a small subset of the world's languages. Aiming to extend this, an increasing number of papers aspires to enhance generalizable multilingual performance across languages. To this end, linguistic typology is commonly used to motivate language selection, on the basis that a broad typological sample ought to imply generalization across a broad range of languages. These selections are often described as being 'typologically diverse'. In this work, we systematically investigate NLP research that includes claims regarding 'typological diversity'. We find there are no set definitions or criteria for such claims. We introduce metrics to approximate the diversity of language selection along several axes and find that the results vary considerably across papers. Crucially, we show that skewed language selection can lead to overestimated multilingual performance. We recommend future work to include an operationalization of 'typological diversity' that empirically justifies the diversity of language samples.

## 02-019 | A Principled Framework for Evaluating on Typologically Diverse Languages
- arXiv: 2407.05022  first public: 2024-07-06  latest: 2025-09-08  primary cat: cs.CL
- authors (6): Esther Ploeger; Wessel Poelman; Andreas Holck Høeg-Petersen; Anders Schlichtkrull; Miryam de Lhoneux; Johannes Bjerva
- seed subtopic: 语言类型学与跨语言迁移; type: 原始研究; cross: ['15']
- arXiv comment: Revised version
- URLs on first pages of PDF: https://github.com/esther2000/typdiv-sampling
- pages: 36

ABSTRACT: Beyond individual languages, multilingual natural language processing (NLP) research increasingly aims to develop models that perform well across languages generally. However, evaluating these systems on all the world's languages is practically infeasible. To attain generalizability, representative language sampling is essential. Previous work argues that generalizable multilingual evaluation sets should contain languages with diverse typological properties. However, 'typologically diverse' language samples have been found to vary considerably in this regard, and popular sampling methods are flawed and inconsistent. We present a language sampling framework for selecting highly typologically diverse languages given a sampling frame, informed by language typology. We compare sampling methods with a range of metrics and find that our systematic methods consistently retrieve more typologically diverse language selections than previous methods in NLP. Moreover, we provide evidence that this affects generalizability in multilingual model evaluation, emphasizing the importance of diverse language sampling in NLP evaluation.

## 02-025 | Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages
- arXiv: 2411.02398  first public: 2024-11-04  latest: 2025-06-26  primary cat: cs.CL
- authors (7): Hoang H Nguyen; Khyati Mahajan; Vikas Yadav; Julian Salazar; Philip S. Yu; Masoud Hashemi ...
- seed subtopic: 文字系统、音译与罗马化; type: 原始研究; cross: []
- arXiv comment: Accepted to NAACL 2025 (Main Conference). This version contains minor improvements to the camera-ready
- journal_ref: Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)
- doi: 10.18653/v1/2025.naacl-long.599
- pages: 20

ABSTRACT: Although multilingual LLMs have achieved remarkable performance across benchmarks, we find they continue to underperform on non-Latin script languages across contemporary LLM families. This discrepancy arises from the fact that LLMs are pretrained with orthographic scripts, which are dominated by Latin characters that obscure their shared phonology with non-Latin scripts. We propose leveraging phonemic transcriptions as complementary signals to induce script-invariant representations. Our study demonstrates that integrating phonemic signals improves performance across both non-Latin and Latin script languages, with a particularly significant impact on closing the performance gap between the two. Through detailed experiments, we show that phonemic and orthographic scripts retrieve distinct examples for in-context learning (ICL). This motivates our proposed Mixed-ICL retrieval strategy, where further aggregation from both leads to our significant performance improvements for both Latin script languages (up to 12.6%) and non-Latin script languages (up to 15.1%) compared to randomized ICL retrieval.

## 02-026 | Natural Language Processing for Dialects of a Language: A Survey
- arXiv: 2401.05632  first public: 2024-01-11  latest: 2024-12-06  primary cat: cs.CL
- authors (7): Aditya Joshi; Raj Dabre; Diptesh Kanojia; Zhuang Li; Haolan Zhan; Gholamreza Haffari ...
- seed subtopic: 方言与语言变体; type: 综述; cross: []
- arXiv comment: The paper is under review at ACM Computing Surveys
- pages: 35

ABSTRACT: State-of-the-art natural language processing (NLP) models are trained on massive training corpora, and report a superlative performance on evaluation datasets. This survey delves into an important attribute of these datasets: the dialect of a language. Motivated by the performance degradation of NLP models for dialectal datasets and its implications for the equity of language technologies, we survey past research in NLP for dialects in terms of datasets, and approaches. We describe a wide range of NLP tasks in terms of two categories: natural language understanding (NLU) (for tasks such as dialect classification, sentiment analysis, parsing, and NLU benchmarks) and natural language generation (NLG) (for summarisation, machine translation, and dialogue systems). The survey is also broad in its coverage of languages which include English, Arabic, German, among others. We observe that past work in NLP concerning dialects goes deeper than mere dialect classification, and extends to several NLU and NLG tasks. For these tasks, we describe classical machine learning using statistical models, along with the recent deep learning-based approaches based on pre-trained language models. We expect that this survey will be useful to NLP researchers interested in building equitable language technologies by rethinking LLM benchmarks and model architectures.

## 02-027 | DIALECTBENCH: A NLP Benchmark for Dialects, Varieties, and Closely-Related Languages
- arXiv: 2403.11009  first public: 2024-03-16  latest: 2024-07-07  primary cat: cs.CL
- authors (7): Fahim Faisal; Orevaoghene Ahia; Aarohi Srivastava; Kabir Ahuja; David Chiang; Yulia Tsvetkov ...
- seed subtopic: 方言与语言变体; type: 基准与数据集; cross: ['15']
- arXiv comment: Equal contribution: Fahim Faisal, Orevaoghene Ahia
- URLs on first pages of PDF: https://github.com/ffaisal93/DialectBench
- pages: 43

ABSTRACT: Language technologies should be judged on their usefulness in real-world use cases. An often overlooked aspect in natural language processing (NLP) research and evaluation is language variation in the form of non-standard dialects or language varieties (hereafter, varieties). Most NLP benchmarks are limited to standard language varieties. To fill this gap, we propose DIALECTBENCH, the first-ever large-scale benchmark for NLP on varieties, which aggregates an extensive set of task-varied variety datasets (10 text-level tasks covering 281 varieties). This allows for a comprehensive evaluation of NLP system performance on different language varieties. We provide substantial evidence of performance disparities between standard and non-standard language varieties, and we also identify language clusters with large performance divergence across tasks. We believe DIALECTBENCH provides a comprehensive view of the current state of NLP for language varieties and one step towards advancing it further. Code/data: https://github.com/ffaisal93/DialectBench

## 02-028 | Dialect prejudice predicts AI decisions about people's character, employability, and criminality
- arXiv: 2403.00742  first public: 2024-03-01  latest: 2024-03-01  primary cat: cs.CL
- authors (4): Valentin Hofmann; Pratyusha Ria Kalluri; Dan Jurafsky; Sharese King
- seed subtopic: 方言与语言变体; type: 原始研究; cross: ['10']
- pages: 54

ABSTRACT: Hundreds of millions of people now interact with language models, with uses ranging from serving as a writing aid to informing hiring decisions. Yet these language models are known to perpetuate systematic racial prejudices, making their judgments biased in problematic ways about groups like African Americans. While prior research has focused on overt racism in language models, social scientists have argued that racism with a more subtle character has developed over time. It is unknown whether this covert racism manifests in language models. Here, we demonstrate that language models embody covert racism in the form of dialect prejudice: we extend research showing that Americans hold raciolinguistic stereotypes about speakers of African American English and find that language models have the same prejudice, exhibiting covert stereotypes that are more negative than any human stereotypes about African Americans ever experimentally recorded, although closest to the ones from before the civil rights movement. By contrast, the language models' overt stereotypes about African Americans are much more positive. We demonstrate that dialect prejudice has the potential for harmful consequences by asking language models to make hypothetical decisions about people, based only on how they speak. Language models are more likely to suggest that speakers of African American English be assigned less prestigious jobs, be convicted of crimes, and be sentenced to death. Finally, we show that existing methods for alleviating racial bias in language models such as human feedback training do not mitigate the dialect prejudice, but can exacerbate the discrepancy between covert and overt stereotypes, by teaching language models to superficially conceal the racism that they maintain on a deeper level. Our findings have far-reaching implications for the fair and safe employment of language technology.

## 02-029 | Standard Language Ideology in AI-Generated Language
- arXiv: 2406.08726  first public: 2024-06-13  latest: 2026-06-09  primary cat: cs.CL
- authors (4): Genevieve Smith; Eve Fleisig; Ishita Rustagi; Xavier Yin
- seed subtopic: 方言与语言变体; type: 原始研究; cross: []
- arXiv comment: To appear in the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26)
- pages: 18

ABSTRACT: Large language models (LLMs) generate text that reinforces standard language ideology: a bias towards certain language varieties that are granted more prestige, authority, and legitimacy than others. This paper contributes a sociotechnically grounded faceted taxonomy that illustrates how generative AI systems reproduce standard language ideology and its societal implications. We introduce the concept of standard AI-generated language ideology to explain how AI systems confer legitimacy on certain language varieties while marginalizing others, structuring patterns of performance disparity, stereotyping, appropriation, and erasure. We then discuss ongoing tensions around what constitutes desirable system behavior, as well as advantages and drawbacks of generative AI tools attempting or refusing to imitate different language varieties. To address the power relations shaping generative AI and the mechanisms identified in our taxonomy--legitimation, stereotyping, appropriation, and erasure--we offer recommendations that emphasize accountability, community agency, control, and ownership. These recommendations recognize linguistic diversity as a resource to be protected, valued, and sustained as part of a just AI future.

## 02-031 | Linguistics Theory Meets LLM: Code-Switched Text Generation via Equivalence Constrained Large Language Models
- arXiv: 2410.22660  first public: 2024-10-30  latest: 2024-10-30  primary cat: cs.CL
- authors (4): Garry Kuwanto; Chaitanya Agarwal; Genta Indra Winata; Derry Tanti Wijaya
- seed subtopic: 语码转换（code-switching）; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Code-switching, the phenomenon of alternating between two or more languages in a single conversation, presents unique challenges for Natural Language Processing (NLP). Most existing research focuses on either syntactic constraints or neural generation, with few efforts to integrate linguistic theory with large language models (LLMs) for generating natural code-switched text. In this paper, we introduce EZSwitch, a novel framework that combines Equivalence Constraint Theory (ECT) with LLMs to produce linguistically valid and fluent code-switched text. We evaluate our method using both human judgments and automatic metrics, demonstrating a significant improvement in the quality of generated code-switching sentences compared to baseline LLMs. To address the lack of suitable evaluation metrics, we conduct a comprehensive correlation study of various automatic metrics against human scores, revealing that current metrics often fail to capture the nuanced fluency of code-switched text. Additionally, we create CSPref, a human preference dataset based on human ratings and analyze model performance across ``hard`` and ``easy`` examples. Our findings indicate that incorporating linguistic constraints into LLMs leads to more robust and human-aligned generation, paving the way for scalable code-switching text generation across diverse language pairs.

## 02-032 | Lost in the Mix: Evaluating LLM Understanding of Code-Switched Text
- arXiv: 2506.14012  first public: 2025-06-16  latest: 2025-06-16  primary cat: cs.CL
- authors (4): Amr Mohamed; Yang Zhang; Michalis Vazirgiannis; Guokan Shang
- seed subtopic: 语码转换（code-switching）; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/amr-mohamedd/Lost-in-the-Mix.git
- pages: 16

ABSTRACT: Code-switching (CSW) is the act of alternating between two or more languages within a single discourse. This phenomenon is widespread in multilingual communities, and increasingly prevalent in online content, where users naturally mix languages in everyday communication. As a result, Large Language Models (LLMs), now central to content processing and generation, are frequently exposed to code-switched inputs. Given their widespread use, it is crucial to understand how LLMs process and reason about such mixed-language text. This paper presents a systematic evaluation of LLM comprehension under code-switching by generating CSW variants of established reasoning and comprehension benchmarks. While degradation is evident when foreign tokens disrupt English text$\unicode{x2013}$even under linguistic constraints$\unicode{x2013}$embedding English into other languages often improves comprehension. Though prompting yields mixed results, fine-tuning offers a more stable path to degradation mitigation.
