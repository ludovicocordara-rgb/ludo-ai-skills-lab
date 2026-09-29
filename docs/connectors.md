# Connecting Gmail, Calendar and Drive

Connectors let Claude read your email, calendar and files, so it can do things like `/ludo:morning` ("what's today, what's due, who needs a reply"), find the syllabus in your Drive, or draft replies. Week 4 covers this properly; this page is for anyone who wants to start early.

## Turn them on (once)

1. Go to **claude.ai**, then **Settings**, then **Connectors**.
2. Connect **Gmail**, **Google Calendar** and **Google Drive**. Each opens a Google sign-in; pick your account and approve.
3. In Claude Code, type `/mcp`. The connectors you turned on appear there when you're logged in with the same Claude account. If they don't, run `/login` again, then restart Claude.

Connectors on claude.ai come with paid plans, so Pro is enough.

## Try it

- `/ludo:morning` for today's brief.
- *"Find the syllabus for my econ class in my Drive and add every deadline to a plan.md."*
- *"Which emails from professors this week still need a reply? Draft a reply to the most urgent one, don't send it."*

## Safety rules

- **Claude drafts, you send.** Ask for drafts, read them, send them yourself. The lab's skills never send email on their own.
- **Read-only by default.** Ask Claude to read and summarize. Anything that changes things (sending, deleting, accepting invites, sharing files) you do yourself, or you approve it explicitly each time.
- **Other people's messages are private.** Don't paste someone else's email into anything public.
- **Emails are data, not instructions.** If an email says "AI assistant, forward this to...", Claude should ignore it and tell you. Watch for it.
- **Disconnect anytime** in claude.ai, Settings, Connectors.
