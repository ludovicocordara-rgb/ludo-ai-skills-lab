---
name: usage-meter
description: Set up a status bar at the bottom of Claude Code that always shows which model is running, the current folder, and how full the context window is, so the user knows when to /clear and when they are burning their Pro limit on an expensive model. Use when the user says "usage meter", "status bar", "statusline", "how full is my context", "show my model", or keeps hitting limits by surprise.
---

# Usage meter

Claude Code can show a custom line under the input box. This skill sets one up that answers the three questions that matter most while working: which model am I on, where am I, and how full is the context.

## Step 1, read the current docs

The status line gets a block of JSON from Claude Code each time it redraws. Field names can change between versions, so first read the official page: https://code.claude.com/docs/en/statusline. Note the exact names for the model's display name, the current folder, and any context or cost fields. Claude Code also has a built-in `/statusline` command that can set this up; this skill does the same thing with a nicer default.

## Step 2, install the script

This skill ships a ready script: `scripts/usage-meter.py` in this skill's folder. Copy it to `~/.claude/usage-meter.py` (on Windows, `C:/Users/<name>/.claude/usage-meter.py`).

It prints one line like `Sonnet 5.5 · outreach · context 42% ▓▓▓▓░░░░░░`, marks Opus and Fable as "(uses limits fast)", adds "time to /clear" past 80% context, and shows session cost when Claude Code provides it. Any field the JSON lacks is skipped, and it never prints an error to the status bar.

If the docs from step 1 show different field names than the script reads (`model.display_name`, `workspace.current_dir`, `context_window.used_percentage`), update the `pick(...)` calls to match.

## Step 3, turn it on

Add to `~/.claude/settings.json` (merge with what's there, never overwrite other settings):

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/usage-meter.py"
  }
}
```

On Windows use `python` instead of `python3` and the full path, for example `python C:/Users/<name>/.claude/usage-meter.py`.

## Step 4, test

Pipe a sample JSON into the script from the docs' example and check the line. Then restart Claude Code and confirm the bar shows. Tell the user what each part means in one line each, and that `/usage` shows their plan's limits in detail.
