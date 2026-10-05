# Career Hub

Resume builder, cover letters, experience bank and job tracker. Canonical app: `2-HOST-ONLINE/index.html`.

## Folders

- `1-SELL-THIS/`: buyer HTML, two-page guide, licence and buyer ZIP.
- `2-HOST-ONLINE/`: hosted app and required offline/PWA files.
- `3-ETSY-LISTING/`: final ten images, interaction video and listing copy/alt text. Capture scripts and their required reference inputs remain alongside them.
- `4-BRAND/`: editable brand assets.
- `5-SOURCE/`: maintained builders and checks. Test/render outputs are temporary and ignored.

## Build and verify

Install development dependencies with `npm ci`. Python guide generation needs reportlab; PDF text checks need pdfplumber/pypdf.

1. `python3 5-SOURCE/make-guide.py`
2. `python3 5-SOURCE/build-release.py`
3. `node 5-SOURCE/check-audit.cjs`
4. `node 5-SOURCE/check-header-design.cjs`
5. `node 5-SOURCE/check-document-sizes.cjs`
6. `node 5-SOURCE/check-resume-pdf.cjs`
7. `node 5-SOURCE/check-release.cjs`
8. `python3 5-SOURCE/build-project.py`

The buyer ZIP contains only the standalone HTML, PDF guide and licence. The project ZIP includes maintained source, final seller assets and buyer files; excludes Git, dependencies, secrets, drafts and test outputs.

The public website and downloaded app use separate browser storage. Use JSON backup/restore to transfer entries. Local edits are not deployed automatically.
