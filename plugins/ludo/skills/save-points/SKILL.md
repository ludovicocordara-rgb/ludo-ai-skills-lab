---
name: save-points
description: Use git as save points, so any project can be rolled back to a version that worked, with plain-English explanations and nothing scary. Covers first-time setup, saving, seeing what changed, undoing, trying ideas on a branch, and putting code on GitHub. Use when the user says "save my progress", "undo", "go back to when it worked", "git", "GitHub", "branch", "I broke everything", or before any risky change.
---

# Save points

Git is a save-point system for folders. Each save (a "commit") is a snapshot you can return to. With it, breaking something is never permanent.

## First time on this computer

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check git exists with `git --version`. Mac: it offers to install developer tools the first time. Windows: install Git for Windows (git-scm.com).

## Everyday moves, in plain English

| You want to | Say to Claude | What happens |
|---|---|---|
| Start tracking a folder | "Turn this folder into a git project" | `git init`, plus a `.gitignore` for secrets and junk |
| Save a point | "Save a save point: login works" | `git add` + `git commit -m "Login works"` |
| See what changed | "What changed since the last save?" | `git status` and `git diff`, explained |
| See the history | "Show my save points" | `git log --oneline` |
| Undo unsaved changes to a file | "Put this file back how it was" | `git restore <file>` (asks first) |
| Go back to an old save | "Go back to when login worked" | shows the list, confirms, then restores safely |
| Try something risky | "Try this on a branch" | `git switch -c experiment`, and you can drop it if it fails |
| Put it on GitHub | "Put this on GitHub, private" | `gh repo create` (needs the GitHub CLI and a login) |

## Rules Claude follows

- **Save before risky changes**, and after anything that works.
- **Never commit secrets.** `.env` and key files go in `.gitignore` before the first commit. If a key was ever committed and pushed, treat it as leaked: revoke it and make a new one.
- **Ask before anything destructive**: `reset --hard`, deleting branches, force-push, or restoring over unsaved work. Explain what would be lost first.
- **Private by default** when creating a GitHub repo, unless the user says public.
- Commit messages say what works now, in plain words.
