---
name: resume
description: Build or fix a clean one-page resume as a Word file (and PDF), in a classic finance and consulting format. Use when the user says "fix my resume", "build my resume", "make my bullets better", "resume", "CV", or pastes resume text and asks for changes.
---

# Resume builder

One format, one script, one page. The format is the classic one recruiters in finance, consulting and tech expect: Times New Roman, bold centered name, a contact line with working email and LinkedIn links, bold section headers with a thin rule underneath, organization in bold italic with the date on the right margin, an italic role line, round bullets.

## Setup (once)

```
pip install python-docx
```

For a PDF you also need LibreOffice (free). Without it, open the .docx in Word or Google Docs and export to PDF.

## The loop

1. **Get the current resume.** Ask the user to paste it or drop the file in the folder. Read it fully.
2. **Ask everything at once**, multiple choice, recommended option first: class year, which roles stay, what an unclear role actually involved, whether high school stays (first-years: one short line; later years: drop it).
3. **Draft the text first** as one plain block the user can read and copy. Get a yes before building the file.
4. **Write the JSON.** Copy `examples/sample.json`, fill it with the user's content, save it in their folder.
5. **Build.**
   ```
   python3 <this skill's folder>/scripts/build_resume.py resume.json Lastname_Firstname_Resume.docx --pdf
   ```
   The script prints the page count and stops with an error if it runs over one page.
6. **Fit one page.** First fix bullets that wrap onto a second line by one or two words. Then shorten the longest bullets. Then remove the weakest bullet. Never shrink the font or the margins.
7. **Check.** Open the PDF and look at it. List what you changed on your own judgment and anything the user must confirm.

## Writing rules

- **No invented facts.** Every number, name, date and tool comes from the user or from a public source you actually read (the employer's own website). Ask for a number rather than making one up.
- **Start each bullet with a strong verb** and end with a result: what changed because of the work. "Built a Google Sheets tracker that cut weekly stockouts from 6 to 1" beats "Responsible for inventory".
- **Make a thin role concrete** with what the employer publicly says it does. The claim stays the user's; the context comes from the company.
- **Tense per bullet.** Ongoing work in present tense, finished results in past tense, even inside a current job. Past jobs all past tense.
- **GPA goes as a labeled line** under the school: `["Cumulative GPA", ": 3.8/4.0"]`. Leave it off if it hurts more than it helps, and ask.
- **Keep real, specific interests.** "History of the Silk Road" starts a conversation; "reading and travel" does not. Never add an interest the user does not have.
- **One page.** Always.

## JSON cheat sheet

| Field | Shows up as |
|---|---|
| `org` | bold italic. Add the trailing comma and space yourself: `"Example College, "` |
| `loc` | italic, right after org |
| `date` | pushed to the right margin: `"09/2025 - Present"` |
| `title` | italic role line under the org |
| `bullets` | plain round bullets |
| `labelled` | bullet with a bold italic label, for GPA and coursework |
| `kv` | section-level lines with a bold label, for Skills & Interests |
