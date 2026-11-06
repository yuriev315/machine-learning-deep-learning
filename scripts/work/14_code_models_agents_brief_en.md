# Brief for annotation: 14 代码模型与编程智能体

## 14-001 | mHumanEval -- A Multilingual Benchmark to Evaluate Large Language Models for Code Generation
- arXiv: 2410.15037  first public: 2024-10-19  latest: 2025-01-26  primary cat: cs.CL
- authors (3): Nishat Raihan; Antonios Anastasopoulos; Marcos Zampieri
- seed subtopic: 多自然语言→代码基准; type: 基准与数据集; cross: []
- arXiv comment: 30 Pages
- doi: 10.18653/v1/2025.naacl-long.570
- pages: 30

ABSTRACT: Recent advancements in large language models (LLMs) have significantly enhanced code generation from natural language prompts. The HumanEval Benchmark, developed by OpenAI, remains the most widely used code generation benchmark. However, this and other Code LLM benchmarks face critical limitations, particularly in task diversity, test coverage, and linguistic scope. Current evaluations primarily focus on English-to-Python conversion tasks with limited test cases, potentially overestimating model performance. While recent works have addressed test coverage and programming language (PL) diversity, code generation from low-resource language prompts remains largely unexplored. To address this gap, we introduce mHumanEval, an extended benchmark supporting prompts in over 200 natural languages. We employ established machine translation methods to compile the benchmark, coupled with a quality assurance process. Furthermore, we provide expert human translations for 15 diverse natural languages (NLs). We conclude by analyzing the multilingual code generation capabilities of state-of-the-art (SOTA) Code LLMs, offering insights into the current landscape of cross-lingual code generation.

## 14-002 | HumanEval-XL: A Multilingual Code Generation Benchmark for Cross-lingual Natural Language Generalization
- arXiv: 2402.16694  first public: 2024-02-26  latest: 2024-03-24  primary cat: cs.CL
- authors (3): Qiwei Peng; Yekun Chai; Xuhong Li
- seed subtopic: 多自然语言→代码基准; type: 基准与数据集; cross: []
- arXiv comment: LREC-COLING 2024
- URLs on first pages of PDF: https://github.com/FloatAI/humaneval-xl
- pages: 12

