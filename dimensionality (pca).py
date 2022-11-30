import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
fig = plt.figure(figsize=(10,10))
img = cv.imread("flower.jpg")
 
red,green,blue=cv.split(img)
p=PCA(20)
 
red=p.fit_transform(red)
red_inv=p.inverse_transform(red)
 
green=p.fit_transform(green)
green_inv=p.inverse_transform(green)
 
blue=p.fit_transform(blue)
blue_inv=p.inverse_transform(blue)
 
PCA_image = np.dstack((red_inv, green_inv,blue_inv)).astype(np.uint8)
 
 
l=[img,PCA_image]
t=["Original","PCA Image"]
 
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(l[i])
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show() 
for i in range(2):
    cv.imshow(t[i],l[i]) 
cv.waitKey(0)
cv.destroyAllWindows()
