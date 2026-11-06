# 检索日志（汇总）

检索日：2026-10-29（UTC）。近三年窗口：首次公开日期 ≥ 2023-10-29。以下按类别原样合并各类检索记录（查询式、返回数、选入/排除原因、替代关系）；原始分文件在 `scripts/work/`。主要检索源：arXiv API（export.arxiv.org，限速 5 s/次，与本机其他资料库共享限速队列）、ACL Anthology、课程官方主页、作者/出版社官方页面、GitHub。


---

<!-- 来源：scripts/work/search_log_01_cn.md -->

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


---

<!-- 来源：scripts/work/search_log_02_cn.md -->

# 检索日志：02 自然语言处理与语言学基础（nlp_linguistics_foundations）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search '<查询>'`（arXiv API，relevance 排序），结合已有知识列候选，`resolve` 以 arXiv ID + 标题相似度（≥0.85）核对。
- 范围：语言模型与计算语言学、形态与句法、文字系统、语言类型学、方言与语言变体、语码转换、语言多样性与 NLP 不平等、UD/UniMorph 等语言学资源，以及濒危语言记录（行间注释、语法整理）与语言学推理。

## 1. 查询式（原样）与返回数

（`[...]` 均为 `submittedDate:[202310290000 TO 202610290000]`）

| # | 查询式 | 返回 | 选入（arXiv） |
|---|---|---|---|
| Q1 | `abs:"morphological inflection" AND abs:"language models" AND [...]` | 1 | 2506.05227 |
| Q2 | `abs:"dependency parsing" AND abs:"large language models" AND (abs:"low-resource" OR abs:"Universal Dependencies") AND [...]` | 1 | 2506.09983 |
| Q3 | `abs:typological AND abs:"large language models" AND (abs:WALS OR abs:Grambank OR abs:URIEL) AND [...]` | 0 | —（改用已知文献 URIEL+ 2409.18472 等） |
| Q4 | `ti:"code-switching" AND (abs:survey OR abs:"large language models") AND [...]` | 30 | 2510.07037、2504.01801、2410.18436、2606.19668、2506.01840、2512.03334、2506.14012、2510.05678；2604.15490（备选）；语音类（ASR/TTS）与安全红队（2406.15481，属 10）排除 |
| Q5 | `ti:dialect AND abs:"large language models" AND [...]` | 30 | 2510.00962、2404.08092、2510.22747、2412.04193、2504.05898、2608.10414、2506.08907；2311.00915、2502.12858、2609.09964（备选）；单一应用系统/诗歌生成等排除 |
| Q6 | `(abs:"writing system" OR abs:"writing systems" OR ti:script) AND abs:"language models" AND abs:multilingual AND [...]` | 25 | 2404.18810、2604.05090、2608.25904、2311.18034；分词/像素模型类（MYTE、Script Tax、BPE Stays on SCRIPT、像素 LM）留给 06 |
| Q7 | `(abs:"endangered languages" OR abs:"indigenous languages") AND abs:"large language models" AND [...]` | 30 | 2412.10960、2406.18895、2412.00218、2504.01522；2407.12620 已归 04；翻译类（Hire a Linguist 等）已归 09 |
| Q8 | `abs:"linguistic diversity" AND abs:NLP AND (abs:inequality OR abs:disparity OR abs:"low-resource") AND [...]` | 25 | 2610.30296；2505.04531（备选）；单语种模型/数据集类留给 03/04 |
| Q9 | `abs:"interlinear gloss" AND [...]` | 15 | 2601.10925、2502.09778、2511.00343、2609.07791；2603.00923、2403.08189（备选） |
| Q10 | `abs:BabyLM AND abs:multilingual AND [...]` | 7 | 2610.20102（备选） |
| Q11 | `(abs:typology OR abs:typological) AND abs:"cross-lingual transfer" AND abs:"language models" AND [...]` | 20 | 2601.16629、2601.21587；2505.13908、2507.20279（备选）；2605.10714 已归 04；2601.05776 |
| Q12 | `abs:UniMorph AND [...]` | 11 | 2402.14411（备选）；非 NLP 结果（压电/机器人）排除 |
| Q13 | `abs:"Universal Dependencies" AND abs:"language models" AND [...]` | 18 | 2311.07497、2506.07274；2603.00432、2512.00214（备选） |

## 2. 基于已有知识直接列入并经 resolve 核对
形态（2410.12656、2403.06399 GlossLM、2406.18895、2412.10960）、句法与语言能力探测（Mission: Impossible 2401.06416、2501.06346、MultiBLiMP 2504.02768、2410.09223、2409.12435、2408.07144、2406.04289）、类型学（URIEL+ 2409.18472、2501.14491、2402.04222、2407.05022）、文字（Prompting with Phonemes 2411.02398）、方言（2401.05632 综述、DIALECTBENCH 2403.11009、2403.00742、2406.08726）、语码转换（2410.22660）、不平等（2311.08391、2412.04497）、语言学推理（LINGOLY 2406.06196、Linguini 2409.12126）、BabyLM 第二届总结（2412.05149）。

## 3. 排除 / 让位 / 替代
- 以下与他类重叠、对方已认领或列为主条目，本类改为 `cross_only`（不下载不计数）：
  - 06 类（分词/词表）：2411.14198（形态复杂语言为何更难建模）、2401.14280 RomanSetu、2401.06620 TransliCo、2407.02320（音译与 ICL）、2406.19759（音译后训练对齐）。这些本属“文字系统/音译/罗马化”主题，但 06 已先列为主条目，为避免抢占改作交叉标签；本类以 2404.18810、2604.05090、2608.25904、2601.05776、2411.02398、2412.00218 补足文字系统方向。
  - 07 类：2411.02460（语码转换课程学习）。
  - 09 类：2409.19151（语法书能否教会翻译）。
  - 04 类：2410.20817（“低资源”定义的芝诺悖论）、2605.10714（卢森堡语经验）、2407.12620（濒危原住民语言 AI）。
- 三年前经典（4 篇，均写 old_reason）：2310.15113（Wug 多语言形态测试，早于窗口 6 天）、2205.03608 UniMorph 4.0、2004.09095（Joshi 语言资源分级）、2004.10643 Universal Dependencies v2。
- 交叉较多但保留为本类主条目的：2601.05776（06 列为备选）、2601.16629（08 列为备选）、2510.22747（07 列为备选）。

## 4. 结果与未完成事项
- 下载：先 `download 02 --target 55`（55 篇一次核验通过）；因“语言多样性与 NLP 不平等”“文字系统”等子方向偏少，再 `download 02 --target 65` 下载主列表剩余 10 篇；备选 17 篇未动用。
- 下载失败 0、待核验 0，未使用 manual。1 篇为兄弟库已核验 PDF 的复制复核（已有复用）。
- 注释：65 篇全部写入 `scripts/annotations/02_nlp_linguistics_foundations_annot_cn.json`，以 brief/arXiv 摘要为主；02-010、02-056 用 text 命令查看正文补充语言列表与资源链接。top_rank 1–10 已标注。
- 相关性：直接相关 61、通用支撑 4。
- 子方向命名：原 “语言学推理与语法书学习” 与 “濒危语言记录与语言学推理” 合并为 “语言学推理与语言记录”（只改 subtopic 字段，未改 sid/arXiv）。
- 未完成/疑点：文字系统方向的音译/罗马化核心论文多已由 06 先列为主条目，本类仅以 cross_only 标注；方言与语码转换中部分评测基准（DIALECTBENCH、AL-QASIDA、泰语方言基准）与 15 类有交叉，已在 cross 中注明。

### 最终状态（status 02 输出）
```
[02 自然语言处理与语言学基础] 已核验完整资料 65 / 目标约 50；待核验 0；下载失败 0。 近三年 61/65 = 93.8%；三年前 4（上限 5）；未定日期 0
  cross_only (tag only, primary elsewhere): 10
  reserve: 17
  OLD 02-003 2023-10-23 Counting the Bugs in ChatGPT's Wugs: A Multilingual Investig | reason: 'LLM 形态能力多语言探测的代表性工作（2023-10-23，仅早于窗口 6 天'
  OLD 02-007 2022-05-07 UniMorph 4.0: Universal Morphology | reason: 'UniMorph 形态资源的现行主版本说明论文，近三年形态评测普遍依赖，没有更新'
  OLD 02-038 2020-04-20 The State and Fate of Linguistic Diversity and Inclusion in  | reason: '语言资源分级（Joshi 等级）的奠基工作，近三年小语种论文普遍沿用该分级定义资'
  OLD 02-043 2020-04-22 Universal Dependencies v2: An Evergrowing Multilingual Treeb | reason: 'UD v2 是现行多语言依存树库的统一标注规范说明，近三年 UD 相关工作均基于'
  subtopics: 句法与语言能力探测 11; 方言与语言变体 11; 形态学与大模型 9; 语码转换（code-switching） 9; 语言类型学与跨语言迁移 8; 文字系统、音译与罗马化 6; 语言多样性与 NLP 不平等 6; 语言学推理与语言记录 3; 资源与基础设施 2
```


---

<!-- 来源：scripts/work/search_log_03_cn.md -->

# 检索日志：03 多语言及低资源语言大模型（multilingual_lowres_llm）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search '<查询>' --max N --sort relevance`（arXiv export API），结合已有知识列出候选，再用 `resolve` 按 ID/标题核对元数据。
- 近三年窗口：首次公开 ≥ 2023-10-29（下列查询中的 `submittedDate:[202310290000 TO 202610290000]` 记为 `<D>`）。

## 1. 查询式与返回数（原样）

| # | 查询式 | max | 返回 | 主要选入 |
|---|---|---|---|---|
| 1 | `abs:"low-resource" AND abs:"large language model" AND abs:adapt* AND <D>` | 40 | 40 | LlamaTurk（2405.07745）、Dicta-LM 3.0（2602.02104）、UrduLLaMA（未选，见排除） |
| 2 | `ti:multilingual AND ti:"language model" AND (abs:"technical report" OR abs:"open") AND <D>` | 40 | 40 | EuroLLM、LOLA、Aya、FuxiTranyu、Babel、Qin 综述（2404.04925） |
| 3 | `abs:"curse of multilinguality" AND <D>` | 30 | 24 | When Is Multilinguality a Curse（2311.09205）、ATLAS（2510.22037）、Gurgurov 综述（2406.10602）、Paramanu（2401.18034） |
| 4 | `abs:"African languages" AND abs:"language model" AND <D>` | 30 | 30 | 非洲 LLM 现状综述（2506.02280）、Cheetah、Lugha-Llama |
| 5 | `abs:"Southeast Asian" AND abs:"language model" AND <D>` | 30 | 30 | SeaLLMs、SeaLLMs 3、SEA-LION；OpenSeal、Toward Robust…（2510.14466）列为备选 |
| 6 | `(abs:Tibetan OR abs:Uyghur OR abs:Mongolian OR abs:Kazakh) AND abs:"large language model" AND <D>` | 30 | 30 | Sherkala-Chat（标题据此更正）、藏语稠密/MoE 持续预训练（2507.09205）、藏语两阶段适配（2512.03976，备选） |
| 7 | `(abs:"language-specific" OR abs:"language neurons") AND abs:multilingual AND abs:LLM AND ti:language AND <D>` | 20 | 20 | Language Arithmetics（2507.22608，备选）；Language-Specific Neurons、How do LLMs Handle Multilingualism 已在列表 |
| 8 | `(ti:Uyghur OR ti:Mongolian OR ti:Kyrgyz OR ti:Uzbek OR ti:Tatar OR ti:Bashkir) AND abs:"language model" AND <D>` | 20 | 7 | 巴什基尔语 LoRA/QLoRA（2605.04948，备选）；其余为基准/树库（归 15/02） |
| 9 | `(ti:Burmese OR ti:Myanmar OR ti:Khmer OR ti:Lao OR ti:Sinhala OR ti:Nepali) AND abs:"language model" AND <D>` | 20 | 20 | SinLlama（2508.09115）、NepaliGPT（2506.16399，备选） |
| 10 | `(ti:Swahili OR ti:Yoruba OR ti:Hausa OR ti:Zulu OR ti:Igbo OR ti:Amharic OR ti:Tigrinya) AND abs:"large language model" AND <D>` | 20 | 13 | Walia-LLM、Amharic LLaMA and LLaVA（2403.06354） |
| 11 | `(ti:Quechua OR ti:Guarani OR ti:Nahuatl OR ti:Aymara OR ti:Mayan OR ti:Cherokee OR ti:Inuktitut) AND abs:"language model" AND <D>` | 20 | 4 | QueEn（2412.05184） |
| 12 | `(ti:Georgian OR ti:Armenian OR ti:Icelandic OR ti:Faroese OR ti:Maltese OR ti:Welsh OR ti:Luxembourgish OR ti:Basque OR ti:Catalan) AND abs:"large language model" AND <D>` | 20 | 19 | Latxa（已在列表）；其余多为基准/指令数据（归 15/08） |
| 13 | `abs:"cross-lingual transfer" AND abs:"large language models" AND abs:"low-resource languages" AND ti:multilingual AND <D>` | 30 | 9 | EMMA-500（已在列表） |
| 14 | `(abs:Uyghur OR abs:Mongolian) AND (abs:"large language model" OR abs:LLM) AND <D>` | 20 | 10 | Do Chinese models speak Chinese languages?（2504.00289）、Left Behind（2603.21036，备选） |
| 15 | `(abs:Guarani OR abs:Quechua OR abs:Nahuatl OR abs:Mapudungun OR abs:Wixarika OR abs:Shipibo) AND (abs:"large language model" OR abs:LLM) AND <D>` | 20 | 4 | 无新增（MTOB 类工作属 09/15） |
| 16 | `abs:"low-resource languages" AND (ti:survey OR ti:review) AND abs:"large language models" AND <D>` | 20 | 8 | 南亚低资源语言综述（2509.11570）、多语言 LLM 综述（2404.00929，备选） |
| 17 | `abs:"indigenous languages" AND abs:"large language model" AND <D>`（与 06 共用批次） | 30 | 14 | 萨米语（2405.05777）、TharuChat（2603.17220）、巴西原住民语言（2407.12620，后被 04 认领） |
| 18 | `(abs:Indic OR abs:Hindi OR abs:Bengali OR abs:Tamil OR abs:Telugu) AND ti:"language model" AND abs:"pretrain" AND <D>`（与 06 共用批次） | 30 | 30 | Agaram 2.5B（2610.18420）；LilMoo（2603.03508）、孟加拉 135M（2606.16383）列为备选 |
| 19 | `abs:"vocabulary expansion" OR …`（06 检索中顺带发现） | 40 | 40 | 确认 Cendol、Swallow（未选，归 07） |
| 20 | `ti:"language imbalance"`（核对 ID） | 10 | 3 | 2404.07982 的正确标题为 *The Role of Language Imbalance in Cross-lingual Generalisation…*，已更正种子标题 |

其余条目（Aya 系列、SeaLLMs、Sailor/Sailor2、Typhoon、Komodo、InkubaLM、Tamil-Llama、Krutrim、Nanda、ALLaM、Atlas-Chat、Fanar、PersianMind、UCCIX、Poro、Salamandra、Llammas、HyperCLOVA X、LLM-jp、Meltemi、Nile-Chat、Apertus、Marco-LLM、Goldfish、X-ELM、语言机制分析三篇、经典 Jais/PolyLM/Glot500/BLOOM）来自已有知识，经 `resolve` 按 arXiv ID 与标题核对一致（除 2404.07982 标题更正外 0 处纠错）。

## 2. 选入与排除原则
- 选入：多语言基座/技术报告；多语言诅咒、语言不均衡与跨语言迁移机制；具体语言/语区的 LLM 适配或从零训练案例（注重语系、文字与资源条件的多样性）；综述。
- 排除或让给其他类别：纯基准（15，如 IrokoBench、SEA-HELM、TLUE、MM-Eval、KazMMLU、TUMLU、SinhalaMMLU）；纯语料/数据集（04，如 MC²、TFD 藏语数据集）；以持续预训练配比为核心的方法研究（07，如 Swallow 2404.17790、Rethinking Multilingual Continual Pretraining 2504.04152、Revisiting Multilingual Data Mixtures 2510.25947）；以指令数据/PEFT 为核心（08，如 Marathi LoRA 2411.18571、Basque instruct pipeline 2412.13922）；翻译/合成（09，如 Tower、LLaMAX）；多模态/语音模型（不收）。
- UrduLLaMA（2502.16961）、Compass（2404.09220）、YAYI 2：信息量或与小语种关联较弱，未选。

## 3. 替代与认领冲突
- 03-053 *Teaching Large Language Models an Unseen Language on the Fly*（壮语）已被 09 认领为 09-003 → 本类改为 `cross_only`，由新增条目补足。
- 03-076 *Harnessing the Power of AI to Vitalize Endangered Indigenous Languages*（巴西原住民语言）已被 04 认领为 04-030 → 改为 `cross_only`。
- 美洲原住民语言目前只有 QueEn（克丘亚语）一篇为本类主分类，属明显缺口。
- 为增加文字/语系覆盖，第二轮追加并下载：萨米语、僧伽罗语、塔鲁语、泰米尔语从零训练、乌克兰语、中国少数民族语言覆盖评测、南亚综述、阿姆哈拉语多模态；备选（未下载）：NepaliGPT、巴什基尔语、Left Behind、Language Arithmetics、多语言 LLM 综述 2404.00929、LilMoo、孟加拉 135M、MaLLaM、VinaLLaMA、Marco-LLM、藏语两阶段、OpenSeal、2510.14466、2604.21637。

## 4. 下载与核验
- `download 03 --target 55` → 55 已核验 + 2 待核验；`--target 70` 补下第二轮 → 共 70 已核验。
- 人工提升（`manual`，均用 `text` 核对首页）：03-046 HyperCLOVA X（pypdf 抽取为 “HyperCLOV A X” 致标题匹配 0.75）；03-061 Meltemi（作者姓 “V oukoutis” 被拆开致姓氏检查失败）。
- 最终：已核验 70；待核验 0；失败 0；近三年 66/70 = 94.3%；经典 4 篇（Jais、PolyLM、Glot500、BLOOM，均写 old_reason）。

## 5. 未完成/缺口
- 维吾尔语、蒙古语（含传统蒙古文）、缅甸语、高棉语、老挝语缺少专门的 LLM 适配主分类论文（检索只得到基准或数据集）；目前仅通过 SeaLLMs/SEA-LION/Sailor2 与 2504.00289 间接覆盖。
- 美洲原住民语言仅 1 篇主分类（QueEn），另 1 篇被 04 认领。
- 注释以摘要为主，top-10 已用正文关键词核对补充；其余条目中“待核实”字段需后续读正文补齐。


---

<!-- 来源：scripts/work/search_log_04_cn.md -->

# 检索日志：04 语料来源、治理与许可（corpus_sources_governance）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv API，`--max 25~50`，按相关度）；辅以通用网页检索（WebSearch）定位 arXiv 编号与 ACL Anthology 条目；已知论文直接按记忆给出 arXiv ID，由 `resolve` 按标题核对（全部通过，0 条纠错）。
- 说明：arXiv API 当日响应很慢（单次查询约 1–2 分钟，并有其他会话并发），部分查询返回噪声较多。

## 1. arXiv 查询式（原样）与返回数

