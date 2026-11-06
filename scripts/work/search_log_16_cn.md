# 检索日志：16 高效训练、推理与部署（efficient_train_deploy）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API），辅以检索者已有知识（经典系统论文 ID 由 `resolve` 回查 arXiv 元数据核对标题，0 处纠正）。
- 时间窗：除经典补充外均加 `submittedDate:[202310290000 TO 202610290000]`（下文记为 `$D`）。
- 选题原则：优先“压缩/部署对多语言、低资源语言能力的影响”与“多语言 token 膨胀带来的推理成本”，标 `直接相关`；通用系统工作（分布式训练、量化方法、KV 缓存、服务调度、推测解码）标 `通用支撑` 并写明用途。

## 查询式（原样）与返回数

| # | 查询式 | 返回 | 主要选入 |
|---|---|---|---|
| 1 | `abs:quantization AND abs:multilingual AND $D` | 40 | 2407.03211, 2601.18306, 2508.20893, 2507.19699, 2503.03592, 2608.09941, 2608.11786, 2602.09130 |
| 2 | `abs:pruning AND abs:multilingual AND abs:"language models" AND $D` | 30 | 2408.14398, 2409.16911, 2505.16956, 2411.14055, 2503.06291, 2605.28042 |
| 3 | `abs:compression AND abs:"low-resource languages" AND $D` | 18 | 2404.04748, 2404.04759, 2502.18020, 2601.13328(备选) |
| 4 | `abs:"speculative decoding" AND (abs:multilingual OR abs:translation) AND $D` | 30 | 2406.16758, 2605.30580, 2604.16368 |
| 5 | `abs:distillation AND abs:multilingual AND abs:"low-resource" AND abs:LLM AND $D` | 14 | （多为 09 合成/翻译蒸馏，未选） |
| 6 | `abs:tokenization AND (abs:cost OR abs:latency OR abs:inference) AND abs:languages AND abs:disparit* AND $D` | 0 | — |
| 7 | `abs:quantized AND (abs:"low-resource" OR abs:multilingual OR abs:"non-English") AND abs:LLMs AND $D` | 30 | 2608.24615, 2603.18037(备选), 2601.12033(备选) |
| 8 | `abs:"KV cache" AND abs:multilingual AND $D` | 5 | 无（均为技术报告/无关） |
| 9 | `abs:tokenization AND abs:cost AND abs:languages AND abs:API AND $D` | 20 | 2410.10665, 2608.09046 |
| 10 | `ti:token AND (ti:tax OR ti:premium OR ti:cost OR ti:fair*) AND $D` | 25 | 2602.11174, 2609.00378（2509.05486 / 2606.24460 / 2607.24276 已在 06 种子，跳过） |
| 11 | `abs:"vocabulary" AND abs:"inference" AND abs:efficien* AND abs:"non-English" AND $D` | 0 | — |
| 12 | `abs:"low-resource languages" AND (abs:edge OR abs:"on-device" OR abs:CPU OR abs:"consumer hardware") AND abs:LLM AND $D` | 10 | 无（多为 03/04/13 主题） |
| 13 | `abs:"model compression" AND abs:multilingual AND abs:"language models" AND $D` | 9 | 2510.26271(备选) |
| 14 | `abs:QLoRA AND (abs:"low-resource language" OR abs:multilingual) AND $D` | 25 | 无（多为下游任务微调应用，属 08/13） |
| 15 | `abs:experts AND abs:pruning AND abs:multilingual AND abs:mixture AND $D` | 2 | 2605.28042 |
| 16 | `(abs:quantization OR abs:pruning OR abs:distillation) AND abs:"machine translation" AND abs:LLM AND abs:"low-resource" AND $D` | 10 | 2509.23990, 2412.05862(备选) |
| 17 | `abs:"cross-lingual vocabulary adaptation" AND abs:inference` | 0 | （2402.10712 已在 06 种子） |
| 18 | `(abs:"inference efficiency" OR abs:"inference cost" OR abs:latency OR abs:throughput) AND abs:multilingual AND abs:LLMs AND abs:languages AND $D` | 40 | 2504.10013, 2610.23249, 2606.17609(备选) |
| 19 | `(abs:"knowledge distillation" OR abs:distill*) AND abs:"multilingual" AND abs:"smaller" AND (abs:compression OR abs:"student model") AND abs:LLM AND $D` | 1 | 2407.19610 |
| 20 | `(abs:"vocabulary trimming" OR abs:"vocabulary reduction" OR abs:"layer skipping" OR abs:"early exit") AND (abs:multilingual OR abs:language-specific) AND $D` | 20 | 2311.09709, 2410.12513(备选) |
| 21 | `abs:"mixture-of-experts" AND (abs:pruning OR abs:offloading OR abs:"expert pruning") AND abs:language AND abs:multilingual AND $D` | 2 | — |
| 22 | `(abs:affordable OR abs:"limited compute" OR abs:"single GPU" OR abs:"consumer GPU") AND abs:"low-resource language" AND abs:LLM AND $D` | 4 | 无（UnifiedCrawl 属 04；Paramanu/LilMoo 属 03） |
| 23 | `(ti:quantization OR ti:quantized OR ti:compression OR ti:compressed OR ti:pruning OR ti:pruned OR ti:distillation) AND (ti:multilingual OR ti:languages OR ti:"low-resource" OR ti:cross-lingual OR ti:translation) AND $D` | 50 | 2603.11881, 2610.21383, 2411.06506, 2409.14162, 2507.21568, 2407.14679(通用), 2410.17170/2501.00733(备选) |

