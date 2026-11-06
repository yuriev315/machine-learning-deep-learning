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
