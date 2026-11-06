# Brief for annotation: 01 数学与学习基础

## 01-003 | ShapleyLaw: A Game-Theoretic Approach to Multilingual Scaling Laws
- arXiv: 2603.17945  first public: 2026-03-18  latest: 2026-09-19  primary cat: cs.CL
- authors (10): Xuyang Cao; Qianying Liu; Chuan Xiao; Yusuke Oda; Jiayi Wang; Pontus Stenetorp ...
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: Accepted at EMNLP 2026 Main Conference. Camera-ready version; revised based on reviewer feedback
- pages: 22

ABSTRACT: In multilingual pretraining, the test loss of a pretrained model is heavily influenced by the proportion of each language in the pretraining data, namely the \textit{language mixture ratios}. Multilingual scaling laws can predict the test loss under different language mixture ratios and can therefore be used to estimate the optimal ratios. However, the current approaches to multilingual scaling laws do not measure the \textit{cross-lingual transfer} effect, resulting in suboptimal mixture ratios. In this paper, we consider multilingual pretraining as a cooperative game in which each language acts as a player that jointly contributes to pretraining, gaining the resulting reduction in test loss as the payoff. Consequently, from the perspective of cooperative game theory, we quantify the cross-lingual transfer from each language by its contribution in the game, and propose a game-theoretic multilingual scaling law called \textit{ShapleyLaw}. Our experiments show that ShapleyLaw outperforms baseline methods in model performance prediction and language mixture optimization.

## 01-004 | Scaling Laws of Decoder-Only Models on the Multilingual Machine Translation Task
- arXiv: 2409.15051  first public: 2024-09-23  latest: 2024-09-23  primary cat: cs.CL
- authors (5): Gaëtan Caillaut; Raheel Qader; Mariam Nakhlé; Jingshu Liu; Jean-Gabriel Barthélemy
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Recent studies have showcased remarkable capabilities of decoder-only models in many NLP tasks, including translation. Yet, the machine translation field has been largely dominated by encoder-decoder models based on the Transformer architecture. As a consequence, scaling laws of encoder-decoder models for neural machine translation have already been well studied, but decoder-only models have received less attention. This work explores the scaling laws of decoder-only models on the multilingual and multidomain translation task. We trained a collection of six decoder-only models, ranging from 70M to 7B parameters, on a sentence-level, multilingual and multidomain dataset. We conducted a series of experiments showing that the loss of decoder-only models can be estimated using a scaling law similar to the one discovered for large language models, but we also show that this scaling law has difficulties to generalize to too large models or to a different data distribution. We also study different scaling methods and show that scaling the depth and the width of a model lead to similar test loss improvements, but with different impact on the model's efficiency.

## 01-005 | Scaling Laws for Downstream Task Performance of Large Language Models
- arXiv: 2402.04177  first public: 2024-02-06  latest: 2026-01-29  primary cat: cs.CL
- authors (6): Berivan Isik; Natalia Ponomareva; Hussein Hazimeh; Dimitris Paparas; Sergei Vassilvitskii; Sanmi Koyejo
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: Published at the International Conference on Learning Representations (ICLR) 2025, with title: "Scaling Laws for Downstream Task Performance in Machine Translation"
- pages: 22

ABSTRACT: Scaling laws provide important insights that can guide the design of large language models (LLMs). Existing work has primarily focused on studying scaling laws for pretraining (upstream) loss. However, in transfer learning settings, in which LLMs are pretrained on an unsupervised dataset and then finetuned on a downstream task, we often also care about the downstream performance. In this work, we study the scaling behavior in a transfer learning setting, where LLMs are finetuned for machine translation tasks. Specifically, we investigate how the choice of the pretraining data and its size affect downstream performance (translation quality) as judged by: downstream cross-entropy and translation quality metrics such as BLEU and COMET scores. Our experiments indicate that the size of the finetuning dataset and the distribution alignment between the pretraining and downstream data significantly influence the scaling behavior. With sufficient alignment, both downstream cross-entropy and translation quality scores improve monotonically with more pretraining data. In such cases, we show that it is possible to predict the downstream translation quality metrics with good accuracy using a log-law. However, there are cases where moderate misalignment causes the downstream translation scores to fluctuate or get worse with more pretraining, whereas downstream cross-entropy monotonically improves. By analyzing these, we provide new practical insights for choosing appropriate pretraining data.

## 01-007 | Scaling Laws for Mixture Pretraining Under Data Constraints
- arXiv: 2605.12715  first public: 2026-05-12  latest: 2026-05-15  primary cat: cs.LG
- authors (4): Anastasiia Sedova; Skyler Seto; Natalie Schluter; Pierre Ablin
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- pages: 33

ABSTRACT: As language models scale, the amount of data they require grows -- yet many target data sources, such as low-resource languages or specialized domains, are inherently limited in size. A common strategy is to mix this scarce but valuable target data with abundant generic data, which presents a fundamental trade-off: too little target data in the mixture underexposes the model to the target domain, while too much target data repeats the same examples excessively, yielding diminishing returns and eventual overfitting. We study this trade-off across more than 2,000 language-model training runs spanning multiple model and target dataset sizes, as well as several data types, including multilingual, domain-specific, and quality-filtered mixtures. Across all settings, we find that repetition is a central driver of target-domain performance, and that mixture training tolerates much higher repetition than single-source training: scarce target corpora can be reused 15-20 times, with the optimal number of repetitions depending on the target data size, compute budget, and model scale. Next, we introduce a repetition-aware mixture scaling law that accounts for the decreasing value of repeated target tokens and the regularizing role of generic data. Optimizing the scaling law provides a principled way to compute effective mixture configurations, yielding practical mixture recommendations for pretraining under data constraints.

## 01-008 | Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
- arXiv: 2403.16952  first public: 2024-03-25  latest: 2025-03-20  primary cat: cs.CL
- authors (6): Jiasheng Ye; Peiju Liu; Tianxiang Sun; Jun Zhan; Yunhua Zhou; Xipeng Qiu
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: accepted by ICLR2025, camera ready version
- URLs on first pages of PDF: https://github.com/yegcjs/mixinglaws
- pages: 27

ABSTRACT: Pretraining data of large language models composes multiple domains (e.g., web texts, academic papers, codes), whose mixture proportions crucially impact the competence of outcome models. While existing endeavors rely on heuristics or qualitative strategies to tune the proportions, we discover the quantitative predictability of model performance regarding the mixture proportions in function forms, which we refer to as the data mixing laws. Fitting such functions on sample mixtures unveils model performance on unseen mixtures before actual runs, thus guiding the selection of an ideal data mixture. Furthermore, we propose nested use of the scaling laws of training steps, model sizes, and our data mixing law to enable predicting the performance of large models trained on massive data under various mixtures with only small-scale training. Moreover, experimental results verify that our method effectively optimizes the training mixture of a 1B model trained for 100B tokens in RedPajama, reaching a performance comparable to the one trained for 48% more steps on the default mixture. Extending the application of data mixing laws to continual training accurately predicts the critical mixture proportion that avoids catastrophic forgetting and outlooks the potential for dynamic data schedules

## 01-009 | Language models scale reliably with over-training and on downstream tasks
- arXiv: 2403.08540  first public: 2024-03-13  latest: 2024-06-14  primary cat: cs.CL
- authors (25): Samir Yitzhak Gadre; Georgios Smyrnis; Vaishaal Shankar; Suchin Gururangan; Mitchell Wortsman; Rulin Shao ...
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/mlfoundations/scaling
- pages: 43

ABSTRACT: Scaling laws are useful guides for derisking expensive training runs, as they predict performance of large models using cheaper, small-scale experiments. However, there remain gaps between current scaling studies and how language models are ultimately trained and evaluated. For instance, scaling is usually studied in the compute-optimal training regime (i.e., "Chinchilla optimal" regime). In contrast, models are often over-trained to reduce inference costs. Moreover, scaling laws mostly predict loss on next-token prediction, but models are usually compared on downstream task performance. To address both shortcomings, we create a testbed of 104 models with 0.011B to 6.9B parameters trained with various numbers of tokens on three data distributions. First, we fit scaling laws that extrapolate in both the amount of over-training and the number of model parameters. This enables us to predict the validation loss of a 1.4B parameter, 900B token run (i.e., 32$\times$ over-trained) and a 6.9B parameter, 138B token run (i.e., a compute-optimal run)$\unicode{x2014}$each from experiments that take 300$\times$ less compute. Second, we relate the perplexity of a language model to its downstream task performance by proposing a power law. We use this law to predict top-1 error averaged over downstream tasks for the two aforementioned models, using experiments that take 20$\times$ less compute. Our experiments are available at https://github.com/mlfoundations/scaling.

## 01-010 | Chinchilla Scaling: A replication attempt
- arXiv: 2404.10102  first public: 2024-04-15  latest: 2024-05-15  primary cat: cs.AI
- authors (4): Tamay Besiroglu; Ege Erdil; Matthew Barnett; Josh You
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- pages: 7

ABSTRACT: Hoffmann et al. (2022) propose three methods for estimating a compute-optimal scaling law. We attempt to replicate their third estimation procedure, which involves fitting a parametric loss function to a reconstruction of data from their plots. We find that the reported estimates are inconsistent with their first two estimation methods, fail at fitting the extracted data, and report implausibly narrow confidence intervals--intervals this narrow would require over 600,000 experiments, while they likely only ran fewer than 500. In contrast, our rederivation of the scaling law using the third approach yields results that are compatible with the findings from the first two estimation procedures described by Hoffmann et al.

