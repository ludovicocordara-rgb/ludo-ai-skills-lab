---
name: video-notes
description: Turn a YouTube video, recorded lecture, podcast or any video or audio file into clean notes with timestamps, key points and a summary, and answer questions about it. Use when the user pastes a YouTube link or drops a video or audio file and says "notes", "summarize", "what did they say about", "watch this", or "I missed this lecture".
---

# Video notes

Claude cannot press play, but it can read a transcript and look at frames. This skill gets the transcript, then writes notes worth reading.

## Step 1, tools (one time)

Check for these and install what is missing, telling the user what you are installing:
- **yt-dlp** for downloading captions and videos. Mac: `brew install yt-dlp`. Windows: `winget install yt-dlp`. Or `pip install yt-dlp`.
- **ffmpeg** only if you need frames or audio. Mac: `brew install ffmpeg`. Windows: `winget install ffmpeg`.

## Step 2, get the words

In order of preference:
1. **Existing captions** (fastest, free):
   ```
   yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*" --sub-format vtt -o "video" "<link>"
   ```
   Clean the .vtt into plain text: drop the timing lines and the repeated lines auto-captions produce, but keep a timestamp every minute or so.
2. **A transcript the user already has** (Zoom, Panopto and Canvas often provide one). Ask before downloading anything.
3. **No captions at all:** tell the user. Transcribing audio needs a speech-to-text tool such as Whisper (`pip install openai-whisper`), which is slow on a laptop. Ask before starting it.

Only download from sites and videos the user has the right to use. Course recordings stay on their machine.

## Step 3, look at slides if they matter

For lectures with slides or diagrams, grab a frame every minute or two with ffmpeg and look at the ones where the transcript refers to something on screen ("as you can see here").

## Step 4, the notes

Save to `notes-<short title>.md`:

```markdown
# <Title>, <speaker>, <date if known>
Link: <url>

## In one paragraph
## Key points
- Point, with timestamp [12:40]
## Definitions and formulas
## Examples used
## Things to look up
```

- Every key point gets a timestamp so the user can jump to it.
- Use the speaker's own terms and numbers. Never add facts that aren't in the video; outside context goes under "Things to look up" and is labeled.

## Step 5, questions

After the notes, the user can ask anything about the video. Answer from the transcript and cite the timestamp. If the video doesn't cover it, say so.
