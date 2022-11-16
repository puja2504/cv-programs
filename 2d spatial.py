import cv2
image = cv2.imread("flower.jpg")
height,width = image.shape[:2]
center = (width/2, height/2)
newsize = (120,200)
out = cv2.resize(image,newsize)
cv2.imshow("resized image",out)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=65, scale=1)
rotated_image = cv2.warpAffine(src = image, M=rotate_matrix,
 dsize=(width,height))
cv2.imshow('Original image', image)
cv2.imshow('Rotate image', rotated_image)
cv2.waitKey(0)
cv2.imwrite('rotated_image.jpg',rotated_image)
