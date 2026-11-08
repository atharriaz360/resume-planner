# Career Hub: Etsy listing kit

Listing: https://www.etsy.com/listing/4588508397 · Shop: KaelLabs · Section: Career & Job Search
Audit date: 2026-11-08. Product tested: `1-SELL-THIS/Career-Hub.html` (byte-identical to `2-HOST-ONLINE/index.html`, v1.1).
Evidence labels: VERIFIED = file inspected or test run · INFERENCE = judgment · UNKNOWN = not checked.

## Live listing baseline (pasted from Etsy editor, 2026-11-08)

- Title: `ATS Resume Builder App | Cover Letter + Job Tracker | 24 Styles | Offline PDF` (77 chars)
- Category: Résumé Templates (digital). Occasion: Graduation. Price: USD 14.27. Listed: 04 Oct 2026.
- Files: `Career-Hub.zip` (506 KB), `Career-Hub-Start-Here.pdf` (717 KB). VERIFIED: 2 of 5 files, both allowed types, both under 20 MB.
- How it's made: "Created by me" selected. 12 photos, 1 video.
- UNKNOWN: views, visits, orders, conversion, search terms, impressions, reviews. Not supplied. Export Etsy Stats (last 30 days + all time) to fill this in.

## Technical audit (runtime: headless Chromium, Playwright, file:// open)

| Section | Item | Status | Evidence | Fix |
|---|---|---|---|---|
| Offline | Network requests from downloaded file | PASS | 0 non-file requests across 8 views | — |
| Offline | Private link offline (service worker) | UNKNOWN | `sw.js` present, not tested | Test on a phone in airplane mode |
| Storage | Save → reload → reopen in new tab | PASS | Edited name incl. emoji + Arabic survived reload and new tab | — |
| Storage | IndexedDB + localStorage + memory fallback, persist() | PASS (code) | `indexedDB.open`, `onupgradeneeded`, `onblocked`, `onversionchange`, `navigator.storage.persist` present | Quota/blocked paths not run |
| Backup | Export backup | PASS | Downloads `career-hub-backup.json` (17,183 bytes, demo data) | — |
| Backup | Restore good / bad / non-JSON file | PASS | Good: "Backup restored". Bad schema + junk: "Invalid backup — data unchanged" | — |
| Security | HTML/script in name field + malicious backup | PASS | `<img onerror>` payload did not run; 20 `innerHTML` uses go through `E()` escaping | — |
| Core | Demo data, 24 designs, tracker, contacts, playbook | PASS | 24 `focus-design` options; statuses Wishlist/Applied/Interviewing/Offer/Rejected; 5 demo contacts with next date; "THE 12 GOLDEN RULES" | — |
| PDF | Text-based PDF | PASS (Chromium) | `pdftotext` extracts resume + cover letter text; fonts embedded | Safari/Firefox print not tested |
| Layout | 390 px phone, horizontal scroll | PASS | scrollWidth = 390 on all 8 views | — |
| A11y | Text under 10.5 px on phone Hub | FAIL | 15 text nodes | Raise to ≥ 10.5 px tokens |
| A11y | Tap targets under 44×44 on phone Hub | FAIL | 3 elements | Pad to 44 px |
| Hygiene | `!important` | Low | 57 uses, mostly print CSS | Document or reduce |
| Hygiene | Duplicate IDs at runtime | PASS | 0 on Hub and Resume | — |
| Errors | JS errors | PASS | 0 across all runs | — |
| Compat | Safari, iOS, iPadOS, Android, Firefox, Edge, Windows | UNKNOWN | Not tested | Test before claiming |
| Known-bug list in audit prompt | Guest list, Wedding Party, falcons | N/A | That list is from another project | — |

Gate: SHIP for the app. FIX for the listing images (see below).

## Etsy rules applied (user-checked on Etsy, 2026-11-08)

- Digital items must show a visual preview or excerpt of what buyers get. Mockups allowed. AI-edited images must not change the item's design or features.
- AI use must be disclosed in the description. No required position or wording.
- Max 5 files, 20 MB each; .zip and .pdf allowed.

## Images

| # | File | Status | Note |
|---|---|---|---|
| 1 | `images/01-hero.jpg` | NEW, SAFE | Real screens at native pixels in drawn, logo-free devices; navy scene; iPhone status bar (time, signal, Wi-Fi, battery); KaelLabs on-dark lockup top-right inside 4:5 zone. 3000×2250, JPG, sRGB, 799,750 bytes. Source: `5-SOURCE/hero-v10-source/` |
| 12 | `images/12-visual-preview-or-excerpt.jpg` | SAFE | Unedited real Resume Builder screenshot, 3000×2250, JPG, sRGB. No crop, overlay or text. Move it to position 2 |
| 2–6, 10 | AI-assisted scenes | VERIFY | Check that every screen in them is a pasted real screenshot, not AI-redrawn text |
| 7 | `07-every-screen.jpg` | CHANGE | "MacBook Pro" printed on the laptop (brand name). Phone/tablet claims are untested |
| 8 | `08-pay-once-how-it-works.jpg` | CHANGE | Lists Mac, Windows, Chromebook, iPhone, Android, iPad and Safari: not tested |
| 9 | `09-experience-bank.jpg` | VERIFY | Large person photo: confirm you hold the rights. Unrelated to the product |
| Video | `video/Career-Hub-Listing-Video.mp4` | CHANGE | Last 3 s show the old AI-rendered hero. Re-render with `01-hero.jpg` |

Old hero `01-hero-premium-refined.jpg` was removed: its screen and cover-letter text were AI-redrawn and garbled (Etsy rule 3 risk).

