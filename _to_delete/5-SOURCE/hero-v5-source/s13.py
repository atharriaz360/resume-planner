import cv2,numpy as np,comp
bg=cv2.imread(comp.B+'13.jpg');H0,W0=bg.shape[:2]
BASE,S=comp.upscale(bg,W=3000,seed=7)
PQ=[[540,985],[1050,1070],[962,1373],[388,1222]]
yy,xx=np.mgrid[0:H0,0:W0];EM=~(yy< 984+(xx-540)*0.256);EM[:955]=False
big,qs=comp.screens_into(BASE.copy(),bg,S,['cap/alt0.png','cap/ms-jobs.png'])
big=comp.paper_into(big,bg,S,PQ,'cap/q-sidebar-ocean.png',thr=(110,38),extra_mask=EM)
cv2.imwrite('scenes/s13.png',big);print(big.shape,[q.round().tolist() for q in qs])