## 01-011 | Resolving Discrepancies in Compute-Optimal Scaling of Language Models
- arXiv: 2406.19146  first public: 2024-06-27  latest: 2025-01-19  primary cat: cs.LG
- authors (5): Tomer Porian; Mitchell Wortsman; Jenia Jitsev; Ludwig Schmidt; Yair Carmon
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: Spotlight at NeurIPS 2024
- URLs on first pages of PDF: https://github.com/formll/ https://huggingface.co/formll/resolving-scaling-law-discrepancies
- pages: 30

ABSTRACT: Kaplan et al. and Hoffmann et al. developed influential scaling laws for the optimal model size as a function of the compute budget, but these laws yield substantially different predictions. We explain the discrepancy by reproducing the Kaplan scaling law on two datasets (OpenWebText2 and RefinedWeb) and identifying three factors causing the difference: last layer computational cost, warmup duration, and scale-dependent optimizer tuning. With these factors corrected, we obtain excellent agreement with the Hoffmann et al. (i.e., "Chinchilla") scaling law. Counter to a hypothesis of Hoffmann et al., we find that careful learning rate decay is not essential for the validity of their scaling law. As a secondary result, we derive scaling laws for the optimal learning rate and batch size, finding that tuning the AdamW $β_2$ parameter is essential at lower batch sizes.

## 01-012 | When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method
- arXiv: 2402.17193  first public: 2024-02-27  latest: 2024-02-27  primary cat: cs.CL
- authors (4): Biao Zhang; Zhongtao Liu; Colin Cherry; Orhan Firat
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: ICLR24
- pages: 20

ABSTRACT: While large language models (LLMs) often adopt finetuning to unlock their capabilities for downstream applications, our understanding on the inductive biases (especially the scaling properties) of different finetuning methods is still limited. To fill this gap, we conduct systematic experiments studying whether and how different scaling factors, including LLM model size, pretraining data size, new finetuning parameter size and finetuning data size, affect the finetuning performance. We consider two types of finetuning -- full-model tuning (FMT) and parameter efficient tuning (PET, including prompt tuning and LoRA), and explore their scaling behaviors in the data-limited regime where the LLM model size substantially outweighs the finetuning data size. Based on two sets of pretrained bilingual LLMs from 1B to 16B and experiments on bilingual machine translation and multilingual summarization benchmarks, we find that 1) LLM finetuning follows a powerbased multiplicative joint scaling law between finetuning data size and each other scaling factor; 2) LLM finetuning benefits more from LLM model scaling than pretraining data scaling, and PET parameter scaling is generally ineffective; and 3) the optimal finetuning method is highly task- and finetuning data-dependent. We hope our findings could shed light on understanding, selecting and developing LLM finetuning methods.

## 01-013 | Training Compute-Optimal Large Language Models
- arXiv: 2203.15556  first public: 2022-03-29  latest: 2022-03-29  primary cat: cs.CL
- authors (22): Jordan Hoffmann; Sebastian Borgeaud; Arthur Mensch; Elena Buchatskaya; Trevor Cai; Eliza Rutherford ...
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- pages: 36

ABSTRACT: We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4$\times$ more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

## 01-014 | Scaling Data-Constrained Language Models
- arXiv: 2305.16264  first public: 2023-05-25  latest: 2025-06-28  primary cat: cs.CL
- authors (9): Niklas Muennighoff; Alexander M. Rush; Boaz Barak; Teven Le Scao; Aleksandra Piktus; Nouamane Tazi ...
- seed subtopic: 规模规律与计算最优; type: 原始研究; cross: []
- arXiv comment: 50 pages (9 main), 39 figures, 15 tables
- URLs on first pages of PDF: https://github.com/huggingface/datablations
- pages: 50

ABSTRACT: The current trend of scaling language models involves increasing both parameter count and training dataset size. Extrapolating this trend suggests that training dataset size may soon be limited by the amount of text data available on the internet. Motivated by this limit, we investigate scaling language models in data-constrained regimes. Specifically, we run a large set of experiments varying the extent of data repetition and compute budget, ranging up to 900 billion training tokens and 9 billion parameter models. We find that with constrained data for a fixed compute budget, training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data. However, with more repetition, the value of adding compute eventually decays to zero. We propose and empirically validate a scaling law for compute optimality that accounts for the decreasing value of repeated tokens and excess parameters. Finally, we experiment with approaches mitigating data scarcity, including augmenting the training dataset with code data or removing commonly used filters. Models and datasets from our 400 training runs are freely available at https://github.com/huggingface/datablations.

## 01-015 | Compression Represents Intelligence Linearly
- arXiv: 2404.09937  first public: 2024-04-15  latest: 2024-08-19  primary cat: cs.CL
- authors (4): Yuzhen Huang; Jinghan Zhang; Zifei Shan; Junxian He
- seed subtopic: 信息论与压缩视角; type: 原始研究; cross: []
- arXiv comment: COLM 2024. Data and code are available at https://github.com/hkust-nlp/llm-compression-intelligence
- URLs on first pages of PDF: https://github.com/hkust-nlp/llm-compression-intelligence
- pages: 22

ABSTRACT: There is a belief that learning to compress well will lead to intelligence. Recently, language modeling has been shown to be equivalent to compression, which offers a compelling rationale for the success of large language models (LLMs): the development of more advanced language models is essentially enhancing compression which facilitates intelligence. Despite such appealing discussions, little empirical evidence is present for the interplay between compression and intelligence. In this work, we examine their relationship in the context of LLMs, treating LLMs as data compressors. Given the abstract concept of "intelligence", we adopt the average downstream benchmark scores as a surrogate, specifically targeting intelligence related to knowledge and commonsense, coding, and mathematical reasoning. Across 12 benchmarks, our study brings together 31 public LLMs that originate from diverse organizations. Remarkably, we find that LLMs' intelligence -- reflected by average benchmark scores -- almost linearly correlates with their ability to compress external text corpora. These results provide concrete evidence supporting the belief that superior compression indicates greater intelligence. Furthermore, our findings suggest that compression efficiency, as an unsupervised metric derived from raw text corpora, serves as a reliable evaluation measure that is linearly associated with the model capabilities. We open-source our compression datasets as well as our data collection pipelines to facilitate future researchers to assess compression properly.

## 01-016 | Language Modeling Is Compression
- arXiv: 2309.10668  first public: 2023-09-19  latest: 2024-03-18  primary cat: cs.LG
- authors (12): Grégoire Delétang; Anian Ruoss; Paul-Ambroise Duquenne; Elliot Catt; Tim Genewein; Christopher Mattern ...
- seed subtopic: 信息论与压缩视角; type: 原始研究; cross: []
- pages: 17

ABSTRACT: It has long been established that predictive models can be transformed into lossless compressors and vice versa. Incidentally, in recent years, the machine learning community has focused on training increasingly large and powerful self-supervised (language) models. Since these large language models exhibit impressive predictive capabilities, they are well-positioned to be strong compressors. In this work, we advocate for viewing the prediction problem through the lens of compression and evaluate the compression capabilities of large (foundation) models. We show that large language models are powerful general-purpose predictors and that the compression viewpoint provides novel insights into scaling laws, tokenization, and in-context learning. For example, Chinchilla 70B, while trained primarily on text, compresses ImageNet patches to 43.4% and LibriSpeech samples to 16.4% of their raw size, beating domain-specific compressors like PNG (58.5%) or FLAC (30.3%), respectively. Finally, we show that the prediction-compression equivalence allows us to use any compressor (like gzip) to build a conditional generative model.

## 01-017 | Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations
- arXiv: 2405.18392  first public: 2024-05-28  latest: 2024-10-17  primary cat: cs.LG
- authors (6): Alexander Hägele; Elie Bakouch; Atli Kosson; Loubna Ben Allal; Leandro Von Werra; Martin Jaggi
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: Spotlight at NeurIPS 2024
- URLs on first pages of PDF: https://github.com/epfml/schedules-and-scaling/ https://huggingface.co/datasets/DKYoon/SlimPajama-6B
- pages: 26

ABSTRACT: Scale has become a main ingredient in obtaining strong machine learning models. As a result, understanding a model's scaling properties is key to effectively designing both the right training setup as well as future generations of architectures. In this work, we argue that scale and training research has been needlessly complex due to reliance on the cosine schedule, which prevents training across different lengths for the same model size. We investigate the training behavior of a direct alternative -- constant learning rate and cooldowns -- and find that it scales predictably and reliably similar to cosine. Additionally, we show that stochastic weight averaging yields improved performance along the training trajectory, without additional training costs, across different scales. Importantly, with these findings we demonstrate that scaling experiments can be performed with significantly reduced compute and GPU hours by utilizing fewer but reusable training runs. Our code is available at \url{https://github.com/epfml/schedules-and-scaling/}.

## 01-018 | Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape Perspective
- arXiv: 2410.05192  first public: 2024-10-07  latest: 2024-12-02  primary cat: cs.LG
- authors (6): Kaiyue Wen; Zhiyuan Li; Jason Wang; David Hall; Percy Liang; Tengyu Ma
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: 45 pages,13 figures
- pages: 45

