---
name: powerpoint
description: Create or edit real PowerPoint files (.pptx) that also open cleanly in Google Slides and Keynote, with a proper layout, readable type, real charts, speaker notes, and a render check of every slide. Use when the user says "PowerPoint", "pptx", "Google Slides", "edit this deck", "the class requires PowerPoint", or needs slides as a file rather than a web page.
---

# PowerPoint

For a quick talk, `/ludo:slides` makes a web deck. When a class, club or company needs a .pptx (or Google Slides), this skill builds a real one, editable by anyone.

## Tools

`pip install python-pptx`. To check the result, LibreOffice renders slides to PDF and images. To get it into Google Slides, upload the .pptx to Google Drive and open it with Google Slides.

## Building a deck

1. **Outline first**: slide titles as full sentences that make the point. Get a yes.
2. **Set up**: 16:9 (13.33 x 7.5 in). One blank layout, your own text boxes, so it looks designed rather than templated.
3. **Design** (see `/ludo:design`): two fonts at most (Google Fonts names work in Google Slides), one accent color, big readable type (titles 32 to 44pt, body at least 16pt), generous margins.
4. **Content**: one idea per slide, at most about 25 words on screen. Details go in the speaker notes.
5. **Charts**: from real numbers the user provided, as native charts or clean images. Never invent data.
6. **Speaker notes** on every slide: what to say, in a few lines.

## Editing an existing deck

Read every slide first and list them. Change only what's asked, keep the original's fonts, colors and layouts. Save as a new file.

## Check every slide (required)

Render to PDF and images and look at each one:
- text overflowing its box or the slide
- titles wrapping into the content below (Google Slides renders fonts a little wider than PowerPoint, so leave slack)
- anything smaller than 14pt
- images stretched or pixelated

Fix, re-render, and look again until clean.
