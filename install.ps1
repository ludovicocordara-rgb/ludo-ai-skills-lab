# Ludo's AI Skills Lab installer for Windows (PowerShell).
#   irm https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.ps1 | iex
$ErrorActionPreference = "Stop"
$Repo = "ludovicocordara-rgb/ludo-ai-skills-lab"
$Market = "ludo-ai-skills-lab"
function Say($t) { Write-Host "`n$t" -ForegroundColor Cyan }

Say "Ludo's AI Skills Lab"

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  Write-Host "Claude Code is not installed yet. Install it first:"
  Write-Host "  irm https://claude.ai/install.ps1 | iex"
  Write-Host "Then open a NEW PowerShell window and run this installer again."
  return
}

Say "1/3  Adding the lab's plugin marketplace"
claude plugin marketplace add $Repo
if ($LASTEXITCODE -ne 0) { claude plugin marketplace update $Market }

Say "2/3  Installing skills and agents (ludo)"
claude plugin install "ludo@$Market"

Say "3/3  Installing tools (ludo-tools-windows)"
if (Get-Command npx -ErrorAction SilentlyContinue) {
  claude plugin install "ludo-tools-windows@$Market"
} else {
  Write-Host "Skipped: the browser and docs tools need Node.js."
  Write-Host "Get it from https://nodejs.org (the LTS button), then run:"
  Write-Host "  claude plugin install ludo-tools-windows@$Market"
}

Say "Done."
Write-Host "Start Claude in any folder with:  claude"
Write-Host "Then type /ludo: to see every skill, or start with /ludo:about-me"
