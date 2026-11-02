from pathlib import Path
from PIL import Image,ImageDraw,ImageChops,ImageStat
import subprocess,json,re
root=Path(__file__).resolve().parent
ff='/private/tmp/kaellabs-video-deps/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
video=root.parents[1]/'6-ETSY-LISTING/Career-Hub-Listing-Video-v9.mp4'
r=subprocess.run([ff,'-i',str(video)],capture_output=True,text=True).stderr
sheet=Image.new('RGB',(1920,1520),'#eee7dc');d=ImageDraw.Draw(sheet)
for i,p in enumerate(sorted((root/'qa').glob('*.jpg'))):
 im=Image.open(p).resize((480,360));x=i%4*480;y=i//4*380;sheet.paste(im,(x,y+20));d.text((x+8,y+3),f'{int(p.stem)/30:.2f} s',fill='black')
sheet.save(root/'contact-sheet.jpg',quality=94)
subprocess.run([ff,'-y','-sseof','-0.034','-i',str(video),'-frames:v','1',str(root/'last-frame.png')],capture_output=True,check=True)
last=Image.open(root/'last-frame.png').convert('RGB');hero=Image.open(root.parents[1]/'3-ETSY-LISTING/images/01-hero-premium-refined.jpg').convert('RGB').resize(last.size)
mae=sum(ImageStat.Stat(ImageChops.difference(last,hero)).mean)/3
raw=video.read_bytes()
result={'video':str(video),'bytes':video.stat().st_size,'duration':re.search(r'Duration: ([\d:.]+)',r).group(1),'h264':'Video: h264' in r,'yuv420p':'yuv420p' in r,'resolution1440x1080':'1440x1080' in r,'fps30':'30 fps' in r,'audioStreams':len(re.findall(r'Stream.*Audio:',r)),'faststart':raw.find(b'moov')<raw.find(b'mdat'),'lastFrameMeanPixelDifferenceFromHero':mae,'capturedAppErrors':json.loads((root/'capture-proof.json').read_text())['errors']}
assert result['h264'] and result['yuv420p'] and result['fps30'] and result['resolution1440x1080']
assert result['audioStreams']==0 and result['faststart'] and result['bytes']<100000000 and mae<6
(root/'qa-report.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
