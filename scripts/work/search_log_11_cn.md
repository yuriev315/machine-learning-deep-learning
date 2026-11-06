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
