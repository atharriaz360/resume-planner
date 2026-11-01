import cv2,numpy as np
s=cv2.imread('scenes/s13.png')  # 3000x3000
X0,Y0,PAD=200,480,200
src=s[Y0:Y0+2250, X0:3000]               # 2800 wide
strip=cv2.flip(src[:, -PAD:],1)           # mirror right edge
strip=cv2.GaussianBlur(strip,(0,0),6)
out=np.concatenate([src,strip],1).astype(np.float32)
# soften the seam + darken far right
H,W=out.shape[:2];xx=np.arange(W)[None,:,None].astype(np.float32)
d=np.clip((xx-(W-PAD-120))/(PAD+120),0,1)
out*=1-0.45*d
# top shade for headline legibility
yy=np.arange(H)[:,None,None].astype(np.float32)
out*=1-0.25*np.clip(1-yy/900,0,1)
cv2.imwrite('scenes/hero-bg.png',np.clip(out,0,255).astype(np.uint8));print(out.shape)
