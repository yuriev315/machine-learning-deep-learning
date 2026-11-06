# 应用开发学习与设计指南（路线 B：现有模型 + 本地知识库 + 检索与工具）

本指南把三条应用路线分开整理：对话助手、知识库问答、编程助手。每条路线都区分两类内容：
- 模型能力：模型本身在目标语言上能做到什么，靠评测证明。
- 产品工程：检索、记忆、界面、隔离、监控等系统设计，靠工程实现与用户研究证明。

论文中的部署案例多为作者自报，场景、语言与用户群体各不相同，不能直接推广。

## 路线 1：对话助手

### 模型能力层
- 先用 evaluation_cn.md 的方法确认三点：
  - 基座在目标语言上的流畅度、事实性与安全性；
  - 对方言、罗马化书写、语码混合输入的鲁棒性；
  - 文化适切性。
- 罗马化与本文字差距：[LRL-P-13-002｜Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Rom](../papers/2025_Khullar_ScriptGap_en.pdf)Script Gap，印度语言医疗分诊。
- 跨语言临床正确性漂移：[LRL-P-13-032｜Safety That Does Not Transfer: Cross-Lingual Clinical Correctness Drif](../papers/2026_Gabriel_SafetyThatDoesNotTransfer_en.pdf)，豪萨语与英语。
- 语码转换与方言：
  - [LRL-P-13-038｜BanglAssist: A Bengali-English Generative AI Chatbot for Code-Switchin](../papers/2025_Kruk_BanglAssist_en.pdf)BanglAssist。
  - [LRL-P-02-032｜Lost in the Mix: Evaluating LLM Understanding of Code-Switched Text](../papers/2025_Mohamed_LostInTheMix_en.pdf)LLM 对语码转换文本的理解。

### 产品工程层
- 真实场景部署与用户研究：
  - [LRL-P-13-001｜ASHABot: An LLM-Powered Chatbot to Support the Informational Needs of](../papers/2024_Ramjee_ASHABot_en.pdf)ASHABot：社区卫生工作者，印地语，含语音。
  - [LRL-P-13-021｜Farmer.Chat: Scaling AI-Powered Agricultural Services for Smallholder](../papers/2024_Singh_FarmerChat_en.pdf)Farmer.Chat：农业服务，多种非洲及印度语言。
  - [LRL-P-13-006｜System X: A Mobile Voice-Based AI System for EMR Generation and Clinic](../papers/2025_Mustafa_SystemX_en.pdf)乌尔都语语音电子病历系统。
  - [LRL-P-13-041｜KumbhDoot: A Scale-Ready, LLM-Bounded Architecture for Mass-Gathering](../papers/2026_Sakalkar_KumbhDoot_en.pdf)KumbhDoot：大型集会公共服务。
- 文化与用户需求：
  - [LRL-P-13-003｜"Koyi Sawaal Nahi Hai": Reimagining Maternal Health Chatbots for Colle](../papers/2025_Hameed_KoyiSawaalNahiHai_en.pdf)重新设想孕产健康聊天机器人。
  - [LRL-P-13-054｜Designing Around Stigma: Human-Centered LLMs for Menstrual Health](../papers/2026_Shahnawaz_DesigningAroundStigma_en.pdf)面向月经健康的以人为本设计。
- 教育：
  - [LRL-P-13-045｜AFRILANGTUTOR: Advancing Language Tutoring and Culture Education in Lo](../papers/2026_Belay_AFRILANGTUTOR_en.pdf)AFRILANGTUTOR。
  - [LRL-P-13-044｜The Impact of Large Language Models on K-12 Education in Rural India:](../papers/2025_Goyal_ImpactLargeLanguageModels_en.pdf)印度农村 K-12 教育中的 LLM（通用支撑）。
- 客服与任务型对话：
  - [LRL-P-13-040｜Telenor Nordics Customer Service self-help corpus](../papers/2026_Riess_TelenorNordicsCustomerService_en.pdf)Telenor 北欧客服语料。
  - [LRL-P-13-052｜Task-Oriented Dialog Systems for the Senegalese Wolof Language](../papers/2024_Mbaye_TaskOrientedDialogSystems_en.pdf)沃洛夫语任务型对话。
  - [LRL-P-13-059｜Multi3WOZ: A Multilingual, Multi-Domain, Multi-Parallel Dataset for Tr](../papers/2023_Hu_Multi3WOZ_en.pdf)Multi3WOZ。
