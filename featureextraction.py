import cv2
imageread = cv2.imread('flower.jpg')
imagegray = cv2.cvtColor(imageread,cv2.COLOR_BGR2GRAY)
imageedges = cv2.Canny(imagegray, 10, 100)
cv2.imshow('original image',imageread)
contours, hierarchy = cv2.findContours(imageedges, 
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imageread, contours,-1, (0,0,255),6)
cv2.imshow('image_with_contours',imageread)
cv2.waitKey()
cv2.destroyAllWindows()
