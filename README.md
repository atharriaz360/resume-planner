# Career Hub

Resume builder, cover letters, experience bank and job tracker. Canonical app: `2-HOST-ONLINE/index.html` (v1.1).

## Folders

- `1-SELL-THIS/`: buyer HTML, two-page Start Here guide, licence and buyer ZIP.
- `2-HOST-ONLINE/`: hosted app (private buyer link) with manifest + service worker for Add to Home Screen and offline use.
- `3-ETSY-LISTING/`: listing images, interaction video and listing copy/alt text.
- `4-BRAND/`: editable brand assets.
- `5-SOURCE/`: guide source (`guide/start-here.html`), builders and checks. Test/render outputs are temporary and ignored.

## Build and verify

Install development dependencies with `npm ci` (Puppeteer; Playwright is used for the guide when installed, Puppeteer otherwise).

1. `node 5-SOURCE/make-start-here.cjs` — 2-page A4 guide → `1-SELL-THIS/Career-Hub-Start-Here.pdf`
2. `python3 5-SOURCE/build-release.py` — copies the app and rebuilds `Career-Hub.zip`
3. `for f in 5-SOURCE/check-*.cjs; do node "$f" || break; done` — 16 browser checks
4. `python3 5-SOURCE/build-project.py`

Phone layout (≤700px): bottom menu with Hub, Experience, Resume, Tracker and More (Cover Letter, Contacts, Playbook, Settings, appearance).

The private online link and the downloaded file use separate browser storage. Use Export/Restore backup to move a workspace. Deploy `2-HOST-ONLINE/` to Vercel after changes.
