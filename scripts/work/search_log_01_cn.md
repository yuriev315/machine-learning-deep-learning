# 检索日志：01 数学与学习基础（math_learning_foundations）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search '<查询>'`（arXiv API，relevance 排序），结合已有知识列出候选，再由 `resolve` 按 arXiv ID 与标题双重核对（标题相似度 ≥0.85 才接受）。
- 范围界定：只收论文/综述/教程；教材类系统基础由 18 类负责。本类允许“通用支撑”占多数，但每条在 `reason` 与注释 `relevance_use` 中写明对小语种开发的用途；优先选择与多语言、跨语言迁移、低资源条件有联系的理论工作。

## 1. 查询式（原样）与返回数

| # | 查询式 | 返回 | 选入（sid） |
|---|---|---|---|
| Q1 | `abs:"latent language" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 3 | 2609.00155（01-059） |
| Q2 | `abs:"language-specific neurons" AND submittedDate:[202310290000 TO 202610290000]` | 20 | 2404.02431、2503.17456、2509.17030、2507.22608、2508.17078（另 2402.16438/2402.18815 已归 03） |
| Q3 | `abs:"catastrophic forgetting" AND abs:"language models" AND (abs:theory OR abs:"scaling law") AND submittedDate:[...]` | 19 | 2401.05605、2509.19371（备选）；2407.17467 已归 07（cross_only） |
| Q4 | `abs:"in-context learning" AND abs:"low-resource" AND abs:theory AND submittedDate:[...]` | 0 | —（查询过窄，改用已知文献 2403.16512、2401.12973 等） |
| Q5 | `abs:"curse of multilinguality" AND submittedDate:[...]` | 20 | 2608.17088；2406.10602、2510.25947 分别已归 03、07（cross_only） |
| Q6 | `(abs:calibration OR abs:uncertainty) AND (abs:multilingual OR abs:"low-resource languages") AND abs:"language models" AND submittedDate:[...]` | 25 | 2601.01362、2510.03136、2507.06306（备选）；2406.15948 已归 10（cross_only） |
| Q7 | `(abs:"cross-lingual transfer") AND (abs:theoretical OR abs:theory) AND submittedDate:[...]` | 5 | 2603.17945 |
| Q8 | `abs:"scaling law" AND abs:multilingual AND submittedDate:[...]` | 22 | 2603.17945、2409.15051、2605.12715、2402.17193；2510.22037/2410.12883 已归 03、2404.08191 列入 06 种子（cross_only） |
| Q9 | `abs:"cross-lingual" AND abs:representation AND abs:alignment AND abs:"large language models" AND submittedDate:[...]` | 30 | 2502.14830、2406.13229、2503.11280、2504.09378、2601.22851、2603.29026 |
| Q10 | `ti:"Scaling Laws for Downstream Task Performance"` 等 3 条标题核对查询 | 1–3 | 用于纠正 01-005、01-047 标题；01-076 原拟收的 MBR 理论论文按标题未检得，改收 2411.03524 |
| Q11 | `ti:"Min-p"` | 2 | 2407.01082；2506.13681（备选，批判性复核） |

（`[...]` 均为 `submittedDate:[202310290000 TO 202610290000]`。arXiv API 在多会话共享限速下偶有返回偏少，Q1/Q4 的低返回数可能与此有关。）

## 2. 基于已有知识直接列入并经 resolve 核对的文献
规模规律（Chinchilla 复现、计算最优分歧、过度训练、数据混合律、数据受限）、学习率调度（WSD、D2Z、Schedule-Free）、优化器（Muon、优化器比较两篇、临界批大小、参数化指数、μP）、ICL 理论（ICL 短暂性、ICLL、多样本 ICL、ICL 综述）、涌现与记忆（损失视角涌现、分布式记忆、知识容量、事实知识获取）、跨语言表示（语义枢纽、语言区域、跨语言对齐综述、对齐涌现、中间层对齐等）、遗忘（遗忘规模规律、伪遗忘、持续学习综述、可塑性丧失）、校准（多语言 QA 校准、校准综述、UQ 综述）、解码（min-p、解码方法综述、MBR 指标偏差）。

## 3. 排除 / 让位 / 替代关系
- 与其他类别重叠且对方已认领或已列为主条目的，本类改为 `cross_only`（不下载不计数）：2410.12883、2510.22037、2402.10588、2402.16438、2311.09205、2402.18815、2406.16135、2404.07982、2406.10602（03 类）；2404.08191（06 类）；2407.17467、2510.25947（07 类）；2406.15948（10 类）。
- 另有 11/07 类以 cross_only 引用本类条目（2502.15603、2408.10811、2403.16512、2404.16789、2405.18392、2501.13453），主分类保留在本类。
- 01-076：原拟 “Theoretical Aspects of Bias and Diversity in Minimum Bayes Risk Decoding”（ID 不确定、标题检索无结果）→ 改为 2411.03524 “Mitigating Metric Bias in MBR Decoding”。
- 三年前经典（共 4 篇，均写 old_reason）：Chinchilla（2203.15556）、μP/Tensor Programs V（2203.03466）、数据受限规模规律（2305.16264）、Language Modeling Is Compression（2309.10668）。未收 2309.10105（遗忘的隐式推断解释）等，以控制经典数量。
- 未收：LoRA Learns Less and Forgets Less（更贴近 08）、Simple and Scalable Strategies to Continually Pre-train（07 已认领）、标记化公平性相关论文（06）。

## 4. 结果与未完成事项
- 下载：先 `download 01 --target 55`（55 篇全部一次核验通过），为补齐“采样与解码”“不确定性与校准”子方向，再 `download 01 --target 64` 下载剩余 9 篇主列表条目；备选（reserve）9 篇未动用。
- 下载失败 0、待核验 0，未使用 manual 提升。7 篇为兄弟库已核验 PDF 的复制复核（已有复用）。
- 注释：64 篇全部写入 `scripts/annotations/01_math_learning_foundations_annot_cn.json`，以 brief 摘要为主；01-007、01-033、01-040 用 text 命令查看了正文首页补充。top_rank 1–10 已标注。
- 相关性：直接相关 27、通用支撑 37（本类允许通用支撑占多数，均写明用途）。
- 未完成/疑点：许多通用支撑论文的语言、数据规模字段仍为“待核实”（摘要未给出）；“分布偏移”子方向未单独收录专门论文（相关内容分散在迁移、校准与遗忘论文中）。

### 最终状态（status 01 输出）
```
[01 数学与学习基础] 已核验完整资料 64 / 目标约 50；待核验 0；下载失败 0。 近三年 60/64 = 93.8%；三年前 4（上限 5）；未定日期 0
  cross_only (tag only, primary elsewhere): 13
  reserve: 9
  OLD 01-013 2022-03-29 Training Compute-Optimal Large Language Models | reason: '计算最优规模规律的奠基工作，近三年多语言/数据受限规模规律均以其为基线，无可替代'
  OLD 01-014 2023-05-25 Scaling Data-Constrained Language Models | reason: '数据受限（重复数据）规模规律的经典工作，小语种语料稀缺场景最常引用的依据，发表于'
  OLD 01-016 2023-09-19 Language Modeling Is Compression | reason: '语言建模—压缩等价视角的代表性论文（2023-09），跨语言比较常用的 bits'
  OLD 01-027 2022-03-07 Tensor Programs V: Tuning Large Neural Networks via Zero-Sho | reason: 'μP 超参数迁移的奠基工作，近三年参数化与学习率迁移研究（如 Scaling E'
  subtopics: 表示几何与跨语言对齐 19; 规模规律与计算最优 11; 优化器与学习率调度 10; 上下文学习与泛化理论 9; 迁移学习与灾难性遗忘 5; 不确定性与校准 5; 采样与解码的概率基础 3; 信息论与压缩视角 2
```

