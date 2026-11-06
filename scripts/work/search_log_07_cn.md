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
