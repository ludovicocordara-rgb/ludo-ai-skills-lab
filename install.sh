#!/usr/bin/env bash
# Ludo's AI Skills Lab installer for Mac and Linux.
#   curl -fsSL https://raw.githubusercontent.com/ludovicocordara-rgb/ludo-ai-skills-lab/main/install.sh | bash
set -euo pipefail

REPO="ludovicocordara-rgb/ludo-ai-skills-lab"
MARKET="ludo-ai-skills-lab"
say() { printf '\n\033[1m%s\033[0m\n' "$1"; }

say "Ludo's AI Skills Lab"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is not installed yet. Install it first:"
  echo "  curl -fsSL https://claude.ai/install.sh | bash"
  echo "Then open a NEW Terminal window and run this installer again."
  exit 1
fi

say "1/3  Adding the lab's plugin marketplace"
claude plugin marketplace add "$REPO" || claude plugin marketplace update "$MARKET"

say "2/3  Installing skills and agents (ludo)"
claude plugin install "ludo@$MARKET"

say "3/3  Installing tools (ludo-tools)"
if command -v npx >/dev/null 2>&1; then
  claude plugin install "ludo-tools@$MARKET"
else
  echo "Skipped: the browser and docs tools need Node.js."
  echo "Get it from https://nodejs.org (the LTS button), then run:"
  echo "  claude plugin install ludo-tools@$MARKET"
fi

say "Done."
echo "Start Claude in any folder with:  claude"
echo "Then type /ludo: to see every skill, or start with /ludo:about-me"
