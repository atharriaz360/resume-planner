from pathlib import Path
import re,pdfplumber
from pypdf import PdfReader
from collections import Counter
for kind in ['executive','mint']:
 p=Path('output/pdf')/(kind+'-resume.pdf')
 with pdfplumber.open(p) as doc:
  text='\n'.join(page.extract_text() or '' for page in doc.pages)
  expected=Path('tmp/pdfs/'+kind+'-expected.txt').read_text()
  normalize=lambda s:re.sub(r'\s+',' ',s).strip()
  logical='\n'.join(page.extract_text() or '' for page in PdfReader(p).pages)
  assert Counter(re.sub(r'\s','',logical))==Counter(re.sub(r'\s','',expected)),(kind,'lost or duplicated text')
  if kind=='executive': assert normalize(text)==normalize(expected),(kind,'text mismatch')
  heads=['Professional Summary','Work Experience','Projects','Education','Skills','Certifications']
  if kind=='executive':
   indices=[re.search(r"^"+re.escape(h)+r"$",text,re.I|re.M).start() for h in heads];assert indices==sorted(indices)
  for page in doc.pages:
   for ch in page.chars:
    assert ch['x0']>=30 and ch['x1']<=page.width-30,(kind,'horizontal clipping')
    assert ch['top']>=25 and ch['bottom']<=page.height-25,(kind,'vertical clipping')
  Path('tmp/pdfs/'+kind+'-extracted.txt').write_text(text)
  print(kind,'pages:',len(doc.pages),'all text preserved; no clipping; bytes:',p.stat().st_size)
 with pdfplumber.open('tmp/pdfs/'+kind+'-long.pdf') as doc:
  text='\n'.join(page.extract_text() or '' for page in doc.pages)
  assert 'Additional Role 8' in text and 'certifications' in text.lower()
  assert all(page.chars for page in doc.pages)
  for page in doc.pages:
   for ch in page.chars: assert ch['top']>=25 and ch['bottom']<=page.height-25,(kind,'long page clipping')
  print(kind,'long pages:',len(doc.pages),'final role present; no blank pages; page margins retained')
