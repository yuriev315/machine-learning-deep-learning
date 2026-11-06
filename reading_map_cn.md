# 阅读路线与各类优先阅读资料

编号对应 [catalog_cn.csv](catalog_cn.csv)：MLP = 论文，MLU = 大学课程讲义，MLB = 书籍。各编号的文件路径见目录表或 [domains/](domains/) 下的分类页。论文的简介只依据摘要；"下载核验通过"不等于已经精读全文。

## 一、从数学基础到机器学习、再到深度学习的路线

| 阶段 | 目标 | 主读 | 辅读/查阅 |
|---|---|---|---|
| 0 数学基础 | 线性代数、微积分、概率、优化 | MLB012 Boyd & Vandenberghe《Introduction to Applied Linear Algebra》→ MLB010 Deisenroth 等《Mathematics for Machine Learning》 | 概率：MLB022 Grinstead & Snell，MLU036 MIT 18.05，MLU039 Berkeley CS70；矩阵求导：MLU031 MIT 矩阵微积分讲义，MLB039 Matrix Cookbook；线性代数理论：MLB034 Axler |
| 1 优化与信息论 | 凸优化、一阶方法、信息论基础 | MLB011 Boyd《Convex Optimization》前 5 章；MLU033 EPFL Optimization for ML 讲义 | MLB028 Kochenderfer《Algorithms for Optimization》；MLU032 Berkeley EECS127 讲义；MLB014 MacKay |
| 2 机器学习入门 | 监督学习、模型评估与选择、经典方法 | MLU001 Stanford CS229 讲义 + MLB002 ISLP（Python） | MLB006 Murphy PML1；MLB018 Hardt & Recht《Patterns, Predictions, and Actions》 |
| 3 机器学习进阶 | 统计学习、概率模型、核方法、树与集成 | MLB001 ESL；MLB005 Bishop PRML | MLB033 GPML（高斯过程）；MLB003 稀疏统计学习；MLU007 Cambridge Mathematics of ML |
| 4 学习理论 | 泛化、PAC、复杂度、高维概率 | MLB015 Shalev-Shwartz & Ben-David → MLB017 Bach《Learning Theory from First Principles》 | MLU009 Stanford STATS214 讲义；MLB016 Mohri；MLB021 Vershynin；C01 论文（双下降、良性过拟合、标度律） |
| 5 深度学习基础 | 网络、反向传播、优化、正则化、架构 | MLB008 Prince《Understanding Deep Learning》（主线）+ MLB009 D2L（代码实践） | MLB055 Goodfellow 等《Deep Learning》；MLB031 Fleuret 小书；MLU018 Penn ESE546；C04 论文 |
| 6 深度学习理论（可选） | 初始化、宽度极限、逼近与优化理论 | MLB050 Petersen & Zech 或 MLB048 Jentzen 等 | MLB044 Roberts 等《Principles of DL Theory》；MLU017 Telgarsky 讲义 |
| 7 方向深入 | 视觉 / 语言 / 生成 / 图 / 强化学习 / 可靠性 | CV：MLB058 Torralba 等；NLP：MLB030 SLP3 → MLB049 Xiao & Zhu；生成：C07 的 MLP0363、MLP0334 + MLU022 MIT 6.S184；图：MLB020 Hamilton → MLB045 GDL；RL：MLB013 Sutton & Barto → MLB041 Bertsekas；可靠性：MLB019 fairmlbook、MLB057 Molnar、MLP0540 共形预测入门 | 各类"优先阅读 10 份"（见下），再按 catalog 中"优先级=高"扩展 |

建议节奏：阶段 0–2 打基础后，阶段 3–5 可并行；进入阶段 7 时先读该方向的综述/教程，再读近三年原始论文。

## 二、各类优先阅读的 10 份资料