| 查询式 | 返回 | 选入（本类） |
|---|---|---|
| `abs:pretraining AND abs:dataset AND abs:multilingual AND abs:languages AND abs:CommonCrawl AND submittedDate:[202310290000 TO 202610290000]` | 0 | — |
| `ti:multilingual AND ti:dataset AND abs:pretraining AND submittedDate:[...]` | 8 | 无直接选入（ÜberWeb、Mix-MinHash-Match 转 05；Lucie 属模型类不选） |
| `abs:"data provenance" AND submittedDate:[...]` | 30 | 2404.12691、2601.14311、2512.21775、2404.14740（多数结果为 IoT/安全，排除） |
| `abs:licensing AND abs:datasets AND abs:"language models" AND submittedDate:[...]` | 30 | 2604.00920、2506.01732、2502.04484（车牌识别等无关结果排除） |
| `abs:"data sovereignty" AND submittedDate:[...]` | 30 | 2608.08905、2311.15473、2404.02309、2510.13871（联邦学习等排除） |
| `abs:indigenous AND abs:languages AND abs:community AND abs:data AND submittedDate:[...]` | 22 | 2409.05247、2407.12620、2501.11003、2603.14873、2610.25440；2405.05777（萨米语，列备选） |
| `ti:HPLT` | 2 | 2503.10267、2511.01066 |
| `ti:FineWeb2` | 2 | 2506.20920（2610.31636 转 05） |
| `ti:MADLAD` | 1 | 2309.04662（经典补充） |
| `ti:GlotCC OR ti:Glot500` | 2 | 2410.23825（Glot500 属模型类 03，不选） |
| `abs:"Data Provenance Initiative"` | 0（超时/无结果） | 2310.16787 由已知 ID 补入 |
| `ti:"Consent in Crisis"` | 1 | 2407.14933 |
| `ti:"Common Pile"` | 1 | 2506.05209 |
| `ti:"Institutional Books"` | 3 | 2506.08300（2608.19026 转 05） |
| `ti:SeaCrowd OR ti:"MC^2" OR (ti:minority AND ti:languages AND ti:China)` | 25 | 2311.08348（其余多为物理学 E=mc² 噪声；MiLiC-Eval、CMHG 属评测类不选） |
| `ti:corpus AND abs:"low-resource" AND abs:"language models" AND submittedDate:[...]` | 20 | 2508.16048、2403.16571、2505.18905、2603.20732（备选）、2506.09560（备选） |
| `ti:parallel AND ti:corpus AND abs:"low-resource" AND submittedDate:[...]` | 11 | 2403.19365、2606.06420、2505.24472（备选） |
| `abs:"personally identifiable information" AND abs:pretraining AND submittedDate:[...]` | 7 | 无（多为成员推断/遗忘，非语料治理） |
| `ti:dialogue AND ti:dataset AND abs:"low-resource" AND submittedDate:[...]` | 2 | 2508.07069 |
| `abs:Wikipedia AND abs:"low-resource" AND abs:quality AND submittedDate:[...]` | 17 | 本类未选（2411.05527、2404.00565 转 05） |
| `abs:toxicity AND abs:filtering AND abs:multilingual AND abs:pretraining AND submittedDate:[...]` | 2 | Apertus 属模型类，不选 |
| `abs:Masakhane AND submittedDate:[...]` | 7 | 未选（多为 NER/增强/基准，属其他类） |

## 2. 网页检索（定位编号）
- “language identification low-resource … closely related” → 转 05。
- “licensing low-resource language datasets audit African” → 2606.28867（Open but Incompatible，RAIL 2026）。
- “pretraining corpus construction low-resource … Swahili Amharic …” → 2603.16354（PashtoCorp）、WURA（EMNLP 2023，ACL Anthology 2023.emnlp-main.11，无 arXiv 版）。
- “Esethu Framework” → 2502.15916。
- “data cards documentation low-resource” → 2401.13822、2605.17442；2201.10066（BigScience 目录，2022，未选）。
- “Indigenous data sovereignty … CARE principles” → 2402.02639；2309.10215（2023-09，窗口外，未选）。
- “privacy PII multilingual pretraining” → 2510.07551（选入）、2601.03791（备选）、2506.00759（跨语言隐私泄露，偏 10 类，未选）。
- “multilingual conversational dataset low-resource” → 2508.07069；IndicTalk、M2Lingual 为合成对话（属 09），未选。
- “deduplication multilingual” → 2609.07699（Fine PT-PT Web）。

## 3. 选入/排除与替代
- 主列表最终核验 61 篇（近三年 56，经典 5：MADLAD-400、Data Provenance Initiative、CulturaX、Masakhane 参与式研究、BigScience 数据治理）。经典均写 old_reason。
- 04-031 SMOL（2502.12301）已被 09 类（09-064）先认领 → 改为 `cross_only`，由备选补足。
- 备选中 04-054（克丘亚语 Common Voice）、04-055（BigScience 数据治理，经典）、04-056（Zeno's Paradox）因首轮下载时主列表不足 55 而被下载并核验；之后追加的 04-059~064（SomaliWeb、OpenWHO、EthioMT、NSINA、Kpelle、Komi-Yazva）以 `--target 61` 补下载。
- 未下载备选：04-057（萨米语 LLM，可能属 03）、04-058（PII 记忆，偏 10）、04-065（MzansiText，含模型）、04-066（马其顿语语料+模型）、04-067（VietMix）。
- 通用支撑 17 篇（英语为主的语料/许可/来源追踪工作），均在注释 relevance_use 中写明对小语种的用途；直接相关 44/61 = 72%。
- 刻意不收：Aya Dataset（社区参与典型，但为 08 指令数据核心论文）、Glot500/EMMA-500/MaLA（模型为主，03）、TransWebEdu/MultiSynt（机器翻译预训练数据，09）、各类评测基准（15）。

## 4. 未完成/疑点
- 04-046 SEADialogues 的对话构建方式（人工撰写或 LLM 生成）摘要未说明，注释标“待核实”。
- WURA（04-049）首次公开日期按 EMNLP 2023 会议（2023-12）记，精度“月”；未找到更早预印本。
- 低资源对话语料、隐私/PII 治理（非英语）方向的近三年专门论文较少，覆盖偏薄。


---

<!-- 来源：scripts/work/search_log_05_cn.md -->

# 检索日志：05 数据处理与质量（data_processing_quality）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv API）；辅以通用网页检索定位 arXiv 编号；已知论文按记忆给 ID，由 `resolve` 按标题核对（0 条纠错，0 条未解析）。
- 说明：arXiv API 当日很慢（单次 1–2 分钟），去重类查询噪声大（多为系统/存储领域“deduplication”）。

## 1. arXiv 查询式（原样）与返回数

| 查询式 | 返回 | 选入（本类） |
|---|---|---|
| `ti:FineWeb2` | 2 | 2610.31636（斯洛伐克 FineWeb2 智能体审计）；FineWeb2 本体放 04 |
| `ti:"machine translated" AND ti:web` | 8 | 2401.05749、2511.03880 |
| `abs:"language identification" AND abs:"low-resource" AND submittedDate:[202310290000 TO 202610290000]` | 25 | 2506.15304、2406.17901、2602.13139、2602.17655、2609.06963、2603.13238、2512.08143（备选）、2502.18148（备选）；ASR/TTS 类排除 |
| `ti:"language identification" AND submittedDate:[...]` | 25 | 2403.09892、2504.21540、2603.15969、2502.06692、2503.06547、2507.11832、2606.06088、2610.16601、2311.09696、2402.01505、2406.06263、2509.07998（备选）；母语识别（NLI）、语言生成理论、口语 LID 排除 |
| `ti:deduplication AND submittedDate:[...]` | 25 | 仅 2411.04257 相关（其余为存储/崩溃去重等）；2501.01046（SEDD/FED）未选 |
| `abs:"quality filtering" AND abs:multilingual AND submittedDate:[...]` | 13 | 2610.11585、2604.20549、2411.05527、2512.18834；2605.18232（SomaliWeb）放 04 |
| `abs:contamination AND abs:multilingual AND submittedDate:[...]` | 25 | 2410.16186、2601.20858、2406.13236、2601.14994；MEGAVERSE、GreekMMLU 等评测基准属 15，不选 |
| `ti:OCR AND abs:"low-resource" AND submittedDate:[...]` | 24 | 2412.16119、2412.15248、2408.02253、2507.18264、2603.13238、2602.21042（备选）、2609.11495（备选）；Lakota OCR 放 04；LaTeX/车牌/场景文字 OCR 排除 |
| `abs:"Unicode" AND abs:normalization AND abs:languages AND submittedDate:[...]` | 13 | 2609.33734（Yorùbá in Unicode）、2601.01091（KS-LIT-3M）；TTS 文本规范化与分词论文排除 |
| `abs:perplexity AND abs:filtering AND abs:languages AND abs:pretraining AND submittedDate:[...]` | 8 | 2509.18577（备选）；BhashaKritika 为合成数据（09） |
| `ti:"data selection" AND abs:multilingual AND submittedDate:[...]` | 10 | 2610.11585、2502.10361、2507.01785、2604.20549 |
| `abs:"language identification" AND abs:"closely related" AND submittedDate:[...]` | 9 | 2502.06692、2406.17901、2602.13139、2602.17655、2512.08143；2404.08345（FastSpell，备选） |
| `abs:Wikipedia AND abs:"low-resource" AND abs:quality AND submittedDate:[...]` | 17 | 2411.05527；2404.00565（埃及阿拉伯语维基模板翻译检测，备选） |
| `abs:"web register" OR ti:register AND abs:multilingual AND submittedDate:[...]` | 8 | 2406.19892 |
| `abs:toxicity AND abs:filtering AND abs:multilingual AND abs:pretraining AND submittedDate:[...]` | 2 | 2509.08824（葡萄牙语语料，备选）；Apertus 属模型（03） |
| `abs:"temperature sampling" AND abs:languages AND submittedDate:[...]` | 25 | 2410.04579（其余多为解码温度，排除） |
| `ti:audit AND abs:multilingual AND abs:dataset AND submittedDate:[...]` | 2 | 2411.05527（已选） |

## 2. 网页检索（定位编号）
- “language identification low-resource 2025 web corpus closely related” → 2602.13139（OpenLID-v3）、2601.18026（CommonLID）。
- “Unicode normalization script low-resource LLM pretraining” → 2410.24140（Don't Touch My Diacritics）、2601.01091/2604.11066（克什米尔语 InPage 旧编码转换；后者放 04）。
- “quality filtering low-resource multilingual” / “cross-lingual quality classifiers” → 2505.22232、2502.10361、2604.20549、2507.01785。
- “OCR post-correction low-resource historical” → 2410.13305、2502.01205。
- “machine translated text detection web corpus” → 2511.02958（SMaTD）。
- “web-mined parallel corpora quality Sinhala Tamil” → 2402.07446。
- “dialect identification VarDial” → 未找到合适 arXiv 综述；NADI 2024（2407.04910）由已知 ID 补入。
- “benchmark contamination translated multilingual” → 2601.14994。
- “language sampling temperature multilingual” → 2410.04579；UniMax（2304.09151，经典）。
- “deduplication multilingual near-duplicate” → 无新的多语言去重专门论文（Mix-MinHash-Match 已选）。
- “register genre classification multilingual” → 2504.01542、2406.19892。

## 3. 选入/排除与替代
- 最终核验 67 篇（近三年 63 = 94.0%）；直接相关 55/67 = 82%。
- 经典补充（种子 5 篇，均写 old_reason）：GlotLID（2023-10-24，窗口前 5 天）、Quality at a Glance、OpenLID、Deduplicating Training Data、UniMax。其中 UniMax（05-057）已被 07 类（07-063）先认领 → 改为 `cross_only`，实际经典 4 篇。
- 05-062（2610.11585）首作者姓 Sabolčec 被 pypdf 抽为 “Sabolˇ cec” 导致软检查失败；已用 `text` 核对首页标题、作者行与摘要后 `manual` 提升。
- 首轮 `--target 55` 在主列表经典条目处停止；第二轮以 `--target 66` 补下载追加的主列表条目（05-062~065、05-067~071），因 UniMax 重复且 05-062 暂为 pending，又顺序下载了备选 05-058（奥摩语词级 LID）、05-059（PolyLingua），均为直接相关。
- 未下载备选：05-060 NusaAksara（基准，可能属 15）、05-061 Perplexed by Perplexity、05-066 平行语料源端筛选、05-072 OmniOCR、05-073 满文 OCR、05-074 先验噪声过滤、05-075 埃及阿拉伯语维基模板翻译检测、05-076 FastSpell、05-077 葡萄牙语语料。
- 与兄弟库（large_model_multimodal_literature 02 类）重叠的通用支撑论文（FineWeb、DCLM、Nemotron-CC、LSHBloom、Data selection survey、BDC survey、Dedup、Mix-MinHash-Match 等）由脚本复制并重新核验，记“已有复用”。
- 刻意不收：数据混合/配比的训练侧研究（RegMix、Data Mixing Laws 等，属 07）；合成/翻译预训练数据（TransWebEdu、BhashaKritika，属 09）；纯评测基准（MEGAVERSE、GreekMMLU，属 15）；隐私泄露与成员推断（属 10）。
- 污染：以“数据流水线中的污染检测”为主线的论文放本类并加 cross 15。

## 4. 未完成/疑点
- 去重方向缺少专门针对低资源/多语言的近三年论文（仅 Mix-MinHash-Match、BREAD 冗余检测、SomaliWeb 中的重复统计），覆盖偏薄。
- 毒性/PII 多语言过滤方向的近三年专门论文较少。
- 05-009 ÜberWeb 为公司技术报告（DatologyAI），实验细节以作者自报为准。


---

<!-- 来源：scripts/work/search_log_06_cn.md -->

# 检索日志：06 分词、词表与模型架构（tokenization_vocab_arch）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search '<查询>' --max N --sort relevance`（arXiv export API）；结合已有知识列出候选，`resolve` 核对（88 条中 0 处 ID 纠错；06-028 标题按 arXiv 实际标题改为 *Adapting Chat Language Models Using Only Target Unlabeled Language Data*）。
- 近三年窗口：首次公开 ≥ 2023-10-29（下表 `<D>` = `submittedDate:[202310290000 TO 202610290000]`）。

## 1. 查询式与返回数（原样）

| # | 查询式 | max | 返回 | 主要选入 |
|---|---|---|---|---|
| 1 | `(ti:Tokenization OR ti:tokenizer OR ti:tokenizers) AND (abs:multilingual OR abs:languages) AND <D>` | 50 | 50 | Token Tax（2509.05486）、One Tokenizer To Rule Them All、MUTANT、Parallel Tokenizers、Modular Tokenizers、Indian Tokenizer Tax（2607.24276）、Tokenization & Morphology mT5/ByT5、Swahili 音节分词、Equity with Efficiency、Accelerating…Excessively Tokenized、MAGNET；备选：Qtok、土耳其混合分词、Beyond Literal Token Overlap、Art of Breaking Words、印度语言分词综述 |
| 2 | `abs:"vocabulary expansion" OR abs:"vocabulary extension" OR abs:"vocabulary adaptation" AND <D>` | 40 | 40 | 0.01GB 词表扩展、VocADT、俄语 LEP（备选）、意大利语（未选）、Exploring Design Choices、渐进式词表扩展（阿拉伯语）、爱沙尼亚语词表裁剪（备选）、嵌入初始化策略比较（备选）、俄语分词影响、吉兹文词表扩展、定制分词器（备选）、像素回退 |
| 3 | `(abs:"embedding initialization" OR abs:"tokenizer transfer" OR abs:"cross-lingual vocabulary") AND <D>` | 30 | 30 | Model-Aware Tokenizer Transfer（备选）、词典驱动词表迁移、Trans-Tokenization、ANGOFA、HYPEROFA（备选）、LGSE（备选）、Bilingual Adaptation of Monolingual FM、UniBridge（未选） |
| 4 | `(ti:byte OR ti:"token-free" OR ti:"tokenizer-free" OR ti:character-level) AND abs:"language model" AND <D>` | 40 | 40 | MambaByte、T-FREE（备选）、H-Net++、Toucan（备选）、BanglaByT5、Bit-level BPE、Measuring Cross-lingual Transfer in Bytes |
| 5 | `(abs:"mixture of experts" OR abs:"mixture-of-experts") AND abs:multilingual AND abs:"language-specific" AND <D>` | 30 | 11 | Group then Scale、Multilingual Routing in MoE、MoE 多语言机制（备选） |
| 6 | `(abs:romanization OR abs:transliteration OR abs:script) AND abs:"non-Latin" AND abs:"language model" AND <D>` | 30 | 30 | 转写与 ICL、One Script Instead of Hundreds（备选）、可逆转写（Huffman）、BPE Stays on SCRIPT（备选）、Multilingual Pixel LM、Tokenization Disparities as Infrastructure Bias（备选）、字节分块零样本迁移（备选）、尼泊尔语分词（备选） |
| 7 | `(ti:Uyghur OR ti:Mongolian OR …)` 等 03 的语种检索中顺带发现 | — | — | KazByte（2603.27859，哈萨克语字节适配器）、尼泊尔语形态预分词（2609.33395，未选） |
| 8 | `abs:"Southeast Asian" AND abs:"language model" AND <D>`（03 检索） | 30 | 30 | Equity with Efficiency（2606.15044） |
| 9 | `abs:"African languages" AND abs:"language model" AND <D>`（03 检索） | 30 | 30 | The African Language Tax（2606.24460） |

已有知识补充（resolve 核对一致）：Parity-aware BPE、MYTE、Splintering、MorphScore 两篇、Tokenization Is More Than Compression、EEVE、Efficiently Adapting Pretrained LMs to New Languages、Cross-lingual Vocabulary Adaptation 实证、ElChat、ZeTT、OFA、Large Vocabulary Size、Scaling Laws with Vocabulary、DictaLM 2.0、TokAlign、BLT、SpaceByte、MrT5、HAT、H-Net、RomanSetu、TransliCo、Breaking the Script Barrier、LangSAMP、MoE-LPR、DEPT，以及经典 Petrov 等（2305.15425）、Ahia 等（2305.13707）、FOCUS、WECHSEL、ByT5。

## 2. 选入与排除原则
- 选入：分词效率/token 税/分词公平；形态与文字对分词和建模的影响；词表扩展、替换与嵌入初始化；分词器迁移；字节/字符/像素级无分词方法；转写/罗马化与文字障碍；多语言 MoE 与语言/文字特定模块。
- `通用支撑`：只在英语上验证但对小语种分词/架构选择有直接借鉴者（Tokenization Is More Than Compression、Scaling Laws with Vocabulary、MambaByte、BLT、SpaceByte、HAT、H-Net、T-FREE、DEPT、Large Vocabulary Size、Toucan），注释中写明用途。
- 排除：领域词表适配（医疗、化学，与小语种无关）；语音/视觉 tokenizer；跨分词器蒸馏（2503.20083，偏 09）；意大利语词表适配（2504.17025，高资源，未选）。

## 3. 认领冲突与替代
- 被其他类先认领（均改为 `cross_only` 并写 cross_reason，由主列表后续条目补足）：06-025 *Efficiently Adapting Pretrained Language Models To New Languages*（07-005）、06-028 *Adapting Chat Language Models Using Only Target Unlabeled Language Data*（07-066）、06-029 *Exploring Design Choices for Building Language-Specific LLMs*（07-056）、06-040 *Bilingual Adaptation of Monolingual Foundation Models*（07-029）、06-071 *MoE-LPR*（07-044）、06-066 *Exploring the Role of Transliteration in ICL for LRL in Non-Latin Scripts*（08-032）。
- 06-079 ByT5（经典）改为 reserve，未下载，以把三年前文献控制在 4 篇。

## 4. 下载与核验
- `download 06 --target 55` → 55 已核验；随后 `--target 57` 补下经典 FOCUS、WECHSEL（嵌入初始化方法的标准基线）。
- 已有复用（从兄弟库复制并重新核验）4 篇：06-013、06-047、06-051、06-055。
- 无 pending、无失败，未使用 `manual`。
- 最终：已核验 57；待核验 0；失败 0；近三年 53/57 = 93.0%；经典 4 篇（Petrov 等 2305.15425、Ahia 等 2305.13707、FOCUS、WECHSEL，均写 old_reason）。
- 疑点：06-063 KazByte 为“技术公告”，作者称实证验证仍在进行、无实验结果，仅可作设计参考；06-043 吉兹文词表扩展的 arXiv v4 注释称替换了 v1/v2 中无法追溯到实验输出的全部结果，结论与早期版本不同，引用须以 v4 为准。

