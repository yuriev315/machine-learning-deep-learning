# 类别 17 检索日志：大学官方教材与完整课程讲义

检索日：2026-10-29。种子：`scripts/seeds/17_university_courses_seed_a_cn.json`（17-001–021，兄弟库复用）、`_b`（17-026–037，数学/统计/优化 + ML/DL）、`_c`（17-041–052，多语言/MT/低资源 + 计算语言学 + IR/RAG）、`_d`（17-061–067，系统/部署 + LLM 补充）。编号区间之间的空号为各片段预留，未使用，不复用。

通用方法：`python3 -I scripts/materials_en.py links <官方页> --pattern ...` 列官方链接；WebFetch/WebSearch 核对课程主页、日程讲数、学期与讲者；只取学校/教师官方页面（及官方页面直接链接的 GitHub/Google Drive/Dropbox/Google Slides 公开文件）；Canvas、ILIAS、OLAT、Learn 等需登录平台的材料一律不收；未执行任何下载来的代码。下载一律 `materials_en.py fetch 17 [--sid]`。

## 片段 A：兄弟库已核验讲义包复用（17-001–021）

来源：`/root/large_model_multimodal_literature/scripts/seeds/13_university_courses_seed_{a,b}_cn.json` 与 `scripts/state/results/13_university_courses_en.json`（只读）。每个 file 条目加 `copy_from` 指向兄弟库同名已核验文件（逐一核对 URL 一致且兄弟库记录 ok），由本库脚本复制后重新做类型检查与讲数核对，记为“已有复用”（`reused_other_library`），不算新下载。课程元数据（学期、讲者、日程讲数、completeness_note、prereq、coverage）沿用兄弟库已核对内容；reason 与 cross 按本库 01–16 分类重写。

选入 21 套：Stanford CS224N (W26)、CS336 (S26)、CME 295 (A25)、CS324 (W22，经典)；Berkeley CS294-196 LLM Agents (F24)、CS294-280 Adv. LLM Agents (S25)、CS294-196 Agentic AI (F25)、CS294-267 Understanding LLMs (S24)；CMU 11-711 (F25)、11-667 (F24)、11-766 (S26)、11-868 (S26)、15-442 (S26)；Princeton COS 484 (S26)、COS 597R (F24)；JHU 601.471 (S25)；UCSD CSE 234 (W25)；UMass CS 685 (S24)；Cornell CS 5740 (S25)；中国人民大学《大语言模型》课件 (2025)；IIT Delhi ELL881 (2024 Sem I)。

兄弟库中未复用的已核验课程及原因：MIT 6.S191、CMU 10-423 生成式 AI（与本库 ML/DL 片段新下载课程重叠、偏视觉生成）；Stanford CS224S、Edinburgh ASR（语音方向不在本类指定范围）；计算机视觉/扩散/机器人/具身/多模态课程（11-777、CS231n、CS236、6.S978、6.S184、16-726、10-799、CS285、CS224R 等）与本库主题无关。兄弟库失败条目（NYU DS-GA 1011、UW CSE 447、Columbia COMS 6706）未用。

## 主线程补救：17-043 第 12 讲

ÚFAL NPFL120 第 12 讲“Contextual Word Embeddings”官方只以 Google Slides 发布页提供。试 `pub?output=pdf`（返回 HTML 发布页本体，非 PDF）、`export/pdf` 与 `pub/export/pdf`（均 404）。发布页 HTML 内嵌幻灯片文字（可检出 BERT/ELMo/contextual 等），按官方发布形式保存 HTML 本体（与兄弟库对 reveal.js 网页幻灯片的处理一致），expected_items 改为 13 后重跑，通过。弱点：完整版式需联网加载 Google 脚本。

## 片段 B：数学/概率/统计/优化 + 机器学习与深度学习（17-026 起）

检索日：2026-10-29。方法：`python3 -I scripts/materials_en.py links <官方页> --pattern ...` 列官方链接；WebFetch 读日程表核对讲数、学期与讲者；GitHub API 只读列目录与提交记录；WebSearch 找课程主页。未登录任何平台，Canvas/ILIAS/Ed 等受限材料一律不收。

