const {chromium}=require('playwright');const F='file://'+process.argv[2];const O=process.argv[3];
(async()=>{const b=await chromium.launch();
async function prep(p){p.on('dialog',d=>d.accept());await p.goto(F+'#settings');await p.waitForTimeout(800);await p.locator('[data-act="sample"]').first().click();await p.waitForTimeout(1200);await p.evaluate(()=>{S.resume.template='executive';S.settings.theme='light';save()});}
async function hide(p){const h=p.locator('[data-act="hide-banner"]');if(await h.count())await h.first().click();await p.waitForTimeout(800)}
// laptop: 1560x923 px app area under a 52px browser bar
const d=await (await b.newContext({viewport:{width:1440,height:852},deviceScaleFactor:1560/1440})).newPage();await prep(d);await d.goto(F+'#resume');await d.waitForTimeout(1500);await hide(d);await d.screenshot({path:O+'/laptop.png'});
// phone: 404x818 px app area under a 56px status bar
const m=await (await b.newContext({viewport:{width:390,height:790},deviceScaleFactor:404/390,isMobile:true,hasTouch:true})).newPage();await prep(m);await m.goto(F+'#jobs');await m.waitForTimeout(1500);await hide(m);await m.screenshot({path:O+'/phone.png'});
await d.emulateMedia({media:'print'});await d.pdf({path:O+'/exec.pdf',preferCSSPageSize:true,printBackground:true});
await b.close()})();
