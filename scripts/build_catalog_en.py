#!/usr/bin/env python3
"""Build the library's deliverable indexes from seeds + results + annotations (read-only on sources).

  python3 -I scripts/build_catalog_en.py

Writes (library root): catalog_cn.csv, download_failures_cn.csv, checksums_en.sha256,
domains/<NN>_<slug>_index_cn.md, scripts/state/stats_en.json.
Only VERIFIED items enter catalog_cn.csv; failed / pending / unresolved items go to
download_failures_cn.csv. Cross-library relations are computed against the sibling libraries
(read-only): same arXiv id or same SHA256.
"""
import csv
import hashlib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402
import papers_en as P  # noqa: E402

CATNAME = {c: n for c, _, n in C.CATEGORIES}
PAPER_CODES = [c for c, _, _ in C.CATEGORIES if int(c) <= 16]
ENG_RESULTS = C.RESULTS / "19_engineering_en.json"
ENG_SEEDS = C.SEEDS / "19_engineering_seed_cn.json"

COLS = ["文献编号", "主分类", "交叉标签", "交叉标签依据", "资料类型", "子方向", "标题", "作者或教师", "学校或机构",
        "发表渠道或出版社", "发表状态", "发表状态依据", "首次公开日期", "日期精度", "首次公开依据", "下载版本", "版本日期",
        "时间窗口", "经典补充理由", "DOI", "arXiv ID", "ISBN", "其他标识符", "资料语言", "来源链接", "下载链接", "本地路径",
        "格式", "完整性", "核验状态", "核验详情", "SHA256", "获取方式", "跨库关系", "相关性", "相关性用途", "选入理由",
        "阅读优先级", "类内优先阅读排名", "优先阅读理由", "内容简介",
        "涉及语言", "语系", "文字系统", "资源条件", "基座模型", "适配方式", "数据类型与数据量", "翻译/合成/教师依赖",
        "母语者审核或人工评价", "对目标语言/原有语言/代码能力的影响", "训练推理资源与代码数据可用性", "评测任务",
        "基准来源（原生/翻译）", "数据污染控制", "作者报告的局限", "证据范围", "结果来源", "关键区分说明", "字段依据",
        "课程代码", "学期或书籍版本", "原著年份", "版本或学期年份", "先修要求", "内容范围", "难度或阶段", "内容完整性说明",
        "工程环节", "许可证", "提交号", "提交日期", "核心模块", "关联论文", "学习价值", "文档集保存范围", "完整文档集"]

ANN_MAP = [("涉及语言", "languages"), ("语系", "language_families"), ("文字系统", "scripts"),
           ("资源条件", "resource_condition"), ("基座模型", "base_model"), ("适配方式", "adaptation"),
           ("数据类型与数据量", "data_type_size"), ("翻译/合成/教师依赖", "translation_synthetic_teacher"),
           ("母语者审核或人工评价", "native_human_eval"), ("对目标语言/原有语言/代码能力的影响", "capability_effects"),
           ("训练推理资源与代码数据可用性", "resources_availability"), ("评测任务", "eval_tasks"),
           ("基准来源（原生/翻译）", "benchmark_origin"), ("数据污染控制", "contamination_control"),
           ("作者报告的局限", "limitations"), ("证据范围", "evidence_scope"), ("结果来源", "result_source"),
           ("关键区分说明", "distinctions"), ("字段依据", "field_basis")]

