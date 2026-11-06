# 检索日志：03 多语言及低资源语言大模型（multilingual_lowres_llm）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search '<查询>' --max N --sort relevance`（arXiv export API），结合已有知识列出候选，再用 `resolve` 按 ID/标题核对元数据。
- 近三年窗口：首次公开 ≥ 2023-10-29（下列查询中的 `submittedDate:[202310290000 TO 202610290000]` 记为 `<D>`）。

## 1. 查询式与返回数（原样）

| # | 查询式 | max | 返回 | 主要选入 |
|---|---|---|---|---|
| 1 | `abs:"low-resource" AND abs:"large language model" AND abs:adapt* AND <D>` | 40 | 40 | LlamaTurk（2405.07745）、Dicta-LM 3.0（2602.02104）、UrduLLaMA（未选，见排除） |
| 2 | `ti:multilingual AND ti:"language model" AND (abs:"technical report" OR abs:"open") AND <D>` | 40 | 40 | EuroLLM、LOLA、Aya、FuxiTranyu、Babel、Qin 综述（2404.04925） |
| 3 | `abs:"curse of multilinguality" AND <D>` | 30 | 24 | When Is Multilinguality a Curse（2311.09205）、ATLAS（2510.22037）、Gurgurov 综述（2406.10602）、Paramanu（2401.18034） |
| 4 | `abs:"African languages" AND abs:"language model" AND <D>` | 30 | 30 | 非洲 LLM 现状综述（2506.02280）、Cheetah、Lugha-Llama |
| 5 | `abs:"Southeast Asian" AND abs:"language model" AND <D>` | 30 | 30 | SeaLLMs、SeaLLMs 3、SEA-LION；OpenSeal、Toward Robust…（2510.14466）列为备选 |
| 6 | `(abs:Tibetan OR abs:Uyghur OR abs:Mongolian OR abs:Kazakh) AND abs:"large language model" AND <D>` | 30 | 30 | Sherkala-Chat（标题据此更正）、藏语稠密/MoE 持续预训练（2507.09205）、藏语两阶段适配（2512.03976，备选） |
| 7 | `(abs:"language-specific" OR abs:"language neurons") AND abs:multilingual AND abs:LLM AND ti:language AND <D>` | 20 | 20 | Language Arithmetics（2507.22608，备选）；Language-Specific Neurons、How do LLMs Handle Multilingualism 已在列表 |
| 8 | `(ti:Uyghur OR ti:Mongolian OR ti:Kyrgyz OR ti:Uzbek OR ti:Tatar OR ti:Bashkir) AND abs:"language model" AND <D>` | 20 | 7 | 巴什基尔语 LoRA/QLoRA（2605.04948，备选）；其余为基准/树库（归 15/02） |
| 9 | `(ti:Burmese OR ti:Myanmar OR ti:Khmer OR ti:Lao OR ti:Sinhala OR ti:Nepali) AND abs:"language model" AND <D>` | 20 | 20 | SinLlama（2508.09115）、NepaliGPT（2506.16399，备选） |
| 10 | `(ti:Swahili OR ti:Yoruba OR ti:Hausa OR ti:Zulu OR ti:Igbo OR ti:Amharic OR ti:Tigrinya) AND abs:"large language model" AND <D>` | 20 | 13 | Walia-LLM、Amharic LLaMA and LLaVA（2403.06354） |
| 11 | `(ti:Quechua OR ti:Guarani OR ti:Nahuatl OR ti:Aymara OR ti:Mayan OR ti:Cherokee OR ti:Inuktitut) AND abs:"language model" AND <D>` | 20 | 4 | QueEn（2412.05184） |
| 12 | `(ti:Georgian OR ti:Armenian OR ti:Icelandic OR ti:Faroese OR ti:Maltese OR ti:Welsh OR ti:Luxembourgish OR ti:Basque OR ti:Catalan) AND abs:"large language model" AND <D>` | 20 | 19 | Latxa（已在列表）；其余多为基准/指令数据（归 15/08） |
| 13 | `abs:"cross-lingual transfer" AND abs:"large language models" AND abs:"low-resource languages" AND ti:multilingual AND <D>` | 30 | 9 | EMMA-500（已在列表） |
| 14 | `(abs:Uyghur OR abs:Mongolian) AND (abs:"large language model" OR abs:LLM) AND <D>` | 20 | 10 | Do Chinese models speak Chinese languages?（2504.00289）、Left Behind（2603.21036，备选） |
| 15 | `(abs:Guarani OR abs:Quechua OR abs:Nahuatl OR abs:Mapudungun OR abs:Wixarika OR abs:Shipibo) AND (abs:"large language model" OR abs:LLM) AND <D>` | 20 | 4 | 无新增（MTOB 类工作属 09/15） |
| 16 | `abs:"low-resource languages" AND (ti:survey OR ti:review) AND abs:"large language models" AND <D>` | 20 | 8 | 南亚低资源语言综述（2509.11570）、多语言 LLM 综述（2404.00929，备选） |
| 17 | `abs:"indigenous languages" AND abs:"large language model" AND <D>`（与 06 共用批次） | 30 | 14 | 萨米语（2405.05777）、TharuChat（2603.17220）、巴西原住民语言（2407.12620，后被 04 认领） |
| 18 | `(abs:Indic OR abs:Hindi OR abs:Bengali OR abs:Tamil OR abs:Telugu) AND ti:"language model" AND abs:"pretrain" AND <D>`（与 06 共用批次） | 30 | 30 | Agaram 2.5B（2610.18420）；LilMoo（2603.03508）、孟加拉 135M（2606.16383）列为备选 |
| 19 | `abs:"vocabulary expansion" OR …`（06 检索中顺带发现） | 40 | 40 | 确认 Cendol、Swallow（未选，归 07） |
| 20 | `ti:"language imbalance"`（核对 ID） | 10 | 3 | 2404.07982 的正确标题为 *The Role of Language Imbalance in Cross-lingual Generalisation…*，已更正种子标题 |

