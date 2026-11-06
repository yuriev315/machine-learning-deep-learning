# 类别 19 工程资料：检索与选择日志

- 检索/核验日期：2026-10-29
- 方法：按协调者给定的 9 个工程环节，从候选清单中按“互补、官方、活跃维护、对小语种开发有直接用途”挑选；每个候选先用 `python3 -I scripts/engineering_en.py refs <url>` 查真实 tag，再在暂存目录用无 blob 的浅层 fetch（`git fetch --depth 1 --filter=blob:none`，不检出、不执行）列出文件树，用于：确认 tag 对应提交日期、核对 core_modules 路径确实存在、定位文档源目录与目录（TOC）文件类型。之后才写入种子并用 `engineering_en.py fetch` 正式下载。
- ref 规则：一律写具体 tag；无 tag 或最新 tag 明显过旧的写完整提交号（GlotLID、text-dedup、open-instruct，以及三个文档仓库 dvc.org / open-webui/docs / OpenHands/docs / langfuse-docs）。未写 main/latest。
- 关联论文：本库论文代理尚未完成（检索时 `scripts/state/claims_en.json` 仅 1 条，与本类项目无关），故 related_papers 写“英文标题 (arXiv:ID)”。全部 32 个 arXiv ID 已用 arXiv API（一次 id_list 查询）核对标题与首次提交日期，无编造。