### 选入
| sid | 课程 | 学期 | 讲义数 | 依据与说明 |
|---|---|---|---|---|
| 17-026 | Berkeley CS 70 离散数学与概率 | Spring 2026 | 27 幻灯片 + 22 Note = 49 | sp26.eecs70.org 日程 27 讲全有 slides；主站 eecs70.org 为进行中的 Fall 2026（讲义不全）不选；annotated 版重复未收 |
| 17-027 | Stanford EE364a 凸优化 I | Summer 2026 | 7 | 官方以单个完整幻灯片 PDF 发布 + 6 份补充讲义；原版（Summer 2023 前）重复未收 |
| 17-028 | EPFL CS-439 Optimization for ML | Spring 2026 | 12 幻灯片 + 讲义全本 = 13 | 官方 GitHub 仓库 main 分支（提交 5afb6f9）；master 分支为 2025 旧版，已区分 |
| 17-029 | Berkeley Stat 210A 理论统计 | Fall 2025 | 24（手写讲义，去重） | Fall 2026 进行中；在线 Reader 后半“under construction”未收 |
| 17-030 | CMU 36-705 中级统计（经典） | Fall 2019 | 36 | **已排除（exclude）**：下载时官方第 5 讲 lec5.pdf 返回 HTTP 404，讲义不完整；以 17-037 替代 |
| 17-031 | CMU 10-301/601 机器学习导论 | Spring 2026 | 26 | 第 27 讲无幻灯片；Inked 版重复未收 |
| 17-032 | CMU 11-785 深度学习导论 | Spring 2025 | 28（第 1–27 讲，GAN 两份）+ jsd aux；第 0 讲 Logistics 官方链接 404 未收 | F25/S26 页面由脚本动态加载、无静态 PDF（S26 lectures 页 404），故选 S25 |
| 17-033 | MIT 6.7960 Deep Learning | Fall 2025 | 21 | 主站为进行中的 Fall 2026；2025 页解析时剔除 HTML 注释中的链接；3 次嘉宾讲座无幻灯片 |
| 17-034 | Berkeley CS 189 机器学习导论 | Fall 2025 | 24 | 各讲次页的 Google Drive 公开 PDF；Sp26 站点无讲义、Fa26 进行中 |
| 17-035 | Cornell CS 4780 机器学习导论 | Spring 2024 | 24 + beamer aux | 2024fa 之后学期站点 404；手写板书扫描与讲义重复未收 |
| 17-036 | UBC CPSC 440/550 高级机器学习 | 2025W2（2026 年 1–4 月） | 25 | 3 次续讲沿用上一份幻灯片 |
| 17-037 | Stanford CS168 The Modern Algorithmic Toolbox | Spring 2024 | 19 | 替代 36-705；MinHash/sketch/Good–Turing/降维等语料处理数学；6/4 差分隐私一讲无讲义 |

### 浏览后排除
- Stanford CS229：官网讲义/幻灯片在 Canvas（需登录），各学期存档页无 PDF，不收。
- Stanford CS109：讲次页为网页，PDF 链接指向错误路径（/class/lectures/…），无法完整获取，不收。
- Tübingen Probabilistic ML（Hennig）：公开幻灯片只有 Summer 2020，近年学期材料在 ILIAS（需登录），不收。
- Stanford EE376A 信息论：主页为 Winter 2018-19 且无讲义链接，不收。
- MIT 18.063 Matrix Calculus（IAP 2026）：讲义为 Google Slides + 黑板 + Dropbox 混合，单讲无独立讲义文件，不收。
- CMU 10-725（Siva Balakrishnan 新学期）：仅前几讲讲义，进行中，不收；Tibshirani Fall 2019 版完整但与 EE364a/CS-439 重叠且为旧学期，作为备选未用。
- GaTech ECE 7750（Fall 2025）：只发布了 3 讲，不收。
- CMU 10-606/607：最新公开学期为 2023 及更早，且与 CS70/EE364a 重叠，不收。
- EPFL CS-433 Machine Learning：仓库为进行中的 Fall 2026，不收。
- UBC CPSC 340（Schmidt 340-F22）：学期较旧，改选同校更新且更贴近 LLM 的 CPSC 440 25W2。
- UBC CPSC 440 24W2：与 25W2 同课程，按“最新完整学期”只收 25W2。
- MIT 6.7960 Fall 2024：同课程旧学期，改收 Fall 2025。

