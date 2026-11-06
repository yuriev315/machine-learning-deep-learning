# 下载与解压说明（低资源语言大模型文献库）

本资料库的发布方式：

- **Git tag `lrl-full-20261029`**：只包含脚本、目录（`catalog_cn.csv`、`domains/`）、学习指南（`guides/`）、版权说明、分包索引和本说明，不含 PDF 全文和参考代码。
- **Release `lrl-full-20261029`**：10 个独立的不压缩 `.tar` 包，合起来就是完整的资料库，包括论文、教材、课程讲义、工程文档、参考代码、目录、报告和脚本。

Release 页面：https://github.com/yuriev315/machine-learning-deep-learning/releases/tag/lrl-full-20261029

没有再分发许可的资料（多数课程讲义、部分书籍、arXiv 默认许可的论文、两个没有许可证的文档仓库）在包内是同路径的 `.url` 占位文件，里面有官方链接、文件大小和 SHA-256，规则见 `LICENSES_cn.md`，逐个文件的公开形式见 `release_status_cn.csv`。

## 1. 包列表

| 包文件名 | 内容范围（按路径顺序） | 文件数 | 字节数 |
|---|---|--:|--:|
| `low_resource_language_llm_20261029_batch001_cn_en.tar` | 顶层目录与说明、`domains/`、`guides/`、`scripts/`、`books/`、`papers/`（至 2024_Hu_LargeLanguageModelsCross） | 831 | 901,754,880 |
| `low_resource_language_llm_20261029_batch002_cn_en.tar` | `papers/`（2024_Hu_MiniCPM … 2026_Leino） | 653 | 1,074,462,720 |
| `low_resource_language_llm_20261029_batch003_cn_en.tar` | `papers/` 剩余部分、`university_materials/`（至 CMU_11-711 第 08 讲） | 307 | 211,742,720 |
| `low_resource_language_llm_20261029_batch004_cn_en.tar` | `university_materials/`（CMU_11-711 第 09 讲 … HKUST_COMP4901B 第 6 讲） | 347 | 203,868,160 |
| `low_resource_language_llm_20261029_batch005_cn_en.tar` | `university_materials/`（HKUST_COMP4901B 第 7 讲 … MIT_6.5940 第 17 讲） | 147 | 317,440 |
| `low_resource_language_llm_20261029_batch006_cn_en.tar` | `university_materials/`（MIT_6.5940 第 18 讲 … UBC_CPSC440 第 5 讲） | 254 | 552,960 |
| `low_resource_language_llm_20261029_batch007_cn_en.tar` | `university_materials/` 剩余部分、`engineering_docs/`、`reference_code/`（至 argilla 的部分截图） | 17373 | 881,029,120 |
| `low_resource_language_llm_20261029_batch008_cn_en.tar` | `reference_code/`（argilla 其余 … haystack） | 23790 | 1,207,797,760 |
| `low_resource_language_llm_20261029_batch009_cn_en.tar` | `reference_code/`（langfuse-docs … vllm 源码目录） | 60848 | 1,406,504,960 |
| `low_resource_language_llm_20261029_batch010_cn_en.tar` | `reference_code/vllm_5df63a7_original_en.tar.gz`（单个文件） | 1 | 42,414,080 |

每个文件属于哪个包，见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开；约 10.5 万行）。表中列出包文件名、批次、相对路径、类型、字节数和备注。

