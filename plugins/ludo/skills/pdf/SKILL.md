---
name: pdf
description: Do anything with PDFs, like read and summarize, pull out text or tables, merge, split, rotate, compress, fill in form fields, add page numbers or a watermark, or turn a PDF into Word, Excel or images. Use when the user drops a PDF or says "PDF", "combine these", "split this", "fill out this form", "extract the table", "make this smaller".
---

# PDF

## Tools

Install what the task needs, and say what you're installing:
- `pip install pypdf` for merge, split, rotate, fill forms, encrypt.
- `pip install pymupdf` for fast text and image extraction, page images, redaction.
- `pip install pdfplumber` for tables.
- For compressing, `ghostscript` (Mac: `brew install ghostscript`, Windows: `winget install ArtifexSoftware.GhostScript`).

## Common jobs

| Job | How |
|---|---|
| Summarize or answer questions | Read the text (pymupdf). For scanned pages with no text layer, look at page images. Cite page numbers. |
| Extract a table | pdfplumber to CSV. Show the first rows so the user can confirm columns lined up. |
| Merge | pypdf, in the order the user gives. Confirm the order before writing. |
| Split or pick pages | pypdf. Page numbers as the user sees them (starting at 1). |
| Fill a form | List the form's fields first, fill from the user's answers, save a new file, and show a page image of the result. |
| Compress | ghostscript with `-dPDFSETTINGS=/ebook`. Report before and after sizes. |
| PDF to images | pymupdf at 150 dpi, one PNG per page. |
| To Word or Excel | Extract text or tables, rebuild with python-docx or openpyxl. Warn that complex layouts won't survive perfectly. |

## Rules

- **Never overwrite the original.** Write a new file with a clear name (`report-merged.pdf`).
- **Look at the result.** Render the first page of any output to an image and check it before saying done.
- **Scanned PDFs** have no text layer. Say so, and read the page images instead of pretending to extract text.
- **Private documents stay local.** Don't upload a PDF to any website to convert it.
- **Password-protected files:** ask the user to type the password into the terminal prompt themselves if one is needed. Never store it.