### 脚本问题（未修改 .py，仅记录）
- `materials_en.py links` 中 `re.sub(r'\\s+', ...)` 位于 f-string 内，实际匹配的是字面反斜杠，链接文字中的换行未被压缩，导致输出一行被拆成多行；解析输出时需只取以 http 开头的行。

### 下载结果（2026-10-29，均为本轮新下载，无复用）
- verified：17-026、027、028、029、031、032、033、034、035、036、037（11 套）。
- 17-032 首次失败（Lec-0.Logistics.pdf 404），从种子移除该行政讲义并在 completeness_note 说明后重试通过。
- 17-030 失败（lec5.pdf 404）后设 exclude。
- 抽查：CS189 Drive PDF 首页为“EECS 189/289, Fall 2025 … Gonzalez and Norouzi”；6.7960 首页为 Fall 2025；11-785 第 20 讲（LLMs，Omar Khattab 讲）首页日期为 Mar 26, 2024，系沿用旧版幻灯片。

# 类别 17 检索日志片段 C：多语言/机器翻译/低资源 NLP、计算语言学、信息检索与 RAG

检索日：2026-10-29。种子文件：`scripts/seeds/17_university_courses_seed_c_cn.json`（sid 17-041 至 17-052）。
方法：WebSearch 找候选 → `materials_en.py links` / curl + 本地 HTML 解析核对官方日程表（逐行对照讲次与幻灯片链接）→ `materials_en.py fetch 17 --sid <sid>` 逐个下载核验。全部为新下载（无兄弟库复用）。

## 检索式（原样）
- `CMU 11-737 Multilingual Natural Language Processing slides schedule 2024 OR 2025`
- `machine translation course lecture slides pdf 2024 university schedule "machine translation" Koehn OR Edinburgh OR "neural machine translation" course page`
- `information retrieval course 2024 lecture slides dense retrieval RAG schedule university "11-642" OR "CS 646" OR "neural information retrieval" course`
- `"multilingual" OR "low-resource" NLP course 2024 lecture slides syllabus university LING 575 OR "subword modeling" 11-824`
- `"machine translation" course 2025 slides schedule university Helsinki OR Zurich OR Tartu OR Uppsala OR Amsterdam neural machine translation lecture pdf`
- `"information retrieval" course 2024 OR 2025 lecture slides pdf schedule "dense retrieval" "learned sparse" university course website`
- `University of Amsterdam "Information Retrieval 1" 52041INR6Y course site slides`
- `"CS 646" OR "CS646" information retrieval UMass Zamani 2024 OR 2025 slides`
- `"search engines" OR "information retrieval" graduate course 2025 github.io lecture slides pdf ColBERT SPLADE RAG "lecture 1"`
- `course "retrieval" "large language models" seminar OR course 2025 schedule slides github.io "neural information retrieval" ...`
- `"computational morphology" OR "linguistic typology" course lecture slides pdf 2024 OR 2025 university schedule computational linguistics`
- `Lei Li UCSB "CS 291" OR "CS 190" machine translation OR "multilingual" course slides lileicc.github.io/course`
- `IIT Bombay Pushpak Bhattacharyya CS772 OR CS626 2024 OR 2025 lecture slides machine translation Indian languages course page`
- `"low-resource" languages NLP university course 2024 OR 2025 lecture slides all lectures pdf schedule "endangered languages" OR "language documentation" computational`

