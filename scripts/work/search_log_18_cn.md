# 类别 18 检索日志：完整教科书、专著与参考书

- 检索日期：2026-10-29
- 种子：`scripts/seeds/18_books_seed_cn.json`（18-001 … 18-053，共 53 条，一本书一条）
- 下载/核验：`python3 -I scripts/materials_en.py fetch 18`；结果见 `scripts/state/results/18_books_en.json`，运行日志 `scripts/work/fetch_18_run*.log`
- 兄弟库（只读）：`/root/large_model_multimodal_literature`（14 类书籍种子与结果）、`/root/machine_learning_deep_learning_literature`（`scripts/cache/materials_results_en.json` 与 `books/`）。同一版本的文件用 `copy_from` 复用，脚本复制后重新核验，记为“已有复用”，不算新下载。

## 1. 检索来源与查询（原样记录）

| # | 渠道 | 查询 / 访问 | 返回 | 用途 |
|---|---|---|---|---|
| 1 | 兄弟库种子与结果 | 读取 `14_books_seed_cn.json`、`14_books_en.json`、`materials_results_en.json`、`C12_books_cn.json` | 40 + 59 条 | 确定可复用的同版本 PDF 及其官方 URL |
| 2 | WebSearch | `Language Science Press open access book linguistic typology morphology introduction` | 10 条 | 未直接命中类型学教科书，转查 LangSci 丛书目录 |
| 3 | WebSearch | `Springer open access book European Language Equality 2023 pdf` | 10 条 | 确认 ELE（10.1007/978-3-031-28819-7）开放获取 |
| 4 | WebFetch | `https://langsci-press.org/catalog/series/tmnlp`（TMNLP 丛书） | 27 种 | 选入 MT for everyone、Unicode Cookbook、Language technologies for a multilingual Europe |
| 5 | WebSearch | `langsci-press.org catalog book textbook "Textbooks in Language Sciences" series` | 19 条 | 找到 TBLS 丛书页 |
| 6 | WebFetch | `https://langsci-press.org/catalog/series/tbls` | 31 种 | 选入 Language and computers、Grammatical theory 第 5 版、Corpus linguistics、Analyzing meaning 第 3 版、Indigenous languages of the Americas: Sounds、Multilingualism、Linguistics Olympiad |
| 7 | WebFetch | `https://langsci-press.org/catalog/series/sidl`（Studies in Diversity Linguistics） | 35 种 | 均为专题论文集/专著，未选入（见排除） |
| 8 | Zenodo API | `https://zenodo.org/api/records/<id>`（LangSci 各书 DOI 记录） | 10 条 | 取得整书 PDF 文件链接、出版日期与许可（CC BY / CC BY-SA） |
| 9 | curl HEAD | Springer `content/pdf/<doi>.pdf` × 5 | 2 个 PDF | ELE、ELG 为 PDF（开放获取）；Towards Responsible MT（978-3-031-14689-3）与 Translation Quality Assessment（978-3-319-91241-7）返回 HTML（非开放获取），排除 |
| 10 | WebSearch | `"Ultra-Scale Playbook" PDF download nanotron free` | 15 条 | 官方 HF Space 文件区有 PDF；第三方“免费 PDF”站点为垃圾站，不用 |
| 11 | WebSearch | `stas00 ml-engineering "Machine Learning Engineering Open Book" pdf release download` | 19 条 | 作者在 HF Hub `stas/ml-engineering-book` 托管 PDF（CC BY-SA 4.0） |
| 12 | WebSearch | `Rothwell "Translation Tools and Technologies" Routledge 2023 open access pdf` | 10 条 | 非开放获取，排除 |
| 13 | WebSearch | `Blitzstein Hwang "Introduction to Probability" second edition free PDF official probabilitybook.net` | 18 条 | 官方仅指向在线版 probabilitybook.net，未找到官方 PDF；搜索结果中“免费 PDF”多为盗版/垃圾站，未收 |
| 14 | WebSearch | `Raschka "Machine Learning Q and AI" free online open access all chapters 2025` | 10 条 | 官方仅提供样章，未收 |
| 15 | GitHub API | `repos/NiuTrans/MTBook`、`repos/NiuTrans/NLPBook`（contents、commits） | — | MTBook 完整 PDF（提交 a55dd1a8，2024-09-14）；NLPBook 完整 PDF（提交 b1255a0f，2026-10-19），固定到提交号 |
| 16 | GitHub API | `repos/harvard-edge/cs249r_book/releases` | 8 个 release | Vol1 v0.8.0、Vol2 v0.3.0（2026-10-24） |
| 17 | arXiv abs 页 | 2501.09223、2504.12501、2311.17633、2412.05265、2404.17625、2403.14606 | — | 最新版本分别为 v4、v12、v2、v5、v3、v4，与兄弟库一致，可复用 |
| 18 | HF API | `api/spaces/nanotron/ultrascale-playbook`、`api/models/stas/ml-engineering-book` | — | 固定提交 c93890dd、9966fd7d |

## 2. 预检（下载到会话暂存目录，仅用 pypdf 抽取文本，不执行任何下载内容）

