import cv2
import numpy as np
i1=cv2.imread(r"flower.jpg",0)
cv2.imshow('ori',i1)
i=cv2.resize(i1,(750,600))
g=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
sift_ob=cv2.SIFT_create()
kp=sift_ob.detect(g,None)
img=cv2.drawKeypoints(g,kp,i)
img=cv2.resize(img,(350,300))
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