## 选入（12 套）
| sid | 课程 | 学期 | 讲义数 | 方向 | 备注 |
|---|---|---|---|---|---|
| 17-041 | CMU 11-737 Multilingual NLP（Lei Li） | Fall 2023 | 20 | 多语言/MT | 24+1 讲中 20 讲有幻灯片；4 次嘉宾讲座与 2 讲无幻灯片；NAT 讲链接错位已按文件名归位 |
| 17-042 | JHU EN 601.468/668 Machine Translation（Koehn） | Fall 2026（进行中） | 23 | MT | 官方 Syllabus 已为全部 23 讲链接幻灯片；https 证书主机名不符，按官方 http 链接下载 |
| 17-043 | Charles Univ ÚFAL NPFL120 Multilingual NLP | Summer 2026（最后一次开设） | 13 | 多语言/低资源 | 第 12 讲仅 Google Slides 发布页，已由主线程补存其 HTML 本体（见上文“主线程补救”） |
| 17-044 | ÚFAL NPFL087 Statistical Machine Translation（Bojar） | Summer 2026 | 12 + 4 aux | MT | 10 讲官方仍链接 2019/20 版幻灯片 |
| 17-045 | LMU Machine Translation（Fraser） | Summer 2023 | 17 + 2 aux | MT/低资源翻译 | 含双语词向量、无监督 NMT、迁移学习、多语言预训练 |
| 17-046 | CMU 11-324/11-824 Subword Modeling（Mortensen） | Spring 2026 | 22 + 2 aux | 计算语言学（形态/正字法/类型学） | 含 Totonac 课堂练习 |
| 17-047 | ÚFAL NPFL094 Morphological and Syntactic Analysis（Zeman） | 2025/26 冬季讲义集（页面现为 2026/27） | 11 | 计算语言学（形态/句法） | 学期进行中，讲义可能更新 |
| 17-048 | Edinburgh INFR11145 TTDS（Magdy, Ross） | 2024-25 Sem 1 | 18 | IR/RAG | 第 5 讲官方链接错指第 12 讲文件（SHA256 相同），该讲实际未发布 |
| 17-049 | Waterloo CS 451/651 Data-Intensive Distributed Computing（Jimmy Lin） | Fall 2025 | 21 | IR/大规模文本处理 | 12/2 LLMs 一讲无幻灯片 |
| 17-050 | Stanford CS224U NLU（Potts） | Spring 2023 | 16 | IR/RAG/评测 | 含 1 份官方链接的 Google Drive 公开 PDF |
| 17-051 | TU Wien Advanced Information Retrieval（Hofstätter） | Summer 2022 | 11 | 神经 IR | 三年前经典，写 old_reason；固定提交 fbdc44cd |
| 17-052 | UZH NLP for Low-Resource and Marginalized Language Varieties（Sina Ahmadi） | Spring 2026 | 4 + 4 aux | 低资源 NLP | 研讨课，教师讲授仅 4 讲，其余为学生论文研读 |

## 排除 / 未采用及原因
- **Edinburgh NLU+（NLU-11，2023-24/2024-25）**：讲义全部托管在 git.ecdf.ed.ac.uk，从本机访问超时（curl 60 s 无响应、GitLab API 亦超时）；opencourse 只镜像了个别周的文件，不完整。未建种子。
- **Edinburgh ANLP 2025-26**：讲义同样全部在 git.ecdf.ed.ac.uk，无法下载；且属通用 NLP 入门。未建种子。
- **Edinburgh MT（INFR11062）**：已停开并入 NLU+；旧主页返回 410。
- **CMU 11-642 Search Engines（Callan）**：boston.lti.cs.cmu.edu 证书链不完整，脚本（urllib 校验证书）无法下载；不绕过。
- **CMU 11-737 Fall 2022（Neubig，phontron.com）**：同课程不同学期，已收 Fall 2023；且日程页链接解析为 0 个 PDF。
- **UCSB CS291K Deep Learning for MT（Lei Li，Fall 2021）**：与 CMU 11-737 F23 同一教师、幻灯片高度重合，且早于 2023，不收。
- **JHU 601.467/667 Intro to HLT（Fall 2026）**：学期进行中，11/3 与 12/3 讲次尚无幻灯片，9/17 无幻灯片，暂不完整；且为 HLT 综述课。
- **Stanford CS276 IR**：主页标 Spring 2019，日程为更早学期的 Coursera 式材料，混杂且老旧；以 TU Wien AIR 作经典替代。
- **Stanford CS224V（Fall 2026）**：学期进行中，幻灯片主要在 Canvas；Berkeley 智能体课已由主线程复用。
- **UMass CS 646 Fall 2023 / CS 546**：课程页无幻灯片链接（讲义在 Moodle）。
- **UvA Information Retrieval 1**：未找到官方公开讲义页（仅第三方镜像），讲义在 Canvas。
- **Oregon State AI539 Advanced IR（2025 春）**、**UIUC CS 510**：幻灯片在 Canvas/Coursera，需登录。
- **Texas A&M CSCE 670 F25**：课程站 404。
- **NUS CS6101**：站点 404。
- **UF LIN 6932 / Saarland 低资源 NLP 研讨课**：论文研读型，无教师讲义。
- **IIT Bombay CS772/CS626**：未找到公开的近年课程讲义页。
- **CMU 11-724 / UW LING 575 / LMU 计算形态学 2016 / Heidelberg 2013**：前两者未找到公开讲义；后两者过旧。

