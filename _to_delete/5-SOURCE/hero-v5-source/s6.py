import cv2,numpy as np,comp
bg=cv2.imread('../bg-new.jpg');H0,W0=bg.shape[:2]
BASE,S=comp.upscale(bg,W=3000,grain=1.2,seed=11)
qs=comp.find_screens(bg)
lap=qs[0];ph=qs[1].copy();ph[2]=[662,1733]   # BR corner hidden by thumb: rebuild from parallel edges
d=comp.greenness(BASE);out=BASE.copy()
for q,src,br in [(lap,'cap/mbp0.png',0.96),(ph,'cap/ms-jobs.png',0.95)]:
  m=np.zeros(d.shape,np.uint8);cv2.fillPoly(m,[(q*S).astype(np.int32)],1);m=cv2.erode(m,np.ones((15,15)))
  med=np.median(d[m>0]);ka=comp.green_alpha(BASE,lo=0.3*med,hi=0.72*med)
  out=comp.screen_into(out,q*S,comp.prep_src(src),ka,bright=br,glare=0.04)
PQ=[[1076,1812],[1913,1914],[1782,2292],[875,2051]]
out=comp.paper_into(out,bg,S,PQ,'cap/q-sidebar-ocean.png',thr=(150,40),ymin=1750,ink_floor=0.1,bright=1.0)
cv2.imwrite('scenes/s6.png',out);print(out.shape)
Y0=387;crop=out[Y0:Y0+2250];yy=np.arange(2250)[:,None,None].astype(np.float32)
crop=crop.astype(np.float32)*(1-0.22*np.clip(1-yy/700,0,1))
cv2.imwrite('scenes/hero6-bg.png',np.clip(crop,0,255).astype(np.uint8))
