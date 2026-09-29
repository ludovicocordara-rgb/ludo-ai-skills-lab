---
name: cite
description: Make correct citations and bibliographies in APA, MLA or Chicago from a link, DOI, book title or PDF, and check the citations already in a paper. Use when the user says "cite this", "make a works cited", "bibliography", "APA", "MLA", "Chicago", "format my sources", or pastes a list of links for a paper.
---

# Cite

Citations are pure rules, which makes them perfect for Claude and miserable for people. The catch: a citation with a made-up detail is worse than none. This skill only uses details it actually found.

## Step 1, pick the style

If the user didn't say, ask once: APA 7, MLA 9, or Chicago (notes and bibliography, or author-date). If there is an assignment sheet or syllabus in the folder, read it first; it usually says.

## Step 2, get the real details for each source

For every source, find: authors, title, where it appeared (journal, site, publisher), date, volume and issue and pages if a journal, DOI or URL, and the date accessed for web pages if the style needs it.

- **DOI:** look it up at https://doi.org/<the DOI> or https://api.crossref.org/works/<the DOI>. Crossref returns the exact metadata.
- **Link:** open the page and read the byline, the title and the date on the page itself.
- **Book:** look it up by title on the publisher's site or Open Library.
- **PDF in the folder:** read the first page and the header or footer.

If a detail cannot be found, leave it out the way the style guide says to (for example "n.d." for no date in APA). Never guess an author or a date. Tell the user which sources are missing what.

## Step 3, format

- Follow the style exactly: capitalization, italics, punctuation, the order of names, "et al." rules, hanging indent.
- Sort the list the way the style requires (alphabetical by first author for APA and MLA).
- Give in-text citation examples for each source too: `(Rivera, 2024, p. 12)` for APA, `(Rivera 12)` for MLA.
- Output as a clean list the user can paste into Google Docs or Word. Italics stay italics.

## Checking an existing paper

When given a paper, check that:
- every in-text citation has a matching entry, and every entry is cited somewhere
- names, years and page numbers match between the two
- the formatting matches the chosen style

Report problems as a short list with the fix for each. Do not rewrite the paper.
