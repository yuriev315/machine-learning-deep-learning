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
