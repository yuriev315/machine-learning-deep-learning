# 基础先修路线：数学、深度学习、NLP、语言学与多语言学习

本路线按“教材打底 → 课程串讲 → 论文接到前沿”组织。课程与书的先修要求、难度、学期或版本，见 `catalog_cn.csv` 的“先修要求”“难度或阶段”“学期或书籍版本”列。

阶段分档：
- 入门：本科低年级可读。
- 进阶：需要前一阶段基础。
- 高阶：研究方向，可按需选读。

## 第 1 阶段：数学与概率统计（入门 → 进阶）

线性代数：
- 〔LRL-B-18-003〕Boyd & Vandenberghe：Introduction to Applied Linear Algebra（入门）。
- 〔LRL-B-18-007〕Axler：Linear Algebra Done Right（偏证明）。

面向机器学习的数学总览：〔LRL-B-18-001〕Mathematics for Machine Learning。

概率与离散数学：〔LRL-C-17-026〕Berkeley CS70。

统计理论（高阶）：〔LRL-C-17-029〕Berkeley Stat 210A。注意这套讲义是手写扫描件，可读性有限。

信息论：
- 〔LRL-B-18-004〕MacKay。
- 〔LRL-B-18-006〕Polyanskiy & Wu（高阶）。

优化：
- 〔LRL-B-18-002〕Boyd：Convex Optimization。
- 〔LRL-C-17-027〕Stanford EE364a。
- 〔LRL-C-17-028〕EPFL Optimization for ML。
- 〔LRL-B-18-008〕Algorithms for Optimization。

高维概率与随机算法（高阶）：
- 〔LRL-B-18-005〕Vershynin。
- 〔LRL-C-17-037〕Stanford CS168。

## 第 2 阶段：机器学习与深度学习（入门 → 进阶）

课程（任选一门入门课，再选一门深度学习课）：
- 入门：
  - 〔LRL-C-17-031〕CMU 10-601。
  - 〔LRL-C-17-034〕Berkeley CS189。
  - 〔LRL-C-17-035〕Cornell CS4780。
- 深度学习：
  - 〔LRL-C-17-032〕CMU 11-785。
  - 〔LRL-C-17-033〕MIT 6.7960。
- 进阶：〔LRL-C-17-036〕UBC CPSC 440。

书：
- 概率机器学习：〔LRL-B-18-009〕Murphy PML1，〔LRL-B-18-010〕PML2。
- 深度学习主教材：〔LRL-B-18-011〕Prince：Understanding Deep Learning。
- 动手实践：〔LRL-B-18-012〕Dive into Deep Learning。
- 速览：〔LRL-B-18-014〕The Little Book of Deep Learning。
- 可微编程视角：
  - 〔LRL-B-18-015〕。
  - 〔LRL-B-18-016〕。
- 学习理论（高阶）：〔LRL-B-18-013〕Bach。
- 经典参考：〔LRL-B-18-017〕Goodfellow（离线 HTML 包）。

## 第 3 阶段：NLP 与大语言模型

课程：
- 入门：
  - 〔LRL-C-17-001〕Stanford CS224N 2026。
  - 〔LRL-C-17-011〕Princeton COS484。
  - 〔LRL-C-17-017〕Cornell LM-class。
- 进阶：
  - 〔LRL-C-17-007〕CMU 11-711。
  - 〔LRL-C-17-012〕JHU 自监督模型。
- LLM 专门课：
  - 〔LRL-C-17-002〕CS336 从零构建语言模型。
  - 〔LRL-C-17-003〕CME295。
  - 〔LRL-C-17-008〕CMU 11-667。
  - 〔LRL-C-17-019〕Princeton COS597R。
  - 〔LRL-C-17-021〕CS324（2022，经典）。