- 工程实现：
  - [LRL-E-32｜open-webui](../reference_code/open-webui_f7ac7ee_original_en.tar.gz)Open WebUI：对话前端，注意其许可证附加品牌条款。
  - [LRL-E-27｜smolagents](../reference_code/smolagents_12c1bc8_original_en.tar.gz)smolagents。

库内缺口：
- 政务、客服的真实部署论文较少。
- “会话记忆”在多语言场景下的专门研究较少。

## 路线 2：知识库问答（多语言 RAG）

### 模型能力层：嵌入、检索与生成
- 多语言嵌入：
  - [LRL-P-12-005｜M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity](../papers/2024_Chen_M3Embedding_en.pdf)M3-Embedding。
  - [LRL-P-12-004｜Multilingual E5 Text Embeddings: A Technical Report](../papers/2024_Wang_MultilingualE5TextEmbeddings_en.pdf)Multilingual E5。
  - [LRL-P-12-006｜mGTE: Generalized Long-Context Text Representation and Reranking Model](../papers/2024_Zhang_MGTE_en.pdf)mGTE。
  - [LRL-P-12-010｜Qwen3 Embedding: Advancing Text Embedding and Reranking Through Founda](../papers/2025_Zhang_Qwen3Embedding_en.pdf)Qwen3 Embedding。
  - 评测基准：[LRL-P-12-014｜MMTEB: Massive Multilingual Text Embedding Benchmark](../papers/2025_Enevoldsen_MMTEB_en.pdf)MMTEB。
- 跨语言检索与重排序：
  - [LRL-P-12-021｜Zero-Shot Cross-Lingual Reranking with Large Language Models for Low-R](../papers/2023_Adeyemi_ZeroShotCrossLingualReranking_en.pdf)面向低资源语言的零样本跨语言重排序。
  - [LRL-P-12-024｜What are the limits of cross-lingual dense passage retrieval for low-r](../papers/2024_Wu_WhatLimitsCrossLingualDense_en.pdf)跨语言稠密检索在低资源语言上的极限。
  - [LRL-P-12-026｜Bridging Language Gaps: Advances in Cross-Lingual Information Retrieva](../papers/2025_Goworek_BridgingLanguageGaps_en.pdf)。
- 多语言 RAG 行为：
  - [LRL-P-12-029｜Retrieval-augmented generation in multilingual settings](../papers/2024_Chirkova_RetrievalAugmentedGeneration_en.pdf)多语言设置下的 RAG。
  - [LRL-P-12-031｜Investigating Language Preference of Multilingual RAG Systems](../papers/2025_Park_InvestigatingLanguagePreference_en.pdf)语言偏好。
  - [LRL-P-12-037｜On the Consistency of Multilingual Context Utilization in Retrieval-Au](../papers/2025_Qi_ConsistencyMultilingualContext_en.pdf)上下文利用一致性。
  - [LRL-P-12-039｜The Cross-Lingual Cost: Retrieval Biases in RAG over Arabic-English Co](../papers/2025_Amiraz_TheCrossLingualCost_en.pdf)阿拉伯语—英语检索偏差。
  - [LRL-P-12-027｜The Multilingual Curse at the Retrieval Layer: Evidence from Amharic](../papers/2026_Alemneh_MultilingualCurseRetrieval_en.pdf)阿姆哈拉语检索层的“多语言诅咒”。
- 不知道时承认不知道：[LRL-P-12-028｜"Knowing When You Don't Know": A Multilingual Relevance Assessment Dat](../papers/2023_Thakur_KnowingWhenYouDonTKnowMultilingual_en.pdf)NoMIRACL。

### 产品工程层：解析、更新、引用与核验
- 文档解析：
  - [LRL-P-12-051｜MDPBench: A Benchmark for Multilingual Document Parsing in Real-World](../papers/2026_Li_MDPBench_en.pdf)MDPBench 多语言文档解析。
  - 工程：[LRL-E-26｜docling](../reference_code/docling_a857fd2_original_en.tar.gz)docling。
  - OCR 相关见 data_pipeline_cn.md 第 4 节。
- 知识更新与编辑：
  - [LRL-P-12-057｜Editing Across Languages: A Survey of Multilingual Knowledge Editing](../papers/2025_Durrani_EditingAcrossLanguages_en.pdf)多语言知识编辑综述。
  - [LRL-P-12-058｜Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Kno](../papers/2025_Wu_EditOnceUpdateEverywhere_en.pdf)跨语言知识同步。
