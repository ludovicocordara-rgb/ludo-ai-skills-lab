# Ludo's AI Skills Lab

**50 skills, 4 agents and 2 power tools that turn Claude Code into a research assistant, tutor, analyst, designer and engineer.** One install. Works on Mac and Windows.

Built by [Ludovico Cordara](https://www.linkedin.com/in/ludovico-cordara), founder of [Krypton AI](https://kryptonai.io), for the AI Skills Lab at the Claremont Colleges, run with the Randall Lewis Center for Innovation and Entrepreneurship and Anthropic.

---

## Install in one line

You need [Claude Code](https://code.claude.com/docs/en/quickstart) and a Claude Pro (or higher) plan. Then:

**Mac** (Terminal)
```bash
curl -fsSL https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.sh | bash
```

**Windows** (PowerShell)
```powershell
irm https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.ps1 | iex
```

Or from inside Claude Code:
```
/plugin marketplace add ludovicocordara-rgb/ludo-ai-skills-lab
/plugin install ludo@ludo-ai-skills-lab
```

Then start Claude in any folder with `claude` and type `/ludo:` to see everything. New here? Start with **`/ludo:about-me`**.

Step-by-step guides: [Mac](docs/install-mac.md) · [Windows](docs/install-windows.md) · [Troubleshooting](docs/troubleshooting.md)

---

## What you get

### Skills: type the command, or just ask in plain English

| | |
|---|---|
| **Start here** | `about-me` teaches Claude who you are (and adds the lab's working rules) · `ask-first` · `brainstorm` · `plan` · `short-answers` · `remember` · `usage-meter` · `prompt-coach` |
| **Research and the web** | `research` answers with a link on every fact · `deep-research` writes a full cited report · `scrape` pulls any website into a spreadsheet · `whats-new` covers the last 30 days · `video-notes` turns lectures into notes |
| **School** | `study` quizzes you from your notes · `explain` · `paper` helps you write, you stay the author · `cite` formats APA, MLA and Chicago · `second-brain` |
| **Career** | `resume` · `job-hunt` scores postings and tracks applications · `pitch` · `idea-check` |
| **Finance** | `comps`, `dcf`, `lbo` and `three-statement` build live Excel models · `earnings` · `equity-note` · `stock-pitch` |
| **Make things** | `design` · `mockup` · `brand-kit` · `slides` · `powerpoint` · `word-doc` · `diagram` · `spreadsheet` · `pdf` · `video-cut` · `sound-human` |
| **Daily life** | `morning` briefs your day from Gmail and Calendar · `journal` |
| **Build and ship code** | `code-carefully` · `test-first` · `fix-it` · `code-review` · `save-points` (git, explained) · `pack-code` · `autopilot` · `make-skill` builds your own skills |

Full list with descriptions: [docs/skills.md](docs/skills.md)

### Agents: helpers Claude sends off on side jobs

`researcher` · `checker` · `tutor` · `fixer`. All run on Sonnet to protect your Pro limits. [docs/agents.md](docs/agents.md)

### Tools (needs [Node.js](https://nodejs.org))

- **chrome**: a private Chrome window Claude can open, click, read, screenshot and debug websites in. Preconfigured with a throwaway profile (your real logins are never touched), smaller screenshots to save your limits, and usage tracking off.
- **docs**: current documentation for any coding library, so Claude stops writing code for old versions.

Details: [docs/tools.md](docs/tools.md)

### Connect your Gmail, Calendar and Drive

Free with Pro, switched on in claude.ai settings. Guide and safety rules: [docs/connectors.md](docs/connectors.md)

---

## Your first 20 minutes

1. `mkdir my-lab && cd my-lab && claude`
2. `/model sonnet` so you don't burn through your weekly limit
3. `/ludo:about-me` and answer Claude's questions. It writes your CLAUDE.md.
4. Ask something that uses it: *"Based on what you know about me, find three professors at my school whose research fits my interests, with links."*
5. `/ludo:usage-meter` so you always see your model and how full the context is.

More in [docs/getting-started.md](docs/getting-started.md).

---

## Updating

```
claude plugin marketplace update ludo-ai-skills-lab
claude plugin update ludo@ludo-ai-skills-lab
```

What changed: [CHANGELOG.md](CHANGELOG.md)

## Safety

Skills never send email, submit applications, spend money or publish anything without you. Tools run in a separate browser profile. Never paste passwords or API keys into Claude. See [SECURITY.md](SECURITY.md).

## Contact

[GitHub](https://github.com/ludovicocordara-rgb) · [LinkedIn](https://www.linkedin.com/in/ludovico-cordara) · [Krypton AI](https://kryptonai.io)

MIT License © 2026 Ludovico Cordara