- LLMBook（赵鑫等《大语言模型》）：391 页，第 7–14 页为目录，但中文字体编码使抽取为乱码，自动检查找不到“目录”。人工核对目录页可读条目（BPE、WordPiece、LLaMA、BIG-Bench、HELM、C-Eval）与五部分书签，设 `toc_override`。兄弟库 14-007 正因此失败。
- MLHP（斯坦福）：当前版（Last-Modified 2026-09-23）第 4 页有 “TABLEOFCONTENTS”，脚本正则可匹配。兄弟库 14-011 失败时的版本不同。
- ML Systems：Vol1 第 8 页 “Contents”，Vol2 第 5 页 “Table of contents”。兄弟库 14-028 把两卷当作一本书，以 Vol2 为主文件而失败。两卷书名不同（Introduction to Machine Learning Systems / Scaling Machine Learning Systems），本库分开计数，列为疑点。
- Ultra-Scale Playbook：官方 PDF 是 1 个超长页面（1133.9×102047.2 pt），可抽取 204,286 字符，含目录、全部章节、结论、附录与参考文献，因此 min_pages 设为 1 并在 completeness_note 说明。
- Happy-LLM（Datawhale）：PDF 用康熙部首兼容字符（如“⼤”），中文书名精确匹配会失败；无目录标题；属于社区教程。未收。
- Goodfellow《Deep Learning》HTML：index 页含 “Table of Contents”，rnn.html 含 “Recurrent”，bib.html 含 “Bibliography”，用作 must_contain。

## 3. 排除与替代

| 候选 | 原因 | 处理 |
|---|---|---|
| Manning, Raghavan & Schütze《Introduction to Information Retrieval》 | 官方站点 nlp.stanford.edu 从本机无法连接（`connect … No route to host`，80/443 都不通） | 用 Croft, Metzler & Strohman《Search Engines: Information Retrieval in Practice》（作者官网合法全文）替代 |
| Bishop & Bishop《Deep Learning: Foundations and Concepts》 | 官网只提供在线阅读，没有合法的完整下载版 | 不收 |
| Blitzstein & Hwang《Introduction to Probability》第 2 版 | 未找到官方 PDF，只有在线版 | 不收 |
| Raschka《Machine Learning Q and AI》等 | 官方只提供样章 | 不收 |
| Xiao & Zhu《Introduction to Transformers: an NLP Perspective》（arXiv 2311.17633） | 内容已并入同作者 NLPBook（README 说明），避免重复 | 收 NLPBook，不收该书 |
| Rothwell 等《Translation Tools and Technologies》、Moniz 等《Towards Responsible MT》、Moorkens 等《Translation Quality Assessment》 | 不是开放获取 | 不收 |
| LangSci Studies in Diversity Linguistics 各卷 | 都是窄专题论文集，不属于教科书/参考书 | 不收；类型学方向由 TBLS 教材（Indigenous languages of the Americas、Kroeger）承担 |
| Happy-LLM | 社区教程，PDF 的中文抽取与书名校验有问题 | 不收 |
| LangSci《Teaching translation in the age of generative AI》 | 翻译教学方向，与模型开发关系弱 | 不收 |
| MT for everyone 中文译本（LangSci 492） | 与英文原书是同一本书 | 只收英文原版 |

## 4. 复用说明

有 `copy_from` 的条目是兄弟库已核验过的同版本文件：arXiv 版本号一致，或官方 URL 一致且文件大小与 Last-Modified 吻合（例如 SLP3：官方 26,506,144 字节，与兄弟库一致，草稿日期 2026-08-19）。复用文件由本库脚本重新核验，计为“已有复用”，不算新下载。

## 5. 运行结果（2026-10-29）

- `fetch 18` 一次跑完（日志 `scripts/work/fetch_18_run1.log`）：53 条全部 verified，0 失败，0 待核验。
- 来源：新下载 23 条（含 2 个 HTML 离线镜像：Goodfellow《Deep Learning》28 页、How to Scale Your Model 16 页，wget rc=8 是个别页面资源 404，must_contain 全部通过）；已有复用 30 条（兄弟库同版本文件，本库重新核验）。
- 按方向：NLP 与计算语言学 10；机器学习与深度学习 9；多语言/机器翻译/低资源 9；数学、概率、统计与优化 8；大模型训练/适配/评测 7；信息检索/RAG/智能体 5；分布式训练/推理/部署 5。
- 2023 年及以后版本（edition_year ≥ 2023）：38/53（71.7%）。
- 用了覆盖开关的条目：18-040《大语言模型》设 toc_override，理由见第 2 节，已人工核对；18-050 Ultra-Scale Playbook 设 min_pages=1（单个超长页面）。
- ISBN 与 DOI：从各书 PDF 前 10 页版权页抽取后回填种子，共 19 条有 ISBN；作者/机构网络公开版不适用或待核实，均已在种子中写明。
- 未完成/疑点：Manning IR 书因主机网络不可达未收；ML Systems 两卷分开计数；SLP3、NLPBook、MLHP、ML Systems、Bekman 均为持续更新的在线版，已用提交号、release 或 arXiv 版本号固定所收版本。
