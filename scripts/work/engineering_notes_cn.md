# 类别 19 工程资料：项目说明（已核验项目）

生成依据：`scripts/seeds/19_engineering_seed_cn.json` + `scripts/state/results/19_engineering_en.json`（脚本 fetch 结果）+ 人工核对许可证文件。
所有路径相对库根 `/root/low_resource_language_llm_literature`。仓库代码只下载、过滤、归档，未执行、未安装、未构建。
“加后缀副本”中每个文件名都加了语言后缀（如 foo.py -> foo_en.py），仅供阅读，不是可运行仓库；原始结构见 *_original_en.tar.gz。

## 环节：语料获取、清洗、语言识别、去重和分词

### E-01 datatrove
- 环节：语料获取、清洗、语言识别、去重和分词；交叉环节：数据版本管理、训练数据配比及质量审计
- 官方地址：https://github.com/huggingface/datatrove；仓库：https://github.com/huggingface/datatrove
- 用途：大规模网页/文档语料处理流水线：读取 CommonCrawl WARC、正文抽取、语言识别（fastText/GlotLID）、启发式质量过滤、MinHash/精确子串去重、分词与 token 统计，支持本地/Slurm/Ray 执行
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.10.1` → 提交 `1977fbb0f3c163d43cace334b073dda17fa3ef26`（提交日期 2026-09-30T09:12:03+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/datatrove/pipeline/readers`、`src/datatrove/pipeline/extractors`、`src/datatrove/pipeline/filters/language_filter.py`、`src/datatrove/utils/lid.py`、`src/datatrove/pipeline/dedup`、`src/datatrove/pipeline/tokens`、`src/datatrove/executor/slurm.py`、`examples/fineweb.py`
- 关联论文：The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (arXiv:2406.17557)；04-001（本库论文：arxiv:2506.20920，papers/2025_Penedo_FineWeb2_en.pdf）
- 学习价值：FineWeb/FineWeb2 数据流水线的官方实现；FineWeb2 正是把同一流水线按语言调参扩展到上千种语言，可直接对照学习小语种的语言识别阈值、过滤与去重配置
- 本地路径：原始归档 `reference_code/datatrove_1977fbb_original_en.tar.gz`（sha256 714db5bb5328ccf8…）；加后缀副本 `reference_code/datatrove_1977fbb_en/`（路径映射 path_map_en.csv）；保留文件 246 个 / 3.7 MB，剔除 1 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：未保存文档集。仓库无独立文档源目录，官方说明仅为 README 与 examples/；不构成文档集

### E-02 GlotLID
- 环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://github.com/cisnlp/GlotLID；仓库：https://github.com/cisnlp/GlotLID
- 用途：覆盖 2000+ 语言标签（含文字系统）的 fastText 语言识别模型的训练数据来源说明、数据清洗/去重/上采样脚本与推理示例；模型权重托管在 Hugging Face，不在本仓库
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：LICENSE 首行为“Apache License 2.0 plus notices”，前部附训练数据/模型行为说明与免责声明，正文为 Apache-2.0；检测值正确，另需注意附加声明
- 版本：ref `d63cc2f6db97de90b6877ccbe0253161f08fdb14` → 提交 `d63cc2f6db97de90b6877ccbe0253161f08fdb14`（提交日期 2026-04-15T06:05:40+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`assets/inference/customlid.py`、`assets/train/dedup_split.py`、`assets/train/upsample.py`、`assets/train/gen_und.py`、`assets/sources`、`languages-v3.md`、`sources.md`
- 关联论文：GlotLID: Language Identification for Low-Resource Languages (arXiv:2310.16248)
- 学习价值：低资源语言识别的直接参考：标签按“语言_文字”设计、未知语言（und/zxx）处理、数据来源清单与去污染，可用于小语种语料筛选前的 LID 选型
- 本地路径：原始归档 `reference_code/GlotLID_d63cc2f_original_en.tar.gz`（sha256 af285d4a95ddb5dc…）；加后缀副本 `reference_code/GlotLID_d63cc2f_en/`（路径映射 path_map_en.csv）；保留文件 21 个 / 1.0 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：未保存文档集。仓库无 tag，固定为 2026-04-15 的默认分支提交；文档仅 README/languages/sources 说明，不构成文档集

### E-03 sentencepiece
- 环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://github.com/google/sentencepiece；仓库：https://github.com/google/sentencepiece
- 用途：与语言无关的子词分词器（Unigram/BPE），直接从原始句子训练，不依赖空格预分词
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.2.2` → 提交 `e0cce7d37b065b5140349dbe12c6bcf6192fdd78`（提交日期 2026-07-02T01:52:43+09:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/unigram_model_trainer.cc`、`src/bpe_model_trainer.cc`、`src/normalizer.cc`、`src/sentencepiece_trainer.cc`、`src/sentencepiece_processor.cc`、`python/src/sentencepiece/__init__.py`、`doc/options.md`、`doc/normalization.md`
- 关联论文：SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing (arXiv:1808.06226)
- 学习价值：小语种词表构建与词表扩展的基础工具；可学习 character_coverage、字节回退、规范化规则对非拉丁文字与无空格文字的影响
- 本地路径：原始归档 `reference_code/sentencepiece_e0cce7d_original_en.tar.gz`（sha256 96589e9e28354162…）；加后缀副本 `reference_code/sentencepiece_e0cce7d_en/`（路径映射 path_map_en.csv）；保留文件 256 个 / 11.3 MB，剔除 15 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `doc` → `engineering_docs/sentencepiece_docs_e0cce7d_en/`，8 个文件（文档源文件 8）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 doc/ 目录的 Markdown 说明（选项、规范化、特殊符号等）；无目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：doc/ 仅 8 个 Markdown，无目录文件，未计完整

### E-04 tokenizers
- 环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://huggingface.co/docs/tokenizers；仓库：https://github.com/huggingface/tokenizers
- 用途：Rust 实现、带 Python/Node 绑定的快速分词器库：规范化、预分词、BPE/WordPiece/Unigram 模型训练、后处理与解码
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.23.3` → 提交 `301277072263fb3830eb66eec7e47adadf76f1dc`（提交日期 2026-10-09T11:37:01+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`tokenizers/src/models/mod.rs`、`tokenizers/src/normalizers/mod.rs`、`tokenizers/src/pre_tokenizers/mod.rs`、`tokenizers/src/processors/mod.rs`、`tokenizers/src/decoders/mod.rs`、`bindings/python/py_src/tokenizers/__init__.py`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：transformers 生态的实际分词实现；对比 sentencepiece 可理解字节级 BPE 与预分词规则在小语种上的分词效率（fertility）差异，用于词表扩展实验
- 本地路径：原始归档 `reference_code/tokenizers_3012770_original_en.tar.gz`（sha256 5a954c078c39227a…）；加后缀副本 `reference_code/tokenizers_3012770_en/`（路径映射 path_map_en.csv）；保留文件 337 个 / 4.9 MB，剔除 1 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/tokenizers_docs_3012770_en/`，46 个文件（文档源文件 26）；目录类型 hf_toctree，目录条目 18，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（HF doc-builder 源 source-doc-builder/ 与旧 Sphinx 源 source/）；格式：源文件（Markdown/RST，未构建 HTML）

