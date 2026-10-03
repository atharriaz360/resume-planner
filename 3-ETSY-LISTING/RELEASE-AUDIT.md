# Career Hub release audit
Checked 4 October 2026.

## Passed
- Hosted-source index.html and buyer Career-Hub.html are byte-identical, SHA-256 prefix 13666e180b47ab25.
- ZIP integrity passed; its HTML, two-page PDF, and licence match current loose files exactly. No rebuild needed.
- All 24 automated action/storage checks passed: save, edit, delete/cancel, reload, demo isolation, backup/restore, reset safeguards, appearance, notes, and rendering without script errors. These are simulated DOM tests, not a full device/browser certification.
- Guide names, URL, PDF steps, backup guidance and household licence match the app.
- Kit title and 13 tags describe current functions; each tag fits 20 characters.
- Restored full-size selected hero to images/01-hero.png, 3000 x 2400. Updated kit references to existing files. AI mockup has altered small UI text; it is not a pixel-exact screenshot.

## Required image corrections before publishing
02: replace Download PDF caption with Save as PDF to match current app.
03: clarify seven RESUME accents versus five WORKSPACE accents; replace industry-fit wording with Choose a resume accent. Autosave applies to appearance controls, not every form.
04: replace Never miss a follow-up with Review upcoming follow-ups; Next best action with Suggested next step; readiness is setup completion, not resume quality. Screenshot contains old dashboard labels.
05: dates on cards are follow-up dates, not applied dates; replace Add jobs in seconds with Add and update jobs.
07: remove in minutes, what employers look for, and fully organised; use Select relevant experience, Practical preparation guides, and Keep search details together.
08: replace Your whole resume. One page. with Preview your resume. Long content can span pages.
09: clarify applications are submitted outside Career Hub; include headers/footers off alongside 100% scale and background graphics.
10: replace All you need to get hired. with Your job search workspace.
06: no material caption mismatch found in overview inspection.

These supporting images have NOT been edited. No blanket copyright clearance or sales-outcome guarantee is given.

## Deployment and device limits
Live Vercel website could not be fetched by the web tool. Local release correctness does not prove the website is deployed at the same revision. Git has uncommitted changes; no commit, push or deployment was performed. Test actual Safari/iPhone PDF saving before claiming full compatibility.

Verdict: app/package locally consistent; listing image set needs corrections before publishing.
