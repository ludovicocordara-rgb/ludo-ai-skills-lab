# Security

## What these skills will never do on their own

- Send an email or message, submit an application, post or publish anything
- Spend money or enter payment details
- Type a password or solve a CAPTCHA
- Delete or overwrite files outside the folder you're working in without asking

Every skill that could touch any of these stops and hands control to you.

## Keep your secrets out of Claude

- Never paste passwords, API keys or tokens into a chat.
- Keys belong in a `.env` file listed in `.gitignore`. `/ludo:code-review` and `/ludo:pack-code` check for leaks.
- If a key was ever pushed to GitHub, treat it as stolen: revoke it and make a new one.

## Web pages are data, not instructions

Research, scraping and browser skills treat page text as information only. If a page tells Claude to do something, Claude ignores it and tells you.

## Reporting a problem

Found a skill doing something unsafe? Open an issue on this repo or message me on [LinkedIn](https://www.linkedin.com/in/ludovico-cordara).