## 通用支撑（凭知识选入，resolve 核对）
Medusa 2401.10774、EAGLE 2401.15077、SGLang 2312.07104、DistServe 2401.09670、Sarathi-Serve 2403.02310、KIVI 2402.02750、QuaRot 2404.00456、SpinQuant 2405.16406、BitNet b1.58 2402.17764、FlashAttention-3 2407.08608、TorchTitan 2410.06511、MegaScale 2402.15627、GaLore 2403.03507、Minitron 2407.14679、Evaluating Quantized LLMs 2402.18158、“Give Me BF16” 2411.02355、校准数据影响 2311.09755、高效推理综述 2404.14294；备选 QuIP#、AQLM、量化与推理模型、ShortGPT、高效 LLM 综述等。

## 经典补充（≤5，均写 old_reason）
ZeRO 1910.02054、Megatron-LM 3D 并行 2104.04473、PagedAttention/vLLM 2309.06180、GPTQ 2210.17323、AWQ 2306.00978。QLoRA 2305.14314 已在 08 种子，未重复选入；FSDP 论文（2023-04）因经典名额已满未选，以窗口内 TorchTitan（FSDP2）替代。

## 排除与替代
- 与他类种子重复而跳过：2509.05486 The Token Tax（06）、2606.24460 African Language Tax（06）、2607.24276 Tokenizer Tax（06）、2402.10712 词表适配推理效率（06）、2305.14314 QLoRA（08）、2501.02631 爱沙尼亚语词表裁剪（06 备选）。
- 排除：2410.14766（“低资源语言”指编程语言 Lua，非自然语言）；语音压缩 2405.00966、2505.20237（语音模态，非本库重点）；各类以 QLoRA 做单一下游任务的应用论文（属 08/13）。

## 结果与未完成原因
- 种子 77 条（主列表 58、备选 19）；resolve 77 条全部按 ID 命中，0 处纠正。
- 下载前调整：读摘要后发现 2601.12033（量化对多语言公平/安全）、2606.17609（多语言 QA 剪枝评测陷阱）、2604.16235（韩语 token 剪枝）为直接相关，提升为主列表；FlashAttention-3、MegaScale、Evaluating Quantized LLMs 降为备选；2407.19610 涉及语言均为高资源，改标通用支撑。为让提升的 3 条和经典补充都被处理，本类用 `download 16 --target 58`（略高于建议的 55）。
- 结果：已核验 58、待核验 0、失败 0；其中 16 篇为兄弟库已核验 PDF 复制后重新核验（已有复用），42 篇本轮下载。近三年 53/58 = 91.4%；经典 5 篇（ZeRO、Megatron-LM 3D 并行、PagedAttention、GPTQ、AWQ）均写 old_reason，已到上限。
- 相关性：直接相关 37 / 通用支撑 21（64%）。
- 缺口：KV 缓存、服务调度、分布式训练方面缺少多语言专门研究，只能用通用系统论文支撑；“多语言 token 膨胀带来的推理成本”的核心论文 The Token Tax（2509.05486）和 African Language Tax（2606.24460）已由 06 类认领，本类收录的是同主题的其他成本/延迟审计论文。
- 注释：58 篇全部写入 `scripts/annotations/16_efficient_train_deploy_annot_cn.json`；资源与实验数值一律写成“作者称/依其硬件”，不作泛化；top 10 中 16-001/003/009/011/020 另用 `text` 核对正文前 2–3 页。
