// Regression checks for the 26 Oct 2026 audit fixes.
const pptr=require('puppeteer'),assert=require('assert'),path=require('path'),http=require('http'),fs=require('fs');
const root=path.resolve('2-HOST-ONLINE'),url='file://'+path.join(root,'index.html');
const wait=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{const b=await pptr.launch();const errors=[];const page=async()=>{const p=await b.newPage();p.on('pageerror',e=>errors.push(e.message));p.on('console',m=>{if(m.type()==='error')errors.push(m.text())});p.on('dialog',d=>d.accept());return p};let server;try{
const p=await page();await p.setViewport({width:1440,height:900});await p.goto(url);await p.waitForSelector('#nav a');
// 1. Awards tab shows a real add button
await p.evaluate(()=>{goTab('bank');bankTab='awards';render()});assert.equal(await p.$eval('#acts',e=>e.textContent.trim()),'+ Award');
await p.evaluate(()=>{bankTab='profile';render()});assert.equal(await p.$eval('#acts',e=>e.textContent.trim()),'');
// 2. Imported invalid dates are cleared, valid ones kept
const d=await p.evaluate(()=>{const r=sampleData();r.applications[0].followUp='<b>x';r.applications[1].applied='2026-02-31x';r.contacts[0].next='2026-13-45';r.cover.date='nope';const n=norm(migrate(r));return [n.applications[0].followUp,n.applications[1].applied,n.contacts[0].next,n.cover.date,n.applications[2].followUp.length]});
assert.deepEqual(d,['','','','',10]);
// 3. Inline "+ New entry" starts from clean defaults (no values copied from the first record)
await p.evaluate(()=>{S=norm(sampleData());sampleMode=true;goTab('resume')});await p.waitForSelector('#paper');
await p.evaluate(()=>focusEditSection('experiences','new'));await p.waitForSelector('.focus-inline-editor');
assert.deepEqual(await p.evaluate(()=>{const f=document.querySelector('.focus-inline-editor form');return [f.dataset.id,f.role.value,f.company.value,f.current.value,document.querySelector('[data-act=focus-record]').value]}),['','','','No','new']);
await p.evaluate(()=>closeFocusEditor());
// 4. Hub contact count includes overdue follow-ups
await p.evaluate(()=>{S.contacts=[{id:'a',name:'A',next:shift(iso(),-2)},{id:'b',name:'B',next:shift(iso(),3)},{id:'c',name:'C',next:shift(iso(),30)}];goTab('hub')});
assert(await p.$eval('#view',e=>e.textContent.includes('2 follow-ups due this week')));
// 5. Remove all data downloads a backup first
await p.evaluate(()=>{window.__dl=[];window.dlBlob=function(n){window.__dl.push(n)};A.reset()});
assert.equal(await p.evaluate(()=>window.__dl.length),1);assert(await p.evaluate(()=>/^career-hub-before-reset-\d{4}-\d{2}-\d{2}\.json$/.test(window.__dl[0])));assert.equal(await p.evaluate(()=>S.experiences.length),0);
// 6a. Phone bottom menu + More sheet; tablet keeps the top menu
{const m=await page();await m.setViewport({width:390,height:844});await m.goto(url+'#hub');await m.waitForSelector('#tabbar a');await m.evaluate(()=>load());
 assert.equal(await m.$eval('#tabbar',e=>getComputedStyle(e).display),'grid');assert.equal(await m.$eval('aside',e=>getComputedStyle(e).display),'none');
 assert.equal(await m.$eval('#tabbar',e=>Math.round(innerHeight-e.getBoundingClientRect().bottom)>=0&&e.getBoundingClientRect().top>innerHeight-110),true);
 for(const v of ['hub','bank','resume','jobs','contacts','playbook','settings','cover']){await m.evaluate(v=>goTab(v),v);await wait(120);assert(await m.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),v+' overflows at 390');assert(await m.$('#tabbar a, #tabbar button'))}
 await m.evaluate(()=>goTab('hub'));await m.click('#tabbar a[href="#jobs"]');await m.waitForFunction(()=>view==='jobs');assert(await m.$('#tabbar a[href="#jobs"][aria-current="page"]'));
 await m.click('[data-act="more-open"]');assert(await m.$eval('#more',e=>e.open));await m.click('#more a[href="#playbook"]');await m.waitForFunction(()=>view==='playbook');assert.equal(await m.$eval('#more',e=>e.open),false);assert(await m.$('#tabbar .is-active[data-act="more-open"]'));
 await m.click('[data-act="more-open"]');await m.click('#more [data-act="theme-toggle"]');assert.equal(await m.evaluate(()=>S.settings.theme),'dark');await m.keyboard.press('Escape');assert.equal(await m.$eval('#more',e=>e.open),false);
 await m.setViewport({width:820,height:1180});await wait(150);assert.equal(await m.$eval('#tabbar',e=>getComputedStyle(e).display),'none');assert.notEqual(await m.$eval('aside',e=>getComputedStyle(e).display),'none');
 for(const v of ['hub','resume','jobs']){await m.evaluate(v=>goTab(v),v);await wait(150);assert(await m.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),v+' overflows at 820')}
 await m.evaluate(()=>{S.settings.theme='light';return save()});await m.close()}
