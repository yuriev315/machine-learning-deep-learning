# 检索日志：12 检索增强与本地知识（rag_local_knowledge）

- 检索日期：2026-10-29
- 检索工具：`python3 -I scripts/papers_en.py search`（arXiv export API）+ 已有知识（经 `resolve` 核对 ID 与标题）
- 近三年窗口：首次公开 ≥ 2023-10-29；查询统一加 `submittedDate:[202310290000 TO 202610290000]`（下记 `$D`）

## 1. 查询式（原样）与返回

| # | 查询式 | 排序 | 返回 | 选入（种子 sid） |
|---|---|---|---|---|
| Q1 | `(abs:"retrieval-augmented" OR abs:RAG) AND (abs:multilingual OR abs:"cross-lingual" OR abs:"low-resource") AND $D` | relevance | 50 | 12-034 BordIRlines、12-036 多语言 RAG 策略、12-040 孟加拉语跨语言 ICL、12-042 CroSearch-R1、12-043 XProvence、12-035 XRAG、12-045 mRAKL、12-039 阿-英检索偏差、12-030 Not All Languages、12-038 语言漂移、12-037 上下文利用一致性、12-031 语言偏好、12-044 翻译质量标注；备选 12-069 孟加拉语农业 RAG、12-070 M4-RAG、12-077 孟加拉语医学 RAG |
| Q2 | `(abs:"embedding model" OR abs:"text embeddings") AND abs:multilingual AND $D` | relevance | 40 | 12-004 mE5、12-007 jina-v3、12-009 Gemini Embedding、12-010 Qwen3 Embedding、12-011 EmbeddingGemma、12-012 Llama-Embed-Nemotron、12-013 LUSIFER、12-014 MMTEB、12-018 Nomic MoE 嵌入、12-008 Arctic-Embed 2.0；备选 12-066 Swan/ArabicMTEB、12-067 KinyaEmbed、12-076 历史卢森堡语。单语言 MTEB（ruMTEB、PL-MTEB、FaMTEB、MTEB-French 等）未选入主列表，避免以单一中高资源语言基准凑数 |
| Q3 | `(abs:"cross-lingual retrieval" OR abs:"cross-language retrieval" OR abs:reranking) AND (abs:"low-resource" OR abs:African OR abs:multilingual) AND $D` | relevance | 40 | 12-021 低资源语言 LLM 重排序、12-019 阿姆哈拉语检索嵌入、12-025 NeuCLIRBench、12-026 CLIR 综述、12-046 跨语言 ODQA 预训练、12-060 AfrIFact；备选 12-068 列表式重排 |
| Q4 | `(abs:OCR OR abs:"document parsing") AND (abs:"low-resource" OR abs:multilingual) AND $D` | relevance | 30 | 12-050 PaddleOCR 3.0、12-051 MDPBench、12-052 多语言 OCR 噪声问答、12-053 RoundTripOCR；备选 12-071 DocAtlas |
| Q5 | `abs:"knowledge editing" AND (abs:multilingual OR abs:"cross-lingual") AND $D` | relevance | 17 | 12-054 检索增强多语言知识编辑、12-055 BMIKE-53、12-056 MLaKE、12-057 多语言知识编辑综述、12-058 Edit Once Update Everywhere |
| Q6 | `(abs:"fact verification" OR abs:"fact-checking" OR abs:citation OR abs:attribution OR abs:hallucination) AND (abs:multilingual OR abs:"low-resource") AND abs:retrieval AND $D` | relevance | 30 | 12-059 SemEval-2025 Task 7、12-063 多语言核查检索偏差；备选 12-075 答案归因 |
| Q7 | `(abs:"question answering") AND abs:"low-resource" AND (abs:retrieval OR abs:"knowledge base") AND $D` | relevance | 30 | 12-024 低资源跨语言 DPR 局限、12-065 PUGG 波兰语 KBQA；备选 12-074 印尼语自适应 RAG |
| Q8 | `abs:"information retrieval" AND abs:African AND $D` | relevance | 3 | 与 Q3 重合（AfrIFact、低资源 LLM 重排序） |
| Q9 | `abs:"SWIM-IR"` / `ti:"Synthetic" AND ti:"Multilingual" AND ti:"Retrieval" AND au:Thakur` | relevance | 0 / 1 | 用于纠正 12-023 标题（resolve 首次 UNRESOLVED，按 arXiv 实际标题改正） |

