from pathlib import Path
import zipfile
R=Path(__file__).resolve().parents[1]
S=R/'1-SELL-THIS'
(S/'Career-Hub.html').write_bytes((R/'2-HOST-ONLINE/index.html').read_bytes())
with zipfile.ZipFile(S/'Career-Hub.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['Career-Hub.html','Career-Hub-Start-Here.pdf','LICENSE.txt']:
  z.write(S/name,'Career-Hub/'+name)
print('Career-Hub.zip updated from the hosted app. Refresh the guide if features changed.')
