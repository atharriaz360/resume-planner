// Shared helpers that drive the current focus workspace UI (resume + cover letter).
// Tests call these instead of selectors from the retired classic builder.
async function showPane(p, pane) {
  const tab = await p.$('[data-act="focus-pane"][data-id="' + pane + '"]');
  if (tab && await tab.evaluate(e => e.offsetParent !== null)) await tab.click();
}
async function designTab(p, id) {
  await showPane(p, 'design');
  await p.waitForSelector('[data-act="focus-design-tab"][data-id="' + id + '"]');
  if (!await p.$('[data-act="focus-design-tab"][data-id="' + id + '"][aria-pressed="true"]')) await p.click('[data-act="focus-design-tab"][data-id="' + id + '"]');
}
async function rightTab(p, id) {
  await showPane(p, 'review');
  await p.waitForSelector('[data-act="focus-review-tab"][data-id="' + id + '"]');
  if (!await p.$('[data-act="focus-review-tab"][data-id="' + id + '"][aria-pressed="true"]')) await p.click('[data-act="focus-review-tab"][data-id="' + id + '"]');
}
async function pickTemplate(p, kind) {
  await designTab(p, 'templates');
  const id = await p.evaluate(k => k + ':' + S.resume.accent + ':' + (S.resume.headerAlign === 'auto' ? (k === 'mint' ? 'center' : 'left') : S.resume.headerAlign), kind);
  await p.click('.focus-design[data-id="' + id + '"]');
  await p.waitForFunction(k => S.resume.template === k && document.querySelector(view === 'cover' ? '#paper.tpl-cover' : '#paper.tpl-' + k), {}, kind);
  await showPane(p, 'document');
}
const openStyle = p => designTab(p, 'style');
const openSections = p => rightTab(p, 'sections');
const openLetter = p => rightTab(p, 'letter');
module.exports = { showPane, pickTemplate, openStyle, openSections, openLetter };