## 疑点
- 17-043 第 12 讲（Contextual Word Embeddings）原为缺口，已由主线程补存 Google Slides 发布页 HTML，13/13 讲齐全。
- 17-048 第 5 讲官方链接错误导致该讲幻灯片缺失；17-052 为研讨课，教师讲义仅 4 讲。
- 17-042 与 17-047 所在学期仍在进行，后续讲义可能被教师更新。
- 17-049 偏数据工程/分布式，计入“IR 与大规模文本处理”；17-050 是 NLU 课，计入 IR/RAG 因其检索增强 ICL 单元。

## 分叉 d：分布式/推理服务/高效 ML 与 LLM 补充课（17-061 起）

检索日：2026-10-29。种子：scripts/seeds/17_university_courses_seed_d_cn.json。页面读取方式：`materials_en.py links`、WebFetch、WebSearch（查询原样记录如下）；未登录任何平台。

### 检索/浏览记录
| 查询或页面 | 结果 | 处理 |
|---|---|---|
| https://dlsyscourse.org/lectures/ （CMU 10-414/714 DLSys） | 页面日程 8/25 起为周二/周四、11/3 Democracy Day，与 2026 年日历一致，即 Fall 2026 正在进行；第 17、19、20、22、23 讲只有视频或无材料，讲义多为 2022 公开版沿用 | 排除：学期未结束、讲义不全；dlsys.cs.cmu.edu 域名无法解析，未找到往届完整官方存档 |
| WebSearch `10-414/714 Deep Learning Systems Fall 2025 lectures slides Tianqi Chen Dettmers` | 仅第三方博客/笔记 | 不采用第三方 |
| https://efficientml.ai/schedule/ | HTTP 522 | 改用 MIT HAN Lab 官方课程页 |
| https://hanlab.mit.edu/courses/2024-fall-65940 | 23 讲全部有 Dropbox 幻灯片链接；课程列表有 2026 Fall（进行中）、2024、2023、2022，无 2025 | 选入 17-061（Fall 2024）；全套约 1.1 GB，单文件最大约 320 MB（<400 MB） |
| https://stanford-cs229s.github.io/ | 404 | 改查 cs229s.stanford.edu |
| https://cs229s.stanford.edu/fall2023/calendar/ | 11 份 Google Slides；6 次嘉宾讲座无幻灯片，2 讲为占位链接 | 选入 17-065（Google Slides 官方导出 PDF）；fall2024 页仅复制了 9 份同样幻灯片，不作新学期 |
| WebSearch `"15-779" OR "15-849" CMU machine learning systems LLM course slides 2025` | 找到 https://www.cs.cmu.edu/~zhihaoj2/15-779/ | 选入 17-062（Fall 2025，17 份 PDF） |
| https://hao-ai-lab.github.io/dsc204a-f25/ → haoailab.com/dsc204a-f25 | UCSD DSC 204A Fall 2025，17 份幻灯片 + 17 份 scribe 笔记 | 选入 17-063 |
| https://www.cs.cornell.edu/courses/cs6787/{2023fa,2024fa,2025fa}/ | 404；2021fa 可访问但过旧；2026sp 第 2、3、11、14 讲未发布幻灯片 | 排除（不完整/过旧），2026sp 仅作备选 |
| https://www.cs.cornell.edu/courses/cs4787/2025fa/ | Principles of Large-Scale ML，28 讲中 27 讲有讲义（PDF/HTML 笔记本/幻灯片） | 选入 17-064 |
| https://ucbsky.github.io/cs294-162-fa24/、https://dsc204a.github.io/ | 404 | 跳过 |
| WebSearch `EECS 598 "Systems for Generative AI" Michigan Chowdhury schedule slides` | UMich CSE 585 为论文研讨课，幻灯片不公开；Princeton COS 597K（Fall 2024）页面无讲义；Berkeley CS294-162 Fall 2023 在 Notion | 排除：研讨课/无公开讲义/Notion 页面无法按官方文件核验 |
| https://basil-web-01.colorado.edu/courses/fa25/csci7000/schedule/ | 只有论文链接 | 排除（论文研讨课） |
| https://zirui-ray-liu.github.io/teaching/25sp-intro-llmsys （Minnesota CSCI 8980） | Google Slides，多讲无幻灯片，日程无日期 | 排除（缺讲较多） |
| WebSearch `university course "efficient" LLM inference systems ...` | IIT Delhi COL851 2025 页面讲义与论文混排、学期进行中 | 排除 |
| WebSearch `UIUC CS 598 "AI Efficiency" ...` | 学生报告型研讨课 | 排除 |
| WebSearch `Stanford CS329H Machine Learning from Human Preferences lecture slides schedule`；https://web.stanford.edu/class/cs329h/fall2025/ | 幻灯片不在课程页（只有 Google Doc 大纲） | 排除 |
| WebSearch `Harvard CS 2881 AI safety Boaz Barak Fall 2025 lecture slides`；https://boazbk.github.io/mltheoryseminar/ | 页面已切换到 Fall 2026（进行中），幻灯片多为 Google Slides/外链 | 排除 |
| https://web.stanford.edu/class/cs329x/ | 2026-27 学期进行中（10 讲），无往届存档 | 排除 |
| WebSearch `Yu Meng UVA CS 6501 large language models course schedule slides pdf` | UVA CS 6501 Spring 2025（21 份 PDF）；HKUST COMP 4901B Fall 2025（23 讲） | 选入 17-067、17-066 |
| https://nyu-cs2590.github.io/fall2024/ | 无讲义链接 | 排除 |

