# 下载与解压恢复说明（机器学习与深度学习文献库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含脚本、目录（`catalog_cn.csv`、`domains/`）、阅读路线、检索记录、分包索引和本说明，不含 PDF 全文和离线网页资料。`main` 分支包含 56 篇论文和脚本，受限论文是 `.url` 占位文件。受限资料的 `.url` 也放在本分支的对应路径下，可直接浏览。
- **Release `mldl-full-20261029`**：4 个独立的不压缩 `.tar` 包，合起来就是完整的资料库。有再分发许可的文件保留全文，其余文件是同路径的 `.url` 占位文件（双击在浏览器打开官方下载页），规则见 `LICENSES_cn.md`。

Release 页面：https://github.com/yuriev315/machine-learning-deep-learning/releases/tag/mldl-full-20261029

## 1. 包列表

| 包文件名 | 内容范围（按路径顺序） |
|---|---|
| `machine_learning_deep_learning_20261029_batch001_cn_en.tar` | 顶层目录与报告、`domains/`、`scripts/`、`books/`（至 Torralba 网页版书的部分插图） |
| `machine_learning_deep_learning_20261029_batch002_cn_en.tar` | `books/` 剩余部分、`papers/`（至 2024_Edge_LocalGlobalGraphRAG） |
| `machine_learning_deep_learning_20261029_batch003_cn_en.tar` | `papers/`（2024_ElNouby … 2024_Yang_DenoisingVisionTransformers） |
| `machine_learning_deep_learning_20261029_batch004_cn_en.tar` | `papers/` 剩余部分、`university_materials/`（全部课程讲义） |

每个文件属于哪个包，见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开；3,715 行）。表中列出包文件名、批次、相对路径、类型、字节数和备注。

- 每个包都可以**单独解压**，不需要拼接。只要某几类资料时，可以只下载对应的包。
- 各包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包未压缩，解压很快，所需磁盘空间约等于包的大小。全部解压约需 **3.2 GiB**。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 4 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\mldl\`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断可在浏览器下载列表里点“恢复”或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，在文件属性里核对每个包的大小（属性窗口里看“大小”的字节数，不要看“占用空间”）。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\mldl\`。

**方法 A：一次批量解压（推荐）**

1. 在下载文件夹中，按住 Ctrl 选中全部 4 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\mldl\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 确定。所有包会解压到同一个 `D:\mldl\` 下，恢复出完整的目录结构：

```
D:\mldl\
├─ README_cn.md、catalog_cn.csv、reading_map_cn.md、checksums_en.sha256 …
├─ books\
├─ domains\
├─ papers\
├─ scripts\
└─ university_materials\
```

**方法 B：逐个解压**

对每个 `.tar` 文件：右键 → WinRAR → **解压文件…** → 目标路径都填同一个 `D:\mldl\` → 确定。

注意：不要用“解压到 machine_learning_deep_learning_..._batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

### Windows 文件名兼容处理（已在发布包中完成）

原资料中有 20 个文件名含 `?`，Windows 不允许这个字符，解压会报错。它们都是离线网页资料里的字体和图标文件，例如 `bootstrap-icons.woff?2820a3852bdb9a5832199cc61cec4e65`、`fontawesome-webfont.eot?v=4.7.0`，分布在：

- 书籍：`Molnar_InterpretableMachineLearning_3rdEd_html_en`、`Torralba_FoundationsOfComputerVision_2024_html_en`
- 课程讲义：`CMU_10708_2019Spring_LectureNotes_en`、`MIT_6390_Online_LectureNotes_en`、`NYU_DSGA1008_2020Spring_LectureNotes_en`、`Stanford_CS228_Online_LectureNotes_en`

发布包中这些文件名里的 `?` 改成了 `_`，例如 `bootstrap-icons.woff_2820a3852bdb9a5832199cc61cec4e65`，文件内容不变。解压时不会再出现文件名报错。

同步更新的文件：

- 引用这些字体的 7 个 CSS 文件改为新文件名，离线打开网页时图标和字体照常显示（已逐个核对：改名前后，离线网页中能找到目标的本地链接数完全相同）。
- 下载记录 `scripts/cache/materials_results_en.json` 中 20 处路径改为新文件名。
- 根目录 `checksums_en.sha256` 中对应的 27 行已更新为新路径或新的 SHA-256。
- 全部改动列在 `windows_rename_map_cn.csv` 中（原路径 → 发布包内路径），`archive_index_cn.csv` 的“备注”列也有标注。

除这 29 个文件外，其余全文文件都与下载时的文件逐字节相同。所有路径都不超过 192 个字符，不会遇到 Windows 长路径问题。

### 原资料自身的已知情况（与打包无关）

离线网页资料中有少量本地引用在离线时打不开，例如以 `/` 开头的站点绝对路径、由脚本拼接的链接和没有镜像下来的个别图片（主要在 Molnar、Torralba 两本书和 CMU_10708、MIT_6390 两门课里）。原资料就是这样，本次发布没有改动。正文页面可以正常阅读。

## 4. Linux / macOS

```bash
mkdir -p ~/mldl
for f in machine_learning_deep_learning_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/mldl || echo "FAILED: $f"; done
```

（macOS 自带 bsdtar，同样支持此格式。）

## 5. 完整性说明

- 每个附件上传后都用 GitHub API 返回的 SHA-256 与本地核对，结果见 `upload_report_cn.md`。
- 解压后的根目录有 `checksums_en.sha256`，这是公开版文件（含 `.url`）的 SHA-256 清单。需要时可以自行核对，例如在 Linux 上运行 `sha256sum -c checksums_en.sha256`。
- 无再分发许可的文件没有打包，只保留 `.url` 占位文件。
