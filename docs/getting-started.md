# Getting started

## 1. The three habits that matter most

- **Pick the model on purpose.** `/model sonnet` for almost everything. Opus and Fable are smarter and slower, and they use your Pro limit much faster.
- **Give context.** Claude only knows what it can see. `/ludo:about-me` once, then drop files in the folder and say who, what and why.
- **Start fresh often.** `/clear` between unrelated tasks. Long chats get worse, not better.

## 2. Your first session

```
mkdir my-lab
cd my-lab
claude
```

Then, one at a time:

```
/model sonnet
/ludo:about-me
```

Answer the interview. Claude writes `~/.claude/CLAUDE.md`, which it reads at the start of every session from now on.

Now use it:

> Based on what you know about me, find three professors at my school whose research fits my interests. Give me a link for each and one line on why.

Claude searches the web, reads the pages, and answers with sources.

## 3. Useful keys and commands

| Key or command | What it does |
|---|---|
| `Shift+Tab` | Switch permission mode: ask first, accept edits, plan mode, auto mode |
| `Esc` | Stop Claude mid-task |
| `/clear` | Start a fresh conversation in the same folder |
| `/compact` | Shrink the conversation into a summary to free up space |
| `/model` | Choose the model |
| `/usage` | See how much of your plan's limit you have left |
| `/ludo:` | List every lab skill |
| `#` then text | Save a rule to memory, like `# always answer in bullet points` |

## 4. Where to go next

- A project idea? `/ludo:idea-check`, then `/ludo:plan`.
- An exam coming? Drop your notes in a folder and run `/ludo:study`.
- Recruiting? `/ludo:resume`, then `/ludo:job-hunt`.
- Want Claude to use a real browser? See [tools.md](tools.md).
