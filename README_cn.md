# 机器学习与深度学习文献库

> **版权说明：** 下文的数量是资料库收录的总数。其中有再分发许可的 2897 个文件为全文，其余 756 个文件是同路径的 `.url` 占位文件。详见 [LICENSES_cn.md](LICENSES_cn.md) 和 [release_status_cn.csv](release_status_cn.csv)。

本库与 `time_series_literature/` 分开管理，只做文献收集、下载、核验与整理，不包含模型训练或论文实验。整理日期为 2026-10-29（UTC）。近三年窗口为首次公开日期 2023-10-29 至 2026-10-29。

计数口径：只有"原文全文已下载到本地并通过核验"的资料才计入。下载失败、仅有链接、只有部分正文、需要登录或填表的资料都不计数，统一记入 [download_failures_cn.csv](download_failures_cn.csv)。核验通过不等于已经精读全文；论文简介只依据摘要。

## 规模（去重后共 648 份独立资料）

| 类别 | 主分类核验通过 | 近三年占比 | 三年前资料 | 状态 |
|---|---|---|---|---|
| C01 机器学习基础 | 56 | 91.1% | 5 篇经典 | 完成 |
| C02 传统机器学习 | 53 | 90.6% | 5 | 完成 |
| C03 无监督与表示学习 | 56 | 91.1% | 5 | 完成 |
| C04 深度学习基础与训练 | 59 | 91.5% | 5 | 完成 |
| C05 计算机视觉 | 55 | 90.9% | 5 | 完成 |
| C06 自然语言处理与大语言模型 | 57 | 91.2% | 5 | 完成 |
| C07 生成模型 | 56 | 91.1% | 5 | 完成 |
| C08 图机器学习 | 52 | 90.4% | 5 | 完成 |
| C09 强化学习与决策 | 52 | 90.4% | 5 | 完成 |
| C10 可靠性与评测 | 55 | 90.9% | 5 | 完成 |
| C11 大学课程教材与讲义 | 38 个资料包 | 17/38（44.7%）；4 份无版本日期 | 17 份，均写明保留理由 | **未完成**（目标约 50） |
| C12 教科书、专著与参考书 | 59 本 | 23/59（39.0%）；7 份日期精度不足或无日期 | 29 本，均写明保留理由 | 完成 |

- 论文共 551 篇：原始研究 506 篇、综述 33 篇、教程/讲义式文章 12 篇；近三年 501 篇（90.9%）。每类三年前的经典恰为 5 篇。
- 每类数量只按主分类计数。交叉分类在 catalog 的"交叉分类"列和 `domains/` 各页的"交叉引用"部分列出，不重复计数。
- 课程与书籍不套用论文的 85% 门槛；较早的版本都在"三年前保留理由"列写明原因。

## 目录

| 路径 | 内容 |
|---|---|
| [catalog_cn.csv](catalog_cn.csv) | 统一目录，UTF-8 带 BOM，648 行，每行一份已核验资料，字段见下 |
| [reading_map_cn.md](reading_map_cn.md) | 从数学基础到机器学习、再到深度学习的阅读路线；每类优先阅读 10 份 |
| [search_log_cn.md](search_log_cn.md) | 检索来源、筛选与核验规则、排除记录 |
| [download_failures_cn.csv](download_failures_cn.csv) | 下载失败或不计数的资料及原因 |
| [checksums_en.sha256](checksums_en.sha256) | 3653 个资料文件的 SHA256（`.url` 占位文件按占位文件本身计算），解压全部 Release 包后在根目录执行 `sha256sum -c checksums_en.sha256` 即可校验；原文件的 SHA256 见 `release_status_cn.csv` |
| [papers/](papers/) | 551 篇论文 PDF，命名为 `首次公开年份_第一作者姓_短标题_en.pdf` |
| [books/](books/) | 54 本 PDF 书籍（`作者_书名_版本_en.pdf`）和 5 本官方仅提供 HTML 的书籍（`*_html_en/` 目录，可离线阅读） |
| [university_materials/](university_materials/) | 38 个课程讲义资料包：21 个单 PDF、12 个多 PDF 目录、5 个 HTML 目录（`学校_课程号_学期_LectureNotes_en`） |
| [domains/](domains/) | 12 个分类页，按文献编号引用文件，不复制实体文件 |
| [scripts/](scripts/) | 检索、下载、核验、编目脚本，候选清单 `seeds/`，中文简介 `annotations/`，缓存 `cache/` |

文件名后缀 `_en` 表示原文为英文，`_cn` 表示中文文件。下载时只改了文件名，没有改动原文内容。

## catalog_cn.csv 主要字段