### Alt text
- 1: `Career Hub resume builder app open in a browser on a laptop, showing the Executive resume layout with example name Jordan Lee, a phone showing the job application tracker, and the printed PDF resume on a walnut desk. Headline: Resume Builder plus Cover Letter and Job Tracker. Labels: 24 resume designs, Text-based PDF, Pay once.`
- 12: `Unedited screenshot of the Career Hub resume builder: template list on the left, Mint Modern resume with example data in the middle, and document completion checks on the right.`

## Title (draft; finalize after eRank)
- Keep live title until eRank results are in.
- Draft A (107 chars, 14 words): `Resume Template Builder, Cover Letter, Job Application Tracker, 24 Designs, Text-Based PDF, No Subscription`
- Removed from draft: "Offline PDF" (unclear phrase). "ATS" kept only in tags: no ATS test exists.

## Tags
- Live (13, all ≤ 20 chars): `resume template, ats resume template, ats friendly resume, ats resume, cover letter, resume template 2026, cv template, resume builder, job tracker, resume cover letter, student resume, resume pdf, career planner`
- Change pending eRank: `ats friendly resume` (unproven claim), `resume pdf`, `career planner` (weak intent).

## Description (ready to paste)

```
Resume builder app with a matching cover letter and job application tracker. Pick from 24 resume designs, save a text-based PDF and keep every application in one place. Instant digital download. Pay once, no subscription, no account. AI tools helped with parts of the code, some listing images and this text. The screens shown are the real app with example data.

WHAT'S INSIDE
- 24 resume designs: 3 layouts x 4 colours x 2 header styles
- Single-column Executive layout
- Matching cover letter that can fill in the company and role from a tracked job
- Job application tracker: Wishlist, Applied, Interviewing, Offer, Rejected
- Experience bank: write your roles, education and skills once and reuse them
- Contacts with last-contact and next follow-up dates
- Playbook with 12 golden rules for applying
- Hub showing your next step and upcoming follow-ups
- Completion and format checks before you export
- A4 or US Letter page size
- Light and dark mode

YOU GET
- Career-Hub.zip: the app (one HTML file), the Start Here PDF and the licence
- Career-Hub-Start-Here.pdf as a separate file
- A private online link for phone and tablet, listed in the Start Here guide

HOW IT WORKS
1. Download and unzip Career-Hub.zip
2. Open Career-Hub.html in your web browser, or tap your private link on your phone
3. Fill in your details once, pick a design and review the checks
4. Save as PDF from the print window
5. Add jobs to the tracker and set follow-up dates

YOUR DATA, SAVING AND BACKUP
- Everything you type is saved in the browser on the device you use. Nothing is sent to a server
- No cloud sync. Your data does not move between devices or browsers by itself
- The downloaded file and the private link keep separate data
- Clearing browser data or using private browsing can erase your entries
- Use Settings, Export backup often. Use Restore backup to move to a new device or browser

GOOD TO KNOW
- Digital download. Nothing physical is shipped. Devices and props in the photos are not included
- The downloaded file makes no internet requests, so it works offline
- Output is PDF only. Not a Word, Google Docs or Canva file
- No resume tool can promise how every applicant tracking system (ATS) reads a file. Follow each employer's instructions
- This is a preparation tool, not career, legal or hiring advice. Hiring decisions rest with each employer, and no job or interview is guaranteed
- No lifetime updates are promised
- Personal use licence for you and your household. No sharing or resale

Questions, or a file won't open? Message me on Etsy.
```

Changes vs live: added no-sync, data-loss risk, backup/restore, AI disclosure moved to the first paragraph, no-advice line (resume version; the "not veterinary advice" line does not apply to this product), "No lifetime updates are promised." Removed browser list, "Works offline" without scope, "ATS results vary" (replaced). The line "Safari and iOS have not been independently verified." does not exist in the live copy or project files (grep, 2026-11-08).

## Note to buyers (replace live note: it has emoji and an untested browser/offline claim)
```
Thank you for your purchase. To get your files: Etsy, You, Purchases and orders, Download files. Unzip Career-Hub.zip and open the Start Here PDF first. It explains setup, your private phone link and how to back up your data. Personal use only, no sharing or resale. If anything won't open, message me on Etsy.
```

## Other listing settings
- Category Résumé Templates: KEEP (INFERENCE).
- Occasion Graduation: KEEP (INFERENCE: students/graduates are a stated audience).
- How it's made: VERIFY. AI assisted with code and images; Etsy's "With an AI generator" option may be the accurate choice. Decide before relisting.
- Price USD 14.27: UNKNOWN position. No competitor data collected this run.

## Start Here guide fix (next run)
- `5-SOURCE/guide/start-here.html:158` "Works with" chips (Mac, Windows, Chromebook, iPhone & iPad, Android, Chrome, Edge, Safari, Firefox) and lines 90 and 97: untested. Reword, rebuild PDF and ZIP.

## eRank: copy into eRank bulk keyword research, first batch
```
resume builder, resume template, ats resume template, ats resume, resume and cover letter, resume cover letter template, cover letter template, job tracker, job application tracker, job search tracker, job search planner, job hunt tracker, resume builder app, digital resume template, resume template pdf, one page resume, modern resume template, professional resume template, simple resume template, student resume template, graduate resume, entry level resume, career change resume, resume template 2026, cv template, cv builder, executive resume template, single column resume, minimalist resume, resume planner, job application organizer, interview tracker, job search organizer, career planner, resume template us letter, resume template a4, resume kit, resume bundle, offline resume builder, no subscription resume
```
Send the results back to finalize title and tags.