- 引用与事实核验：
  - [LRL-P-12-059｜SemEval-2025 Task 7: Multilingual and Crosslingual Fact-Checked Claim](../papers/2025_Peng_SemEval2025Task7_en.pdf)多语言事实核查声明检索。
  - [LRL-P-12-060｜AfrIFact: Cultural Information Retrieval, Evidence Extraction and Fact](../papers/2026_Azime_AfrIFact_en.pdf)AfrIFact。
  - [LRL-P-12-062｜Poly-FEVER: A Multilingual Fact Verification Benchmark for Hallucinati](../papers/2025_Zhang_PolyFEVER_en.pdf)Poly-FEVER。
- 领域案例：
  - [LRL-P-13-037｜Cloud and On-Premises Deployment of Uzbek Legal RAG via Targeted Retri](../papers/2026_Danielyan_CloudPremisesDeploymentUzbek_en.pdf)乌兹别克语法律 RAG，云端与本地部署。
  - [LRL-P-13-034｜MizanQA: Benchmarking Large Language Models on Moroccan Legal Question](../papers/2025_Bahaj_MizanQA_en.pdf)摩洛哥法律问答。
  - [LRL-P-13-035｜VLQA: The First Comprehensive, Large, and High-Quality Vietnamese Data](../papers/2025_Nguyen_VLQA_en.pdf)越南语法律数据集。
- 工程实现：
  - [LRL-E-23｜sentence-transformers](../reference_code/sentence-transformers_0b6937d_original_en.tar.gz)sentence-transformers。
  - [LRL-E-24｜FlagEmbedding](../reference_code/FlagEmbedding_fd1a2bd_original_en.tar.gz)FlagEmbedding。
  - [LRL-E-25｜haystack](../reference_code/haystack_7f0ab62_original_en.tar.gz)Haystack。

## 路线 3：编程助手与编程智能体（用小语种提出编程需求）

### 模型能力层
- 非英语需求的代码生成：
  - [LRL-P-14-001｜mHumanEval -- A Multilingual Benchmark to Evaluate Large Language Mode](../papers/2024_Raihan_MHumanEvalMultilingualBenchmark_en.pdf)mHumanEval。
  - [LRL-P-14-002｜HumanEval-XL: A Multilingual Code Generation Benchmark for Cross-lingu](../papers/2024_Peng_HumanEvalXL_en.pdf)HumanEval-XL。
  - [LRL-P-14-004｜Bridging the Language Gap: Enhancing Multilingual Prompt-Based Code Ge](../papers/2024_Li_BridgingTheLanguageGap_en.pdf)。
  - [LRL-P-14-020｜Breaking the Programming Language Barrier: Multilingual Prompting to E](../papers/2024_Prather_BreakingProgrammingLanguage_en.pdf)多语言提示帮助非英语母语的编程者。
- 单一语言案例：
  - [LRL-P-14-013｜TigerCoder: A Novel Suite of LLMs for Code Generation in Bangla](../papers/2025_Raihan_TigerCoder_en.pdf)TigerCoder（孟加拉语）。
  - BLP-2025 孟加拉语到 Python 共享任务：
    - [LRL-P-14-015｜PyBangla at BLP-2025 Task 2: Enhancing Bangla-to-Python Code Generatio](../papers/2025_Islam_PyBanglaBLP2025Task2Enhancing_en.pdf)。
    - [LRL-P-14-016｜Retriv at BLP-2025 Task 2: Test-Driven Feedback-Guided Framework for B](../papers/2025_Asib_RetrivBLP2025Task2TestDriven_en.pdf)测试驱动反馈。
    - [LRL-P-14-017｜NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instr](../papers/2025_Saadi_NALAMAINZBLP2025Task2Multi_en.pdf)多智能体。
- 非英语开发者与注释：
  - [LRL-P-14-023｜"Write in English, Nobody Understands Your Language Here": A Study of](../papers/2026_Bhuiyan_WriteEnglishNobodyUnderstands_en.pdf)“用英语写，这里没人懂你的语言”。
  - [LRL-P-14-024｜A Qualitative Investigation into LLM-Generated Multilingual Code Comme](../papers/2025_Katzy_QualitativeInvestigation_en.pdf)多语言代码注释。
  - [LRL-P-14-009｜Evaluating Non-English Developer Support in Machine Learning for Softw](../papers/2026_Katzy_EvaluatingNonEnglishDeveloper_en.pdf)。
- 自然语言到 SQL：
  - [LRL-P-14-025｜Ar-Spider: Text-to-SQL in Arabic](../papers/2024_Almohaimeed_ArSpider_en.pdf)Ar-Spider。
  - [LRL-P-14-027｜Dialect2SQL: A Novel Text-to-SQL Dataset for Arabic Dialects with a Fo](../papers/2025_Chafik_Dialect2SQL_en.pdf)Dialect2SQL。
  - [LRL-P-14-030｜Multilingual Text-to-SQL: Benchmarking the Limits of Language Models w](../papers/2025_Pham_MultilingualTextToSQL_en.pdf)。