### 选入（下载结果见状态）
- 17-061 MIT 6.5940 TinyML and Efficient DL Computing，Fall 2024，23 讲
- 17-062 CMU 15-779 Advanced Topics in ML Systems (LLM Edition)，Fall 2025，17 份
- 17-063 UCSD DSC 204A Scalable Data Systems，Fall 2025，17 份（+17 份 scribe aux）
- 17-064 Cornell CS 4787/5777 Principles of Large-Scale ML，Fall 2025，27 讲（+4 aux）
- 17-065 Stanford CS 229S Systems for ML，Fall 2023，11 讲
- 17-066 HKUST COMP 4901B Large Language Models，Fall 2025，23 讲（+20 批注版 aux）
- 17-067 UVA CS 6501 NLP（LLM 专题），Spring 2025，21 份

### 下载结果（2026-10-29，均为本轮新下载，无兄弟库复用）
17-061～17-067 共 7 套全部 VERIFIED（`fetch 17 --sid` 逐个运行）。合计约 1.4 GB，其中 MIT 6.5940 约 1.08 GB。
疑点：Cornell CS4787 第 1、18 讲官方讲义 PDF 仅 2 页（文字约 5000 字符，为官方原样）；该课 19 讲为 notebook 渲染 HTML，公式/脚本依赖 cdnjs 在线资源。CMU 15-779 学期（Fall 2025）由日期与 Piazza 链接推定。CS229S 用 Google Slides 自带导出 PDF。
