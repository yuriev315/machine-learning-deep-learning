# 检索与筛选记录

检索与整理日期：2026-10-29（UTC）。近三年窗口：首次公开日期 2023-10-29 至 2026-10-29。

## 1. 检索来源

| 来源 | 用途 | 访问方式 |
|---|---|---|
| arXiv API（export.arxiv.org） | 按 arXiv ID 批量取元数据（标题、作者、v1 日期、最新版本号、摘要、comments、journal_ref、DOI）；ID 与预期标题不符时按标题检索 | 公开 API，跨进程限速 ≥ 4 秒/次 |
| arXiv PDF（arxiv.org/pdf） | 论文全文，下载 API 返回的最新版本号（如 v3） | 公开，限速 ≥ 4 秒/次 |
| Semantic Scholar Graph API（batch） | 正式发表渠道、发表日期、DOI | 公开 API，单次批量请求 |
| Crossref API | 仅有 DOI 的论文（Nature 开放获取论文）的元数据 | 公开 API |
| Nature 官网 | 3 篇开放获取论文的正式版 PDF | 公开开放获取 |
| 作者/出版社/大学官网 | 书籍与课程讲义全文 | 只用官方公开链接（含作者在官网上给出的 Google Drive、Dropbox、GitHub Releases 链接） |

未使用：付费数据库、需要登录或填表的下载页、影子图书馆、第三方转载站。

## 2. 选文方式

- 论文候选名单由人工按各类别主题拟定（依据对领域代表性工作的了解：顶会/顶刊论文、广泛采用的方法、基准与综述），每条写明选入理由；随后用 arXiv API 逐条核对标题、作者与日期。
- 候选名单与检索规则见 `scripts/seeds/`：每行 `arXiv ID | 预期标题 | 类型 | 交叉分类 | 选入理由 | 三年前保留理由`。ID 不确定时填 `-`，由脚本按标题检索。
- ID 核对规则：arXiv 返回标题与预期标题的词集合 Jaccard ≥ 0.6 才接受；否则按标题检索，最佳匹配 ≥ 0.75 才接受；仍不匹配的条目记为未解析并删除或替换（不猜测）。
- 年份规则：论文按 arXiv v1 提交日（无 arXiv 时用 Crossref 最早日期）判断是否在近三年窗口内；每类三年前的经典补充不超过 5 篇，并写明保留理由。
- 交叉分类：仅当论文内容确实涉及另一类别主题时标注（例如 LLM 评测基准同时属于 C06 与 C10）。统计"每类完成数"时只按主分类计数，交叉分类单列，不重复计数。
- 书籍与课程：只收作者、出版社或大学官方公开的完整版本；同一本书只收最新完整版本（例如 ISLP 收录、内容相同的 ISLR2 不重复收录）。

## 3. 下载与核验规则

- 论文：HTTP 200 → `%PDF-` 文件头 → pypdf 可解析 → 页数 ≥ 4（排除仅摘要文件）→ 前两页文本包含 ≥ 80% 标题词 → SHA256 去重。
- 书籍（PDF）：上述检查 + 页数不低于该书的保守下限（如 ESL ≥ 700 页）+ 前 8 页包含书名短语；同时从版权页提取 ISBN（提取到才登记，不猜测）。
- HTML 书籍/讲义：从官方目录页解析全部章节链接，逐页检查 HTTP 200、text/html、正文字符数下限、首页含书名；用 wget（`--page-requisites --convert-links`，不递归）保存可离线阅读的页面及图片样式。
- 多文件课程资料包：官方讲义索引列出的全部分册都下载并核验才计为 1 份资料包。
- 失败、仅链接、需登录/填表、只给在线阅读的资料一律不计数，记入 `download_failures_cn.csv`。

## 4. 主要排除与替代记录

| 资料 | 原因 | 处理 |
|---|---|---|
| Szeliski《Computer Vision: Algorithms and Applications》第 2 版 | 官网下载需填写姓名与邮箱 | 不绕过；以 Torralba 等《Foundations of Computer Vision》替代 |
| Manning 等《Introduction to Information Retrieval》 | 官网连接超时 | 记入失败表，可续跑 |
| Peters 等《Elements of Causal Inference》 | 出版社页 403，未找到官方直链 | 以 Hernán & Robins《What If》覆盖因果推断 |
| Bishop & Bishop《Deep Learning: Foundations and Concepts》 | 官方只提供免费在线阅读，PDF 需购买 | 不以在线阅读页替代 |
| "Loss Functions in Deep Learning: A Comprehensive Review"（C01 候选） | 预设 arXiv ID 对应另一篇论文，按标题检索无可信匹配 | 删除，不猜测 |

（续跑中新增的排除项见 `download_failures_cn.csv`。）

## 5. C11 大学课程讲义的检索与排除（2026-10-29）

共核对 378 个 URL（逐个顺序请求，按主机限速）：PDF 都确认了 `%PDF` 文件头和页数，HTML 逐页确认正文长度。符合"官方、完整、系统"标准的资料包有 39 个；其中 Cornell CS4780 后来判为不完整（见下表），实际收录 38 个，没有达到约 50 的目标。

| 候选 | 处理 | 原因 |
|---|---|---|
| Cornell CS4780 Fall 2018 讲义 | 撤出，不计数 | 官方索引共 21 项，第 21 项为无文本层的扫描 PDF，无法完整保存 |
| UIUC Telgarsky《two.pdf》2023 | 改收 2021 完整版 | 2023 版为作者自述的进行中草稿（DRAFT 1） |
| Toronto CSC2541 2021 | 不收 | 12 讲中只有前 5 讲有讲义 |
| Stanford CS236 notes | 不收 | 只有 5 页，标注"under construction" |
| Stanford CS324 W2022 | 不收 | 3 讲只有占位页（幻灯片授课） |
| Stanford CS224N notes | 不收 | 只有少数几讲有讲义，且 2019 版与 2023 草稿混杂 |
| Berkeley CS70 Fall 2026 | 改收 Spring 2026 | 学期进行中，讲义尚未完整 |
| Berkeley Stat240 S21、Stat260 F19 | 不收 | 讲义不完整，或完整性无法确认 |
| UIUC CS542（Nan Jiang） | 不收 | 讲义来自多个年份，本学期进行中 |
| Cambridge MSM 本学年讲义 | 改收上一学年完整版 | 当前版本只有 24 页，仍在编写 |
| EPFL 统计物理讲义 | 不收 | 标注"in construction" |
| Columbia COMS 4771、Stanford EE263 | 不收 | 只有幻灯片，或讲义零散 |
| Stanford EE364A | 不收 | 讲义即 Boyd《Convex Optimization》（已在 C12 收录） |
| Edinburgh MLPR | 不收 | 站点只有 IPv6 地址，本机连接超时 |
| Princeton ORF523、COS 324，Milan 课程页 | 不收 | 返回 403，未绕过 |
| Cornell CS4787 | 不收 | 只有进行中的学期，往届 URL 返回 404 |
| UvA DL notebooks、Peyré 讲义、math4ml、Data 100、CS109 阅读材料、EECS16A | 不收 | 以代码为主、未绑定具体课程、非官方课程文本、偏离主题，或页面过短 |
