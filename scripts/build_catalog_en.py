#!/usr/bin/env python3
"""Build the library's registers from the caches and manifests.

Inputs : cache/papers_resolved_en.json, cache/download_papers_en.json, annotations/*_cn.json,
         seeds/C11_courses_cn.json, seeds/C12_books_cn.json, cache/materials_results_en.json,
         seeds/manual_failures_cn.json
Outputs: catalog_cn.csv (UTF-8 with BOM; verified items only), download_failures_cn.csv,
         checksums_en.sha256 (every verified file, relative paths), domains/Cxx_*_cn.md,
         cache/stats_en.json (counts used by the report).
Only items whose full text was downloaded and verified are written to the catalog.

Usage: python3 -I scripts/build_catalog_en.py
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CACHE, CATS, ROOT, SCRIPTS, WINDOW_START, load, window_status  # noqa: E402

KIND = {"R": "原始研究论文", "S": "综述", "T": "教程/讲义式文章"}
COLS = ["文献编号", "主分类", "交叉分类", "资料类型", "标题", "作者或教师", "学校或机构", "发表渠道或出版社",
        "渠道依据", "首次公开日期", "日期精度", "首次公开日期依据", "正式发表日期", "版本", "版本日期", "时间窗口",
        "三年前保留理由", "DOI/arXiv ID/ISBN", "原始来源链接", "下载链接", "语言", "文件格式", "本地路径",
        "全文完整性", "核验状态", "SHA256", "选入理由", "问题", "主要方法", "评测范围", "简介", "简介依据",
        "课程名称", "课程代码", "学期", "先修要求", "内容覆盖", "章节完整性", "适合阅读阶段", "阅读难度", "优先级",
        "关联资料"]


def catname(c):
    return f"{c} {CATS.get(c, '')}"


def venue(p):
    s2 = p.get("s2") or {}
    v = s2.get("venue_full") or s2.get("venue") or s2.get("journal") or ""
    if v and v.lower() not in ("arxiv.org", "arxiv", "arxiv (cornell university)"):
        return v, "Semantic Scholar 元数据（未逐篇核对官方论文集）"
    if p.get("journal_ref"):
        return p["journal_ref"], "arXiv journal_ref（作者自填）"
    m = re.search(r"(accepted|published|to appear)[^.;]*", p.get("arxiv_comment") or "", re.I)
    if m:
        return "arXiv comments：" + m.group(0)[:120], "arXiv comments（作者自述，未核实）"
    c = p.get("crossref") or {}
    if c.get("container"):
        return c["container"], "Crossref DOI 元数据"
    return "arXiv 预印本", "未发现正式发表信息（未核实是否已发表）"


def paper_rows(ann):
    recs = load(CACHE / "papers_resolved_en.json", {})
    dl = load(CACHE / "download_papers_en.json", {})
    over = load(SCRIPTS / "seeds/paper_pdf_overrides_cn.json", {})
    rows, fails = [], []
    for pid, p in sorted(recs.items()):
        d = dl.get(pid, {})
        if d.get("status") != "ok" or not (ROOT / d["local_path"]).exists():
            fails.append({"编号": pid, "分类": p["primary"], "类型": "论文", "标题": p["title"],
                          "尝试来源": "; ".join(t.get("url", "") for t in d.get("tries", [])) or "未尝试",
                          "失败原因": d.get("reason", "尚未下载（待续跑）"), "处理": "不计数；见续跑命令或替代检索"})
            continue
        a = ann.get(pid, {})
        v, vsrc = venue(p)
        ids = []
        if p.get("arxiv"):
            ids.append("arXiv:" + p["arxiv"])
        if p.get("doi"):
            ids.append("DOI:" + p["doi"])
        src = f"https://arxiv.org/abs/{p['arxiv']}" if p.get("arxiv") else f"https://doi.org/{p['doi']}"
        s2d = (p.get("s2") or {}).get("date") or ""
        ver = d.get("version_label", "")
        if not p.get("arxiv"):
            ver = over.get(p["key"], {}).get("version_label", ver)
        letters_ok = (d.get("ascii_letter_ratio") or 1) >= 0.8
        rows.append({
            "文献编号": pid, "主分类": catname(p["primary"]),
            "交叉分类": "; ".join(catname(c) for c in p["cats"][1:]), "资料类型": KIND.get(p["kind"], p["kind"]),
            "标题": p["title"], "作者或教师": "; ".join(p["authors"]), "学校或机构": "未登记（论文作者单位不在登记范围）",
            "发表渠道或出版社": v, "渠道依据": vsrc,
            "首次公开日期": p["first_public"], "日期精度": {10: "日", 7: "月", 4: "年"}.get(len(p["first_public"]), "未知"),
            "首次公开日期依据": p["first_public_source"],
            "正式发表日期": (s2d + "（Semantic Scholar，未核实）") if s2d and s2d != p["first_public"] else "",
            "版本": ver, "版本日期": p.get("version_date", "") if p.get("arxiv") else "",
            "时间窗口": p["window"], "三年前保留理由": p["old_reason"] if p["window"] != "近三年" else "",
            "DOI/arXiv ID/ISBN": "; ".join(ids), "原始来源链接": src, "下载链接": d["pdf_url"],
            "语言": "英文" if letters_ok else "待核实", "文件格式": "PDF", "本地路径": d["local_path"],
            "全文完整性": f"完整论文全文 PDF（{d['pages']} 页）",
            "核验状态": f"通过：HTTP 200；%PDF 文件头；pypdf 可解析 {d['pages']} 页；前两页标题词匹配率 {d['title_match']}",
            "SHA256": d["sha256"], "选入理由": p["reason"],
            "问题": a.get("problem", ""), "主要方法": a.get("method", ""), "评测范围": a.get("evaluation", ""),
            "简介": a.get("summary", ""),
            "简介依据": "摘要（arXiv API 返回的摘要）；未读全文，未核实全文结论" if a else "待补充",
            "阅读难度": a.get("difficulty", ""), "优先级": a.get("priority", ""),
        })
    return rows, fails


def material_rows():
    res = load(CACHE / "materials_results_en.json", {})
    rows, fails, files = [], [], []
    for mf in ("C11_courses_cn.json", "C12_books_cn.json"):
        for e in load(SCRIPTS / "seeds" / mf, []):
            r = res.get(e["id"], {})
            if r.get("status") != "ok" or not (ROOT / r["local_path"]).exists():
                fails.append({"编号": e["id"], "分类": "C11" if e["type"] == "course" else "C12",
                              "类型": "课程资料" if e["type"] == "course" else "书籍", "标题": e["title"],
                              "尝试来源": "; ".join(f["url"] for f in e.get("files", [])) or e.get("arxiv", ""),
                              "失败原因": r.get("reason", "尚未下载（待续跑）"), "处理": "不计数"})
                continue
            files += r["files"]
            fmt = {"pdf": "PDF", "pdf_multi": f"PDF 资料包（{len(r['files'])} 个文件）",
                   "html": f"HTML 离线完整正文（{r.get('html_pages')} 个页面，含图片/样式）"}[e["format"]]
            if e["format"] == "html":
                complete = f"官方目录全部 {len(e['files'])} 个页面均下载并通过核验；{e.get('toc_check', '')}"
                check = f"通过：每页 HTTP 200、text/html、正文字符数 ≥ {e.get('min_chars_per_page', 2000)}；首页含书名"
            else:
                pages = r.get("total_pages")
                complete = (f"完整 PDF（{pages} 页）" if e["format"] == "pdf" else f"全部 {len(r['files'])} 个分册（共 {pages} 页）") \
                    + (f"；{e['toc_check']}" if e.get("toc_check") else "")
                check = f"通过：HTTP 200；%PDF；pypdf 可解析共 {pages} 页（≥ {e.get('min_pages')}）；前 8 页含书名/讲义名"
            ax = r.get("arxiv_info") or {}
            ey = str(e.get("edition_year") or "")
            if ax:
                ey = ax.get("updated", ey)
            first = str(e.get("orig_year") or "") or (ax.get("published", "") if ax else "")
            ids = []
            if e.get("arxiv"):
                ids.append("arXiv:" + e["arxiv"])
            if r.get("isbn_in_pdf"):
                ids.append("ISBN（PDF 版权页提取）:" + ", ".join(r["isbn_in_pdf"]))
            is_course = e["type"] == "course"
            term = e.get("term", "")
            if len(ey) >= 10:
                recent = "近三年" if ey[:10] >= WINDOW_START else "三年前（经典例外）"
            elif ey:
                recent = "近三年" if ey[:4] >= "2024" else ("待核实（年份精度不足）" if ey[:4] == "2023" else "三年前（经典例外）")
            else:
                recent = "待核实（无版本日期）"
            sha = r["files"][0]["sha256"] if len(r["files"]) == 1 else f"见 checksums_en.sha256（{len(r['files'])} 个文件）"
            urls = [f["url"] for f in e.get("files", [])]
            if ax:
                urls = ["https://arxiv.org/pdf/" + ax["latest_version"]]
            rows.append({
                "文献编号": e["id"], "主分类": catname("C11" if is_course else "C12"),
                "交叉分类": "; ".join(catname(c) for c in e.get("cats", []) if c not in ("C11", "C12") or
                                       (c == "C12" and is_course) or (c == "C11" and not is_course)),
                "资料类型": "大学课程讲义" if is_course else "教科书/专著/参考书", "标题": e["title"],
                "作者或教师": e.get("authors", ""), "学校或机构": e.get("institution", "") if is_course else "",
                "发表渠道或出版社": e.get("publisher", "") or (e.get("institution", "") + " 课程官网" if is_course else ""),
                "渠道依据": e.get("license_note", ""), "首次公开日期": first, "日期精度": "年" if len(first) == 4 else ("日" if len(first) == 10 else ""),
                "首次公开日期依据": "原著/首版年份（出版信息）" if not ax else "arXiv v1 提交日",
                "版本": (term if is_course else e.get("edition", "")) + (f"；arXiv {ax['latest_version']}" if ax else ""),
                "版本日期": ey, "时间窗口": recent, "三年前保留理由": e.get("old_reason", "") if recent != "近三年" else "",
                "DOI/arXiv ID/ISBN": "; ".join(ids), "原始来源链接": e.get("source_page", ""),
                "下载链接": urls[0] + (f" 等 {len(urls)} 个" if len(urls) > 1 else ""), "语言": "英文",
                "文件格式": fmt, "本地路径": r["local_path"], "全文完整性": complete, "核验状态": check, "SHA256": sha,
                "选入理由": e.get("reason", ""), "课程名称": e.get("course_name", ""), "课程代码": e.get("course_code", ""),
                "学期": term if is_course else "", "先修要求": e.get("prereq", ""), "内容覆盖": e.get("coverage", ""),
                "章节完整性": "" if is_course else complete, "适合阅读阶段": e.get("stage", ""),
                "阅读难度": e.get("difficulty", ""), "优先级": e.get("priority", ""), "关联资料": e.get("related", ""),
                "简介依据": "", "_cats": e.get("cats", []),
            })
    return rows, fails, files


def main():
    ann = {}
    for f in sorted((SCRIPTS / "annotations").glob("*_cn.json")):
        ann.update(json.loads(f.read_text()))
    prows, pfails = paper_rows(ann)
    mrows, mfails, mfiles = material_rows()
    manual = load(SCRIPTS / "seeds/manual_failures_cn.json", [])
    rows = prows + mrows

    with open(ROOT / "catalog_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    fcols = ["编号", "分类", "类型", "标题", "尝试来源", "失败原因", "处理"]
    with open(ROOT / "download_failures_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(pfails + mfails + manual)

    lines = [f"{r['SHA256']}  {r['本地路径']}" for r in prows]
    lines += [f"{x['sha256']}  {x['path']}" for x in mfiles]
    (ROOT / "checksums_en.sha256").write_text("\n".join(sorted(lines, key=lambda s: s[66:])) + "\n")

    # per-category pages: primary entries first, then cross-listed ones (same file, no copies)
    by_cat = defaultdict(lambda: {"primary": [], "cross": []})
    for r in rows:
        prim = r["主分类"][:3]
        by_cat[prim]["primary"].append(r)
        for c in re.findall(r"C\d\d", r["交叉分类"]):
            by_cat[c]["cross"].append(r)
    (ROOT / "domains").mkdir(exist_ok=True)
    for c, name in CATS.items():
        d = by_cat[c]
        out = [f"# {c} {name}", "", f"主分类收录 {len(d['primary'])} 份（已下载并核验）；另有 {len(d['cross'])} 份从其他类别交叉引用。",
               "文件只在 papers/、books/、university_materials/ 中各存一份，本页通过文献编号与相对路径引用。", "",
               "## 主分类资料", "", "| 编号 | 首次公开 | 窗口 | 类型 | 标题 | 本地文件 |", "|---|---|---|---|---|---|"]
        for r in sorted(d["primary"], key=lambda r: r["文献编号"]):
            out.append(f"| {r['文献编号']} | {r['首次公开日期']} | {r['时间窗口']} | {r['资料类型']} | "
                       f"{r['标题'].replace('|', '/')} | [链接](../{r['本地路径']}) |")
        out += ["", "## 交叉引用（主分类在其他类别）", "", "| 编号 | 主分类 | 标题 | 本地文件 |", "|---|---|---|---|"]
        for r in sorted(d["cross"], key=lambda r: r["文献编号"]):
            out.append(f"| {r['文献编号']} | {r['主分类']} | {r['标题'].replace('|', '/')} | [链接](../{r['本地路径']}) |")
        slug = {"C01": "ml_foundations", "C02": "traditional_ml", "C03": "unsupervised_representation",
                "C04": "dl_foundations_training", "C05": "computer_vision", "C06": "nlp_llm", "C07": "generative_models",
                "C08": "graph_ml", "C09": "rl_decision", "C10": "reliability_evaluation", "C11": "university_courses",
                "C12": "books"}[c]
        (ROOT / "domains" / f"{c}_{slug}_cn.md").write_text("\n".join(out) + "\n")

    # statistics for the report
    st = {"per_category": {}, "unique": Counter(r["资料类型"] for r in rows), "failures": len(pfails + mfails + manual)}
    for c in CATS:
        prim = by_cat[c]["primary"]
        recent = sum(r["时间窗口"] == "近三年" for r in prim)
        st["per_category"][c] = {"verified_primary": len(prim), "cross_listed": len(by_cat[c]["cross"]),
                                 "recent": recent, "recent_share": round(recent / len(prim), 3) if prim else None,
                                 "older": len(prim) - recent,
                                 "failed": sum(1 for x in pfails + mfails if x["分类"] == c)}
    st["formats"] = Counter(r["文件格式"].split("（")[0] for r in rows)
    st["venues_papers"] = Counter("arXiv 预印本" if r["发表渠道或出版社"] == "arXiv 预印本" else "有正式渠道信息"
                                  for r in prows)
    st["total_unique"] = len(rows)
    (CACHE / "stats_en.json").write_text(json.dumps(st, ensure_ascii=False, indent=1))
    for c, v in st["per_category"].items():
        print(c, CATS[c], v)
    print("unique:", dict(st["unique"]), "total", len(rows), "failures", st["failures"])


if __name__ == "__main__":
    main()
