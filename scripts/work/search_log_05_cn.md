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