ABSTRACT: Training language models currently requires pre-determining a fixed compute budget because the typical cosine learning rate schedule depends on the total number of steps. In contrast, the Warmup-Stable-Decay (WSD) schedule uses a constant learning rate to produce a main branch of iterates that can in principle continue indefinitely without a pre-specified compute budget. Then, given any compute budget, one can branch out from the main branch at a proper time with a rapidly decaying learning rate to produce a strong model. Empirically, WSD generates a non-traditional loss curve: the loss remains elevated during the stable phase but sharply declines during the decay phase. Towards explaining this phenomenon, we conjecture that pretraining loss exhibits a river valley landscape, which resembles a deep valley with a river at its bottom. Under this assumption, we show that during the stable phase, the iterate undergoes large oscillations due to the high learning rate, yet it progresses swiftly along the river. During the decay phase, the rapidly dropping learning rate minimizes the iterate's oscillations, moving it closer to the river and revealing true optimization progress. Therefore, the sustained high learning rate phase and fast decaying phase are responsible for progress in the river and the mountain directions respectively, and are both critical. Our analysis predicts phenomenons consistent with empirical observations and shows that this landscape can emerge from pretraining on a simple bi-gram dataset. Inspired by the theory, we introduce WSD-S, a variant of WSD that reuses previous checkpoints' decay phases and keeps only one main branch, where we resume from a decayed checkpoint. WSD-S empirically outperforms WSD and Cyclic-Cosine in obtaining multiple language model checkpoints across various compute budgets in a single run for parameters scaling from 0.1B to 1.2B.

## 01-019 | Straight to Zero: Why Linearly Decaying the Learning Rate to Zero Works Best for LLMs
- arXiv: 2502.15938  first public: 2025-02-21  latest: 2025-11-23  primary cat: cs.LG
- authors (6): Shane Bergsma; Nolan Dey; Gurpreet Gosal; Gavia Gray; Daria Soboleva; Joel Hestness
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: ICLR 2025
- pages: 34

ABSTRACT: LLMs are commonly trained with a learning rate (LR) warmup, followed by cosine decay to 10% of the maximum (10x decay). In a large-scale empirical study, we show that under an optimal peak LR, a simple linear decay-to-zero (D2Z) schedule consistently outperforms other schedules when training at compute-optimal dataset sizes. D2Z is superior across a range of model sizes, batch sizes, datasets, and vocabularies. Benefits increase as dataset size increases. Leveraging a novel interpretation of AdamW as an exponential moving average of weight updates, we show how linear D2Z optimally balances the demands of early training (moving away from initial conditions) and late training (averaging over more updates in order to mitigate gradient noise). In experiments, a 610M-parameter model trained for 80 tokens-per-parameter (TPP) using D2Z achieves lower loss than when trained for 200 TPP using 10x decay, corresponding to an astonishing 60% compute savings. Models such as Llama2-7B, trained for 286 TPP with 10x decay, could likely have saved a majority of compute by training with D2Z.

## 01-020 | The Road Less Scheduled
- arXiv: 2405.15682  first public: 2024-05-24  latest: 2024-10-29  primary cat: cs.LG
- authors (6): Aaron Defazio; Xingyu Alice Yang; Harsh Mehta; Konstantin Mishchenko; Ahmed Khaled; Ashok Cutkosky
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/facebookresearch/schedule_free
- pages: 35

ABSTRACT: Existing learning rate schedules that do not require specification of the optimization stopping step T are greatly out-performed by learning rate schedules that depend on T. We propose an approach that avoids the need for this stopping time by eschewing the use of schedules entirely, while exhibiting state-of-the-art performance compared to schedules across a wide family of problems ranging from convex problems to large-scale deep learning problems. Our Schedule-Free approach introduces no additional hyper-parameters over standard optimizers with momentum. Our method is a direct consequence of a new theory we develop that unifies scheduling and iterate averaging. An open source implementation of our method is available at https://github.com/facebookresearch/schedule_free. Schedule-Free AdamW is the core algorithm behind our winning entry to the MLCommons 2024 AlgoPerf Algorithmic Efficiency Challenge Self-Tuning track.

## 01-021 | Muon is Scalable for LLM Training
- arXiv: 2502.16982  first public: 2025-02-24  latest: 2025-02-24  primary cat: cs.LG
- authors (28): Jingyuan Liu; Jianlin Su; Xingcheng Yao; Zhejun Jiang; Guokun Lai; Yulun Du ...
- seed subtopic: 优化器与学习率调度; type: 技术报告; cross: []
- pages: 19

ABSTRACT: Recently, the Muon optimizer based on matrix orthogonalization has demonstrated strong results in training small-scale language models, but the scalability to larger models has not been proven. We identify two crucial techniques for scaling up Muon: (1) adding weight decay and (2) carefully adjusting the per-parameter update scale. These techniques allow Muon to work out-of-the-box on large-scale training without the need of hyper-parameter tuning. Scaling law experiments indicate that Muon achieves $\sim\!2\times$ computational efficiency compared to AdamW with compute optimal training. Based on these improvements, we introduce Moonlight, a 3B/16B-parameter Mixture-of-Expert (MoE) model trained with 5.7T tokens using Muon. Our model improves the current Pareto frontier, achieving better performance with much fewer training FLOPs compared to prior models. We open-source our distributed Muon implementation that is memory optimal and communication efficient. We also release the pretrained, instruction-tuned, and intermediate checkpoints to support future research.

## 01-022 | Deconstructing What Makes a Good Optimizer for Language Models
- arXiv: 2407.07972  first public: 2024-07-10  latest: 2025-02-28  primary cat: cs.LG
- authors (5): Rosie Zhao; Depen Morwani; David Brandfonbrener; Nikhil Vyas; Sham Kakade
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: 21 pages, ICLR 2025
- pages: 21

ABSTRACT: Training language models becomes increasingly expensive with scale, prompting numerous attempts to improve optimization efficiency. Despite these efforts, the Adam optimizer remains the most widely used, due to a prevailing view that it is the most effective approach. We aim to compare several optimization algorithms, including SGD, Adafactor, Adam, Lion, and Sophia in the context of autoregressive language modeling across a range of model sizes, hyperparameters, and architecture variants. Our findings indicate that, except for SGD, these algorithms all perform comparably both in their optimal performance and also in terms of how they fare across a wide range of hyperparameter choices. Our results suggest to practitioners that the choice of optimizer can be guided by practical considerations like memory constraints and ease of implementation, as no single algorithm emerged as a clear winner in terms of performance or stability to hyperparameter misspecification. Given our findings, we further dissect these approaches, examining two simplified versions of Adam: a) signed momentum (Signum) which we see recovers both the performance and hyperparameter stability of Adam and b) Adalayer, a layerwise variant of Adam which we introduce to study the impact on Adam's preconditioning for different layers of the network. Examining Adalayer leads us to the conclusion that, perhaps surprisingly, adaptivity on both the last layer and LayerNorm parameters in particular are necessary for retaining performance and stability to learning rate.

## 01-023 | Fantastic Pretraining Optimizers and Where to Find Them
- arXiv: 2509.02046  first public: 2025-09-02  latest: 2026-10-25  primary cat: cs.LG
- authors (4): Kaiyue Wen; David Hall; Tengyu Ma; Percy Liang
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: 108 pages, 8 figures, reproducible runs available at https://wandb.ai/marin-community/optimizer-scaling
- pages: 108

ABSTRACT: AdamW has long been the dominant optimizer in language model pretraining, despite numerous claims that alternative optimizers offer 1.4 to 2x speedup. We posit that two methodological shortcomings have obscured fair comparisons and hindered practical adoption: (i) unequal hyperparameter tuning and (ii) limited or misleading evaluation setups. To address these two issues, we conduct a systematic study of ten deep learning optimizers across four model scales (0.1B-1.2B parameters) and data-to-model ratios (1-8x the Chinchilla optimum). We find that fair and informative comparisons require rigorous hyperparameter tuning and evaluations across a range of model scales and data-to-model ratios, performed at the end of training. First, optimal hyperparameters for one optimizer may be suboptimal for another, making blind hyperparameter transfer unfair. Second, the actual speedup of many proposed optimizers over well-tuned baselines is lower than claimed and decreases with model size to only 1.1x for 1.2B parameter models. Thirdly, comparing intermediate checkpoints before reaching the target training budgets can be misleading, as rankings between two optimizers can flip during training due to learning rate decay. Through our thorough investigation, we find that all the fastest optimizers such as Muon and Soap, use matrices as preconditioners -- multiplying gradients with matrices rather than entry-wise scalars. However, the speedup of matrix-based optimizers is inversely proportional to model scale, decreasing from 1.4x over AdamW for 0.1B parameter models to merely 1.1x for 1.2B parameter models.

## 01-025 | How Does Critical Batch Size Scale in Pre-training?
- arXiv: 2410.21676  first public: 2024-10-29  latest: 2025-04-21  primary cat: cs.LG
- authors (8): Hanlin Zhang; Depen Morwani; Nikhil Vyas; Jingfeng Wu; Difan Zou; Udaya Ghai ...
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: ICLR 2025, Blog post: https://kempnerinstitute.harvard.edu/research/deeper-learning/how-does-critical-batch-size-scale-in-pre-training-decoupling-data-and-model-size
- URLs on first pages of PDF: https://github.com/hlzhang109/critical-batch-size
- pages: 31