## 5. 未完成/缺口
- 维吾尔文、蒙古文、藏文等中国少数民族文字的专门分词研究：仅 2509.17493（可逆转写）间接涉及；缺专门藏文/蒙古文分词论文。
- 美洲原住民语言分词研究缺失。


---

<!-- 来源：scripts/work/search_log_07_cn.md -->

# 检索日志：07 预训练与持续预训练（pretraining_continual）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search`（arXiv API），近三年窗口 `submittedDate:[202310290000 TO 202610290000]`（下记为 $D）；另结合已有领域知识补充经典与代表论文（均经 `resolve` 按 arXiv 元数据核对标题）。

## 查询式（原样）与返回数

| # | 查询式 | 返回 | 选入（种子 sid/arXiv） |
|---|---|---|---|
| 1 | `abs:"continual pre-training" AND abs:language AND abs:"low-resource" AND $D` | 40 | 2409.17892, 2506.00469, 2407.03994, 2410.14815, 2507.09205, 2405.13010, 2508.09115, 2411.02460, 2412.10244, 2601.08141, 2510.22747(备) |
| 2 | `abs:"continued pretraining" AND abs:"new language" AND $D` | 8 | 2509.11414, 2506.00288, 2407.02118 |
| 3 | `abs:"catastrophic forgetting" AND abs:"language adaptation" AND $D` | 7 | 2407.08699, 2601.01244, 2510.13580(备) |
| 4 | `abs:"model merging" AND abs:"low-resource" AND abs:language AND $D` | 10 | 2502.09056, 2601.10804, 2510.00810 |
| 5 | `abs:"continual pre-training" AND abs:replay AND abs:language AND $D` | 14 | 2508.01908, 2505.07796, 2407.17467, 2403.08763, 2608.30609(备), 2608.17530(备), 2503.05029(备) |
| 6 | `ti:"continual pre-training" AND abs:multilingual AND $D` | 7 | 2404.00399, 2601.06395, 2403.15470(备) |
| 7 | `abs:"from scratch" AND abs:pretraining AND abs:"low-resource language" AND $D` | 11 | 2311.05741, 2401.18034, 2512.10545, 2608.30092(备), 2603.20732(备), 2603.03508(备), 2606.06738(备) |
| 8 | `abs:"data mixture" AND abs:multilingual AND abs:pretraining AND $D` | 7 | 2510.25947 |
| 9 | `abs:"language adaptation" AND abs:LLM AND abs:pretraining AND $D` | 11 | 2412.07633, 2502.11187, 2408.15793（判归 06，未选） |
| 10 | `ti:merging AND abs:"cross-lingual" AND $D` | 8 | 2505.18356（2402.18913 转入 08） |
| 11 | `abs:"parallel data" AND abs:"continual pre-training" AND $D` | 7 | 无新增（2407.03145 偏机器翻译，归 09 更合适，未选） |
| 12 | `abs:"continued pretraining" AND abs:"English data" AND abs:forgetting AND $D` | 1 | 与 #2 重复 |
| 13 | `ti:"from scratch" AND abs:language AND abs:model AND abs:monolingual AND $D` | 0 | — |
| （08 检索中顺带） | `abs:"language adapters" AND abs:LLM AND $D` | 40 | 2404.05829 SambaLingo, 2402.09759, 2412.11704, 2412.04277 |

知识补充（非检索命中，resolve 核对）：2308.04014、2304.09151、2310.04799、2212.09535（经典，均写 old_reason）、2404.17790、2401.01055、2405.12413、2412.06484、2412.12956、2311.05640、2407.12869、2403.01851、2402.17400、2401.03129、2402.01364、2406.14833、2407.07263、2404.06395、2406.14670、2411.11171、2402.00786、2410.01335、2408.11396 等。

## 选入 / 排除原则
- 选入：方法核心为持续预训练/从零预训练/数据混合与重放/学习率调度/遗忘缓解/模型合并式语言适配；或小语种从零/持续预训练案例报告。
- 排除或转出：词表扩展与嵌入初始化为主（2311.08849 OFA、2406.11477、2407.05841、2408.15793、2506.10766 → 06）；机器翻译为主（2407.05975 LLaMAX、2407.03145、2410.07830 → 09）；语音/编码器分类任务（2402.02302、2409.08872 等）；与语言无关的领域 CPT（2609.31871 等）。

## 结果与替代关系（下载后）
- `download 07 --target 55`：主列表 55 条中 53 条直接核验通过；07-067（波兰语 LAPT）因首作者姓氏变音符抽取为 `Ruci´nski` 落入 pending，经 `text` 核对首页标题/作者/摘要后 `manual` 提升；07-059 SinLlama 被 03 类（03-072）先行认领 → 改为 cross_only；由备选 07-071（方言扰动 CPT）、07-072（MoE 路由与语言适配）自动补足。
- 最终：已核验 56，近三年 52/56 = 92.9%，三年前经典 4 篇（07-002、07-063、07-064、07-070，均写 old_reason）。直接相关 46 / 通用支撑 10。
- 让出给别类（cross_only，共 20）：01 类先列入的 2410.12883、2405.18392、2404.07982、2311.09205、2404.16789、2501.13453；03 类先列入的 EMMA-500、Goldfish、X-ELM、Sailor、InkubaLM、Lugha-Llama、Paramanu、Latxa、UCCIX、Poro、Llammas、Meltemi、藏语 CPT、SinLlama。
- 备选未用（reserve，21 条）保留在种子中供后续补位。
- 种子修正：07-077 RakutenAI-7B 原题写错（resolve 未解析），已按 arXiv 标题改正（备选，未下载）；07-033 选入理由去除未核实的“繁体中文/Llama-2-chat”细节。
- 未完成/缺口：小语种从零预训练小模型案例（07-075 尼泊尔语、07-076 葡萄牙语等）仅在备选；“学习率重热”直接针对语言迁移的研究较少，主要依赖 07-001/07-002 通用证据。


---

<!-- 来源：scripts/work/search_log_08_cn.md -->

# 检索日志：08 指令微调与参数高效适配（instruction_tuning_peft）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search`（arXiv API），近三年窗口 `submittedDate:[202310290000 TO 202610290000]`（下记为 $D）；结合领域知识补充（均经 `resolve` 核对标题）。

## 查询式（原样）与返回数

| # | 查询式 | 返回 | 选入 |
|---|---|---|---|
| 1 | `abs:"instruction tuning" AND abs:multilingual AND abs:"cross-lingual transfer" AND $D` | 14 | 2504.16677, 2402.14778, 2404.04850, 2312.12683, 2606.10428, 2605.29414, 2502.08037 |
| 2 | `abs:"instruction" AND abs:dataset AND abs:"low-resource languages" AND abs:LLM AND $D` | 40 | 2502.13647, 2510.24434, 2508.15239, 2506.07597, 2410.21200, 2401.07598, 2504.09753(备)；2409.12958/2512.02213/2402.08015/2409.17912 已被 09/03 列入 → cross_only |
| 3 | `abs:LoRA AND abs:"low-resource language" AND $D` | 40 | 2411.18571, 2407.11186；2404.06138 已被 03 列入 → cross_only |
| 4 | `abs:"language adapters" AND abs:LLM AND $D` | 40 | 2412.12674, 2410.16006, 2312.09993；2404.05829/2412.11704/2402.09759 转入 07 |
| 5 | `abs:"in-context learning" AND abs:"low-resource languages" AND abs:"few-shot" AND $D` | 15 | 2508.19089, 2506.19187, 2403.06018, 2407.02320, 2403.01929, 2508.19464(备), 2403.00411(备), 2410.06898(备)；2403.16512 已被 01 列入 → cross_only |
| 6 | `abs:"instruction tuning" AND abs:"how many languages" AND $D` | 0 | —（相关论文已由 #1 与知识补充覆盖） |
| 7 | `abs:"parameter-efficient" AND abs:multilingual AND abs:"low-resource" AND $D` | 40 | 2407.01406, 2502.10140, 2510.24619, 2512.07454, 2601.16629(备), 2507.03003(备), 2502.04387(备), 2311.07820(备), 2408.03172(备) |
| （07 检索中顺带） | `ti:merging AND abs:"cross-lingual" AND $D` | 8 | 2402.18913 AdaMergeX |
| （07 检索中顺带） | `abs:"model merging" AND abs:"low-resource" AND abs:language AND $D` | 10 | 2603.28263 |

知识补充（resolve 核对）：2402.06619 Aya Dataset、2401.01854、2402.13703、2309.08958、2211.01786、2106.09685、2305.14314（经典，写 old_reason）、2402.09353、2405.09673、2403.14608、2412.13922、2401.15006、2406.19167、2311.08711、2405.13816、2401.16405、2402.12354、2404.02948、2312.03732、2311.08572、2404.09138、2402.18766、2406.17377、2412.12499、2501.06892、2311.09344、2402.12976、2410.21228、2311.17487(备)。

## 选入 / 排除原则
- 选入：本地语言指令数据构造、多语/跨语言指令迁移（指令语言数量、仅英文指令迁移）、LoRA/QLoRA/DoRA 等 PEFT 及其在小语种上的比较、语言适配器/适配器合并、少样本与上下文学习教新语言。
- 让出（cross_only）：别类已先列入的 Bactrian-X（09）、MURI/InstructLR/“翻译 vs 原生指令数据”（09，翻译/合成指令归 09）、Cendol/Walia/Atlas-Chat/Aya Model（03）、LLMs Are Few-Shot In-Context Low-Resource Language Learners（01）。
- 排除：语音 ASR 适配（2410.13445、2406.06329 等）、仅编码器分类小任务（仇恨言论等）、安全/越狱（归 10）、多模态（2512.14926）。
## 补充检索（下载进行中，补备选）

| # | 查询式 | 返回 | 选入 |
|---|---|---|---|
| 8（补备选） | `ti:"instruction tuning" AND abs:multilingual AND $D` | 30 | 08-076 2406.08796、08-077 2503.01611、08-078 2511.10229、08-079 2404.11932（均为备选；2410.07809 已在 02 类种子中，未加） |
| 9（补备选） | `abs:"language-specific" AND abs:LoRA AND abs:multilingual AND $D` | 24 | 无新增（多为语音 ASR 或已选论文） |

## 结果与替代关系（下载后）
- `download 08 --target 55`：已核验 55，待核验 0，失败 0；近三年 51/55 = 92.7%；三年前经典 4 篇（08-008、08-009、08-010、08-011，均写 old_reason）。直接相关 45 / 通用支撑 10。
- 已有复用（兄弟库已核验 PDF 复制后重新核验）：08-010 LoRA、08-011 QLoRA、08-012 DoRA、08-013、08-014、08-041、08-042、08-057，共 8 篇。
- 替代：08-046（乌克兰语 From Bytes to Borsch）下载时已被 03 类（03-075）认领 → duplicate_elsewhere，改 cross_only，由备选 08-058 Taiwan LLM 补位。
- 种子修正：08-033 原 arXiv 号写错（2406.19167→2402.19167），改正后发现已被 09 类认领（09-003）→ cross_only；08-031（Toukmaji 学士论文）与 08-030 为同作者同主题前后版本 → exclude；08-023 选入理由更正为冰岛语（原误写瑞典语）；08-059 已在 02 类种子中 → cross_only。
- 让出给别类（cross_only，共 11）：01（2403.16512）、03（Cendol、Walia-LLM、Atlas-Chat、From Bytes to Borsch）、09（Is It Good Data…、MURI、InstructLR、Bactrian-X、Teaching LLMs an Unseen Language on the Fly）、02（Typologically Informed Parameter Aggregation）。
- 缺口：语言专属 LoRA/语言适配器在生成式 LLM 上的系统研究较少（08-025/08-026 基座为编码器类）；“仅英文指令迁移”的低资源语言（非欧洲语言）证据仍有限。


---

<!-- 来源：scripts/work/search_log_09_cn.md -->

# 检索日志 · 09 合成数据、翻译与蒸馏（synthetic_translation_distill）

- 检索日：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 工具：`python3 -I scripts/papers_en.py search '<查询> AND submittedDate:[202310290000 TO 202610290000]' --max 30|40`（arXiv API，按相关度排序），并结合已知文献按标题回查（`resolve` 按标题纠正 ID）。
- 原始返回保存在会话暂存区（不入库）；下表“返回数”为该查询实际返回条数。

## 一、查询式与返回

| # | 查询式（均另加 `AND submittedDate:[202310290000 TO 202610290000]`） | 返回 | 选入（sid） |
|---|---|---|---|
| Q1 | `abs:"low-resource" AND abs:"machine translation" AND abs:"large language models"` | 40 | 09-004, 09-016(备), 09-018, 09-022, 09-024, 09-029(备), 09-065(备), 09-066(备) |
| Q2 | `abs:"grammar book" AND abs:translation` | 9 | 09-001, 09-003, 09-004, 09-005, 09-006, 09-007, 09-008, 09-009 |
| Q3 | `abs:"translationese" AND abs:"large language model"` | 7 | 09-057, 09-058, 09-059 |
| Q4 | `abs:"back-translation" AND abs:"low-resource" AND abs:LLM` | 11 | 09-023, 09-031(备) |
| Q5 | `abs:"synthetic data" AND abs:"low-resource languages" AND abs:instruction` | 8 | 09-035, 09-036, 09-037, 09-046, 09-054 |
| Q6 | `abs:"translated" AND abs:"instruction" AND abs:multilingual AND abs:"native"` | 20 | 09-033, 09-034, 09-040, 09-047(备) |
| Q7 | `abs:"cross-lingual" AND abs:distillation AND abs:"low-resource"` | 13 | 09-041, 09-025, 09-055, 09-071(备) |
| Q8 | `abs:"dictionary" AND abs:"in-context" AND abs:"low-resource" AND abs:translation` | 16 | 09-010, 09-011, 09-012, 09-015(备) |
| Q9 | `abs:"machine-translated" AND abs:"instruction" AND abs:"low-resource"` | 27 | 09-026, 09-013, 09-017(备), 09-030(备), 09-063, 09-070(备) |
| Q10 | `abs:"translate-train" AND abs:LLM` | 15 | 09-042, 09-043, 09-044 |
| Q11 | `abs:"synthetic" AND abs:"machine translation" AND abs:"low-resource" AND abs:LLM` | 24 | 09-019, 09-020, 09-021, 09-027, 09-050, 09-051(备), 09-062(备), 09-072(备) |
| Q12 | `abs:"distillation" AND abs:"multilingual" AND abs:"instruction" AND abs:"teacher"` | 8 | （0；2602.11157 归 10 类） |
| Q13 | `abs:"machine translated" AND abs:"benchmark" AND abs:"translationese"` | 2 | 09-060 |
| Q14 | `abs:"self-instruct" AND abs:multilingual` | 2 | （Alif 已由 Q6 选入） |
| Q15 | `abs:"translated data" AND abs:"native data" AND abs:"language model"` | 1 | 09-052(备) |
| Q16 | `abs:"quality estimation" AND abs:"filtering" AND abs:"low-resource" AND abs:"synthetic"` | 0 | — |
| Q17 | `abs:"MTOB" OR abs:"Machine Translation from One Book"` | 4 | 09-014（经典） |
| Q18 | `abs:"African languages" AND abs:"machine translation" AND abs:"LLM"` | 8 | 09-067 |

## 二、按标题回查的已知文献（非检索命中）
09-028 X-ALMA、09-032 回译原始论文（Sennrich 2015，经典）、09-045 Multilingual Arbitrage、09-048 Fineweb-Edu-Ar（Q1 亦命中）、09-049 TransWebEdu（种子只给标题，`resolve` 回写 2502.13252）、09-053 Bactrian-X（经典）、09-056 Translation Errors…Low-Resource、09-064 SMOL、09-068 Tower、09-069 In-context Example Generation（Q1 命中）、09-061、09-073。

## 三、主要排除及原因
- 纯评测/基准（IrokoBench、SSA-COMET、AFRIDOC-MT、BenchMAX、IndicIFEval、Batayan、GlotEval 等）：归 15 类或 04 类，非本类核心。
- 原生构建的本地语言指令数据（如 Konkani LLM、UrduLLaMA、Aya Dataset）：按分工归 08 类。
- 与低资源无关的 MT 工程/比赛报告（In2x WMT25、Qwen-MT-Lumen、FuxiMT、Index-Translate 等）、多模态/OCR/语音翻译、代码翻译：主题不符。
- 安全/毒性相关的蒸馏与翻译检测（2602.11157、2509.14493、2507.11966）：移入 10 类处理。
- 子方向“合成数据验证与过滤”专门检索（Q16）0 命中，相关证据主要来自 09-019、09-036、09-037、09-046 等论文中的过滤步骤，属缺口。

## 四、替代关系与未完成
（下载完成后补记，见文末“下载结果”。）

## 五、下载结果（2026-10-29）
- `resolve 09`：72 条查询元数据，1 条按标题回写 ID（09-049 → 2502.13252，标题相似度 1.00），无未解析条目。
- `download 09 --target 55`：主列表 57 条 + 备选 2 条（09-015、09-016，在 Mufu 进入待核验后被递补）下载核验；无下载失败，无与其他类别重复认领。
- 09-014（MTOB）：自动检查未找到参考文献标题（字体拆字为 “REFERENC ES”），用 `text` 核对首页标题/首作者并定位参考文献节后 `manual` 提升。注意：首次 `manual` 在下载进程运行期间执行，被下载进程覆盖回 pending，下载结束后重做（见报告“脚本问题”）。
- 09-025（Mufu，2409.13949）：标题匹配 0.00；`text` 命令在第 1 页即因 pypdf `_type1_alternative` 报 `UnboundLocalError` 崩溃，无法人工核对首页，按规则保持 pending、不计数（作者检查在后页命中，应为正确论文）。
- 备选 09-017、09-029～031、09-039、09-047、09-051、09-052、09-061、09-062、09-065、09-066、09-070～073 未下载（主列表已达标）。
- 最终：已核验 56（近三年 53/56 = 94.6%；经典 3：MTOB、回译原始论文、Bactrian-X）；直接相关 52，通用支撑 4（09-032 回译、09-057 翻译腔成因、09-059 评审翻译腔偏差、09-068 Tower）。

## 六、缺口
- “合成数据验证与过滤”专题论文少，现有证据分散在 09-019（人工质量评估）、09-036（1 万次人工评估）、09-037（RAG 过滤+人工在环）、09-046（KenLM 等过滤流水线）、09-067（QE 过滤）中。
- 非洲、美洲原住民语言的“教师模型生成本地数据”实证仍以作者自报为主，缺独立复现。
- 翻译腔研究（09-057、09-058）多基于高资源语言，低资源语言上的翻译腔证据主要来自 09-059、09-060。


---

<!-- 来源：scripts/work/search_log_10_cn.md -->

# 检索日志 · 10 偏好对齐与安全（preference_alignment_safety）

- 检索日：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 工具：`python3 -I scripts/papers_en.py search '<查询> AND submittedDate:[202310290000 TO 202610290000]' --max 30`（arXiv API，按相关度排序）；另按标题回查已知文献（`resolve` 按标题纠正 ID）。
- 原始返回保存在会话暂存区（不入库）；下表“返回数”为实际返回条数。

## 一、查询式与返回