### E-05 text-dedup
- 环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://github.com/ChenghaoMou/text-dedup；仓库：https://github.com/ChenghaoMou/text-dedup
- 用途：文本去重算法集合：MinHash-LSH、SimHash、Bloom filter、后缀数组精确子串去重，带配置与基准脚本
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `7538f3ec6a28e72a86de5978e58655175b46a11e` → 提交 `7538f3ec6a28e72a86de5978e58655175b46a11e`（提交日期 2026-03-09T10:24:42Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/text_dedup/minhash.py`、`src/text_dedup/simhash.py`、`src/text_dedup/suffix_array.py`、`src/text_dedup/bloom_filter.py`、`configs/minhash.toml`、`benchmarks/benchmark_core.py`
- 关联论文：Deduplicating Training Data Makes Language Models Better (arXiv:2107.06499)
- 学习价值：算法实现短小、单文件可读，适合理解近似去重参数（n-gram、band/row、阈值）对多文字语料的影响；与 datatrove 的流水线式去重互补
- 本地路径：原始归档 `reference_code/text-dedup_7538f3e_original_en.tar.gz`（sha256 a005ce4124daa1e8…）；加后缀副本 `reference_code/text-dedup_7538f3e_en/`（路径映射 path_map_en.csv）；保留文件 75 个 / 0.7 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：未保存文档集。最新 tag（2023.09.20 / 0.4.1）过旧，固定为 2026-03-09 默认分支提交；文档仅 README 与 benchmarks 说明

## 环节：数据版本管理、训练数据配比及质量审计

### E-06 dvc
- 环节：数据版本管理、训练数据配比及质量审计
- 官方地址：https://dvc.org/doc；仓库：https://github.com/iterative/dvc
- 用途：Git 之上的数据与模型版本管理：大文件缓存与远端存储、可复现流水线（dvc.yaml stages）、实验跟踪
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `3.67.1` → 提交 `356dfa03278058b02df42124f243c2c345329dae`（提交日期 2026-03-31T10:49:52+05:45）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`dvc/repo/add.py`、`dvc/output.py`、`dvc/cachemgr.py`、`dvc/data_cloud.py`、`dvc/stage`、`dvc/repo/reproduce.py`、`dvc/repo/experiments`、`dvc/api`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：为小语种语料各清洗阶段产物打版本、记录数据血缘与复现流水线的通用工具
- 本地路径：原始归档 `reference_code/dvc_356dfa0_original_en.tar.gz`（sha256 1e460cb820178027…）；加后缀副本 `reference_code/dvc_356dfa0_en/`（路径映射 path_map_en.csv）；保留文件 591 个 / 3.1 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：独立文档仓库 https://github.com/iterative/dvc.org 提交 `21fabba8d66bf81e3cfcbcb9e061d4a5363399ad`（原始归档 `reference_code/dvc-docs_21fabba_original_en.tar.gz`）的 `content/docs` → `engineering_docs/dvc_docs_21fabba_en/`，202 个文件（文档源文件 201）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：官方站点源仓库 dvc.org 的 content/docs（目录为 sidebar.json）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：dvc.org 站点目录为 content/docs/sidebar.json，脚本不支持，未计完整

### E-07 datasets
- 环节：数据版本管理、训练数据配比及质量审计
- 官方地址：https://huggingface.co/docs/datasets；仓库：https://github.com/huggingface/datasets
- 用途：数据集加载、Arrow 内存映射、流式读取、指纹缓存与按概率交错混合（interleave_datasets）
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `5.1.0` → 提交 `efe6ea4f88260b1a5066f28a9c90d82365a29f42`（提交日期 2026-10-05T17:32:38+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/datasets/load.py`、`src/datasets/arrow_dataset.py`、`src/datasets/iterable_dataset.py`、`src/datasets/combine.py`、`src/datasets/fingerprint.py`、`src/datasets/builder.py`、`src/datasets/packaged_modules`
- 关联论文：Datasets: A Community Library for Natural Language Processing (arXiv:2109.02846)
- 学习价值：多语言数据按语言配比混合（interleave 概率、温度采样）与可复现数据处理（fingerprint）的基础实现
- 本地路径：原始归档 `reference_code/datasets_efe6ea4_original_en.tar.gz`（sha256 2a11f30256579313…）；加后缀副本 `reference_code/datasets_efe6ea4_en/`（路径映射 path_map_en.csv）；保留文件 382 个 / 7.9 MB，剔除 10 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/datasets_docs_efe6ea4_en/`，67 个文件（文档源文件 62）；目录类型 hf_toctree，目录条目 62，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（HF doc-builder _toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

### E-08 data-juicer
- 环节：数据版本管理、训练数据配比及质量审计；交叉环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://github.com/modelscope/data-juicer；仓库：https://github.com/modelscope/data-juicer
- 用途：以算子（mapper/filter/deduplicator/selector）组合的数据处理与数据质量分析系统，带数据统计分析、配方（recipe）与可视化
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.6.1` → 提交 `abb9e49897bdd0e0e2f44ce3272cc1ea5c5a6111`（提交日期 2026-10-19T14:00:44+08:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`data_juicer/ops/filter`、`data_juicer/ops/mapper`、`data_juicer/ops/deduplicator`、`data_juicer/ops/selector`、`data_juicer/core/executor`、`data_juicer/analysis`、`data_juicer/config`、`tools/distributed_deduplication`
- 关联论文：Data-Juicer: A One-Stop Data Processing System for Large Language Models (arXiv:2309.02033)；Data-Juicer 2.0: Cloud-Scale Adaptive Data Processing for and with Foundation Models (arXiv:2501.14755)
- 学习价值：数据质量审计（统计分布、算子前后对比）与配方化数据处理的参考；含语言识别分数过滤等多语种算子
- 本地路径：原始归档 `reference_code/data-juicer_abb9e49_original_en.tar.gz`（sha256 6ab24e4f417cb9e6…）；加后缀副本 `reference_code/data-juicer_abb9e49_en/`（路径映射 path_map_en.csv）；保留文件 1412 个 / 27.6 MB，剔除 27 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/data-juicer_docs_abb9e49_en/`，306 个文件（文档源文件 286）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/（中英 Markdown 文档与 sphinx_doc 源）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：docs/sphinx_doc/source/index.rst 的 toctree 位于文件末尾，脚本正则要求块后还有非缩进行，导致未识别（toc_kind=None）；且该 Sphinx 源只索引 API，主体是 docs/ 下中英 Markdown。未计完整

### E-09 dolma
- 环节：数据版本管理、训练数据配比及质量审计；交叉环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://github.com/allenai/dolma；仓库：https://github.com/allenai/dolma
- 用途：OLMo 预训练语料 Dolma 的工具链：打标签（taggers）、Bloom filter 去重、按规则混合（mixer）与分词，配有各版本语料配方
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.2.1` → 提交 `fd22a34972a36bf1a60d2f161533d55b2be4c047`（提交日期 2025-06-25T11:52:53-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`python/dolma/taggers`、`python/dolma/cli/mixer.py`、`python/dolma/cli/deduper.py`、`python/dolma/cli/tokenizer.py`、`src/mixer.rs`、`src/deduper.rs`、`configs/dolma-v1_7`
- 关联论文：04-015（本库论文：arxiv:2402.00159，papers/2024_Soldaini_Dolma_en.pdf）
- 学习价值：“打分标签→按属性混合”的语料配比与审计方式，可学习可追溯的数据配方写法
- 本地路径：原始归档 `reference_code/dolma_fd22a34_original_en.tar.gz`（sha256 87cc7378debc9983…）；加后缀副本 `reference_code/dolma_fd22a34_en/`（路径映射 path_map_en.csv）；保留文件 618 个 / 13.7 MB，剔除 25 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/dolma_docs_fd22a34_en/`，30 个文件（文档源文件 9）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/ Markdown（mixer/taggers/tokenize 等），无目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：docs/ 仅约 9 个 Markdown，无目录文件，未计完整

## 环节：持续预训练、指令微调、参数高效适配及偏好训练

### E-10 peft
- 环节：持续预训练、指令微调、参数高效适配及偏好训练
- 官方地址：https://huggingface.co/docs/peft；仓库：https://github.com/huggingface/peft
- 用途：参数高效微调库：LoRA/QLoRA、AdaLoRA、IA3、Prompt Tuning 等适配器的实现与合并
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.21.2` → 提交 `eaa35c777c7ba554a2a3639ac9c79bb690f39a57`（提交日期 2026-10-01T12:17:57+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/peft/peft_model.py`、`src/peft/mapping.py`、`src/peft/tuners/lora/config.py`、`src/peft/tuners/lora/layer.py`、`src/peft/tuners/lora/model.py`、`src/peft/tuners/adalora`、`src/peft/tuners/ia3`、`src/peft/tuners/prompt_tuning`
- 关联论文：LoRA: Low-Rank Adaptation of Large Language Models (arXiv:2106.09685)；QLoRA: Efficient Finetuning of Quantized LLMs (arXiv:2305.14314)
- 学习价值：小语种低算力适配的主力实现；可学习 LoRA 与扩展词表 embedding 一起训练（modules_to_save / trainable_token_indices）的做法
- 本地路径：原始归档 `reference_code/peft_eaa35c7_original_en.tar.gz`（sha256 c840750dd7aab5dc…）；加后缀副本 `reference_code/peft_eaa35c7_en/`（路径映射 path_map_en.csv）；保留文件 984 个 / 25.3 MB，剔除 3 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/peft_docs_eaa35c7_en/`，84 个文件（文档源文件 81）；目录类型 hf_toctree，目录条目 81，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（_toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

