const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    headless: "new"
  });
  const page = await browser.newPage();
  
  // Set viewport to a large size so everything renders
  await page.setViewport({ width: 3000, height: 2500, deviceScaleFactor: 1 });
  
  const htmlPath = 'file://' + path.resolve(__dirname, 'generator.html');
  console.log('Loading ' + htmlPath);
  await page.goto(htmlPath, { waitUntil: 'networkidle0' });

  // Get all slide elements
  const slides = await page.$$('.slide');
  console.log(`Found ${slides.length} slides.`);

  const outDir = path.resolve(__dirname, 'images');
  if (!fs.existsSync(outDir)){
      fs.mkdirSync(outDir);
  }

  for (let i = 0; i < slides.length; i++) {
    const slide = slides[i];
    const numStr = (i + 1).toString().padStart(2, '0');
    let title = 'slide';
    
    // Map slide index to a nice name based on the order we defined
    const names = [
      'hero', 'whats-included', 'compare-templates', 'customizable', 
      'cover-letters', 'dark-light-mode', 'job-tracker', 'experience-bank', 
      'contacts', 'playbook', 'privacy', 'purchase-steps'
    ];
    
    if (i < names.length) {
      title = names[i];
    }
    
    const outPath = path.join(outDir, `${numStr}-${title}.png`);
    
    console.log(`Capturing slide ${numStr}: ${outPath}...`);
    await slide.screenshot({ path: outPath });
  }

  await browser.close();
  console.log('All screenshots captured successfully.');
})();
