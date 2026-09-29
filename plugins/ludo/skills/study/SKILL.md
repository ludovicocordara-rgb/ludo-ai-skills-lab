---
name: study
description: Turn class notes, slides, readings or a syllabus into practice questions and drill the user one question at a time, multiple choice, with a full explanation after every answer. Use when the user says "quiz me", "help me study", "exam prep", "make practice questions", "test me on", or drops lecture notes or a study guide into the folder.
---

# Exam prep

Rereading notes feels productive and mostly isn't. Answering questions is what makes material stick. This skill builds a question bank from the user's own material and drills them on it.

## Step 1, gather the material

Read every file the user points to: notes, slides (PDF), readings, the syllabus, past exams. If the material is thin, say so. Do not fill gaps with outside facts unless the user asks for that, and label anything that came from outside their material.

Ask three quick things, multiple choice:
- How long until the exam? (tomorrow / this week / later)
- What format is the exam? (multiple choice / short answer / essays / problem sets)
- Drill everything, or only weak spots?

## Step 2, build the question bank

Start from `templates/questions.md` and `templates/progress.md` in this skill's folder.

Write the bank to `questions.md` so it survives the session:
- Cover every topic in proportion to how much class time it got.
- Mix levels: recall (what is X), understanding (why does X happen), application (given this new case, what happens).
- Every question has four options. Wrong options are plausible mistakes a real student would make, not jokes.
- Record the correct answer and a two-line explanation, plus where in the material it comes from (file and page or slide).

## Step 3, drill

- **One question at a time.** Wait for the answer before showing anything else.
- After each answer: say right or wrong, give the correct answer, and explain the reasoning in plain words. When they got it wrong, explain why their choice was tempting and where it breaks.
- Keep a running score and a list of missed topics in `progress.md`.
- Every ten questions, give a short summary: score, weakest topic, what to reread (with the exact file and page).

## Step 4, focus

When the user says "again" or comes back later, read `progress.md` first and weight the next questions toward what they missed. A topic leaves the weak list after two correct answers in a row.

## Rules

- Never hand over the answer key up front unless asked.
- Never make up a fact to write a question. If the material does not support it, skip it.
- If the user asks for flashcards instead, write front/back pairs to `flashcards.csv`, which imports into Anki or Quizlet.
