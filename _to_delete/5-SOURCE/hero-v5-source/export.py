import sys,io
from PIL import Image,ImageCms
srgb=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
def save(src,dst,lim=1000*1024):
  im=Image.open(src).convert('RGB')
  for q in range(92,60,-2):
    b=io.BytesIO();im.save(b,'JPEG',quality=q,optimize=True,progressive=True,subsampling=0 if q>=88 else 2,icc_profile=srgb)
    if b.tell()<lim: break
  open(dst,'wb').write(b.getvalue());print(dst,im.size,q,b.tell()//1024,'KB')
for a in sys.argv[1:]:
  s,d=a.split(':');save(s,d)
