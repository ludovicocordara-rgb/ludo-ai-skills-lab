---
name: job-hunt
description: Run an internship or job search from the terminal. Scores job postings against the user's background, finds the real requirements and red flags, tailors the resume and a short note for each application, and keeps a tracker of every application and deadline. Use when the user says "job hunt", "internship search", "should I apply", "tailor my resume for this", "track my applications", or pastes a job posting or link.
---

# Job hunt

Most students apply to too many roles with one generic resume, and lose track of what they sent where. This skill makes each application count and keeps the whole search in one folder.

## Setup (once)

In a folder called `job-hunt`:
- `me.md`: what the user wants (roles, industries, cities, dates, pay floor, visa needs) and what they bring. Build it by interviewing them, or pull from their CLAUDE.md and resume.
- `resume.json` or their resume file (see `/ludo:resume`).
- `tracker.csv` with columns: `company, role, link, found, deadline, score, status, applied_on, contact, next_step, notes`

## Scoring a posting

Read the full posting (use `/ludo:research` or `/ludo:scrape` if it needs a login). Then write a short report:

1. **Summary**: role, team, location, dates, pay if listed, deadline.
2. **Must-haves vs nice-to-haves**: split the requirements. Most postings list wishes as requirements.
3. **Fit, 1 to 5**, with reasons: where the user clearly matches, where they partly match, real gaps.
4. **Red flags**: vague role, unpaid, "rockstar", huge requirement list for an intern, no company info, reposted for months.
5. **Verdict**: apply now, apply with a tweak, or skip, in one line.

Add the row to `tracker.csv` with the score and status `to apply`.

## Tailoring

For roles worth applying to:
- Reorder and reword resume bullets so the most relevant ones come first, using the posting's own terms where they truthfully fit. Never add a skill, tool or result the user doesn't have.
- Draft a short note (under 120 words) for a cover letter field, a recruiter message or an alum: why this team, one proof point, one ask.
- Save each version as `applications/<company>-<role>/` with the resume and the note, so the user always knows what was sent.

The user submits and sends everything themselves. Claude never submits an application or sends a message.

## Finding roles

When asked to find openings: search company career pages, school job boards the user can access, and reputable boards. Log each find in the tracker with the link and the date found. Prefer postings less than 30 days old.

## Weekly check

When the user says "job hunt status": read the tracker, list deadlines in the next 7 days, applications with no reply after 10 days (suggest a polite follow-up), and a count by status.
