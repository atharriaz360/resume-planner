// Builds 1-SELL-THIS/Career-Hub-Start-Here.pdf (2-page A4) from 5-SOURCE/guide/start-here.html.
// Usage: node 5-SOURCE/make-start-here.cjs   (uses Playwright; falls back to Puppeteer if Playwright is not installed)
const path = require('path'), fs = require('fs');
const root = path.resolve(__dirname, '..');
const src = 'file://' + path.join(__dirname, 'guide', 'start-here.html');
const out = path.join(root, '1-SELL-THIS', 'Career-Hub-Start-Here.pdf');
(async () => {
  let browser, page;
  try {
    const { chromium } = require('playwright');
    browser = await chromium.launch();
    page = await browser.newPage();
  } catch (e) {
    const pptr = require('puppeteer');
    browser = await pptr.launch();
    page = await browser.newPage();
  }
  try {
    await page.goto(src, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const pages = await page.evaluate(() => document.querySelectorAll('.page').length);
    const overflow = await page.evaluate(() => [...document.querySelectorAll('.page')].map(p => {
      const foot = p.querySelector('.foot').getBoundingClientRect().top;
      return Math.max(0, ...[...p.querySelectorAll('.card')].map(c => c.getBoundingClientRect().bottom - foot + 8));
    }));
    if (process.env.FORCE!=='1' && (pages !== 2 || overflow.some(v => v > 0))) throw new Error('Layout check failed: pages=' + pages + ' overflow=' + overflow.join(','));
    await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    console.log('Wrote ' + path.relative(root, out) + ' (' + fs.statSync(out).size + ' bytes)');
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exit(1); });
