#!/usr/bin/env python3
"""Pack a project folder into one Markdown file any AI can read.

Usage:
  python3 pack.py [folder] [-o packed.md] [--review]

Skips dependencies, build output, binaries, .gitignore'd paths and secret files,
and redacts anything that looks like an API key. Standard library only.
"""
import argparse
import fnmatch
import os
import re
import sys
from datetime import date

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "env", "dist", "build", ".next", "__pycache__",
             ".cache", ".idea", ".vscode", "coverage", ".pytest_cache", ".mypy_cache", "target", ".turbo"}
SECRET_FILES = [".env", ".env.*", "*.pem", "*.key", "*secret*", "*credential*", "*token*", "id_rsa*", "*.p12"]
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz", ".tar", ".mp4", ".mov",
              ".mp3", ".wav", ".woff", ".woff2", ".ttf", ".otf", ".db", ".sqlite", ".xlsx", ".docx", ".pptx",
              ".pyc", ".so", ".dylib", ".dll", ".exe", ".bin", ".pkl", ".parquet"}
KEY_PATTERNS = [
    r"sk-ant-[A-Za-z0-9_\-]{20,}", r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{30,}", r"gho_[A-Za-z0-9]{30,}",
    r"github_pat_[A-Za-z0-9_]{30,}", r"AKIA[0-9A-Z]{16}", r"AIza[0-9A-Za-z_\-]{35}", r"xox[baprs]-[A-Za-z0-9\-]{10,}",
    r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]",
]
LANG = {".py": "python", ".js": "javascript", ".ts": "typescript", ".tsx": "tsx", ".jsx": "jsx", ".json": "json",
        ".md": "markdown", ".html": "html", ".css": "css", ".sh": "bash", ".ps1": "powershell", ".yml": "yaml",
        ".yaml": "yaml", ".toml": "toml", ".sql": "sql", ".csv": "csv", ".txt": "text"}
MAX_LINES = 200


def gitignore_patterns(root):
    path = os.path.join(root, ".gitignore")
    if not os.path.exists(path):
        return []
    out = []
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("!"):
            out.append(line.rstrip("/"))
    return out


def ignored(rel, patterns):
    name = os.path.basename(rel)
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(name, p) or rel.startswith(p + "/") for p in patterns)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", nargs="?", default=".")
    ap.add_argument("-o", "--out", default="packed.md")
    ap.add_argument("--review", action="store_true", help="add a code review request at the top")
    a = ap.parse_args()

    root = os.path.abspath(a.folder)
    out_path = os.path.abspath(a.out)
    patterns = gitignore_patterns(root)
    files, skipped, redactions = [], [], 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not ignored(
            os.path.relpath(os.path.join(dirpath, d), root), patterns))
        for f in sorted(filenames):
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if full == out_path or ignored(rel, patterns):
                continue
            if any(fnmatch.fnmatch(f.lower(), p) for p in SECRET_FILES):
                skipped.append((rel, "possible secret, left out"))
            elif os.path.splitext(f)[1].lower() in BINARY_EXT:
                skipped.append((rel, "binary"))
            else:
                files.append(rel)

    title = os.path.basename(root)
    parts = []
    if a.review:
        parts.append("> Review this project for bugs, security problems and anything confusing. Rank issues by "
                     "severity and quote the file and line for each.\n")
    parts.append(f"# {title}\n\nPacked on {date.today().isoformat()}. {len(files)} files included.\n")
    for readme in ("README.md", "plan.md"):
        if readme in files:
            text = open(os.path.join(root, readme), encoding="utf-8", errors="ignore").read().strip()
            parts.append("## About\n\n" + "\n".join(text.splitlines()[:15]) + "\n")
            break
    parts.append("## Files\n\n```\n" + "\n".join(files + [f"{r}  ({why})" for r, why in skipped]) + "\n```\n")

    for rel in files:
        try:
            text = open(os.path.join(root, rel), encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            skipped.append((rel, "not text"))
            continue
        for pat in KEY_PATTERNS:
            text, n = re.subn(pat, "[REDACTED]", text)
            redactions += n
        lines = text.splitlines()
        note = ""
        if os.path.splitext(rel)[1].lower() in (".csv", ".txt", ".json") and len(lines) > MAX_LINES:
            note = f"\n[... {len(lines) - 20} more lines not shown]"
            lines = lines[:20]
        lang = LANG.get(os.path.splitext(rel)[1].lower(), "")
        parts.append(f"## {rel}\n\n```{lang}\n" + "\n".join(lines) + f"\n```{note}\n")

    body = "\n".join(parts)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(body)

    print(f"Wrote {out_path}")
    print(f"{len(files)} files, {len(body):,} characters, about {len(body) // 4:,} tokens")
    if redactions:
        print(f"Redacted {redactions} string(s) that looked like keys or passwords. Check before sharing.")
    if skipped:
        print(f"Left out {len(skipped)} file(s): binaries and possible secrets (listed in the file tree).")
    if len(body) > 400_000:
        print("Warning: over 400,000 characters. Many chat tools cut off long pastes; pack one subfolder instead.")


if __name__ == "__main__":
    sys.exit(main())
