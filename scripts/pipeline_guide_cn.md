# 采集流水线工作说明（低资源语言 LLM 资料库）

库根目录：`/root/low_resource_language_llm_literature`。所有命令在库根目录下运行，一律 `python3 -I scripts/<脚本>`（宿主机无 pip；pypdf 在 `/root/.cache/lrl_lit/pylib`，暂存在 `/root/.cache/lrl_lit/staging`）。脚本改造自 `/root/large_model_multimodal_literature/scripts/`（其他会话的库，**只读，绝不写入**）。

本轮只收集、下载、核验、整理；不训练、不部署、不执行下载来的代码。

## 0. 总规则
- 检索日 2026-10-29；近三年窗口：首次公开日期 ≥ 2023-10-29。首次公开 = arXiv v1 提交日（无 arXiv 用最早公开版本日期）；正式发表、最新版本日期另记。
- 每类目标约 50 篇**已核验**；每类近三年占比 ≥85%（争取 ≥90%），三年前经典补充每类最多 5 篇，种子逐篇写 `old_reason`。
- 一篇论文只能有一个主分类（`scripts/state/claims_en.json` 先到先得）；交叉分类只在有实质依据时加 `cross` + `cross_reason`；不得靠重复标注凑数。
- 只用合法公开来源（arXiv、ACL Anthology、PMLR、OpenReview、作者/机构主页等），不绕过登录、付费墙。
- 不以重复版本、无关论文、零散章节或仅链接条目补额。
- “小语种”≠“低资源语言”：记录研究实际涉及的语言、资源条件与文字特征，不混用。
- 不把普通英文模型论文包装成小语种研究：每条必须标 `relevance` = `直接相关` 或 `通用支撑`，`通用支撑` 要写清对小语种开发的用途。
- 每类“直接相关”应占多数（建议 ≥60%，01 数学基础类除外，02 类以语言学/多语言为主）。

## 1. 论文（01–16）
种子：`scripts/seeds/<NN_slug>_seed_cn.json`（JSON 数组）。字段：

| 字段 | 说明 |
|---|---|
| `sid` | `NN-001` 起编号，唯一且不复用 |
| `arxiv` | arXiv ID（无版本号）；不确定时只给 `title`，`resolve` 会按标题检索并回写 |
| `title` | 英文原题 |
| `subtopic` | 子方向（中文） |
| `type` | `原始研究` / `综述` / `技术报告` / `学术教程` / `基准与数据集` |
| `priority` | `高` / `中` / `低` |
| `relevance` | `直接相关` / `通用支撑` |
| `reason` | 选入理由（中文一句，不写未经核实的结论） |
| `old_reason` | 首次公开早于 2023-10-29 时必填 |
| `cross`, `cross_reason` | 交叉分类编号列表与依据 |
| `reserve` | `true` = 备选，主列表核验数不足 `--target` 才下载 |
| `cross_only` | 主分类在别类，本类只作交叉标签（不下载不计数），写 `cross_reason` |
| `exclude`, `exclude_reason` | 人工排除 |
| `team` | 团队署名时的团队名 |
| 非 arXiv 文献 | `pdf_url`（合法公开全文，如 `https://aclanthology.org/2024.acl-long.1.pdf`）、`landing_url`、`authors`（列表）、`first_public_date`、`date_precision`（日/月/年）、`first_public_basis`、`version`、`version_date`、`doi`、`venue` |

命令：
```bash
python3 -I scripts/papers_en.py search '<arXiv 查询>' --max 50 --sort relevance|submittedDate
#   例：'abs:"low-resource" AND abs:tokenizer AND submittedDate:[202310290000 TO 202610290000]'
python3 -I scripts/papers_en.py resolve NN          # 元数据；ID 与标题不符时按标题纠正
python3 -I scripts/papers_en.py download NN --target 55   # 断点续跑；已在兄弟库核验过的 PDF 复制并重新核验（记“已有复用”）
python3 -I scripts/papers_en.py status NN           # 统一进度句式 + 近三年占比 + 失败明细
python3 -I scripts/papers_en.py text NN <sid> --pages 2   # 人工核对首页
python3 -I scripts/papers_en.py manual NN <sid> --note '<核对了什么>'   # 仅 pending 且硬检查通过
python3 -I scripts/papers_en.py brief NN [--missing-only] # 摘要汇编 -> scripts/work/，用于写注释
python3 -I scripts/papers_en.py venue NN            # OpenAlex 发表渠道
```
核验（计数前提）：HTTP 200、`%PDF-`、pypdf 可解析、≥4 页、可抽取字符 ≥12000、非补充材料；首两页标题有效词匹配 ≥0.8；首作者姓氏/团队名出现；有参考文献标题。只差软检查的进 `pending`，人工用 `text` 核对后 `manual` 提升（note 写明核对内容）。失败条目找替代，不计数。