- 每个包都可以**单独解压**，不需要拼接。只要某几类资料时，可以只下载对应的包。
- 各包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包未压缩，解压很快，所需磁盘空间约等于包的大小。全部解压约需 **5.5 GiB**，建议预留 8 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 10 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`SHA256SUMS.txt`，全部保存到**同一个下载文件夹**，例如 `D:\下载\lrl\`。
3. 单个包最大约 1.4 GB。浏览器提示“是否保留”时选择保留。下载中断可在浏览器下载列表里点“恢复”或重新下载。
4. 对照上表或 `SHA256SUMS.txt` 核对每个包的大小（属性窗口里看“大小”的字节数，不要看“占用空间”）。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用**短路径**，例如 `D:\lrl\`。

**方法 A：一次批量解压（推荐）**

1. 在下载文件夹中，按住 Ctrl 选中全部 10 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\lrl\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 确定。所有包会解压到同一个 `D:\lrl\` 下，恢复出完整的目录结构：

```
D:\lrl\
├─ README_cn.md、LICENSES_cn.md、catalog_cn.csv、release_status_cn.csv、checksums_en.sha256 …
├─ books\
├─ domains\
├─ engineering_docs\
├─ guides\
├─ papers\
├─ reference_code\
├─ scripts\
└─ university_materials\
```

**方法 B：逐个解压**

对每个 `.tar` 文件：右键 → WinRAR → **解压文件…** → 目标路径都填同一个 `D:\lrl\` → 确定。

注意：不要用“解压到 low_resource_language_llm_..._batch0XX_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

### Windows 文件名兼容处理（已在发布包中完成）

有两类文件名在 Windows 上会出错，发布包里已经改好，解压时不会再出现文件名报错或覆盖提示：

1. **文件名含 `?`（28 个）**：离线网页版书 `books/Austin_HowToScaleYourModel_2025_html_en/scaling-book_site/scaling-book/assets/` 下的 css/js/字体/图标文件，例如 `main.css?d41d8cd98f00b204e9800998ecf8427e_en.css`。Windows 不允许文件名中出现 `?`，发布包中改为 `_`，例如 `main.css_d41d8cd98f00b204e9800998ecf8427e_en.css`。文件内容不变。
2. **同一目录下仅大小写不同的两个文件（1 对）**：`reference_code/argilla_78cb518_en/argilla-frontend/components/base/base-feedback/base-feedback-error/` 下的 `BaseFeedbackError.spec_en.js` 和 `baseFeedbackError.spec_en.js`。Windows 不区分大小写，会互相覆盖。发布包中后者改名为 `baseFeedbackError_case2.spec_en.js`。这两个文件内容完全相同（SHA-256 一致）。

同步更新的文件：

- 上面两处的路径对照表 `path_map_en.csv`（scaling-book 的 28 处、argilla 的 1 处）改为新文件名。
- 根目录 `checksums_en.sha256` 中对应的行使用新路径，改过内容的两个 `path_map_en.csv` 使用新的 SHA-256。
- 全部改动列在 `windows_rename_map_cn.csv` 中（原路径 → 发布包内路径）。

### 长路径

`reference_code/` 里的源码快照保留了原仓库的目录结构，其中 26 个文件的相对路径超过 230 个字符，最长 429 个字符，集中在 `langfuse_d89f49b_en/web/src/features/sessions/…`。这些都是上游代码本身的目录层级，改短会破坏源码结构，所以没有改动。

- WinRAR 支持超过 260 个字符的长路径，能正常解压这些文件。
- Windows 自带的“全部解压缩”和部分旧软件不支持长路径，可能报错，所以请用 WinRAR 解压。如果之后要在资源管理器里打开或删除这些深层文件，可以在 Windows 10/11 中开启“启用 Win32 长路径”（组策略：计算机配置 → 管理模板 → 系统 → 文件系统）。
- 同一份源码也以原始压缩包形式保存在 `reference_code/*_original_en.tar.gz`。

### 资料自身的已知问题（与打包无关）

离线网页版书 `Austin_HowToScaleYourModel_2025_html_en` 的页面和资源文件统一加了 `_en` 后缀，例如 `index_en.html`。但网页内的链接和 `manifest_en.json` 仍指向不带 `_en` 的原名，所以离线打开时页面间跳转和样式加载会失效。需要离线阅读时，解压同目录下的 `scaling-book_site_original_en.tar.gz`（原始文件名）；也可以看在线版 https://jax-ml.github.io/scaling-book/ 。

## 4. Linux / macOS

```bash
mkdir -p ~/lrl
for f in low_resource_language_llm_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/lrl || echo "FAILED: $f"; done
```

（macOS 自带 bsdtar，同样支持此格式。）

## 5. 完整性校验

- 每个包的 SHA-256 见 Release 附件 `SHA256SUMS.txt`，上传后已逐个核对 GitHub 显示的摘要。
- 解压后的根目录有 `checksums_en.sha256`，列出资料库全部原件的 SHA-256，包括只给 `.url` 的文件。在 Linux 上可以运行 `sha256sum -c --ignore-missing checksums_en.sha256` 核对包内全文；`.url` 对应的原件自行下载后，也可以用同一个文件核对。
- `.url` 文件是文本文件（Windows 快捷方式格式），双击会在浏览器中打开官方链接。