### E-11 trl
- 环节：持续预训练、指令微调、参数高效适配及偏好训练
- 官方地址：https://huggingface.co/docs/trl；仓库：https://github.com/huggingface/trl
- 用途：后训练库：SFT、DPO、KTO、奖励模型、GRPO/RLOO 等偏好与强化学习训练器及命令行脚本
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.16.0` → 提交 `1b5c75ed94b7387f42532adb090c935166d4878d`（提交日期 2026-10-15T13:54:58-04:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`trl/trainer/sft_trainer.py`、`trl/trainer/dpo_trainer.py`、`trl/trainer/kto_trainer.py`、`trl/trainer/reward_trainer.py`、`trl/trainer/grpo_trainer.py`、`trl/data_utils.py`、`trl/scripts`
- 关联论文：Direct Preference Optimization: Your Language Model is Secretly a Reward Model (arXiv:2305.18290)
- 学习价值：指令微调与偏好训练的标准训练器；可学习聊天模板、packing、偏好数据格式，适合小语种指令/偏好数据实验
- 本地路径：原始归档 `reference_code/trl_1b5c75e_original_en.tar.gz`（sha256 07aa729bca8418d2…）；加后缀副本 `reference_code/trl_1b5c75e_en/`（路径映射 path_map_en.csv）；保留文件 556 个 / 9.2 MB，剔除 3 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/trl_docs_1b5c75e_en/`，59 个文件（文档源文件 57）；目录类型 hf_toctree，目录条目 57，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（_toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

### E-12 LLaMA-Factory
- 环节：持续预训练、指令微调、参数高效适配及偏好训练
- 官方地址：https://github.com/hiyouga/LLaMA-Factory；仓库：https://github.com/hiyouga/LLaMA-Factory
- 用途：统一的配置驱动微调框架：继续预训练（pt）、SFT、奖励模型、PPO/DPO/KTO，支持 LoRA/QLoRA/全参与多种模型对话模板
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.9.5` → 提交 `7af909522a951e3ad9f022ea6f88b6755257eaa5`（提交日期 2026-05-30T23:57:09+08:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/llamafactory/train/pt/workflow.py`、`src/llamafactory/train/sft/workflow.py`、`src/llamafactory/train/dpo/workflow.py`、`src/llamafactory/data/template.py`、`src/llamafactory/data/loader.py`、`src/llamafactory/model/adapter.py`、`examples/train_lora/qwen3_lora_sft.yaml`
- 关联论文：LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models (arXiv:2403.13372)
- 学习价值：用 YAML 即可串起“继续预训练→指令微调→偏好训练”的完整流程，适合小语种团队快速复现基线；数据注册（dataset_info）方式值得参考
- 本地路径：原始归档 `reference_code/LLaMA-Factory_7af9095_original_en.tar.gz`（sha256 99c0bae24f26c771…）；加后缀副本 `reference_code/LLaMA-Factory_7af9095_en/`（路径映射 path_map_en.csv）；保留文件 530 个 / 11.5 MB，剔除 9 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/LLaMA-Factory_docs_7af9095_en/`，62 个文件（文档源文件 55）；目录类型 sphinx_toctree，目录条目 24，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（en/ 与 zh/ 两套 Sphinx 源）；格式：源文件（Markdown/RST，未构建 HTML）

### E-13 open-instruct
- 环节：持续预训练、指令微调、参数高效适配及偏好训练；交叉环节：数据版本管理、训练数据配比及质量审计
- 官方地址：https://github.com/allenai/open-instruct；仓库：https://github.com/allenai/open-instruct
- 用途：AI2 Tülu 系列后训练代码：SFT、DPO、带可验证奖励的强化学习（GRPO），含数据混合与转换工具
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `64beb76c3efe2b600f39922ef83b5ea44669ea61` → 提交 `64beb76c3efe2b600f39922ef83b5ea44669ea61`（提交日期 2026-10-28T23:27:16Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`open_instruct/finetune.py`、`open_instruct/dpo.py`、`open_instruct/grpo_fast.py`、`open_instruct/dataset_transformation.py`、`open_instruct/mix_data.py`
- 关联论文：Tulu 3: Pushing Frontiers in Open Language Model Post-Training (arXiv:2411.15124)
- 学习价值：完全公开数据与配方的后训练参考实现，可学习 SFT/DPO/RLVR 三阶段配比与去污染流程，再迁移到小语种
- 本地路径：原始归档 `reference_code/open-instruct_64beb76_original_en.tar.gz`（sha256 7a13761d20487d8c…）；加后缀副本 `reference_code/open-instruct_64beb76_en/`（路径映射 path_map_en.csv）；保留文件 1077 个 / 38.2 MB，剔除 4 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/open-instruct_docs_64beb76_en/`，134 个文件（文档源文件 53）；目录类型 mkdocs_nav，目录条目 49，缺失 4，解析率 0.918；**未计为完整文档集**。范围：仓库内 docs/（根目录 mkdocs.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：mkdocs 导航 49 条中缺 4 条（miles/configuration 等），这些页面由 scripts/miles/docs_site.py 在构建时生成，源仓库中不存在；解析率 0.918 < 0.95，未计完整
- 版本备注：旧 tag v0.1.0–v0.3.0 远落后于主线，固定为 2026-10-28 默认分支提交

## 环节：分布式训练、检查点、日志与训练故障恢复

