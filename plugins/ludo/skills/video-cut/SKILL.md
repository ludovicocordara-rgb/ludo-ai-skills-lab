---
name: video-cut
description: Edit phone videos from the terminal with ffmpeg, including trimming, joining clips, cutting dead air, adding captions, changing to vertical 9:16 for Reels and TikTok, fixing volume, adding music and exporting at the right size. Use when the user says "edit this video", "make a reel", "cut this clip", "add captions", "make it vertical", "compress this video", or drops a .mov or .mp4 file.
---

# Video cut

ffmpeg can do most of what a basic video editor does, in seconds, without uploading anything. This skill plans the cut with the user, runs ffmpeg, and checks the result.

## Setup (once)

- ffmpeg: Mac `brew install ffmpeg` (needs Homebrew, brew.sh), Windows `winget install ffmpeg`.
- For captions: `pip install openai-whisper` to transcribe (slow on a laptop; for a short clip it's fine).

## Step 1, look before cutting

Run `ffprobe` on every clip: length, resolution, frame rate, audio track. Tell the user what you found in one or two lines. Phone videos are often vertical already (1080x1920), and audio can end slightly before the video.

## Step 2, agree on the cut

Write the plan as a simple list: clip, start, end, what happens there. For talking videos, transcribe first and cut on sentence boundaries. Get a yes before rendering.

## Step 3, common recipes

| Job | Command idea |
|---|---|
| Trim | `ffmpeg -ss 00:00:05 -to 00:00:20 -i in.mov -c:v libx264 -c:a aac out.mp4` (re-encode for frame-exact cuts) |
| Join | Write `list.txt` with `file 'a.mp4'` lines, then `ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4` (same format clips only; otherwise re-encode) |
| Vertical 9:16 | `-vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"` |
| Burn captions | Make an .srt from the transcript, then `-vf subtitles=captions.srt:force_style='FontSize=18,Outline=2'` |
| Normalize volume | `-af loudnorm=I=-14:TP=-1.5:LRA=11` (about right for social media) |
| Add music under voice | `-filter_complex "[1:a]volume=0.15[m];[0:a][m]amix=inputs=2:duration=first"` |
| Compress | `-c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k` |

Keep every cut inside the audio track's length so sound stays in sync, and snap cuts to whole frames.

## Step 4, check

Extract a few frames (`-vf fps=1`) and look at them, especially right after each cut. Report the final length, size and resolution. Never overwrite the originals.

## Rules

Only edit footage the user owns or has permission to use. Music must be something they have rights to (royalty-free libraries, or the platform's own music inside the app).
