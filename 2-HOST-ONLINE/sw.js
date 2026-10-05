// Career Hub offline cache. Caches the app only; workspace entries are stored in the browser.
const C="career-hub-v1.0.32-bronze-accent",FILES=['./','./index.html','./manifest.webmanifest','./icons/icon-180.png','./icons/icon-192.png','./icons/icon-512.png','./icons/icon-maskable-512.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(C).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith('career-hub-')&&x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 e.respondWith(fetch(r).then(res=>{if(res.ok&&res.type==='basic'){const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}return res})
 .catch(()=>caches.match(r,{ignoreSearch:true}).then(m=>m||(r.mode==='navigate'?caches.match('./index.html'):Response.error()))))});