### 产品工程层：仓库检索、测试反馈、IDE、执行隔离
- 智能体框架与接口（通用支撑）：
  - [LRL-P-14-039｜SWE-agent: Agent-Computer Interfaces Enable Automated Software Enginee](../papers/2024_Yang_SWEAgent_en.pdf)SWE-agent。
  - [LRL-P-14-040｜OpenHands: An Open Platform for AI Software Developers as Generalist A](../papers/2024_Wang_OpenHands_en.pdf)OpenHands。
  - [LRL-P-14-041｜Agentless: Demystifying LLM-based Software Engineering Agents](../papers/2024_Xia_Agentless_en.pdf)Agentless。
  - [LRL-P-14-042｜Executable Code Actions Elicit Better LLM Agents](../papers/2024_Wang_ExecutableCodeActionsElicit_en.pdf)可执行代码动作。
- 仓库文档与测评：
  - [LRL-P-14-047｜RepoAgent: An LLM-Powered Open-Source Framework for Repository-level C](../papers/2024_Luo_RepoAgent_en.pdf)RepoAgent。
  - [LRL-P-14-049｜Copilot Evaluation Harness: Evaluating LLM-Guided Software Programming](../papers/2024_Agarwal_CopilotEvaluationHarness_en.pdf)Copilot 评测框架。
- 执行隔离：[LRL-P-14-050｜Multi-Programming Language Sandbox for LLMs](../papers/2024_Dou_MultiProgrammingLanguage_en.pdf)多编程语言沙箱。
- 工程实现：
  - [LRL-E-33｜continue](../reference_code/continue_b238c1f_original_en.tar.gz)Continue（IDE 扩展）。
  - [LRL-E-34｜OpenHands-software-agent-sdk](../reference_code/OpenHands-software-agent-sdk_ccae18c_original_en.tar.gz)OpenHands software-agent-sdk。
  - [LRL-E-35｜aider](../reference_code/aider_253f036_original_en.tar.gz)aider。

注意：
- 目前的通用编程智能体研究基本以英语需求为主。
- 用小语种需求驱动智能体，要单独评测两层能力：
  - 需求理解：可用目标语言版本的任务描述；
  - 端到端任务完成。

## 工具调用（三条路线共用）

- [LRL-P-11-051｜Lost in Execution: On the Multilingual Robustness of Tool Calling in L](../papers/2026_Luo_LostInExecution_en.pdf)Lost in Execution。
- [LRL-P-11-054｜Tool Calling for Arabic LLMs: Data Strategies and Instruction Tuning](../papers/2025_Ersoy_ToolCallingArabicLLMsData_en.pdf)阿拉伯语工具调用。
- [LRL-P-11-055｜Teaching a Language Model to Speak the Language of Tools](../papers/2025_Emanuilov_TeachingLanguageModelSpeak_en.pdf)保加利亚语工具语言。
- [LRL-P-03-074｜Agaram 2.5B: The First Tamil-First Language Model Trained from Scratch](../papers/2026_Kumaresan_Agaram25B_en.pdf)Agaram：泰米尔语优先、含工具调用的从零训练模型。

## 推荐学习顺序

1. 课程：
   - [LRL-C-17-004｜Large Language Model Agents](../university_materials/Berkeley_CS294-196_LLMAgents_2024Fall_LectureMaterials_en)Berkeley LLM Agents。
   - [LRL-C-17-009｜Large Language Model Applications](../university_materials/CMU_11-766_LLMApplications_2026Spring_LectureMaterials_en)CMU 11-766 LLM 应用。
   - [LRL-C-17-048｜Text Technologies for Data Science](../university_materials/Edinburgh_TTDS_2024-25_LectureMaterials_en)Edinburgh TTDS（检索基础）。
2. 书：
   - [LRL-B-18-044｜Search Engines: Information Retrieval in Practice](../books/Croft_SearchEnginesIRInPractice_2015_en.pdf)Search Engines。
   - [LRL-B-18-045｜Foundations of Vector Retrieval](../books/Bruch_FoundationsOfVectorRetrieval_2024_en.pdf)Foundations of Vector Retrieval。
   - [LRL-B-18-048｜Agentic Large Language Models](../books/vanDuijn_AgenticLargeLanguageModels_2026_en.pdf)Agentic Large Language Models。