ABSTRACT: Training large-scale models under given resources requires careful design of parallelism strategies. In particular, the efficiency notion of critical batch size (CBS), concerning the compromise between time and compute, marks the threshold beyond which greater data parallelism leads to diminishing returns. To operationalize it, we propose a measure of CBS and pre-train a series of auto-regressive language models, ranging from 85 million to 1.2 billion parameters, on the C4 dataset. Through extensive hyper-parameter sweeps and careful control of factors such as batch size, momentum, and learning rate along with its scheduling, we systematically investigate the impact of scale on CBS. Then we fit scaling laws with respect to model and data sizes to decouple their effects. Overall, our results demonstrate that CBS scales primarily with data size rather than model size, a finding we justify theoretically through the analysis of infinite-width limits of neural networks and infinite-dimensional least squares regression. Of independent interest, we highlight the importance of common hyper-parameter choices and strategies for studying large-scale pre-training beyond fixed training durations.

## 01-026 | Scaling Exponents Across Parameterizations and Optimizers
- arXiv: 2407.05872  first public: 2024-07-08  latest: 2024-07-16  primary cat: cs.LG
- authors (11): Katie Everett; Lechao Xiao; Mitchell Wortsman; Alexander A. Alemi; Roman Novak; Peter J. Liu ...
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: 63 pages, International Conference on Machine Learning 2024
- pages: 63

ABSTRACT: Robust and effective scaling of models from small to large width typically requires the precise adjustment of many algorithmic and architectural details, such as parameterization and optimizer choices. In this work, we propose a new perspective on parameterization by investigating a key assumption in prior work about the alignment between parameters and data and derive new theoretical results under weaker assumptions and a broader set of optimizers. Our extensive empirical investigation includes tens of thousands of models trained with all combinations of three optimizers, four parameterizations, several alignment assumptions, more than a dozen learning rates, and fourteen model sizes up to 26.8B parameters. We find that the best learning rate scaling prescription would often have been excluded by the assumptions in prior work. Our results show that all parameterizations, not just maximal update parameterization (muP), can achieve hyperparameter transfer; moreover, our novel per-layer learning rate prescription for standard parameterization outperforms muP. Finally, we demonstrate that an overlooked aspect of parameterization, the epsilon parameter in Adam, must be scaled correctly to avoid gradient underflow and propose Adam-atan2, a new numerically stable, scale-invariant version of Adam that eliminates the epsilon hyperparameter entirely.

## 01-027 | Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer
- arXiv: 2203.03466  first public: 2022-03-07  latest: 2022-03-28  primary cat: cs.LG
- authors (10): Greg Yang; Edward J. Hu; Igor Babuschkin; Szymon Sidor; Xiaodong Liu; David Farhi ...
- seed subtopic: 优化器与学习率调度; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2021
- pages: 48

ABSTRACT: Hyperparameter (HP) tuning in deep learning is an expensive process, prohibitively so for neural networks (NNs) with billions of parameters. We show that, in the recently discovered Maximal Update Parametrization (muP), many optimal HPs remain stable even as model size changes. This leads to a new HP tuning paradigm we call muTransfer: parametrize the target model in muP, tune the HP indirectly on a smaller model, and zero-shot transfer them to the full-sized model, i.e., without directly tuning the latter at all. We verify muTransfer on Transformer and ResNet. For example, 1) by transferring pretraining HPs from a model of 13M parameters, we outperform published numbers of BERT-large (350M parameters), with a total tuning cost equivalent to pretraining BERT-large once; 2) by transferring from 40M parameters, we outperform published numbers of the 6.7B GPT-3 model, with tuning cost only 7% of total pretraining cost. A Pytorch implementation of our technique can be found at github.com/microsoft/mup and installable via `pip install mup`.

## 01-030 | The Transient Nature of Emergent In-Context Learning in Transformers
- arXiv: 2311.08360  first public: 2023-11-14  latest: 2023-12-11  primary cat: cs.LG
- authors (6): Aaditya K. Singh; Stephanie C. Y. Chan; Ted Moskovitz; Erin Grant; Andrew M. Saxe; Felix Hill
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: 19 pages, 16 figures
- pages: 19

ABSTRACT: Transformer neural networks can exhibit a surprising capacity for in-context learning (ICL) despite not being explicitly trained for it. Prior work has provided a deeper understanding of how ICL emerges in transformers, e.g. through the lens of mechanistic interpretability, Bayesian inference, or by examining the distributional properties of training data. However, in each of these cases, ICL is treated largely as a persistent phenomenon; namely, once ICL emerges, it is assumed to persist asymptotically. Here, we show that the emergence of ICL during transformer training is, in fact, often transient. We train transformers on synthetic data designed so that both ICL and in-weights learning (IWL) strategies can lead to correct predictions. We find that ICL first emerges, then disappears and gives way to IWL, all while the training loss decreases, indicating an asymptotic preference for IWL. The transient nature of ICL is observed in transformers across a range of model sizes and datasets, raising the question of how much to "overtrain" transformers when seeking compact, cheaper-to-run models. We find that L2 regularization may offer a path to more persistent ICL that removes the need for early stopping based on ICL-style validation tasks. Finally, we present initial evidence that ICL transience may be caused by competition between ICL and IWL circuits.

## 01-031 | In-Context Language Learning: Architectures and Algorithms
- arXiv: 2401.12973  first public: 2024-01-23  latest: 2024-01-30  primary cat: cs.CL
- authors (4): Ekin Akyürek; Bailin Wang; Yoon Kim; Jacob Andreas
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: Fixes a typo in the title, and adds additional references
- URLs on first pages of PDF: https://github.com/berlino/seq_icl
- pages: 30

ABSTRACT: Large-scale neural language models exhibit a remarkable capacity for in-context learning (ICL): they can infer novel functions from datasets provided as input. Most of our current understanding of when and how ICL arises comes from LMs trained on extremely simple learning problems like linear regression and associative recall. There remains a significant gap between these model problems and the "real" ICL exhibited by LMs trained on large text corpora, which involves not just retrieval and function approximation but free-form generation of language and other structured outputs. In this paper, we study ICL through the lens of a new family of model problems we term in context language learning (ICLL). In ICLL, LMs are presented with a set of strings from a formal language, and must generate additional strings from the same language. We focus on in-context learning of regular languages generated by random finite automata. We evaluate a diverse set of neural sequence models (including several RNNs, Transformers, and state-space model variants) on regular ICLL tasks, aiming to answer three questions: (1) Which model classes are empirically capable of ICLL? (2) What algorithmic solutions do successful models implement to perform ICLL? (3) What architectural changes can improve ICLL in less performant models? We first show that Transformers significantly outperform neural sequence models with recurrent or convolutional representations on ICLL tasks. Next, we provide evidence that their ability to do so relies on specialized "n-gram heads" (higher-order variants of induction heads) that compute input-conditional next-token distributions. Finally, we show that hard-wiring these heads into neural models improves performance not just on ICLL, but natural language modeling -- improving the perplexity of 340M-parameter models by up to 1.14 points (6.7%) on the SlimPajama dataset.

## 01-032 | Many-Shot In-Context Learning
- arXiv: 2404.11018  first public: 2024-04-17  latest: 2024-10-17  primary cat: cs.LG
- authors (15): Rishabh Agarwal; Avi Singh; Lei M. Zhang; Bernd Bohnet; Luis Rosias; Stephanie Chan ...
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: NeurIPS (Spotlight)
- pages: 32

ABSTRACT: Large language models (LLMs) excel at few-shot in-context learning (ICL) -- learning from a few examples provided in context at inference, without any weight updates. Newly expanded context windows allow us to investigate ICL with hundreds or thousands of examples -- the many-shot regime. Going from few-shot to many-shot, we observe significant performance gains across a wide variety of generative and discriminative tasks. While promising, many-shot ICL can be bottlenecked by the available amount of human-generated examples. To mitigate this limitation, we explore two new settings: Reinforced and Unsupervised ICL. Reinforced ICL uses model-generated chain-of-thought rationales in place of human examples. Unsupervised ICL removes rationales from the prompt altogether, and prompts the model only with domain-specific questions. We find that both Reinforced and Unsupervised ICL can be quite effective in the many-shot regime, particularly on complex reasoning tasks. Finally, we demonstrate that, unlike few-shot learning, many-shot learning is effective at overriding pretraining biases, can learn high-dimensional functions with numerical inputs, and performs comparably to fine-tuning. We also find that inference cost increases linearly in the many-shot regime, and frontier LLMs benefit from many-shot ICL to varying degrees. Our analysis also reveals the limitations of next-token prediction loss as an indicator of downstream ICL performance.

## 01-033 | LLMs Are Few-Shot In-Context Low-Resource Language Learners
- arXiv: 2403.16512  first public: 2024-03-25  latest: 2024-06-25  primary cat: cs.CL
- authors (3): Samuel Cahyawijaya; Holy Lovenia; Pascale Fung
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: ['11']
- URLs on first pages of PDF: https://github.com/SamuelCahyawijaya/
- pages: 29

ABSTRACT: In-context learning (ICL) empowers large language models (LLMs) to perform diverse tasks in underrepresented languages using only short in-context information, offering a crucial avenue for narrowing the gap between high-resource and low-resource languages. Nonetheless, there is only a handful of works explored ICL for low-resource languages with most of them focusing on relatively high-resource languages, such as French and Spanish. In this work, we extensively study ICL and its cross-lingual variation (X-ICL) on 25 low-resource and 7 relatively higher-resource languages. Our study not only assesses the effectiveness of ICL with LLMs in low-resource languages but also identifies the shortcomings of in-context label alignment, and introduces a more effective alternative: query alignment. Moreover, we provide valuable insights into various facets of ICL for low-resource languages. Our study concludes the significance of few-shot in-context information on enhancing the low-resource understanding quality of LLMs through semantically relevant information by closing the language gap in the target language and aligning the semantics between the targeted low-resource and the high-resource language that the model is proficient in. Our work highlights the importance of advancing ICL research, particularly for low-resource languages. Our code is publicly released at https://github.com/SamuelCahyawijaya/in-context-alignment

