"""Build the complete maintained project without dependencies, drafts or secrets."""
from pathlib import Path
import zipfile
R=Path(__file__).resolve().parents[1]
OUT=R/'Career-Hub-Project.zip'
roots=['1-SELL-THIS','2-HOST-ONLINE','3-ETSY-LISTING','4-BRAND','5-SOURCE']
files=['.gitignore','README.md','package.json','package-lock.json','vercel.json']
skip={'node_modules','frames','studio-refresh','output','tmp','renders','__pycache__','.git'}
def wanted(p):
 rel=p.relative_to(R)
 return not any(x in skip for x in rel.parts) and p.name!='.DS_Store' and not p.name.endswith(('.pyc','.log')) and (not (rel.parts[:2]==('3-ETSY-LISTING','hero-source') and p.parent.name=='hero-source') or p.suffix=='.cjs') and not (p.parent.name=='video' and p.name not in ['Resume-Studio-Interactive.mp4','record-interactions.cjs','encode-video.py'])
with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
 for name in files:
  p=R/name
  if p.exists():z.write(p,'Career-Hub/'+name)
 for name in roots:
  for p in sorted((R/name).rglob('*')):
   if p.is_file() and wanted(p):z.write(p,'Career-Hub/'+str(p.relative_to(R)))
with zipfile.ZipFile(OUT) as z:
 assert z.testzip() is None
 print(f'{OUT.name}: {len(z.namelist())} files; {OUT.stat().st_size/1024/1024:.1f} MB; integrity passed.')