| # | 查询式（均另加 `AND submittedDate:[202310290000 TO 202610290000]`） | 返回 | 选入（sid） |
|---|---|---|---|
| R1 | `abs:"multilingual" AND abs:"preference optimization"` | 30 | 10-001, 10-008, 10-011(备), 10-012, 10-013(备), 10-014(备), 10-019, 10-024(备), 10-064；MAPO 见下 |
| R2 | `abs:"reward model" AND abs:"multilingual"` | 30 | 10-003, 10-004, 10-005, 10-009, 10-015, 10-016(备), 10-017, 10-018(备), 10-076, 10-077(备) |
| R3 | `abs:"jailbreak" AND abs:"low-resource languages"` | 16 | 10-041, 10-042, 10-043, 10-044, 10-045, 10-048, 10-050, 10-051(备), 10-055, 10-057(备) |
| R4 | `abs:"multilingual" AND abs:"safety" AND abs:"red-teaming"` | 12 | 10-040, 10-053, 10-054 |
| R5 | `abs:"cultural alignment" AND abs:"large language models"` | 30 | 10-071, 10-072, 10-073, 10-079(备), 10-080, 10-081(备), 10-078(备) |
| R6 | `abs:"multilingual" AND abs:"toxicity" AND abs:"large language models"` | 28 | 10-049, 10-052, 10-062(备), 10-065, 10-066, 10-067, 10-068, 10-069, 10-059, 10-061 |
| R7 | `abs:"cross-lingual" AND abs:"alignment" AND abs:"RLHF"` | 6 | 10-037, 10-063(备) |
| R8 | `abs:"safety" AND abs:"African languages" AND abs:LLM` | 8 | 10-058, 10-060(备), 10-089(备) |
| R9 | `abs:"reinforcement learning" AND abs:"verifiable" AND abs:"multilingual"` | 30 | 10-025, 10-026, 10-027(备), 10-023(备) |
| R10 | `abs:"guardrail" AND abs:"multilingual"` | 30 | 10-084, 10-085, 10-086, 10-090(备) |
| R11 | `abs:"DPO" AND abs:"low-resource"` | 19 | 10-083, 10-091(备) |
| R12 | `abs:"culturally" AND abs:"low-resource" AND abs:"alignment"` | 30 | 10-047, 10-075, 10-087(备), 10-088 |
| R13 | `ti:CARE AND abs:cultural AND abs:preference`（不加日期，补查 10-074 正确 ID） | 3 | 10-074（2504.05154；原题名记忆有误，已按 arXiv 题名更正） |

## 二、按标题回查的已知文献（非检索命中或命中前已列入）
10-002 Multilingual Alignment Prism、10-007 Language Imbalance Driven Rewarding（`resolve` 回写 2410.08964）、10-010 IndoPref、10-020 Teaching LLMs to Abstain across Languages、10-022 CPO、10-028 InstructGPT（经典）、10-029 DPO（经典）、10-030 KTO、10-031 ORPO、10-032 Tülu 3（备）、10-033 Okapi（经典）、10-034 Low-Resource Languages Jailbreak GPT-4（经典）、10-035 MultiJail（经典）、10-036、10-038（备）、10-039、10-046、10-070 CultureLLM、10-082 NormAd（备）。

## 三、交叉与排除
- 10-006 MAPO：11 类主列表已列（11-011），本类改为 `cross_only`。
- 10-021 Aya Expanse：已由 03 类认领（03-004），本类改为 `cross_only`。
- 纯文化/安全评测基准（BLEnD、CulturalBench、SinhalaMMLU、WangchanThaiInstruct、DRISHTIKON 等）：归 15 类；仅保留明确与“对齐/安全/偏好”直接相关的基准（M-RewardBench、MultiJail、RabakBench、TukaBench、SEA-SafeguardBench、Pak3H 等），并在种子写 cross 15。
- 多模态/语音偏好对齐（Align2Speak、TTS 偏好对齐、Han-Nom 图像翻译 RLHF、Lingua-SafetyBench）、代码奖励模型、通用智能体红队：与小语种文本对齐主题不符，排除。
- 本地语言模型发布报告（NileChat、Compass、FuxiTranyu、CantoneseLLM v2、EstLLM）：归 03/07 类。
- 机器翻译偏好优化（CPO 选入作通用支撑；DQO、Trans-Zero 作备选），其余 MT-RL 工作（MT-R1-Zero、DeepTrans、ExTrans）归 09/11 类讨论，未选。

## 四、排序与通用支撑
- 种子按优先级（高→中→低）排序后下载；主列表 64 条、备选 25 条、cross_only 2 条。
- 通用支撑：InstructGPT、DPO、KTO、ORPO（方法来源）、CPO（翻译偏好优化）、HelpSteer3-Preference 与 Tülu 3（备选）。

## 五、下载结果（2026-10-29）
- `resolve 10`：87 条查询元数据；10-007 按标题回写 2410.08964；10-074（CARE）首次未解析（种子题名为记忆中的旧题名），经 R13 检索确认 2504.05154 并更正题名后解析成功。
- `download 10 --target 55`：按优先级下载 56 条，55 条核验通过（其中 4 条为兄弟库已核验 PDF 复制后重新核验：10-028 InstructGPT、10-029 DPO、10-030 KTO、10-031 ORPO，记“已有复用”）。
- 10-061（Bridging the Multilingual Safety Divide，2602.13867）：失败——PDF 仅 2 页、可抽取 11076 字符（AAAI 研讨会短文/扩展摘要），不满足 ≥4 页与 ≥12000 字符，不计数，未找替代全文。
- 为补足“文化对齐”子方向，追加 `download 10 --target 63`，主列表剩余 8 条（10-074/075/076/080/084/085/086/088）全部核验通过。
- 最终：已核验 63，近三年 58/63 = 92.1%，经典 5（InstructGPT、DPO、Okapi、Low-Resource Languages Jailbreak GPT-4、MultiJail，均写 old_reason）；直接相关 58、通用支撑 5（InstructGPT、DPO、KTO、ORPO、CPO）。
- 备选 25 条未下载；cross_only 2 条（10-006 MAPO→11、10-021 Aya Expanse→03）。

## 六、缺口与疑点
- RLVR 多语言仅 2 篇（10-025、10-026），且后者只涉及日/英/中，低资源语言 RLVR 证据缺乏。
- 原生（非翻译）偏好数据仅少数：10-010 IndoPref、10-017 MENLO、10-074 CARE、10-002 红队提示；多数多语言偏好/安全数据依赖机器翻译或模型合成。
- 多语言安全基准多为翻译构造（MultiJail、M-RewardBench、HarmBench/AdvBench 译本），原生构建的有 10-084、10-055（部分）、10-059、10-088；10-043 显示误译会制造“伪安全差距”。
- 10-034、10-035 发表于窗口前 4 周内，按规则计为经典补充，已占满 5 篇上限。


---

<!-- 来源：scripts/work/search_log_11_cn.md -->

# 检索日志：11 推理、长上下文与工具调用（reasoning_longctx_tools）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API）+ 已有知识（经 `resolve` 按 ID/标题核对）
- 近三年窗口：首次公开 ≥ 2023-10-29；查询中统一加 `submittedDate:[202310290000 TO 202610290000]`（下记为 `$D`）

## 1. 查询式（原样）与返回

| # | 查询式 | 排序 | 返回 | 选入（种子 sid） |
|---|---|---|---|---|
| Q1 | `abs:multilingual AND abs:reasoning AND abs:"chain-of-thought" AND $D` | relevance | 40 | 11-012 mCoT、11-013 AdaMCoT、11-027 多语言 CoT 综合评测、11-031 PoT 跨语言、11-036 MathMist、11-075 跨语言一致性推理（xCoT/QAlign/test-time scaling 同时命中） |
| Q2 | `abs:multilingual AND abs:"reasoning models" AND $D` | relevance | 40 | 11-016 思考语言控制、11-015 Language Matters、11-017 长 CoT 跨语言、11-018 Think Natively、11-019 Reasoning Lingua Franca、11-029 潜在推理、11-032 EfficientXLang、11-035 Reasoning Gym、11-037 推理迁移、11-076 推理轨迹特征；备选 11-071 ExpLang、11-072 x1、11-078 AdaMame |
| Q3 | `(abs:"function calling" OR abs:"tool calling" OR abs:"tool use") AND (abs:multilingual OR abs:"low-resource" OR abs:"cross-lingual") AND $D` | relevance | 40 | 11-051 Lost in Execution、11-052 国际工具调用数据、11-053 Ticket-Bench、11-054 阿拉伯语工具调用、11-055 保加利亚语工具语言、11-056 函数调用多语言翻译、11-057 PolyWorkBench、11-058 Think in English Answer in Korean、11-059 BabelArena；备选 11-066 M-SQE |
| Q4 | `abs:"long-context" AND (abs:multilingual OR abs:"low-resource") AND $D` | relevance | 40 | 11-043 MLNeedle、11-044 多语言长上下文检索与推理、11-045 ONERULER、11-046 MLRBench、11-047 印度语言长文问答；备选 11-069 MGAL、11-068 神经符号多语言推理 |
| Q5 | `(abs:"structured output" OR abs:"JSON" OR abs:"constrained decoding") AND (abs:multilingual OR abs:"low-resource" OR abs:languages) AND $D` | relevance | 30 | 11-049 JSONSchemaBench（通用支撑）；备选 11-073 The Format Tax。结果中多语言结构化输出专门研究很少（多为跨语言标签投影/ABSA 的约束解码，属别类），记为缺口 |
| Q6 | `(abs:"logical reasoning" OR abs:logic) AND (abs:multilingual OR abs:"low-resource language") AND $D` | relevance | 30 | 11-026 MultiNRC、11-023 多语言推理综述；备选 11-074 BanglaMATH。多语言形式逻辑专门基准较少，未单独凑数 |
| Q7 | `abs:"low-resource" AND abs:"mathematical reasoning" AND $D` | relevance | 30 | 11-024 濒危语言推理迁移、11-025 非洲语言数学推理、11-039 东南亚原生 CoT、11-040 PluraMath、11-041 跨语言自蒸馏；备选 11-080 僧伽罗/泰米尔数学 |

由已有知识直接列入并经 `resolve` 核对 ID 与标题（0 处纠正）：MGSM、CoT、XLT、Think Better in English（经典补充）、MathOctopus、xCoT、MindMerger、LangBridge、MAPO、MCLM、PolyMath、MMATH、Could Thinking Multilingually、Learn Globally Speak Locally、Knowledge-Free Reasoners、RULER、Let Me Speak Freely、APIGen、ToolACE、tau-bench、BenchMAX、Beg to Differ、CURE-Med 等。

## 2. 选入 / 排除原则
- 优先“直接相关”：多语言/跨语言/低资源语言的推理、长上下文、工具调用；通用方法（CoT、RULER、JSONSchemaBench、Let Me Speak Freely、APIGen、ToolACE）标“通用支撑”并写用途。
- 经典补充 4 篇（MGSM、CoT、XLT、Think Better in English），均写 `old_reason`。
- 排除：多模态 VQA 推理（LaV-CoT、印度语 VLM 推理审计等，偏多模态）、翻译专用推理（Seed-X、ExTrans、法律 MT，归 09）、安全类推理（ACTR、跨语言拒答电路，归 10）、代码检索（UNICS，归 14）、通用教育评测（IndicEval，归 15）、文化/修辞推理（BengaliFig，归 15）。
- 与别类重叠（先到先得，避免抢核心论文）：QAlign（09-044）、Do Llamas Work in English（01-039）、Do Multilingual LLMs Think In English（01-049）、Beyond English-Centric LLMs（01-050）→ 本类只写 `cross_only`（11-009/11-030/11-062/11-063），以 11-075~11-077 补足。2608.00533 在 09 为备选，本类作为主条目。

## 3. 替代关系与下载结果（下载后补记）
- `resolve 11`：78 条查询，0 处 ID 纠正，无未解析条目。
- 第一轮 `download 11 --target 55`：按种子顺序核验到 11-058 即达 55 篇；11-026（MultiNRC）因参考文献标题为法文排版 “Références” 未被自动识别 → pending。用 `text`/逐页抽取核对首页标题、首作者 Fabbri（Scale AI）、16 页正文完整、第 9 页起为参考文献后，`manual` 提升为 verified。
- 第二轮 `download 11 --target 62`：补齐主列表剩余 6 篇（11-059 BabelArena、11-060 APIGen、11-061 ToolACE、11-075 CLC、11-076 推理轨迹特征、11-077 CURE-Med），以覆盖工具调用数据合成与多语言智能体子方向；未动用备选（14 篇 reserve 均未下载）。
- 已有复用（兄弟库 /root/large_model_multimodal_literature 已核验 PDF 复制并重新核验）：11-002 CoT、11-048 RULER、11-060 APIGen、11-061 ToolACE。
- 下载失败 0；duplicate_elsewhere 0（重叠条目事先改为 cross_only）。
- 最终：已核验 62，近三年 58/62 = 93.5%，三年前 4 篇（均有 old_reason）；直接相关 56 / 通用支撑 6。

## 4. 未完成与缺口
- 多语言结构化输出（JSON/约束解码）专门研究稀少，目前只有通用支撑 2 篇（JSONSchemaBench、Let Me Speak Freely）；多语言 JSON 合规研究为缺口。
- 多语言形式逻辑（命题/一阶逻辑）基准未找到合适的近三年专门论文；BFCL 无 arXiv 版本，未收录。
- 长上下文方面缺少面向低资源语言的长上下文训练方法论文（现有均为评测）。
- 2026 年新论文（如 BabelArena、PolyWorkBench、PluraMath、COPSD）仅有 arXiv 预印本，结论待同行评审。


---

<!-- 来源：scripts/work/search_log_12_cn.md -->

# 检索日志：12 检索增强与本地知识（rag_local_knowledge）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API）+ 已有知识（经 `resolve` 核对 ID 与标题）
- 近三年窗口：首次公开 ≥ 2023-10-29；查询统一加 `submittedDate:[202310290000 TO 202610290000]`（下记 `$D`）

## 1. 查询式（原样）与返回

| # | 查询式 | 排序 | 返回 | 选入（种子 sid） |
|---|---|---|---|---|
| Q1 | `(abs:"retrieval-augmented" OR abs:RAG) AND (abs:multilingual OR abs:"cross-lingual" OR abs:"low-resource") AND $D` | relevance | 50 | 12-034 BordIRlines、12-036 多语言 RAG 策略、12-040 孟加拉语跨语言 ICL、12-042 CroSearch-R1、12-043 XProvence、12-035 XRAG、12-045 mRAKL、12-039 阿-英检索偏差、12-030 Not All Languages、12-038 语言漂移、12-037 上下文利用一致性、12-031 语言偏好、12-044 翻译质量标注；备选 12-069 孟加拉语农业 RAG、12-070 M4-RAG、12-077 孟加拉语医学 RAG |
| Q2 | `(abs:"embedding model" OR abs:"text embeddings") AND abs:multilingual AND $D` | relevance | 40 | 12-004 mE5、12-007 jina-v3、12-009 Gemini Embedding、12-010 Qwen3 Embedding、12-011 EmbeddingGemma、12-012 Llama-Embed-Nemotron、12-013 LUSIFER、12-014 MMTEB、12-018 Nomic MoE 嵌入、12-008 Arctic-Embed 2.0；备选 12-066 Swan/ArabicMTEB、12-067 KinyaEmbed、12-076 历史卢森堡语。单语言 MTEB（ruMTEB、PL-MTEB、FaMTEB、MTEB-French 等）未选入主列表，避免以单一中高资源语言基准凑数 |
| Q3 | `(abs:"cross-lingual retrieval" OR abs:"cross-language retrieval" OR abs:reranking) AND (abs:"low-resource" OR abs:African OR abs:multilingual) AND $D` | relevance | 40 | 12-021 低资源语言 LLM 重排序、12-019 阿姆哈拉语检索嵌入、12-025 NeuCLIRBench、12-026 CLIR 综述、12-046 跨语言 ODQA 预训练、12-060 AfrIFact；备选 12-068 列表式重排 |
| Q4 | `(abs:OCR OR abs:"document parsing") AND (abs:"low-resource" OR abs:multilingual) AND $D` | relevance | 30 | 12-050 PaddleOCR 3.0、12-051 MDPBench、12-052 多语言 OCR 噪声问答、12-053 RoundTripOCR；备选 12-071 DocAtlas |
| Q5 | `abs:"knowledge editing" AND (abs:multilingual OR abs:"cross-lingual") AND $D` | relevance | 17 | 12-054 检索增强多语言知识编辑、12-055 BMIKE-53、12-056 MLaKE、12-057 多语言知识编辑综述、12-058 Edit Once Update Everywhere |
| Q6 | `(abs:"fact verification" OR abs:"fact-checking" OR abs:citation OR abs:attribution OR abs:hallucination) AND (abs:multilingual OR abs:"low-resource") AND abs:retrieval AND $D` | relevance | 30 | 12-059 SemEval-2025 Task 7、12-063 多语言核查检索偏差；备选 12-075 答案归因 |
| Q7 | `(abs:"question answering") AND abs:"low-resource" AND (abs:retrieval OR abs:"knowledge base") AND $D` | relevance | 30 | 12-024 低资源跨语言 DPR 局限、12-065 PUGG 波兰语 KBQA；备选 12-074 印尼语自适应 RAG |
| Q8 | `abs:"information retrieval" AND abs:African AND $D` | relevance | 3 | 与 Q3 重合（AfrIFact、低资源 LLM 重排序） |
| Q9 | `abs:"SWIM-IR"` / `ti:"Synthetic" AND ti:"Multilingual" AND ti:"Retrieval" AND au:Thakur` | relevance | 0 / 1 | 用于纠正 12-023 标题（resolve 首次 UNRESOLVED，按 arXiv 实际标题改正） |

由已有知识列入并经 `resolve` 核对：RAG 原论文、MIRACL、Self-RAG（经典补充 3 篇，均写 `old_reason`）、BGE-M3、mGTE、Jina-ColBERT-v2、ColBERT-XM、E5-mistral、Translate-Distill、SWIM-IR、NoMIRACL、Chirkova 多语言 RAG、MIRAGE-Bench、MEMERAG、Faux Polyglot、Pleias-RAG、OCR Hinders RAG、Mu-SHROOM、Poly-FEVER、RAG 综述、Docling、ColPali。

## 2. 选入 / 排除原则
- “直接相关”：多语言/跨语言/低资源语言的嵌入、检索、重排、RAG、文档解析、知识编辑、事实核验。“通用支撑”（RAG 原论文、Self-RAG、E5-mistral、OCR Hinders RAG、PaddleOCR、RAG 综述）写清用途。
- 排除：音乐/代码/多模态字幕等非文本检索（CLaMP 3、跨语言代码 RAG，归 14 或不相关）；纯应用场景 RAG（农业、医学、法律 RAG 放备选或交给 13）；单一共享任务参赛系统报告（SemEval/CheckThat! 队伍论文，证据薄弱）；纯情感分析等。
- 与别类重叠：olmOCR 已由 05（05-016）认领 → 本类 `cross_only`（12-049）。

## 3. 替代关系与下载结果（下载后补记）
- `resolve 12`：首次 12-023 UNRESOLVED（种子标题与 arXiv 实际标题不符，sim 0.70），按 Q9 查到 2311.05800 实际标题 “Leveraging LLMs for Synthesizing Training Data Across Many Languages in Multilingual Dense Retrieval”，改正种子标题后解析成功；其余 0 处纠正。
- 第一轮 `download 12 --target 55`：核验到 12-057 达 55 篇；12-053 RoundTripOCR 被判 duplicate_elsewhere（05 类 05-069 已认领）→ 本类改为 `cross_only`，不计数。
- 第二轮 `download 12 --target 63`：补齐主列表剩余 8 篇（12-058 X-KDE、12-059 SemEval-2025 Task 7、12-060 AfrIFact、12-061 Mu-SHROOM、12-062 Poly-FEVER、12-063 核查检索偏差、12-064 RAG 综述、12-065 PUGG），以覆盖“引用与事实核验”“低资源知识库问答”子方向；12 篇备选未下载。
- 已有复用：12-003 Self-RAG、12-015 E5-mistral、12-064 RAG 综述（复制自 /root/large_model_multimodal_literature 并重新核验）。
- 下载失败 0；待核验 0。
- 最终：已核验 63，近三年 60/63 = 95.2%，三年前 3 篇（均有 old_reason）；直接相关 57 / 通用支撑 6。

