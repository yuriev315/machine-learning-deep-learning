#!/usr/bin/env python3
"""Concatenate per-category search logs (scripts/work/search_log_NN_cn.md) into search_log_cn.md.
  python3 -I scripts/merge_logs_en.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
parts = sorted((ROOT / "scripts" / "work").glob("search_log_*_cn.md"))
head = ("# 检索日志（汇总）\n\n检索日：2026-10-29（UTC）。近三年窗口：首次公开日期 ≥ 2023-10-29。"
        "以下按类别原样合并各类检索记录（查询式、返回数、选入/排除原因、替代关系）；"
        "原始分文件在 `scripts/work/`。主要检索源：arXiv API（export.arxiv.org，限速 5 s/次，与本机其他资料库共享限速队列）、"
        "ACL Anthology、课程官方主页、作者/出版社官方页面、GitHub。\n")
body = [head]
for p in parts:
    body.append(f"\n\n---\n\n<!-- 来源：scripts/work/{p.name} -->\n\n" + p.read_text("utf-8").strip() + "\n")
(ROOT / "search_log_cn.md").write_text("".join(body), "utf-8")
print(f"merged {len(parts)} logs")
