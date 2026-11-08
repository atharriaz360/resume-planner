import sys,pathlib
from playwright.sync_api import sync_playwright
src,dst=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1500,'height':1125},device_scale_factor=2)
  pg.goto(pathlib.Path(src).resolve().as_uri());pg.evaluate('document.fonts.ready');pg.wait_for_timeout(500)
  pg.locator('.s').screenshot(path=dst);b.close()
