# Resume layout and PDF checks

4 October 2026

Executive stays single-column. Mint Modern restores its two-column appearance, with plain-text contact details, education, skills and certifications on the left, and summary, work experience and projects on the right. The name and headline are centred above the columns. The divider follows the longer content column. Mint Modern keeps its colour choices; Executive keeps its classic navy serif name. The former layout table is replaced by CSS; contact icons and wide character spacing stay removed. Standard body text is 14px, approximately 10.5pt in the exported PDF.

PDF export clones the actual preview into the print frame, resets preview zoom and uses A4 printing; Mint Modern uses normal 12mm page margins to avoid Chrome fragment clipping. Normal experience and project entries stay together; oversized entries can flow across pages. Existing content-selection controls and saved template IDs remain compatible.

Checks:

- `node 5-SOURCE/check-resume-pdf.cjs`: generates sample PDFs from the actual print-frame HTML, checks absence of tables, images and SVG icons, exercises both styles, long content and mobile preview scaling; fails on JavaScript errors.
- Bundled Python `5-SOURCE/check-resume-text.py`: extracted PDF text matches all preview text after whitespace normalization; Executive headings retain a linear order; two-column extraction order varies by extractor, so Mint Modern is checked for preservation of all content; text remains inside page bounds. Longer resumes include the final added role with no empty pages.
- Sample PDF pages rendered with Poppler and visually reviewed. Both sample layouts take two pages; Executive long samples take four pages and Mint Modern long samples take three. No forced one-page compression or clipped content. The initial two-column fragmentation issue was fixed and the final long PDF rendered and reviewed.
- Buyer HTML and ZIP rebuilt from the source. Updated studio listing images and template descriptions match the new layouts.

This is text-extraction and visual validation, not certification by Greenhouse, Workday, or any other employer ATS. Enhancv has not been rerun. No universal 98+ score is claimed. Job-specific content and honest keywords still need to be supplied by each user. Sample data is fictional.

Reference: Greenhouse identifies table/column layouts, spaced letters and graphics among possible parsing issues: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse

## Awards, ordering and cover letters

Added editable Awards & Honours, saved section ordering, drag movement between Mint columns, and arrow controls for touch and keyboard use. Name and headline stay pinned. Edit controls are excluded from exported PDFs. Cover Letter reuses contact details, optionally fills tracked job details, saves the draft, and exports matching Executive or Mint styling.

`node 5-SOURCE/check-career-features.cjs` passes old-data migration, award create/edit/hide, drag movement, arrow ordering, reload persistence, profile editing from preview, cover draft saving and job details, both cover exports, mobile layout, and invalid-order cleanup. Both cover PDFs and the updated two-page guide were rendered and visually checked.

Professional Sidebar is a third style with a coloured right sidebar and white sidebar text. Resume accents are Mint, Teal, Steel, Amber and Slate; old Indigo/Plum resume selections fall back to Mint. Separate sidebar section order is saved. Sample and long PDF checks preserve all text across two and three pages respectively. Sample PDF visually reviewed.