ABSTRACT: Large language models (LLMs) have made significant progress in generating codes from textual prompts. However, existing benchmarks have mainly concentrated on translating English prompts to multilingual codes or have been constrained to very limited natural languages (NLs). These benchmarks have overlooked the vast landscape of massively multilingual NL to multilingual code, leaving a critical gap in the evaluation of multilingual LLMs. In response, we introduce HumanEval-XL, a massively multilingual code generation benchmark specifically crafted to address this deficiency. HumanEval-XL establishes connections between 23 NLs and 12 programming languages (PLs), and comprises of a collection of 22,080 prompts with an average of 8.33 test cases. By ensuring parallel data across multiple NLs and PLs, HumanEval-XL offers a comprehensive evaluation platform for multilingual LLMs, allowing the assessment of the understanding of different NLs. Our work serves as a pioneering step towards filling the void in evaluating NL generalization in the area of multilingual code generation. We make our evaluation code and data publicly available at \url{https://github.com/FloatAI/humaneval-xl}.

## 14-003 | Exploring Multi-Lingual Bias of Large Code Models in Code Generation
- arXiv: 2404.19368  first public: 2024-04-30  latest: 2024-04-30  primary cat: cs.SE
- authors (9): Chaozheng Wang; Zongjie Li; Cuiyun Gao; Wenxuan Wang; Ting Peng; Hailiang Huang ...
- seed subtopic: 提示语言偏差; type: 原始研究; cross: []
- arXiv comment: 12 pages
- pages: 12

ABSTRACT: Code generation aims to synthesize code and fulfill functional requirements based on natural language (NL) specifications, which can greatly improve development efficiency. In the era of large language models (LLMs), large code models (LCMs) have been recently proposed to generate source code. LCMs can generate highly feasible solutions for programming problems described in natural language. Despite the effectiveness, we observe a noticeable multilingual bias in the generation performance of LCMs. Specifically, LCMs demonstrate proficiency in generating solutions when provided with instructions in English, yet may falter when faced with semantically equivalent instructions in other NLs such as Chinese. Moreover, the ability of LCMs to generate code exhibits variety across different programming languages (PLs), such as Python and C++. The observed phenomenon indicates the presence of multi-lingual bias within the generative capabilities of LCMs, which has remained unexplored. In this paper, we aim to investigate the multi-lingual bias that exists in current LCMs. First, we initiate our investigation by constructing the first multi-lingual evaluation benchmark X-HumanEval-X, enabling us to systematically evaluate the extent of multi-lingual bias that exists in current LCMs. In our large-scale experiments on nine popular LCMs, we observe a pronounced multi-lingual bias of LCMs in code generation, including multi-NL and multi-PL bias. Specifically, when using Chinese instructions, the code generation capabilities of LCMs decrease by at least 13% in terms of the Pass@1 metric. Furthermore, LCMs perform variously across different programming languages, e.g., the performance gap between Python and C++ reaches as high as 20.9%. ...

## 14-004 | Bridging the Language Gap: Enhancing Multilingual Prompt-Based Code Generation in LLMs via Zero-Shot Cross-Lingual Transfer
- arXiv: 2408.09701  first public: 2024-08-19  latest: 2025-05-09  primary cat: cs.CL
- authors (3): Mingda Li; Abhijit Mishra; Utkarsh Mujumdar
- seed subtopic: 跨语言迁移改进; type: 原始研究; cross: []
- arXiv comment: Accepted and to appear in IJCNN 2025
- URLs on first pages of PDF: https://github.com/lmd0420/Multilingual https://huggingface.co/datasets/AnonymousDoe/MBPP-Translated
- pages: 9

ABSTRACT: The use of Large Language Models (LLMs) for program code generation has gained substantial attention, but their biases and limitations with non-English prompts challenge global inclusivity. This paper investigates the complexities of multilingual prompt-based code generation. Our evaluations of LLMs, including CODELLAMA and CODEGEMMA, reveal significant disparities in code quality for non-English prompts; we also demonstrate the inadequacy of simple approaches like prompt translation, bootstrapped data augmentation, and fine-tuning. To address this, we propose a zero-shot cross-lingual approach using a neural projection technique, integrating a cross-lingual encoder like LASER to map multilingual embeddings from it into the LLM's token space. This method requires training only on English data and scales effectively to other languages. Results on a translated and quality-checked MBPP dataset show substantial improvements in code quality. This research promotes a more inclusive code generation landscape by empowering LLMs with multilingual capabilities to support the diverse linguistic spectrum in programming.

## 14-005 | IndicEval-XL: Bridging Linguistic Diversity in Code Generation Across Indic Languages
- arXiv: 2502.19067  first public: 2025-02-26  latest: 2025-02-26  primary cat: cs.SE
- authors (5): Ujjwal Singh; Aditi Sharma; Nikhil Gupta; Deepakshi; Vivek Kumar Jha
- seed subtopic: 印度语言→代码基准; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/telekom/IndicEval-XL https://github.com/telekom/IndicEval-XL
- pages: 11

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation from natural language prompts, revolutionizing software development workflows. As we advance towards agent-based development paradigms, these models form the cornerstone of next-generation software development lifecycles. However, current benchmarks for evaluating multilingual code generation capabilities are predominantly English-centric, limiting their applicability across the global developer community. To address this limitation, we present IndicEval-XL, a comprehensive benchmark for code generation that incorporates 6 major Indic languages, collectively spoken by approximately 14\% of the world's population. Our benchmark bridges these languages with 12 programming languages, creating a robust evaluation framework. This work is particularly significant given India's representation of one-eighth of the global population and the crucial role Indic languages play in Indian society. IndicEval-XL represents a significant step toward expanding the linguistic diversity in code generation systems and evaluation frameworks. By developing resources that support multiple languages, we aim to make AI-powered development tools more inclusive and accessible to developers of various linguistic backgrounds. To facilitate further research and development in this direction, we make our dataset and evaluation benchmark publicly available at https://github.com/telekom/IndicEval-XL

## 14-006 | CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts
- arXiv: 2505.05063  first public: 2025-05-08  latest: 2025-05-08  primary cat: cs.LG
- authors (2): Manik Sheokand; Parth Sawant
- seed subtopic: 语码混用提示; type: 基准与数据集; cross: []
- pages: 14

ABSTRACT: Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use code-mixed language while interacting with LLMs. To address this gap, we introduce CodeMixBench, a novel benchmark designed to evaluate the robustness of LLMs on code generation from code-mixed prompts. Built upon BigCodeBench, CodeMixBench introduces controlled code-mixing (CMD) into the natural language parts of prompts across three language pairs: Hinglish (Hindi-English), Spanish-English, and Chinese Pinyin-English. We comprehensively evaluate a diverse set of open-source code generation models ranging from 1.5B to 15B parameters. Our results show that code-mixed prompts consistently degrade Pass@1 performance compared to their English-only counterparts, with performance drops increasing under higher CMD levels for smaller models. CodeMixBench provides a realistic evaluation framework for studying multilingual code generation and highlights new challenges and directions for building robust code generation models that generalize well across diverse linguistic settings.

## 14-007 | Large Language Models for Code Generation from Multilingual Prompts: A Curated Benchmark and a Study on Code Quality
- arXiv: 2607.14816  first public: 2026-07-16  latest: 2026-07-16  primary cat: cs.SE
- authors (8): Saima Afrin; Alessandro Midolo; Camilo Escobar-Velásquez; Mario Linares-Vásquez; Weiyuan Ding; Bowen Xu ...
- seed subtopic: 多自然语言→代码与代码质量; type: 基准与数据集; cross: []
- pages: 34

ABSTRACT: Large Language Models (LLMs) perform differently on identical programming tasks when prompted in different natural languages, a phenomenon known as language bias. While this behavior has been widely studied for general text generation, its impact on code generation quality and programming conventions remains largely unexplored. We investigate how the language used to describe programming tasks affects the source code generated by GPT-4o mini, DeepSeek, and Claude. Our study comprises 460 coding tasks spanning Python (230) and Java (230). We translate and manually curate the original English prompts into Chinese, Hindi, Spanish, and Italian while preserving their technical meaning. We evaluate the generated code using multiple dimensions, including functional correctness through test pass rates, structural quality using established code metrics, issues detected by static analysis tools, and lexical characteristics such as the language used in identifiers and comments. Our results show that (i) English prompts do not consistently produce the best functional correctness or code quality, (ii) the impact of prompt language depends on both the programming language and the LLM, and (iii) generated code frequently mixes English with the prompt language in comments and string literals. These findings provide the first curated multilingual benchmark for studying language bias in code generation and offer insights for developing more robust multilingual code generation systems.

## 14-008 | A Study on the Impact of Natural Language Differences in Prompts on Automatic Code Generation Using LLMs
- arXiv: 2609.18311  first public: 2026-09-16  latest: 2026-09-16  primary cat: cs.SE
- authors (8): Haruka Tokumasu; Masanari Kondo; Alexander Serebrenik; Dong Wang; Kei Koyanagi; Kotaro Noguchi ...
- seed subtopic: 提示语言差异实证; type: 原始研究; cross: []
- arXiv comment: Accepted for publication in Empirical Software Engineering
- pages: 55

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable performance in automatic code generation tasks, thereby encouraging new research in this area. Although numerous studies have explored LLM-based code generation, the impact of the natural language in input prompts remains unexplored (language bias). This study aims to (1) quantify how the natural language of input prompts influences LLM-based code generation performance and (2) evaluate a mitigation strategy to reduce language bias in code generation. We assess code generation Accuracy on AtCoder, LeetCode, and BigCodeBench. To quantify the language bias on code generation, each problem is presented in English, Japanese, and Chinese. We use seven LLMs (GPT-4o, o3-mini, DeepSeek-V3.2, Llama-3, Qwen2.5-Coder-14B, Qwen2.5-Coder-0.5B, and GitHub Copilot) and assess their performance in terms of Accuracy (the number of problems for which generated code passes all test cases). We compare Accuracy before and after translation to evaluate the effectiveness of translation as a mitigation strategy. We observed that the natural language of problem statements affects LLM-based code generation performance. Specifically, the languages officially supported by each dataset achieved the highest median Accuracy. Also, translation improved Accuracy, but its effectiveness was not consistent across datasets and model types. We found that AtCoder contained a particularly high proportion of narrative-style problem statements and longer problem statements. Natural language significantly affects LLM code generation accuracy. Translation can mitigate language bias in some settings, but its effectiveness depends on the dataset and model type. Furthermore, the narrative aspects and context length of input prompts are important factors related to language bias and the effectiveness of translation as a mitigation strategy.

## 14-009 | Evaluating Non-English Developer Support in Machine Learning for Software Engineering
- arXiv: 2605.05902  first public: 2026-05-07  latest: 2026-05-07  primary cat: cs.SE
- authors (8): Jonathan Katzy; Yongcheng Huang; Gopal-Raj Panchu; Maksym Ziemlewski; Paris Loizides; Sander Vermeulen ...
- seed subtopic: 非英语开发者支持评估; type: 原始研究; cross: []
- pages: 59

ABSTRACT: Large Language Models are increasingly used in software engineering, but both code generation and its evaluation remain predominantly English-centric. This leaves a major gap in our understanding of how well current tools support multilingual development, where code contains non-English natural language. In this paper, we investigate non-English code comment generation and the reliability of current methods for evaluating such outputs. We evaluate five code LLMs (CodeGemma, CodeLlama, CodeQwen1.5, GraniteCode, and StarCoder2) across five natural languages: Dutch, English, Greek, Polish and Chinese. We further conduct an open-coding study of 12,500 generated comments, from which we derive a publicly released human-annotated dataset and a taxonomy of 26 error types. We use these human annotations, to evaluate the performance of neural metrics, and LLM-as-a-judge pipelines. Our findings show that generative performance deteriorates substantially outside English, with linguistic errors increasing by up to 15.1$\times$, alongside frequent incoherent generations and a rise in semantic errors. More critically, we show that detecting errors in non-English comments underperforms. Across classical overlap-based metrics, off-the-shelf neural metrics, extended neural metrics using newer multilingual, language-specific, and code-specific models, and LLM-as-a-judge pipelines, no automatic approach provides reliable and consistent assessment. Neural metrics fail to distinguish correct comments from incorrect outputs or even random noise, and tend to overestimate quality in non-English settings. LLM-as-a-judge methods achieve the highest agreement with human annotations but fail to reliably capture important language-related and semantic errors. Overall, our results show that evaluation and generation are key barriers for multilingual tooling, and that human judgment remains indispensable.

## 14-010 | UA-Code-Bench: A Competitive Programming Benchmark for Evaluating LLM Code Generation in Ukrainian
- arXiv: 2511.05040  first public: 2025-11-07  latest: 2025-11-07  primary cat: cs.CL
- authors (2): Mykyta Syromiatnikov; Victoria Ruvinskaya
- seed subtopic: 单一语言代码基准（乌克兰语）; type: 基准与数据集; cross: []
- arXiv comment: 8 pages, 5 figures. XI International conference "Informatics. Culture. Technique." (2025)
- journal_ref: XI International conference "Informatics. Culture. Technique." (2025) 308-314
- doi: 10.15276/ict.02.2025.47
- URLs on first pages of PDF: https://huggingface.co/datasets/NLPForUA/ua-code-bench https://huggingface.co/datasets/NLPForUA/ua-code-bench
- pages: 8

ABSTRACT: Evaluating the real capabilities of large language models in low-resource languages still represents a challenge, as many existing benchmarks focus on widespread tasks translated from English or evaluate only simple language understanding. This paper introduces UA-Code-Bench, a new open-source benchmark established for a thorough evaluation of language models' code generation and competitive programming problem-solving abilities in Ukrainian. The benchmark comprises 500 problems from the Eolymp platform, evenly distributed across five complexity levels from very easy to very hard. A diverse set of 13 leading proprietary and open-source models, generating Python solutions based on a one-shot prompt, was evaluated via the dedicated Eolymp environment against hidden tests, ensuring code correctness. The obtained results reveal that even top-performing models, such as OpenAI o3 and GPT-5, solve only half of the problems, highlighting the challenge of code generation in low-resource natural language. Furthermore, this research presents a comprehensive analysis of performance across various difficulty levels, as well as an assessment of solution uniqueness and computational efficiency, measured by both elapsed time and memory consumption of the generated solutions. In conclusion, this work demonstrates the value of competitive programming benchmarks in evaluating large language models, especially in underrepresented languages. It also paves the way for future research on multilingual code generation and reasoning-enhanced models. The benchmark, data parsing, preparation, code generation, and evaluation scripts are available at https://huggingface.co/datasets/NLPForUA/ua-code-bench.

## 14-011 | RoCode: A Dataset for Measuring Code Intelligence from Problem Definitions in Romanian
- arXiv: 2402.13222  first public: 2024-02-20  latest: 2024-02-20  primary cat: cs.CL
- authors (3): Adrian Cosma; Bogdan Iordache; Paolo Rosso
- seed subtopic: 单一语言代码基准（罗马尼亚语）; type: 基准与数据集; cross: []
- arXiv comment: Accepted at LREC-COLING 2024
- pages: 13

ABSTRACT: Recently, large language models (LLMs) have become increasingly powerful and have become capable of solving a plethora of tasks through proper instructions in natural language. However, the vast majority of testing suites assume that the instructions are written in English, the de facto prompting language. Code intelligence and problem solving still remain a difficult task, even for the most advanced LLMs. Currently, there are no datasets to measure the generalization power for code-generation models in a language other than English. In this work, we present RoCode, a competitive programming dataset, consisting of 2,642 problems written in Romanian, 11k solutions in C, C++ and Python and comprehensive testing suites for each problem. The purpose of RoCode is to provide a benchmark for evaluating the code intelligence of language models trained on Romanian / multilingual text as well as a fine-tuning set for pretrained Romanian models. Through our results and review of related works, we argue for the need to develop code models for languages other than English.

## 14-012 | MERA Code: A Unified Framework for Evaluating Code Generation Across Tasks
- arXiv: 2507.12284  first public: 2025-07-16  latest: 2025-12-01  primary cat: cs.SE
- authors (23): Artem Chervyakov; Alexander Kharitonov; Pavel Zadorozhny; Adamenko Pavel; Rodion Levichev; Dmitrii Vorobev ...
- seed subtopic: 单一语言代码评测框架（俄语）; type: 基准与数据集; cross: []
- pages: 24

ABSTRACT: Advancements in LLMs have enhanced task automation in software engineering; however, current evaluations primarily focus on natural language tasks, overlooking code quality. Most benchmarks prioritize high-level reasoning over executable code and real-world performance, leaving gaps in understanding true capabilities and risks associated with these models in production. To address this issue, we propose MERA Code, a new addition to the MERA benchmark family, specifically focused on evaluating code for the latest code generation LLMs in Russian. This benchmark includes 11 evaluation tasks that span 8 programming languages. Our proposed evaluation methodology features a taxonomy that outlines the practical coding skills necessary for models to complete these tasks. The benchmark comprises an open-source codebase for users to conduct MERA assessments, a scoring system compatible with various programming environments, and a platform featuring a leaderboard and submission system. We evaluate open LLMs and frontier API models, analyzing their limitations in terms of practical coding tasks in non-English languages. We are publicly releasing MERA to guide future research, anticipate groundbreaking features in model development, and standardize evaluation procedures.

## 14-013 | TigerCoder: A Novel Suite of LLMs for Code Generation in Bangla
- arXiv: 2509.09101  first public: 2025-09-11  latest: 2025-09-11  primary cat: cs.CL
- authors (3): Nishat Raihan; Antonios Anastasopoulos; Marcos Zampieri
- seed subtopic: 孟加拉语代码模型; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/mraihan-gmu/
- pages: 17

ABSTRACT: Despite being the 5th most spoken language, Bangla remains underrepresented in Large Language Models (LLMs), particularly for code generation. This primarily stems from the scarcity of high-quality data to pre-train and/or finetune such models. Hence, we introduce the first dedicated family of Code LLMs for Bangla (1B & 9B). We offer three major contributions: (1) a comprehensive Bangla code instruction datasets for programming domain adaptation; (2) MBPP-Bangla, an evaluation benchmark for Bangla code generation; and (3) the TigerCoder-family of Code LLMs, achieving significant ~11-18% performance gains at Pass@1 over existing multilingual and general-purpose Bangla LLMs. Our findings show that curated, high-quality datasets can overcome limitations of smaller models for low-resource languages. We open-source all resources to advance further Bangla LLM research.

## 14-014 | BanglaForge: LLM Collaboration with Self-Refinement for Bangla Code Generation
- arXiv: 2512.19122  first public: 2025-12-22  latest: 2025-12-22  primary cat: cs.SE
- authors (3): Mahir Labib Dihan; Sadif Ahmed; Md Nafiu Rahman
- seed subtopic: 孟加拉语代码生成与自我修复; type: 原始研究; cross: []
- arXiv comment: Accepted at BLP Workshop @ IJCNLP-AACL 2025. Code is available at https://github.com/mahirlabibdihan/BanglaForge
- URLs on first pages of PDF: https://github.com/mahirlabibdihan/ https://noshinulfat.github.io/blp25_code_
- pages: 13

ABSTRACT: Bangla is a low-resource language for code generation, lacking large-scale annotated datasets and tools to transform natural language specifications into executable programs. This makes Bangla-to-code generation a challenging task requiring innovative solutions. To address this, we introduce BanglaForge, a novel framework for generating code from Bangla function descriptions. BanglaForge leverages a retrieval-augmented dual-model collaboration paradigm with self-refinement, combining in-context learning, llm-based translation, systematic prompt engineering, and iterative self-refinement based on execution feedback, where a coder generates initial solutions and a reviewer enhances them for robustness. On the BLP-2025 Bangla Code Generation benchmark, BanglaForge achieves a competitive Pass@1 accuracy of 84.00%, demonstrating the effectiveness of retrieval, model collaboration, and self-refinement for low-resource Bangla code generation.

## 14-015 | PyBangla at BLP-2025 Task 2: Enhancing Bangla-to-Python Code Generation with Iterative Self-Correction and Multilingual Agents
- arXiv: 2512.23713  first public: 2025-11-27  latest: 2025-11-27  primary cat: cs.CL
- authors (3): Jahidul Islam; Md Ataullha; Saiful Azad
- seed subtopic: 孟加拉语共享任务系统; type: 原始研究; cross: []
- arXiv comment: 6 Pages
- pages: 6

ABSTRACT: LLMs excel at code generation from English prompts, but this progress has not extended to low-resource languages. We address Bangla-to-Python code generation by introducing BanglaCodeAct, an agent-based framework that leverages multi-agent prompting and iterative self-correction. Unlike prior approaches relying on task-specific fine-tuning, BanglaCodeAct employs an open-source multilingual LLM within a Thought-Code-Observation loop, enabling dynamic generation, testing, and refinement of code from Bangla instructions. We benchmark several small-parameter open-source LLMs and evaluate their effectiveness on the mHumanEval dataset for Bangla NL2Code. Our results show that Qwen3-8B, when deployed with BanglaCodeAct, achieves the best performance, with pass@1 accuracy of 94.0\% on the development set and 71.6\% on the blind test set. These results establish a new benchmark for Bangla-to-Python translation and highlight the potential of agent-based reasoning for reliable code generation in low-resource languages. Experimental scripts are publicly available at github.com/jahidulzaid/PyBanglaCodeActAgent.

## 14-016 | Retriv at BLP-2025 Task 2: Test-Driven Feedback-Guided Framework for Bangla-to-Python Code Generation
- arXiv: 2511.07382  first public: 2025-11-10  latest: 2025-11-10  primary cat: cs.CL
- authors (3): K M Nafi Asib; Sourav Saha; Mohammed Moshiul Hoque
- seed subtopic: 孟加拉语共享任务系统/测试反馈; type: 原始研究; cross: []
- arXiv comment: 8 pages, 1 figure, experimental scripts publicly available at https://github.com/NafiAsib/Retriv-BLP25-Task-2
- URLs on first pages of PDF: https://github.com/NafiAsib/
- pages: 8

ABSTRACT: Large Language Models (LLMs) have advanced the automated generation of code from natural language prompts. However, low-resource languages (LRLs) like Bangla remain underrepresented due to the limited availability of instruction-to-code datasets and evaluation benchmarks. To address this, the BLP Workshop at IJCNLP-AACL 2025 introduced a shared task on "Code Generation in Bangla". In this work, we propose a method that combines instruction prompting with a test-driven, feedback-guided iterative refinement process using a fine-tuned Qwen2.5-14B model. The model generates code from Bangla instructions, tests it against unit tests, and iteratively refines any failing outputs through three evaluation passes, using test feedback to guide each step. This approach helped our team "Retriv" to secure 2nd place in the shared task with a Pass@1 score of 0.934. The analysis highlights challenges in Bangla instruction understanding and Python code generation, emphasizing the need for targeted methods in LRLs. We made experimental scripts publicly available for the community.

## 14-017 | NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instruction to Python Code Generation
- arXiv: 2511.16787  first public: 2025-11-20  latest: 2025-11-20  primary cat: cs.CL
- authors (6): Hossain Shaikh Saadi; Faria Alam; Mario Sanz-Guerrero; Minh Duc Bui; Manuel Mager; Katharina von der Wense
- seed subtopic: 孟加拉语共享任务系统/多智能体; type: 原始研究; cross: []
- arXiv comment: BLP 2025 Shared Task 2 - Code Generation in Bangla
- URLs on first pages of PDF: https://github.com/shaikhsaadi999/blp25_code_
- pages: 7

ABSTRACT: This paper presents JGU Mainz's winning system for the BLP-2025 Shared Task on Code Generation from Bangla Instructions. We propose a multi-agent-based pipeline. First, a code-generation agent produces an initial solution from the input instruction. The candidate program is then executed against the provided unit tests (pytest-style, assert-based). Only the failing cases are forwarded to a debugger agent, which reruns the tests, extracts error traces, and, conditioning on the error messages, the current program, and the relevant test cases, generates a revised solution. Using this approach, our submission achieved first place in the shared task with a $Pass@1$ score of 95.4. We also make our code public.

## 14-018 | Large Language Models for Multilingual Code Intelligence: A Survey
- arXiv: 2604.25960  first public: 2026-04-27  latest: 2026-04-27  primary cat: cs.SE
- authors (9): Chao Jiang; Dugang Liu; Cheng Wen; Zhiwu Xu; Hua Zheng; Muhammad Sadiq ...
- seed subtopic: 多编程语言代码智能综述（类比）; type: 综述; cross: []
- pages: 12

ABSTRACT: Large language models have transformed AI-assisted software engineering, but current research remains biased toward high-resource languages such as Python, with weaker performance in languages like Rust and OCaml. Since real-world systems are inherently polyglot, robust multilingual code intelligence is crucial. This survey focuses on two key tasks: multilingual code generation from shared natural-language requirements, and multilingual code translation that preserves semantics across languages. It reviews representative methods, benchmarks, and evaluation metrics, and highlights challenges and opportunities for trustworthy cross-language generalization.

## 14-019 | NaturalCodeBench: Examining Coding Performance Mismatch on HumanEval and Natural User Prompts
- arXiv: 2405.04520  first public: 2024-05-07  latest: 2024-05-07  primary cat: cs.CL
- authors (9): Shudan Zhang; Hanlin Zhao; Xiao Liu; Qinkai Zheng; Zehan Qi; Xiaotao Gu ...
- seed subtopic: 真实用户提示基准（中英）; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/THUDM/NaturalCodeBench
- pages: 23

ABSTRACT: Large language models (LLMs) have manifested strong ability to generate codes for productive activities. However, current benchmarks for code synthesis, such as HumanEval, MBPP, and DS-1000, are predominantly oriented towards introductory tasks on algorithm and data science, insufficiently satisfying challenging requirements prevalent in real-world coding. To fill this gap, we propose NaturalCodeBench (NCB), a challenging code benchmark designed to mirror the complexity and variety of scenarios in real coding tasks. NCB comprises 402 high-quality problems in Python and Java, meticulously selected from natural user queries from online coding services, covering 6 different domains. Noting the extraordinary difficulty in creating testing cases for real-world queries, we also introduce a semi-automated pipeline to enhance the efficiency of test case construction. Comparing with manual solutions, it achieves an efficiency increase of more than 4 times. Our systematic experiments on 39 LLMs find that performance gaps on NCB between models with close HumanEval scores could still be significant, indicating a lack of focus on practical code synthesis scenarios or over-specified optimization on HumanEval. On the other hand, even the best-performing GPT-4 is still far from satisfying on NCB. The evaluation toolkit and development set are available at https://github.com/THUDM/NaturalCodeBench.

## 14-020 | Breaking the Programming Language Barrier: Multilingual Prompting to Empower Non-Native English Learners
- arXiv: 2412.12800  first public: 2024-12-17  latest: 2024-12-17  primary cat: cs.CY
- authors (14): James Prather; Brent N. Reeves; Paul Denny; Juho Leinonen; Stephen MacNeil; Andrew Luxton-Reilly ...
- seed subtopic: 非英语母语学习者编程; type: 原始研究; cross: []
- arXiv comment: 10 pages, 3 tables. Accepted for publication at the 27th Australasian Computing Education Conference (ACE 2025)
- pages: 10

ABSTRACT: Non-native English speakers (NNES) face multiple barriers to learning programming. These barriers can be obvious, such as the fact that programming language syntax and instruction are often in English, or more subtle, such as being afraid to ask for help in a classroom full of native English speakers. However, these barriers are frustrating because many NNES students know more about programming than they can articulate in English. Advances in generative AI (GenAI) have the potential to break down these barriers because state of the art models can support interactions in multiple languages. Moreover, recent work has shown that GenAI can be highly accurate at code generation and explanation. In this paper, we provide the first exploration of NNES students prompting in their native languages (Arabic, Chinese, and Portuguese) to generate code to solve programming problems. Our results show that students are able to successfully use their native language to solve programming problems, but not without some difficulty specifying programming terminology and concepts. We discuss the challenges they faced, the implications for practice in the short term, and how this might transform computing education globally in the long term.

## 14-021 | Leveraging LLM Tutoring Systems for Non-Native English Speakers in Introductory CS Courses
- arXiv: 2411.02725  first public: 2024-11-05  latest: 2025-08-21  primary cat: cs.HC
- authors (5): Ismael Villegas Molina; Audria Montalvo; Benjamin Ochoa; Paul Denny; Leo Porter
- seed subtopic: 非英语母语者编程辅导; type: 原始研究; cross: []
- arXiv comment: 11 pages, 5 tables, 4 figures, 2025 ASEE Annual Conference & Exposition
- pages: 11

ABSTRACT: Computer science has historically presented barriers for non-native English speaking (NNES) students, often due to language and terminology challenges. With the rise of large language models (LLMs), there is potential to leverage this technology to support NNES students more effectively. Recent implementations of LLMs as tutors in classrooms have shown promising results. In this study, we deployed an LLM tutor in an accelerated introductory computing course to evaluate its effectiveness specifically for NNES students. Key insights for LLM tutor use are as follows: NNES students signed up for the LLM tutor at a similar rate to native English speakers (NES); NNES students used the system at a lower rate than NES students -- to a small effect; NNES students asked significantly more questions in languages other than English compared to NES students, with many of the questions being multilingual by incorporating English programming keywords. Results for views of the LLM tutor are as follows: both NNES and NES students appreciated the LLM tutor for its accessibility, conversational style, and the guardrails put in place to guide users to answers rather than directly providing solutions; NNES students highlighted its approachability as they did not need to communicate in perfect English; NNES students rated help-seeking preferences of online resources higher than NES students; Many NNES students were unfamiliar with computing terminology in their native languages. These results suggest that LLM tutors can be a valuable resource for NNES students in computing, providing tailored support that enhances their learning experience and overcomes language barriers.

## 14-022 | CodeVaani: A Multilingual, Voice-Based Code Learning Assistant
- arXiv: 2511.20654  first public: 2025-10-08  latest: 2025-10-08  primary cat: cs.HC
- authors (7): Jayant Havare; Srikanth Tamilselvam; Ashish Mittal; Shalaka Thorat; Soham Jadia; Varsha Apte ...
- seed subtopic: 多语言语音编程学习助手; type: 原始研究; cross: []
- pages: 4

ABSTRACT: Programming education often assumes English proficiency and text-based interaction, creating barriers for students from multilingual regions such as India. We present CodeVaani, a multilingual speech-driven assistant for understanding code, built into Bodhitree [1], a Learning Management System developed at IIT Bombay. It is a voice-enabled assistant that helps learners explore programming concepts in their native languages. The system integrates Indic ASR, a codeaware transcription refinement module, and a code model for generating relevant answers. Responses are provided in both text and audio for natural interaction. In a study with 28 beginner programmers, CodeVaani achieved 75% response accuracy, with over 80% of participants rating the experience positively. Compared to classroom assistance, our framework offers ondemand availability, scalability to support many learners, and multilingual support that lowers the entry barrier for students with limited English proficiency. The demo will illustrate these capabilities and highlight how voice-based AI systems can make programming education more inclusive. Supplementary artifacts and demo video are also made available.

## 14-023 | "Write in English, Nobody Understands Your Language Here": A Study of Non-English Trends in Open-Source Repositories
- arXiv: 2602.19446  first public: 2026-02-23  latest: 2026-02-23  primary cat: cs.SE
- authors (3): Masudul Hasan Masud Bhuiyan; Manish Kumar Bala Kumar; Cristian-Alexandru Staicu
- seed subtopic: 开源仓库中的非英语内容; type: 原始研究; cross: []
- doi: 10.1145/3744916.3787766
- URLs on first pages of PDF: https://github.com/dariowouters/ts-fmod-plugin/issues/34
- pages: 13

ABSTRACT: The open-source software (OSS) community has historically been dominated by English as the primary language for code, documentation, and developer interactions. However, with growing global participation and better support for non-Latin scripts through standards like Unicode, OSS is gradually becoming more multilingual. This study investigates the extent to which OSS is becoming more multilingual, analyzing 9.14 billion GitHub issues, pull requests, and discussions, and 62,500 repositories across five programming languages and 30 natural languages, covering the period from 2015 to 2025. We examine six research questions to track changes in language use across communication, code, and documentation. We find that multilingual participation has steadily increased, especially in Korean, Chinese, and Russian. This growth appears not only in issues and discussions but also in code comments, string literals, and documentation files. While this shift reflects greater inclusivity and language diversity in OSS, it also creates language tension. The ability to express oneself in a native language can clash with shared norms around English use, especially in collaborative settings. Non-English or multilingual projects tend to receive less visibility and participation, suggesting that language remains both a resource and a barrier, shaping who gets heard, who contributes, and how open collaboration unfolds.

## 14-024 | A Qualitative Investigation into LLM-Generated Multilingual Code Comments and Automatic Evaluation Metrics
- arXiv: 2505.15469  first public: 2025-05-21  latest: 2025-05-21  primary cat: cs.SE
- authors (8): Jonathan Katzy; Yongcheng Huang; Gopal-Raj Panchu; Maksym Ziemlewski; Paris Loizides; Sander Vermeulen ...
- seed subtopic: 非英语代码注释生成; type: 原始研究; cross: []
- arXiv comment: Accepted PROMISE '25
- URLs on first pages of PDF: https://github.com/oprogramador/most-common-words-by-language
- pages: 10

ABSTRACT: Large Language Models are essential coding assistants, yet their training is predominantly English-centric. In this study, we evaluate the performance of code language models in non-English contexts, identifying challenges in their adoption and integration into multilingual workflows. We conduct an open-coding study to analyze errors in code comments generated by five state-of-the-art code models, CodeGemma, CodeLlama, CodeQwen1.5, GraniteCode, and StarCoder2 across five natural languages: Chinese, Dutch, English, Greek, and Polish. Our study yields a dataset of 12,500 labeled generations, which we publicly release. We then assess the reliability of standard metrics in capturing comment \textit{correctness} across languages and evaluate their trustworthiness as judgment criteria. Through our open-coding investigation, we identified a taxonomy of 26 distinct error categories in model-generated code comments. They highlight variations in language cohesion, informativeness, and syntax adherence across different natural languages. Our analysis shows that, while these models frequently produce partially correct comments, modern neural metrics fail to reliably differentiate meaningful completions from random noise. Notably, the significant score overlap between expert-rated correct and incorrect comments calls into question the effectiveness of these metrics in assessing generated comments.

## 14-025 | Ar-Spider: Text-to-SQL in Arabic
- arXiv: 2402.15012  first public: 2024-02-22  latest: 2024-02-22  primary cat: cs.CL
- authors (4): Saleh Almohaimeed; Saad Almohaimeed; Mansour Al Ghanim; Liqiang Wang
- seed subtopic: 非英语 Text-to-SQL（阿拉伯语）; type: 基准与数据集; cross: []
- arXiv comment: ACM SAC Conference (SAC 24)
- doi: 10.1145/3605098.3636065.
- URLs on first pages of PDF: https://github.com/sasmohaimeed/Ar-Spider
- pages: 7

ABSTRACT: In Natural Language Processing (NLP), one of the most important tasks is text-to-SQL semantic parsing, which focuses on enabling users to interact with the database in a more natural manner. In recent years, text-to-SQL has made significant progress, but most were English-centric. In this paper, we introduce Ar-Spider 1, the first Arabic cross-domain text-to-SQL dataset. Due to the unique nature of the language, two major challenges have been encountered, namely schema linguistic and SQL structural challenges. In order to handle these issues and conduct the experiments, we adopt two baseline models LGESQL [4] and S2SQL [12], both of which are tested with two cross-lingual models to alleviate the effects of schema linguistic and SQL structure linking challenges. The baselines demonstrate decent single-language performance on our Arabic text-to-SQL dataset, Ar-Spider, achieving 62.48% for S2SQL and 65.57% for LGESQL, only 8.79% below the highest results achieved by the baselines when trained in English dataset. To achieve better performance on Arabic text-to-SQL, we propose the context similarity relationship (CSR) approach, which results in a significant increase in the overall performance of about 1.52% for S2SQL and 1.06% for LGESQL and closes the gap between Arabic and English languages to 7.73%.

## 14-026 | AraSpider: Democratizing Arabic-to-SQL
- arXiv: 2402.07448  first public: 2024-02-12  latest: 2024-02-12  primary cat: cs.CL
- authors (3): Ahmed Heakl; Youssef Mohamed; Ahmed B. Zaky
- seed subtopic: 非英语 Text-to-SQL（阿拉伯语）; type: 基准与数据集; cross: []
- arXiv comment: 11 pages, 4 figures
- pages: 11

ABSTRACT: This study presents AraSpider, the first Arabic version of the Spider dataset, aimed at improving natural language processing (NLP) in the Arabic-speaking community. Four multilingual translation models were tested for their effectiveness in translating English to Arabic. Additionally, two models were assessed for their ability to generate SQL queries from Arabic text. The results showed that using back translation significantly improved the performance of both ChatGPT 3.5 and SQLCoder models, which are considered top performers on the Spider dataset. Notably, ChatGPT 3.5 demonstrated high-quality translation, while SQLCoder excelled in text-to-SQL tasks. The study underscores the importance of incorporating contextual schema and employing back translation strategies to enhance model performance in Arabic NLP tasks. Moreover, the provision of detailed methodologies for reproducibility and translation of the dataset into other languages highlights the research's commitment to promoting transparency and collaborative knowledge sharing in the field. Overall, these contributions advance NLP research, empower Arabic-speaking researchers, and enrich the global discourse on language comprehension and database interrogation.

## 14-027 | Dialect2SQL: A Novel Text-to-SQL Dataset for Arabic Dialects with a Focus on Moroccan Darija
- arXiv: 2501.11498  first public: 2025-01-20  latest: 2025-01-20  primary cat: cs.SE
- authors (3): Salmane Chafik; Saad Ezzini; Ismail Berrada
- seed subtopic: 方言 Text-to-SQL（摩洛哥达里贾语）; type: 基准与数据集; cross: []
- journal_ref: [Dialect2SQL: A Novel Text-to-SQL Dataset for Arabic Dialects with a Focus on Moroccan Darija](https://aclanthology.org/2025.wacl-1.10/) (Chafik et al., WACL 2025)
- pages: 7

ABSTRACT: The task of converting natural language questions (NLQs) into executable SQL queries, known as text-to-SQL, has gained significant interest in recent years, as it enables non-technical users to interact with relational databases. Many benchmarks, such as SPIDER and WikiSQL, have contributed to the development of new models and the evaluation of their performance. In addition, other datasets, like SEDE and BIRD, have introduced more challenges and complexities to better map real-world scenarios. However, these datasets primarily focus on high-resource languages such as English and Chinese. In this work, we introduce Dialect2SQL, the first large-scale, cross-domain text-to-SQL dataset in an Arabic dialect. It consists of 9,428 NLQ-SQL pairs across 69 databases in various domains. Along with SQL-related challenges such as long schemas, dirty values, and complex queries, our dataset also incorporates the complexities of the Moroccan dialect, which is known for its diverse source languages, numerous borrowed words, and unique expressions. This demonstrates that our dataset will be a valuable contribution to both the text-to-SQL community and the development of resources for low-resource languages.

## 14-028 | BIRDTurk: Adaptation of the BIRD Text-to-SQL Dataset to Turkish
- arXiv: 2602.03633  first public: 2026-02-03  latest: 2026-02-03  primary cat: cs.CL
- authors (7): Burak Aktaş; Mehmet Can Baytekin; Süha Kağan Köse; Ömer İlbilgi; Elif Özge Yılmaz; Çağrı Toraman ...
- seed subtopic: 非英语 Text-to-SQL（土耳其语）; type: 基准与数据集; cross: []
- arXiv comment: Accepted by EACL 2026 SIGTURK
- URLs on first pages of PDF: https://github.com/metunlp/birdturk
- pages: 17

ABSTRACT: Text-to-SQL systems have achieved strong performance on English benchmarks, yet their behavior in morphologically rich, low-resource languages remains largely unexplored. We introduce BIRDTurk, the first Turkish adaptation of the BIRD benchmark, constructed through a controlled translation pipeline that adapts schema identifiers to Turkish while strictly preserving the logical structure and execution semantics of SQL queries and databases. Translation quality is validated on a sample size determined by the Central Limit Theorem to ensure 95% confidence, achieving 98.15% accuracy on human-evaluated samples. Using BIRDTurk, we evaluate inference-based prompting, agentic multi-stage reasoning, and supervised fine-tuning. Our results reveal that Turkish introduces consistent performance degradation, driven by both structural linguistic divergence and underrepresentation in LLM pretraining, while agentic reasoning demonstrates stronger cross-lingual robustness. Supervised fine-tuning remains challenging for standard multilingual baselines but scales effectively with modern instruction-tuned models. BIRDTurk provides a controlled testbed for cross-lingual Text-to-SQL evaluation under realistic database conditions. We release the training and development splits to support future research.

## 14-029 | IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages
- arXiv: 2604.13686  first public: 2026-04-15  latest: 2026-04-15  primary cat: cs.CL
- authors (4): Aviral Dawar; Roshan Karanth; Vikram Goyal; Dhruv Kumar
- seed subtopic: 多语言 Text-to-SQL（印度语言）; type: 基准与数据集; cross: []
- arXiv comment: Under Review
- pages: 25

ABSTRACT: While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced from open-data platforms, including the National Data and Analytics Platform (NDAP) and the India Data Portal (IDP), ensuring realistic administrative data complexity. IndicDB comprises 20 databases across 237 tables. To convert denormalized government data into rich relational structures, we employ an iterative three-agent framework (Architect, Auditor, Refiner) to ensure structural rigor and high relational density (11.85 tables per database; join depths up to six). Our pipeline is value-aware, difficulty-calibrated, and join-enforced, generating 15,617 tasks across English, Hindi, and five Indic languages. We evaluate cross-lingual semantic parsing performance of state-of-the-art models (DeepSeek v3.2, MiniMax 2.7, LLaMA 3.3, Qwen3) across seven linguistic variants. Results show a 9.00% performance drop from English to Indic languages, revealing an "Indic Gap" driven by harder schema linking, increased structural ambiguity, and limited external knowledge. IndicDB serves as a rigorous benchmark for multilingual Text-to-SQL. Code and data: https://anonymous.4open.science/r/multilingualText2Sql-Indic--DDCC/

## 14-030 | Multilingual Text-to-SQL: Benchmarking the Limits of Language Models with Collaborative Language Agents
- arXiv: 2509.24405  first public: 2025-09-29  latest: 2025-09-29  primary cat: cs.CL
- authors (5): Khanh Trinh Pham; Thu Huong Nguyen; Jun Jo; Quoc Viet Hung Nguyen; Thanh Tam Nguyen
- seed subtopic: 多语言 Text-to-SQL 与语言智能体; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/phkhanhtrinh23/Multilingual_Text_to_SQL
- pages: 8

ABSTRACT: Text-to-SQL enables natural access to databases, yet most benchmarks are English-only, limiting multilingual progress. We introduce MultiSpider 2.0, extending Spider 2.0 to eight languages (English, German, French, Spanish, Portuguese, Japanese, Chinese, Vietnamese). It preserves Spider 2.0's structural difficulty while adding linguistic and dialectal variability, demanding deeper reasoning for complex SQL. On this benchmark, state-of-the-art LLMs (such as DeepSeek-R1 and OpenAI o1) reach only 4\% execution accuracy when relying on intrinsic reasoning, versus 60\% on MultiSpider 1.0. Therefore, we provide a collaboration-driven language agents baseline that iteratively refines queries, improving accuracy to 15\%. These results reveal a substantial multilingual gap and motivate methods that are robust across languages and ready for real-world enterprise deployment. Our benchmark is available at https://github.com/phkhanhtrinh23/Multilingual_Text_to_SQL.

## 14-031 | Bridging the Semantic Gap: Contrastive Rewards for Multilingual Text-to-SQL with GRPO
- arXiv: 2510.13827  first public: 2025-10-10  latest: 2025-11-21  primary cat: cs.CL
- authors (6): Ashish Kattamuri; Ishita Prasad; Meetu Malhotra; Arpita Vats; Rahul Raja; Albert Lie
- seed subtopic: 多语言 Text-to-SQL 强化学习; type: 原始研究; cross: []
- arXiv comment: 20th International Workshop on Semantic and Social Media Adaptation & Personalization
- pages: 7

ABSTRACT: Current Text-to-SQL methods are evaluated and only focused on executable queries, overlooking the semantic alignment challenge -- both in terms of the semantic meaning of the query and the correctness of the execution results. Even execution accuracy itself shows significant drops when moving from English to other languages, with an average decline of 6 percentage points across non-English languages. We address these challenges by presenting a new framework that combines Group Relative Policy Optimization (GRPO) within a multilingual contrastive reward signal to enhance both task efficiency and semantic accuracy in Text-to-SQL systems in cross-lingual scenarios. Our method teaches models to obtain better correspondence between SQL generation and user intent by combining a reward signal based on semantic similarity. On the seven-language MultiSpider dataset, fine-tuning the LLaMA-3-3B model with GRPO improved the execution accuracy up to 87.4 percent (+26 pp over zero-shot) and semantic accuracy up to 52.29 percent (+32.86 pp). Adding our contrastive reward signal in the GRPO framework further improved the average semantic accuracy to 59.14 percent (+6.85 pp, up to +10 pp for Vietnamese). Our experiments showcase that a smaller, parameter-efficient 3B LLaMA model fine-tuned with our contrastive reward signal outperforms a much larger zero-shot 8B LLaMA model, with an uplift of 7.43 pp in execution accuracy (from 81.43 percent on the 8B model to 88.86 percent on the 3B model), and nearly matches its semantic accuracy (59.14 percent vs. 68.57 percent) -- all using just 3,000 reinforcement learning training examples. These results demonstrate how we can improve the performance of Text-to-SQL systems with contrastive rewards for directed semantic alignment, without requiring large-scale training datasets.

## 14-032 | Prompt Engineering Techniques for Context-dependent Text-to-SQL in Arabic
- arXiv: 2511.20677  first public: 2025-11-16  latest: 2025-11-16  primary cat: cs.CL
- authors (5): Saleh Almohaimeed; May Alsofyani; Saad Almohaimeed; Mansour Al Ghanim; Liqiang Wang
- seed subtopic: 多轮上下文 Text-to-SQL（阿拉伯语）; type: 原始研究; cross: []
- arXiv comment: Accepted at IJCNN 2025 (to appear in IEEE/IJCNN proceedings). This arXiv submission corresponds to the camera-ready version
- pages: 9

ABSTRACT: In recent years, the task of cross-domain, context-dependent text-to-SQL has received significant attention. Enables users with no prior knowledge of SQL to have a conversation with databases using natural language. However, most of the available datasets and research have been conducted in English, along with some work in Chinese. To this date, no effort has been made to address this task in the Arabic language. In this paper, we introduce Ar-SParC, the first Arabic cross-domain, context-dependent text-to-SQL dataset. The dataset consists of 3,450 sequences of interrelated questions, each sequence containing an average of approximately three questions, which results in a total of 10225 questions along with their corresponding SQL queries. We conducted 40 experiments on the Ar-SParC dataset using two large language models, GPT-3.5-turbo and GPT-4.5-turbo, applying 10 different prompt engineering techniques, including four question representation methods and six in-context learning techniques. Furthermore, we developed a novel approach named GAT corrector, which enhanced the performance across all 40 experiments, yielding an average improvement of 1.9% in execution accuracy (EX) and 1.9% in interaction accuracy (IX) under zero-shot settings, and an average increase of 1.72% EX and 0.92% IX under in-context learning settings. Finally, we conducted an ablation study with two more experiments to explain why the GAT corrector outperformed the previous GAT verifier technique, particularly for the Arabic language.

## 14-033 | A Survey on LLM-based Code Generation for Low-Resource and Domain-Specific Programming Languages
- arXiv: 2410.03981  first public: 2024-10-04  latest: 2025-09-26  primary cat: cs.SE
- authors (3): Sathvik Joel; Jie JW Wu; Fatemeh H. Fard
- seed subtopic: 低资源编程语言（类比）; type: 综述; cross: []
- arXiv comment: 64 pages, 3 figures, 15 tables. Accepted in ACM Transactions on Software Engineering and Methodology (TOSEM)
- URLs on first pages of PDF: https://github.com/jie-jw-wu/Survey-CodeLLM4LowResource-DSL https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard
- pages: 64

ABSTRACT: Large Language Models (LLMs) have shown impressive capabilities in code generation for popular programming languages. However, their performance on Low-Resource Programming Languages (LRPLs) and Domain-Specific Languages (DSLs) remains a significant challenge, affecting millions of developers-3.5 million users in Rust alone-who cannot fully utilize LLM capabilities. LRPLs and DSLs encounter unique obstacles, including data scarcity and, for DSLs, specialized syntax that is poorly represented in general-purpose datasets. Addressing these challenges is crucial, as LRPLs and DSLs enhance development efficiency in specialized domains, such as finance and science. While several surveys discuss LLMs in software engineering, none focus specifically on the challenges and opportunities associated with LRPLs and DSLs. Our survey fills this gap by systematically reviewing the current state, methodologies, and challenges in leveraging LLMs for code generation in these languages. We filtered 111 papers from over 27,000 published studies between 2020 and 2024 to evaluate the capabilities and limitations of LLMs in LRPLs and DSLs. We report the LLMs used, benchmarks, and metrics for evaluation, strategies for enhancing performance, and methods for dataset collection and curation. We identified four main evaluation techniques and several metrics for assessing code generation in LRPLs and DSLs. Our analysis categorizes improvement methods into six groups and summarizes novel architectures proposed by researchers. Despite various techniques and metrics, a standard approach and benchmark dataset for evaluating code generation in LRPLs and DSLs are lacking. This survey serves as a resource for researchers and practitioners at the intersection of LLMs, software engineering, and specialized programming languages, laying the groundwork for future advancements in code generation for LRPLs and DSLs.

## 14-034 | Bridge-Coder: Unlocking LLMs' Potential to Overcome Language Gaps in Low-Resource Code
- arXiv: 2410.18957  first public: 2024-10-24  latest: 2024-10-24  primary cat: cs.CL
- authors (8): Jipeng Zhang; Jianshu Zhang; Yuanzhe Li; Renjie Pi; Rui Pan; Runtao Liu ...
- seed subtopic: 低资源编程语言（类比）; type: 原始研究; cross: []
- arXiv comment: 15 pages, 3 figures
- URLs on first pages of PDF: https://github.com/2003pro/bridgecoder
- pages: 18

ABSTRACT: Large Language Models (LLMs) demonstrate strong proficiency in generating code for high-resource programming languages (HRPLs) like Python but struggle significantly with low-resource programming languages (LRPLs) such as Racket or D. This performance gap deepens the digital divide, preventing developers using LRPLs from benefiting equally from LLM advancements and reinforcing disparities in innovation within underrepresented programming communities. While generating additional training data for LRPLs is promising, it faces two key challenges: manual annotation is labor-intensive and costly, and LLM-generated LRPL code is often of subpar quality. The underlying cause of this issue is the gap between natural language to programming language gap (NL-PL Gap), which is especially pronounced in LRPLs due to limited aligned data. In this work, we introduce a novel approach called Bridge-Coder, which leverages LLMs' intrinsic capabilities to enhance the performance on LRPLs. Our method consists of two key stages. Bridge Generation, where we create high-quality dataset by utilizing LLMs' general knowledge understanding, proficiency in HRPLs, and in-context learning abilities. Then, we apply the Bridged Alignment, which progressively improves the alignment between NL instructions and LRPLs. Experimental results across multiple LRPLs show that Bridge-Coder significantly enhances model performance, demonstrating the effectiveness and generalization of our approach. Furthermore, we offer a detailed analysis of the key components of our method, providing valuable insights for future work aimed at addressing the challenges associated with LRPLs.

## 14-035 | StarCoder 2 and The Stack v2: The Next Generation
- arXiv: 2402.19173  first public: 2024-02-29  latest: 2024-02-29  primary cat: cs.SE
- authors (66): Anton Lozhkov; Raymond Li; Loubna Ben Allal; Federico Cassano; Joel Lamy-Poirier; Nouamane Tazi ...
- seed subtopic: 代码模型技术报告; type: 技术报告; cross: []
- pages: 61

ABSTRACT: The BigCode project, an open-scientific collaboration focused on the responsible development of Large Language Models for Code (Code LLMs), introduces StarCoder2. In partnership with Software Heritage (SWH), we build The Stack v2 on top of the digital commons of their source code archive. Alongside the SWH repositories spanning 619 programming languages, we carefully select other high-quality data sources, such as GitHub pull requests, Kaggle notebooks, and code documentation. This results in a training set that is 4x larger than the first StarCoder dataset. We train StarCoder2 models with 3B, 7B, and 15B parameters on 3.3 to 4.3 trillion tokens and thoroughly evaluate them on a comprehensive set of Code LLM benchmarks. We find that our small model, StarCoder2-3B, outperforms other Code LLMs of similar size on most benchmarks, and also outperforms StarCoderBase-15B. Our large model, StarCoder2- 15B, significantly outperforms other models of comparable size. In addition, it matches or outperforms CodeLlama-34B, a model more than twice its size. Although DeepSeekCoder- 33B is the best-performing model at code completion for high-resource languages, we find that StarCoder2-15B outperforms it on math and code reasoning benchmarks, as well as several low-resource languages. We make the model weights available under an OpenRAIL license and ensure full transparency regarding the training data by releasing the SoftWare Heritage persistent IDentifiers (SWHIDs) of the source code data.

## 14-036 | Qwen2.5-Coder Technical Report
- arXiv: 2409.12186  first public: 2024-09-18  latest: 2024-11-12  primary cat: cs.CL
- authors (24): Binyuan Hui; Jian Yang; Zeyu Cui; Jiaxi Yang; Dayiheng Liu; Lei Zhang ...
- seed subtopic: 代码模型技术报告; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen2.5-Coder
- pages: 32

ABSTRACT: In this report, we introduce the Qwen2.5-Coder series, a significant upgrade from its predecessor, CodeQwen1.5. This series includes six models: Qwen2.5-Coder-(0.5B/1.5B/3B/7B/14B/32B). As a code-specific model, Qwen2.5-Coder is built upon the Qwen2.5 architecture and continues pretrained on a vast corpus of over 5.5 trillion tokens. Through meticulous data cleaning, scalable synthetic data generation, and balanced data mixing, Qwen2.5-Coder demonstrates impressive code generation capabilities while retaining general and math skills. These models have been evaluated on a wide range of code-related tasks, achieving state-of-the-art (SOTA) performance across more than 10 benchmarks, including code generation, completion, reasoning, and repair, consistently outperforming larger models of the same model size. We believe that the release of the Qwen2.5-Coder series will advance research in code intelligence and, with its permissive licensing, support wider adoption by developers in real-world applications.

## 14-037 | DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence
- arXiv: 2401.14196  first public: 2024-01-25  latest: 2024-01-26  primary cat: cs.SE
- authors (13): Daya Guo; Qihao Zhu; Dejian Yang; Zhenda Xie; Kai Dong; Wentao Zhang ...
- seed subtopic: 代码模型技术报告; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/deepseek-ai/DeepSeek-Coder
- pages: 23

ABSTRACT: The rapid development of large language models has revolutionized code intelligence in software development. However, the predominance of closed-source models has restricted extensive research and development. To address this, we introduce the DeepSeek-Coder series, a range of open-source code models with sizes from 1.3B to 33B, trained from scratch on 2 trillion tokens. These models are pre-trained on a high-quality project-level code corpus and employ a fill-in-the-blank task with a 16K window to enhance code generation and infilling. Our extensive evaluations demonstrate that DeepSeek-Coder not only achieves state-of-the-art performance among open-source code models across multiple benchmarks but also surpasses existing closed-source models like Codex and GPT-3.5. Furthermore, DeepSeek-Coder models are under a permissive license that allows for both research and unrestricted commercial use.

## 14-038 | OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models
- arXiv: 2411.04905  first public: 2024-11-07  latest: 2025-03-20  primary cat: cs.CL
- authors (19): Siming Huang; Tianhao Cheng; J. K. Liu; Jiaran Hao; Liuyihan Song; Yang Xu ...
- seed subtopic: 代码模型技术报告; type: 技术报告; cross: []
- pages: 35

ABSTRACT: Large language models (LLMs) for code have become indispensable in various domains, including code generation, reasoning tasks and agent systems. While open-access code LLMs are increasingly approaching the performance levels of proprietary models, high-quality code LLMs suitable for rigorous scientific investigation, particularly those with reproducible data processing pipelines and transparent training protocols, remain limited. The scarcity is due to various challenges, including resource constraints, ethical considerations, and the competitive advantages of keeping models advanced. To address the gap, we introduce OpenCoder, a top-tier code LLM that not only achieves performance comparable to leading models but also serves as an "open cookbook" for the research community. Unlike most prior efforts, we release not only model weights and inference code, but also the reproducible training data, complete data processing pipeline, rigorous experimental ablation results, and detailed training protocols for open scientific research. Through this comprehensive release, we identify the key ingredients for building a top-tier code LLM: (1) code optimized heuristic rules for data cleaning and methods for data deduplication, (2) recall of text corpus related to code and (3) high-quality synthetic data in both annealing and supervised fine-tuning stages. By offering this level of openness, we aim to broaden access to all aspects of a top-tier code LLM, with OpenCoder serving as both a powerful model and an open foundation to accelerate research, and enable reproducible advancements in code AI.

## 14-039 | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- arXiv: 2405.15793  first public: 2024-05-06  latest: 2024-11-11  primary cat: cs.SE
- authors (7): John Yang; Carlos E. Jimenez; Alexander Wettig; Kilian Lieret; Shunyu Yao; Karthik Narasimhan ...
- seed subtopic: 编程智能体; type: 原始研究; cross: []
- arXiv comment: Code, data, and demo available at https://swe-agent.com
- pages: 118

ABSTRACT: Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.

## 14-040 | OpenHands: An Open Platform for AI Software Developers as Generalist Agents
- arXiv: 2407.16741  first public: 2024-07-23  latest: 2025-04-18  primary cat: cs.SE
- authors (24): Xingyao Wang; Boxuan Li; Yufan Song; Frank F. Xu; Xiangru Tang; Mingchen Zhuge ...
- seed subtopic: 编程智能体平台; type: 原始研究; cross: []
- arXiv comment: Accepted by ICLR 2025; Code: https://github.com/All-Hands-AI/OpenHands
- URLs on first pages of PDF: https://github.com/All-Hands-AI/OpenHands
- pages: 38

ABSTRACT: Software is one of the most powerful tools that we humans have at our disposal; it allows a skilled programmer to interact with the world in complex and profound ways. At the same time, thanks to improvements in large language models (LLMs), there has also been a rapid development in AI agents that interact with and affect change in their surrounding environments. In this paper, we introduce OpenHands (f.k.a. OpenDevin), a platform for the development of powerful and flexible AI agents that interact with the world in similar ways to those of a human developer: by writing code, interacting with a command line, and browsing the web. We describe how the platform allows for the implementation of new agents, safe interaction with sandboxed environments for code execution, coordination between multiple agents, and incorporation of evaluation benchmarks. Based on our currently incorporated benchmarks, we perform an evaluation of agents over 15 challenging tasks, including software engineering (e.g., SWE-BENCH) and web browsing (e.g., WEBARENA), among others. Released under the permissive MIT license, OpenHands is a community project spanning academia and industry with more than 2.1K contributions from over 188 contributors.

## 14-041 | Agentless: Demystifying LLM-based Software Engineering Agents
- arXiv: 2407.01489  first public: 2024-07-01  latest: 2024-10-29  primary cat: cs.SE
- authors (4): Chunqiu Steven Xia; Yinlin Deng; Soren Dunn; Lingming Zhang
- seed subtopic: 编程智能体（简化流程）; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/OpenAutoCoder/Agentless
- pages: 25

ABSTRACT: Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity of these agent-based approaches, together with the limited abilities of current LLMs, raises the following question: Do we really have to employ complex autonomous software agents? To attempt to answer this question, we build Agentless -- an agentless approach to automatically solve software development problems. Compared to the verbose and complex setup of agent-based approaches, Agentless employs a simplistic three-phase process of localization, repair, and patch validation, without letting the LLM decide future actions or operate with complex tools. Our results on the popular SWE-bench Lite benchmark show that surprisingly the simplistic Agentless is able to achieve both the highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents! Furthermore, we manually classified the problems in SWE-bench Lite and found problems with exact ground truth patch or insufficient/misleading issue descriptions. As such, we construct SWE-bench Lite-S by excluding such problematic issues to perform more rigorous evaluation and comparison. Our work highlights the current overlooked potential of a simple, interpretable technique in autonomous software development. We hope Agentless will help reset the baseline, starting point, and horizon for autonomous software agents, and inspire future work along this crucial direction.

## 14-042 | Executable Code Actions Elicit Better LLM Agents
- arXiv: 2402.01030  first public: 2024-02-01  latest: 2024-06-07  primary cat: cs.CL
- authors (7): Xingyao Wang; Yangyi Chen; Lifan Yuan; Yizhe Zhang; Yunzhu Li; Hao Peng ...
- seed subtopic: 代码即动作; type: 原始研究; cross: []
- arXiv comment: Accepted by ICML 2024; Code, data, model, and demo are available at https://github.com/xingyaoww/code-act
- pages: 25

ABSTRACT: Large Language Model (LLM) agents, capable of performing a broad range of actions, such as invoking tools and controlling robots, show great potential in tackling real-world challenges. LLM agents are typically prompted to produce actions by generating JSON or text in a pre-defined format, which is usually limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools). This work proposes to use executable Python code to consolidate LLM agents' actions into a unified action space (CodeAct). Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions. Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate). The encouraging performance of CodeAct motivates us to build an open-source LLM agent that interacts with environments by executing interpretable code and collaborates with users using natural language. To this end, we collect an instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn interactions using CodeAct. We show that it can be used with existing data to improve models in agent-oriented tasks without compromising their general capability. CodeActAgent, finetuned from Llama2 and Mistral, is integrated with Python interpreter and uniquely tailored to perform sophisticated tasks (e.g., model training) using existing libraries and autonomously self-debug.

## 14-043 | Training Software Engineering Agents and Verifiers with SWE-Gym
- arXiv: 2412.21139  first public: 2024-12-30  latest: 2025-06-06  primary cat: cs.SE
- authors (7): Jiayi Pan; Xingyao Wang; Graham Neubig; Navdeep Jaitly; Heng Ji; Alane Suhr ...
- seed subtopic: 智能体训练环境; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2025. Code at https://github.com/SWE-Gym/SWE-Gym
- pages: 21

ABSTRACT: We present SWE-Gym, the first environment for training real-world software engineering (SWE) agents. SWE-Gym contains 2,438 real-world Python task instances, each comprising a codebase with an executable runtime environment, unit tests, and a task specified in natural language. We use SWE-Gym to train language model based SWE agents, achieving up to 19% absolute gains in resolve rate on the popular SWE-Bench Verified and Lite test sets. We also experiment with inference-time scaling through verifiers trained on agent trajectories sampled from SWE-Gym. When combined with our fine-tuned SWE agents, we achieve 32.0% and 26.0% on SWE-Bench Verified and Lite, respectively, reflecting a new state-of-the-art for open-weight SWE agents. To facilitate further research, we publicly release SWE-Gym, models, and agent trajectories.

## 14-044 | Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving
- arXiv: 2504.02605  first public: 2025-04-03  latest: 2025-04-03  primary cat: cs.SE
- authors (19): Daoguang Zan; Zhirong Huang; Wei Liu; Hanwu Chen; Linhao Zhang; Shulin Xin ...
- seed subtopic: 多编程语言智能体基准; type: 基准与数据集; cross: []
- pages: 32

ABSTRACT: The task of issue resolving is to modify a codebase to generate a patch that addresses a given issue. However, existing benchmarks, such as SWE-bench, focus almost exclusively on Python, making them insufficient for evaluating Large Language Models (LLMs) across diverse software ecosystems. To address this, we introduce a multilingual issue-resolving benchmark, called Multi-SWE-bench, covering Java, TypeScript, JavaScript, Go, Rust, C, and C++. It includes a total of 1,632 high-quality instances, which were carefully annotated from 2,456 candidates by 68 expert annotators, ensuring that the benchmark can provide an accurate and reliable evaluation. Based on Multi-SWE-bench, we evaluate a series of state-of-the-art models using three representative methods (Agentless, SWE-agent, and OpenHands) and present a comprehensive analysis with key empirical insights. In addition, we launch a Multi-SWE-RL open-source community, aimed at building large-scale reinforcement learning (RL) training datasets for issue-resolving tasks. As an initial contribution, we release a set of 4,723 well-structured instances spanning seven programming languages, laying a solid foundation for RL research in this domain. More importantly, we open-source our entire data production pipeline, along with detailed tutorials, encouraging the open-source community to continuously contribute and expand the dataset. We envision our Multi-SWE-bench and the ever-growing Multi-SWE-RL community as catalysts for advancing RL toward its full potential, bringing us one step closer to the dawn of AGI.

## 14-045 | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code
- arXiv: 2403.07974  first public: 2024-03-12  latest: 2024-06-06  primary cat: cs.SE
- authors (10): Naman Jain; King Han; Alex Gu; Wen-Ding Li; Fanjia Yan; Tianjun Zhang ...
- seed subtopic: 评测与污染控制; type: 基准与数据集; cross: []
- arXiv comment: Website - https://livecodebench.github.io/
- pages: 46

ABSTRACT: Large Language Models (LLMs) applied to code-related applications have emerged as a prominent field, attracting significant interest from both academia and industry. However, as new and improved LLMs are developed, existing evaluation benchmarks (e.g., HumanEval, MBPP) are no longer sufficient for assessing their capabilities. In this work, we propose LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces. Notably, our benchmark also focuses on a broader range of code related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation. Currently, LiveCodeBench hosts four hundred high-quality coding problems that were published between May 2023 and May 2024. We have evaluated 18 base LLMs and 34 instruction-tuned LLMs on LiveCodeBench. We present empirical findings on contamination, holistic performance comparisons, potential overfitting in existing benchmarks as well as individual model comparisons. We will release all prompts and model completions for further community analysis, along with a general toolkit for adding new scenarios and model

## 14-046 | Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step
- arXiv: 2402.16906  first public: 2024-02-25  latest: 2024-06-06  primary cat: cs.SE
- authors (3): Li Zhong; Zilong Wang; Jingbo Shang
- seed subtopic: 测试反馈与自我修复; type: 原始研究; cross: []
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/FloridSleeves/LLMDebugger
- pages: 20

ABSTRACT: Large language models (LLMs) are leading significant progress in code generation. Beyond one-pass code generation, recent works further integrate unit tests and program verifiers into LLMs to iteratively refine the generated programs. However, these works consider the generated programs as an indivisible entity, which falls short for LLMs in debugging the programs, especially when the programs contain complex logic flows and data operations. In contrast, when human developers debug programs, they typically set breakpoints and selectively examine runtime execution information. The execution flow and the intermediate variables play a crucial role in the debugging process, yet they are underutilized in the existing literature on code generation. In this study, we introduce Large Language Model Debugger (LDB), a novel debugging framework that enables LLMs to refine their generated programs with the runtime execution information. Specifically, LDB segments the programs into basic blocks and tracks the values of intermediate variables after each block throughout the runtime execution. This allows LLMs to concentrate on simpler code units within the overall execution flow, verify their correctness against the task description block by block, and efficiently pinpoint any potential errors. Experiments demonstrate that LDB consistently enhances the baseline performance by up to 9.8% across the HumanEval, MBPP, and TransCoder benchmarks, archiving new state-of-the-art performance in code debugging for various LLM selections.

## 14-047 | RepoAgent: An LLM-Powered Open-Source Framework for Repository-level Code Documentation Generation
- arXiv: 2402.16667  first public: 2024-02-26  latest: 2024-02-26  primary cat: cs.CL
- authors (13): Qinyu Luo; Yining Ye; Shihao Liang; Zhong Zhang; Yujia Qin; Yaxi Lu ...
- seed subtopic: 仓库级文档生成; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/davidhalter/jedi
- pages: 30

ABSTRACT: Generative models have demonstrated considerable potential in software engineering, particularly in tasks such as code generation and debugging. However, their utilization in the domain of code documentation generation remains underexplored. To this end, we introduce RepoAgent, a large language model powered open-source framework aimed at proactively generating, maintaining, and updating code documentation. Through both qualitative and quantitative evaluations, we have validated the effectiveness of our approach, showing that RepoAgent excels in generating high-quality repository-level documentation. The code and results are publicly accessible at https://github.com/OpenBMB/RepoAgent.

## 14-048 | CodeRAG-Bench: Can Retrieval Augment Code Generation?
- arXiv: 2406.14497  first public: 2024-06-20  latest: 2025-02-26  primary cat: cs.SE
- authors (7): Zora Zhiruo Wang; Akari Asai; Xinyan Velocity Yu; Frank F. Xu; Yiqing Xie; Graham Neubig ...
- seed subtopic: 检索增强代码生成; type: 基准与数据集; cross: []
- pages: 16

ABSTRACT: While language models (LMs) have proven remarkably adept at generating code, many programs are challenging for LMs to generate using their parametric knowledge alone. Providing external contexts such as library documentation can facilitate generating accurate and functional code. Despite the success of retrieval-augmented generation (RAG) in various text-oriented tasks, its potential for improving code generation remains under-explored. In this work, we conduct a systematic, large-scale analysis by asking: in what scenarios can retrieval benefit code generation models? and what challenges remain? We first curate a comprehensive evaluation benchmark, CodeRAG-Bench, encompassing three categories of code generation tasks, including basic programming, open-domain, and repository-level problems. We aggregate documents from five sources for models to retrieve contexts: competition solutions, online tutorials, library documentation, StackOverflow posts, and GitHub repositories. We examine top-performing models on CodeRAG-Bench by providing contexts retrieved from one or multiple sources. While notable gains are made in final code generation by retrieving high-quality contexts across various settings, our analysis reveals room for improvement -- current retrievers still struggle to fetch useful contexts especially with limited lexical overlap, and generators fail to improve with limited context lengths or abilities to integrate additional contexts. We hope CodeRAG-Bench serves as an effective testbed to encourage further development of advanced code-oriented RAG methods.

## 14-049 | Copilot Evaluation Harness: Evaluating LLM-Guided Software Programming
- arXiv: 2402.14261  first public: 2024-02-22  latest: 2024-02-22  primary cat: cs.SE
- authors (9): Anisha Agarwal; Aaron Chan; Shubham Chandel; Jinu Jang; Shaun Miller; Roshanak Zilouchian Moghaddam ...
- seed subtopic: IDE 集成评测; type: 原始研究; cross: []
- pages: 14

ABSTRACT: The integration of Large Language Models (LLMs) into Development Environments (IDEs) has become a focal point in modern software development. LLMs such as OpenAI GPT-3.5/4 and Code Llama offer the potential to significantly augment developer productivity by serving as intelligent, chat-driven programming assistants. However, utilizing LLMs out of the box is unlikely to be optimal for any given scenario. Rather, each system requires the LLM to be honed to its set of heuristics to ensure the best performance. In this paper, we introduce the Copilot evaluation harness: a set of data and tools for evaluating LLM-guided IDE interactions, covering various programming scenarios and languages. We propose our metrics as a more robust and information-dense evaluation than previous state of the art evaluation systems. We design and compute both static and execution based success metrics for scenarios encompassing a wide range of developer tasks, including code generation from natural language (generate), documentation generation from code (doc), test case generation (test), bug-fixing (fix), and workspace understanding and query resolution (workspace). These success metrics are designed to evaluate the performance of LLMs within a given IDE and its respective parameter space. Our learnings from evaluating three common LLMs using these metrics can inform the development and validation of future scenarios in LLM guided IDEs.

## 14-050 | Multi-Programming Language Sandbox for LLMs
- arXiv: 2410.23074  first public: 2024-10-30  latest: 2024-11-05  primary cat: cs.SE
- authors (28): Shihan Dou; Jiazheng Zhang; Jianxiang Zang; Yunbo Tao; Weikang Zhou; Haoxiang Jia ...
- seed subtopic: 执行隔离/沙箱; type: 原始研究; cross: []
- arXiv comment: 25 pages, 14 figures
- pages: 25

ABSTRACT: We introduce MPLSandbox, an out-of-the-box multi-programming language sandbox designed to provide unified and comprehensive feedback from compiler and analysis tools for Large Language Models (LLMs). It can automatically identify the programming language of the code, compiling and executing it within an isolated sub-sandbox to ensure safety and stability. In addition, MPLSandbox also integrates both traditional and LLM-based code analysis tools, providing a comprehensive analysis of generated code. MPLSandbox can be effortlessly integrated into the training and deployment of LLMs to improve the quality and correctness of their generated code. It also helps researchers streamline their workflows for various LLM-based code-related tasks, reducing the development cost. To validate the effectiveness of MPLSandbox, we integrate it into training and deployment approaches, and also employ it to optimize workflows for a wide range of real-world code-related tasks. Our goal is to enhance researcher productivity on LLM-based code-related tasks by simplifying and automating workflows through delegation to MPLSandbox.

## 14-051 | A Survey on Large Language Models for Code Generation
- arXiv: 2406.00515  first public: 2024-06-01  latest: 2024-11-10  primary cat: cs.CL
- authors (5): Juyong Jiang; Fan Wang; Jiasi Shen; Sungju Kim; Sunghun Kim
- seed subtopic: 综述; type: 综述; cross: []
- doi: 10.1145/3747588
- URLs on first pages of PDF: https://github.com/features/copilot https://github.com/juyongjiang/CodeLLMSurvey
- pages: 70

ABSTRACT: Large Language Models (LLMs) have garnered remarkable advancements across diverse code-related tasks, known as Code LLMs, particularly in code generation that generates source code with LLM from natural language descriptions. This burgeoning field has captured significant interest from both academic researchers and industry professionals due to its practical significance in software development, e.g., GitHub Copilot. Despite the active exploration of LLMs for a variety of code tasks, either from the perspective of natural language processing (NLP) or software engineering (SE) or both, there is a noticeable absence of a comprehensive and up-to-date literature review dedicated to LLM for code generation. In this survey, we aim to bridge this gap by providing a systematic literature review that serves as a valuable reference for researchers investigating the cutting-edge progress in LLMs for code generation. We introduce a taxonomy to categorize and discuss the recent developments in LLMs for code generation, covering aspects such as data curation, latest advances, performance evaluation, ethical implications, environmental impact, and real-world applications. In addition, we present a historical overview of the evolution of LLMs for code generation and offer an empirical comparison using the HumanEval, MBPP, and BigCodeBench benchmarks across various levels of difficulty and types of programming tasks to highlight the progressive enhancements in LLM capabilities for code generation. We identify critical challenges and promising opportunities regarding the gap between academia and practical development. Furthermore, we have established a dedicated resource GitHub page (https://github.com/juyongjiang/CodeLLMSurvey) to continuously document and disseminate the most recent advances in the field.

## 14-052 | Large Language Model-Based Agents for Software Engineering: A Survey
- arXiv: 2409.02977  first public: 2024-09-04  latest: 2025-12-03  primary cat: cs.SE
- authors (7): Junwei Liu; Kaixin Wang; Yixuan Chen; Xin Peng; Zhenpeng Chen; Lingming Zhang ...
- seed subtopic: 综述; type: 综述; cross: []
- arXiv comment: Accepted by TOSEM
- URLs on first pages of PDF: https://github.com/FudanSELab/Agent4SE-Paper-List
- pages: 57

ABSTRACT: The recent advance in Large Language Models (LLMs) has shaped a new paradigm of AI agents, i.e., LLM-based agents. Compared to standalone LLMs, LLM-based agents substantially extend the versatility and expertise of LLMs by enhancing LLMs with the capabilities of perceiving and utilizing external resources and tools. To date, LLM-based agents have been applied and shown remarkable effectiveness in Software Engineering (SE). The synergy between multiple agents and human interaction brings further promise in tackling complex real-world SE problems. In this work, we present a comprehensive and systematic survey on LLM-based agents for SE. We collect 124 papers and categorize them from two perspectives, i.e., the SE and agent perspectives. In addition, we discuss open challenges and future directions in this critical domain. The repository of this survey is at https://github.com/FudanSELab/Agent4SE-Paper-List.

## 14-053 | Evaluating Large Language Models Trained on Code
- arXiv: 2107.03374  first public: 2021-07-07  latest: 2021-07-14  primary cat: cs.LG
- authors (58): Mark Chen; Jerry Tworek; Heewoo Jun; Qiming Yuan; Henrique Ponde de Oliveira Pinto; Jared Kaplan ...
- seed subtopic: 经典：Codex/HumanEval; type: 原始研究; cross: []
- arXiv comment: corrected typos, added references, added authors, added acknowledgements
- pages: 35

ABSTRACT: We introduce Codex, a GPT language model fine-tuned on publicly available code from GitHub, and study its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot. On HumanEval, a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings, our model solves 28.8% of the problems, while GPT-3 solves 0% and GPT-J solves 11.4%. Furthermore, we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method, we solve 70.2% of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations, including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally, we discuss the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics.

## 14-054 | MCoNaLa: A Benchmark for Code Generation from Multiple Natural Languages
- arXiv: 2203.08388  first public: 2022-03-16  latest: 2023-02-07  primary cat: cs.CL
- authors (5): Zhiruo Wang; Grace Cuenca; Shuyan Zhou; Frank F. Xu; Graham Neubig
- seed subtopic: 经典：多自然语言→代码; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/zorazrw/
- pages: 9

ABSTRACT: While there has been a recent burgeoning of applications at the intersection of natural and programming languages, such as code generation and code summarization, these applications are usually English-centric. This creates a barrier for program developers who are not proficient in English. To mitigate this gap in technology development across languages, we propose a multilingual dataset, MCoNaLa, to benchmark code generation from natural language commands extending beyond English. Modeled off of the methodology from the English Code/Natural Language Challenge (CoNaLa) dataset, we annotated a total of 896 NL-code pairs in three languages: Spanish, Japanese, and Russian. We present a quantitative evaluation of performance on the MCoNaLa dataset by testing with state-of-the-art code generation systems. While the difficulties vary across these three languages, all systems lag significantly behind their English counterparts, revealing the challenges in adapting code generation to new languages.

## 14-055 | Execution-Based Evaluation for Open-Domain Code Generation
- arXiv: 2212.10481  first public: 2022-12-20  latest: 2023-05-19  primary cat: cs.SE
- authors (4): Zhiruo Wang; Shuyan Zhou; Daniel Fried; Graham Neubig
- seed subtopic: 经典：多自然语言执行评测; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/zorazrw/odex
- pages: 19

ABSTRACT: To extend the scope of coding queries to more realistic settings, we propose ODEX, the first Open-Domain EXecution-based natural language (NL) to Python code generation dataset. ODEX has 945 NL-Code pairs spanning 79 diverse libraries, along with 1,707 human-written test cases for execution. Our NL-Code pairs are harvested from StackOverflow forums to encourage natural and practical coding queries. Moreover, ODEX supports four natural languages as intents, in English, Spanish, Japanese, and Russian. ODEX unveils intriguing behavioral differences among top-performing code language models (LM). While CODEX achieves better overall results, CODEGEN improves effectively via scaling -- CODEGEN 6.1B performs comparably with CODEX 12B. Both models show substantial gaps between open and closed domains, but CODEGEN gaps tend to decrease with model size while CODEX gaps increase. We release ODEX to facilitate research into open-domain problems for the code generation community.

## 14-056 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- arXiv: 2310.06770  first public: 2023-10-10  latest: 2024-11-11  primary cat: cs.CL
- authors (7): Carlos E. Jimenez; John Yang; Alexander Wettig; Shunyu Yao; Kexin Pei; Ofir Press ...
- seed subtopic: 经典：仓库级智能体基准; type: 基准与数据集; cross: []
- arXiv comment: Data, code, and leaderboard are available at https://www.swebench.com ICLR 2024, https://openreview.net/forum?id=VTF8yNQM66
- pages: 52

ABSTRACT: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of $2,294$ software engineering problems drawn from real GitHub issues and corresponding pull requests across $12$ popular Python repositories. Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks. Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model SWE-Llama can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere $1.96$% of the issues. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous.

## 14-057 | MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation
- arXiv: 2208.08227  first public: 2022-08-17  latest: 2022-12-19  primary cat: cs.LG
- authors (13): Federico Cassano; John Gouwar; Daniel Nguyen; Sydney Nguyen; Luna Phipps-Costin; Donald Pinckney ...
- seed subtopic: 经典：多编程语言基准; type: 基准与数据集; cross: []
- URLs on first pages of PDF: https://github.com/features/copilot/
- pages: 37

ABSTRACT: Large language models have demonstrated the ability to generate both natural language and programming language text. Such models open up the possibility of multi-language code generation: could code generation models generalize knowledge from one language to another? Although contemporary code generation models can generate semantically correct Python code, little is known about their abilities with other languages. We propose MultiPL-E, a system for translating unit test-driven code generation benchmarks to new languages. We create the first massively multilingual code generation benchmark by using MultiPL-E to translate two popular Python code generation benchmarks to 18 additional programming languages. We use MultiPL-E to extend the HumanEval benchmark and MBPP benchmark to 18 languages that encompass a range of programming paradigms and popularity. Using these new parallel benchmarks, we evaluate the multi-language performance of three state-of-the-art code generation models: Codex, CodeGen, and InCoder. We find that Codex matches or even exceeds its performance on Python for several other languages. The range of programming languages represented in MultiPL-E allow us to explore the impact of language frequency and language features on model performance. Finally, the MultiPL-E approach of compiling code generation benchmarks to new programming languages is both scalable and extensible, making it straightforward to evaluate new models, benchmarks, and languages.

## 14-071 | IFEvalCode: Controlled Code Generation
- arXiv: 2507.22462  first public: 2025-07-30  latest: 2026-10-10  primary cat: cs.CL
- authors (12): Jian Yang; Wei Zhang; Shukai Liu; Linzheng Chai; Yingshui Tan; Jiaheng Liu ...
- seed subtopic: 中英双语受控代码生成; type: 基准与数据集; cross: []
- pages: 18

ABSTRACT: Code large language models (Code LLMs) have made significant progress in code generation by translating natural language descriptions into functional code; however, real-world applications often demand stricter adherence to detailed requirements such as coding style, line count, and structural constraints, beyond mere correctness. To address this, the paper introduces forward and backward constraints generation to improve the instruction-following capabilities of Code LLMs in controlled code generation, ensuring outputs align more closely with human-defined guidelines. The authors further present IFEvalCode, a multilingual benchmark comprising 1.6K test samples across seven programming languages (Python, Java, JavaScript, TypeScript, Shell, C++, and C#), with each sample featuring both Chinese and English queries. Unlike existing benchmarks, IFEvalCode decouples evaluation into two metrics: correctness (Corr.) and instruction-following (Instr.), enabling a more nuanced assessment. Experiments on over 40 LLMs reveal that closed-source models outperform open-source ones in controllable code generation and highlight a significant gap between the models' ability to generate correct code versus code that precisely follows instructions.

## 14-072 | CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics
- arXiv: 2512.21877  first public: 2025-12-26  latest: 2026-04-11  primary cat: cs.CL
- authors (10): Parth Agarwal; Navya Kommuri; Trizal Garg; Prisha Singhal; Dhruv Shah; Vaibhav Devraj ...
- seed subtopic: 多语言 Text-to-SQL（印地语/旁遮普语/泰卢固语）; type: 基准与数据集; cross: []
- arXiv comment: Under Review
- pages: 15

ABSTRACT: Cricket is the second most popular sport worldwide, with billions of fans seeking advanced statistical insights unavailable through standard web searches. Although LLMs have advanced significantly in Text-to-SQL tasks, their capability to handle domain-specific nuances and multilingual requirements in sports analytics remains under-explored. We present CricBench, a benchmark suite evaluating the intrinsic SQL generation abilities of LLMs on cricket data across four formats: Test, ODI, T20I, and IPL. We curate a Gold-Standard dataset of 2,654 evaluation instances across four languages (English, Hindi, Punjabi, and Telugu). We evaluate seven models, GPT-5 Mini, Claude Sonnet 4, DeepSeek R1 and V3, Qwen 235B, Llama 3.1, and Gemma 2, using schema-only prompting. No single model dominates across all formats: GPT-5 Mini leads on Test cricket (12.4% DMA), Qwen 235B leads on IPL (28.7%) and T20I (17.5%), and all models score 0% on hard ODI queries. All models show a stark disconnect between syntactic validity (>98% execution accuracy) and semantic correctness (<29% DMA), with a domain gap of 37-55 percentage points versus BIRD. To our knowledge, CricBench is the first Text-to-SQL benchmark for cricket analytics.

## 14-073 | Multi-sourced AI Tutor for Non-Native English Speaker Students
- arXiv: 2610.22163  first public: 2026-10-15  latest: 2026-10-15  primary cat: cs.AI
- authors (5): Yiyin Shen; Xinyi Ai; Weibing Wang; Rogers Jeffrey Leo John; Meenakshi Syamkumar
- seed subtopic: 非英语母语者编程课程助教; type: 原始研究; cross: []
- pages: 7

ABSTRACT: Large language models (LLMs) are increasingly being adopted as teaching tools in computing education, particularly for developing AI tutors capable of answering student questions. With the rise in enrollment of international students in computing programs, researchers have begun to explore the difficulties that non-native English speaker (NNES) students face in computing courses due to language barriers. To aid such students, we developed a general-purpose AI tutor system that can process student questions in foreign languages (currently focused on Mandarin) and provide bilingual responses. Our system also incorporates the functionality of generating a glossary of technical terms and their explanations to enhance comprehension. Our approach utilizes a specialized Retrieval-Augmented Generation (RAG) pipeline with a novel question extraction mechanism, enabling us to effectively utilize a diverse array of course materials for answering student queries. We evaluated our AI tutor using 91 Piazza posts, demonstrating that it could answer 83.52% of the posts correctly and in a helpful manner. The tutor also provided high-quality translations for 76.92% of the questions and generated technical term glossaries for 64.47% of them. Our findings underscore the potential of multi-source RAG pipeline in enhancing AI tutor systems, offering support for non-native speakers that are challenging to provide with traditional supporting staff of a computing course.
