from playwright.sync_api import sync_playwright
import pathlib,datetime
u=pathlib.Path('app.html').resolve().as_uri()
CSS='.banner{display:none!important}#toast{display:none!important}'
def page(b,w,h,dsf):
  pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=dsf);pg.set_default_timeout(6000)
  pg.clock.install(time=datetime.datetime(2026,10,27,9,41))
  pg.goto(u+'#settings');pg.wait_for_timeout(500);pg.click('[data-act="sample"]');pg.wait_for_timeout(400)
  return pg
def go(pg,r):
  pg.goto(u+'#'+r);pg.wait_for_timeout(800);pg.add_style_tag(content=CSS);pg.wait_for_timeout(300)
with sync_playwright() as p:
  b=p.chromium.launch()
  # plain 4:3 captures for listing (3000x2250)
  pg=page(b,1500,1125,2)
  for r in ['hub','resume','jobs','cover','bank']:
    go(pg,r);pg.screenshot(path=f'cap/plain-{r}.png')
  # laptop screen 16:10
  pg=page(b,1512,945,2)
  for r in ['hub','resume','jobs']:
    go(pg,r);pg.screenshot(path=f'cap/d-{r}.png')
  b.close()