## 4. 未完成与缺口
- 文档解析/OCR：olmOCR（05）、RoundTripOCR（05）已被 05 类认领，本类仅作交叉标签；低资源文字 OCR 端到端评测仍偏少。
- 低资源语言知识库问答（KBQA）原生数据集较少，仅 PUGG（波兰语）入主列表；HybridRAG-BN（孟加拉语）等 2026 新作未收录。
- CIRAL（非洲语言 CLIR 测试集）未找到 arXiv 版本，未收录；可后续用 ACL Anthology/SIGIR 合法 PDF 补充。
- 知识更新方面以知识编辑为主，缺少“小语种知识库增量更新/时效性”专门研究。


---

<!-- 来源：scripts/work/search_log_13_cn.md -->

# 检索日志：13 对话助手与实际应用（assistants_applications）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search '<查询>' --max N`（arXiv API，按相关度）；少量已知代表作（Farmer.Chat、AfriMed-QA、Apollo、MMedLM、Multi3WOZ、Rori 加纳 RCT、Kallaama）用标题/ID 定位，经 `resolve` 校验（64 条全部 ID 与标题一致，0 处纠正）。
- 种子文件：`scripts/seeds/13_assistants_applications_seed_cn.json`（主列表 59 + 备选 5 = 64 条）。
- 判定原则：优先“真实场景/真实用户/实地部署”且涉及低资源或本地语言的工作，标“直接相关”；场景在低资源地区但交互语言为英语/法语、或仅提供方法/原则的，标“通用支撑”并写明用途。领域应用（医疗/农业/法律/客服/政务/教育）归本类；纯多语言 RAG 方法归 12（已避让 12 类已列的 2601.02065、2511.04560）。

## 1. 查询式与返回数（原样）

| 查询式 | 返回条数 |
|---|---|
| `abs:chatbot AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 12 |
| `abs:chatbot AND abs:Africa AND abs:"language model" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"conversational agent" AND abs:multilingual AND abs:deployment AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:WhatsApp AND abs:"language model" AND submittedDate:[202310290000 TO 202610290000]` | 18 |
| `abs:farmers AND abs:"language model" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 3 |
| `abs:health AND abs:chatbot AND abs:"low-resource languages" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"community health workers" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 4 |
| `abs:"language learning" AND abs:chatbot AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:tutor AND abs:LLM AND (abs:Africa OR abs:India OR abs:Ghana OR abs:Kenya) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:agricultur* AND abs:"language model" AND (abs:Swahili OR abs:Hindi OR abs:farmers) AND submittedDate:[202310290000 TO 202610290000]` | 22 |
| `abs:medical AND abs:"question answering" AND abs:"low-resource language" AND submittedDate:[202310290000 TO 202610290000]` | 15 |
| `abs:legal AND abs:"question answering" AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"public services" AND abs:"language model" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"customer service" AND abs:LLM AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"voice" AND abs:assistant AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"multi-turn" AND abs:dialogue AND abs:"low-resource languages" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"mental health" AND abs:LLM AND abs:"low-resource" AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"user study" AND abs:multilingual AND abs:LLM AND abs:chatbot AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `ti:"Farmer.Chat"` | 1 |
| `abs:AfriMed-QA OR ti:"AfriMed-QA"` | 3 |
| `abs:"AI tutor" AND abs:WhatsApp AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"endangered language" AND abs:"language learning" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"Indigenous" AND abs:chatbot AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:chatbot AND abs:Swahili AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:chatbot AND (abs:Hindi OR abs:Indic) AND abs:deploy* AND submittedDate:[202310290000 TO 202610290000]` | 15 |
| `abs:"real users" AND abs:multilingual AND abs:LLM AND abs:conversations AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"maternal health" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 9 |
| `abs:government AND abs:chatbot AND abs:LLM AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 19 |
| `abs:"conversational" AND abs:"low-resource language" AND abs:"field" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"speech" AND abs:"language model" AND abs:"rural" AND abs:India AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"language learning" AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 9 |
| `abs:deployment AND abs:"language model" AND (abs:Nepali OR abs:Sinhala OR abs:Khmer OR abs:Lao OR abs:Burmese OR abs:Tagalog) AND abs:assistant AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:chatbot AND abs:"Global South" AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"health" AND abs:chatbot AND (abs:Urdu OR abs:Bengali OR abs:Hindi OR abs:Marathi OR abs:Telugu) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"multilingual" AND abs:"clinical" AND abs:"African languages" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:tutor AND abs:math AND abs:Ghana` | 2 |
| `abs:"low-literate" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"language revitalization" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `ti:Kallaama` | 1 |
| `abs:chatbot AND (abs:Amharic OR abs:Yoruba OR abs:Hausa OR abs:Kinyarwanda OR abs:Luganda OR abs:Zulu) AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"health" AND abs:"language model" AND (abs:Amharic OR abs:Yoruba OR abs:Hausa OR abs:Kinyarwanda OR abs:Luganda OR abs:Twi) AND submittedDate:[202310290000 TO 202610290000]` | 2 |

说明：多词 `abs:` 交集查询有 9 条返回 0（如 `abs:chatbot AND abs:Africa AND abs:"language model"`），随后改用 WhatsApp、community health workers、maternal health、Global South 等更具体的场景词，命中显著增加。

## 2. 选入（按子方向）
- 医疗（20 篇主列表）：ASHABot（印地语，GPT-4+专家在环）、Script Gap（6 种南亚语言原生 vs 罗马化分诊）、Noora Health 可审计分诊（7 种语言，先译英再抽取）、印度孕产聊天机器人评测工作流（英/印地/阿萨姆语）、巴基斯坦孕产聊天机器人部署、System X（罗马化乌尔都语语音→病历）、豪萨语临床正确性漂移、SIM-UT 多轮多语言分诊模拟、DocTalkBN（孟加拉语远程问诊）、PerMedCQA（波斯语）、IndoNutriQA（印尼语）、阿拉伯语医疗跨语言评估、Med-CoReasoner、巴斯克/哈萨克语医疗问答证据、L2M3、IMAS、尼日利亚孕产/疫苗微调评估；通用支撑：AfriMed-QA（英语）、Apollo、MMedLM、MH-INDIC（问卷英语施测，正文核实后改为通用支撑）、孕产 NLP 原则。
- 农业（10 篇）：Farmer.Chat（正文列出斯瓦希里、阿姆哈拉、豪萨、印地、奥里亚、泰卢固语）、KrishokBondhu、KrishokChat、英/印地/旁遮普语合成问答、希腊岛屿双语农技助手、Kallaama（沃洛夫/普拉尔/塞雷尔语语音）；通用支撑：比哈尔农业咨询微调、加纳 Pezego、AgriLLM、WASHtsApp。
- 法律（4 篇）：MizanQA、VLQA、ALKAFI-LLAMA3、乌兹别克语法律 RAG 云/本地部署。
- 客服与政务（4 篇）：BanglAssist、物流客服原生 vs 翻译意图基准、北欧四语客服语料、KumbhDoot 大型集会公共服务助手。
- 教育与语言学习（8 篇）：AFRILANGTUTOR、孟加拉语语法错误解释、阿姆哈拉语 FAQ 机器人；通用支撑：加纳 Rori 数学辅导 RCT、喀麦隆教师 WhatsApp 培训、印度农村 K-12、科特迪瓦出声思维、中文 L2 提示、EFL 会话机器人。
- 通用使用/对话/用户研究（其余）：Beyond Metrics（斯瓦希里/Sheng/英语混用 WhatsApp）、沃洛夫语任务型对话、LUMO 离线语音助手（孟加拉语识别）、巴基斯坦经期健康（罗马化乌尔都语）、孟加拉语心理健康建议、BhashaBench V1；通用支撑：WaLLM（正文核实以英语为主，约 2% 其他语言）、Ansari（25+ 语言、14 万次对话）。
- 经典补充（1 篇）：Multi3WOZ（2023-07，TACL；英/阿/法/土文化适配任务型对话），已写 old_reason。

## 3. 排除与原因
- 2504.20519（HPV 疫苗 RCT）：参与者为美/加/英英语用户，与小语种无关。
- 2608.14651（灾害援助多模态）、2411.12760（VayuBuddy）、2606.29467（mamabench）：摘要无语言维度，删除。
- 2409.10697、2312.13096 等政治/虚假信息审计：属 10/15 类。
- 2504.06011 Nanda、2507.11502 HKGAI：模型构建属 03 类。
- 2601.02065、2511.04560：12 类已列（多语言 RAG），避让。
- 2405.01470 WildChat：04 类已列。
- 2505.17417 Speechless、2507.03241 KinyaColBERT：属语音训练/检索方法，非应用。
- 2602.14517（僧伽罗/泰米尔语数学教育）：11 类已列。

## 4. 替代关系
- 无下载失败，未发生替代。下载顺序：`download 13 --target 55` 得 55 篇；再 `--target 59` 补下主列表末 4 篇（BhashaBench、Ansari、孕产 NLP 原则、Multi3WOZ）。备选 5 篇（2603.22115、2511.17554、2603.16872、2602.06669、2512.06734）未下载。

## 5. 未完成/疑点
- 13-042 Rori 的教学语言、13-021 Farmer.Chat 的具体 LLM 版本、13-041 KumbhDoot 的语言名单等在摘要/前几页未明确，注释中标“待核实”。
- 直接相关中不少为“地区+本地语言”的 HCI 部署研究，其模型能力证据有限，注释已区分产品工程与模型能力。
- 政务类真实部署论文在 arXiv 偏少（compar:IA 为法语、列备选），是主要缺口；客服类仅 4 篇。


---

<!-- 来源：scripts/work/search_log_14_cn.md -->

# 检索日志：14 代码模型与编程智能体（code_models_agents）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search '<查询>' --max N`（arXiv API，默认按相关度排序）；另结合已知代表作直接给出 arXiv ID，经 `resolve` 校验标题（本类 73 条全部 ID 与标题一致，0 处纠正）。
- 种子文件：`scripts/seeds/14_code_models_agents_seed_cn.json`（主列表 60 条 + 备选 13 条 = 73 条）。
- 判定原则：用非英语自然语言提出编程需求（多自然语言→代码、非英语注释/文档、非英语 Text-to-SQL、非英语母语学习者编程）标“直接相关”；通用代码模型技术报告、编程智能体、评测/沙箱/IDE 基础设施标“通用支撑”并写明用途；低资源**编程语言**工作一律注明【类比材料】且标“通用支撑”。

## 1. 查询式与返回数（原样）

| 查询式 | 返回条数 |
|---|---|
| `abs:"code generation" AND (abs:Japanese OR abs:Korean OR abs:Arabic OR abs:Vietnamese OR abs:Persian) AND abs:prompts AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"BLP-2025" AND abs:code` | 2 |
| `abs:"code comments" AND (abs:"non-English" OR abs:multilingual OR abs:Chinese) AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"non-native English" AND (abs:programming OR abs:code) AND submittedDate:[202310290000 TO 202610290000]` | 8 |
| `abs:"code" AND abs:"natural language" AND abs:"language of the prompt" AND submittedDate:[202310290000 TO 202610290000]` | 14 |
| `abs:"text-to-SQL" AND abs:multilingual AND abs:"low-resource" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"programming education" AND (abs:"native language" OR abs:"non-English") AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"text-to-SQL" AND (abs:Arabic OR abs:Vietnamese OR abs:Russian OR abs:Korean OR abs:Persian OR abs:Bangla OR abs:Turkish OR abs:multilingual) AND submittedDate:[202310290000 TO 202610290000]` | 12 |
| `abs:"code generation" AND abs:benchmark AND (abs:Korean OR abs:Japanese OR abs:Indonesian OR abs:Swahili OR abs:Hindi) AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:multilingual AND abs:"code" AND abs:"instruction tuning" AND abs:"natural languages" AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"code generation" AND abs:"natural languages" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 24 |
| `abs:"code generation" AND abs:"non-English" AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `ti:HumanEval AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"code generation" AND abs:Bangla AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"code generation" AND (abs:Chinese AND abs:English) AND abs:prompts AND abs:bias AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"code" AND abs:"cross-lingual" AND abs:"natural language" AND abs:LLM AND abs:programming AND submittedDate:[202310290000 TO 202610290000]` | 4 |
| `abs:"low-resource programming languages" AND submittedDate:[202310290000 TO 202610290000]` | 13 |
| `abs:Bangla AND abs:Python AND abs:"code generation" AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"code explanation*" AND (abs:multilingual OR abs:"non-English" OR abs:languages) AND abs:students AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"natural language" AND abs:"code" AND abs:"language bias" AND submittedDate:[202310290000 TO 202610290000]` | 3 |
| `abs:"code generation" AND abs:"low-resource natural language*" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"multilingual" AND abs:"code LLM*" AND abs:"natural language" AND abs:instructions AND (abs:Chinese OR abs:Russian OR abs:Japanese) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `ti:IFEvalCode` | 1 |
| `abs:HumanEval AND (abs:Japanese OR abs:Korean OR abs:Vietnamese OR abs:Indonesian OR abs:Swahili) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"code generation" AND abs:"Arabic" AND abs:LLM AND abs:prompts AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"text-to-SQL" AND (abs:Vietnamese OR abs:Persian OR abs:Korean OR abs:Indonesian OR abs:Bengali OR abs:Urdu OR abs:Swahili) AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"code" AND abs:LLM AND (abs:"non-English speakers" OR abs:"non-English-speaking") AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"natural language to code" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 0 |

说明：返回数为 `--max` 截断后的实际条数；部分查询与 13 类在同一批次运行（批次文件不同但不影响结果）。多词 `abs:` 交集查询偶有 0 返回，已改用更宽查询或直接按已知标题补充。

## 2. 直接给出 ID 的已知代表作（经 resolve 校验）
- 代码模型技术报告：StarCoder2（2402.19173）、Qwen2.5-Coder（2409.12186）、DeepSeek-Coder（2401.14196）、OpenCoder（2411.04905）；备选 DeepSeek-Coder-V2、CodeGemma、Granite Code、Magicoder。
- 编程智能体：SWE-agent、OpenHands、Agentless、CodeAct、SWE-Gym、Multi-SWE-bench；备选 AutoCodeRover、SWE-smith。
- 评测/仓库上下文/自修复/沙箱/IDE：LiveCodeBench、LDB、RepoAgent、CodeRAG-Bench、Copilot Evaluation Harness、MPLSandbox；综述 2406.00515、2409.02977。
- 多自然语言→代码：mHumanEval、HumanEval-XL（检索命中）；NaturalCodeBench（正文第 2.4 节核实为中文原生用户查询+英译版，故标直接相关）；IFEvalCode（正文核实每题含中英查询）。
- 经典补充（三年前，共 5 篇，均写 old_reason）：Codex/HumanEval（2107.03374）、MCoNaLa（2203.08388）、ODEX（2212.10481）、SWE-bench（2310.06770，2023-10-10 公开，略早于窗口）、MultiPL-E（2208.08227）。

## 3. 选入与排除
- 选入（直接相关，36 条主列表）：多语言提示代码生成基准与偏差研究（mHumanEval、HumanEval-XL、X-HumanEval-X、IndicEval-XL、CodeMixBench、多语言提示代码质量研究、英日中提示差异研究、UA-Code-Bench、RoCode、MERA Code、NaturalCodeBench、IFEvalCode）；孟加拉语专题（TigerCoder、BanglaForge、BLP-2025 Task 2 三个系统：PyBangla、Retriv、NALA_MAINZ）；非英语注释（2505.15469、2605.05902）与开源仓库非英语趋势（2602.19446）；非英语母语学习者/助教（2412.12800、2411.02725、CodeVaani、2610.22163）；非英语 Text-to-SQL（Ar-Spider、AraSpider、Dialect2SQL、BIRDTurk、IndicDB、MultiSpider 2.0、GRPO 多语言 Text-to-SQL、Ar-SParC、CricBench）；方法：零样本跨语言迁移（2408.09701）；经典 MCoNaLa、ODEX。
- 排除/降级：
  - 2604.25960（多语言代码智能综述）：摘要显示“多语言”指编程语言 → 改标通用支撑【类比材料】。
  - 2411.15470、2403.03894（IRCoder）：编程语言维度 → 备选、通用支撑【类比】。
  - 2512.20482 SweRank+、2506.03535、2503.18760、2406.03636、2502.18449 SWE-RL、2504.08703 SWE-PolyBench、2412.00535 FullStack Bench、2406.07436 McEval：与核心关系较弱或类比材料过多，删除以控制条数与“直接相关”占比。
  - 2507.05418（多语言推理）、2412.14471（日本本地 LLM）：主题属 11/03 类，不收。
  - 2402.01687、2501.10365、2606.28882 等编程教育论文：未涉及非英语，不收。
  - 2507.14688（阿拉伯语后训练数据综述）：属 08/04 类。
- BLP-2025 Task 2 共享任务总述论文未在 arXiv 检索到（ACL Anthology 可能有），未收入，记为缺口。

## 4. 替代关系
- 无下载失败，未发生替代。为把“直接相关”占比拉近 60%，在主列表末尾追加 14-071 IFEvalCode、14-072 CricBench、14-073 多源 AI 助教（均为直接相关）。

## 5. 下载与核验
- `download 14 --target 55` → 55 篇核验通过；随后 `--target 58` 补下 SWE-bench、MultiPL-E、IFEvalCode；最后补下 14-072/14-073（结果见 progress 文件）。
- 已有复用（兄弟库复制并重新核验）6 篇，其余为本轮下载。

## 6. 未完成/疑点
- “直接相关”占比约 60%（通用支撑主要为代码模型报告、智能体与评测基础设施，属任务要求的必要内容）。
- 日语、韩语、斯瓦希里语等原生提示代码基准在 arXiv 检索中未找到（JHumanEval 等疑为非 arXiv 发表），记为缺口。
- 若干注释中的语言名单、基座模型为“待核实”（摘要未给出），未编造。


---

<!-- 来源：scripts/work/search_log_15_cn.md -->

# 检索日志：15 评测与人工评价（evaluation_human）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API），辅以检索者已有知识（凭知识选入者由 `resolve` 回查 arXiv 元数据核对标题，82 条 0 处纠正）。
- 时间窗：除经典补充外均加 `submittedDate:[202310290000 TO 202610290000]`（下文记为 `$D`）。
- 选题原则：多语言/低资源语言基准（区分原生构建 vs 翻译构建）、基准翻译质量、文化偏差、母语者评价与 LLM-as-judge 可靠性、MT 指标在低资源语言上的有效性、评测统计不确定性与污染控制。专门的推理/工具（11）、检索（12）、代码（14）、安全（10）基准留给对应类别。

## 查询式（原样）与返回数

