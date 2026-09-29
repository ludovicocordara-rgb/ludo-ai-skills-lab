---
name: second-brain
description: Turn a messy folder of notes, readings, screenshots and downloads into an organized, linked set of Markdown notes that Claude can search and answer questions from. Use when the user says "organize my notes", "second brain", "make sense of this folder", "what do my notes say about", "connect my notes", or points Claude at a folder full of files. Works with Obsidian, which opens the result as a clickable graph.
---

# Second brain

Notes are only useful if you can find them again. This skill turns a pile into a small wiki: one note per idea, linked to related ideas, with an index on top. Everything stays as plain text files the user owns.

## Setup

1. Ask which folder is the brain, and whether to **reorganize in place** or **build a new organized copy** (recommend the copy, so nothing is lost).
2. Optional: suggest installing Obsidian (free, https://obsidian.md) and opening the folder as a vault. It shows the links as a graph. Everything also works without it.

## Structure

```
brain/
  index.md          start here: every topic, one line each
  inbox/            new stuff lands here, gets filed later
  topics/           one note per idea, concept or person
  sources/          one note per reading, lecture or video
  log.md            what changed and when
```

## Filing a source

For each file in the pile:
1. Read it.
2. Write a note in `sources/` with a 3 to 5 line summary, the key ideas, and where it came from (file name, link, date).
3. For each important idea, add it to the matching note in `topics/`, or create one. Link both ways with `[[double brackets]]`, which Obsidian understands.
4. Add a line to `index.md` for any new topic.

Keep the original files. Never delete or overwrite anything without asking.

## Rules for notes

- One idea per topic note. Title is the idea in plain words: `opportunity cost.md`, not `econ notes 3.md`.
- Write in the user's words where possible; quote the source when exact wording matters and say where it's from.
- Short. A topic note that grows past a page should split in two.

## Answering questions

When the user asks "what do my notes say about X":
1. Read `index.md`, then the relevant topic notes, then the sources they link.
2. Answer from the notes only, and link the note each point came from.
3. If the notes don't cover it, say so plainly and suggest what to add.

## Keeping it alive

When the user drops new files into `inbox/`, file them the same way and note it in `log.md`. Once a week, suggest merging duplicate topics and linking notes that should be connected.