## tag 选择中发现的问题（据实记录）
| 项目 | 现象 | 处理 |
|---|---|---|
| datatrove | 原测试种子 ref 为 v0.6.0（旧） | 改为 v0.10.1（2026-09-30） |
| sentencepiece | 存在 `1.0.0` tag，但其提交日期为 2019-06-11（历史遗留标签，非新版） | 选 v0.2.2（2026-07-02） |
| tokenizers | 有 v1.0.0-rc.* 预发布 | 选最新稳定版 v0.23.3 |
| text-dedup | 最新 tag 2023.09.20 / 0.4.1 过旧 | 固定 2026-03-09 提交 7538f3ec… |
| GlotLID | 仓库无 tag | 固定 2026-04-15 提交 d63cc2f6… |
| open-instruct | 仅 v0.1.0–v0.3.0 旧 tag 与 runs/ledger 实验标签 | 固定 2026-10-28 提交 64beb76c… |
| Megatron-LM | 有 26.09-*.rc 容器标签与 core_v* 发布标签 | 选 Megatron Core 正式发布 core_v0.19.2 |
| torchtitan | 大量 ciflow/* CI 标签 | 选 v0.4.0（2026-10-28） |
| vllm | 有 v0.33.0rc* | 选稳定版 v0.32.0 |
| llama.cpp | 有大量 backup/* 分支式标签；v0.x 为语义版本 tag | 选 v0.8.0（提交日期 2026-10-28） |
| continue | v1.5.x 与 v2.x-vscode 两条线 | v2.1.0-vscode（2026-06-18）比 v1.5.45（2026-03-04）新，选前者 |
| argilla | v2.8.0 为最新 tag，提交日期 2025-03-10 | 照录，注明项目更新放缓 |
| OpenHands | 主仓库 1.11.0 中 openhands/ 只剩 app_server 与前端，智能体核心与沙箱已迁出 | 改收官方 OpenHands/software-agent-sdk v1.59.0，文档取 OpenHands/docs 仓库 |

## 各环节选择理由与未选同质项目

### 1 语料获取、清洗、语言识别、去重和分词
- 选：datatrove（流水线，FineWeb2 实际使用）、GlotLID（低资源 LID，专门面向 2000+ 语言）、sentencepiece（语言无关子词训练）、tokenizers（HF 生态实际分词实现）、text-dedup（独立去重算法实现）。
- 不选：OpenLID 数据集仓库（与 GlotLID 同为 fastText LID，GlotLID 覆盖语言更多且明确面向低资源）；fastText 主仓库（已于 2024 年归档，LID 模型使用方式在 GlotLID/datatrove 中已有）；NeMo-Curator（与 datatrove 同质，体量大）。

### 2 数据版本管理、训练数据配比及质量审计
- 选：dvc（数据版本与流水线复现）、datasets（加载、流式与按概率混合）、data-juicer（算子化处理与质量分析）、dolma（标签→混合的配方化语料工具链）。
- 不选：lakeFS / git-lfs（与 DVC 同质）；NeMo-Curator（同上）。

### 3 持续预训练、指令微调、参数高效适配及偏好训练
- 选：peft（适配器实现）、trl（SFT/DPO/GRPO 训练器）、LLaMA-Factory（配置驱动端到端）、open-instruct（公开配方的后训练参考）。
- 不选：axolotl（与 LLaMA-Factory 同属配置驱动微调框架，二选一取后者，因有对应论文且中英文档俱全）；transformers 全仓（体量大，训练相关部分已由 trl/peft/accelerate 覆盖）；OLMo-core（与 torchtitan/Megatron 预训练框架同质）。

### 4 分布式训练、检查点、日志与训练故障恢复
- 选：Megatron-LM（工业级并行与分布式检查点、ft_integration）、DeepSpeed（ZeRO 与通用检查点）、torchtitan（PyTorch 原生、代码量小）、accelerate（单卡到多机的薄封装）。
- 不选：NeMo（构建在 Megatron Core 之上，同质且仓库大）；Colossal-AI（与 DeepSpeed 同质）。

### 5 语言评测、人工评测和回归测试
- 选：lm-evaluation-harness（多语种任务最全）、lighteval（多语种任务模板）、sacrebleu（MT 可复现指标）、COMET（学习型 MT 指标）、argilla（人工标注/评测平台）。
- 不选：Label Studio（与 Argilla 同质，Argilla 更贴近 LLM 数据与偏好标注）；OpenCompass（与 lm-eval-harness 同质）。

### 6 多语言检索、RAG、工具调用及智能体
- 选：sentence-transformers（向量模型训练，含多语种蒸馏）、FlagEmbedding（BGE-M3 多语种检索）、haystack（RAG/Agent 管线）、docling（文档解析与 OCR）、smolagents（工具调用与代码执行沙箱）。
- 不选：LlamaIndex（与 Haystack 同质，且单仓库集成包极多、体量大）；LangChain（同质）。

### 7 推理服务、量化、容器化、API 与流式输出
- 选：vllm、sglang（两种主流服务引擎，前缀缓存/约束解码互补）、llama.cpp（本地/边缘与 GGUF 量化）、llm-compressor（训练后量化）。
- 不选：text-generation-inference（已查 tag：最新 v3.3.7 提交日期 2025-12-18，HF 已转入维护模式，功能与 vLLM/SGLang 同质，改选 SGLang）；AutoAWQ（官方已归档，功能由 llm-compressor 接替）。

### 8 对话产品、编程工具、IDE 扩展及执行隔离
- 选：open-webui（自托管对话产品）、continue（IDE 扩展）、OpenHands software-agent-sdk（智能体与 Docker/远程沙箱执行隔离）、aider（终端编程助手）。
- 不选：e2b（沙箱即服务，核心基础设施不在开源 SDK 仓库内，且执行隔离已由 OpenHands 工作区与 smolagents 远程执行器覆盖）；gVisor（文档在 gvisor 主仓库内，仓库体量很大，非 LLM 专用，未收）。

### 9 运行监控、成本统计、灰度发布和回滚
- 选：prometheus（指标与告警）、opentelemetry-python（追踪/指标标准层）、langfuse（LLM 追踪、成本与评测）、argo-rollouts（金丝雀/蓝绿与自动回滚）。
- 不选：Flagger（与 Argo Rollouts 同质）；Kubernetes website（体量过大，且非 LLM 专用）；opentelemetry.io 站点仓库（体量大，仅收 Python SDK 仓库内 docs）。

## 下载结果
见 `progress_19_cn.md` 与 `engineering_notes_cn.md`。

## 下载结果摘要（2026-10-29）
- `engineering_en.py fetch` 一次跑完：39 个项目全部 verified，0 失败；脚本判定完整文档集 13 个（tokenizers、datasets、peft、trl、LLaMA-Factory、DeepSpeed、accelerate、lighteval、smolagents、sglang、continue、opentelemetry-python、argo-rollouts）。
- 磁盘占用：reference_code 3.14 GB + engineering_docs 0.39 GB，合计约 3.53 GB（含 39 个源码原始归档、4 个独立文档仓库原始归档、加后缀副本）。
- 关联论文：本库 claims 中已可查到 FineWeb2（04-001）与 Dolma（04-015），种子已改写为 sid；其余 30 个仍以“标题 (arXiv:ID)”记录，待论文代理完成后可再映射。
- 文档集未计完整的原因（逐项见 engineering_notes_cn.md）：仓库无目录文件；目录在构建时生成；或脚本不支持该目录格式/解析有误。

## 发现的脚本问题（未修改 .py，仅记录）
1. toc_check 的 Sphinx 正则 `(?:\.\. toctree::|```\{toctree\})(.*?)(?:\n\S|```)`：
   - MyST ```{toctree}``` 块中选项行（`:maxdepth:`）不缩进，块在第一行即结束 → Megatron-LM 解析到 0 条；
   - toctree 位于文件末尾、后面没有非缩进行时不匹配 → data-juicer 未识别；
   - 结束匹配 `\n\S` 会吞掉下一个 `.. toctree::` 的首字符，连续两个 toctree 只解析第一个 → opentelemetry-python 只得 2 条（但仍被判完整；人工复核 21/21）；
   - Sphinx 特殊条目 `self` 被当作文件 → FlagEmbedding 解析率 0.909。
2. 文档字符串称支持 “docusaurus sidebars”，代码中并无 sidebars.js/ts 解析（haystack、open-webui/docs）；也不支持 `mkdocs.yaml` 扩展名与 awesome-nav 的 `.nav.yml`（vllm、llm-compressor）、dvc.org 的 sidebar.json、Next.js 的 meta.json（langfuse-docs）、Jekyll `_data` 导航（DeepSpeed、aider）。
3. 目录类型优先级：Sphinx 早于 docs.json，OpenHands/docs 根目录有 docs.json，却因 scripts/sphinx/source 下的零散 toctree 得 0.0（人工按 docs.json 规则约 0.994）。
4. 只看到 code-docs 子目录 toctree 就判 DeepSpeed 文档完整，Jekyll 教程部分实际未经目录核对。
5. detect_license 按正则顺序首个命中：Megatron-LM（BSD-3 主条款 + 附 Apache 文本）报 Apache-2.0；Open WebUI License（BSD-3 + 品牌条款）报 BSD-3-Clause；langfuse 的 ee/ 商业许可部分未体现。
6. 独立文档仓库只过滤、不检查 400 MB 上限（MAX_TREE_BYTES 只作用于主仓库）；本轮未超限。