### C01 机器学习基础
1. MLP0055 Understanding deep learning requires rethinking generalization —— 现代泛化讨论的起点（经典）。
2. MLP0054 Reconciling modern ML practice and the bias-variance trade-off —— 双下降原始论文（经典）。
3. MLP0023 Understanding the Double Descent Phenomenon in Deep Learning —— 入门教程，衔接前两篇。
4. MLP0004 Classical Statistical (In-Sample) Intuitions Don't Generalize Well —— 澄清偏差-方差直觉的适用条件。
5. MLP0002 Deep Learning is Not So Mysterious or Different —— 用 PAC-Bayes/软归纳偏置统一解释"反常"现象。
6. MLP0001 Rethinking Conventional Wisdom in ML: From Generalization to Scaling —— 从泛化范式到标度范式。
7. MLP0053 Cross-validation: what does it estimate and how well does it do it? —— 模型选择必读（经典）。
8. MLP0042 Hyperparameter Optimization in Machine Learning —— 超参数优化与模型选择综述。
9. MLP0005 Non-Vacuous Generalization Bounds for Large Language Models —— 学习理论在 LLM 上的落地。
10. MLP0019 Resolving Discrepancies in Compute-Optimal Scaling of Language Models —— 标度律实证细节。

### C02 传统机器学习
1. MLP0100 XGBoost —— 梯度提升标准实现（经典）。
2. MLP0102 Why do tree-based models still outperform deep learning on tabular data? —— 表格学习讨论起点（经典）。
3. MLP0066 Why do Random Forests Work? —— 随机森林作为自适应平滑器。
4. MLP0103 A Unified Theory of Diversity in Ensemble Learning —— 集成多样性理论（经典）。
5. MLP0060 A Closer Look at Deep Learning Methods on Tabular Datasets —— 大规模对比树模型与深度方法。
6. MLP0059 Better by Default —— GBDT/MLP 强默认超参数。
7. MLP0219 TabArena —— 持续维护的表格基准。
8. MLP0057 TabPFN v2（Nature）—— 表格基础模型。
9. MLP0058 TabM —— 参数高效集成的表格深度模型。
10. MLP0085 A Survey on Deep Tabular Learning —— 综述收尾。

### C03 无监督与表示学习
1. MLP0155 SimCLR（经典）；2. MLP0156 MAE（经典）；3. MLP0158 CLIP（经典）—— 三类主流自监督范式。
4. MLP0157 DINOv2 → 5. MLP0105 DINOv3 —— 视觉自监督主线的最新进展。
6. MLP0107 V-JEPA —— 潜空间预测式视频自监督。
7. MLP0112 The Platonic Representation Hypothesis —— 表示趋同的整体视角。
8. MLP0142 Battle of the Backbones —— 表征评估的大规模比较。
9. MLP0115 A Survey on Deep Clustering —— 聚类综述。
10. MLP0159 UMAP —— 降维与可视化（经典）。

### C04 深度学习基础与训练
1. MLP0216 Attention Is All You Need（经典）；2. MLP0215 ResNet（经典）；3. MLP0214 Adam（经典）。
4. MLP0217 BatchNorm（经典）；5. MLP0218 μP（经典）—— 归一化与超参数迁移基础。
6. MLP0172 Old Optimizer, New Norm —— 统一理解 Adam/Shampoo/Muon 的教程。
7. MLP0176 Deconstructing What Makes a Good Optimizer for Language Models —— 优化器实证比较。
8. MLP0160 Mamba —— Transformer 之外的主要序列架构。
9. MLP0191 DeepSeekMoE —— MoE 架构设计。
10. MLP0206 Efficient Large Language Models: A Survey —— 训练/推理效率综述。

### C05 计算机视觉
1. MLP0271 ViT（经典）；2. MLP0272 Mask R-CNN（经典）；3. MLP0273 DETR（经典）；4. MLP0275 U-Net（经典）。
5. MLP0274 SAM（经典）→ 6. MLP0221 SAM 2 —— 可提示分割。
7. MLP0232 YOLOv1 to YOLOv10 综述 —— 实时检测脉络。
8. MLP0223 Depth Anything —— 单目深度基础模型。
9. MLP0225 DUSt3R —— 三维视觉新范式。
10. MLP0263 Video Understanding with LLMs: A Survey —— 视频理解综述。

### C06 自然语言处理与大语言模型
1. MLP0328 BERT（经典）；2. MLP0329 GPT-3（经典）；3. MLP0331 Chinchilla（经典）。
4. MLP0330 InstructGPT（经典）→ 5. MLP0332 DPO（经典）—— 对齐主线。
6. MLP0276 The Llama 3 Herd of Models —— 完整的预训练/后训练技术报告。
7. MLP0290 FineWeb —— 预训练数据构建。
8. MLP0300 Tulu 3 —— 完全开放的后训练配方。
9. MLP0279 DeepSeek-R1 —— 强化学习推理模型。
10. MLP0323 Chatbot Arena —— 基于人类偏好的评测。

