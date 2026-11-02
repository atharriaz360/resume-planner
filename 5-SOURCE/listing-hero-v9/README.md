# Career Hub listing video v9

Final video: `6-ETSY-LISTING/Career-Hub-Listing-Video-v9.mp4`. Hero: `3-ETSY-LISTING/images/01-hero-premium-refined.jpg`.

## Timeline

- 0–3.4 s: real Executive-to-Mint template change. Click appears within first second. Same Jordan Lee data.
- 3.4–6.6 s: real saved application move, Applied to Interviewing. Motion overlay uses the actual card capture; before/after are real saved states.
- 6.6–9.1 s: choose a tracked job; real company/role fields update in the cover letter. Existing letter prose stays unchanged, as the app specifies.
- 9.1–11.8 s: real PDF output preview beside the real mobile tracker. Browser print invocation is verified; the print document is saved using Chromium PDF output.
- 11.8–14.8 s: exact final hero composition, brief zoom settles by 12.4 s, then a still hold through the final frame.

No opening blank frame, no invented countdown, no hiring promise, no offline tag or byline added. Navy/cream/gold follows the final hero rather than the generic rose brand brief. Crossfades take 0.35 s. Designed for silent autoplay; loop returns directly to the product interaction rather than fading to black. This is not a seamless matching-frame loop.

## Build

From repository root, with Puppeteer installed:

```sh
node 5-SOURCE/listing-hero-v9/capture.cjs
node 5-SOURCE/listing-hero-v9/render.cjs
python3 5-SOURCE/listing-hero-v9/qa.py
```

Render uses `FFMPEG` if set, otherwise the existing local `/private/tmp/kaellabs-video-deps/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1`. Set it to your FFmpeg executable if needed. QA currently uses the same local binary path. Pillow required for the contact sheet.

`video.html` is the 3000 × 2250 scene source, scaled 0.48 for 1440 × 1080 output. `window.R(t)` controls every frame. `video-render.html` binds the verified capture coordinates. `capture-proof.json` records action results. `qa-report.json` records codec, size and last-frame comparison. `contact-sheet.jpg` shows sixteen frames at 480 px width.

VERIFIED: 14.80 s, 30 fps, H.264, yuv420p, faststart, no audio, under 100 MB. Last-frame mean pixel difference from the hero is below 4/255 after compression. No app JavaScript errors during capture. Previous upload preserved in `6-ETSY-LISTING/archive/`.

INFERENCE: This sequence makes the main product actions easier to understand quickly. UNKNOWN: conversion performance, ranking or live Etsy acceptance/crop. The exact final hero is user-selected and includes AI-rendered screen text; interaction captures do not.
