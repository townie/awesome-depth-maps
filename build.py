#!/usr/bin/env python3
"""Regenerate README.md, SOURCES.md, and stats.txt from links.json.

The JSON file is the catalog. This script does not fetch the network.
It dedupes by normalized URL, refuses unknown sections, and rewrites the
README so a hand-edit to the markdown cannot drift from the data.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse, urlunparse

ROOT = Path(__file__).resolve().parent
LINKS_PATH = ROOT / "links.json"
README_PATH = ROOT / "README.md"
SOURCES_PATH = ROOT / "SOURCES.md"
STATS_PATH = ROOT / "stats.txt"

INGEST_DATE = "2026-11-19 PT"

CAT_DP2 = "Depth Pro 2"
CAT_MODELS = "Models"
CAT_VIDEO = "Video and temporal depth"
CAT_RUNTIME = "Runtimes and ports"
CAT_DEMOS = "Demos"
CAT_USE = "Use cases"
CAT_DATA = "Datasets and benchmarks"
CAT_LISTS = "Awesome lists and indexes"

DISPLAY_ORDER = [
    CAT_DP2,
    CAT_MODELS,
    CAT_VIDEO,
    CAT_RUNTIME,
    CAT_DEMOS,
    CAT_USE,
    CAT_DATA,
    CAT_LISTS,
]

SUB_ORDER = {
    CAT_DP2: [
        "Official release",
        "Sizes and weights",
        "Ports and demos",
    ],
    CAT_MODELS: [
        "Depth Pro v1",
        "Foundation and relative depth",
        "Metric monocular",
        "Diffusion and generative",
        "Geometry and point maps",
    ],
    CAT_VIDEO: [],
    CAT_RUNTIME: [
        "Libraries and official ports",
        "ONNX, TensorRT and Core ML",
        "ComfyUI and creative tools",
        "Browser",
    ],
    CAT_DEMOS: [],
    CAT_USE: [
        "3D photos and parallax",
        "Gaussian splatting and NeRF",
        "AR occlusion",
        "VFX and relighting",
        "Depth-conditioned generation",
    ],
    CAT_DATA: [],
    CAT_LISTS: [],
}

BLURBS = {
    CAT_DP2: "Apple ML Research's 2026 metric monocular depth family: one network for a photo, a video, or a live feed, at the input's full resolution. Weights are research-only.",
    CAT_MODELS: "Downloadable monocular depth and geometry models besides Depth Pro 2. The blurb says whether a release is metric or relative, and flags a research or custom license when that is what the card or repo says.",
    CAT_VIDEO: "Methods that estimate depth across frames so the map stays steady over a clip. Depth Pro 2's own video path lives in the Depth Pro 2 section.",
    CAT_RUNTIME: "Libraries, converters, and nodes that load a published depth model on your machine or in a tool. A demo Space belongs under Demos.",
    CAT_DEMOS: "Live pages where you can try a model in the browser. Official project pages that are not runnable demos live with their models.",
    CAT_USE: "Applications that consume a depth map: 3D photos, geometry initialization, occlusion, compositing, and controlled generation. Sensor-depth APIs are labeled as such.",
    CAT_DATA: "Datasets and benches commonly used to train or compare monocular and video depth, including Sintel and Spring, which Depth Pro 2 uses for its sharpness and jitter comparisons.",
    CAT_LISTS: "Related indexes. This list does not try to replace a complete paper bibliography.",
}

SOURCE_ROWS = [
    (
        "seed-manual",
        "Manual curation",
        "(this repository)",
        "Entries written for this list on 2026-11-19 PT",
    ),
    (
        "hf-api",
        "Hugging Face Hub API",
        "https://huggingface.co/models",
        "Model id, license field, pipeline tag, and createdAt for Hub repos in this list",
    ),
    (
        "vendor-pages",
        "First-party Depth Pro 2 pages",
        "https://huggingface.co/apple/DepthPro2",
        "Apple model card, GitHub README, project page, Core ML card, LICENSE_MODEL, and arXiv 2611.26603",
    ),
    (
        "choyingw/Awesome-Monocular-Depth",
        "choyingw/Awesome-Monocular-Depth",
        "https://github.com/choyingw/Awesome-Monocular-Depth",
        "Consulted as a paper index; links re-checked and not bulk-imported",
    ),
    (
        "Ideal-111/Awesome-Foundation-Model-Based-Depth",
        "Ideal-111/Awesome-Foundation-Model-Based-Depth",
        "https://github.com/Ideal-111/Awesome-Foundation-Model-Based-Depth",
        "Consulted as a foundation-model depth index; links re-checked and not bulk-imported",
    ),
]


def normalize_url(url: str) -> str:
    url = (url or "").strip()
    if not url or url.startswith(("#", "mailto:")):
        return ""
    url = url.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return ""
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path or ""
    path = path.rstrip("/")
    while "//" in path:
        path = path.replace("//", "/")
    return urlunparse((parsed.scheme.lower(), host, path, "", "", ""))


def gh_anchor(text: str) -> str:
    chars: list[str] = []
    for ch in text.lower():
        if ch.isalnum() or ch in "-_ ":
            chars.append(ch)
    return "".join(chars).strip().replace(" ", "-")


def load_entries() -> list[dict]:
    raw = json.loads(LINKS_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        sys.exit("links.json must be a list")
    seen: dict[str, dict] = {}
    for row in raw:
        for key in ("url", "title", "category", "blurb", "sources"):
            if key not in row:
                sys.exit(f"missing {key} on {row.get('url')}")
        url = row["url"].strip()
        norm = normalize_url(url)
        if not norm:
            sys.exit(f"bad url: {url}")
        cat = row["category"]
        sub = row.get("subsection") or ""
        if cat not in SUB_ORDER:
            sys.exit(f"unknown category: {cat}")
        allowed = SUB_ORDER[cat]
        if allowed:
            if sub not in allowed:
                sys.exit(f"unknown subsection {cat!r} / {sub!r} for {url}")
        elif sub:
            sys.exit(f"{cat} does not use subsections: {url}")
        blurb = " ".join(str(row["blurb"]).split())
        if not blurb.endswith("."):
            sys.exit(f"blurb must end with a period: {url}")
        if "—" in blurb or "–" in blurb:
            sys.exit(f"blurb must not contain a dash used as a separator: {url}")
        sources = row["sources"]
        if not isinstance(sources, list) or not sources:
            sys.exit(f"sources must be a non-empty list: {url}")
        pin = row.get("pin")
        if pin is not None and not isinstance(pin, int):
            sys.exit(f"pin must be an int: {url}")
        entry = {
            "url": url,
            "title": str(row["title"]).strip(),
            "category": cat,
            "subsection": sub,
            "blurb": blurb,
            "sources": sources,
            "pin": pin,
        }
        if not entry["title"]:
            sys.exit(f"empty title: {url}")
        if norm in seen:
            sys.exit(f"duplicate normalized URL:\n  {seen[norm]['url']}\n  {url}")
        seen[norm] = entry
    return list(seen.values())


def sort_entries(entries: list[dict]) -> None:
    def key(entry: dict):
        pin = entry["pin"]
        title = entry["title"].casefold()
        if pin is None:
            return (1, 0, title, entry["url"])
        return (0, pin, title, entry["url"])

    entries.sort(key=key)


def intro(n: int) -> list[str]:
    return [
        "# Awesome Depth Maps",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> Curated monocular and metric depth estimation models, runtimes, demos, datasets, and use cases, anchored on Apple's **Depth Pro 2**.",
        "",
        "**Monocular depth** estimates a distance for every pixel from a single ordinary photo, or from a video taken with one camera. **Metric** depth is in real units, usually meters, rather than a relative, up-to-scale map. Sharp object edges and, for video, low temporal jitter are what make a depth map usable for 3D photos, compositing, and geometry.",
        "",
        "**Depth Pro 2** is Apple Machine Learning Research's 2026 follow-up to Depth Pro. The [technical report](https://arxiv.org/abs/2611.26603) (submitted 19 November 2026) and the [model card](https://huggingface.co/apple/DepthPro2) describe a single network that predicts full-resolution metric depth for a photo, a video, or a live feed. Official pages say it outperforms prior single-frame and multi-frame methods on sharpness (Boundary F1) and temporal consistency (jitter), averaged over the Sintel and Spring datasets. The public family has four sizes, S (24M parameters, 97 MB), B (97M, 386 MB), L (334M, 1.3 GB), and H+ (872M, 3.5 GB), plus a shared focal-length estimator (23.5M, 94 MB). Those counts are from the official card and README, not from a secondary recap.",
        "",
        "The weights are released under the [Apple Machine Learning Research Model license](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/LICENSE_MODEL), for research use only: non-commercial scientific research and academic development. The inference [code](https://github.com/apple-aiml-research/ml-depth-pro-2) has a separate Apple software license. The repository states that it does not include training or evaluation code. A research page at `machinelearning.apple.com/research/depth-pro-2` was not published (that URL returned 404 on 2026-11-19 PT). The [Depth Pro v1 research page](https://machinelearning.apple.com/research/depth-pro) is still up. The project page links an official Hugging Face Space that returned 401 to this checker, so it is not listed; a community Space is.",
        "",
        "Quick start, from the official card: `pip install \"git+https://github.com/apple-aiml-research/ml-depth-pro-2\"`, or clone the repo and run `uv run depth-pro-2 predict -i assets/example.jpg -o out/`. On a laptop, start with `-m depthpro2-s`. Default weights are H+.",
        "",
        "The rest of this list is the broader depth-map ecosystem: other monocular and video models, runtimes and ports, live demos, datasets, and applications. A vendor's \"open source\" slogan is not treated as the license.",
        "",
        "Deduplicated by normalized URL (trailing slash, `www.`, query, and fragment stripped).",
        "",
        f"**{n} unique links** · Ingested **{INGEST_DATE}** · License for this compilation: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses).",
        "",
        "### Start here",
        "",
        "- [Depth Pro 2 model card](https://huggingface.co/apple/DepthPro2) — Official sizes, quick start, and the research-only license.",
        "- [Depth Pro 2 paper](https://arxiv.org/abs/2611.26603) — *Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth*, arXiv:2611.26603.",
        "- [ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2) — Inference code, CLI, and the Mac / Core ML demo.",
        "- [LICENSE_MODEL](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/LICENSE_MODEL) — Apple ML Research Model license: research use only.",
        "- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2) — A widely used foundation model for monocular depth, Apache-2.0.",
        "- [Use cases](#use-cases) — 3D photos, Gaussian splatting and NeRF, AR occlusion, VFX, and ControlNet.",
        "- [Datasets and benchmarks](#datasets-and-benchmarks) — KITTI, NYUv2, Sintel, Spring, ETH3D, DIODE, and related sets.",
        "",
    ]


def render_contents(by_cat: dict, by_sub: dict) -> list[str]:
    lines = ["## Contents", ""]
    for cat in DISPLAY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines.append(f"- [{cat}](#{gh_anchor(cat)}) ({len(items)})")
        for sub in SUB_ORDER[cat]:
            sub_items = by_sub[cat].get(sub, [])
            if sub_items:
                lines.append(f"  - [{sub}](#{gh_anchor(sub)}) ({len(sub_items)})")
    lines += [
        "- [Sources](#sources)",
        "- [Contributing](#contributing)",
        "- [License](#license)",
        "",
    ]
    return lines


def render_body(by_cat: dict, by_sub: dict) -> list[str]:
    lines: list[str] = []
    for cat in DISPLAY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines += [f"## {cat}", "", BLURBS[cat], ""]
        subs = [sub for sub in SUB_ORDER[cat] if by_sub[cat].get(sub)]
        if subs:
            for sub in subs:
                lines += [f"### {sub}", ""]
                for entry in by_sub[cat][sub]:
                    lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
                lines.append("")
        else:
            for entry in items:
                lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
            lines.append("")
    return lines


def render_tail() -> list[str]:
    lines = [
        "## Sources",
        "",
        "Indexes consulted for this pass. Entries were not bulk-copied; each README link was checked on its own. Machine-readable rows: [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). Notes on pages that did not earn a README line: [`discoveries/`](discoveries/).",
        "",
    ]
    for _key, name, url, note in SOURCE_ROWS:
        if url.startswith("http"):
            lines.append(f"- [{name}]({url}) — {note}.")
        else:
            lines.append(f"- {name} — {note}.")
    lines += [
        "",
        "## Contributing",
        "",
        "One factual line in the right subsection: `[Name](url) — What it actually is.` Say whether a model predicts metric or relative depth, and whether weights are Apache-2.0 or MIT, or a research / non-commercial license. Do not invent star counts, release days, benchmark scores, or paper ids. Prefer a model card or official repo over a roundup. Weak or unverified finds go in [`discoveries/`](discoveries/) instead of the README.",
        "",
        "Add the row to [`links.json`](links.json) (url, title, category, subsection, blurb, sources) and run `python3 build.py`. The script dedupes on the normalized URL and rewrites this file.",
        "",
        "List text is dedicated to the public domain under [CC0 1.0](LICENSE). Linked projects keep their own licenses.",
        "",
        "## License",
        "",
        "This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Individual projects and linked content retain their own licenses and terms. Depth Pro 2 weights are under Apple's research-only model license, not this compilation's CC0.",
        "",
    ]
    return lines


def write_sources() -> None:
    lines = [
        "# Sources consulted",
        "",
        f"Ingest date: **{INGEST_DATE}** (America/Los_Angeles).",
        "",
        "This first pass is a curated catalog, not a merge of every awesome-list bullet. The indexes below were read. A link appears in the README only after its own URL returned a successful page, and license claims for Hub models were taken from the Hub API license field or the first-party license file.",
        "",
        "| Key | Source | URL | How it was used |",
        "| --- | --- | --- | --- |",
    ]
    for key, name, url, note in SOURCE_ROWS:
        lines.append(f"| {key} | {name} | {url} | {note} |")
    lines += [
        "",
        "Normalization: strip the fragment, query, trailing slash, and a leading `www.`; drop a trailing `.git`.",
        "",
        "Not listed: [huggingface.co/spaces/apple/DepthPro2](https://huggingface.co/spaces/apple/DepthPro2) (401), [machinelearning.apple.com/research/depth-pro-2](https://machinelearning.apple.com/research/depth-pro-2) (404). See [`discoveries/`](discoveries/).",
        "",
    ]
    SOURCES_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_stats(entries: list[dict], by_cat: dict, by_sub: dict) -> None:
    source_counts: Counter[str] = Counter()
    for entry in entries:
        for source in entry["sources"]:
            source_counts[source] += 1
    lines = [f"unique_links\t{len(entries)}", "", "by_category"]
    for cat in DISPLAY_ORDER:
        lines.append(f"{cat}\t{len(by_cat.get(cat, []))}")
    lines += ["", "by_subsection"]
    for cat in DISPLAY_ORDER:
        if not SUB_ORDER[cat]:
            lines.append(f"{cat} / (none)\t{len(by_cat.get(cat, []))}")
            continue
        for sub in SUB_ORDER[cat]:
            count = len(by_sub[cat].get(sub, []))
            if count:
                lines.append(f"{cat} / {sub}\t{count}")
    lines += ["", "by_source_appearance_count", "# a link counted once per source tag"]
    for source, count in sorted(source_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"{source}\t{count}")
    on_disk = json.loads(LINKS_PATH.read_text(encoding="utf-8"))
    lines += ["", f"json_count_matches_unique\t{len(on_disk) == len(entries)}", ""]
    STATS_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_readme(entries: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    by_sub: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        by_cat[entry["category"]].append(entry)
        by_sub[entry["category"]][entry["subsection"]].append(entry)
    for cat in by_cat:
        sort_entries(by_cat[cat])
        for sub in by_sub[cat]:
            sort_entries(by_sub[cat][sub])
    lines = intro(len(entries))
    lines += render_contents(by_cat, by_sub)
    lines += render_body(by_cat, by_sub)
    lines += render_tail()
    text = "\n".join(lines)
    README_PATH.write_text(text, encoding="utf-8")
    for line in lines:
        if line.startswith("- [") or line.startswith("  - ["):
            if "](#" not in line:
                continue
            anchor = line.split("](#", 1)[1].split(")", 1)[0]
            if f"#{anchor}" not in text and f"{{#{anchor}}}" not in text:
                headings = [
                    ln[3:] if ln.startswith("### ") else ln[2:]
                    for ln in lines
                    if ln.startswith("## ") or ln.startswith("### ")
                ]
                if anchor not in {gh_anchor(h) for h in headings} and anchor not in {
                    "sources",
                    "contributing",
                    "license",
                }:
                    sys.exit(f"TOC anchor missing: {anchor}")
    write_stats(entries, by_cat, by_sub)


def main() -> None:
    entries = load_entries()
    write_readme(entries)
    write_sources()
    print(f"Wrote {len(entries)} links")


if __name__ == "__main__":
    main()
