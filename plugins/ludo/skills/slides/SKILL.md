---
name: slides
description: Make a clean presentation from notes, a paper, an outline or a topic, as a single HTML file that runs in any browser and exports to PDF. Use when the user says "make slides", "presentation", "deck", "pitch deck", "turn this into slides", or has a class presentation or club meeting coming up.
---

# Slides

Most AI decks are walls of bullets on a template. A good deck has one idea per slide, big and clear, with the details in what the speaker says. This skill builds decks as one HTML file: no PowerPoint needed, opens in any browser, arrow keys to present, prints to PDF.

## Step 1, questions

Ask in one message, multiple choice:
- Who is the audience and how long is the talk? (5 min is about 6 slides, 15 min about 12)
- The one thing the audience should remember.
- Look: follow `/ludo:design`, or match a brand (school colors, club colors, a company's site)?
- Need a PDF, speaker notes, or both?

## Step 2, the outline first

Write the slide titles as full sentences that make the point, not labels. "Dining halls waste 30% of food on weekends" beats "Food waste". Show the outline and get a yes before building. Reading only the titles in order should tell the whole story.

## Step 3, build `slides.html`

Start from `templates/deck.html` in this skill's folder: it already has the layout, fonts, arrow-key navigation, speaker notes (N), fullscreen (F), a sample chart and print-to-PDF. Copy it, then replace the slides.

- One self-contained file: all CSS and JavaScript inline. Fonts load from Google Fonts when online and fall back to Georgia and the system font offline, so it always presents.
- 16:9 slides that scale to any screen. Arrow keys and clicks move between slides. Press F for fullscreen.
- Print CSS so File, Print, Save as PDF gives one slide per page.
- Speaker notes in a hidden element per slide; pressing N shows them.
- Design rules: one idea per slide, at most about 25 words on screen, one strong visual (chart, image, diagram, big number) where it helps. Two typefaces at most, one accent color. No bullet walls, no clip art, no gradients.
- Charts drawn with inline SVG from real numbers the user gave. Never invent data.
- Images only from the user's files or ones they approve; say where each came from.

## Step 4, check

Open it in the browser and go through every slide. Look for text overflowing the slide, text too small to read from the back of a room (nothing under about 24px at 1080p), and slides with more than one idea. Export the PDF and check the page count matches the slide count.

## PowerPoint or Google Slides

If the user needs a .pptx (for a class that requires it, or to edit in Google Slides), build it with the `python-pptx` library (`pip install python-pptx`) using the same outline and design rules, then open the file to check it.