书：
- 〔LRL-B-18-018〕Jurafsky & Martin SLP3。
- 〔LRL-B-18-019〕Eisenstein。
- 〔LRL-B-18-023〕Xiao：NLP 神经网络与 LLM。
- 〔LRL-B-18-037〕Foundations of Large Language Models。
- 中文资料：
  - 〔LRL-B-18-040〕《大语言模型》。注意这份 PDF 的中文文本抽取质量差，全文检索时会漏检。
  - 〔LRL-B-18-039〕《大规模语言模型：从理论到实践》。
  - 课程课件：〔LRL-C-17-018〕人大《大语言模型》。

## 第 4 阶段：语言学基础（小语种开发必需）

形态、句法与语义：
- 〔LRL-B-18-025〕Müller：Grammatical Theory。
- 〔LRL-B-18-027〕Kroeger：Analyzing Meaning。
- 〔LRL-C-17-047〕Charles NPFL094 形态与句法分析。

语料与方法：〔LRL-B-18-026〕Corpus Linguistics。

文字系统与 Unicode：〔LRL-B-18-033〕The Unicode Cookbook for Linguists。

语言类型与多样性：
- 〔LRL-B-18-034〕美洲原住民语言的结构。
- 〔LRL-B-18-035〕Multilingualism。
- 〔LRL-B-18-036〕语言学奥赛训练指南：适合训练分析陌生语言。

入门读物：〔LRL-B-18-024〕Language and Computers。

论文，接到 LLM 时代的语言学问题：
- 形态与 LLM：
  - 〔LRL-P-02-001〕形态组合泛化。
  - 〔LRL-P-02-003〕多语言形态测试（经典补充）。
  - 〔LRL-P-02-045〕。
- 类型学：
  - 〔LRL-P-02-018〕NLP 中的“类型多样性”是什么。
  - 〔LRL-P-02-019〕。
  - 〔LRL-P-02-016〕URIEL+。
  - 〔LRL-P-02-009〕跨类型共享语法概念表示。
  - 〔LRL-P-02-051〕LLM 智能体作为计算类型学家。
- 文字：
  - 〔LRL-P-02-054〕。
  - 〔LRL-P-02-055〕模型编码文字多于语言结构。
  - 〔LRL-P-02-025〕。
- 方言与语码转换：
  - 〔LRL-P-02-026〕方言 NLP 综述。
  - 〔LRL-P-02-027〕DIALECTBENCH。
  - 〔LRL-P-02-059〕语码转换综述。
  - 〔LRL-P-02-032〕。
- 语言态度与偏见：
  - 〔LRL-P-02-028〕方言偏见。
  - 〔LRL-P-02-029〕标准语意识形态。

## 第 5 阶段：多语言学习、机器翻译与低资源 NLP

课程：
- 〔LRL-C-17-041〕CMU 11-737 多语言 NLP（2023 秋，核心）。
- 〔LRL-C-17-043〕Charles NPFL120 多语言 NLP。
- 〔LRL-C-17-052〕UZH 低资源与边缘语言变体 NLP（2026）。
- 〔LRL-C-17-046〕CMU 子词建模。
- 机器翻译：
  - 〔LRL-C-17-042〕JHU 601.468。
  - 〔LRL-C-17-044〕Charles NPFL087。
  - 〔LRL-C-17-045〕LMU。

书：
- 〔LRL-B-18-028〕《机器翻译：基础与模型》。
- 〔LRL-B-18-029〕Machine Translation for Everyone。
- 〔LRL-B-18-030〕European Language Equality。

论文（第 01 类中与跨语言相关的基础）：
- 〔LRL-P-01-044〕跨语言对齐综述。
- 〔LRL-P-01-040〕Semantic Hub 假说。
- 〔LRL-P-01-033〕LLM 作为低资源语言的少样本学习者。
- 〔LRL-P-01-066〕多语言问答的校准。

## 第 6 阶段：接入专题

学完以上内容后，可按目标进入以下指南：
- data_pipeline_cn.md
- model_adaptation_cn.md
- evaluation_cn.md
- application_development_cn.md
- deployment_cn.md

规模规律与数据受限训练，是理解“小语种数据少”这一问题的理论入口：
- 〔LRL-P-01-007〕。
- 〔LRL-P-01-014〕。
- 〔LRL-P-01-005〕。
