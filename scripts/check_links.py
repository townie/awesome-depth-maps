#!/usr/bin/env python3
"""Fetch every links.json URL and require a successful final HTTP status."""

from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (compatible; awesome-depth-maps-curation/1.0)"
OK = {"200", "203"}


def check(url: str) -> tuple[str, str, str]:
    try:
        out = subprocess.check_output(
            [
                "curl",
                "-sS",
                "-o",
                "/dev/null",
                "-w",
                "%{http_code} %{url_effective}",
                "-L",
                "--max-time",
                "25",
                "-A",
                UA,
                url,
            ],
            stderr=subprocess.STDOUT,
            text=True,
            timeout=35,
        ).strip()
    except Exception as exc:  # noqa: BLE001
        return url, "000", str(exc)
    parts = out.split(None, 1)
    code = parts[0] if parts else "000"
    final = parts[1] if len(parts) > 1 else ""
    return url, code, final


def main() -> int:
    rows = json.loads((ROOT / "links.json").read_text(encoding="utf-8"))
    urls = [row["url"] for row in rows]
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = [pool.submit(check, url) for url in urls]
        for fut in as_completed(futs):
            url, code, final = fut.result()
            if code not in OK:
                failures.append(f"{code} {url} -> {final}")
                print(f"FAIL {code} {url} -> {final}", file=sys.stderr)
    if failures:
        print(f"{len(failures)} of {len(urls)} links failed", file=sys.stderr)
        return 1
    print(f"link check passed ({len(urls)} urls)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
