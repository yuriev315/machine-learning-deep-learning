# 检索日志：06 分词、词表与模型架构（tokenization_vocab_arch）

- 检索日期：2026-10-29
- 工具：`python3 -I scripts/papers_en.py search '<查询>' --max N --sort relevance`（arXiv export API）；结合已有知识列出候选，`resolve` 核对（88 条中 0 处 ID 纠错；06-028 标题按 arXiv 实际标题改为 *Adapting Chat Language Models Using Only Target Unlabeled Language Data*）。
- 近三年窗口：首次公开 ≥ 2023-10-29（下表 `<D>` = `submittedDate:[202310290000 TO 202610290000]`）。

## 1. 查询式与返回数（原样）

| # | 查询式 | max | 返回 | 主要选入 |
|---|---|---|---|---|
| 1 | `(ti:Tokenization OR ti:tokenizer OR ti:tokenizers) AND (abs:multilingual OR abs:languages) AND <D>` | 50 | 50 | Token Tax（2509.05486）、One Tokenizer To Rule Them All、MUTANT、Parallel Tokenizers、Modular Tokenizers、Indian Tokenizer Tax（2607.24276）、Tokenization & Morphology mT5/ByT5、Swahili 音节分词、Equity with Efficiency、Accelerating…Excessively Tokenized、MAGNET；备选：Qtok、土耳其混合分词、Beyond Literal Token Overlap、Art of Breaking Words、印度语言分词综述 |
| 2 | `abs:"vocabulary expansion" OR abs:"vocabulary extension" OR abs:"vocabulary adaptation" AND <D>` | 40 | 40 | 0.01GB 词表扩展、VocADT、俄语 LEP（备选）、意大利语（未选）、Exploring Design Choices、渐进式词表扩展（阿拉伯语）、爱沙尼亚语词表裁剪（备选）、嵌入初始化策略比较（备选）、俄语分词影响、吉兹文词表扩展、定制分词器（备选）、像素回退 |
| 3 | `(abs:"embedding initialization" OR abs:"tokenizer transfer" OR abs:"cross-lingual vocabulary") AND <D>` | 30 | 30 | Model-Aware Tokenizer Transfer（备选）、词典驱动词表迁移、Trans-Tokenization、ANGOFA、HYPEROFA（备选）、LGSE（备选）、Bilingual Adaptation of Monolingual FM、UniBridge（未选） |
| 4 | `(ti:byte OR ti:"token-free" OR ti:"tokenizer-free" OR ti:character-level) AND abs:"language model" AND <D>` | 40 | 40 | MambaByte、T-FREE（备选）、H-Net++、Toucan（备选）、BanglaByT5、Bit-level BPE、Measuring Cross-lingual Transfer in Bytes |
| 5 | `(abs:"mixture of experts" OR abs:"mixture-of-experts") AND abs:multilingual AND abs:"language-specific" AND <D>` | 30 | 11 | Group then Scale、Multilingual Routing in MoE、MoE 多语言机制（备选） |
| 6 | `(abs:romanization OR abs:transliteration OR abs:script) AND abs:"non-Latin" AND abs:"language model" AND <D>` | 30 | 30 | 转写与 ICL、One Script Instead of Hundreds（备选）、可逆转写（Huffman）、BPE Stays on SCRIPT（备选）、Multilingual Pixel LM、Tokenization Disparities as Infrastructure Bias（备选）、字节分块零样本迁移（备选）、尼泊尔语分词（备选） |
| 7 | `(ti:Uyghur OR ti:Mongolian OR …)` 等 03 的语种检索中顺带发现 | — | — | KazByte（2603.27859，哈萨克语字节适配器）、尼泊尔语形态预分词（2609.33395，未选） |
| 8 | `abs:"Southeast Asian" AND abs:"language model" AND <D>`（03 检索） | 30 | 30 | Equity with Efficiency（2606.15044） |
| 9 | `abs:"African languages" AND abs:"language model" AND <D>`（03 检索） | 30 | 30 | The African Language Tax（2606.24460） |

已有知识补充（resolve 核对一致）：Parity-aware BPE、MYTE、Splintering、MorphScore 两篇、Tokenization Is More Than Compression、EEVE、Efficiently Adapting Pretrained LMs to New Languages、Cross-lingual Vocabulary Adaptation 实证、ElChat、ZeTT、OFA、Large Vocabulary Size、Scaling Laws with Vocabulary、DictaLM 2.0、TokAlign、BLT、SpaceByte、MrT5、HAT、H-Net、RomanSetu、TransliCo、Breaking the Script Barrier、LangSAMP、MoE-LPR、DEPT，以及经典 Petrov 等（2305.15425）、Ahia 等（2305.13707）、FOCUS、WECHSEL、ByT5。

## 2. 选入与排除原则
- 选入：分词效率/token 税/分词公平；形态与文字对分词和建模的影响；词表扩展、替换与嵌入初始化；分词器迁移；字节/字符/像素级无分词方法；转写/罗马化与文字障碍；多语言 MoE 与语言/文字特定模块。
- `通用支撑`：只在英语上验证但对小语种分词/架构选择有直接借鉴者（Tokenization Is More Than Compression、Scaling Laws with Vocabulary、MambaByte、BLT、SpaceByte、HAT、H-Net、T-FREE、DEPT、Large Vocabulary Size、Toucan），注释中写明用途。
- 排除：领域词表适配（医疗、化学，与小语种无关）；语音/视觉 tokenizer；跨分词器蒸馏（2503.20083，偏 09）；意大利语词表适配（2504.17025，高资源，未选）。

## 3. 认领冲突与替代
- 被其他类先认领（均改为 `cross_only` 并写 cross_reason，由主列表后续条目补足）：06-025 *Efficiently Adapting Pretrained Language Models To New Languages*（07-005）、06-028 *Adapting Chat Language Models Using Only Target Unlabeled Language Data*（07-066）、06-029 *Exploring Design Choices for Building Language-Specific LLMs*（07-056）、06-040 *Bilingual Adaptation of Monolingual Foundation Models*（07-029）、06-071 *MoE-LPR*（07-044）、06-066 *Exploring the Role of Transliteration in ICL for LRL in Non-Latin Scripts*（08-032）。
- 06-079 ByT5（经典）改为 reserve，未下载，以把三年前文献控制在 4 篇。

## 4. 下载与核验
- `download 06 --target 55` → 55 已核验；随后 `--target 57` 补下经典 FOCUS、WECHSEL（嵌入初始化方法的标准基线）。
- 已有复用（从兄弟库复制并重新核验）4 篇：06-013、06-047、06-051、06-055。
- 无 pending、无失败，未使用 `manual`。
- 最终：已核验 57；待核验 0；失败 0；近三年 53/57 = 93.0%；经典 4 篇（Petrov 等 2305.15425、Ahia 等 2305.13707、FOCUS、WECHSEL，均写 old_reason）。
- 疑点：06-063 KazByte 为“技术公告”，作者称实证验证仍在进行、无实验结果，仅可作设计参考；06-043 吉兹文词表扩展的 arXiv v4 注释称替换了 v1/v2 中无法追溯到实验输出的全部结果，结论与早期版本不同，引用须以 v4 为准。

## 5. 未完成/缺口
- 维吾尔文、蒙古文、藏文等中国少数民族文字的专门分词研究：仅 2509.17493（可逆转写）间接涉及；缺专门藏文/蒙古文分词论文。
- 美洲原住民语言分词研究缺失。
