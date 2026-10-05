const puppeteer=require(process.cwd()+'/node_modules/puppeteer');
const fs=require('fs'),path=require('path');
(async()=>{
 const out=path.resolve('3-ETSY-LISTING/images');
 const browser=await puppeteer.launch({headless:true});try{
 const p=await browser.newPage();await p.setViewport({width:1440,height:1050,deviceScaleFactor:1});await p.goto('file://'+path.resolve('2-HOST-ONLINE/index.html'));await p.waitForSelector('#nav a');await p.click('#nav a[href="#settings"]');await p.waitForSelector('[data-act="sample"]');await p.click('[data-act="sample"]');await p.click('#nav a[href="#resume"]');await p.waitForSelector('[data-act="tpl"]');
 for(const [template,file] of [['executive','06-executive.png'],['mint','07-2column.png'],['sidebar','08-sidebar.png']]){
 await p.click('[data-act="tpl"][data-id="'+template+'"]');
 const source=await p.evaluate(()=>{const n=document.querySelector('#paper').cloneNode(true);n.querySelectorAll('.noprint').forEach(x=>x.remove());return {css:Array.from(document.querySelectorAll('style')).map(x=>x.textContent).join('\n'),html:n.outerHTML}});
 const q=await browser.newPage();await q.setViewport({width:800,height:600,deviceScaleFactor:4});await q.setContent('<style>'+source.css+' body{margin:0!important;padding:0!important;background:white!important}#paper{zoom:1!important;transform:none!important;width:800px!important;max-height:none!important;height:auto!important;max-width:none!important;overflow:visible!important;margin:0!important;box-shadow:none!important}</style>'+source.html);await q.evaluate(()=>document.fonts.ready);

 await q.screenshot({path:path.join(out,file),clip:{x:0,y:0,width:800,height:600}});await q.close();console.log(file+' 3200×2400, top-only 4:3 preview');
 }
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