| # | 查询式 | 返回 | 主要选入 |
|---|---|---|---|
| 1 | `abs:benchmark AND abs:multilingual AND abs:"translated" AND abs:"culturally" AND $D` | 50 | 2412.03304 Global-MMLU, 2411.19799 INCLUDE, 2504.15521, 2607.00724 MSQA, 2602.10732 Macaron, 2604.20225 GaoYao, 2509.03162 SinhalaMMLU, 2511.11334 LaoBench, 2409.11404 AraDiCE, 2504.09714, 2508.20511, 2406.15053 PARIKSHA, 2608.09766 Cultivar, 2606.15643, 2610.36990；备选 2511.00657, 2505.02177, 2412.07251 |
| 2 | `(abs:"LLM-as-a-judge" OR abs:"LLM evaluators" OR abs:"LLM-based evaluators") AND (abs:multilingual OR abs:"low-resource") AND $D` | 40 | 2607.02235, 2505.12201, 2404.01667 METAL, 2607.14480, 2410.13394, 2504.04953, 2503.17039, 2410.17578 MM-Eval, 2411.05049 ProverbEval, 2502.14301 SEA-HELM, 2601.15706, 2602.22207, 2503.10497 MMLU-ProX, 2311.07463 MEGAVERSE；备选 2503.04360, 2507.06774, 2409.08706, 2509.06401 |
| 3 | `(abs:COMET OR abs:chrF OR abs:metrics) AND abs:"machine translation" AND (abs:"low-resource" OR abs:African OR abs:Indic) AND abs:evaluation AND $D` | 30 | 2506.04557 SSA-COMET, 2311.09828 AfriCOMET, 2406.03893, 2602.17425, 2603.25222, 2605.04208 Nsanku |
| 4 | `abs:benchmark AND abs:African AND abs:languages AND abs:LLMs AND $D` | 30 | 2311.07978 AfroBench, 2406.03368 IrokoBench, 2412.00948 Uhura, 2502.19582, 2412.12417 |
| 5 | `(abs:"machine-translated" OR abs:"translated benchmarks" OR abs:translationese) AND abs:benchmark AND abs:LLMs AND abs:native AND $D` | 28 | 2602.05150 GreekMMLU, 2510.21193 爱沙尼亚语, 2502.14911 Batayan, 2605.07093, 2610.09152 sk-bench, 2502.11020 TUMLU, 2602.18788 BURMESE-SAN |
| 6 | `(ti:variance OR ti:"error bars" OR ti:noise OR ti:significance OR ti:uncertainty) AND ti:evaluation AND (abs:"language model" OR abs:LLM) AND $D` | 20 | 2411.00640, 2406.10229, 2508.13144（通用支撑）；备选 2410.03492 |

## 凭知识选入（resolve 核对标题一致）
BLEnD 2406.09948、P-MMEval 2411.09116、MultiLoKo 2504.10356、ECLeKTic 2502.21228、Global PIQA 2510.24081、SeaExam/SeaBench 2502.06298、MILU 2411.02538、IndicGenBench 2404.16816、KMMLU 2402.11548、ArabicMMLU 2402.12840、TurkishMMLU 2407.12402、BertaQA 2406.07302、Spanish MMLU 翻译问题 2406.17789、WMT24++ 2502.12404、FLORES 非洲语言修订 2409.00626、BOUQuET 2502.04314、COMET 陷阱 2408.15366、CulturalBench 2410.02677；备选 M-RewardBench 2410.15522、ESA 2406.11580。

## 经典补充（≤5，均写 old_reason）
Belebele 2308.16884、SIB-200 2309.07445、Hada 等多语言 LLM 评审 2309.07462；备选 MEGA 2303.12528。IndoMMLU（2023-10-07）、CMMLU、HAE-RAE 等早于窗口的单语基准未选，以窗口内同类基准替代。

## 排除与替代
- 与他类种子重复而跳过（尊重先到先得）：BenchMAX 2502.07346（11 备选）、MultiNRC 2507.17476（11）、语言混淆基准 2406.20052（01）、跨语言污染 2406.13236（05）、“好数据还是坏评测”2406.12822（08/09）、多语言基准污染报告 2410.16186（05）、FLORES 跨方向污染 2601.20858（05）、翻译腔偏差 LLM 评审 2603.10351（09）、MIRAGE-Bench（12）、各数学/长上下文/智能体多语言基准（11）、SeaCrowd（04）。
- 排除：多模态（视觉/视频）多语言基准（JMMMU、Kaleidoscope、IndicVisionBench 等）；安全基准（IndicSafe、SEA-SafeguardBench、UbuntuGuard 等，属 10）；医疗/语音领域基准（AfriMed-QA、AfriVox 等，属 13 或非本库重点）。

## 结果与未完成原因
- 种子 82 条（主列表 71、备选 10、cross_only 1）；resolve 82 条全部按 ID 命中，标题一致，0 处纠正。
- `download 15 --target 55`：按种子顺序核验 15-001～15-055 共 55 篇，全部一次通过硬/软检查，待核验 0、失败 0、兄弟库复用 0（均为本轮下载）。近三年 55/55 = 100%；经典补充（Belebele、SIB-200、Hada 等 2309.07462）排在主列表末尾，因达到目标未下载（状态 todo），不计数。
- 未下载的主列表条目（todo 16 篇）：15-056～15-071（印度语言 MT 指标、chrF++/BLEU、COMET 陷阱、Translation or Recitation、Cultivar、Multilingual-IRT、AISI 多语言评测方法、多语言评测审计、三篇评测统计不确定性、CulturalBench、非洲语言新基准、三篇经典）。原因：达到 --target 55 即停止；多进程共享 arXiv 速率锁，单篇约 1–2 分钟。若后续要补齐 MT 指标与统计不确定性子方向，可用 `download 15 --target 71` 续跑（已在 16 类完成后视时间决定）。
- M-RewardBench（2410.15522）已被 10 类（10-005）认领，本类改为 cross_only 交叉标签。
- 疑点：15-010 MSQA（2607.00724）arXiv 注释称作者因公司数据审批问题“需撤回”，但 v3 PDF 为完整 24 页正文且已通过核验；脚本无法撤销已核验记录，已在注释 limitations 中标明，建议协调者人工决定是否保留。
- 注释：55 篇全部写入 `scripts/annotations/15_evaluation_human_annot_cn.json`；以摘要为主，top 10 中 9 篇（15-001/002/003/004/007/011/013/023/024/034）另用 `text` 核对正文前 2–4 页补充语言、规模、构建方式与污染控制信息。

### 续跑（同日）
- 16 类完成后执行 `download 15 --target 71`，把主列表剩余 16 条（15-056～15-071）补齐：16 条全部通过核验，待核验 0、失败 0。
- 最终：已核验 71（68 篇本轮下载、3 篇兄弟库复用）；近三年 68/71 = 95.8%；经典 3 篇（Belebele、SIB-200、2309.07462），均写 old_reason。
- 相关性：直接相关 67 / 通用支撑 4（COMET 陷阱、评测误差条、基准方差、信噪比）。
- 注释已覆盖全部 71 篇。


---

<!-- 来源：scripts/work/search_log_16_cn.md -->

# 检索日志：16 高效训练、推理与部署（efficient_train_deploy）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API），辅以检索者已有知识（经典系统论文 ID 由 `resolve` 回查 arXiv 元数据核对标题，0 处纠正）。
- 时间窗：除经典补充外均加 `submittedDate:[202310290000 TO 202610290000]`（下文记为 `$D`）。
- 选题原则：优先“压缩/部署对多语言、低资源语言能力的影响”与“多语言 token 膨胀带来的推理成本”，标 `直接相关`；通用系统工作（分布式训练、量化方法、KV 缓存、服务调度、推测解码）标 `通用支撑` 并写明用途。

## 查询式（原样）与返回数

| # | 查询式 | 返回 | 主要选入 |
|---|---|---|---|
| 1 | `abs:quantization AND abs:multilingual AND $D` | 40 | 2407.03211, 2601.18306, 2508.20893, 2507.19699, 2503.03592, 2608.09941, 2608.11786, 2602.09130 |
| 2 | `abs:pruning AND abs:multilingual AND abs:"language models" AND $D` | 30 | 2408.14398, 2409.16911, 2505.16956, 2411.14055, 2503.06291, 2605.28042 |
| 3 | `abs:compression AND abs:"low-resource languages" AND $D` | 18 | 2404.04748, 2404.04759, 2502.18020, 2601.13328(备选) |
| 4 | `abs:"speculative decoding" AND (abs:multilingual OR abs:translation) AND $D` | 30 | 2406.16758, 2605.30580, 2604.16368 |
| 5 | `abs:distillation AND abs:multilingual AND abs:"low-resource" AND abs:LLM AND $D` | 14 | （多为 09 合成/翻译蒸馏，未选） |
| 6 | `abs:tokenization AND (abs:cost OR abs:latency OR abs:inference) AND abs:languages AND abs:disparit* AND $D` | 0 | — |
| 7 | `abs:quantized AND (abs:"low-resource" OR abs:multilingual OR abs:"non-English") AND abs:LLMs AND $D` | 30 | 2608.24615, 2603.18037(备选), 2601.12033(备选) |
| 8 | `abs:"KV cache" AND abs:multilingual AND $D` | 5 | 无（均为技术报告/无关） |
| 9 | `abs:tokenization AND abs:cost AND abs:languages AND abs:API AND $D` | 20 | 2410.10665, 2608.09046 |
| 10 | `ti:token AND (ti:tax OR ti:premium OR ti:cost OR ti:fair*) AND $D` | 25 | 2602.11174, 2609.00378（2509.05486 / 2606.24460 / 2607.24276 已在 06 种子，跳过） |
| 11 | `abs:"vocabulary" AND abs:"inference" AND abs:efficien* AND abs:"non-English" AND $D` | 0 | — |
| 12 | `abs:"low-resource languages" AND (abs:edge OR abs:"on-device" OR abs:CPU OR abs:"consumer hardware") AND abs:LLM AND $D` | 10 | 无（多为 03/04/13 主题） |
| 13 | `abs:"model compression" AND abs:multilingual AND abs:"language models" AND $D` | 9 | 2510.26271(备选) |
| 14 | `abs:QLoRA AND (abs:"low-resource language" OR abs:multilingual) AND $D` | 25 | 无（多为下游任务微调应用，属 08/13） |
| 15 | `abs:experts AND abs:pruning AND abs:multilingual AND abs:mixture AND $D` | 2 | 2605.28042 |
| 16 | `(abs:quantization OR abs:pruning OR abs:distillation) AND abs:"machine translation" AND abs:LLM AND abs:"low-resource" AND $D` | 10 | 2509.23990, 2412.05862(备选) |
| 17 | `abs:"cross-lingual vocabulary adaptation" AND abs:inference` | 0 | （2402.10712 已在 06 种子） |
| 18 | `(abs:"inference efficiency" OR abs:"inference cost" OR abs:latency OR abs:throughput) AND abs:multilingual AND abs:LLMs AND abs:languages AND $D` | 40 | 2504.10013, 2610.23249, 2606.17609(备选) |
| 19 | `(abs:"knowledge distillation" OR abs:distill*) AND abs:"multilingual" AND abs:"smaller" AND (abs:compression OR abs:"student model") AND abs:LLM AND $D` | 1 | 2407.19610 |
| 20 | `(abs:"vocabulary trimming" OR abs:"vocabulary reduction" OR abs:"layer skipping" OR abs:"early exit") AND (abs:multilingual OR abs:language-specific) AND $D` | 20 | 2311.09709, 2410.12513(备选) |
| 21 | `abs:"mixture-of-experts" AND (abs:pruning OR abs:offloading OR abs:"expert pruning") AND abs:language AND abs:multilingual AND $D` | 2 | — |
| 22 | `(abs:affordable OR abs:"limited compute" OR abs:"single GPU" OR abs:"consumer GPU") AND abs:"low-resource language" AND abs:LLM AND $D` | 4 | 无（UnifiedCrawl 属 04；Paramanu/LilMoo 属 03） |
| 23 | `(ti:quantization OR ti:quantized OR ti:compression OR ti:compressed OR ti:pruning OR ti:pruned OR ti:distillation) AND (ti:multilingual OR ti:languages OR ti:"low-resource" OR ti:cross-lingual OR ti:translation) AND $D` | 50 | 2603.11881, 2610.21383, 2411.06506, 2409.14162, 2507.21568, 2407.14679(通用), 2410.17170/2501.00733(备选) |

## 通用支撑（凭知识选入，resolve 核对）
Medusa 2401.10774、EAGLE 2401.15077、SGLang 2312.07104、DistServe 2401.09670、Sarathi-Serve 2403.02310、KIVI 2402.02750、QuaRot 2404.00456、SpinQuant 2405.16406、BitNet b1.58 2402.17764、FlashAttention-3 2407.08608、TorchTitan 2410.06511、MegaScale 2402.15627、GaLore 2403.03507、Minitron 2407.14679、Evaluating Quantized LLMs 2402.18158、“Give Me BF16” 2411.02355、校准数据影响 2311.09755、高效推理综述 2404.14294；备选 QuIP#、AQLM、量化与推理模型、ShortGPT、高效 LLM 综述等。

## 经典补充（≤5，均写 old_reason）
ZeRO 1910.02054、Megatron-LM 3D 并行 2104.04473、PagedAttention/vLLM 2309.06180、GPTQ 2210.17323、AWQ 2306.00978。QLoRA 2305.14314 已在 08 种子，未重复选入；FSDP 论文（2023-04）因经典名额已满未选，以窗口内 TorchTitan（FSDP2）替代。

## 排除与替代
- 与他类种子重复而跳过：2509.05486 The Token Tax（06）、2606.24460 African Language Tax（06）、2607.24276 Tokenizer Tax（06）、2402.10712 词表适配推理效率（06）、2305.14314 QLoRA（08）、2501.02631 爱沙尼亚语词表裁剪（06 备选）。
- 排除：2410.14766（“低资源语言”指编程语言 Lua，非自然语言）；语音压缩 2405.00966、2505.20237（语音模态，非本库重点）；各类以 QLoRA 做单一下游任务的应用论文（属 08/13）。

## 结果与未完成原因
- 种子 77 条（主列表 58、备选 19）；resolve 77 条全部按 ID 命中，0 处纠正。
- 下载前调整：读摘要后发现 2601.12033（量化对多语言公平/安全）、2606.17609（多语言 QA 剪枝评测陷阱）、2604.16235（韩语 token 剪枝）为直接相关，提升为主列表；FlashAttention-3、MegaScale、Evaluating Quantized LLMs 降为备选；2407.19610 涉及语言均为高资源，改标通用支撑。为让提升的 3 条和经典补充都被处理，本类用 `download 16 --target 58`（略高于建议的 55）。
- 结果：已核验 58、待核验 0、失败 0；其中 16 篇为兄弟库已核验 PDF 复制后重新核验（已有复用），42 篇本轮下载。近三年 53/58 = 91.4%；经典 5 篇（ZeRO、Megatron-LM 3D 并行、PagedAttention、GPTQ、AWQ）均写 old_reason，已到上限。
- 相关性：直接相关 37 / 通用支撑 21（64%）。
- 缺口：KV 缓存、服务调度、分布式训练方面缺少多语言专门研究，只能用通用系统论文支撑；“多语言 token 膨胀带来的推理成本”的核心论文 The Token Tax（2509.05486）和 African Language Tax（2606.24460）已由 06 类认领，本类收录的是同主题的其他成本/延迟审计论文。
- 注释：58 篇全部写入 `scripts/annotations/16_efficient_train_deploy_annot_cn.json`；资源与实验数值一律写成“作者称/依其硬件”，不作泛化；top 10 中 16-001/003/009/011/020 另用 `text` 核对正文前 2–3 页。


---

<!-- 来源：scripts/work/search_log_17_cn.md -->

# 类别 17 检索日志：大学官方教材与完整课程讲义

检索日：2026-10-29。种子：`scripts/seeds/17_university_courses_seed_a_cn.json`（17-001–021，兄弟库复用）、`_b`（17-026–037，数学/统计/优化 + ML/DL）、`_c`（17-041–052，多语言/MT/低资源 + 计算语言学 + IR/RAG）、`_d`（17-061–067，系统/部署 + LLM 补充）。编号区间之间的空号为各片段预留，未使用，不复用。

通用方法：`python3 -I scripts/materials_en.py links <官方页> --pattern ...` 列官方链接；WebFetch/WebSearch 核对课程主页、日程讲数、学期与讲者；只取学校/教师官方页面（及官方页面直接链接的 GitHub/Google Drive/Dropbox/Google Slides 公开文件）；Canvas、ILIAS、OLAT、Learn 等需登录平台的材料一律不收；未执行任何下载来的代码。下载一律 `materials_en.py fetch 17 [--sid]`。

## 片段 A：兄弟库已核验讲义包复用（17-001–021）

来源：`/root/large_model_multimodal_literature/scripts/seeds/13_university_courses_seed_{a,b}_cn.json` 与 `scripts/state/results/13_university_courses_en.json`（只读）。每个 file 条目加 `copy_from` 指向兄弟库同名已核验文件（逐一核对 URL 一致且兄弟库记录 ok），由本库脚本复制后重新做类型检查与讲数核对，记为“已有复用”（`reused_other_library`），不算新下载。课程元数据（学期、讲者、日程讲数、completeness_note、prereq、coverage）沿用兄弟库已核对内容；reason 与 cross 按本库 01–16 分类重写。

选入 21 套：Stanford CS224N (W26)、CS336 (S26)、CME 295 (A25)、CS324 (W22，经典)；Berkeley CS294-196 LLM Agents (F24)、CS294-280 Adv. LLM Agents (S25)、CS294-196 Agentic AI (F25)、CS294-267 Understanding LLMs (S24)；CMU 11-711 (F25)、11-667 (F24)、11-766 (S26)、11-868 (S26)、15-442 (S26)；Princeton COS 484 (S26)、COS 597R (F24)；JHU 601.471 (S25)；UCSD CSE 234 (W25)；UMass CS 685 (S24)；Cornell CS 5740 (S25)；中国人民大学《大语言模型》课件 (2025)；IIT Delhi ELL881 (2024 Sem I)。

兄弟库中未复用的已核验课程及原因：MIT 6.S191、CMU 10-423 生成式 AI（与本库 ML/DL 片段新下载课程重叠、偏视觉生成）；Stanford CS224S、Edinburgh ASR（语音方向不在本类指定范围）；计算机视觉/扩散/机器人/具身/多模态课程（11-777、CS231n、CS236、6.S978、6.S184、16-726、10-799、CS285、CS224R 等）与本库主题无关。兄弟库失败条目（NYU DS-GA 1011、UW CSE 447、Columbia COMS 6706）未用。

## 主线程补救：17-043 第 12 讲

ÚFAL NPFL120 第 12 讲“Contextual Word Embeddings”官方只以 Google Slides 发布页提供。试 `pub?output=pdf`（返回 HTML 发布页本体，非 PDF）、`export/pdf` 与 `pub/export/pdf`（均 404）。发布页 HTML 内嵌幻灯片文字（可检出 BERT/ELMo/contextual 等），按官方发布形式保存 HTML 本体（与兄弟库对 reveal.js 网页幻灯片的处理一致），expected_items 改为 13 后重跑，通过。弱点：完整版式需联网加载 Google 脚本。

## 片段 B：数学/概率/统计/优化 + 机器学习与深度学习（17-026 起）

检索日：2026-10-29。方法：`python3 -I scripts/materials_en.py links <官方页> --pattern ...` 列官方链接；WebFetch 读日程表核对讲数、学期与讲者；GitHub API 只读列目录与提交记录；WebSearch 找课程主页。未登录任何平台，Canvas/ILIAS/Ed 等受限材料一律不收。