其余条目（Aya 系列、SeaLLMs、Sailor/Sailor2、Typhoon、Komodo、InkubaLM、Tamil-Llama、Krutrim、Nanda、ALLaM、Atlas-Chat、Fanar、PersianMind、UCCIX、Poro、Salamandra、Llammas、HyperCLOVA X、LLM-jp、Meltemi、Nile-Chat、Apertus、Marco-LLM、Goldfish、X-ELM、语言机制分析三篇、经典 Jais/PolyLM/Glot500/BLOOM）来自已有知识，经 `resolve` 按 arXiv ID 与标题核对一致（除 2404.07982 标题更正外 0 处纠错）。

## 2. 选入与排除原则
- 选入：多语言基座/技术报告；多语言诅咒、语言不均衡与跨语言迁移机制；具体语言/语区的 LLM 适配或从零训练案例（注重语系、文字与资源条件的多样性）；综述。
- 排除或让给其他类别：纯基准（15，如 IrokoBench、SEA-HELM、TLUE、MM-Eval、KazMMLU、TUMLU、SinhalaMMLU）；纯语料/数据集（04，如 MC²、TFD 藏语数据集）；以持续预训练配比为核心的方法研究（07，如 Swallow 2404.17790、Rethinking Multilingual Continual Pretraining 2504.04152、Revisiting Multilingual Data Mixtures 2510.25947）；以指令数据/PEFT 为核心（08，如 Marathi LoRA 2411.18571、Basque instruct pipeline 2412.13922）；翻译/合成（09，如 Tower、LLaMAX）；多模态/语音模型（不收）。
- UrduLLaMA（2502.16961）、Compass（2404.09220）、YAYI 2：信息量或与小语种关联较弱，未选。

## 3. 替代与认领冲突
- 03-053 *Teaching Large Language Models an Unseen Language on the Fly*（壮语）已被 09 认领为 09-003 → 本类改为 `cross_only`，由新增条目补足。
- 03-076 *Harnessing the Power of AI to Vitalize Endangered Indigenous Languages*（巴西原住民语言）已被 04 认领为 04-030 → 改为 `cross_only`。
- 美洲原住民语言目前只有 QueEn（克丘亚语）一篇为本类主分类，属明显缺口。
- 为增加文字/语系覆盖，第二轮追加并下载：萨米语、僧伽罗语、塔鲁语、泰米尔语从零训练、乌克兰语、中国少数民族语言覆盖评测、南亚综述、阿姆哈拉语多模态；备选（未下载）：NepaliGPT、巴什基尔语、Left Behind、Language Arithmetics、多语言 LLM 综述 2404.00929、LilMoo、孟加拉 135M、MaLLaM、VinaLLaMA、Marco-LLM、藏语两阶段、OpenSeal、2510.14466、2604.21637。

## 4. 下载与核验
- `download 03 --target 55` → 55 已核验 + 2 待核验；`--target 70` 补下第二轮 → 共 70 已核验。
- 人工提升（`manual`，均用 `text` 核对首页）：03-046 HyperCLOVA X（pypdf 抽取为 “HyperCLOV A X” 致标题匹配 0.75）；03-061 Meltemi（作者姓 “V oukoutis” 被拆开致姓氏检查失败）。
- 最终：已核验 70；待核验 0；失败 0；近三年 66/70 = 94.3%；经典 4 篇（Jais、PolyLM、Glot500、BLOOM，均写 old_reason）。

## 5. 未完成/缺口
- 维吾尔语、蒙古语（含传统蒙古文）、缅甸语、高棉语、老挝语缺少专门的 LLM 适配主分类论文（检索只得到基准或数据集）；目前仅通过 SeaLLMs/SEA-LION/Sailor2 与 2504.00289 间接覆盖。
- 美洲原住民语言仅 1 篇主分类（QueEn），另 1 篇被 04 认领。
- 注释以摘要为主，top-10 已用正文关键词核对补充；其余条目中“待核实”字段需后续读正文补齐。