### C07 生成模型
1. MLP0386 VAE（经典）；2. MLP0385 GAN（经典）；3. MLP0384 DDPM（经典）。
4. MLP0363 Step-by-Step Diffusion: An Elementary Tutorial —— 扩散入门教程。
5. MLP0388 Flow Matching（经典）→ 6. MLP0334 Flow Matching Guide and Code —— 流匹配理论与实现。
7. MLP0387 Latent Diffusion（经典）—— 现代文生图框架。
8. MLP0333 SD3（Rectified Flow Transformers）—— 规模化文生图。
9. MLP0336 VAR —— 自回归视觉生成。
10. MLP0377 Transfusion —— 统一多模态生成。

### C08 图机器学习
1. MLP0434 GCN（经典）；2. MLP0435 GAT（经典）；3. MLP0437 GraphSAGE（经典）。
4. MLP0438 MPNN（经典）；5. MLP0436 GIN（经典）—— 消息传递与表达力。
6. MLP0391 Classic GNNs are Strong Baselines —— 近年重新评估。
7. MLP0389 Graph Transformers: A Survey。
8. MLP0426 A Hitchhiker's Guide to Geometric GNNs —— 几何 GNN 教程。
9. MLP0411 Large Language Models on Graphs: A Comprehensive Survey。
10. MLP0423 Relational Deep Learning —— 图学习在关系数据库上的应用。

### C09 强化学习与决策
1. MLP0485 DQN（经典）；2. MLP0486 PPO（经典）；3. MLP0487 SAC（经典）。
4. MLP0439 Reinforcement Learning: An Overview（Murphy）—— 长篇综述，覆盖新旧方法。
5. MLP0488 Decision Transformer（经典）—— 序列决策视角。
6. MLP0489 DreamerV3（经典）→ 7. MLP0459 世界模型综述。
8. MLP0467 A Survey of RLHF。
9. MLP0460 Back to Basics (RLOO) —— LLM 强化学习的简化算法。
10. MLP0464 Understanding R1-Zero-Like Training —— 推理 RL 的批判性分析。

### C10 可靠性与评测
1. MLP0539 On Calibration of Modern Neural Networks（经典）。
2. MLP0540 A Gentle Introduction to Conformal Prediction（经典）→ 3. MLP0490 Theoretical Foundations of Conformal Prediction。
4. MLP0542 Deep Ensembles（经典）—— 不确定性强基线。
5. MLP0543 SHAP（经典）→ 6. MLP0509 Open Problems in Mechanistic Interpretability。
7. MLP0541 Leakage and the Reproducibility Crisis（经典）—— 数据泄漏分类。
8. MLP0551 The Clever Hans Mirage —— 伪相关与分布变化综述。
9. MLP0531 Adding Error Bars to Evals —— 评测的统计方法。
10. MLP0498 Detecting hallucinations using semantic entropy（Nature）—— LLM 不确定性。

### C11 大学课程讲义
1. MLU001 Stanford CS229（Spring 2026 讲义）—— 机器学习主干课程。
2. MLU036 MIT 18.05 —— 概率统计基础。
3. MLU033 EPFL CS-439 Optimization for ML（2025）。
4. MLU007 Cambridge Mathematics of Machine Learning —— 学习理论入门。
5. MLU009 Stanford STATS214/CS229M —— 机器学习理论。
6. MLU018 Penn ESE 546 Principles of Deep Learning（Fall 2024）。
7. MLU022 MIT 6.S184 Flow Matching and Diffusion（2026）。
8. MLU026 ETH Probabilistic Artificial Intelligence —— 贝叶斯深度学习与不确定性、强化学习。
9. MLU030 Stanford CS168（Spring 2024）—— 数据算法工具箱（PCA、SVD、随机投影等）。
10. MLU019 Stanford CS231n 讲义 —— 视觉与卷积网络入门（在线讲义无版本日期）。

### C12 教科书、专著与参考书
1. MLB010 Mathematics for Machine Learning；2. MLB002 ISLP；3. MLB001 ESL；4. MLB005 Bishop PRML。
5. MLB015 Understanding Machine Learning → 6. MLB017 Bach LTFP（学习理论新教材）。
7. MLB008 Understanding Deep Learning（2026 版 PDF）；8. MLB009 Dive into Deep Learning。
9. MLB013 Sutton & Barto 第 2 版；10. MLB006 Murphy PML1。
