import cv2,numpy as np,comp
bg=cv2.imread('../bg-new.jpg');S=3000/bg.shape[1]
qs=comp.find_screens(bg);ph=qs[1].copy();ph[2]=[662,1733]
im=cv2.imread('scenes/s6.png').astype(np.float32)
H,W=im.shape[:2];band=np.zeros((H,W),np.uint8)
for q in [qs[0],ph]:
  p=(q*S).astype(np.int32)
  outer=np.zeros_like(band);cv2.fillPoly(outer,[p],255);outer=cv2.dilate(outer,np.ones((61,61)))
  inner=np.zeros_like(band);cv2.fillPoly(inner,[p],255);inner=cv2.erode(inner,np.ones((9,9)))
  band|=outer&~inner
b,g,r=im[...,0],im[...,1],im[...,2];mx=np.maximum(r,b)
spill=(band>0)&(g>mx+4)
# only touch pixels outside composited UI (UI is near-white/purple, rarely g-dominant)
im[...,1]=np.where(spill,mx+ (g-mx)*0.1,g)
cv2.imwrite('scenes/s6.png',im.astype(np.uint8));print(spill.sum())
Y0=387;crop=im[Y0:Y0+2250];yy=np.arange(2250)[:,None,None].astype(np.float32)
crop=crop*(1-0.22*np.clip(1-yy/700,0,1))
cv2.imwrite('scenes/hero6-bg.png',np.clip(crop,0,255).astype(np.uint8))