## 01-034 | The Mystery of In-Context Learning: A Comprehensive Survey on Interpretation and Analysis
- arXiv: 2311.00237  first public: 2023-11-01  latest: 2024-10-03  primary cat: cs.CL
- authors (6): Yuxiang Zhou; Jiazheng Li; Yanzheng Xiang; Hanqi Yan; Lin Gui; Yulan He
- seed subtopic: 上下文学习与泛化理论; type: 综述; cross: []
- arXiv comment: Accepted to the main conference of EMNLP 2024. Resources are available at https://github.com/zyxnlp/ICL-Interpretation-Analysis-Resources
- URLs on first pages of PDF: https://github.com/zyxnlp/
- pages: 13

ABSTRACT: Understanding in-context learning (ICL) capability that enables large language models (LLMs) to excel in proficiency through demonstration examples is of utmost importance. This importance stems not only from the better utilization of this capability across various tasks, but also from the proactive identification and mitigation of potential risks, including concerns regarding truthfulness, bias, and toxicity, that may arise alongside the capability. In this paper, we present a thorough survey on the interpretation and analysis of in-context learning. First, we provide a concise introduction to the background and definition of in-context learning. Then, we give an overview of advancements from two perspectives: 1) a theoretical perspective, emphasizing studies on mechanistic interpretability and delving into the mathematical foundations behind ICL; and 2) an empirical perspective, concerning studies that empirically analyze factors associated with ICL. We conclude by highlighting the challenges encountered and suggesting potential avenues for future research. We believe that our work establishes the basis for further exploration into the interpretation of in-context learning. Additionally, we have created a repository containing the resources referenced in our survey.

## 01-035 | Understanding Emergent Abilities of Language Models from the Loss Perspective
- arXiv: 2403.15796  first public: 2024-03-23  latest: 2025-01-15  primary cat: cs.CL
- authors (4): Zhengxiao Du; Aohan Zeng; Yuxiao Dong; Jie Tang
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: 23 pages, 8 figures. Accepted in NeurIPS 2024
- pages: 23

ABSTRACT: Recent studies have put into question the belief that emergent abilities in language models are exclusive to large models. This skepticism arises from two observations: 1) smaller models can also exhibit high performance on emergent abilities and 2) there is doubt on the discontinuous metrics used to measure these abilities. In this paper, we propose to study emergent abilities in the lens of pre-training loss, instead of model size or training compute. We demonstrate that the Transformer models with the same pre-training loss, but different model and data sizes, generate the same performance on various downstream tasks, with a fixed data corpus, tokenization, and model architecture. We also discover that a model exhibits emergent abilities on certain tasks -- regardless of the continuity of metrics -- when its pre-training loss falls below a specific threshold. Before reaching this threshold, its performance remains at the level of random guessing. This inspires us to redefine emergent abilities as those that manifest in models with lower pre-training losses, highlighting that these abilities cannot be predicted by merely extrapolating the performance trends of models with higher pre-training losses.

## 01-036 | Generalization v.s. Memorization: Tracing Language Models' Capabilities Back to Pretraining Data
- arXiv: 2407.14985  first public: 2024-07-20  latest: 2025-03-02  primary cat: cs.CL
- authors (7): Xinyi Wang; Antonis Antoniades; Yanai Elazar; Alfonso Amayuelas; Alon Albalak; Kexun Zhang ...
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: Accepted to ICLR 2025
- URLs on first pages of PDF: https://github.com/a-antoniades/llm-corpus-search
- pages: 21

ABSTRACT: The impressive capabilities of large language models (LLMs) have sparked debate over whether these models genuinely generalize to unseen tasks or predominantly rely on memorizing vast amounts of pretraining data. To explore this issue, we introduce an extended concept of memorization, distributional memorization, which measures the correlation between the LLM output probabilities and the pretraining data frequency. To effectively capture task-specific pretraining data frequency, we propose a novel task-gram language model, which is built by counting the co-occurrence of semantically related $n$-gram pairs from task inputs and outputs in the pretraining corpus. Using the Pythia models trained on the Pile dataset, we evaluate four distinct tasks: machine translation, factual question answering, world knowledge understanding, and math reasoning. Our findings reveal varying levels of memorization, with the strongest effect observed in factual question answering. Furthermore, while model performance improves across all tasks as LLM size increases, only factual question answering shows an increase in memorization, whereas machine translation and reasoning tasks exhibit greater generalization, producing more novel outputs. This study demonstrates that memorization plays a larger role in simpler, knowledge-intensive tasks, while generalization is the key for harder, reasoning-based tasks, providing a scalable method for analyzing large pretraining corpora in greater depth.

## 01-037 | Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws
- arXiv: 2404.05405  first public: 2024-04-08  latest: 2024-04-08  primary cat: cs.CL
- authors (2): Zeyuan Allen-Zhu; Yuanzhi Li
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- pages: 41

ABSTRACT: Scaling laws describe the relationship between the size of language models and their capabilities. Unlike prior studies that evaluate a model's capability via loss or benchmarks, we estimate the number of knowledge bits a model stores. We focus on factual knowledge represented as tuples, such as (USA, capital, Washington D.C.) from a Wikipedia page. Through multiple controlled datasets, we establish that language models can and only can store 2 bits of knowledge per parameter, even when quantized to int8, and such knowledge can be flexibly extracted for downstream applications. Consequently, a 7B model can store 14B bits of knowledge, surpassing the English Wikipedia and textbooks combined based on our estimation. More broadly, we present 12 results on how (1) training duration, (2) model architecture, (3) quantization, (4) sparsity constraints such as MoE, and (5) data signal-to-noise ratio affect a model's knowledge storage capacity. Notable insights include: * The GPT-2 architecture, with rotary embedding, matches or even surpasses LLaMA/Mistral architectures in knowledge storage, particularly over shorter training durations. This arises because LLaMA/Mistral uses GatedMLP, which is less stable and harder to train. * Prepending training data with domain names (e.g., wikipedia.org) significantly increases a model's knowledge capacity. Language models can autonomously identify and prioritize domains rich in knowledge, optimizing their storage capacity.

## 01-038 | How Do Large Language Models Acquire Factual Knowledge During Pretraining?
- arXiv: 2406.11813  first public: 2024-06-17  latest: 2024-11-12  primary cat: cs.CL
- authors (7): Hoyeon Chang; Jinho Park; Seonghyeon Ye; Sohee Yang; Youngkyung Seo; Du-Seong Chang ...
- seed subtopic: 上下文学习与泛化理论; type: 原始研究; cross: []
- arXiv comment: Accepted at NeurIPS 2024
- URLs on first pages of PDF: https://github.com/kaistAI/factual-knowledge-acquisition/
- pages: 36

ABSTRACT: Despite the recent observation that large language models (LLMs) can store substantial factual knowledge, there is a limited understanding of the mechanisms of how they acquire factual knowledge through pretraining. This work addresses this gap by studying how LLMs acquire factual knowledge during pretraining. The findings reveal several important insights into the dynamics of factual knowledge acquisition during pretraining. First, counterintuitively, we observe that pretraining on more data shows no significant improvement in the model's capability to acquire and maintain factual knowledge. Next, there is a power-law relationship between training steps and forgetting of memorization and generalization of factual knowledge, and LLMs trained with duplicated training data exhibit faster forgetting. Third, training LLMs with larger batch sizes can enhance the models' robustness to forgetting. Overall, our observations suggest that factual knowledge acquisition in LLM pretraining occurs by progressively increasing the probability of factual knowledge presented in the pretraining data at each step. However, this increase is diluted by subsequent forgetting. Based on this interpretation, we demonstrate that we can provide plausible explanations for recently observed behaviors of LLMs, such as the poor performance of LLMs on long-tail knowledge and the benefits of deduplicating the pretraining corpus.

## 01-040 | The Semantic Hub Hypothesis: Language Models Share Semantic Representations Across Languages and Modalities
- arXiv: 2411.04986  first public: 2024-11-07  latest: 2025-03-11  primary cat: cs.CL
- authors (5): Zhaofeng Wu; Xinyan Velocity Yu; Dani Yogatama; Jiasen Lu; Yoon Kim
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: ICLR 2025
- URLs on first pages of PDF: https://github.com/ZhaofengWu/semantic-hub
- pages: 23

ABSTRACT: Modern language models can process inputs across diverse languages and modalities. We hypothesize that models acquire this capability through learning a shared representation space across heterogeneous data types (e.g., different languages and modalities), which places semantically similar inputs near one another, even if they are from different modalities/languages. We term this the semantic hub hypothesis, following the hub-and-spoke model from neuroscience (Patterson et al., 2007) which posits that semantic knowledge in the human brain is organized through a transmodal semantic "hub" which integrates information from various modality-specific "spokes" regions. We first show that model representations for semantically equivalent inputs in different languages are similar in the intermediate layers, and that this space can be interpreted using the model's dominant pretraining language via the logit lens. This tendency extends to other data types, including arithmetic expressions, code, and visual/audio inputs. Interventions in the shared representation space in one data type also predictably affect model outputs in other data types, suggesting that this shared representations space is not simply a vestigial byproduct of large-scale training on broad data, but something that is actively utilized by the model during input processing.