// 6. Phone: no horizontal scroll in builder panes; document fits width
for(const v of ['resume','cover']){const m=await page();await m.setViewport({width:390,height:844});await m.goto(url+'#'+v);await m.waitForSelector('#paper');await m.evaluate(async()=>{await load();loadSample()});await wait(300);
 for(const pane of ['document','design','review']){await m.click('[data-act="focus-pane"][data-id="'+pane+'"]');await wait(120);assert(await m.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),v+' '+pane+' overflows')}
 await m.click('[data-act="focus-pane"][data-id="document"]');assert(await m.$eval('#paper',e=>e.getBoundingClientRect().right<=innerWidth));await m.close()}
// 7. Two tabs: a hidden tab with a dialog open must not overwrite newer edits
const A1=await page(),B1=await page();for(const t of [A1,B1]){await t.goto(url+'#hub');await t.waitForSelector('#nav a');await t.evaluate(()=>load())}
await A1.evaluate(()=>{S=norm(sampleData());return save()});await wait(300);
await B1.evaluate(()=>A.edit({dataset:{col:'contacts',id:S.contacts[1].id}}));
await A1.evaluate(()=>{S.profile.headline='Newest from tab A';return save()});await wait(300);
await B1.evaluate(()=>{flushLocal()});await wait(300);
assert.equal(await A1.evaluate(()=>S.profile.headline),'Newest from tab A');
assert.equal(await B1.evaluate(()=>S.profile.headline),'Newest from tab A');
// Saving B's open dialog merges into the latest data rather than restoring stale data
await B1.evaluate(()=>{document.querySelector('#dlg [name=notes]').value='Edited in tab B';document.querySelector('#dlg form').requestSubmit()});await wait(400);
assert.deepEqual(await A1.evaluate(()=>[S.profile.headline,S.contacts[1].notes]),['Newest from tab A','Edited in tab B']);
await A1.close();await B1.close();
// 7b. Hub tab + Resume tab open together: no save ping-pong between tabs
const H1=await page(),R1=await page();await H1.goto(url+'#hub');await H1.waitForSelector('#nav a');await R1.goto(url+'#resume');await R1.waitForSelector('#paper');
await H1.evaluate(()=>{S.profile.name='Ping';return save()});await wait(500);
for(const t of [H1,R1])await t.evaluate(()=>{window.__n=0;addEventListener('storage',()=>window.__n++)});await wait(1500);
assert.deepEqual([await H1.evaluate(()=>__n),await R1.evaluate(()=>__n)],[0,0]);await H1.close();await R1.close();
// 8. Hosted copy registers manifest + service worker; local file does not
assert.equal(await p.$('link[rel=manifest]'),null);
server=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0])==='/'?'index.html':decodeURIComponent(q.url.split('?')[0]));if(!f.startsWith(root)||!fs.existsSync(f)){r.writeHead(404);return r.end()}r.writeHead(200,{'Content-Type':{'.html':'text/html','.js':'text/javascript','.webmanifest':'application/manifest+json','.png':'image/png'}[path.extname(f)]||'text/plain'});fs.createReadStream(f).pipe(r)}).listen(0);
const port=server.address().port;const h=await page();await h.goto('http://localhost:'+port+'/');await h.waitForSelector('#nav a');
assert(await h.$('link[rel=manifest]'));await h.waitForFunction(()=>navigator.serviceWorker.getRegistration().then(r=>!!r),{timeout:10000});
assert.deepEqual(errors,[]);console.log('PASS: awards add button, date sanitising, clean new entries, overdue contact count, backup before reset, phone builder fit, two-tab merge, hosted-only PWA; zero console errors.');
}finally{if(server)server.close();await b.close()}})().catch(e=>{console.error(e);process.exit(1)});
