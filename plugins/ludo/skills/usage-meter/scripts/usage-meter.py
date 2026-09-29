#!/usr/bin/env python3
"""Ludo's usage meter: a Claude Code status line.

Shows:  Sonnet 5.5 · my-folder · context 42% ▓▓▓▓░░░░░░
Reads the JSON Claude Code sends on stdin. Any missing field is skipped, never an error.
"""
import json
import re
import sys

EXPENSIVE = ("opus", "fable")


def pick(d, *path):
    for key in path:
        if not isinstance(d, dict):
            return None
        d = d.get(key)
    return d


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        print("Claude")
        return
    try:
        model = pick(data, "model", "display_name") or pick(data, "model", "id") or "Claude"
        parts = [model + (" (uses limits fast)" if any(x in model.lower() for x in EXPENSIVE) else "")]

        folder = pick(data, "workspace", "current_dir") or data.get("cwd")
        if folder:
            parts.append(re.split(r"[\\/]", folder.rstrip("/\\"))[-1] or folder)

        pct = pick(data, "context_window", "used_percentage")
        if pct is None:
            used = pick(data, "context_window", "total_input_tokens")
            size = pick(data, "context_window", "context_window_size")
            if used is not None and size:
                pct = 100 * used / size
        if pct is not None:
            pct = max(0, min(100, float(pct)))
            filled = int(round(pct / 10))
            bar = "▓" * filled + "░" * (10 - filled)
            parts.append(f"context {pct:.0f}% {bar}")
            if pct >= 80:
                parts.append("time to /clear")

        cost = pick(data, "cost", "total_cost_usd")
        if cost:
            parts.append(f"${cost:.2f} this session")

        print(" · ".join(parts))
    except Exception:
        print(pick(data, "model", "display_name") or "Claude")


if __name__ == "__main__":
    main()
