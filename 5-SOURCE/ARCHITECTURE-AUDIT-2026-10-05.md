# Career Hub audit — 5 October 2026

Scope: 2-HOST-ONLINE/index.html and its buyer release, tests, guide and listing images. Earlier audit remains historical. Line numbers below refer to the final source.

## Failures found and fixed

| Location | Failure | Fix |
|---|---|---|
| 2-HOST-ONLINE/index.html:262 | Cover contact stack and header spacing wasted space. | Compact wrapping contact row; smaller Mint header bottom padding. |
| 2-HOST-ONLINE/index.html:266 | User reported Executive letter did not match the resume banner. | Verified shared Executive banner rules apply to the cover; matching name, headline, icons and accent. |
| 2-HOST-ONLINE/index.html:515 | Design settings split across oversized cards. | One grouped Design panel, dividers, named colour controls with selected ticks, segmented alignment. |
| 2-HOST-ONLINE/index.html:637 | Text-only template cards gave weak visual guidance. | Three miniature layout previews, readable labels and selected tick. |
| 2-HOST-ONLINE/index.html:285 | Experimental pinned export overlapped colour/actions on short screens. | Removed overlap; visible export card in normal flow. |
| 5-SOURCE/check-header-design.cjs:4 | Screenshot navigation raced the view render. | Wait for the destination controls before capture and next interaction. |
| 5-SOURCE/check-career-features.cjs:14 | Test used a removed inline profile button. | Test the current profile action; retain edit and save assertions. |
| 3-ETSY-LISTING/ETSY-LISTING-KIT.md:133 | Copy still said five resume accent changes. | Four resume accents; distinct from five workspace themes. |
| 2-HOST-ONLINE/sw.js:2 | Cache name predated control-panel polish. | Incremented cache identifier. |
| 1-SELL-THIS/Career-Hub.html:1 | Buyer copy could drift from hosted source. | Rebuilt byte-identical HTML, guide and ZIP. |
| 3-ETSY-LISTING/images/02-templates.jpg | Product screenshots predated current design. | Regenerated supporting images, hero laptop capture and cropped resume previews. |

## Architecture results

PASS: IndexedDB first, localStorage fallback, memory fallback; serialized saves and blocked-storage handling.
PASS: version 6 migration, old salary conversion, saved shared header alignment; newer backups rejected safely.
PASS: SCH + DEF + input() forms; labelled fields and controlled options.
PASS: delegated A / data-act actions; escaped user content through E().
PASS: integer cents for salaries, editable money fields and save/reload.
PASS: light/dark variables, readable Mist text, keyboard modal handling and labelled controls.
PASS: three layouts, four resume accents, both header alignments and matching cover-letter headers.
PASS: native section movement, keyboard arrow controls, awards CRUD and saved order.

## Verification

Headless Chromium: check-audit.cjs, check-header-design.cjs, check-career-features.cjs, check-sidebar.cjs and check-resume-pdf.cjs. Final audit and header checks recorded zero console/page errors. Desktop and mobile light/dark screenshots are in output/audit; eight matching-header screenshots in output/audit/headers.

Actual print-frame PDFs: all three layouts, both letter styles, long-content and mobile checks. Text checks preserve Executive/Mint content, no clipped text or blank continuation pages in the tested fixtures. These checks do not guarantee a universal ATS score or every browser/printer result. Browser headers/footers are a user print setting.

Images 01–10 refreshed where affected. Existing user-supplied phone and letter reference images remain in the hero; original files preserved. Historical video has an older palette and is explicitly marked as such in the listing kit; it was not rerecorded in this image refresh.

No unresolved failures in the listed final checks. Custom colours were not added: four curated choices keep document contrast predictable.
