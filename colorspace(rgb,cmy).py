import cv2
import numpy as np
image=cv2.imread("flower.jpg")
hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
img=image.astype (np.float64)/255
c=(1-img[...,2])
m=(1-img[...,1])
y=(1-img[...,0])
cmy_image=(np.dstack((c,m,y))*255).astype(np. uint8)
cv2.imshow("Original image", image)
cv2.imshow("HSV image", hsv_image)
cv2.imshow("cmy image", cmy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