### 选入
| sid | 课程 | 学期 | 讲义数 | 依据与说明 |
|---|---|---|---|---|
| 17-026 | Berkeley CS 70 离散数学与概率 | Spring 2026 | 27 幻灯片 + 22 Note = 49 | sp26.eecs70.org 日程 27 讲全有 slides；主站 eecs70.org 为进行中的 Fall 2026（讲义不全）不选；annotated 版重复未收 |
| 17-027 | Stanford EE364a 凸优化 I | Summer 2026 | 7 | 官方以单个完整幻灯片 PDF 发布 + 6 份补充讲义；原版（Summer 2023 前）重复未收 |
| 17-028 | EPFL CS-439 Optimization for ML | Spring 2026 | 12 幻灯片 + 讲义全本 = 13 | 官方 GitHub 仓库 main 分支（提交 5afb6f9）；master 分支为 2025 旧版，已区分 |
| 17-029 | Berkeley Stat 210A 理论统计 | Fall 2025 | 24（手写讲义，去重） | Fall 2026 进行中；在线 Reader 后半“under construction”未收 |
| 17-030 | CMU 36-705 中级统计（经典） | Fall 2019 | 36 | **已排除（exclude）**：下载时官方第 5 讲 lec5.pdf 返回 HTTP 404，讲义不完整；以 17-037 替代 |
| 17-031 | CMU 10-301/601 机器学习导论 | Spring 2026 | 26 | 第 27 讲无幻灯片；Inked 版重复未收 |
| 17-032 | CMU 11-785 深度学习导论 | Spring 2025 | 28（第 1–27 讲，GAN 两份）+ jsd aux；第 0 讲 Logistics 官方链接 404 未收 | F25/S26 页面由脚本动态加载、无静态 PDF（S26 lectures 页 404），故选 S25 |
| 17-033 | MIT 6.7960 Deep Learning | Fall 2025 | 21 | 主站为进行中的 Fall 2026；2025 页解析时剔除 HTML 注释中的链接；3 次嘉宾讲座无幻灯片 |
| 17-034 | Berkeley CS 189 机器学习导论 | Fall 2025 | 24 | 各讲次页的 Google Drive 公开 PDF；Sp26 站点无讲义、Fa26 进行中 |
| 17-035 | Cornell CS 4780 机器学习导论 | Spring 2024 | 24 + beamer aux | 2024fa 之后学期站点 404；手写板书扫描与讲义重复未收 |
| 17-036 | UBC CPSC 440/550 高级机器学习 | 2025W2（2026 年 1–4 月） | 25 | 3 次续讲沿用上一份幻灯片 |
| 17-037 | Stanford CS168 The Modern Algorithmic Toolbox | Spring 2024 | 19 | 替代 36-705；MinHash/sketch/Good–Turing/降维等语料处理数学；6/4 差分隐私一讲无讲义 |

### 浏览后排除
- Stanford CS229：官网讲义/幻灯片在 Canvas（需登录），各学期存档页无 PDF，不收。
- Stanford CS109：讲次页为网页，PDF 链接指向错误路径（/class/lectures/…），无法完整获取，不收。
- Tübingen Probabilistic ML（Hennig）：公开幻灯片只有 Summer 2020，近年学期材料在 ILIAS（需登录），不收。
- Stanford EE376A 信息论：主页为 Winter 2018-19 且无讲义链接，不收。
- MIT 18.063 Matrix Calculus（IAP 2026）：讲义为 Google Slides + 黑板 + Dropbox 混合，单讲无独立讲义文件，不收。
- CMU 10-725（Siva Balakrishnan 新学期）：仅前几讲讲义，进行中，不收；Tibshirani Fall 2019 版完整但与 EE364a/CS-439 重叠且为旧学期，作为备选未用。
- GaTech ECE 7750（Fall 2025）：只发布了 3 讲，不收。
- CMU 10-606/607：最新公开学期为 2023 及更早，且与 CS70/EE364a 重叠，不收。
- EPFL CS-433 Machine Learning：仓库为进行中的 Fall 2026，不收。
- UBC CPSC 340（Schmidt 340-F22）：学期较旧，改选同校更新且更贴近 LLM 的 CPSC 440 25W2。
- UBC CPSC 440 24W2：与 25W2 同课程，按“最新完整学期”只收 25W2。
- MIT 6.7960 Fall 2024：同课程旧学期，改收 Fall 2025。

### 脚本问题（未修改 .py，仅记录）
- `materials_en.py links` 中 `re.sub(r'\\s+', ...)` 位于 f-string 内，实际匹配的是字面反斜杠，链接文字中的换行未被压缩，导致输出一行被拆成多行；解析输出时需只取以 http 开头的行。

### 下载结果（2026-10-29，均为本轮新下载，无复用）
- verified：17-026、027、028、029、031、032、033、034、035、036、037（11 套）。
- 17-032 首次失败（Lec-0.Logistics.pdf 404），从种子移除该行政讲义并在 completeness_note 说明后重试通过。
- 17-030 失败（lec5.pdf 404）后设 exclude。
- 抽查：CS189 Drive PDF 首页为“EECS 189/289, Fall 2025 … Gonzalez and Norouzi”；6.7960 首页为 Fall 2025；11-785 第 20 讲（LLMs，Omar Khattab 讲）首页日期为 Mar 26, 2024，系沿用旧版幻灯片。

# 类别 17 检索日志片段 C：多语言/机器翻译/低资源 NLP、计算语言学、信息检索与 RAG

检索日：2026-10-29。种子文件：`scripts/seeds/17_university_courses_seed_c_cn.json`（sid 17-041 至 17-052）。
方法：WebSearch 找候选 → `materials_en.py links` / curl + 本地 HTML 解析核对官方日程表（逐行对照讲次与幻灯片链接）→ `materials_en.py fetch 17 --sid <sid>` 逐个下载核验。全部为新下载（无兄弟库复用）。

## 检索式（原样）
- `CMU 11-737 Multilingual Natural Language Processing slides schedule 2024 OR 2025`
- `machine translation course lecture slides pdf 2024 university schedule "machine translation" Koehn OR Edinburgh OR "neural machine translation" course page`
- `information retrieval course 2024 lecture slides dense retrieval RAG schedule university "11-642" OR "CS 646" OR "neural information retrieval" course`
- `"multilingual" OR "low-resource" NLP course 2024 lecture slides syllabus university LING 575 OR "subword modeling" 11-824`
- `"machine translation" course 2025 slides schedule university Helsinki OR Zurich OR Tartu OR Uppsala OR Amsterdam neural machine translation lecture pdf`
- `"information retrieval" course 2024 OR 2025 lecture slides pdf schedule "dense retrieval" "learned sparse" university course website`
- `University of Amsterdam "Information Retrieval 1" 52041INR6Y course site slides`
- `"CS 646" OR "CS646" information retrieval UMass Zamani 2024 OR 2025 slides`
- `"search engines" OR "information retrieval" graduate course 2025 github.io lecture slides pdf ColBERT SPLADE RAG "lecture 1"`
- `course "retrieval" "large language models" seminar OR course 2025 schedule slides github.io "neural information retrieval" ...`
- `"computational morphology" OR "linguistic typology" course lecture slides pdf 2024 OR 2025 university schedule computational linguistics`
- `Lei Li UCSB "CS 291" OR "CS 190" machine translation OR "multilingual" course slides lileicc.github.io/course`
- `IIT Bombay Pushpak Bhattacharyya CS772 OR CS626 2024 OR 2025 lecture slides machine translation Indian languages course page`
- `"low-resource" languages NLP university course 2024 OR 2025 lecture slides all lectures pdf schedule "endangered languages" OR "language documentation" computational`

## 选入（12 套）
| sid | 课程 | 学期 | 讲义数 | 方向 | 备注 |
|---|---|---|---|---|---|
| 17-041 | CMU 11-737 Multilingual NLP（Lei Li） | Fall 2023 | 20 | 多语言/MT | 24+1 讲中 20 讲有幻灯片；4 次嘉宾讲座与 2 讲无幻灯片；NAT 讲链接错位已按文件名归位 |
| 17-042 | JHU EN 601.468/668 Machine Translation（Koehn） | Fall 2026（进行中） | 23 | MT | 官方 Syllabus 已为全部 23 讲链接幻灯片；https 证书主机名不符，按官方 http 链接下载 |
| 17-043 | Charles Univ ÚFAL NPFL120 Multilingual NLP | Summer 2026（最后一次开设） | 13 | 多语言/低资源 | 第 12 讲仅 Google Slides 发布页，已由主线程补存其 HTML 本体（见上文“主线程补救”） |
| 17-044 | ÚFAL NPFL087 Statistical Machine Translation（Bojar） | Summer 2026 | 12 + 4 aux | MT | 10 讲官方仍链接 2019/20 版幻灯片 |
| 17-045 | LMU Machine Translation（Fraser） | Summer 2023 | 17 + 2 aux | MT/低资源翻译 | 含双语词向量、无监督 NMT、迁移学习、多语言预训练 |
| 17-046 | CMU 11-324/11-824 Subword Modeling（Mortensen） | Spring 2026 | 22 + 2 aux | 计算语言学（形态/正字法/类型学） | 含 Totonac 课堂练习 |
| 17-047 | ÚFAL NPFL094 Morphological and Syntactic Analysis（Zeman） | 2025/26 冬季讲义集（页面现为 2026/27） | 11 | 计算语言学（形态/句法） | 学期进行中，讲义可能更新 |
| 17-048 | Edinburgh INFR11145 TTDS（Magdy, Ross） | 2024-25 Sem 1 | 18 | IR/RAG | 第 5 讲官方链接错指第 12 讲文件（SHA256 相同），该讲实际未发布 |
| 17-049 | Waterloo CS 451/651 Data-Intensive Distributed Computing（Jimmy Lin） | Fall 2025 | 21 | IR/大规模文本处理 | 12/2 LLMs 一讲无幻灯片 |
| 17-050 | Stanford CS224U NLU（Potts） | Spring 2023 | 16 | IR/RAG/评测 | 含 1 份官方链接的 Google Drive 公开 PDF |
| 17-051 | TU Wien Advanced Information Retrieval（Hofstätter） | Summer 2022 | 11 | 神经 IR | 三年前经典，写 old_reason；固定提交 fbdc44cd |
| 17-052 | UZH NLP for Low-Resource and Marginalized Language Varieties（Sina Ahmadi） | Spring 2026 | 4 + 4 aux | 低资源 NLP | 研讨课，教师讲授仅 4 讲，其余为学生论文研读 |

## 排除 / 未采用及原因
- **Edinburgh NLU+（NLU-11，2023-24/2024-25）**：讲义全部托管在 git.ecdf.ed.ac.uk，从本机访问超时（curl 60 s 无响应、GitLab API 亦超时）；opencourse 只镜像了个别周的文件，不完整。未建种子。
- **Edinburgh ANLP 2025-26**：讲义同样全部在 git.ecdf.ed.ac.uk，无法下载；且属通用 NLP 入门。未建种子。
- **Edinburgh MT（INFR11062）**：已停开并入 NLU+；旧主页返回 410。
- **CMU 11-642 Search Engines（Callan）**：boston.lti.cs.cmu.edu 证书链不完整，脚本（urllib 校验证书）无法下载；不绕过。
- **CMU 11-737 Fall 2022（Neubig，phontron.com）**：同课程不同学期，已收 Fall 2023；且日程页链接解析为 0 个 PDF。
- **UCSB CS291K Deep Learning for MT（Lei Li，Fall 2021）**：与 CMU 11-737 F23 同一教师、幻灯片高度重合，且早于 2023，不收。
- **JHU 601.467/667 Intro to HLT（Fall 2026）**：学期进行中，11/3 与 12/3 讲次尚无幻灯片，9/17 无幻灯片，暂不完整；且为 HLT 综述课。
- **Stanford CS276 IR**：主页标 Spring 2019，日程为更早学期的 Coursera 式材料，混杂且老旧；以 TU Wien AIR 作经典替代。
- **Stanford CS224V（Fall 2026）**：学期进行中，幻灯片主要在 Canvas；Berkeley 智能体课已由主线程复用。
- **UMass CS 646 Fall 2023 / CS 546**：课程页无幻灯片链接（讲义在 Moodle）。
- **UvA Information Retrieval 1**：未找到官方公开讲义页（仅第三方镜像），讲义在 Canvas。
- **Oregon State AI539 Advanced IR（2025 春）**、**UIUC CS 510**：幻灯片在 Canvas/Coursera，需登录。
- **Texas A&M CSCE 670 F25**：课程站 404。
- **NUS CS6101**：站点 404。
- **UF LIN 6932 / Saarland 低资源 NLP 研讨课**：论文研读型，无教师讲义。
- **IIT Bombay CS772/CS626**：未找到公开的近年课程讲义页。
- **CMU 11-724 / UW LING 575 / LMU 计算形态学 2016 / Heidelberg 2013**：前两者未找到公开讲义；后两者过旧。

## 疑点
- 17-043 第 12 讲（Contextual Word Embeddings）原为缺口，已由主线程补存 Google Slides 发布页 HTML，13/13 讲齐全。
- 17-048 第 5 讲官方链接错误导致该讲幻灯片缺失；17-052 为研讨课，教师讲义仅 4 讲。
- 17-042 与 17-047 所在学期仍在进行，后续讲义可能被教师更新。
- 17-049 偏数据工程/分布式，计入“IR 与大规模文本处理”；17-050 是 NLU 课，计入 IR/RAG 因其检索增强 ICL 单元。

## 分叉 d：分布式/推理服务/高效 ML 与 LLM 补充课（17-061 起）

检索日：2026-10-29。种子：scripts/seeds/17_university_courses_seed_d_cn.json。页面读取方式：`materials_en.py links`、WebFetch、WebSearch（查询原样记录如下）；未登录任何平台。

### 检索/浏览记录
| 查询或页面 | 结果 | 处理 |
|---|---|---|
| https://dlsyscourse.org/lectures/ （CMU 10-414/714 DLSys） | 页面日程 8/25 起为周二/周四、11/3 Democracy Day，与 2026 年日历一致，即 Fall 2026 正在进行；第 17、19、20、22、23 讲只有视频或无材料，讲义多为 2022 公开版沿用 | 排除：学期未结束、讲义不全；dlsys.cs.cmu.edu 域名无法解析，未找到往届完整官方存档 |
| WebSearch `10-414/714 Deep Learning Systems Fall 2025 lectures slides Tianqi Chen Dettmers` | 仅第三方博客/笔记 | 不采用第三方 |
| https://efficientml.ai/schedule/ | HTTP 522 | 改用 MIT HAN Lab 官方课程页 |
| https://hanlab.mit.edu/courses/2024-fall-65940 | 23 讲全部有 Dropbox 幻灯片链接；课程列表有 2026 Fall（进行中）、2024、2023、2022，无 2025 | 选入 17-061（Fall 2024）；全套约 1.1 GB，单文件最大约 320 MB（<400 MB） |
| https://stanford-cs229s.github.io/ | 404 | 改查 cs229s.stanford.edu |
| https://cs229s.stanford.edu/fall2023/calendar/ | 11 份 Google Slides；6 次嘉宾讲座无幻灯片，2 讲为占位链接 | 选入 17-065（Google Slides 官方导出 PDF）；fall2024 页仅复制了 9 份同样幻灯片，不作新学期 |
| WebSearch `"15-779" OR "15-849" CMU machine learning systems LLM course slides 2025` | 找到 https://www.cs.cmu.edu/~zhihaoj2/15-779/ | 选入 17-062（Fall 2025，17 份 PDF） |
| https://hao-ai-lab.github.io/dsc204a-f25/ → haoailab.com/dsc204a-f25 | UCSD DSC 204A Fall 2025，17 份幻灯片 + 17 份 scribe 笔记 | 选入 17-063 |
| https://www.cs.cornell.edu/courses/cs6787/{2023fa,2024fa,2025fa}/ | 404；2021fa 可访问但过旧；2026sp 第 2、3、11、14 讲未发布幻灯片 | 排除（不完整/过旧），2026sp 仅作备选 |
| https://www.cs.cornell.edu/courses/cs4787/2025fa/ | Principles of Large-Scale ML，28 讲中 27 讲有讲义（PDF/HTML 笔记本/幻灯片） | 选入 17-064 |
| https://ucbsky.github.io/cs294-162-fa24/、https://dsc204a.github.io/ | 404 | 跳过 |
| WebSearch `EECS 598 "Systems for Generative AI" Michigan Chowdhury schedule slides` | UMich CSE 585 为论文研讨课，幻灯片不公开；Princeton COS 597K（Fall 2024）页面无讲义；Berkeley CS294-162 Fall 2023 在 Notion | 排除：研讨课/无公开讲义/Notion 页面无法按官方文件核验 |
| https://basil-web-01.colorado.edu/courses/fa25/csci7000/schedule/ | 只有论文链接 | 排除（论文研讨课） |
| https://zirui-ray-liu.github.io/teaching/25sp-intro-llmsys （Minnesota CSCI 8980） | Google Slides，多讲无幻灯片，日程无日期 | 排除（缺讲较多） |
| WebSearch `university course "efficient" LLM inference systems ...` | IIT Delhi COL851 2025 页面讲义与论文混排、学期进行中 | 排除 |
| WebSearch `UIUC CS 598 "AI Efficiency" ...` | 学生报告型研讨课 | 排除 |
| WebSearch `Stanford CS329H Machine Learning from Human Preferences lecture slides schedule`；https://web.stanford.edu/class/cs329h/fall2025/ | 幻灯片不在课程页（只有 Google Doc 大纲） | 排除 |
| WebSearch `Harvard CS 2881 AI safety Boaz Barak Fall 2025 lecture slides`；https://boazbk.github.io/mltheoryseminar/ | 页面已切换到 Fall 2026（进行中），幻灯片多为 Google Slides/外链 | 排除 |
| https://web.stanford.edu/class/cs329x/ | 2026-27 学期进行中（10 讲），无往届存档 | 排除 |
| WebSearch `Yu Meng UVA CS 6501 large language models course schedule slides pdf` | UVA CS 6501 Spring 2025（21 份 PDF）；HKUST COMP 4901B Fall 2025（23 讲） | 选入 17-067、17-066 |
| https://nyu-cs2590.github.io/fall2024/ | 无讲义链接 | 排除 |

### 选入（下载结果见状态）
- 17-061 MIT 6.5940 TinyML and Efficient DL Computing，Fall 2024，23 讲
- 17-062 CMU 15-779 Advanced Topics in ML Systems (LLM Edition)，Fall 2025，17 份
- 17-063 UCSD DSC 204A Scalable Data Systems，Fall 2025，17 份（+17 份 scribe aux）
- 17-064 Cornell CS 4787/5777 Principles of Large-Scale ML，Fall 2025，27 讲（+4 aux）
- 17-065 Stanford CS 229S Systems for ML，Fall 2023，11 讲
- 17-066 HKUST COMP 4901B Large Language Models，Fall 2025，23 讲（+20 批注版 aux）
- 17-067 UVA CS 6501 NLP（LLM 专题），Spring 2025，21 份

### 下载结果（2026-10-29，均为本轮新下载，无兄弟库复用）
17-061～17-067 共 7 套全部 VERIFIED（`fetch 17 --sid` 逐个运行）。合计约 1.4 GB，其中 MIT 6.5940 约 1.08 GB。
疑点：Cornell CS4787 第 1、18 讲官方讲义 PDF 仅 2 页（文字约 5000 字符，为官方原样）；该课 19 讲为 notebook 渲染 HTML，公式/脚本依赖 cdnjs 在线资源。CMU 15-779 学期（Fall 2025）由日期与 Piazza 链接推定。CS229S 用 Google Slides 自带导出 PDF。


---

<!-- 来源：scripts/work/search_log_18_cn.md -->

# 类别 18 检索日志：完整教科书、专著与参考书

- 检索日期：2026-10-29
- 种子：`scripts/seeds/18_books_seed_cn.json`（18-001 … 18-053，共 53 条，一本书一条）
- 下载/核验：`python3 -I scripts/materials_en.py fetch 18`；结果见 `scripts/state/results/18_books_en.json`，运行日志 `scripts/work/fetch_18_run*.log`
- 兄弟库（只读）：`/root/large_model_multimodal_literature`（14 类书籍种子与结果）、`/root/machine_learning_deep_learning_literature`（`scripts/cache/materials_results_en.json` 与 `books/`）。同一版本的文件用 `copy_from` 复用，脚本复制后重新核验，记为“已有复用”，不算新下载。

## 1. 检索来源与查询（原样记录）

