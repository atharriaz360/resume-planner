# Career Hub listing v2 (2026-10-27)

Photos: `3-ETSY-LISTING/images-v2/` (2700x2026, 4:3). Video: `3-ETSY-LISTING/video/Career-Hub-Listing-Video.mp4`.
Source (scripts + HTML): `5-SOURCE/listing-v2-source.zip`. Backgrounds: `5-SOURCE/canva-bg/` (13 = hero, 15, 16, 17, 19, 20, 21, 22).
Every screen is a real Career Hub screen with the built-in demo data, composited into the green screens by chroma key + perspective warp.

## Upload order
Photos 01–10 in file order (alt text in `ETSY-LISTING-KIT.md`), video in slot 2.

## Video timeline (14.8 s, 1440x1080, 30 fps, H.264 High, no audio)
| Time | Beat | Caption | On screen |
|---|---|---|---|
| 0–2.2 | Hook (dim, cool) | Job hunt feeling scattered? | Laptop + phone visible, floating notes: resume_FINAL_v7.docx, jobs-list.xlsx, follow-up question |
| 2.2–4.6 | Step 1 · Experience bank | Fill in once. Reuse it. | Notes fly into the laptop, lamp light warms, tap Save → real toast "Profile saved" |
| 4.6–7.0 | Step 2 · Resume styles | Pick a style. Done. | Push-in, two real template taps: Executive → Mint left → Mint centred |
| 7.0–9.0 | Step 3 · Job tracker | Track every application. | Drag Interviewing card to Offer → real toast "Moved to Offer" |
| 9.0–11.8 | Step 4 · Save as PDF | Save as a PDF. | Tap Download PDF → real toast "Choose Save as PDF…", printed resume appears on the desk |
| 11.8–14.8 | End | (hero) | Crossfade into photo 1, 3% push-in, loops back to hook |

## Claims check
No "ATS-approved", no "#1/best", no job or interview promises, no reviews. "24 resume styles" = 3 layouts × 4 colours × 2 headers. "Text-based PDF", "Pay once", "Works offline", "No account" all match the app and the listing description. Photo 8 states output is PDF, not Word/Canva.

## Rebuild
Unzip the source into the project root next to `2-HOST-ONLINE/`, then: capture.py / cappaper.py / capphone.py / capvid2.py (screens) → scenes.py + make13.py + scene13.py (composites) → render.py hero.html / render2.py slides.html (photos) → recvid.py + ffmpeg (video). Needs Python Playwright, OpenCV, Pillow, ffmpeg, @fontsource/dm-serif-display.
