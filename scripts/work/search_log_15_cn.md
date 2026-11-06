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
