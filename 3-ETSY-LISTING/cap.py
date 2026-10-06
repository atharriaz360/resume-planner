import sys
from playwright.sync_api import sync_playwright
n=['hero','whats-included','layouts','job-tracker','hub-next-step','cover-letter','experience-bank','contacts','playbook','pay-once']
with sync_playwright() as p:
 b=p.chromium.launch();pg=b.new_page(viewport={'width':1400,'height':1100},device_scale_factor=2)
 import pathlib;d=pathlib.Path(__file__).parent;pg.goto((d/'generator.html').as_uri());pg.wait_for_timeout(500)
 for i,s in enumerate(pg.query_selector_all('.slide')):s.screenshot(path=str(d/'images'/f'{i+1:02d}-{n[i]}.png'))
 b.close()