| # | 渠道 | 查询 / 访问 | 返回 | 用途 |
|---|---|---|---|---|
| 1 | 兄弟库种子与结果 | 读取 `14_books_seed_cn.json`、`14_books_en.json`、`materials_results_en.json`、`C12_books_cn.json` | 40 + 59 条 | 确定可复用的同版本 PDF 及其官方 URL |
| 2 | WebSearch | `Language Science Press open access book linguistic typology morphology introduction` | 10 条 | 未直接命中类型学教科书，转查 LangSci 丛书目录 |
| 3 | WebSearch | `Springer open access book European Language Equality 2023 pdf` | 10 条 | 确认 ELE（10.1007/978-3-031-28819-7）开放获取 |
| 4 | WebFetch | `https://langsci-press.org/catalog/series/tmnlp`（TMNLP 丛书） | 27 种 | 选入 MT for everyone、Unicode Cookbook、Language technologies for a multilingual Europe |
| 5 | WebSearch | `langsci-press.org catalog book textbook "Textbooks in Language Sciences" series` | 19 条 | 找到 TBLS 丛书页 |
| 6 | WebFetch | `https://langsci-press.org/catalog/series/tbls` | 31 种 | 选入 Language and computers、Grammatical theory 第 5 版、Corpus linguistics、Analyzing meaning 第 3 版、Indigenous languages of the Americas: Sounds、Multilingualism、Linguistics Olympiad |
| 7 | WebFetch | `https://langsci-press.org/catalog/series/sidl`（Studies in Diversity Linguistics） | 35 种 | 均为专题论文集/专著，未选入（见排除） |
| 8 | Zenodo API | `https://zenodo.org/api/records/<id>`（LangSci 各书 DOI 记录） | 10 条 | 取得整书 PDF 文件链接、出版日期与许可（CC BY / CC BY-SA） |
| 9 | curl HEAD | Springer `content/pdf/<doi>.pdf` × 5 | 2 个 PDF | ELE、ELG 为 PDF（开放获取）；Towards Responsible MT（978-3-031-14689-3）与 Translation Quality Assessment（978-3-319-91241-7）返回 HTML（非开放获取），排除 |
| 10 | WebSearch | `"Ultra-Scale Playbook" PDF download nanotron free` | 15 条 | 官方 HF Space 文件区有 PDF；第三方“免费 PDF”站点为垃圾站，不用 |
| 11 | WebSearch | `stas00 ml-engineering "Machine Learning Engineering Open Book" pdf release download` | 19 条 | 作者在 HF Hub `stas/ml-engineering-book` 托管 PDF（CC BY-SA 4.0） |
| 12 | WebSearch | `Rothwell "Translation Tools and Technologies" Routledge 2023 open access pdf` | 10 条 | 非开放获取，排除 |
| 13 | WebSearch | `Blitzstein Hwang "Introduction to Probability" second edition free PDF official probabilitybook.net` | 18 条 | 官方仅指向在线版 probabilitybook.net，未找到官方 PDF；搜索结果中“免费 PDF”多为盗版/垃圾站，未收 |
| 14 | WebSearch | `Raschka "Machine Learning Q and AI" free online open access all chapters 2025` | 10 条 | 官方仅提供样章，未收 |
| 15 | GitHub API | `repos/NiuTrans/MTBook`、`repos/NiuTrans/NLPBook`（contents、commits） | — | MTBook 完整 PDF（提交 a55dd1a8，2024-09-14）；NLPBook 完整 PDF（提交 b1255a0f，2026-10-19），固定到提交号 |
| 16 | GitHub API | `repos/harvard-edge/cs249r_book/releases` | 8 个 release | Vol1 v0.8.0、Vol2 v0.3.0（2026-10-24） |
| 17 | arXiv abs 页 | 2501.09223、2504.12501、2311.17633、2412.05265、2404.17625、2403.14606 | — | 最新版本分别为 v4、v12、v2、v5、v3、v4，与兄弟库一致，可复用 |
| 18 | HF API | `api/spaces/nanotron/ultrascale-playbook`、`api/models/stas/ml-engineering-book` | — | 固定提交 c93890dd、9966fd7d |

## 2. 预检（下载到会话暂存目录，仅用 pypdf 抽取文本，不执行任何下载内容）

- LLMBook（赵鑫等《大语言模型》）：391 页，第 7–14 页为目录，但中文字体编码使抽取为乱码，自动检查找不到“目录”。人工核对目录页可读条目（BPE、WordPiece、LLaMA、BIG-Bench、HELM、C-Eval）与五部分书签，设 `toc_override`。兄弟库 14-007 正因此失败。
- MLHP（斯坦福）：当前版（Last-Modified 2026-09-23）第 4 页有 “TABLEOFCONTENTS”，脚本正则可匹配。兄弟库 14-011 失败时的版本不同。
- ML Systems：Vol1 第 8 页 “Contents”，Vol2 第 5 页 “Table of contents”。兄弟库 14-028 把两卷当作一本书，以 Vol2 为主文件而失败。两卷书名不同（Introduction to Machine Learning Systems / Scaling Machine Learning Systems），本库分开计数，列为疑点。
- Ultra-Scale Playbook：官方 PDF 是 1 个超长页面（1133.9×102047.2 pt），可抽取 204,286 字符，含目录、全部章节、结论、附录与参考文献，因此 min_pages 设为 1 并在 completeness_note 说明。
- Happy-LLM（Datawhale）：PDF 用康熙部首兼容字符（如“⼤”），中文书名精确匹配会失败；无目录标题；属于社区教程。未收。
- Goodfellow《Deep Learning》HTML：index 页含 “Table of Contents”，rnn.html 含 “Recurrent”，bib.html 含 “Bibliography”，用作 must_contain。

## 3. 排除与替代

| 候选 | 原因 | 处理 |
|---|---|---|
| Manning, Raghavan & Schütze《Introduction to Information Retrieval》 | 官方站点 nlp.stanford.edu 从本机无法连接（`connect … No route to host`，80/443 都不通） | 用 Croft, Metzler & Strohman《Search Engines: Information Retrieval in Practice》（作者官网合法全文）替代 |
| Bishop & Bishop《Deep Learning: Foundations and Concepts》 | 官网只提供在线阅读，没有合法的完整下载版 | 不收 |
| Blitzstein & Hwang《Introduction to Probability》第 2 版 | 未找到官方 PDF，只有在线版 | 不收 |
| Raschka《Machine Learning Q and AI》等 | 官方只提供样章 | 不收 |
| Xiao & Zhu《Introduction to Transformers: an NLP Perspective》（arXiv 2311.17633） | 内容已并入同作者 NLPBook（README 说明），避免重复 | 收 NLPBook，不收该书 |
| Rothwell 等《Translation Tools and Technologies》、Moniz 等《Towards Responsible MT》、Moorkens 等《Translation Quality Assessment》 | 不是开放获取 | 不收 |
| LangSci Studies in Diversity Linguistics 各卷 | 都是窄专题论文集，不属于教科书/参考书 | 不收；类型学方向由 TBLS 教材（Indigenous languages of the Americas、Kroeger）承担 |
| Happy-LLM | 社区教程，PDF 的中文抽取与书名校验有问题 | 不收 |
| LangSci《Teaching translation in the age of generative AI》 | 翻译教学方向，与模型开发关系弱 | 不收 |
| MT for everyone 中文译本（LangSci 492） | 与英文原书是同一本书 | 只收英文原版 |

## 4. 复用说明

有 `copy_from` 的条目是兄弟库已核验过的同版本文件：arXiv 版本号一致，或官方 URL 一致且文件大小与 Last-Modified 吻合（例如 SLP3：官方 26,506,144 字节，与兄弟库一致，草稿日期 2026-08-19）。复用文件由本库脚本重新核验，计为“已有复用”，不算新下载。

## 5. 运行结果（2026-10-29）

- `fetch 18` 一次跑完（日志 `scripts/work/fetch_18_run1.log`）：53 条全部 verified，0 失败，0 待核验。
- 来源：新下载 23 条（含 2 个 HTML 离线镜像：Goodfellow《Deep Learning》28 页、How to Scale Your Model 16 页，wget rc=8 是个别页面资源 404，must_contain 全部通过）；已有复用 30 条（兄弟库同版本文件，本库重新核验）。
- 按方向：NLP 与计算语言学 10；机器学习与深度学习 9；多语言/机器翻译/低资源 9；数学、概率、统计与优化 8；大模型训练/适配/评测 7；信息检索/RAG/智能体 5；分布式训练/推理/部署 5。
- 2023 年及以后版本（edition_year ≥ 2023）：38/53（71.7%）。
- 用了覆盖开关的条目：18-040《大语言模型》设 toc_override，理由见第 2 节，已人工核对；18-050 Ultra-Scale Playbook 设 min_pages=1（单个超长页面）。
- ISBN 与 DOI：从各书 PDF 前 10 页版权页抽取后回填种子，共 19 条有 ISBN；作者/机构网络公开版不适用或待核实，均已在种子中写明。
- 未完成/疑点：Manning IR 书因主机网络不可达未收；ML Systems 两卷分开计数；SLP3、NLPBook、MLHP、ML Systems、Bekman 均为持续更新的在线版，已用提交号、release 或 arXiv 版本号固定所收版本。


---

<!-- 来源：scripts/work/search_log_19_cn.md -->

# 类别 19 工程资料：检索与选择日志

- 检索/核验日期：2026-10-29
- 方法：按协调者给定的 9 个工程环节，从候选清单中按“互补、官方、活跃维护、对小语种开发有直接用途”挑选；每个候选先用 `python3 -I scripts/engineering_en.py refs <url>` 查真实 tag，再在暂存目录用无 blob 的浅层 fetch（`git fetch --depth 1 --filter=blob:none`，不检出、不执行）列出文件树，用于：确认 tag 对应提交日期、核对 core_modules 路径确实存在、定位文档源目录与目录（TOC）文件类型。之后才写入种子并用 `engineering_en.py fetch` 正式下载。
- ref 规则：一律写具体 tag；无 tag 或最新 tag 明显过旧的写完整提交号（GlotLID、text-dedup、open-instruct，以及三个文档仓库 dvc.org / open-webui/docs / OpenHands/docs / langfuse-docs）。未写 main/latest。
- 关联论文：本库论文代理尚未完成（检索时 `scripts/state/claims_en.json` 仅 1 条，与本类项目无关），故 related_papers 写“英文标题 (arXiv:ID)”。全部 32 个 arXiv ID 已用 arXiv API（一次 id_list 查询）核对标题与首次提交日期，无编造。

## tag 选择中发现的问题（据实记录）
| 项目 | 现象 | 处理 |
|---|---|---|
| datatrove | 原测试种子 ref 为 v0.6.0（旧） | 改为 v0.10.1（2026-09-30） |
| sentencepiece | 存在 `1.0.0` tag，但其提交日期为 2019-06-11（历史遗留标签，非新版） | 选 v0.2.2（2026-07-02） |
| tokenizers | 有 v1.0.0-rc.* 预发布 | 选最新稳定版 v0.23.3 |
| text-dedup | 最新 tag 2023.09.20 / 0.4.1 过旧 | 固定 2026-03-09 提交 7538f3ec… |
| GlotLID | 仓库无 tag | 固定 2026-04-15 提交 d63cc2f6… |
| open-instruct | 仅 v0.1.0–v0.3.0 旧 tag 与 runs/ledger 实验标签 | 固定 2026-10-28 提交 64beb76c… |
| Megatron-LM | 有 26.09-*.rc 容器标签与 core_v* 发布标签 | 选 Megatron Core 正式发布 core_v0.19.2 |
| torchtitan | 大量 ciflow/* CI 标签 | 选 v0.4.0（2026-10-28） |
| vllm | 有 v0.33.0rc* | 选稳定版 v0.32.0 |
| llama.cpp | 有大量 backup/* 分支式标签；v0.x 为语义版本 tag | 选 v0.8.0（提交日期 2026-10-28） |
| continue | v1.5.x 与 v2.x-vscode 两条线 | v2.1.0-vscode（2026-06-18）比 v1.5.45（2026-03-04）新，选前者 |
| argilla | v2.8.0 为最新 tag，提交日期 2025-03-10 | 照录，注明项目更新放缓 |
| OpenHands | 主仓库 1.11.0 中 openhands/ 只剩 app_server 与前端，智能体核心与沙箱已迁出 | 改收官方 OpenHands/software-agent-sdk v1.59.0，文档取 OpenHands/docs 仓库 |

## 各环节选择理由与未选同质项目

### 1 语料获取、清洗、语言识别、去重和分词
- 选：datatrove（流水线，FineWeb2 实际使用）、GlotLID（低资源 LID，专门面向 2000+ 语言）、sentencepiece（语言无关子词训练）、tokenizers（HF 生态实际分词实现）、text-dedup（独立去重算法实现）。
- 不选：OpenLID 数据集仓库（与 GlotLID 同为 fastText LID，GlotLID 覆盖语言更多且明确面向低资源）；fastText 主仓库（已于 2024 年归档，LID 模型使用方式在 GlotLID/datatrove 中已有）；NeMo-Curator（与 datatrove 同质，体量大）。

### 2 数据版本管理、训练数据配比及质量审计
- 选：dvc（数据版本与流水线复现）、datasets（加载、流式与按概率混合）、data-juicer（算子化处理与质量分析）、dolma（标签→混合的配方化语料工具链）。
- 不选：lakeFS / git-lfs（与 DVC 同质）；NeMo-Curator（同上）。

### 3 持续预训练、指令微调、参数高效适配及偏好训练
- 选：peft（适配器实现）、trl（SFT/DPO/GRPO 训练器）、LLaMA-Factory（配置驱动端到端）、open-instruct（公开配方的后训练参考）。
- 不选：axolotl（与 LLaMA-Factory 同属配置驱动微调框架，二选一取后者，因有对应论文且中英文档俱全）；transformers 全仓（体量大，训练相关部分已由 trl/peft/accelerate 覆盖）；OLMo-core（与 torchtitan/Megatron 预训练框架同质）。

### 4 分布式训练、检查点、日志与训练故障恢复
- 选：Megatron-LM（工业级并行与分布式检查点、ft_integration）、DeepSpeed（ZeRO 与通用检查点）、torchtitan（PyTorch 原生、代码量小）、accelerate（单卡到多机的薄封装）。
- 不选：NeMo（构建在 Megatron Core 之上，同质且仓库大）；Colossal-AI（与 DeepSpeed 同质）。

### 5 语言评测、人工评测和回归测试
- 选：lm-evaluation-harness（多语种任务最全）、lighteval（多语种任务模板）、sacrebleu（MT 可复现指标）、COMET（学习型 MT 指标）、argilla（人工标注/评测平台）。
- 不选：Label Studio（与 Argilla 同质，Argilla 更贴近 LLM 数据与偏好标注）；OpenCompass（与 lm-eval-harness 同质）。

### 6 多语言检索、RAG、工具调用及智能体
- 选：sentence-transformers（向量模型训练，含多语种蒸馏）、FlagEmbedding（BGE-M3 多语种检索）、haystack（RAG/Agent 管线）、docling（文档解析与 OCR）、smolagents（工具调用与代码执行沙箱）。
- 不选：LlamaIndex（与 Haystack 同质，且单仓库集成包极多、体量大）；LangChain（同质）。

### 7 推理服务、量化、容器化、API 与流式输出
- 选：vllm、sglang（两种主流服务引擎，前缀缓存/约束解码互补）、llama.cpp（本地/边缘与 GGUF 量化）、llm-compressor（训练后量化）。
- 不选：text-generation-inference（已查 tag：最新 v3.3.7 提交日期 2025-12-18，HF 已转入维护模式，功能与 vLLM/SGLang 同质，改选 SGLang）；AutoAWQ（官方已归档，功能由 llm-compressor 接替）。

### 8 对话产品、编程工具、IDE 扩展及执行隔离
- 选：open-webui（自托管对话产品）、continue（IDE 扩展）、OpenHands software-agent-sdk（智能体与 Docker/远程沙箱执行隔离）、aider（终端编程助手）。
- 不选：e2b（沙箱即服务，核心基础设施不在开源 SDK 仓库内，且执行隔离已由 OpenHands 工作区与 smolagents 远程执行器覆盖）；gVisor（文档在 gvisor 主仓库内，仓库体量很大，非 LLM 专用，未收）。

### 9 运行监控、成本统计、灰度发布和回滚
- 选：prometheus（指标与告警）、opentelemetry-python（追踪/指标标准层）、langfuse（LLM 追踪、成本与评测）、argo-rollouts（金丝雀/蓝绿与自动回滚）。
- 不选：Flagger（与 Argo Rollouts 同质）；Kubernetes website（体量过大，且非 LLM 专用）；opentelemetry.io 站点仓库（体量大，仅收 Python SDK 仓库内 docs）。

## 下载结果
见 `progress_19_cn.md` 与 `engineering_notes_cn.md`。

## 下载结果摘要（2026-10-29）
- `engineering_en.py fetch` 一次跑完：39 个项目全部 verified，0 失败；脚本判定完整文档集 13 个（tokenizers、datasets、peft、trl、LLaMA-Factory、DeepSpeed、accelerate、lighteval、smolagents、sglang、continue、opentelemetry-python、argo-rollouts）。
- 磁盘占用：reference_code 3.14 GB + engineering_docs 0.39 GB，合计约 3.53 GB（含 39 个源码原始归档、4 个独立文档仓库原始归档、加后缀副本）。
- 关联论文：本库 claims 中已可查到 FineWeb2（04-001）与 Dolma（04-015），种子已改写为 sid；其余 30 个仍以“标题 (arXiv:ID)”记录，待论文代理完成后可再映射。
- 文档集未计完整的原因（逐项见 engineering_notes_cn.md）：仓库无目录文件；目录在构建时生成；或脚本不支持该目录格式/解析有误。

## 发现的脚本问题（未修改 .py，仅记录）
1. toc_check 的 Sphinx 正则 `(?:\.\. toctree::|```\{toctree\})(.*?)(?:\n\S|```)`：
   - MyST ```{toctree}``` 块中选项行（`:maxdepth:`）不缩进，块在第一行即结束 → Megatron-LM 解析到 0 条；
   - toctree 位于文件末尾、后面没有非缩进行时不匹配 → data-juicer 未识别；
   - 结束匹配 `\n\S` 会吞掉下一个 `.. toctree::` 的首字符，连续两个 toctree 只解析第一个 → opentelemetry-python 只得 2 条（但仍被判完整；人工复核 21/21）；
   - Sphinx 特殊条目 `self` 被当作文件 → FlagEmbedding 解析率 0.909。
2. 文档字符串称支持 “docusaurus sidebars”，代码中并无 sidebars.js/ts 解析（haystack、open-webui/docs）；也不支持 `mkdocs.yaml` 扩展名与 awesome-nav 的 `.nav.yml`（vllm、llm-compressor）、dvc.org 的 sidebar.json、Next.js 的 meta.json（langfuse-docs）、Jekyll `_data` 导航（DeepSpeed、aider）。
3. 目录类型优先级：Sphinx 早于 docs.json，OpenHands/docs 根目录有 docs.json，却因 scripts/sphinx/source 下的零散 toctree 得 0.0（人工按 docs.json 规则约 0.994）。
4. 只看到 code-docs 子目录 toctree 就判 DeepSpeed 文档完整，Jekyll 教程部分实际未经目录核对。
5. detect_license 按正则顺序首个命中：Megatron-LM（BSD-3 主条款 + 附 Apache 文本）报 Apache-2.0；Open WebUI License（BSD-3 + 品牌条款）报 BSD-3-Clause；langfuse 的 ee/ 商业许可部分未体现。
6. 独立文档仓库只过滤、不检查 400 MB 上限（MAX_TREE_BYTES 只作用于主仓库）；本轮未超限。
