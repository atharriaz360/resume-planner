from playwright.sync_api import sync_playwright
import pathlib,datetime
u=pathlib.Path('app.html').resolve().as_uri()
CSS='.banner{display:none!important}#toast{display:none!important}'
with sync_playwright() as p:
  b=p.chromium.launch()
  for i,(w,h) in enumerate([(1512,945)]):
    pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=2);pg.set_default_timeout(6000)
    pg.goto(u+'#settings');pg.wait_for_timeout(500);pg.click('[data-act="sample"]');pg.wait_for_timeout(400)
    pg.goto(u+'#resume');pg.wait_for_timeout(800);pg.add_style_tag(content=CSS)
    try:
      pg.click('[data-act="preview-fit"][data-id="width"]',timeout=2000);pg.wait_for_timeout(500)
    except Exception as e: print('nofit',w)
    pg.screenshot(path=f'cap/alt{i}.png')
  b.close()