SCRIPT_KW = {"拉丁": r"拉丁|Latin", "西里尔": r"西里尔|Cyrillic", "阿拉伯": r"阿拉伯(文|字母|字)|Arabic script|Perso-Arabic|波斯-阿拉伯",
             "天城文": r"天城|Devanagari", "孟加拉文": r"孟加拉(文|字)|Bengali script|Bangla script", "汉字": r"汉字|Han |CJK|中文字",
             "埃塞俄比亚(吉兹)": r"吉兹|Ge'?ez|Ethiopic|埃塞俄比亚(文|字)", "藏文": r"藏文|Tibetan script", "泰文": r"泰文|Thai script",
             "韩文": r"韩文|谚文|Hangul", "日文假名": r"假名|Kana", "希伯来": r"希伯来(文|字)|Hebrew script",
             "泰米尔等南印度文字": r"泰米尔(文|字)|泰卢固(文|字)|卡纳达|马拉雅拉姆|Tamil script|Telugu script", "格鲁吉亚/亚美尼亚": r"格鲁吉亚(文|字)|亚美尼亚(文|字)",
             "蒙古/传统文字": r"蒙古(文|字)|Mongolian script", "缅文/高棉/老挝": r"缅(文|甸文)|高棉|老挝(文|字)|Khmer|Myanmar script|Lao script",
             "希腊": r"希腊(文|字母)|Greek script", "提菲纳/其他非洲文字": r"提非纳|Tifinagh|N'?Ko|Vai"}
FAMILY_KW = {"印欧": r"印欧|Indo-European", "尼日尔-刚果/班图": r"尼日尔-刚果|Niger-Congo|班图|Bantu", "亚非(闪含)": r"亚非|Afro-Asiatic|闪米特|Semitic|闪含",
             "汉藏": r"汉藏|Sino-Tibetan", "南岛": r"南岛|Austronesian", "突厥": r"突厥|Turkic", "达罗毗荼": r"达罗毗荼|Dravidian",
             "南亚(孟-高棉)": r"南亚语系|Austroasiatic|孟-高棉", "乌拉尔": r"乌拉尔|Uralic", "壮侗(台-卡岱)": r"壮侗|台-卡岱|Kra-Dai|Tai-Kadai",
             "美洲原住民语言": r"美洲原住民|克丘亚|Quechua|艾马拉|Aymara|瓜拉尼|Guarani|纳瓦特|Nahuatl|Indigenous languages of the Americas|美洲土著",
             "尼罗-撒哈拉": r"尼罗-撒哈拉|Nilo-Saharan", "孤立/克里奥尔/手语": r"克里奥尔|Creole|孤立语言|language isolate|手语|sign language"}


def load_seeds_all(code):
    out = []
    for p in sorted(C.SEEDS.glob(f"{C.cat_key(code)}_seed*_cn.json")):
        out += C.load_json(p, [])
    return out


def sibling_hashes():
    """sha256 -> (lib, relpath) from sibling libraries' checksum lists and state JSON records
    (read-only; their PDFs are not re-read, to avoid page-cache churn on this host)."""
    import glob
    by_sha = {}
    for lib in P.OTHER_LIBS:
        cks = lib / "checksums_en.sha256"
        if cks.exists():
            for line in cks.read_text("utf-8", "replace").splitlines():
                m = re.match(r"([0-9a-f]{64})\s+\*?(.+)", line.strip())
                if m:
                    by_sha.setdefault(m.group(1), (lib.name, m.group(2)))
        for jf in glob.glob(str(lib / "scripts" / "**" / "*.json"), recursive=True):
            try:
                d = C.load_json(jf, {})
            except Exception:
                continue
            if not isinstance(d, dict):
                continue
            for r in d.values():
                if not isinstance(r, dict):
                    continue
                if re.fullmatch(r"[0-9a-f]{64}", str(r.get("sha256", ""))) and r.get("local_path"):
                    by_sha.setdefault(r["sha256"], (lib.name, r["local_path"]))
                for f in r.get("files", []) if isinstance(r.get("files"), list) else []:
                    if isinstance(f, dict) and re.fullmatch(r"[0-9a-f]{64}", str(f.get("sha256", ""))):
                        by_sha.setdefault(f["sha256"], (lib.name, f.get("path", "")))
    return by_sha


