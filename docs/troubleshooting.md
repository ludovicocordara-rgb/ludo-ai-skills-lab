# Troubleshooting

## Installing Claude Code

| You see | Paste this, then open a new terminal window |
|---|---|
| Mac: `zsh: command not found: claude` | `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc` then `source ~/.zshrc` |
| Windows: `'claude' is not recognized` | `$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')` then `[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')` |
| Windows: `'irm' is not recognized` | You're in Command Prompt. Open PowerShell, or paste `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |
| Windows: `Could not create SSL/TLS secure channel` | `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12` then run the install line again |
| Windows: `does not support 32-bit Windows` | You opened the (x86) PowerShell. Open the normal one. |
| Mac: `dyld: cannot load` or `built for Mac OS X 13.0` | Your macOS is older than 13. Update in System Settings, Software Update. |

Still stuck: run `claude doctor` and show the output to a TA.

## Installing the lab

| Problem | Fix |
|---|---|
| `marketplace add` fails | Check your internet, then run the installer again. It's safe to run twice. |
| `/ludo:` shows nothing | Quit Claude (`/exit`) and start it again. Then `claude plugin list` should show `ludo`. |
| Tools don't start | Install Node.js LTS from nodejs.org, open a new terminal, run the tools install line again. |
| Windows: tools fail with `npx` errors | Make sure you installed `ludo-tools-windows`, not `ludo-tools`. |

## Python packages

| Problem | Fix |
|---|---|
| `pip install` says `externally-managed-environment` | Make a private environment in your project: `python3 -m venv .venv`, then `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`), then run the `pip install` again. Or just ask Claude to do it. |
| `python3` not found on Windows | Use `python` instead, or install Python from python.org and tick "Add to PATH". |

## Using Claude

| Problem | Fix |
|---|---|
| "Usage limit reached" | Wait for the reset shown, switch to `/model sonnet`, and `/clear` more often. `/usage` shows where you stand. |
| Claude seems to forget or get worse | The context is full. `/clear`, or `/compact`. Put lasting facts in CLAUDE.md with `/ludo:about-me` or `/ludo:remember`. |
| Claude keeps asking permission | Press `Shift+Tab` to switch to accept-edits or auto mode once you trust the task. |
| Login browser doesn't open | Press `c` to copy the login link, paste it in your browser. |