通用字段：文献编号（MLP 论文 / MLU 课程 / MLB 书籍）、主分类、交叉分类、资料类型、标题、作者或教师、学校或机构、发表渠道或出版社、渠道依据、首次公开日期、日期精度、首次公开日期依据、正式发表日期、版本、版本日期、时间窗口、三年前保留理由、DOI/arXiv ID/ISBN、原始来源链接、下载链接、语言、文件格式、本地路径、全文完整性、核验状态、SHA256、选入理由、阅读难度、优先级。

- 论文另有：问题、主要方法、评测范围、简介、简介依据。简介全部依据摘要。
- 课程另有：课程名称、课程代码、学期、先修要求、内容覆盖。
- 书籍另有：章节完整性、先修要求、适合阅读阶段。

各字段的取值来源与注意事项：

- **首次公开日期**：论文取 arXiv v1 提交日（日精度）；3 篇 Nature 论文取 Crossref 日期。
- **版本**：论文记录实际下载的 arXiv 最新版本号。书籍的版本日期取自 PDF 封面或版权页。课程学期取自课程页或讲义页眉；无法确认的标"待核实"。
- **渠道依据**：分为四档。
  - Semantic Scholar 元数据：394 篇，未逐篇核对官方论文集。
  - arXiv comments 或 journal_ref（作者自述）：16 篇。
  - Crossref：3 篇。
  - 未发现正式发表信息：138 篇。这是指"未核实是否已发表"，不等于没有发表。
- **ISBN**：只登记从 PDF 版权页实际提取到的号码，不猜测。

## 核验规则（摘要）

- **论文**：HTTP 200、`%PDF` 文件头、pypdf 可解析、页数 ≥ 4、前两页包含 ≥ 80% 的标题词，并按 SHA256 去重。
- **PDF 书籍与课程**：页数不低于该资料的保守下限，前 8 页包含书名或讲义名；多文件资料包的每个分册都要通过。
- **HTML**：从官方目录页解析出全部章节，逐页检查 HTTP 200、text/html、正文字符数下限，并用 wget 保存页面及图片和样式。

## 续跑（断点续传）

宿主机没有 pip。pypdf 用 PyPI 纯 Python wheel 解压到本目录之外，不安装到系统：

```bash
cd /root/machine_learning_deep_learning_literature
LIB=/path/to/pylib; STAGE=/path/to/staging        # 放在本目录之外的任意可写目录
mkdir -p "$LIB" && curl -sSL -o /tmp/pypdf.whl \
  https://files.pythonhosted.org/packages/04/fc/6f52588ac1cb4400a7804ef88d0d4e00cfe57a7ac6793ec3b00de5a8758b/pypdf-5.1.0-py3-none-any.whl
echo "3bd4f503f4ebc58bae40d81e81a9176c400cbbac2ba2d877367595fb524dfdfc  /tmp/pypdf.whl" | sha256sum -c \
  && python3 -I -c "import zipfile,sys; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])" /tmp/pypdf.whl "$LIB"

python3 -I scripts/resolve_papers_en.py                          # 论文：解析 seeds/C01–C10，已缓存的条目跳过
python3 -I scripts/download_papers_en.py "$LIB" "$STAGE"         # 论文：只下载未核验的条目
python3 -I scripts/build_book_manifest_en.py                     # 书籍清单（PDF 部分）
python3 -I scripts/build_html_manifest_en.py                     # 书籍清单（HTML 部分，重新解析官方目录）
python3 -I scripts/fetch_materials_en.py "$LIB" "$STAGE"         # 书籍与课程：只下载未核验的条目；可在末尾加编号只处理指定条目
python3 -I scripts/build_catalog_en.py                           # 重新生成 catalog / 失败表 / 校验和 / domains
```

新增论文时，在 `scripts/seeds/Cxx_*_cn.txt` 末尾追加一行（格式见文件头注释），然后依次运行上面的解析、下载和编目三步；中文简介写入 `scripts/annotations/`。已有编号保持稳定（`scripts/cache/registry_en.json`）。所有请求都按主机限速（arXiv ≥ 4 秒/次）。不要同时运行两个 `fetch_materials_en.py`，它们共用一个结果文件。

## 已知缺口与说明

- **C11 未完成**：只有 38 个资料包达到"完整、官方、系统"的标准。不完整、只有幻灯片、需要登录或无法访问的候选见 `search_log_cn.md` 与失败表。
- **未能纳入的书籍**：
  - Szeliski 第 2 版：下载需填写表单。
  - Manning 等《IR》：官网超时。
  - Peters 等《Elements of Causal Inference》：未找到官方直链。
  - Bishop & Bishop 2024：官方只提供在线阅读。
- 本目录下有一个 `.git` 仓库（约 4.6 GB，2026-10-29 15:43 前后出现，含 "first commit"、"2-nd commit"），不是本次整理脚本创建的；整理过程中没有改动它。
- 磁盘占用：papers 约 3.1 GB，books 约 1.9 GB（其中 FoCV 的 HTML 含图片约 0.9 GB），课程约 0.5 GB；加上 `.git` 合计约 10 GB。
