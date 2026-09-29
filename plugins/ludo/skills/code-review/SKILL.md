---
name: code-review
description: Review code before it goes live, looking for real bugs, security holes, leaked secrets and confusing parts, explained in plain English and ranked by how much they matter. Use when the user says "review my code", "is this safe to deploy", "check my code", "anything wrong with this", or before putting a project on the internet or GitHub.
---

# Code review

A review is useful when it finds the few things that will actually hurt, not when it lists fifty style nitpicks. This skill looks for problems that break things, leak data or embarrass the user, and explains each so a beginner understands.

## Scope

Ask what to review: the whole project, one file, or only what changed since the last commit (`git diff`). Read all of it before writing anything.

## What to look for, in order

1. **Secrets**: API keys, passwords or tokens written in code or committed to git, and `.env` files not listed in `.gitignore`. Anything already pushed to a public repo must be treated as leaked: the key needs to be revoked and replaced, not just deleted.
2. **Security**: user input used directly in database queries, shell commands or HTML; pages that should need a login but don't; files anyone can overwrite.
3. **Bugs**: code paths that will crash (empty lists, missing values, a file that isn't there), wrong math, off-by-one errors, results silently thrown away.
4. **Data loss**: anything that deletes or overwrites without asking or without a backup.
5. **Confusing parts**: code the user won't understand in a month. Only mention the worst one or two.

Skip pure style unless it hides a bug.

## How to report

For each finding:
- **Severity**: must fix before going live / should fix / nice to have
- **Where**: file and line
- **What happens**: the concrete failure, like "if someone submits the form empty, the page crashes"
- **Fix**: the change, briefly

Most severe first. Stop at about ten findings; if there are more, say how many and list the worst.

## Rules

- Only report things you can point to in the code. Say how sure you are when unsure.
- Don't change the code during a review unless the user asks. Offer to fix the "must fix" items next.
- If you find a live secret, tell the user immediately, before the rest of the review.
