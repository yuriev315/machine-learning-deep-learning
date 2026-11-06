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
