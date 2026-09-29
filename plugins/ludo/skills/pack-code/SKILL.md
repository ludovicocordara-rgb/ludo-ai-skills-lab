---
name: pack-code
description: Pack a whole project folder into one clean text file (a table of contents, then every relevant file with its path) so it can be pasted into ChatGPT, Gemini, Claude on the web, or shared with a mentor for review. Skips junk like node_modules, images, secrets and build output. Use when the user says "pack my code", "one file", "send my project to ChatGPT", "share my code", "get a second opinion", or wants another AI to look at the whole project.
---

# Pack code

Other AI tools can't see your folder. Pasting files one by one loses the structure. This skill writes the whole project into one file, `packed.md`, in a format any AI reads well.

## What goes in

- Every source and text file: code, configs, Markdown, CSVs under about 200 lines.
- At the top: the project name, today's date, a one-paragraph description (from the README or plan.md), and a tree of the folder.
- Then each file as:
  ````
  ## path/to/file.py
  ```python
  ...contents...
  ```
  ````

## What stays out (always)

- Secrets: `.env` files, anything named like `*key*`, `*secret*`, `*token*`, `credentials*`. Also scan file contents for strings that look like API keys (long random strings starting with `sk-`, `ghp_`, `AKIA`, and similar) and replace them with `[REDACTED]`. Tell the user what was redacted.
- Dependencies and build output: `node_modules/`, `.venv/`, `venv/`, `dist/`, `build/`, `.next/`, `__pycache__/`, `.git/`
- Binary files: images, PDFs, videos, zip files, databases. List them in the tree but don't include contents.
- Anything matched by `.gitignore`.
- Large data files: include the first 20 lines and a note on the total size.

## How

This skill ships a ready script, `scripts/pack.py` (standard Python, nothing to install):

```
python3 <this skill's folder>/scripts/pack.py <project folder> -o packed.md
python3 <this skill's folder>/scripts/pack.py <project folder> -o packed.md --review   # adds a review request on top
```

On Windows use `python` instead of `python3`. The script prints the file count, the size, a rough token count, how many secrets it redacted, and a warning over 400,000 characters. Then open `packed.md` and skim it so the user can confirm nothing private slipped in before sharing.

## Asking for a review

If the user wants a second opinion, add a short request at the very top of `packed.md`, like: "Review this project for bugs, security problems and anything confusing. Rank issues by severity, and quote the file and line for each."