### E-14 Megatron-LM
- 环节：分布式训练、检查点、日志与训练故障恢复
- 官方地址：https://github.com/NVIDIA/Megatron-LM；仓库：https://github.com/NVIDIA/Megatron-LM
- 用途：张量/流水线/序列/专家并行的大模型训练框架与 Megatron Core 库，含分布式检查点与容错集成
- 许可证：预期 BSD-3-Clause（另含第三方许可）；脚本检测 `LICENSE` → Apache-2.0；人工确认：检测值不准确：LICENSE 开头为 NVIDIA 的 BSD-3-Clause 条款（适用于除另注明外的全部文件），文件中另附 Apache-2.0 等第三方许可证文本（脚本因匹配到 Apache 段落而报 Apache-2.0）；人工确认主许可证为 BSD-3-Clause
- 版本：ref `core_v0.19.2` → 提交 `4b4acac9a1d28ea6829c8d4f566d75698a21249d`（提交日期 2026-09-18T12:18:15-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`megatron/core/parallel_state.py`、`megatron/core/tensor_parallel`、`megatron/core/pipeline_parallel/schedules.py`、`megatron/core/distributed`、`megatron/core/dist_checkpointing`、`megatron/core/optimizer`、`megatron/training/training.py`、`megatron/training/checkpointing.py`、`megatron/training/ft_integration.py`、`pretrain_gpt.py`
- 关联论文：Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism (arXiv:1909.08053)；Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM (arXiv:2104.04473)
- 学习价值：大规模持续预训练的并行切分、分布式检查点（可改变并行度后恢复）与故障恢复机制的工业级实现
- 本地路径：原始归档 `reference_code/Megatron-LM_4b4acac_original_en.tar.gz`（sha256 237330550eab0129…）；加后缀副本 `reference_code/Megatron-LM_4b4acac_en/`（路径映射 path_map_en.csv）；保留文件 2964 个 / 59.9 MB，剔除 2 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/Megatron-LM_docs_4b4acac_en/`，93 个文件（文档源文件 60）；目录类型 sphinx_toctree，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/（Sphinx/MyST 源，index.md toctree）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：脚本未能解析 MyST ```{toctree}``` 块（正则在首个 :maxdepth: 选项行即结束），故目录条目为 0、不计完整；人工按 MyST 语法解析 index.md 等文件得 56 条、缺 1 条（apidocs/index 为构建时自动生成），解析率约 0.982。按规则仍记为未计完整文档集

### E-15 DeepSpeed
- 环节：分布式训练、检查点、日志与训练故障恢复
- 官方地址：https://www.deepspeed.ai；仓库：https://github.com/deepspeedai/DeepSpeed
- 用途：ZeRO 1/2/3 与 offload、流水线并行、通用检查点（universal checkpoint）、多节点启动器与监控
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.19.8` → 提交 `0eb3a8bcc6d9a8775478e5377482c4bf2dd23c1c`（提交日期 2026-10-19T13:31:24Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`deepspeed/runtime/engine.py`、`deepspeed/runtime/zero/stage_1_and_2.py`、`deepspeed/runtime/zero/stage3.py`、`deepspeed/runtime/pipe/engine.py`、`deepspeed/runtime/checkpoint_engine`、`deepspeed/checkpoint/ds_to_universal.py`、`deepspeed/launcher/runner.py`、`deepspeed/monitor/monitor.py`
- 关联论文：ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (arXiv:1910.02054)
- 学习价值：有限 GPU 上做小语种持续预训练/全参微调的显存优化方案；通用检查点可在改变 GPU 数后续训
- 本地路径：原始归档 `reference_code/DeepSpeed_0eb3a8b_original_en.tar.gz`（sha256 8ed2aba02cf8e886…）；加后缀副本 `reference_code/DeepSpeed_0eb3a8b_en/`（路径映射 path_map_en.csv）；保留文件 2070 个 / 117.2 MB，剔除 11 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/DeepSpeed_docs_0eb3a8b_en/`，296 个文件（文档源文件 113）；目录类型 sphinx_toctree，目录条目 17，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（Jekyll 站点源：教程 _tutorials、博客 _posts，以及 code-docs 的 Sphinx API 源）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：脚本判为完整，依据仅是 docs/code-docs/source 的 Sphinx API 目录（17 条全部存在）；同目录下 Jekyll 教程/博客站点的导航（_data/navigation.yml）未被脚本检查，教程部分的完整性未经目录核对

### E-16 torchtitan
- 环节：分布式训练、检查点、日志与训练故障恢复
- 官方地址：https://github.com/pytorch/torchtitan；仓库：https://github.com/pytorch/torchtitan
- 用途：PyTorch 原生大模型预训练平台：FSDP2/TP/PP/CP 组合并行、DCP 分布式检查点、指标与结构化日志（observability）
- 许可证：预期 BSD-3-Clause；脚本检测 `LICENSE` → BSD-3-Clause；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.4.0` → 提交 `45e33cd413b64cb37a7840cfd3c9765d3c639ae1`（提交日期 2026-10-28T11:02:07-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`torchtitan/trainer.py`、`torchtitan/train.py`、`torchtitan/distributed`、`torchtitan/components/checkpointer`、`torchtitan/observability/metrics.py`、`torchtitan/observability/structured_logger`、`torchtitan/config`
- 关联论文：TorchTitan: One-stop PyTorch native solution for production ready LLM pre-training (arXiv:2410.06511)
- 学习价值：代码量小、模块清晰，适合学习纯 PyTorch 的并行组合、DCP 检查点保存/恢复与训练日志，再对照 Megatron/DeepSpeed
- 本地路径：原始归档 `reference_code/torchtitan_45e33cd_original_en.tar.gz`（sha256 000faa8eb0111929…）；加后缀副本 `reference_code/torchtitan_45e33cd_en/`（路径映射 path_map_en.csv）；保留文件 1061 个 / 17.0 MB，剔除 17 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/torchtitan_docs_45e33cd_en/`，6 个文件（文档源文件 6）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/ 少量 Markdown（调试、评测、基准），主说明在各模块 README；无目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：docs/ 仅少量 Markdown，无目录文件，未计完整

### E-17 accelerate
- 环节：分布式训练、检查点、日志与训练故障恢复
- 官方地址：https://huggingface.co/docs/accelerate；仓库：https://github.com/huggingface/accelerate
- 用途：把同一份 PyTorch 训练脚本运行在单卡/多卡/多机、DeepSpeed/FSDP/Megatron 后端上的薄封装，含状态保存恢复与实验跟踪
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.15.0` → 提交 `6afc1e5ee217051fde702b23de2813344dc0fd33`（提交日期 2026-09-09T14:56:56+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/accelerate/accelerator.py`、`src/accelerate/state.py`、`src/accelerate/checkpointing.py`、`src/accelerate/tracking.py`、`src/accelerate/utils/deepspeed.py`、`src/accelerate/utils/fsdp_utils.py`、`src/accelerate/commands/launch.py`、`examples/by_feature/checkpointing.py`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：transformers/trl/peft 训练的底层启动与检查点机制；小团队从单卡扩到多卡时最直接的入口
- 本地路径：原始归档 `reference_code/accelerate_6afc1e5_original_en.tar.gz`（sha256 5f81c758f568e07c…）；加后缀副本 `reference_code/accelerate_6afc1e5_en/`（路径映射 path_map_en.csv）；保留文件 359 个 / 4.2 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/accelerate_docs_6afc1e5_en/`，62 个文件（文档源文件 58）；目录类型 hf_toctree，目录条目 58，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（_toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

## 环节：语言评测、人工评测和回归测试

### E-18 lm-evaluation-harness
- 环节：语言评测、人工评测和回归测试
- 官方地址：https://github.com/EleutherAI/lm-evaluation-harness；仓库：https://github.com/EleutherAI/lm-evaluation-harness
- 用途：统一的语言模型 few-shot 评测框架：YAML 任务定义、多后端（HF/vLLM/API）、含大量多语种任务（Global-MMLU、Belebele、AfriXNLI、AfriMGSM、INCLUDE、XCOPA 等）
- 许可证：预期 MIT；脚本检测 `LICENSE.md` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.4.13` → 提交 `ddd67220430a2470529f25fd5c05a576ca1057a0`（提交日期 2026-09-01T01:38:54+05:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`lm_eval/evaluator.py`、`lm_eval/api/task.py`、`lm_eval/api/model.py`、`lm_eval/api/metrics.py`、`lm_eval/models/huggingface.py`、`lm_eval/models/vllm_causallms.py`、`lm_eval/tasks/belebele`、`lm_eval/tasks/global_mmlu`、`lm_eval/tasks/afrixnli`、`lm_eval/tasks/include`
- 关联论文：Lessons from the Trenches on Reproducible Evaluation of Language Models (arXiv:2405.14782)
- 学习价值：小语种基准的事实标准评测入口；可学习任务 YAML 写法以新增本地语言基准，并用固定版本做回归测试
- 本地路径：原始归档 `reference_code/lm-evaluation-harness_ddd6722_original_en.tar.gz`（sha256 f9f9df36df4f2b63…）；加后缀副本 `reference_code/lm-evaluation-harness_ddd6722_en/`（路径映射 path_map_en.csv）；保留文件 16388 个 / 13.7 MB，剔除 23 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/lm-evaluation-harness_docs_ddd6722_en/`，13 个文件（文档源文件 12）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/ Markdown（接口、任务指南、新任务指南、去污染说明），无目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：docs/ 为若干 Markdown 指南，无目录文件，未计完整

