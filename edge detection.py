import cv2
img=cv2.imread("flower.jpg")
canny=cv2.Canny(img,150,250)
cv2.imshow('Original',img)
cv2.imshow('Canny',canny)
img1=cv2.GaussianBlur(img,(3,3),0)
Laplacian=cv2.Laplacian(img1,cv2.CV_64F)
cv2.imshow("Laplacian",Laplacian)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.GaussianBlur(gray,(3,3),0)
sobelx = cv2.Sobel(img , cv2.CV_64F, 1,0, ksize = 5)
sobely = cv2.Sobel(img , cv2.CV_64F, 0,1, ksize = 5)
cv2.imshow('SobelX', sobelx)
cv2.imshow('SobelY', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