由已有知识列入并经 `resolve` 核对：RAG 原论文、MIRACL、Self-RAG（经典补充 3 篇，均写 `old_reason`）、BGE-M3、mGTE、Jina-ColBERT-v2、ColBERT-XM、E5-mistral、Translate-Distill、SWIM-IR、NoMIRACL、Chirkova 多语言 RAG、MIRAGE-Bench、MEMERAG、Faux Polyglot、Pleias-RAG、OCR Hinders RAG、Mu-SHROOM、Poly-FEVER、RAG 综述、Docling、ColPali。

## 2. 选入 / 排除原则
- “直接相关”：多语言/跨语言/低资源语言的嵌入、检索、重排、RAG、文档解析、知识编辑、事实核验。“通用支撑”（RAG 原论文、Self-RAG、E5-mistral、OCR Hinders RAG、PaddleOCR、RAG 综述）写清用途。
- 排除：音乐/代码/多模态字幕等非文本检索（CLaMP 3、跨语言代码 RAG，归 14 或不相关）；纯应用场景 RAG（农业、医学、法律 RAG 放备选或交给 13）；单一共享任务参赛系统报告（SemEval/CheckThat! 队伍论文，证据薄弱）；纯情感分析等。
- 与别类重叠：olmOCR 已由 05（05-016）认领 → 本类 `cross_only`（12-049）。

## 3. 替代关系与下载结果（下载后补记）
- `resolve 12`：首次 12-023 UNRESOLVED（种子标题与 arXiv 实际标题不符，sim 0.70），按 Q9 查到 2311.05800 实际标题 “Leveraging LLMs for Synthesizing Training Data Across Many Languages in Multilingual Dense Retrieval”，改正种子标题后解析成功；其余 0 处纠正。
- 第一轮 `download 12 --target 55`：核验到 12-057 达 55 篇；12-053 RoundTripOCR 被判 duplicate_elsewhere（05 类 05-069 已认领）→ 本类改为 `cross_only`，不计数。
- 第二轮 `download 12 --target 63`：补齐主列表剩余 8 篇（12-058 X-KDE、12-059 SemEval-2025 Task 7、12-060 AfrIFact、12-061 Mu-SHROOM、12-062 Poly-FEVER、12-063 核查检索偏差、12-064 RAG 综述、12-065 PUGG），以覆盖“引用与事实核验”“低资源知识库问答”子方向；12 篇备选未下载。
- 已有复用：12-003 Self-RAG、12-015 E5-mistral、12-064 RAG 综述（复制自 /root/large_model_multimodal_literature 并重新核验）。
- 下载失败 0；待核验 0。
- 最终：已核验 63，近三年 60/63 = 95.2%，三年前 3 篇（均有 old_reason）；直接相关 57 / 通用支撑 6。

## 4. 未完成与缺口
- 文档解析/OCR：olmOCR（05）、RoundTripOCR（05）已被 05 类认领，本类仅作交叉标签；低资源文字 OCR 端到端评测仍偏少。
- 低资源语言知识库问答（KBQA）原生数据集较少，仅 PUGG（波兰语）入主列表；HybridRAG-BN（孟加拉语）等 2026 新作未收录。
- CIRAL（非洲语言 CLIR 测试集）未找到 arXiv 版本，未收录；可后续用 ACL Anthology/SIGIR 合法 PDF 补充。
- 知识更新方面以知识编辑为主，缺少“小语种知识库增量更新/时效性”专门研究。