## 01-042 | Unveiling Linguistic Regions in Large Language Models
- arXiv: 2402.14700  first public: 2024-02-22  latest: 2024-05-30  primary cat: cs.CL
- authors (5): Zhihao Zhang; Jun Zhao; Qi Zhang; Tao Gui; Xuanjing Huang
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted by ACL 2024. Camera-Ready Version
- pages: 20

ABSTRACT: Large Language Models (LLMs) have demonstrated considerable cross-lingual alignment and generalization ability. Current research primarily focuses on improving LLMs' cross-lingual generalization capabilities. However, there is still a lack of research on the intrinsic mechanisms of how LLMs achieve cross-lingual alignment. From the perspective of region partitioning, this paper conducts several investigations on the linguistic competence of LLMs. We discover a core region in LLMs that corresponds to linguistic competence, accounting for approximately 1% of the total model parameters. Removing this core region by setting parameters to zero results in a significant performance decrease across 30 different languages. Furthermore, this core region exhibits significant dimensional dependence, perturbations to even a single parameter on specific dimensions leading to a loss of linguistic competence. Moreover, we discover that distinct monolingual regions exist for different languages, and disruption to these specific regions substantially reduces the LLMs' proficiency in those corresponding languages. Our research also indicates that freezing the core linguistic region during further pre-training can mitigate the issue of catastrophic forgetting (CF), a common phenomenon observed during further pre-training of LLMs. Overall, exploring the LLMs' functional regions provides insights into the foundation of their intelligence.

## 01-043 | On the Multilingual Ability of Decoder-based Pre-trained Language Models: Finding and Controlling Language-Specific Neurons
- arXiv: 2404.02431  first public: 2024-04-03  latest: 2024-04-03  primary cat: cs.CL
- authors (5): Takeshi Kojima; Itsuki Okimura; Yusuke Iwasawa; Hitomi Yanaka; Yutaka Matsuo
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted to NAACL2024. Our code is available at https://github.com/kojima-takeshi188/lang_neuron
- pages: 53

ABSTRACT: Current decoder-based pre-trained language models (PLMs) successfully demonstrate multilingual capabilities. However, it is unclear how these models handle multilingualism. We analyze the neuron-level internal behavior of multilingual decoder-based PLMs, Specifically examining the existence of neurons that fire ``uniquely for each language'' within decoder-only multilingual PLMs. We analyze six languages: English, German, French, Spanish, Chinese, and Japanese, and show that language-specific neurons are unique, with a slight overlap (< 5%) between languages. These neurons are mainly distributed in the models' first and last few layers. This trend remains consistent across languages and models. Additionally, we tamper with less than 1% of the total neurons in each model during inference and demonstrate that tampering with a few language-specific neurons drastically changes the probability of target language occurrence in text generation.

## 01-044 | Understanding Cross-Lingual Alignment -- A Survey
- arXiv: 2404.06228  first public: 2024-04-09  latest: 2024-06-11  primary cat: cs.CL
- authors (3): Katharina Hämmerl; Jindřich Libovický; Alexander Fraser
- seed subtopic: 表示几何与跨语言对齐; type: 综述; cross: []
- arXiv comment: Camera-ready version, ACL Findings 2024
- pages: 22

ABSTRACT: Cross-lingual alignment, the meaningful similarity of representations across languages in multilingual language models, has been an active field of research in recent years. We survey the literature of techniques to improve cross-lingual alignment, providing a taxonomy of methods and summarising insights from throughout the field. We present different understandings of cross-lingual alignment and their limitations. We provide a qualitative summary of results from a large number of surveyed papers. Finally, we discuss how these insights may be applied not only to encoder models, where this topic has been heavily studied, but also to encoder-decoder or even decoder-only models, and argue that an effective trade-off between language-neutral and language-specific information is key.

## 01-045 | Probing the Emergence of Cross-lingual Alignment during LLM Training
- arXiv: 2406.13229  first public: 2024-06-19  latest: 2024-06-19  primary cat: cs.CL
- authors (3): Hetong Wang; Pasquale Minervini; Edoardo M. Ponti
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted to Findings of the Association for Computational Linguistics: ACL 2024
- URLs on first pages of PDF: https://huggingface.co/bigscience/
- pages: 15

ABSTRACT: Multilingual Large Language Models (LLMs) achieve remarkable levels of zero-shot cross-lingual transfer performance. We speculate that this is predicated on their ability to align languages without explicit supervision from parallel sentences. While representations of translationally equivalent sentences in different languages are known to be similar after convergence, however, it remains unclear how such cross-lingual alignment emerges during pre-training of LLMs. Our study leverages intrinsic probing techniques, which identify which subsets of neurons encode linguistic features, to correlate the degree of cross-lingual neuron overlap with the zero-shot cross-lingual transfer performance for a given model. In particular, we rely on checkpoints of BLOOM, a multilingual autoregressive LLM, across different training steps and model scales. We observe a high correlation between neuron overlap and downstream performance, which supports our hypothesis on the conditions leading to effective cross-lingual transfer. Interestingly, we also detect a degradation of both implicit alignment and multilingual abilities in certain phases of the pre-training process, providing new insights into the multilingual pretraining dynamics.

## 01-046 | Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs
- arXiv: 2502.14830  first public: 2025-02-20  latest: 2025-06-02  primary cat: cs.CL
- authors (2): Danni Liu; Jan Niehues
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: ['08']
- arXiv comment: ACL 2025
- URLs on first pages of PDF: https://github.com/dannigt/mid-align
- pages: 18

ABSTRACT: While large language models demonstrate remarkable capabilities at task-specific applications through fine-tuning, extending these benefits across diverse languages is essential for broad accessibility. However, effective cross-lingual transfer is hindered by LLM performance gaps across languages and the scarcity of fine-tuning data in many languages. Through analysis of LLM internal representations from over 1,000+ language pairs, we discover that middle layers exhibit the strongest potential for cross-lingual alignment. Building on this finding, we propose a middle-layer alignment objective integrated into task-specific training. Our experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages. The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment. Furthermore, we show that separately trained alignment modules can be merged with existing task-specific modules, improving cross-lingual capabilities without full re-training. Our code is publicly available (https://github.com/dannigt/mid-align).

## 01-049 | Do Multilingual LLMs Think In English?
- arXiv: 2502.15603  first public: 2025-02-21  latest: 2025-02-21  primary cat: cs.CL
- authors (3): Lisa Schut; Yarin Gal; Sebastian Farquhar
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Main paper 9 pages; including appendix 48 pages
- pages: 48

ABSTRACT: Large language models (LLMs) have multilingual capabilities and can solve tasks across various languages. However, we show that current LLMs make key decisions in a representation space closest to English, regardless of their input and output languages. Exploring the internal representations with a logit lens for sentences in French, German, Dutch, and Mandarin, we show that the LLM first emits representations close to English for semantically-loaded words before translating them into the target language. We further show that activation steering in these LLMs is more effective when the steering vectors are computed in English rather than in the language of the inputs and outputs. This suggests that multilingual LLMs perform key reasoning steps in a representation that is heavily shaped by English in a way that is not transparent to system users.

## 01-050 | Beyond English-Centric LLMs: What Language Do Multilingual Language Models Think in?
- arXiv: 2408.10811  first public: 2024-08-20  latest: 2024-08-20  primary cat: cs.CL
- authors (8): Chengzhi Zhong; Fei Cheng; Qianying Liu; Junfeng Jiang; Zhen Wan; Chenhui Chu ...
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: work in progress
- pages: 11

ABSTRACT: In this study, we investigate whether non-English-centric LLMs, despite their strong performance, `think' in their respective dominant language: more precisely, `think' refers to how the representations of intermediate layers, when un-embedded into the vocabulary space, exhibit higher probabilities for certain dominant languages during generation. We term such languages as internal $\textbf{latent languages}$. We examine the latent language of three typical categories of models for Japanese processing: Llama2, an English-centric model; Swallow, an English-centric model with continued pre-training in Japanese; and LLM-jp, a model pre-trained on balanced English and Japanese corpora. Our empirical findings reveal that, unlike Llama2 which relies exclusively on English as the internal latent language, Japanese-specific Swallow and LLM-jp employ both Japanese and English, exhibiting dual internal latent languages. For any given target language, the model preferentially activates the latent language most closely related to it. In addition, we explore how intermediate layers respond to questions involving cultural conflicts between latent internal and target output languages. We further explore how the language identity shifts across layers while keeping consistent semantic meaning reflected in the intermediate layer representations. This study deepens the understanding of non-English-centric large language models, highlighting the intricate dynamics of language representation within their intermediate layers.

## 01-051 | High-Dimensional Interlingual Representations of Large Language Models
- arXiv: 2503.11280  first public: 2025-03-14  latest: 2025-08-17  primary cat: cs.CL
- authors (4): Bryan Wilie; Samuel Cahyawijaya; Junxian He; Pascale Fung
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/HLTCHKUST/interlingua
- pages: 34

ABSTRACT: Large language models (LLMs) trained on massive multilingual datasets hint at the formation of interlingual constructs--a shared subspace in the representation space. However, evidence regarding this phenomenon is mixed, leaving it unclear whether these models truly develop unified interlingual representations, or present a partially aligned constructs. We explore 31 diverse languages varying on their resource-levels, typologies, and geographical regions; and find that multilingual LLMs exhibit inconsistent cross-lingual alignments. To address this, we propose an interlingual representation framework identifying both the shared interlingual semantic subspace and fragmented components, existed due to representational limitations. We introduce Interlingual Local Overlap (ILO) score to quantify interlingual alignment by comparing the local neighborhood structures of high-dimensional representations. We utilize ILO to investigate the impact of single-language fine-tuning on the interlingual representations in multilingual LLMs. Our results indicate that training exclusively on a single language disrupts the alignment in early layers, while freezing these layers preserves the alignment of interlingual representations, leading to improved cross-lingual generalization. These results validate our framework and metric for evaluating interlingual representation, and further underscore that interlingual alignment is crucial for scalable multilingual learning.

## 01-052 | Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs
- arXiv: 2504.09378  first public: 2025-04-13  latest: 2026-01-29  primary cat: cs.CL
- authors (4): Kartik Ravisankar; Hyojung Han; Sarah Wiegreffe; Marine Carpuat
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- pages: 19

ABSTRACT: Large language models (LLMs) can answer prompts in many languages, despite being trained predominantly on English; yet, the mechanisms driving this generalization remain poorly understood. This work asks: How does an LLM's ability to align representations of non-English inputs to English impact its performance on natural language understanding (NLU) tasks? We study the role of representation alignment in instance-level task decisions, complementing prior analyses conducted both at the language level and task-independently. We introduce the Discriminative Alignment Index ($\DALI$) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks. Results show that incorrect NLU predictions are strongly associated with lower representation alignment with English in the model's middle layers. Through activation patching, we show that incorrect predictions in languages other than English can be fixed by patching their parallel English activations in the middle layers, thereby demonstrating the causal role of representation (mis)alignment in cross-lingual correctness.

## 01-054 | When Meanings Meet: Investigating the Emergence and Quality of Shared Concept Spaces during Multilingual Language Model Training
- arXiv: 2601.22851  first public: 2026-01-30  latest: 2026-01-30  primary cat: cs.CL
- authors (4): Felicia Körner; Max Müller-Eberstein; Anna Korhonen; Barbara Plank
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted to EACL 2026 Main Conference
- URLs on first pages of PDF: https://github.com/mainlp/
- pages: 21

ABSTRACT: Training Large Language Models (LLMs) with high multilingual coverage is becoming increasingly important -- especially when monolingual resources are scarce. Recent studies have found that LLMs process multilingual inputs in shared concept spaces, thought to support generalization and cross-lingual transfer. However, these prior studies often do not use causal methods, lack deeper error analysis or focus on the final model only, leaving open how these spaces emerge during training. We investigate the development of language-agnostic concept spaces during pretraining of EuroLLM through the causal interpretability method of activation patching. We isolate cross-lingual concept representations, then inject them into a translation prompt to investigate how consistently translations can be altered, independently of the language. We find that shared concept spaces emerge early} and continue to refine, but that alignment with them is language-dependent}. Furthermore, in contrast to prior work, our fine-grained manual analysis reveals that some apparent gains in translation quality reflect shifts in behavior -- like selecting senses for polysemous words or translating instead of copying cross-lingual homographs -- rather than improved translation ability. Our findings offer new insight into the training dynamics of cross-lingual alignment and the conditions under which causal interpretability methods offer meaningful insights in multilingual contexts.

