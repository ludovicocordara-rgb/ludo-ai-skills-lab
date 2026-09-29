# Install on a Mac

## 1. Claude Code

Press **Cmd + Space**, type **Terminal**, press **Enter**. Paste this and press **Enter**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Wait for `Claude Code successfully installed!`. Quit Terminal fully (**Cmd + Q**), open it again, and check:

```bash
claude --version
```

You should see a version number.

## 2. Log in

```bash
claude
```

A browser window opens. Log in with your Claude account (the one with Pro). If it asks how to log in, choose your Claude subscription, not the Anthropic Console.

Type `/exit` to leave Claude for now.

## 3. The lab

```bash
curl -fsSL https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.sh | bash
```

It adds the lab, installs the skills and agents, and installs the tools if you have Node.js.

## 4. Node.js (for the tools)

Download the **LTS** version from https://nodejs.org, run the installer, then:

```bash
claude plugin install ludo-tools@ludo-ai-skills-lab
```

## Something went wrong?

See [troubleshooting.md](troubleshooting.md).
