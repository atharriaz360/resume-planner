# Hero v10
Real screens only. No AI-rendered UI.
1. `node capture.cjs <abs path to 1-SELL-THIS/Career-Hub.html> <this folder>` → laptop.png (1560×923, under 52 px browser bar), phone.png (404×818, under 56 px iOS-style status bar), exec.pdf. Then `pdftoppm -f 1 -l 1 -scale-to-x 640 -scale-to-y -1 -png exec.pdf pg`.
2. Copy `~/Documents/KLabs/kaellabs-lockup-on-dark.svg` here as `logo.svg` (strip the <metadata> block). Not stored here to avoid a duplicate.
3. `node r.cjs` → hero.png 3000×2250, DSF 1. Screens drawn at native pixels (one render, no resample).
4. Export JPG q92, sRGB ICC, < 1 MB → `3-ETSY-LISTING/images/01-hero.jpg`.
Devices CSS-drawn, no brand logos. Logo per KLabs/LOGO-USAGE.md: right edge x 2360, top y 46, height 93, no background, drop-shadow only. Crop-safe: x 600–2400 (4:5), 375–2625 (1:1).
