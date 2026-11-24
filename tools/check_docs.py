#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""文档自检：检查 Markdown 文件的相对链接、代码围栏、文件结尾换行。

用法：
    python tools/check_docs.py

退出码 0 表示全部通过，1 表示存在错误（CI 会因此失败）。
只检查仓库内的相对链接，外链不校验（避免网络波动导致误报）。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "build", ".pio", "dist"}

LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE_RE = re.compile(r"^\s*```")
FENCE_BLOCK_RE = re.compile(r"^[ \t]*```.*?^[ \t]*```", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

IGNORED_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "data:")


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")

    if not text.strip():
        errors.append(f"{rel}: 文件为空")
        return errors

    if not text.endswith("\n"):
        errors.append(f"{rel}: 文件结尾缺少换行")

    # 代码围栏必须成对
    fences = sum(1 for line in text.splitlines() if FENCE_RE.match(line))
    if fences % 2 != 0:
        errors.append(f"{rel}: 代码围栏未闭合（``` 出现 {fences} 次，应为偶数）")

    # 代码块与行内代码里出现的链接是示例，不参与校验
    scannable = INLINE_CODE_RE.sub("", FENCE_BLOCK_RE.sub("", text))

    for match in LINK_RE.finditer(scannable):
        target = match.group(1).strip()
        if not target or target.lower().startswith(IGNORED_PREFIXES):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (path.parent / unquote(target)).resolve()
        try:
            resolved.relative_to(REPO_ROOT)
        except ValueError:
            errors.append(f"{rel}: 链接指向仓库外 -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"{rel}: 链接目标不存在 -> {target}")

    return errors


def main() -> int:
    files = iter_markdown_files()
    all_errors: list[str] = []
    for path in files:
        all_errors.extend(check_file(path))

    print(f"检查 {len(files)} 个 Markdown 文件")
    if all_errors:
        print(f"\n发现 {len(all_errors)} 个问题：\n")
        for err in all_errors:
            print(f"  ✗ {err}")
        return 1

    print("全部通过：链接可解析、围栏成对、结尾换行齐全")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
