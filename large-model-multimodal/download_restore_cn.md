# 下载与解压说明（大模型与多模态文献库）

全文文件放在 Release `lmml-20261106` 的 3 个不压缩 `.tar` 包中。每个包都以 `large-model-multimodal/` 为顶层目录，可以单独解压；全部解压到同一目录，就得到完整的资料库（2655 个文件，其中全文 1823 个、`.url` 占位 832 个）。

## 1. 包列表

| 包文件名 | 字节数 | 内容 |
|---|--:|---|
| `large_model_multimodal_20261106_batch001_cn_en.tar` | 1,605,888,000 | 顶层说明文件、`domains/`、`scripts/`、`books/`、`papers/` |
| `large_model_multimodal_20261106_batch002_cn_en.tar` | 1,600,102,400 | `papers/` |
| `large_model_multimodal_20261106_batch003_cn_en.tar` | 661,514,240 | `papers/`、`university_materials/` |

合计 3,867,504,640 字节（约 3.60 GiB）。每个文件在哪个包里，见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开）；包的 SHA-256 见 `SHA256SUMS.txt`。

## 2. Windows

1. 在 Release 页面展开 **Assets**，把全部 `.tar` 包和 `archive_index_cn.csv`、`SHA256SUMS.txt` 保存到同一个文件夹。
2. 可选：在该文件夹打开 PowerShell，用 `Get-FileHash 文件名 -Algorithm SHA256` 与 `SHA256SUMS.txt` 核对。
3. 选中全部 `.tar` 包，右键用 WinRAR 或 7-Zip “解压到”同一个短路径目录，例如 `D:\lmml\`，**不要**选“解压到各自的子文件夹”。解压后得到 `D:\lmml\large-model-multimodal\`。
4. Windows 10/11 自带的 `tar` 也可以：`for %f in (*.tar) do tar -xf "%f" -C D:\lmml`。

包内最长路径为 191 个字符，目标目录尽量短，避免超过 Windows 260 字符的路径上限。所有文件名都已避开 Windows 不允许的字符。

## 3. Linux / macOS

```bash
mkdir -p ~/lmml
sha256sum -c SHA256SUMS.txt
for f in *_batch*_cn_en.tar; do tar -xf "$f" -C ~/lmml || echo "FAILED: $f"; done
cd ~/lmml/large-model-multimodal && sha256sum -c checksums_en.sha256
```

## 4. `.url` 占位文件

没有再分发许可或超过 100 MiB 的文件只放 `.url` 占位。它是 Windows Internet 快捷方式，双击即可在浏览器中打开官方下载地址；文件中还记录了原文件名、字节数和 SHA-256。批量下载：

```bash
python3 -I large-model-multimodal/scripts/fetch_placeholders.py large-model-multimodal downloads
```

## 5. 只看目录

不下载全文时，Git 标签 `lmml-20261106` 中的 `large-model-multimodal/` 目录已经包含 `README_cn.md`、`catalog_cn.csv`、各主题索引、`release_status_cn.csv` 和全部 `.url` 占位文件。