**近三年比例控制**：目标 ≥90%。先下载近三年文献；经典论文最多 5 篇。别类已认领的论文会被标 `duplicate_elsewhere`，需要时在本类加 `cross_only` 条目并用备选补足。

### 注释 `scripts/annotations/<NN_slug>_annot_cn.json`
以 `sid` 为键。依据摘要 / arXiv 注释 / PDF 正文（`text` 命令）填写；未核实写 `待核实`；不适用写 `不适用`。**不得编造**数值、规模、语言列表或结论；结果一律“作者称/摘要称”。

```json
{
 "03-001": {
  "relevance": "直接相关",
  "relevance_use": "对小语种开发的用途（通用支撑必填）",
  "summary": "中文 2–3 句：做了什么、怎么做；结论用“作者称”转述",
  "languages": "实际涉及语言（多时写“N 种，含 X/Y/Z”）",
  "language_families": "语系（摘要/正文可见者）",
  "scripts": "文字系统（拉丁/西里尔/天城/阿拉伯/汉字/埃塞俄比亚/…）",
  "resource_condition": "作者对资源条件的界定（及依据）",
  "base_model": "基座模型", "adaptation": "适配方式（持续预训练/指令微调/LoRA/词表扩展/…）",
  "data_type_size": "数据类型与数据量",
  "translation_synthetic_teacher": "是否依赖机器翻译/合成数据/高资源语言教师模型",
  "native_human_eval": "是否有母语者审核或人工评价",
  "capability_effects": "对目标语言、原有语言、代码能力的影响（作者称）",
  "resources_availability": "训练/推理资源；代码与数据是否公开（链接）",
  "eval_tasks": "评测任务/基准",
  "benchmark_origin": "原生构建 / 翻译 / 混合 / 不适用 / 待核实",
  "contamination_control": "数据污染控制措施或 待核实",
  "limitations": "作者报告的局限",
  "evidence_scope": "通用方法证据 / 特定语言案例证据 / 两者",
  "result_source": "作者自报 / 独立复现 / 不适用",
  "distinctions": "如相关：区分“用目标语言回答” vs “用该语言正确推理/执行工具”；机器翻译文本 vs 自然本地文本",
  "field_basis": "摘要 / 摘要+正文（第几节或页） / 摘要+arXiv注释",
  "top_rank": 3,
  "top_reason": "仅本类优先阅读前 10 篇填写"
 }
}
```

### 检索日志
每类写 `scripts/work/search_log_<NN>_cn.md`：检索日期、查询式（原样）、返回数、选入/排除原因、替代关系、未完成原因。

## 2. 课程（17）与书籍（18）
`python3 -I scripts/materials_en.py fetch 17|18 [--sid ...] [--retry-failed]`；`status 17|18`；`links <官方页面> --pattern '\.pdf$'`（列出官方页面链接）。
种子格式与兄弟库相同（参考 `/root/large_model_multimodal_literature/scripts/seeds/13_university_courses_seed_a_cn.json`、`14_books_seed_cn.json`，只读）：一套课程/一本书一条，`files` 列出全部文件（文件名带语言后缀），`expected_items`（课程讲义数）、`min_pages`（书）、`mirror`（完整 HTML 书）。必填：`prereq`（先修）、`coverage`（内容范围）、`stage`/难度、`term`/`term_year`（课程学期）或 `edition`/`edition_year` 与原著年份、`verification_basis`、`completeness_note`、`reason`、`cross`。
- 兄弟库里已核验的同一份资料：在 file 条目加 `"copy_from": "/root/<兄弟库>/<相对路径>"`，脚本复制并重新核验，记“已有复用”。
- 同课程不同学期、同书不同版本不重复计数；只用作者/出版社/学校合法公开的完整版本；分章开放的书必须核对目录并保存全部正文。

## 3. 工程资料（19）
`python3 -I scripts/engineering_en.py refs <github_url>`（列出 tag，不克隆）；`fetch [--eid E-xx]`；`status`。
种子 `scripts/seeds/19_engineering_seed_cn.json`：`eid, stage, name, repo, ref`（固定 tag 或完整提交号，禁止写 main/latest）、`purpose, core_modules, related_papers`（库内 sid 列表）、`learning_value`、可选 `docs: {"path": "docs", "format": "...", "scope_note": "...", "min_toc_resolved": 0.95}` 或 `docs: {"repo": "...", "ref": "...", "path": "..."}`。
脚本只保存源码、文档与配置示例；自动剔除权重/数据/归档/二进制/>5MB 文件并记录；生成原始结构归档包 `*_original_en.tar.gz` 与文件名加语言后缀的只读副本（`path_map_en.csv`）。文档集需目录（TOC）解析率 ≥95% 才计为“完整文档集”。
