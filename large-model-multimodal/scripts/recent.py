#!/usr/bin/env python3
"""Pick recent (2026-01-01 .. 2026-10-31) arXiv papers per domain by Hugging Face Papers upvotes.

usage: python3 -I recent.py <exclude_ids.txt> <out.json> [per_domain]
"""
import json, sys, time, urllib.request, urllib.parse, re
Q = {
 '01': ['scaling law language model', 'mixture of experts language model', 'tokenizer language model', 'linear attention transformer', 'long context language model architecture', 'state space model language'],
 '02': ['pretraining data curation', 'data mixture pretraining', 'synthetic data pretraining', 'web corpus dataset language model', 'data filtering pretraining'],
 '03': ['preference optimization alignment', 'reinforcement learning from human feedback', 'reward model', 'instruction tuning', 'supervised fine-tuning language model', 'RLVR'],
 '04': ['reasoning language model reinforcement learning', 'test-time scaling', 'chain of thought reasoning', 'mathematical reasoning LLM', 'long chain-of-thought'],
 '05': ['retrieval augmented generation', 'RAG', 'deep research agent retrieval', 'knowledge graph LLM', 'embedding model retrieval'],
 '06': ['LLM agent', 'agentic', 'tool use language model', 'GUI agent', 'software engineering agent', 'multi-agent'],
 '07': ['vision language model', 'multimodal large language model', 'visual reasoning MLLM', 'vision encoder', 'unified multimodal model'],
 '08': ['text-to-image diffusion', 'video generation', 'image editing diffusion', 'flow matching generation', 'autoregressive image generation'],
 '09': ['speech language model', 'text-to-speech', 'speech recognition', 'audio language model', 'spoken dialogue model', 'music generation'],
 '10': ['vision-language-action', 'embodied agent', 'robot foundation model', 'video understanding', 'world model', 'long video'],
 '11': ['quantization LLM', 'speculative decoding', 'KV cache compression', 'LLM inference serving', 'efficient training large language model', 'sparse attention'],
 '12': ['LLM benchmark', 'LLM evaluation', 'jailbreak', 'hallucination', 'AI safety language model', 'LLM-as-a-judge'],
}
excl = set(open(sys.argv[1]).read().split()); out = sys.argv[2]; per = int(sys.argv[3]) if len(sys.argv) > 3 else 9
res = {}; taken = set(excl)
for dom, qs in Q.items():
    cand = {}
    for q in qs:
        u = 'https://huggingface.co/api/papers/search?limit=120&q=' + urllib.parse.quote(q)
        for a in range(4):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'literature-archive/1.0'}), timeout=60)); break
            except Exception:
                time.sleep(15 * (a + 1))
        else: continue
        for w in d:
            p = w.get('paper', w); pid = p.get('id', ''); dt = (p.get('publishedAt') or '')[:10]
            if not re.match(r'^\d{4}\.\d{4,5}$', pid) or not ('2026-01-01' <= dt <= '2026-10-31'): continue
            cand[pid] = dict(id=pid, title=' '.join((p.get('title') or '').split()), upvotes=p.get('upvotes') or 0, date=dt, query=q)
        time.sleep(1.0)
    pick = [c for c in sorted(cand.values(), key=lambda c: -c['upvotes']) if c['id'] not in taken][:per]
    for c in pick: taken.add(c['id'])
    res[dom] = pick
    print(dom, len(cand), [(c['id'], c['upvotes']) for c in pick], flush=True)
json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