### E-19 lighteval
- 环节：语言评测、人工评测和回归测试
- 官方地址：https://huggingface.co/docs/lighteval；仓库：https://github.com/huggingface/lighteval
- 用途：HF 的轻量评测工具：多后端（accelerate/vLLM/SGLang/端点），内置多语种任务模板与适配器
- 许可证：预期 MIT；脚本检测 `LICENSE` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.13.0` → 提交 `7c1cd62716b0a198a630c26d781430c54726cd02`（提交日期 2025-11-24T16:34:58+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/lighteval/pipeline.py`、`src/lighteval/tasks/registry.py`、`src/lighteval/tasks/multilingual`、`src/lighteval/metrics/metrics.py`、`src/lighteval/models/model_loader.py`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：FineWeb2/FineTasks 多语种早期信号评测所用框架；多语种任务模板（tasks/multilingual）便于批量生成低资源语言任务
- 本地路径：原始归档 `reference_code/lighteval_7c1cd62_original_en.tar.gz`（sha256 6ed7748ea28f72fa…）；加后缀副本 `reference_code/lighteval_7c1cd62_en/`（路径映射 path_map_en.csv）；保留文件 479 个 / 3.0 MB，剔除 55 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/lighteval_docs_7c1cd62_en/`，27 个文件（文档源文件 26）；目录类型 hf_toctree，目录条目 26，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（_toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

### E-20 sacrebleu
- 环节：语言评测、人工评测和回归测试
- 官方地址：https://github.com/mjpost/sacrebleu；仓库：https://github.com/mjpost/sacrebleu
- 用途：可复现的机器翻译自动评测：BLEU/chrF/TER 及签名、多种分词器（含 flores spm 分词）与显著性检验
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE.txt` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v2.6.0` → 提交 `2277caccfc7b956671a6a09f1646f62250034157`（提交日期 2026-01-12T18:07:17+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`sacrebleu/metrics/bleu.py`、`sacrebleu/metrics/chrf.py`、`sacrebleu/metrics/ter.py`、`sacrebleu/tokenizers`、`sacrebleu/significance.py`、`sacrebleu/dataset`
- 关联论文：A Call for Clarity in Reporting BLEU Scores (arXiv:1804.08771)
- 学习价值：小语种翻译评测必用；chrF 与 spBLEU（flores 分词）对形态丰富/无空格语言更稳健，签名机制保证结果可比
- 本地路径：原始归档 `reference_code/sacrebleu_2277cac_original_en.tar.gz`（sha256 31fffd063ead0ce1…）；加后缀副本 `reference_code/sacrebleu_2277cac_en/`（路径映射 path_map_en.csv）；保留文件 57 个 / 0.5 MB，剔除 1 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：未保存文档集。无独立文档目录，说明在 README 与 DATASETS.md；不构成文档集

### E-21 COMET
- 环节：语言评测、人工评测和回归测试
- 官方地址：https://unbabel.github.io/COMET；仓库：https://github.com/Unbabel/COMET
- 用途：基于多语种编码器的神经机器翻译评测指标（COMET、CometKiwi 无参考质量估计、xCOMET 错误片段）及训练/打分 CLI
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v2.2.7` → 提交 `49c348dd0ff569c4d7c3f2b7c720fd5696f8de59`（提交日期 2025-05-21T11:37:19+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`comet/models`、`comet/encoders/xlmr.py`、`comet/cli/score.py`、`comet/cli/train.py`、`comet/cli/mbr.py`
- 关联论文：COMET: A Neural Framework for MT Evaluation (arXiv:2009.09025)；xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection (arXiv:2310.10482)
- 学习价值：学习型评测指标的实现；需注意其编码器对低资源语言覆盖有限，适合与 chrF、人工评测对照
- 本地路径：原始归档 `reference_code/COMET_49c348d_original_en.tar.gz`（sha256 161b239bd41ba973…）；加后缀副本 `reference_code/COMET_49c348d_en/`（路径映射 path_map_en.csv）；保留文件 90 个 / 1.8 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/COMET_docs_49c348d_en/`，16 个文件（文档源文件 6）；目录类型 sphinx_toctree，目录条目 4，缺失 0，解析率 1.0；**未计为完整文档集**。范围：仓库内 docs/source（Sphinx）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：Sphinx 目录全部解析（5 条，人工复核 5/5），但文档源文件少于脚本默认下限 10 个，故未计完整文档集；官方文档本身规模很小

### E-22 argilla
- 环节：语言评测、人工评测和回归测试；交叉环节：数据版本管理、训练数据配比及质量审计
- 官方地址：https://docs.argilla.io；仓库：https://github.com/argilla-io/argilla
- 用途：人工标注与数据质量协作平台：Python SDK + 服务端，支持评分、排序、文本修正等问题类型与多人标注分配
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v2.8.0` → 提交 `78cb5183f72e59857cf4da3015c42a91c3b46205`（提交日期 2025-03-10T09:51:29+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`argilla/src/argilla/client.py`、`argilla/src/argilla/datasets`、`argilla/src/argilla/records`、`argilla/src/argilla/settings`、`argilla-server/src/argilla_server/api/handlers/v1/datasets/records.py`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：组织母语者做人工评测、偏好标注与数据纠错的开源平台；可学习标注任务模式与标注一致性管理
- 本地路径：原始归档 `reference_code/argilla_78cb518_original_en.tar.gz`（sha256 09079a3f6ba65fce…）；加后缀副本 `reference_code/argilla_78cb518_en/`（路径映射 path_map_en.csv）；保留文件 3133 个 / 236.5 MB，剔除 20 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `argilla/docs` → `engineering_docs/argilla_docs_78cb518_en/`，110 个文件（文档源文件 53）；目录类型 mkdocs_nav，目录条目 29，缺失 2，解析率 0.931；**未计为完整文档集**。范围：仓库内 argilla/docs（argilla/mkdocs.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：mkdocs 导航缺 community/changelog、community/popular_issues 两页，均由 docs/scripts/gen_changelog.py、gen_popular_issues.py 构建时生成；解析率 0.931，未计完整
- 版本备注：v2.8.0 为最新 tag（2025-03-10），此后项目更新明显放缓

## 环节：多语言检索、RAG、工具调用及智能体

### E-23 sentence-transformers
- 环节：多语言检索、RAG、工具调用及智能体
- 官方地址：https://www.sbert.net；仓库：https://github.com/UKPLab/sentence-transformers
- 用途：句向量/稀疏向量/交叉编码器的训练与推理库，含多语种知识蒸馏训练示例与检索评测器
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v6.2.0` → 提交 `0b6937d55981e3486caf9b64ad2664c9a9edb51d`（提交日期 2026-10-21T13:15:54+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`sentence_transformers/sentence_transformer/model.py`、`sentence_transformers/sentence_transformer/trainer.py`、`sentence_transformers/cross_encoder`、`sentence_transformers/sparse_encoder`、`examples/sentence_transformer/training/multilingual/make_multilingual.py`
- 关联论文：Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (arXiv:1908.10084)；Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation (arXiv:2004.09813)
- 学习价值：用平行语料把英文句向量蒸馏到小语种的官方示例，是低资源检索模型的直接参考
- 本地路径：原始归档 `reference_code/sentence-transformers_0b6937d_original_en.tar.gz`（sha256 83d4c1ff9e55b262…）；加后缀副本 `reference_code/sentence-transformers_0b6937d_en/`（路径映射 path_map_en.csv）；保留文件 832 个 / 23.6 MB，剔除 1 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/sentence-transformers_docs_0b6937d_en/`，153 个文件（文档源文件 100）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/（Sphinx 源；根 index.rst 位于仓库根，docs/ 下为分节文件）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：Sphinx 根 index.rst 位于仓库根目录而非 docs/，按 docs/ 路径保存时脚本找不到根目录 toctree；人工以源码副本（含根 index.rst 与 docs/）解析得 77 条全部存在。按规则未计完整

### E-24 FlagEmbedding
- 环节：多语言检索、RAG、工具调用及智能体
- 官方地址：https://github.com/FlagOpen/FlagEmbedding；仓库：https://github.com/FlagOpen/FlagEmbedding
- 用途：BGE 系列检索模型（含多语种 BGE-M3 稠密/稀疏/多向量）与重排器的推理、微调和评测代码
- 许可证：预期 MIT；脚本检测 `LICENSE` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.4.2` → 提交 `fd1a2bdf69488ffebe0327999d4400d8c8058a0b`（提交日期 2026-08-24T10:54:09+08:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`FlagEmbedding/inference/embedder/encoder_only/m3.py`、`FlagEmbedding/finetune/embedder/encoder_only/m3`、`FlagEmbedding/abc/finetune/embedder`、`FlagEmbedding/evaluation/miracl`、`FlagEmbedding/evaluation/mkqa`、`FlagEmbedding/evaluation/mldr`
- 关联论文：M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation (arXiv:2402.03216)
- 学习价值：多语种检索模型微调与 MIRACL/MKQA/MLDR 多语种检索评测的实现，可用于小语种 RAG 检索器选型与微调
- 本地路径：原始归档 `reference_code/FlagEmbedding_fd1a2bd_original_en.tar.gz`（sha256 bff9b325a8f10e94…）；加后缀副本 `reference_code/FlagEmbedding_fd1a2bd_en/`（路径映射 path_map_en.csv）；保留文件 1150 个 / 50.3 MB，剔除 2 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/FlagEmbedding_docs_fd1a2bd_en/`，178 个文件（文档源文件 166）；目录类型 sphinx_toctree，目录条目 11，缺失 1，解析率 0.909；**未计为完整文档集**。范围：仓库内 docs/source（Sphinx）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：唯一“缺失”条目为 Sphinx 特殊条目 self（指向页面自身），脚本误作文件；去掉后人工复核其余条目全部存在。按规则仍记为未计完整

### E-25 haystack
- 环节：多语言检索、RAG、工具调用及智能体
- 官方地址：https://docs.haystack.deepset.ai；仓库：https://github.com/deepset-ai/haystack
- 用途：以组件+有向图管线组织的 RAG 与智能体框架：检索器、嵌入器、生成器、工具调用 Agent
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v3.4.1` → 提交 `7f0ab62afb01c096557d5d69ec57276dd6583a57`（提交日期 2026-10-21T19:10:09Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`haystack/core/pipeline/pipeline.py`、`haystack/components/retrievers`、`haystack/components/embedders`、`haystack/components/generators`、`haystack/components/agents/agent.py`、`haystack/tools/component_tool.py`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：生产化 RAG 管线与工具调用的清晰组件抽象；与 LlamaIndex 同质，选 Haystack 因其管线序列化与评测组件更适合工程化回归
- 本地路径：原始归档 `reference_code/haystack_7f0ab62_original_en.tar.gz`（sha256 648b37bead3d5553…）；加后缀副本 `reference_code/haystack_7f0ab62_en/`（路径映射 path_map_en.csv）；保留文件 12130 个 / 105.0 MB，剔除 4 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs-website/docs` → `engineering_docs/haystack_docs_7f0ab62_en/`，470 个文件（文档源文件 470）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs-website/docs（Docusaurus 当前版本文档；目录为 docs-website/sidebars.js，未纳入本路径）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：Docusaurus 目录 docs-website/sidebars.js 不在保存路径内，且脚本实际不解析 Docusaurus sidebars（与其文档字符串所述不符），未计完整

