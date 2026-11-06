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

