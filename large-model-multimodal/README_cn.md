# 大模型与多模态文献库

大语言模型与多模态方向的学习和研究资料：论文、著名大学课程讲义和教材，按 14 个主题整理。共 748 项（688 篇论文、32 门课程、28 本书），2655 个文件。

## 主题

| 编号 | 主题 | 条目 | 全文文件 | `.url` 占位 |
|---|---|--:|--:|--:|
| 01 | [大语言模型基础](domains/01_llm_foundations/index_cn.md) | 69 | 36 | 33 |
| 02 | [预训练与数据](domains/02_pretraining_data/index_cn.md) | 60 | 37 | 23 |
| 03 | [微调与对齐](domains/03_finetuning_alignment/index_cn.md) | 60 | 37 | 23 |
| 04 | [推理与测试时计算](domains/04_reasoning_test_time/index_cn.md) | 73 | 40 | 33 |
| 05 | [检索增强与知识](domains/05_rag_knowledge/index_cn.md) | 42 | 25 | 17 |
| 06 | [智能体与工具使用](domains/06_agents_tools/index_cn.md) | 58 | 39 | 19 |
| 07 | [多模态与视觉语言模型](domains/07_multimodal_vlm/index_cn.md) | 55 | 32 | 23 |
| 08 | [图像与视频生成](domains/08_image_video_generation/index_cn.md) | 56 | 29 | 27 |
| 09 | [音频与语音](domains/09_audio_speech/index_cn.md) | 51 | 22 | 29 |
| 10 | [视频理解与具身智能](domains/10_video_embodied/index_cn.md) | 44 | 24 | 20 |
| 11 | [高效训练与部署](domains/11_efficient_train_deploy/index_cn.md) | 52 | 25 | 27 |
| 12 | [评测、安全与可信](domains/12_eval_trust/index_cn.md) | 68 | 36 | 32 |
| 13 | [著名大学课程教材与讲义](domains/13_university_courses/index_cn.md) | 32 | 2 | 514 |
| 14 | [教科书、专著与参考书](domains/14_books/index_cn.md) | 28 | 1439 | 12 |

每篇论文只归入一个主题（按选题主题或 arXiv 标题与摘要关键词确定）；跨主题的论文请在 `catalog_cn.csv` 中按关键词检索。

## 目录

```
large-model-multimodal/
├─ README_cn.md            本说明
├─ catalog_cn.csv          资料目录（每项一行：编号、主题、标题、作者、日期、arXiv ID、链接、本地路径、SHA-256 等）
├─ release_status_cn.csv   逐文件的公开形式、许可、许可依据、下载链接、大小和 SHA-256
├─ LICENSES_cn.md          公开规则
├─ reading_map_cn.md       阅读路线
├─ checksums_en.sha256     全文文件的 SHA-256
├─ domains/NN_*/index_cn.md 各主题索引
├─ papers/                 论文
├─ books/                  教材与专著（含两本离线网页版）
├─ university_materials/   大学课程讲义（每门课一个目录）
└─ scripts/                下载与整理脚本、选题种子
```

## 公开规则

只有查到明确再分发许可（CC、MIT、GNU FDL 或公有领域）的资料放全文。其他资料在同一路径放一个 `.url` 占位文件（Windows 可双击打开），里面有官方下载链接、文件大小和 SHA-256。没有声明许可的资料按不能再分发处理，arXiv 默认许可（non-exclusive licence）也按不能再分发处理。超过 100 MiB 的文件同样只放 `.url`。详见 [LICENSES_cn.md](LICENSES_cn.md)。

## 获取全文

本目录在 Git 标签 `lmml-20261106` 中只有目录、索引、脚本和 `.url` 占位文件。全文文件在同名 Release 的 tar 包中，解压到同一目录即可得到完整的 `large-model-multimodal/` 目录，方法见 Release 附件 `download_restore_cn.md`。

`.url` 占位文件可以用 `scripts/fetch_placeholders.py` 批量下载，例如：

```bash
python3 -I scripts/fetch_placeholders.py large-model-multimodal downloads
```

下载后可用 `.url` 中的 SHA256 核对文件。

## 统计口径

- 全文文件 1823 个，约 3.60 GiB；`.url` 占位 832 个，其中 4 个是超过 100 MiB 的文件。
- 资料于 2026-11-06 前后从官方地址下载；arXiv 论文记录了下载的版本号。