### E-26 docling
- 环节：多语言检索、RAG、工具调用及智能体；交叉环节：语料获取、清洗、语言识别、去重和分词
- 官方地址：https://docling-project.github.io/docling；仓库：https://github.com/docling-project/docling
- 用途：PDF/Office/HTML 等文档解析为结构化表示：版面分析、表格结构、OCR（多引擎）与导出 Markdown/JSON
- 许可证：预期 MIT；脚本检测 `LICENSE` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v2.144.0` → 提交 `a857fd208ccd61fb4a5d230384554ce778f216df`（提交日期 2026-10-28T12:03:07Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`docling/document_converter.py`、`docling/pipeline/standard_pdf_pipeline.py`、`docling/pipeline/simple_pipeline.py`、`docling/models/stages/ocr`、`docling/backend`
- 关联论文：Docling Technical Report (arXiv:2408.09869)
- 学习价值：小语种资料常以扫描 PDF/政府文件存在，文档解析与 OCR 引擎选择直接决定 RAG 与语料抽取质量
- 本地路径：原始归档 `reference_code/docling_a857fd2_original_en.tar.gz`（sha256 0563e0ee60af062a…）；加后缀副本 `reference_code/docling_a857fd2_en/`（路径映射 path_map_en.csv）；保留文件 1869 个 / 125.9 MB，剔除 28 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/docling_docs_a857fd2_en/`，162 个文件（文档源文件 91）；目录类型 mkdocs_nav，目录条目 115，缺失 53，解析率 0.539；**未计为完整文档集**。范围：仓库内 docs/（根目录 mkdocs.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：mkdocs 导航 115 条中 53 条指向 _generated/examples/*（构建时由 docs/examples/*.py 生成），解析率 0.539，未计完整

### E-27 smolagents
- 环节：多语言检索、RAG、工具调用及智能体；交叉环节：对话产品、编程工具、IDE 扩展及执行隔离
- 官方地址：https://huggingface.co/docs/smolagents；仓库：https://github.com/huggingface/smolagents
- 用途：极简智能体库：以代码为动作的 CodeAgent、工具调用 Agent、本地受限 Python 解释器与远程沙箱执行器
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.26.0` → 提交 `12c1bc820eca50ace6f80a21d90426d41d74f845`（提交日期 2026-05-29T07:08:24+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/smolagents/agents.py`、`src/smolagents/tools.py`、`src/smolagents/default_tools.py`、`src/smolagents/local_python_executor.py`、`src/smolagents/remote_executors.py`、`src/smolagents/models.py`
- 关联论文：Executable Code Actions Elicit Better LLM Agents (arXiv:2402.01030)
- 学习价值：代码量小，适合理解工具调用循环与代码执行隔离；文档含多语种版本（es/hi/ko/zh）
- 本地路径：原始归档 `reference_code/smolagents_12c1bc8_original_en.tar.gz`（sha256 392ff42801fc2d03…）；加后缀副本 `reference_code/smolagents_12c1bc8_en/`（路径映射 path_map_en.csv）；保留文件 184 个 / 2.7 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs/source` → `engineering_docs/smolagents_docs_12c1bc8_en/`，80 个文件（文档源文件 70）；目录类型 hf_toctree，目录条目 70，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/source（en/es/hi/ko/zh 各自 _toctree.yml）；格式：源文件（Markdown/RST，未构建 HTML）

## 环节：推理服务、量化、容器化、API 与流式输出

### E-28 vllm
- 环节：推理服务、量化、容器化、API 与流式输出
- 官方地址：https://docs.vllm.ai；仓库：https://github.com/vllm-project/vllm
- 用途：高吞吐推理与服务引擎：PagedAttention KV 缓存、连续批处理、OpenAI 兼容 API 与流式输出、多种量化格式加载
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.32.0` → 提交 `5df63a7203cdb9328d824a27b682e77c7b9928be`（提交日期 2026-10-17T11:57:10-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`vllm/v1/engine/core.py`、`vllm/v1/engine/async_llm.py`、`vllm/v1/core/sched/scheduler.py`、`vllm/v1/core/kv_cache_manager.py`、`vllm/entrypoints/openai/api_server.py`、`vllm/entrypoints/openai/chat_completion/serving.py`、`vllm/model_executor/layers/quantization`
- 关联论文：Efficient Memory Management for Large Language Model Serving with PagedAttention (arXiv:2309.06180)
- 学习价值：部署小语种模型的主流服务端；需关注分词效率差导致的序列变长对 KV 缓存与吞吐的影响
- 本地路径：原始归档 `reference_code/vllm_5df63a7_original_en.tar.gz`（sha256 bfb53c0aa17e7d9b…）；加后缀副本 `reference_code/vllm_5df63a7_en/`（路径映射 path_map_en.csv）；保留文件 7711 个 / 117.7 MB，剔除 4 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/vllm_docs_5df63a7_en/`，357 个文件（文档源文件 243）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/（mkdocs.yaml + .nav.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：导航为 mkdocs.yaml（.yaml 扩展名）+ awesome-nav 插件的 .nav.yml，脚本只识别 mkdocs.yml，未解析到目录，未计完整

### E-29 llama.cpp
- 环节：推理服务、量化、容器化、API 与流式输出
- 官方地址：https://github.com/ggml-org/llama.cpp；仓库：https://github.com/ggml-org/llama.cpp
- 用途：C/C++ 本地推理：GGUF 格式转换、k-quant 等低比特量化、CPU/GPU 多后端、带 OpenAI 兼容接口的 llama-server
- 许可证：预期 MIT；脚本检测 `LICENSE` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.8.0` → 提交 `8642541b255bfb5dc39cd351a178be09013a55d6`（提交日期 2026-10-28T13:30:38+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`convert_hf_to_gguf.py`、`gguf-py/gguf/gguf_writer.py`、`src/llama-vocab.cpp`、`src/llama-quant.cpp`、`ggml/src/ggml-quants.c`、`tools/quantize/quantize.cpp`、`tools/server/server-chat.cpp`、`tools/server/README.md`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：小语种社区在低端设备/离线环境部署的首选；可学习词表（含扩展词表）如何写入 GGUF 及量化对低资源语言质量的影响
- 本地路径：原始归档 `reference_code/llamacpp_8642541_original_en.tar.gz`（sha256 59caecd55d6ecb30…）；加后缀副本 `reference_code/llamacpp_8642541_en/`（路径映射 path_map_en.csv）；保留文件 3920 个 / 102.3 MB，剔除 22 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/llamacpp_docs_8642541_en/`，70 个文件（文档源文件 53）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/ Markdown（构建、后端、多模态等），无目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：docs/ 为 Markdown 指南，无目录文件，未计完整

### E-30 sglang
- 环节：推理服务、量化、容器化、API 与流式输出
- 官方地址：https://docs.sglang.ai；仓库：https://github.com/sgl-project/sglang
- 用途：高性能服务框架：RadixAttention 前缀缓存、结构化输出（语法约束解码）、函数调用解析、OpenAI 兼容 API
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.5.22` → 提交 `baa9befa381511cd4d56f83980951e5a45fffc6d`（提交日期 2026-10-13T23:26:00-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`python/sglang/srt/managers/scheduler.py`、`python/sglang/srt/managers/tokenizer_manager.py`、`python/sglang/srt/mem_cache/radix_cache.py`、`python/sglang/srt/constrained`、`python/sglang/srt/function_call`、`python/sglang/srt/entrypoints/http_server.py`、`python/sglang/srt/entrypoints/openai/serving_chat.py`
- 关联论文：SGLang: Efficient Execution of Structured Language Model Programs (arXiv:2312.07104)
- 学习价值：与 vLLM 互补：前缀缓存与约束解码、工具调用解析器的实现，适合多轮对话与智能体服务
- 本地路径：原始归档 `reference_code/sglang_baa9bef_original_en.tar.gz`（sha256 d94d07352842661d…）；加后缀副本 `reference_code/sglang_baa9bef_en/`（路径映射 path_map_en.csv）；保留文件 10589 个 / 139.9 MB，剔除 3 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/sglang_docs_baa9bef_en/`，614 个文件（文档源文件 357）；目录类型 docs.json，目录条目 341，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（Mintlify docs.json 导航）；格式：源文件（Markdown/RST，未构建 HTML）

### E-31 llm-compressor
- 环节：推理服务、量化、容器化、API 与流式输出
- 官方地址：https://docs.vllm.ai/projects/llm-compressor；仓库：https://github.com/vllm-project/llm-compressor
- 用途：面向 vLLM 部署的训练后量化/压缩库：GPTQ、AWQ、SmoothQuant、FP8、AutoRound 等修改器与 oneshot 入口
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `0.15.0` → 提交 `04546e05125298c87b267253959eff39c6968925`（提交日期 2026-10-28T17:12:10Z）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`src/llmcompressor/entrypoints/oneshot.py`、`src/llmcompressor/modifiers/gptq`、`src/llmcompressor/modifiers/awq`、`src/llmcompressor/modifiers/quantization`、`src/llmcompressor/modifiers/smoothquant`、`examples/awq/llama_example.py`
- 关联论文：GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (arXiv:2210.17323)；AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration (arXiv:2306.00978)
- 学习价值：量化校准数据的语言分布会影响小语种质量；可学习如何用目标语言校准集做 GPTQ/AWQ（AutoAWQ 已归档，由本项目接替）
- 本地路径：原始归档 `reference_code/llm-compressor_04546e0_original_en.tar.gz`（sha256 68f21f3c6d375069…）；加后缀副本 `reference_code/llm-compressor_04546e0_en/`（路径映射 path_map_en.csv）；保留文件 816 个 / 6.0 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/llm-compressor_docs_04546e0_en/`，84 个文件（文档源文件 66）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/（.nav.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：导航为 .nav.yml（awesome-nav），脚本不支持，未计完整

## 环节：对话产品、编程工具、IDE 扩展及执行隔离

### E-32 open-webui
- 环节：对话产品、编程工具、IDE 扩展及执行隔离
- 官方地址：https://docs.openwebui.com；仓库：https://github.com/open-webui/open-webui
- 用途：自托管对话界面：对接 Ollama/OpenAI 兼容接口、RAG 知识库、工具/函数、代码解释器、模型评测（竞技场）与多语言界面
- 许可证：预期 Open WebUI License（BSD-3 衍生并附品牌保留条款）；脚本检测 `LICENSE` → BSD-3-Clause；人工确认：检测值不准确：LICENSE 为“Open WebUI License”，在 BSD-3 条款基础上增加品牌保留条款（不得移除/修改 Open WebUI 品牌，除非用户数≤50 或获企业授权等）；非标准 OSI 许可证
- 版本：ref `v0.12.5` → 提交 `f7ac7ee10962ddec0017f5c29b6740d9b9c5faca`（提交日期 2026-10-29T18:05:24+09:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`backend/open_webui/main.py`、`backend/open_webui/routers/openai.py`、`backend/open_webui/routers/ollama.py`、`backend/open_webui/routers/retrieval.py`、`backend/open_webui/routers/evaluations.py`、`backend/open_webui/utils/middleware.py`、`backend/open_webui/utils/code_interpreter.py`、`src/lib/i18n`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：小语种模型面向用户的最短路径；其界面 i18n 翻译机制、RAG 与评测竞技场可直接用于收集母语者反馈
- 本地路径：原始归档 `reference_code/open-webui_f7ac7ee_original_en.tar.gz`（sha256 87d298f5a720beb9…）；加后缀副本 `reference_code/open-webui_f7ac7ee_en/`（路径映射 path_map_en.csv）；保留文件 5195 个 / 52.7 MB，剔除 4 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：独立文档仓库 https://github.com/open-webui/docs 提交 `c4f49998d7416a1defba7c2e78dbcf9c16ff8ac4`（原始归档 `reference_code/open-webui-docs_c4f4999_original_en.tar.gz`）的 `docs` → `engineering_docs/open-webui_docs_c4f4999_en/`，511 个文件（文档源文件 459）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：官方文档站源仓库 open-webui/docs 的 docs/（Docusaurus，自动生成侧边栏）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：Docusaurus 自动生成侧边栏（sidebars.ts），脚本不解析，未计完整

### E-33 continue
- 环节：对话产品、编程工具、IDE 扩展及执行隔离
- 官方地址：https://docs.continue.dev；仓库：https://github.com/continuedev/continue
- 用途：开源 IDE 编程助手（VS Code / JetBrains 扩展）：对话、补全、代码库索引检索、工具调用与可配置模型提供方
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v2.1.0-vscode` → 提交 `b238c1f11f26805f4387e10bab878b009f98e7a4`（提交日期 2026-06-18T17:23:08-07:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`core/autocomplete/CompletionProvider.ts`、`core/config/load.ts`、`core/context/providers/index.ts`、`core/indexing/CodebaseIndexer.ts`、`core/tools/definitions`、`core/llm/llms/Ollama.ts`、`extensions/vscode`、`extensions/intellij`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：IDE 扩展形态的参考：如何接入自托管模型、代码库检索与工具调用；可评估小语种注释/提示下的编程助手体验
- 本地路径：原始归档 `reference_code/continue_b238c1f_original_en.tar.gz`（sha256 8c918bb0932b3201…）；加后缀副本 `reference_code/continue_b238c1f_en/`（路径映射 path_map_en.csv）；保留文件 3043 个 / 154.1 MB，剔除 14 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/continue_docs_b238c1f_en/`，408 个文件（文档源文件 153）；目录类型 docs.json，目录条目 94，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（Mintlify docs.json 导航）；格式：源文件（Markdown/RST，未构建 HTML）

### E-34 OpenHands-software-agent-sdk
- 环节：对话产品、编程工具、IDE 扩展及执行隔离
- 官方地址：https://docs.openhands.dev；仓库：https://github.com/OpenHands/software-agent-sdk
- 用途：OpenHands 智能体核心 SDK：Agent 循环、对话状态、工具（终端/文件编辑/浏览器）、Docker/远程/Apptainer 沙箱工作区与 agent server
- 许可证：预期 MIT；脚本检测 `LICENSE` → MIT；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.59.0` → 提交 `ccae18cb897bef7960f210aa3f380b577a84be7c`（提交日期 2026-10-28T15:34:29+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`openhands-sdk/openhands/sdk/agent/agent.py`、`openhands-sdk/openhands/sdk/conversation`、`openhands-sdk/openhands/sdk/llm`、`openhands-sdk/openhands/sdk/security`、`openhands-tools/openhands/tools/terminal`、`openhands-tools/openhands/tools/file_editor`、`openhands-workspace/openhands/workspace/docker`、`openhands-agent-server/openhands/agent_server`
- 关联论文：OpenHands: An Open Platform for AI Software Developers as Generalist Agents (arXiv:2407.16741)
- 学习价值：主仓库 OpenHands 1.x 已只剩应用服务与前端，智能体与执行隔离核心迁到本 SDK；可学习沙箱工作区、危险动作确认与安全分析器
- 本地路径：原始归档 `reference_code/OpenHands-software-agent-sdk_ccae18c_original_en.tar.gz`（sha256 83835720c0573adf…）；加后缀副本 `reference_code/OpenHands-software-agent-sdk_ccae18c_en/`（路径映射 path_map_en.csv）；保留文件 1957 个 / 23.5 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：独立文档仓库 https://github.com/OpenHands/docs 提交 `b053812969689d9dab97bbcd969f03f7cfb71a3b`（原始归档 `reference_code/OpenHands-software-agent-sdk-docs_b053812_original_en.tar.gz`）的 `.` → `engineering_docs/OpenHands-software-agent-sdk_docs_b053812_en/`，524 个文件（文档源文件 369）；目录类型 sphinx_toctree，目录条目 1，缺失 1，解析率 0.0；**未计为完整文档集**。范围：官方文档源仓库 OpenHands/docs 全部（Mintlify docs.json；含 SDK 与应用文档）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：根目录有 Mintlify docs.json，但脚本先命中 scripts/sphinx/source 下的 Sphinx toctree（1 条、缺 1 条）而跳过 docs.json，得 0.0；人工按脚本同一 docs.json 规则解析得 308 条、缺 2 条（两个 api-reference 为 OpenAPI 自动生成页），约 0.994。按规则记为未计完整

### E-35 aider
- 环节：对话产品、编程工具、IDE 扩展及执行隔离
- 官方地址：https://aider.chat；仓库：https://github.com/Aider-AI/aider
- 用途：终端结对编程助手：基于 tree-sitter 的仓库地图、多种编辑格式（search/replace、unified diff）、自动 lint/测试与 git 提交
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE.txt` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v0.86.2` → 提交 `253f0368b873ba30d8ee26e463718f0c03614ddf`（提交日期 2026-02-11T16:42:24-08:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`aider/coders/base_coder.py`、`aider/coders/editblock_coder.py`、`aider/coders/udiff_coder.py`、`aider/repomap.py`、`aider/linter.py`、`aider/models.py`、`aider/queries`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：与 IDE 扩展互补的命令行形态；编辑格式与仓库地图的设计说明了模型输出格式遵循能力的重要性（小模型尤甚）
- 本地路径：原始归档 `reference_code/aider_253f036_original_en.tar.gz`（sha256 0828b494138f848c…）；加后缀副本 `reference_code/aider_253f036_en/`（路径映射 path_map_en.csv）；保留文件 562 个 / 17.8 MB，剔除 123 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `aider/website/docs` → `engineering_docs/aider_docs_253f036_en/`，84 个文件（文档源文件 84）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 aider/website/docs（Jekyll 站点源），无可解析目录文件；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：Jekyll 站点源，无脚本可解析的目录，未计完整

## 环节：运行监控、成本统计、灰度发布和回滚

### E-36 prometheus
- 环节：运行监控、成本统计、灰度发布和回滚
- 官方地址：https://prometheus.io/docs；仓库：https://github.com/prometheus/prometheus
- 用途：时序指标采集、存储、PromQL 查询与告警规则引擎（vLLM/SGLang 等推理服务均暴露 Prometheus 指标）
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v3.15.1` → 提交 `bae3eced0a5369e050e83ea73bc381d7c4b1a719`（提交日期 2026-10-21T15:24:03+02:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`scrape/scrape.go`、`tsdb/head.go`、`promql/engine.go`、`rules/alerting.go`、`rules/manager.go`、`storage/remote/queue_manager.go`、`model/rulefmt/rulefmt.go`、`documentation/examples/prometheus.yml`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：推理服务延迟、吞吐、token 用量与错误率监控和告警的基础设施
- 本地路径：原始归档 `reference_code/prometheus_bae3ece_original_en.tar.gz`（sha256 a5b2a817583221b2…）；加后缀副本 `reference_code/prometheus_bae3ece_en/`（路径映射 path_map_en.csv）；保留文件 1685 个 / 19.4 MB，剔除 1 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/prometheus_docs_bae3ece_en/`，32 个文件（文档源文件 30）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：仓库内 docs/ Markdown（配置、查询、存储等；站点导航在独立的 prometheus/docs 站点仓库，未纳入）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：仓库内 docs/ 无导航文件（导航在独立的 prometheus/docs 站点仓库），未计完整

### E-37 opentelemetry-python
- 环节：运行监控、成本统计、灰度发布和回滚
- 官方地址：https://opentelemetry.io/docs/languages/python；仓库：https://github.com/open-telemetry/opentelemetry-python
- 用途：OpenTelemetry Python API/SDK：链路追踪、指标、日志与 OTLP 导出器
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.45.1` → 提交 `14971cef9c84c2354cbaf6871090896fad0f9a1a`（提交日期 2026-10-06T14:29:19-03:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`opentelemetry-api/src/opentelemetry/trace/__init__.py`、`opentelemetry-api/src/opentelemetry/metrics/__init__.py`、`opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py`、`opentelemetry-sdk/src/opentelemetry/sdk/metrics/__init__.py`、`opentelemetry-sdk/src/opentelemetry/sdk/_logs/__init__.py`、`exporter/opentelemetry-exporter-otlp-proto-grpc`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：LLM 应用可观测性（Langfuse 等均以 OTLP 接入）的标准层；可学习为 RAG/智能体调用链打点
- 本地路径：原始归档 `reference_code/opentelemetry-python_14971ce_original_en.tar.gz`（sha256 e010d97b5c4e79ac…）；加后缀副本 `reference_code/opentelemetry-python_14971ce_en/`（路径映射 path_map_en.csv）；保留文件 1115 个 / 6.9 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/opentelemetry-python_docs_14971ce_en/`，148 个文件（文档源文件 71）；目录类型 sphinx_toctree，目录条目 2，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（Sphinx API 参考与示例）；概念文档在 opentelemetry.io 站点仓库，体量过大未收；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：脚本只解析到 2 条目录（连续两个 toctree 时前一块的结束匹配吞掉后一块开头），但判定为完整；人工复核全部 toctree 得 21 条全部存在，完整判定成立

### E-38 langfuse
- 环节：运行监控、成本统计、灰度发布和回滚；交叉环节：语言评测、人工评测和回归测试
- 官方地址：https://langfuse.com/docs；仓库：https://github.com/langfuse/langfuse
- 用途：LLM 应用工程平台：调用链追踪（OTel 接入）、token 与成本统计、提示词版本管理、数据集实验、LLM-as-judge 与人工标注队列
- 许可证：预期 MIT（ee/ 目录另有商业许可）；脚本检测 `LICENSE` → MIT；人工确认：LICENSE 为 MIT，但 ee/、web/src/ee/、worker/src/ee/、packages/shared/src/server/ee/ 目录另按 ee/LICENSE（商业许可）授权；检测值只反映主体部分
- 版本：ref `v4.71.0` → 提交 `d89f49b82620dc9a773bd2f97449289f4f6c199e`（提交日期 2026-10-27T16:01:24+01:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`worker/src/features/otel-ingestion`、`worker/src/features/tokenisation`、`worker/src/features/evaluation`、`packages/shared/src/server/ingestion`、`packages/shared/clickhouse/migrations`、`web/src/features/prompts`、`web/src/features/datasets`、`web/src/features/annotation-queues`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：按模型/用户/语言统计成本与质量的线上闭环；提示词版本与数据集实验可支撑灰度对比与回归
- 本地路径：原始归档 `reference_code/langfuse_d89f49b_original_en.tar.gz`（sha256 dabb2f0b4a8021cb…）；加后缀副本 `reference_code/langfuse_d89f49b_en/`（路径映射 path_map_en.csv）；保留文件 7492 个 / 55.1 MB，剔除 2 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：独立文档仓库 https://github.com/langfuse/langfuse-docs 提交 `f7a44fa1961eedb2d430877ea656802c76b46837`（原始归档 `reference_code/langfuse-docs_f7a44fa_original_en.tar.gz`）的 `content` → `engineering_docs/langfuse_docs_f7a44fa_en/`，1106 个文件（文档源文件 1028）；目录类型 None，目录条目 0，缺失 0，解析率 None；**未计为完整文档集**。范围：官方站点源仓库 langfuse-docs 的 content/（docs、self-hosting、integrations、faq、guides 等 MDX；目录为各级 meta.json）；格式：源文件（Markdown/RST，未构建 HTML）
- 文档人工说明：langfuse-docs 为 Next.js 站点，目录为各级 meta.json，脚本不支持，未计完整；独立文档仓库原始归档含站点图片等资源

### E-39 argo-rollouts
- 环节：运行监控、成本统计、灰度发布和回滚
- 官方地址：https://argo-rollouts.readthedocs.io；仓库：https://github.com/argoproj/argo-rollouts
- 用途：Kubernetes 渐进式发布控制器：金丝雀/蓝绿发布、流量切分、基于 Prometheus 等指标的自动分析与自动回滚
- 许可证：预期 Apache-2.0；脚本检测 `LICENSE` → Apache-2.0；人工确认：与检测一致（已读许可证文件开头）
- 版本：ref `v1.10.1` → 提交 `356117c8e9a21b74b58c2c01d640aa91994522b5`（提交日期 2026-10-12T14:30:54+03:00）；检索日 2026-10-29
- 核心模块（已在该提交文件树中核对存在）：`rollout/canary.go`、`rollout/bluegreen.go`、`rollout/analysis.go`、`analysis/analysis.go`、`metricproviders/prometheus/prometheus.go`、`pkg/apis/rollouts/v1alpha1/types.go`、`examples/analysis-templates.yaml`
- 关联论文：无对应论文（工程项目，无官方论文）
- 学习价值：新版小语种模型上线时按指标灰度、失败自动回滚的标准做法；与 Prometheus 指标直接衔接
- 本地路径：原始归档 `reference_code/argo-rollouts_356117c_original_en.tar.gz`（sha256 549923c9069752a8…）；加后缀副本 `reference_code/argo-rollouts_356117c_en/`（路径映射 path_map_en.csv）；保留文件 1011 个 / 27.1 MB，剔除 0 项（权重/数据/归档/二进制/>5MB/符号链接）
- 文档：仓库内 `docs` → `engineering_docs/argo-rollouts_docs_356117c_en/`，189 个文件（文档源文件 126）；目录类型 mkdocs_nav，目录条目 121，缺失 0，解析率 1.0；**是完整文档集**。范围：仓库内 docs/（根目录 mkdocs.yml 导航）；格式：源文件（Markdown/RST，未构建 HTML）

