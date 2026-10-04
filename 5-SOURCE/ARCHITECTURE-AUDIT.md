# Architecture and UI audit

4 October 2026. Scope: this project, centred on `2-HOST-ONLINE/index.html`. All findings below were fixed. Original line numbers refer to the source at the start of this audit; final line numbers refer to the current source.

| Original FAIL | Problem | Fix | Final location |
|---|---|---|---|
| `2-HOST-ONLINE/index.html:399` (load()) | localStorage overrode IndexedDB. | IndexedDB → localStorage → memory read order. | `2-HOST-ONLINE/index.html:406` |
| `2-HOST-ONLINE/index.html:338` (idb()) | Blocked opens could leave startup waiting forever. | Bounded open; blocked or failed opens use the fallback. | `2-HOST-ONLINE/index.html:342` |
| `2-HOST-ONLINE/index.html:339` (idbGet()/idbSet()) | Storage transactions had no bounded fallback. | Timeouts and abort/error handling. | `2-HOST-ONLINE/index.html:343` |
| `2-HOST-ONLINE/index.html:398` (save()) | Fast edits could enqueue overlapping writes without an explicit order. | Snapshots written through a serial save queue. | `2-HOST-ONLINE/index.html:405` |
| `2-HOST-ONLINE/index.html:380` (migrate()) | Migration stopped at v3; v4 features depended on defaults. | Explicit v3 → v4 → v5 migrations. | `2-HOST-ONLINE/index.html:386` |
| `2-HOST-ONLINE/index.html:380` (migrate()/load()) | Future version data could be normalized down and overwritten. | Newer versions rejected; existing storage kept read-only. | `2-HOST-ONLINE/index.html:386` |
| `2-HOST-ONLINE/index.html:409` (SCH.applications) | Salary stored as free text. | Integer cents, currency, optional notes; old ranges preserved and currency symbols migrated. | `2-HOST-ONLINE/index.html:418` |
| `2-HOST-ONLINE/index.html:571` (BANKVIEW.profile) | Profile form bypassed SCH + DEF + input(). | Shared schema and cleaning. | `2-HOST-ONLINE/index.html:421` |
| `2-HOST-ONLINE/index.html:488` (coverLetterUI()) | Cover letter inputs duplicated schema logic. | SCH.cover + DEF.cover + input(); editing routed through A. | `2-HOST-ONLINE/index.html:497` |
| `2-HOST-ONLINE/index.html:429` (openDlg()) | Dialog actions used assigned onclick/onsubmit handlers. | Delegated data-act submit and delete actions in A. | `2-HOST-ONLINE/index.html:439` |
| `2-HOST-ONLINE/index.html:762` (submit handler) | Profile save bypassed A. | profile-save action dispatched by the form. | `2-HOST-ONLINE/index.html:723` |
| `2-HOST-ONLINE/index.html:754` (input/change handlers) | Notes and cover edits bypassed A. | Central note-edit and cover-edit actions; unsafe note keys rejected. | `2-HOST-ONLINE/index.html:720` |
| `2-HOST-ONLINE/index.html:424` (input()) | Field keys, labels, and types were not escaped; required select/textarea handling incomplete. | E() at schema output boundaries; required applied to all field types. | `2-HOST-ONLINE/index.html:433` |
| `2-HOST-ONLINE/index.html:426` (clean()) | Cleaning copied submitted keys instead of schema allowlisting. | Only schema fields accepted. | `2-HOST-ONLINE/index.html:435` |
| `2-HOST-ONLINE/index.html:737` (tpl/raccent actions) | Template/colour actions lacked value allowlists. | Allowed template IDs and accent keys only. | `2-HOST-ONLINE/index.html:751` |
| `2-HOST-ONLINE/index.html:428` (showDlg()) | Focus chose the close icon before the form; return focus not explicit. | First editable field receives focus; focus returns on close. | `2-HOST-ONLINE/index.html:438` |
| `2-HOST-ONLINE/index.html:17` (theme CSS) | Light Emerald/Amber button colours and status labels had weak text contrast. | Darker light accent colours, theme-aware status text; primary button contrast tested. | `2-HOST-ONLINE/index.html:17` |
| `2-HOST-ONLINE/index.html:133` (template CSS) | Selected hint text kept muted colours on the selected background. | Hints inherit selected button text colour. | `2-HOST-ONLINE/index.html:133` |
| `2-HOST-ONLINE/index.html:330` (RESUME_ACCENTS) | White sidebar text on Mint had insufficient contrast. | Deeper Mint (#0b7c73); every sidebar accent ≥ 4.5:1. | `2-HOST-ONLINE/index.html:334` |
| `2-HOST-ONLINE/index.html:451` (checkBadges()) | Confetti and “Resume Master” implied more than setup completion. | Quiet “Setup complete” badge; old badge labels migrate. | `2-HOST-ONLINE/index.html:460` |
| `2-HOST-ONLINE/index.html:160` (motion/touch CSS) | No reduced-motion override; some touch controls were small. | Reduced-motion styles and 44px coarse-pointer controls. | `2-HOST-ONLINE/index.html:183` |
| `2-HOST-ONLINE/sw.js:4` | Activation deleted every origin cache. | Only Career Hub cache names are removed. | `2-HOST-ONLINE/sw.js:4` |
| `3-ETSY-LISTING/studio-refresh/LISTING-READY.md:23`; `3-ETSY-LISTING/ETSY-LISTING-KIT.md:64`; `5-SOURCE/make-listing-art.py:16` | Copy omitted the third style and claimed seven resume colours. Older hero instructions selected an artificial mockup. | Three layouts, five resume colours, current screenshots; supporting graphics regenerated. | Same files, current release |

## Checks passed

- Headless Chrome: all 8 views in light/dark at 1440px and 390px. 34 screenshots saved in `output/audit/`. No page overflow, missing field labels or unnamed buttons in tested views. Zero console errors or uncaught page errors.
- Storage: IndexedDB priority, denied IndexedDB → localStorage, both denied → memory, stuck database open → fallback, serial saves, salary reload, newer-version protection.
- Migrations: old v3 data → v5; old amounts become integer cents; free-text salary ranges kept as notes. Currency symbols map to GBP/EUR/USD.
- Forms/actions: schema fields, profile and awards editing, cover autosave, salary CRUD, modal focus/Escape, HTML injection escaping, allowed template/colour values.
- Contrast: primary button/selected hint pairs for all five workspace accents in both themes, plus white sidebar text on all five resume colours. Tested ratios ≥ 4.5:1, recorded in `output/audit/contrast-results.json`.
- Resume regression: all three layouts, selectable text, no layout tables/graphics, sample and long exports, mobile sizing. Mint and Executive text checks preserve all sample content.
- Career features: awards CRUD/hide, drag movement, arrows, saved ordering, profile preview editing, cover drafts and both cover PDF styles.
- Buyer HTML and ZIP rebuilt; ZIP integrity and byte equality verified. Current hero/template/tracker/playbook/cover images regenerated.

## Evidence and limits

Run `node 5-SOURCE/check-audit.cjs`, `node 5-SOURCE/check-career-features.cjs`, `node 5-SOURCE/check-sidebar.cjs`, and `node 5-SOURCE/check-resume-pdf.cjs`. Use bundled Python for `5-SOURCE/check-resume-text.py`.

Screenshots were reviewed locally. These checks cover the rules and scenarios above. They do not certify every browser, screen reader, operating system or employer ATS. No 98+ ATS score, hiring outcome or sales result is promised. Live deployment and Etsy publication were not performed.

Etsy copy follows clear product names and relevant keywords, factual feature descriptions, actual product screenshots, and thumbnail crop review. Sources: [Etsy title guidance](https://www.etsy.com/uk/seller-handbook/article/1399426136697), [listing checklist](https://www.etsy.com/seller-handbook/article/27130654583), [listing anatomy](https://www.etsy.com/ca/seller-handbook/article/1347574487014).
