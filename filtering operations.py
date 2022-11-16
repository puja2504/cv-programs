import cv2
import numpy as np
image=cv2.imread(r"flower.jpg",0)
img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('ori',img)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-5,kernel)
cv2.imshow('2d',dst)
bil=cv2.bilateralFilter(img,11,75,75)
cv2.imshow('bilateral',bil)
d=cv2.boxFilter(img,0,(5,5),img)
cv2.imshow('box',d)
blur=cv2.blur(img,(5,5))
cv2.imshow('blurred image',blur)
gblur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('gaussian',gblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