## 01-057 | Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer
- arXiv: 2503.17456  first public: 2025-03-21  latest: 2025-03-21  primary cat: cs.CL
- authors (4): Soumen Kumar Mondal; Sayambhu Sen; Abhishek Singhania; Preethi Jyothi
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted (oral) at NAACL 2025 (InsightsNLP)
- pages: 17

ABSTRACT: Multilingual large language models (LLMs) aim towards robust natural language understanding across diverse languages, yet their performance significantly degrades on low-resource languages. This work explores whether existing techniques to identify language-specific neurons can be leveraged to enhance cross-lingual task performance of lowresource languages. We conduct detailed experiments covering existing language-specific neuron identification techniques (such as Language Activation Probability Entropy and activation probability-based thresholding) and neuron-specific LoRA fine-tuning with models like Llama 3.1 and Mistral Nemo. We find that such neuron-specific interventions are insufficient to yield cross-lingual improvements on downstream tasks (XNLI, XQuAD) in lowresource languages. This study highlights the challenges in achieving cross-lingual generalization and provides critical insights for multilingual LLMs.

## 01-058 | On the limited utility of parallel data for learning shared multilingual representations
- arXiv: 2603.29026  first public: 2026-03-30  latest: 2026-03-30  primary cat: cs.CL
- authors (2): Julius Leino; Jörg Tiedemann
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- pages: 13

ABSTRACT: Shared multilingual representations are essential for cross-lingual tasks and knowledge transfer across languages. This study looks at the impact of parallel data, i.e. translated sentences, in pretraining as a signal to trigger representations that are aligned across languages. We train reference models with different proportions of parallel data and show that parallel data seem to have only a minimal effect on the cross-lingual alignment. Based on multiple evaluation methods, we find that the effect is limited to potentially accelerating the representation sharing in the early phases of pretraining, and to decreasing the amount of language-specific neurons in the model. Cross-lingual alignment seems to emerge on similar levels even without the explicit signal from parallel data.

## 01-059 | Lingua Franca or Probing Artifact? Rethinking Latent Language in Multilingual LLMs
- arXiv: 2609.00155  first public: 2026-08-31  latest: 2026-08-31  primary cat: cs.CL
- authors (3): Deniz Bayazit; Badr AlKhamissi; Antoine Bosselut
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- arXiv comment: Accepted to EMNLP 2026 Findings
- URLs on first pages of PDF: https://github.com/bayazitdeniz/latent-lid
- pages: 21

ABSTRACT: Latent language identification is often used to argue that multilingual language models route computation through language-specific states, such as English pivots. However, existing probes infer latent language from different signals, such as the geometry of hidden states or what can be decoded from intermediate representations. Since such claims shape conclusions about how models share and route information across languages, we ask whether these probes measure the same phenomenon or expose distinct aspects of multilingual computation. We study this question across model families, training regimes, domains, tasks, checkpoints, and up to 27 languages. We find that identification probes systematically disagree: the GMM-based representation probe, which draws evidence from hidden state geometry, shows earlier cross-lingual mixing, whereas decoding-based probes, which rely on output-space decodability, retain sharper language-specific and more English-biased signals. These differences track model multilinguality and training progression, but are comparatively stable across domains. Our results suggest a more cautious interpretation of latent language identification, where current probes expose different aspects of multilingual processing, rather than directly revealing a single internal lingua franca.

## 01-060 | Scaling Laws for Forgetting When Fine-Tuning Large Language Models
- arXiv: 2401.05605  first public: 2024-01-11  latest: 2024-01-11  primary cat: cs.CL
- authors (1): Damjan Kalajdzievski
- seed subtopic: 迁移学习与灾难性遗忘; type: 原始研究; cross: []
- pages: 17

ABSTRACT: We study and quantify the problem of forgetting when fine-tuning pre-trained large language models (LLMs) on a downstream task. We find that parameter-efficient fine-tuning (PEFT) strategies, such as Low-Rank Adapters (LoRA), still suffer from catastrophic forgetting. In particular, we identify a strong inverse linear relationship between the fine-tuning performance and the amount of forgetting when fine-tuning LLMs with LoRA. We further obtain precise scaling laws that show forgetting increases as a shifted power law in the number of parameters fine-tuned and the number of update steps. We also examine the impact of forgetting on knowledge, reasoning, and the safety guardrails trained into Llama 2 7B chat. Our study suggests that forgetting cannot be avoided through early stopping or by varying the number of parameters fine-tuned. We believe this opens up an important safety-critical direction for future research to evaluate and develop fine-tuning schemes which mitigate forgetting

## 01-061 | Spurious Forgetting in Continual Learning of Language Models
- arXiv: 2501.13453  first public: 2025-01-23  latest: 2025-01-23  primary cat: cs.LG
- authors (4): Junhao Zheng; Xidi Cai; Shengjie Qiu; Qianli Ma
- seed subtopic: 迁移学习与灾难性遗忘; type: 原始研究; cross: []
- arXiv comment: ICLR2025
- URLs on first pages of PDF: https://github.com/zzz47zzz/spurious-forgetting
- pages: 66

ABSTRACT: Recent advancements in large language models (LLMs) reveal a perplexing phenomenon in continual learning: despite extensive training, models experience significant performance declines, raising questions about task alignment and underlying knowledge retention. This study first explores the concept of "spurious forgetting", proposing that such performance drops often reflect a decline in task alignment rather than true knowledge loss. Through controlled experiments with a synthesized dataset, we investigate the dynamics of model performance during the initial training phases of new tasks, discovering that early optimization steps can disrupt previously established task alignments. Our theoretical analysis connects these shifts to orthogonal updates in model weights, providing a robust framework for understanding this behavior. Ultimately, we introduce a Freezing strategy that fix the bottom layers of the model, leading to substantial improvements in four continual learning scenarios. Our findings underscore the critical distinction between task alignment and knowledge retention, paving the way for more effective strategies in continual learning.

## 01-062 | Continual Learning of Large Language Models: A Comprehensive Survey
- arXiv: 2404.16789  first public: 2024-04-25  latest: 2024-11-25  primary cat: cs.LG
- authors (9): Haizhou Shi; Zihao Xu; Hengyi Wang; Weiyi Qin; Wenyuan Wang; Yibin Wang ...
- seed subtopic: 迁移学习与灾难性遗忘; type: 综述; cross: ['07']
- arXiv comment: 44 pages, 2 figures, 4 tables; Work in progress
- URLs on first pages of PDF: https://github.com/Wang-ML-Lab/llm-continual-
- pages: 44

