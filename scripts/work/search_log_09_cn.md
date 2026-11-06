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