def pub_status(seed, meta):
    jr = (meta or {}).get("journal_ref", "")
    if jr:
        return "作者声明已发表（未独立核实）", f"arXiv journal_ref：{jr}"
    com = (meta or {}).get("comment", "")
    m = re.search(r"(accepted|to appear|published|camera[- ]ready|oral|spotlight|Findings|ACL|EMNLP|NAACL|COLING|LREC|ICLR|NeurIPS|ICML|TACL)[^.;]{0,80}", com, re.I)
    if m:
        return "作者在 arXiv 注释中声明发表/接收（未独立核实）", f"arXiv 注释：{m.group(0).strip()}"
    if seed.get("venue"):
        return f"已发表：{seed['venue']}", f"来源页面（{seed.get('landing_url', '')}）"
    if seed.get("type") == "技术报告":
        return "技术报告（预印本形式公开）", "资料类型；未核查正式发表记录"
    return "预印本（未核查正式发表）", "arXiv 元数据无 journal_ref/发表注释"


def window_label(date):
    if not date:
        return "日期待核实"
    return "近三年" if date >= C.WINDOW_START else "三年前经典补充"


def esc(v):
    if isinstance(v, (list, tuple)):
        return "；".join(str(x) for x in v)
    return "" if v is None else str(v)


def main():
    meta = C.load_json(C.STATE / "arxiv_meta_en.json", {})
    sib_arxiv = P.other_lib_index()
    sib_sha = sibling_hashes()
    rows, fails, stats = [], [], {"categories": {}, "materials": {}, "engineering": {}}
    cross_tags = {}
    for code in PAPER_CODES:
        for s in load_seeds_all(code):
            if s.get("cross_only"):
                k = P.paper_key(s)
                cross_tags.setdefault(k, []).append((code, s.get("cross_reason", "")))
    seen_sha = {}
    lang_cov = {"scripts": {}, "families": {}}
    # ------------------------------------------------------------- papers
    for code in PAPER_CODES:
        slug = C.CAT_BY_CODE[code][1]
        seeds = load_seeds_all(code)
        res = C.load_json(C.RESULTS / f"{code}_{slug}_en.json", {})
        ann = C.load_json(C.ANNOT / f"{code}_{slug}_annot_cn.json", {})
        st = {"verified": 0, "pending": 0, "failed": 0, "recent": 0, "old": 0, "undated": 0, "new_download": 0,
              "reused": 0, "cross_library_dup": 0, "dup_elsewhere": 0, "cross_only": 0, "direct": 0, "support": 0,
              "relevance_missing": 0, "annotated": 0, "todo": 0}
        for s in seeds:
            sid = s["sid"]
            r = res.get(sid, {})
            status = r.get("status")
            if s.get("cross_only"):
                st["cross_only"] += 1
                continue
            if s.get("exclude"):
                if status == "verified":
                    fails.append({"文献编号": f"LRL-P-{sid}", "类别": f"{code} {CATNAME[code]}", "标题": r.get("title") or s.get("title", ""),
                                  "状态": "核验后人工排除", "阶段": "review", "原因": s.get("exclude_reason", ""),
                                  "尝试来源": r.get("source_url", ""), "尝试时间": r.get("time", ""), "处理": "不计数；PDF 已移出交付目录"})
                continue
            if status == "duplicate_elsewhere":
                st["dup_elsewhere"] += 1
                continue
            if status != "verified":
                if status in ("failed", "pending"):
                    st[status] += 1
                    fails.append({"文献编号": f"LRL-P-{sid}", "类别": f"{code} {CATNAME[code]}", "标题": r.get("title") or s.get("title", ""),
                                  "状态": "待核验" if status == "pending" else "下载或核验失败", "阶段": r.get("stage", "verify"),
                                  "原因": "；".join(r.get("notes", [])), "尝试来源": r.get("source_url") or s.get("pdf_url") or s.get("arxiv", ""),
                                  "尝试时间": r.get("time", ""), "处理": "未计数；已用备选替代" if status == "failed" else "未计数；待人工核对"})
                elif not s.get("reserve"):
                    st["todo"] += 1
                continue
            m = P.seed_meta(s, meta) or {}
            a = P.norm_arxiv(s.get("arxiv"))
            am = meta.get(a, {}) if a else {}
            an = ann.get(sid, {})
            fp = m.get("first_public", "")
            win = window_label(fp)
            st["verified"] += 1
            st["recent" if win == "近三年" else ("old" if fp else "undated")] += 1
            rel = an.get("relevance") or s.get("relevance") or ""
            st["direct" if rel == "直接相关" else ("support" if rel == "通用支撑" else "relevance_missing")] += 1
            st["annotated"] += bool(an)
            origin = r.get("origin", "downloaded_this_round")
            sha = r.get("sha256", "")
            rel_bits = []
            if origin == "reused_other_library":
                st["reused"] += 1
                rel_bits.append(f"已有复用：复制自 {r.get('origin_path')} 并重新核验")
            else:
                st["new_download"] += 1
            if a and a in sib_arxiv and origin != "reused_other_library":
                rel_bits.append(f"兄弟库有同一 arXiv 论文：{sib_arxiv[a][0]}/{sib_arxiv[a][1]}")
            if sha in sib_sha and origin != "reused_other_library":
                rel_bits.append(f"兄弟库有同哈希文件：{sib_sha[sha][0]}/{sib_sha[sha][1]}")
            if rel_bits:
                st["cross_library_dup"] += 1
            if sha in seen_sha:
                rel_bits.append(f"库内同哈希：{seen_sha[sha]}")
            seen_sha.setdefault(sha, f"LRL-P-{sid}")
            ps, pb = pub_status(s, am)
            key = P.paper_key(s)
            cross = [c for c in s.get("cross", []) if c != code]
            cross_reason = s.get("cross_reason", "")
            for c2, why in cross_tags.get(key, []):
                if c2 != code and c2 not in cross:
                    cross.append(c2)
                    cross_reason += f"；{c2}类：{why}"
            v = r.get("verification", {})
            row = {"文献编号": f"LRL-P-{sid}", "主分类": f"{code} {CATNAME[code]}",
                   "交叉标签": "；".join(f"{c} {CATNAME.get(c, '')}" for c in cross), "交叉标签依据": cross_reason.strip("；"),
                   "资料类型": s.get("type", "论文"), "子方向": s.get("subtopic", ""), "标题": m.get("title") or s.get("title", ""),
                   "作者或教师": "；".join(m.get("authors", [])[:12]) + (" 等" if len(m.get("authors", [])) > 12 else ""),
                   "学校或机构": an.get("institutions", "待核实"), "发表渠道或出版社": s.get("venue") or ("arXiv 预印本" if a else ""),
                   "发表状态": ps, "发表状态依据": pb, "首次公开日期": fp, "日期精度": m.get("date_precision", ""),
                   "首次公开依据": m.get("first_public_basis", ""), "下载版本": m.get("version", ""), "版本日期": m.get("version_date", ""),
                   "时间窗口": win, "经典补充理由": s.get("old_reason", "") if win != "近三年" else "",
                   "DOI": am.get("doi") or s.get("doi", ""), "arXiv ID": a, "ISBN": "", "其他标识符": s.get("acl_id", ""),
                   "资料语言": "英文", "来源链接": m.get("landing", ""), "下载链接": r.get("source_url", ""),
                   "本地路径": r.get("local_path", ""), "格式": "PDF", "完整性": "全文（含参考文献）",
                   "核验状态": "已核验" + ("（人工核对）" if r.get("manual_verification") else ""),
                   "核验详情": f"页数 {v.get('pages')}；抽取字符 {v.get('chars_extracted')}；标题匹配 {v.get('title_match')}；作者 {v.get('author_check')}"
                               + (f"；人工：{r['manual_verification']['note']}" if r.get("manual_verification") else ""),
                   "SHA256": sha, "获取方式": "已有复用" if origin == "reused_other_library" else f"新下载（{(r.get('time') or '')[:10]}）",
                   "跨库关系": "；".join(rel_bits), "相关性": rel, "相关性用途": an.get("relevance_use", ""), "选入理由": s.get("reason", ""),
                   "阅读优先级": s.get("priority", ""), "类内优先阅读排名": an.get("top_rank", ""), "优先阅读理由": an.get("top_reason", ""),
                   "内容简介": an.get("summary", "待补充")}
            for col, k in ANN_MAP:
                row[col] = esc(an.get(k, "待核实" if an else "未注释"))
            rows.append(row)
            for name, rx in SCRIPT_KW.items():
                if re.search(rx, esc(an.get("scripts", "")) + " " + esc(an.get("languages", ""))):
                    lang_cov["scripts"].setdefault(name, []).append(f"LRL-P-{sid}")
            for name, rx in FAMILY_KW.items():
                if re.search(rx, esc(an.get("language_families", "")) + " " + esc(an.get("languages", ""))):
                    lang_cov["families"].setdefault(name, []).append(f"LRL-P-{sid}")
        st["recent_ratio"] = round(st["recent"] / st["verified"], 4) if st["verified"] else 0.0
        stats["categories"][code] = st
    # ------------------------------------------------------------- courses / books
    for code, prefix in (("17", "C"), ("18", "B")):
        slug = C.CAT_BY_CODE[code][1]
        seeds = load_seeds_all(code)
        res = C.load_json(C.RESULTS / f"{code}_{slug}_en.json", {})
        st = {"verified": 0, "failed": 0, "todo": 0, "new_download": 0, "reused": 0, "recent_edition": 0}
        for s in seeds:
            if s.get("exclude"):
                continue
            sid = s["sid"]
            r = res.get(sid, {})
            title = s.get("title") or s.get("course_title", "")
            if r.get("status") != "verified":
                if r.get("status") in ("failed", "duplicate_elsewhere"):
                    st["failed"] += 1
                    fails.append({"文献编号": f"LRL-{prefix}-{sid}", "类别": f"{code} {CATNAME[code]}", "标题": title,
                                  "状态": "下载或核验失败" if r.get("status") == "failed" else "与论文重复",
                                  "阶段": "fetch", "原因": "；".join(r.get("notes", []))[:800],
                                  "尝试来源": s.get("official_url") or s.get("landing_url", ""), "尝试时间": r.get("time", ""),
                                  "处理": "未计数"})
                else:
                    st["todo"] += 1
                continue
            st["verified"] += 1
            reused = r.get("origin") == "reused_other_library"
            st["reused" if reused else "new_download"] += 1
            yr = str(s.get("edition_year") or s.get("term_year") or "")
            st["recent_edition"] += yr >= "2023"
            files = [f for f in r.get("files", [])]
            book = r.get("book_check", {})
            course = r.get("course_check", {})
            fmt = sorted({Path(f["path"]).suffix.lstrip(".").upper() or "?" for f in files})
            sib = [f"{sib_sha[f['sha256']][0]}/{sib_sha[f['sha256']][1]}" for f in files if f.get("sha256") in sib_sha]
            row = {"文献编号": f"LRL-{prefix}-{sid}", "主分类": f"{code} {CATNAME[code]}",
                   "交叉标签": "；".join(f"{c} {CATNAME.get(c, '')}" for c in s.get("cross", [])), "交叉标签依据": s.get("cross_reason", ""),
                   "资料类型": "大学课程讲义" if code == "17" else (s.get("book_type") or "教科书/专著/参考书"),
                   "子方向": s.get("subtopic") or s.get("area", ""), "标题": title,
                   "作者或教师": "；".join(s.get("instructors") or s.get("authors") or []),
                   "学校或机构": s.get("university") or s.get("institution", ""), "发表渠道或出版社": s.get("publisher", ""),
                   "发表状态": s.get("status_note") or ("课程官方发布" if code == "17" else "正式出版/作者公开版本"),
                   "发表状态依据": s.get("verification_basis", ""), "首次公开日期": str(s.get("original_year") or s.get("term_year") or ""),
                   "日期精度": "年", "首次公开依据": "种子记录（课程学期/原著年份）", "下载版本": s.get("edition") or s.get("term", ""),
                   "版本日期": str(s.get("edition_year") or s.get("term_year") or ""), "时间窗口": "近三年版本/学期" if yr >= "2023" else "较早版本（教材不强制比例）",
                   "经典补充理由": s.get("old_reason", ""), "DOI": s.get("doi", ""), "arXiv ID": s.get("arxiv", ""), "ISBN": esc(s.get("isbn", "")),
                   "其他标识符": s.get("course_code", ""), "资料语言": {"en": "英文", "cn": "中文"}.get(s.get("language", "en"), s.get("language", "")),
                   "来源链接": s.get("official_url") or s.get("landing_url", ""), "下载链接": "；".join(f.get("url", "") for f in files[:3]) + (" 等（见 manifest）" if len(files) > 3 else ""),
                   "本地路径": r.get("local_path", ""), "格式": "/".join(fmt) + ("（离线 HTML 包）" if r.get("mirror") else ""),
                   "完整性": s.get("completeness_note", ""), "核验状态": "已核验",
                   "核验详情": (f"页数 {book.get('pages')}；标题匹配 {book.get('title_match')}；目录 {book.get('toc_found')}；作者 {book.get('author_found')}" if book else
                              f"讲义文件 {course.get('lecture_files_ok')} / 应有 {course.get('expected_items')}" if course else f"文件 {len(files)} 个均通过类型检查"),
                   "SHA256": r.get("pack_sha256", ""), "获取方式": "已有复用" if reused else f"新下载（{(r.get('time') or '')[:10]}）",
                   "跨库关系": ("已有复用：" + "；".join(r.get("origin_paths", [])[:3])) if reused else ("兄弟库有同哈希文件：" + "；".join(sib[:3]) if sib else ""),
                   "相关性": "通用支撑（系统教材）", "相关性用途": s.get("relevance_use", ""), "选入理由": s.get("reason", ""),
                   "阅读优先级": s.get("priority", ""), "内容简介": s.get("coverage", ""), "字段依据": "官方页面/书籍前言与目录",
                   "课程代码": s.get("course_code", ""), "学期或书籍版本": s.get("term") or s.get("edition", ""),
                   "原著年份": str(s.get("original_year", "")), "版本或学期年份": yr, "先修要求": s.get("prereq", ""),
                   "内容范围": s.get("coverage", ""), "难度或阶段": s.get("stage", ""), "内容完整性说明": s.get("completeness_note", "")}
            rows.append(row)
        stats["materials"][code] = st
    # ------------------------------------------------------------- engineering
    eres = C.load_json(ENG_RESULTS, {})
    est = {"verified": 0, "docs_complete": 0, "failed": 0, "stages": {}}
    for s in C.load_json(ENG_SEEDS, []):
        r = eres.get(s["eid"], {})
        if s.get("exclude"):
            continue
        if r.get("status") != "verified":
            if r.get("status") == "failed":
                est["failed"] += 1
                fails.append({"文献编号": f"LRL-{s['eid']}", "类别": "19 工程资料", "标题": s["name"], "状态": "获取失败", "阶段": "fetch",
                              "原因": "；".join(r.get("notes", [])), "尝试来源": f"{s['repo']}@{s['ref']}", "尝试时间": r.get("time", ""), "处理": "未计数"})
            continue
        est["verified"] += 1
        d = r.get("docs", {})
        est["docs_complete"] += bool(d.get("complete_doc_set"))
        est["stages"].setdefault(s.get("stage", "?"), []).append(s["name"])
        paths = [r.get("archive_path", ""), r.get("renamed_copy_path", "")] + ([d.get("local_path")] if d else [])
        rows.append({"文献编号": f"LRL-{s['eid']}", "主分类": "19 工程资料（官方文档与参考实现）", "交叉标签": esc(s.get("cross_stages", [])),
                     "资料类型": "开源参考实现" + ("+官方文档集" if d else ""), "子方向": s.get("stage", ""), "标题": s["name"],
                     "学校或机构": s.get("org", ""), "来源链接": s.get("official_url") or s["repo"], "下载链接": f"{s['repo']} @ {r.get('commit')}",
                     "下载版本": s["ref"], "版本日期": r.get("commit_date", ""), "首次公开日期": r.get("retrieved", ""), "日期精度": "日",
                     "首次公开依据": "访问日期（工程资料按提交号/版本记录）", "本地路径": "；".join(p for p in paths if p),
                     "格式": "源码归档 tar.gz + 加后缀只读副本" + ("；文档源文件" if d else ""),
                     "完整性": f"源码过滤后 {r.get('files_kept')} 个文件，剔除 {r.get('excluded_count')} 个（权重/二进制/大文件）",
                     "核验状态": "已核验", "核验详情": f"提交 {r.get('commit')}；文档 TOC {d.get('toc_kind')} {d.get('toc_entries')} 项缺 {d.get('toc_missing')}" if d else f"提交 {r.get('commit')}",
                     "SHA256": r.get("archive_sha256", ""), "获取方式": f"新获取（{r.get('retrieved', '')}）", "资料语言": "英文",
                     "相关性": "通用支撑（工程）", "选入理由": s.get("why", "") or s.get("learning_value", ""), "内容简介": s.get("purpose", ""),
                     "工程环节": s.get("stage", ""), "许可证": f"人工确认/预期：{s.get('license_expected', '')}；脚本检测：{r.get('license', {}).get('detected')}（{r.get('license', {}).get('file')}）；人工复核见 scripts/work/engineering_notes_cn.md",
                     "提交号": r.get("commit", ""), "提交日期": r.get("commit_date", ""), "核心模块": esc(s.get("core_modules", [])),
                     "关联论文": esc(s.get("related_papers", [])), "学习价值": s.get("learning_value", ""),
                     "文档集保存范围": (d.get("format", "") + "；" + d.get("scope_note", "") + f"；仓库路径 {d.get('path_in_repo')}") if d else "未保存文档集",
                     "完整文档集": (("是：" if d.get("complete_doc_set") else "否（不计为完整文档集）：") + str(d.get("completeness_basis", ""))) if d else "无", "字段依据": "官方仓库/文档"})
    stats["engineering"] = est
    # ------------------------------------------------------------- write
    with open(C.ROOT / "catalog_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in COLS})
    fcols = ["文献编号", "类别", "标题", "状态", "阶段", "原因", "尝试来源", "尝试时间", "处理"]
    with open(C.ROOT / "download_failures_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fcols)
        w.writeheader()
        for r in fails:
            w.writerow(r)
    # per-category domain indexes
    C.ROOT.joinpath("domains").mkdir(exist_ok=True)
    for code, slug, name in C.CATEGORIES:
        mine = [r for r in rows if r["主分类"].startswith(code + " ")]
        if not mine:
            continue
        mine.sort(key=lambda r: (int(r["类内优先阅读排名"]) if str(r.get("类内优先阅读排名", "")).isdigit() else 99, r["文献编号"]))
        crossed = [r for r in rows if re.search(rf"(^|；){code} ", r.get("交叉标签", ""))]
        out = [f"# {code} {name}：资料索引\n", f"由 `scripts/build_catalog_en.py` 自动生成；字段详见 `catalog_cn.csv`。本类主分类 {len(mine)} 条，交叉标签 {len(crossed)} 条。\n"]
        if code in stats["categories"]:
            st = stats["categories"][code]
            out.append(f"已核验完整资料 {st['verified']} / 目标约 50；待核验 {st['pending']}；下载失败 {st['failed']}。近三年 {st['recent']}/{st['verified']}（{st['recent_ratio']:.1%}）；直接相关 {st['direct']}，通用支撑 {st['support']}；已有复用 {st['reused']}。\n")
        out.append("| 编号 | 优先 | 首次公开 | 相关性 | 标题 | 本地路径 |\n|---|---|---|---|---|---|")
        for r in mine:
            out.append(f"| {r['文献编号']} | {r.get('类内优先阅读排名', '')} | {r['首次公开日期']} | {r.get('相关性', '')} | {r['标题'][:90]} | [{Path(r['本地路径'].split('；')[0]).name}](../{r['本地路径'].split('；')[0]}) |")
        if crossed:
            out.append("\n## 交叉标签（主分类在别类）\n")
            for r in crossed:
                out.append(f"- {r['文献编号']}（主类 {r['主分类']}）{r['标题'][:90]} — 依据：{r.get('交叉标签依据', '')[:120]}")
        (C.ROOT / "domains" / f"{code}_{slug}_index_cn.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    # checksums of every delivered file (not scripts/state internals)
    lines = []
    for top in ("papers", "university_materials", "books", "engineering_docs", "reference_code", "guides", "domains"):
        for p in sorted((C.ROOT / top).rglob("*")):
            if p.is_file():
                lines.append(f"{C.sha256_file(p)}  {p.relative_to(C.ROOT)}")
    for p in sorted(C.ROOT.glob("*_cn.*")) + sorted((C.ROOT / "scripts").glob("*.py")) + sorted((C.ROOT / "scripts").glob("*_cn.md")):
        if p.name != "checksums_en.sha256":
            lines.append(f"{C.sha256_file(p)}  {p.relative_to(C.ROOT)}")
    (C.ROOT / "checksums_en.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    # library-wide unique counts
    keys = {}
    for r in rows:
        k = r.get("arXiv ID") or r.get("DOI") or r.get("SHA256") or r["标题"].lower()
        keys.setdefault(k, []).append(r["文献编号"])
    stats["unique_items"] = len(keys)
    stats["in_library_duplicates"] = {k: v for k, v in keys.items() if len(v) > 1}
    stats["papers_total_verified"] = sum(s["verified"] for s in stats["categories"].values())
    stats["papers_unique"] = len({(r.get("arXiv ID") or r.get("SHA256")) for r in rows if r["文献编号"].startswith("LRL-P-")})
    stats["language_coverage"] = {k: {n: len(v) for n, v in d.items()} for k, d in lang_cov.items()}
    stats["language_coverage_ids"] = lang_cov
    stats["catalog_rows"] = len(rows)
    stats["failures_rows"] = len(fails)
    C.save_json(C.STATE / "stats_en.json", stats)
    for code, st in stats["categories"].items():
        print(f"[{code} {CATNAME[code]}] 已核验完整资料 {st['verified']} / 目标约 50；待核验 {st['pending']}；下载失败 {st['failed']}。"
              f" 近三年 {st['recent_ratio']:.1%}；直接 {st['direct']}/支撑 {st['support']}；复用 {st['reused']}；注释 {st['annotated']}")
    for code, st in stats["materials"].items():
        print(f"[{code} {CATNAME[code]}] 已核验完整资料 {st['verified']} / 目标约 50；待核验 {st['todo']}；下载失败 {st['failed']}。复用 {st['reused']}")
    print(f"[19 工程] 项目 {est['verified']}，完整文档集 {est['docs_complete']}，失败 {est['failed']}")
    print(f"catalog rows {len(rows)}; unique {stats['unique_items']}; papers verified {stats['papers_total_verified']} unique {stats['papers_unique']}; failures {len(fails)}")


if __name__ == "__main__":
    main()
