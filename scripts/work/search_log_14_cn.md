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