ABSTRACT: The recent success of large language models (LLMs) trained on static, pre-collected, general datasets has sparked numerous research directions and applications. One such direction addresses the non-trivial challenge of integrating pre-trained LLMs into dynamic data distributions, task structures, and user preferences. Pre-trained LLMs, when tailored for specific needs, often experience significant performance degradation in previous knowledge domains -- a phenomenon known as "catastrophic forgetting". While extensively studied in the continual learning (CL) community, it presents new manifestations in the realm of LLMs. In this survey, we provide a comprehensive overview of the current research progress on LLMs within the context of CL. This survey is structured into four main sections: we first describe an overview of continually learning LLMs, consisting of two directions of continuity: vertical continuity (or vertical continual learning), i.e., continual adaptation from general to specific capabilities, and horizontal continuity (or horizontal continual learning), i.e., continual adaptation across time and domains (Section 3). We then summarize three stages of learning LLMs in the context of modern CL: Continual Pre-Training (CPT), Domain-Adaptive Pre-training (DAP), and Continual Fine-Tuning (CFT) (Section 4). Then we provide an overview of evaluation protocols for continual learning with LLMs, along with the current available data sources (Section 5). Finally, we discuss intriguing questions pertaining to continual learning for LLMs (Section 6). The full list of papers examined in this survey is available at https://github.com/Wang-ML-Lab/llm-continual-learning-survey.

## 01-063 | Can Scale Save Us From Plasticity Loss in Large Language Models?
- arXiv: 2606.24752  first public: 2026-06-23  latest: 2026-06-23  primary cat: cs.AI
- authors (3): J. Fernando Hernandez-Garcia; Tomás Figliolia; Beren Millidge
- seed subtopic: 迁移学习与灾难性遗忘; type: 原始研究; cross: []
- pages: 17

ABSTRACT: The loss of plasticity - the ability of a network to learn new information after having already learned older information - is a fundamental challenge in creating artificial neural networks capable of continual learning. Although this phenomenon has been known for decades, it has mostly been studied in older, relatively small architectures and rarely in natural-language domains. To determine whether loss of plasticity remains a problem in the modern transformer-based LLM paradigm, we study plasticity loss in GPT-style Transformer models trained on a multilingual continual learning problem. Consistent with prior work, we find evidence of plasticity loss across models ranging from 5M to 314M non-embedding parameters, as measured by deterioration on a held-out Vietnamese probing task. We further find that the onset of plasticity loss follows a predictable scaling law, growing sublinearly with model size. These results suggest that larger models may delay the measurable effects of plasticity loss, but that increasing parameter count alone is likely to be insufficient to completely prevent it. We also find evidence of plasticity loss under stationary multilingual training, challenging the view that the phenomenon is exclusive to continual learning with abrupt task changes. Overall, our results suggest that even large Transformer language models trained on natural-language will eventually lose the ability to efficiently adapt to new data after sufficiently long training, in both continual and stationary settings.

## 01-064 | Revisiting Catastrophic Forgetting in Large Language Model Tuning
- arXiv: 2406.04836  first public: 2024-06-07  latest: 2024-06-07  primary cat: cs.CL
- authors (4): Hongyu Li; Liang Ding; Meng Fang; Dacheng Tao
- seed subtopic: 迁移学习与灾难性遗忘; type: 原始研究; cross: []
- pages: 12

ABSTRACT: Catastrophic Forgetting (CF) means models forgetting previously acquired knowledge when learning new data. It compromises the effectiveness of large language models (LLMs) during fine-tuning, yet the underlying causes have not been thoroughly investigated. This paper takes the first step to reveal the direct link between the flatness of the model loss landscape and the extent of CF in the field of LLMs. Based on this, we introduce the sharpness-aware minimization to mitigate CF by flattening the loss landscape. Experiments on three widely-used fine-tuning datasets, spanning different model scales, demonstrate the effectiveness of our method in alleviating CF. Analyses show that we nicely complement the existing anti-forgetting strategies, further enhancing the resistance of LLMs to CF.

## 01-066 | On the Calibration of Multilingual Question Answering LLMs
- arXiv: 2311.08669  first public: 2023-11-15  latest: 2024-04-15  primary cat: cs.CL
- authors (4): Yahan Yang; Soham Dan; Dan Roth; Insup Lee
- seed subtopic: 不确定性与校准; type: 原始研究; cross: []
- arXiv comment: Preprint. Under Submission
- pages: 17

ABSTRACT: Multilingual pre-trained Large Language Models (LLMs) are incredibly effective at Question Answering (QA), a core task in Natural Language Understanding, achieving high accuracies on several multilingual benchmarks. However, little is known about how well their confidences are calibrated. In this paper, we comprehensively benchmark the calibration of several multilingual LLMs (MLLMs) on a variety of QA tasks. We perform extensive experiments, spanning encoder-only, encoder-decoder, and decoder-only QA models (size varying from 110M to 7B parameters) and diverse languages, including both high- and low-resource ones. We study different dimensions of calibration in in-distribution, out-of-distribution, and cross-lingual transfer settings, and investigate strategies to improve it, including post-hoc methods and regularized fine-tuning. For decoder-only LLMs such as LlaMa2, we additionally find that in-context learning improves confidence calibration on multilingual data. We also conduct several ablation experiments to study the effect of language distances, language corpus size, and model size on calibration, and how multilingual models compare with their monolingual counterparts for diverse tasks and languages. Our experiments suggest that the multilingual QA models are poorly calibrated for languages other than English and incorporating a small set of cheaply translated multilingual samples during fine-tuning/calibration effectively enhances the calibration performance.

## 01-067 | A Survey of Confidence Estimation and Calibration in Large Language Models
- arXiv: 2311.08298  first public: 2023-11-14  latest: 2024-03-25  primary cat: cs.CL
- authors (6): Jiahui Geng; Fengyu Cai; Yuxia Wang; Heinz Koeppl; Preslav Nakov; Iryna Gurevych
- seed subtopic: 不确定性与校准; type: 综述; cross: []
- arXiv comment: 16 pages, 1 page, 1 table
- pages: 18

ABSTRACT: Large language models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks in various domains. Despite their impressive performance, they can be unreliable due to factual errors in their generations. Assessing their confidence and calibrating them across different tasks can help mitigate risks and enable LLMs to produce better generations. There has been a lot of recent research aiming to address this, but there has been no comprehensive overview to organize it and outline the main lessons learned. The present survey aims to bridge this gap. In particular, we outline the challenges and we summarize recent technical advancements for LLM confidence estimation and calibration. We further discuss their applications and suggest promising directions for future work.

## 01-068 | A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions
- arXiv: 2412.05563  first public: 2024-12-07  latest: 2025-07-01  primary cat: cs.CL
- authors (5): Ola Shorinwa; Zhiting Mei; Justin Lidard; Allen Z. Ren; Anirudha Majumdar
- seed subtopic: 不确定性与校准; type: 综述; cross: []
- pages: 35

ABSTRACT: The remarkable performance of large language models (LLMs) in content generation, coding, and common-sense reasoning has spurred widespread integration into many facets of society. However, integration of LLMs raises valid questions on their reliability and trustworthiness, given their propensity to generate hallucinations: plausible, factually-incorrect responses, which are expressed with striking confidence. Previous work has shown that hallucinations and other non-factual responses generated by LLMs can be detected by examining the uncertainty of the LLM in its response to the pertinent prompt, driving significant research efforts devoted to quantifying the uncertainty of LLMs. This survey seeks to provide an extensive review of existing uncertainty quantification methods for LLMs, identifying their salient features, along with their strengths and weaknesses. We present existing methods within a relevant taxonomy, unifying ostensibly disparate methods to aid understanding of the state of the art. Furthermore, we highlight applications of uncertainty quantification methods for LLMs, spanning chatbot and textual applications to embodied artificial intelligence applications in robotics. We conclude with open research challenges in uncertainty quantification of LLMs, seeking to motivate future research.

## 01-069 | There is No Theoretical Curse of Multilinguality For Embedding Space Structure
- arXiv: 2608.17088  first public: 2026-08-17  latest: 2026-09-07  primary cat: cs.CL
- authors (5): Niyati Bafna; Neha Verma; Vilém Zouhar; Philipp Koehn; David Yarowsky
- seed subtopic: 表示几何与跨语言对齐; type: 原始研究; cross: []
- pages: 23

ABSTRACT: A central goal of multilingual NLP is to achieve high monolingual performance per language and cross-lingual alignment for large-scale language coverage with a multilingual model. The curse of multilinguality describes the phenomenon of degradation in multilingual model performance as we increase language coverage, posing a threat to the above goal. This paper asks whether multilingual embedding spaces are inherently incapable of achieving perfect multilinguality without a prohibitive increase in required capacity. We first formalize the goal of "perfect multilinguality", embodied in two multilinguality conditions. We then prove that the minimum dimensionality required for perfect multilinguality grows only logarithmically in the number of languages. That is, we show that there is no theoretical curse of multilinguality for embedding space structure. This suggests that the empirical curse of multilinguality is a result of real world data and training conditions. We back this understanding with a small-scale empirical study. Our paper provides the first theoretical and intrinsic perspective on the curse of multilinguality.
