#!/usr/bin/env python3
"""Assign a paper to one of the 12 paper domains from its arXiv title, abstract and categories.

Title hits weigh 3, abstract hits 1; ties go to the earlier rule in RULES order of specificity.
usage (module): from classify import domain
"""
import re
RULES = [
 ('09', r'speech|audio|asr\b|tts\b|text-to-speech|spoken|voice|music|sound|acoustic|speaker|codec'),
 ('10', r'robot|embodied|vision-language-action|\bvla\b|manipulation|navigation|driving|world model|video understanding|long video|video question|video-language|video llm|video large|egocentric|action recognition|humanoid|policy learning'),
 ('08', r'diffusion|text-to-image|image generation|video generation|text-to-video|image editing|flow matching|rectified flow|generative adversarial|gan\b|image synthesis|autoregressive image|visual generation|controlnet|inpainting|3d generation'),
 ('07', r'vision-language|visual instruction|multimodal large language|\bmllm|\bvlm|image-text|visual question|vision encoder|clip\b|multimodal|visual reasoning|ocr|document understanding|chart|grounding'),
 ('06', r'\bagent|agentic|tool use|tool-use|tool learning|tool calling|function calling|web navigation|gui\b|computer use|software engineering|swe-bench|multi-agent|planning'),
 ('05', r'retrieval|\brag\b|knowledge graph|search engine|dense retriev|embedding model|question answering over|citation|long-term memory|memory'),
 ('12', r'benchmark|evaluation|evaluating|jailbreak|safety|red[- ]teaming|hallucination|bias|fairness|privacy|contamination|llm-as-a-judge|judge|truthful|toxicity|watermark|adversarial attack|uncertainty|trustworth|interpretab|unlearning|misalignment'),
 ('11', r'quantiz|pruning|sparsit|distillation|speculative|kv cache|kv-cache|inference|serving|throughput|latency|memory-efficient|efficient training|parallelism|flashattention|kernel|compress|low-bit|on-device|edge device|deployment'),
 ('04', r'reasoning|chain-of-thought|chain of thought|test-time|math|theorem|verifier|process reward|self-consistency|o1\b|r1\b|thinking'),
 ('03', r'alignment|preference|rlhf|reward model|instruction tuning|instruction-tuning|fine-tun|finetun|dpo\b|ppo\b|grpo|reinforcement learning from|post-training|sft\b|lora'),
 ('02', r'pretraining data|pre-training data|data curation|data mixture|data selection|dataset|corpus|deduplicat|synthetic data|data quality|tokeniz|web data|filtering'),
 ('01', r'transformer|attention|scaling law|language model|architecture|mixture of experts|mixture-of-experts|state space|positional|long context|context length|pretraining|pre-training|foundation model'),
]
def domain(title, abstract='', cats=()):
    t = title.lower(); a = abstract.lower(); score = {}
    for i, (d, pat) in enumerate(RULES):
        s = 3 * len(re.findall(pat, t)) + len(re.findall(pat, a)) * 0.5
        if d == '01': s *= 0.4
        if s: score[d] = (s, -i)
    if not score:
        if any(c.startswith(('eess.AS', 'cs.SD')) for c in cats): return '09'
        if any(c.startswith('cs.RO') for c in cats): return '10'
        if any(c.startswith('cs.CV') for c in cats): return '07'
        return '01'
    return max(score, key=lambda d: score[d])
