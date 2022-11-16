import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("flower.jpg")
canny = cv2.Canny(img, 150, 250)
cv2.imshow('Original',img)
cv2.imshow('canny', canny)
img1 = cv2.GaussianBlur(img,(3,3),0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('laplacian', laplacian)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.GaussianBlur(gray,(3,3),0)
sobelx = cv2.Sobel(img , cv2.CV_64F, 1,0, ksize = 5)
sobely = cv2.Sobel(img , cv2.CV_64F, 0,1, ksize = 5)
cv2.imshow('SobelX', sobelx)
cv2.imshow('SobelY', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
plt.subplot(1,5,1)
plt.imshow(img)
plt.title("Original image")
plt.xticks([]),plt.yticks([])
 
plt.subplot(1,5,2)
plt.imshow(canny*255)
plt.title("canny image")
plt.xticks([]),plt.yticks([])
 
plt.subplot(1,5,3)
plt.imshow(laplacian*255)
plt.title("laplacian  image")
plt.xticks([]),plt.yticks([])
 
plt.subplot(1,5,4)
plt.imshow(sobelx*255)
plt.title("sobelx  image")
plt.xticks([]),plt.yticks([])
 
plt.subplot(1,5,5)
plt.imshow(sobely*255)
plt.title("sobely  image")
plt.xticks([]),plt.yticks([])
 
plt.show()
