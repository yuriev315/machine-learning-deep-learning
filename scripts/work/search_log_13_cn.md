# 检索日志：13 对话助手与实际应用（assistants_applications）

- 检索日期：2026-10-29（近三年窗口：首次公开 ≥ 2023-10-29）
- 检索工具：`python3 -I scripts/papers_en.py search '<查询>' --max N`（arXiv API，按相关度）；少量已知代表作（Farmer.Chat、AfriMed-QA、Apollo、MMedLM、Multi3WOZ、Rori 加纳 RCT、Kallaama）用标题/ID 定位，经 `resolve` 校验（64 条全部 ID 与标题一致，0 处纠正）。
- 种子文件：`scripts/seeds/13_assistants_applications_seed_cn.json`（主列表 59 + 备选 5 = 64 条）。
- 判定原则：优先“真实场景/真实用户/实地部署”且涉及低资源或本地语言的工作，标“直接相关”；场景在低资源地区但交互语言为英语/法语、或仅提供方法/原则的，标“通用支撑”并写明用途。领域应用（医疗/农业/法律/客服/政务/教育）归本类；纯多语言 RAG 方法归 12（已避让 12 类已列的 2601.02065、2511.04560）。

## 1. 查询式与返回数（原样）

| 查询式 | 返回条数 |
|---|---|
| `abs:chatbot AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 12 |
| `abs:chatbot AND abs:Africa AND abs:"language model" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"conversational agent" AND abs:multilingual AND abs:deployment AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:WhatsApp AND abs:"language model" AND submittedDate:[202310290000 TO 202610290000]` | 18 |
| `abs:farmers AND abs:"language model" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 3 |
| `abs:health AND abs:chatbot AND abs:"low-resource languages" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"community health workers" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 4 |
| `abs:"language learning" AND abs:chatbot AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:tutor AND abs:LLM AND (abs:Africa OR abs:India OR abs:Ghana OR abs:Kenya) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:agricultur* AND abs:"language model" AND (abs:Swahili OR abs:Hindi OR abs:farmers) AND submittedDate:[202310290000 TO 202610290000]` | 22 |
| `abs:medical AND abs:"question answering" AND abs:"low-resource language" AND submittedDate:[202310290000 TO 202610290000]` | 15 |
| `abs:legal AND abs:"question answering" AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"public services" AND abs:"language model" AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"customer service" AND abs:LLM AND abs:multilingual AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"voice" AND abs:assistant AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"multi-turn" AND abs:dialogue AND abs:"low-resource languages" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"mental health" AND abs:LLM AND abs:"low-resource" AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 5 |
| `abs:"user study" AND abs:multilingual AND abs:LLM AND abs:chatbot AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `ti:"Farmer.Chat"` | 1 |
| `abs:AfriMed-QA OR ti:"AfriMed-QA"` | 3 |
| `abs:"AI tutor" AND abs:WhatsApp AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"endangered language" AND abs:"language learning" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"Indigenous" AND abs:chatbot AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:chatbot AND abs:Swahili AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:chatbot AND (abs:Hindi OR abs:Indic) AND abs:deploy* AND submittedDate:[202310290000 TO 202610290000]` | 15 |
| `abs:"real users" AND abs:multilingual AND abs:LLM AND abs:conversations AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"maternal health" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 9 |
| `abs:government AND abs:chatbot AND abs:LLM AND abs:language AND submittedDate:[202310290000 TO 202610290000]` | 19 |
| `abs:"conversational" AND abs:"low-resource language" AND abs:"field" AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"speech" AND abs:"language model" AND abs:"rural" AND abs:India AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"language learning" AND abs:"low-resource" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 9 |
| `abs:deployment AND abs:"language model" AND (abs:Nepali OR abs:Sinhala OR abs:Khmer OR abs:Lao OR abs:Burmese OR abs:Tagalog) AND abs:assistant AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:chatbot AND abs:"Global South" AND submittedDate:[202310290000 TO 202610290000]` | 6 |
| `abs:"health" AND abs:chatbot AND (abs:Urdu OR abs:Bengali OR abs:Hindi OR abs:Marathi OR abs:Telugu) AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `abs:"multilingual" AND abs:"clinical" AND abs:"African languages" AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:tutor AND abs:math AND abs:Ghana` | 2 |
| `abs:"low-literate" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 0 |
| `abs:"language revitalization" AND abs:LLM AND submittedDate:[202310290000 TO 202610290000]` | 1 |
| `ti:Kallaama` | 1 |
| `abs:chatbot AND (abs:Amharic OR abs:Yoruba OR abs:Hausa OR abs:Kinyarwanda OR abs:Luganda OR abs:Zulu) AND submittedDate:[202310290000 TO 202610290000]` | 2 |
| `abs:"health" AND abs:"language model" AND (abs:Amharic OR abs:Yoruba OR abs:Hausa OR abs:Kinyarwanda OR abs:Luganda OR abs:Twi) AND submittedDate:[202310290000 TO 202610290000]` | 2 |

说明：多词 `abs:` 交集查询有 9 条返回 0（如 `abs:chatbot AND abs:Africa AND abs:"language model"`），随后改用 WhatsApp、community health workers、maternal health、Global South 等更具体的场景词，命中显著增加。

## 2. 选入（按子方向）
- 医疗（20 篇主列表）：ASHABot（印地语，GPT-4+专家在环）、Script Gap（6 种南亚语言原生 vs 罗马化分诊）、Noora Health 可审计分诊（7 种语言，先译英再抽取）、印度孕产聊天机器人评测工作流（英/印地/阿萨姆语）、巴基斯坦孕产聊天机器人部署、System X（罗马化乌尔都语语音→病历）、豪萨语临床正确性漂移、SIM-UT 多轮多语言分诊模拟、DocTalkBN（孟加拉语远程问诊）、PerMedCQA（波斯语）、IndoNutriQA（印尼语）、阿拉伯语医疗跨语言评估、Med-CoReasoner、巴斯克/哈萨克语医疗问答证据、L2M3、IMAS、尼日利亚孕产/疫苗微调评估；通用支撑：AfriMed-QA（英语）、Apollo、MMedLM、MH-INDIC（问卷英语施测，正文核实后改为通用支撑）、孕产 NLP 原则。
- 农业（10 篇）：Farmer.Chat（正文列出斯瓦希里、阿姆哈拉、豪萨、印地、奥里亚、泰卢固语）、KrishokBondhu、KrishokChat、英/印地/旁遮普语合成问答、希腊岛屿双语农技助手、Kallaama（沃洛夫/普拉尔/塞雷尔语语音）；通用支撑：比哈尔农业咨询微调、加纳 Pezego、AgriLLM、WASHtsApp。
- 法律（4 篇）：MizanQA、VLQA、ALKAFI-LLAMA3、乌兹别克语法律 RAG 云/本地部署。
- 客服与政务（4 篇）：BanglAssist、物流客服原生 vs 翻译意图基准、北欧四语客服语料、KumbhDoot 大型集会公共服务助手。
- 教育与语言学习（8 篇）：AFRILANGTUTOR、孟加拉语语法错误解释、阿姆哈拉语 FAQ 机器人；通用支撑：加纳 Rori 数学辅导 RCT、喀麦隆教师 WhatsApp 培训、印度农村 K-12、科特迪瓦出声思维、中文 L2 提示、EFL 会话机器人。
- 通用使用/对话/用户研究（其余）：Beyond Metrics（斯瓦希里/Sheng/英语混用 WhatsApp）、沃洛夫语任务型对话、LUMO 离线语音助手（孟加拉语识别）、巴基斯坦经期健康（罗马化乌尔都语）、孟加拉语心理健康建议、BhashaBench V1；通用支撑：WaLLM（正文核实以英语为主，约 2% 其他语言）、Ansari（25+ 语言、14 万次对话）。
- 经典补充（1 篇）：Multi3WOZ（2023-07，TACL；英/阿/法/土文化适配任务型对话），已写 old_reason。

## 3. 排除与原因
- 2504.20519（HPV 疫苗 RCT）：参与者为美/加/英英语用户，与小语种无关。
- 2608.14651（灾害援助多模态）、2411.12760（VayuBuddy）、2606.29467（mamabench）：摘要无语言维度，删除。
- 2409.10697、2312.13096 等政治/虚假信息审计：属 10/15 类。
- 2504.06011 Nanda、2507.11502 HKGAI：模型构建属 03 类。
- 2601.02065、2511.04560：12 类已列（多语言 RAG），避让。
- 2405.01470 WildChat：04 类已列。
- 2505.17417 Speechless、2507.03241 KinyaColBERT：属语音训练/检索方法，非应用。
- 2602.14517（僧伽罗/泰米尔语数学教育）：11 类已列。

## 4. 替代关系
- 无下载失败，未发生替代。下载顺序：`download 13 --target 55` 得 55 篇；再 `--target 59` 补下主列表末 4 篇（BhashaBench、Ansari、孕产 NLP 原则、Multi3WOZ）。备选 5 篇（2603.22115、2511.17554、2603.16872、2602.06669、2512.06734）未下载。

## 5. 未完成/疑点
- 13-042 Rori 的教学语言、13-021 Farmer.Chat 的具体 LLM 版本、13-041 KumbhDoot 的语言名单等在摘要/前几页未明确，注释中标“待核实”。
- 直接相关中不少为“地区+本地语言”的 HCI 部署研究，其模型能力证据有限，注释已区分产品工程与模型能力。
- 政务类真实部署论文在 arXiv 偏少（compar:IA 为法语、列备选），是主要缺口；客服类仅 4 篇。
