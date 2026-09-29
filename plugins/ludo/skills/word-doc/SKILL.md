---
name: word-doc
description: Create or edit real Word documents (.docx) with proper headings, styles, tables, page numbers, footnotes and tracked-change-friendly edits, and export to PDF. Also reads .docx files. Use when the user says "Word doc", "docx", "make a document", "format this report", "memo", "cover letter file", "edit this Word file", or needs a document for a class or job that must be a .docx.
---

# Word doc

Many classes, jobs and applications still want a .docx. This skill makes clean, correctly structured Word files, not text pasted into a blank page.

## Tools

`pip install python-docx`. For PDF export, LibreOffice (free) or open the file in Word or Google Docs and export.

## Creating a document

1. Agree on the content first as plain text (or Markdown) and get a yes.
2. Build with real Word structure, so the document stays editable:
   - Headings as Heading 1, 2, 3 styles (so a table of contents and navigation work), not bold body text.
   - Body in one readable font (for example Calibri or Times New Roman 11 to 12pt), 1.15 line spacing, 1-inch margins unless the assignment says otherwise.
   - Real tables for tabular data, with a header row.
   - Page numbers in the footer, a title block at the top.
   - Footnotes or a references section as the style requires (see `/ludo:cite`).
3. Save as `<Title>.docx` and, if asked, a PDF next to it.

## Editing an existing .docx

- Read it first and summarize its structure.
- Change only what was asked. Keep the original's styles, fonts and layout.
- Save as a new file (`<name>-edited.docx`) unless the user says to overwrite.
- For documents others will review, list every change in a short summary so they can check it.

## Check

Convert to PDF (or render a page image) and look at it: headings consistent, no orphaned headings at the bottom of a page, tables not overflowing, page count as expected.

## Formatting rules for school and job documents

Follow the assignment's rules first (font, spacing, margins, header with name and date). Resumes: use `/ludo:resume`. Cover letters: one page, three short paragraphs, run `/ludo:sound-human` on it.
