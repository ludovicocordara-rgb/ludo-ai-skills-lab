---
name: diagram
description: Draw a clear, good-looking diagram (a flowchart, process, system map, timeline, org chart, comparison, cycle or concept map) as a clean SVG or HTML file. Use when the user says "diagram", "flowchart", "draw how this works", "visualize this process", "timeline", "map this out", or when an explanation would be clearer as a picture.
---

# Diagram

A diagram should explain something faster than words can. Most generated diagrams fail because they show everything at once, in default colors, with arrows crossing everywhere. This skill draws fewer boxes, clearer paths and calm styling.

## Step 1, decide what it must show

Ask or infer: what question does the diagram answer? ("How does a request get from the browser to the database?", "What happens after I apply?") Then pick the form:

| Question | Form |
|---|---|
| What happens in what order | flow, left to right |
| How parts connect | system map with grouped boxes |
| When things happen | timeline |
| Who reports to whom | tree |
| What repeats | cycle |
| How options compare | side-by-side table-diagram |

## Step 2, sketch in text first

List the boxes (5 to 9 is ideal, never more than 12) and the arrows between them, with a two-to-four word label on each arrow. Show this list and adjust before drawing.

## Step 3, draw

Output one file, `diagram.svg` or `diagram.html` with inline SVG, that opens in any browser.

Style:
- Off-white background, near-black lines and text, one accent color for the single most important path or box.
- Thin 1.5px lines, square or slightly rounded boxes, no shadows, no gradients, no 3D.
- One typeface, labels at least 14px, sentence case.
- Arrows flow in one main direction. Rearrange boxes until no arrows cross; if they must, use a small bridge.
- Group related boxes in a light outlined region with a small label, instead of coloring every box differently.
- Numbered steps when order matters.

## Step 4, check

Open it. Can someone who hasn't read the notes explain it back in 30 seconds? Remove any box they wouldn't miss. Check at phone width if it's going on a website.

For a quick version inside Markdown or GitHub, a Mermaid code block is fine. For anything someone will present or publish, draw the SVG.
