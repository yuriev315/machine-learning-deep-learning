#!/usr/bin/env python3
"""Append the HTML-only books to scripts/seeds/C12_books_cn.json.

For each book, the official table of contents page is fetched and every chapter link is taken in
order of first appearance (filtered by a per-book pattern), so the saved package equals the
official TOC. The TOC page itself is included as the first page. Run after
build_book_manifest_en.py (which keeps entries with format == "html").

Usage: python3 -I scripts/build_html_manifest_en.py
"""
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import SCRIPTS, http  # noqa: E402

BOOKS = [
    dict(id="MLB055", file_stem="Goodfellow_DeepLearning_2016_html_en", title="Deep Learning",
         authors="Ian Goodfellow; Yoshua Bengio; Aaron Courville", edition="MIT Press 2016；官网 HTML 版",
         orig_year=2016, edition_year=2016, publisher="MIT Press", toc="https://www.deeplearningbook.org/",
         pattern=r'href="(contents/[a-z_\-]+\.html)"', title_phrase="Deep Learning", min_chars_per_page=300,
         source_page="https://www.deeplearningbook.org/", cats=["C12", "C04", "C03", "C07"],
         prereq="线性代数、概率、微积分", stage="进阶", difficulty="中级", priority="高",
         reason="深度学习经典教材：数学基础、前馈/卷积/循环网络、正则化与优化、表示学习与生成模型",
         old_reason="2016 年出版，深度学习最常被引用的系统教材；出版社协议仅允许官网 HTML 形式",
         license_note="作者官网免费 HTML（出版社协议不提供 PDF）",
         toc_note="官网首页目录列出的全部章节、前言、记号、参考文献与索引页面；分部标题页较短，故每页最少正文阈值设为 300 字符"),
    dict(id="MLB056", file_stem="Nielsen_NeuralNetworksDeepLearning_2019_html_en", title="Neural Networks and Deep Learning",
         authors="Michael A. Nielsen", edition="Determination Press 2015；官网 HTML 版（2019-12 更新）",
         orig_year=2015, edition_year=2019, publisher="Determination Press", toc="http://neuralnetworksanddeeplearning.com/",
         pattern=r'href="((?:chap[0-9]+|sai|about|exercises_and_problems)\.html)"', title_phrase="Neural Networks and Deep Learning",
         min_chars_per_page=1500, source_page="http://neuralnetworksanddeeplearning.com/", cats=["C12", "C04"],
         prereq="微积分、线性代数、Python", stage="入门", difficulty="入门", priority="中",
         reason="从感知机到反向传播、训练技巧与卷积网络的入门在线书",
         old_reason="经典入门读物，作者官网仅以 HTML 形式发布；用于建立反向传播直觉",
         license_note="作者官网免费 HTML（CC BY-NC 3.0）",
         toc_note="首页目录：6 章 + 附录（sai）+ 说明页（about、exercises_and_problems）"),
    dict(id="MLB057", file_stem="Molnar_InterpretableMachineLearning_3rdEd_html_en", title="Interpretable Machine Learning: A Guide for Making Black Box Models Explainable",
         authors="Christoph Molnar", edition="第 3 版（官网 HTML）", orig_year=2019, edition_year="",
         publisher="自出版（Leanpub/官网）", toc="https://christophm.github.io/interpretable-ml-book/",
         pattern=r'href="(?:\./)?([a-z0-9_\-]+\.html)"', title_phrase="Interpretable Machine Learning",
         min_chars_per_page=800, source_page="https://christophm.github.io/interpretable-ml-book/", cats=["C12", "C10"],
         prereq="机器学习基础", stage="进阶", difficulty="中级", priority="高",
         reason="可解释机器学习标准参考：可解释模型、PDP/ALE、LIME、SHAP、反事实、神经网络解释",
         old_reason="官网第 3 版页面未标注发布日期（待核实）；保留理由：可解释性方向最常用的系统参考书", license_note="作者官网免费 HTML（CC BY-NC-SA 4.0）",
         toc_note="官网侧栏目录中的全部章节页面（去重、按出现顺序）；参考文献等短页阈值 800 字符"),
    dict(id="MLB058", file_stem="Torralba_FoundationsOfComputerVision_2024_html_en", title="Foundations of Computer Vision",
         authors="Antonio Torralba; Phillip Isola; William T. Freeman", edition="MIT Press 2024；官网 HTML 版",
         orig_year=2024, edition_year=2024, publisher="MIT Press", toc="https://visionbook.mit.edu/",
         pattern=r'href="(?:\./)?([a-z0-9_\-]+\.html)"', title_phrase="Foundations of Computer Vision",
         min_chars_per_page=500, source_page="https://visionbook.mit.edu/", cats=["C12", "C05", "C04", "C07"],
         prereq="线性代数、概率、基础机器学习", stage="进阶", difficulty="中级", priority="高",
         reason="MIT 计算机视觉新教材：成像、信号处理、学习、表示、生成模型、三维与运动",
         old_reason="", license_note="作者官网免费 HTML（MIT Press 开放网页版）",
         toc_note="官网首页目录中的全部章节页面（去重、按出现顺序）；各\"部分\"标题页（part_*）与版权页正文仅 600–1400 字符，故阈值设为 500 字符"),
    dict(id="MLB059", file_stem="Bellemare_DistributionalReinforcementLearning_2023_html_en", title="Distributional Reinforcement Learning",
         authors="Marc G. Bellemare; Will Dabney; Mark Rowland", edition="MIT Press 2023；官网 HTML 草稿版",
         orig_year=2023, edition_year=2023, publisher="MIT Press", toc="https://www.distributional-rl.org/",
         pattern=r"href='(/contents/[a-z0-9_\-]+)'", title_phrase="Distributional Reinforcement Learning",
         min_chars_per_page=1500, source_page="https://www.distributional-rl.org/", cats=["C12", "C09"],
         prereq="强化学习基础、概率论", stage="研究", difficulty="高级", priority="低",
         reason="分布式强化学习的系统专著：回报分布、分布式动态规划与 TD、函数逼近、深度 RL",
         old_reason="2023 年出版（早于窗口起点）；出版社协议只允许网页版草稿，不提供 PDF",
         license_note="作者官网 HTML 草稿（出版社协议不提供 PDF）",
         toc_note="官网目录：前言、目录、第 1–11 章、记号、参考文献"),
]


def main():
    path = SCRIPTS / "seeds/C12_books_cn.json"
    entries = [e for e in json.loads(path.read_text()) if e.get("format") != "html"]
    for b in BOOKS:
        st, body, final, _ = http(b["toc"], accept="text/html")
        if st != 200:
            print("TOC fetch failed", b["id"], st)
            continue
        html = body.decode("utf-8", "replace")
        seen, files = set(), [{"url": final, "label": "toc"}]
        for m in re.finditer(b["pattern"], html):
            u = urllib.parse.urljoin(final, m.group(1))
            if u.rstrip("/") == final.rstrip("/") or u.endswith("/index.html") or u in seen:
                continue
            seen.add(u)
            files.append({"url": u, "label": re.sub(r"\.html$", "", u.rsplit("/", 1)[-1])})
        e = {k: v for k, v in b.items() if k not in ("toc", "pattern", "toc_note")}
        e.update(type="book", lang="en", format="html", files=files, min_pages=0, span_hosts=False,
                 toc_check=f"{b['toc_note']}；目录页 {b['toc']} 解析得到 {len(files) - 1} 个正文页面 + 目录页")
        entries.append(e)
        print(b["id"], len(files), "pages")
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
