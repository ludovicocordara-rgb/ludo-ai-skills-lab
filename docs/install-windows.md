# Install on Windows

## 1. Open PowerShell (not Command Prompt)

Press **Windows key + X** and click **Terminal** or **Windows PowerShell**. Do not pick anything that says **(x86)**.
The line must start with `PS`, like `PS C:\Users\YourName>`. No `PS` means you are in Command Prompt: close it and try again.

## 2. Claude Code

Paste this with **Ctrl + V** (or right-click) and press **Enter**:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Wait for `Claude Code successfully installed!`. Close the window, open a new PowerShell window, and check:

```powershell
claude --version
```

## 3. Log in

```powershell
claude
```

A browser window opens. Log in with your Claude account (the one with Pro). Type `/exit` to leave for now.

## 4. The lab

First install Git, which the lab's plugin marketplace needs. Paste this in PowerShell, not inside Claude:

```powershell
winget install --id Git.Git -e --source winget --accept-source-agreements --accept-package-agreements
```

If it says `'winget' is not recognized`, download Git from https://git-scm.com/downloads/win and click Next on every screen. Close the window and open a new PowerShell window, then:

```powershell
irm https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.ps1 | iex
```

## 5. Node.js (for the tools)

Download the **LTS** version from https://nodejs.org, run the installer, open a new PowerShell window, then:

```powershell
claude plugin install ludo-tools-windows@ludo-ai-skills-lab
```

WSL is not needed.

## Something went wrong?

See [troubleshooting.md](troubleshooting.md).
