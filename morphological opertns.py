import cv2
import numpy as np
import matplotlib.pyplot as plt
i=cv2.imread(r"flower.jpg",cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(i,210,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
dilation=cv2.dilate(mask,kernal)
erode=cv2.erode(mask,kernal)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
titles=['original image','masked image','dilated image','eroded image','opening image','closed image']
images=[i,mask,dilation,erode,opening,closing]
for i in range(6):
 plt.subplot(1,6,i+1),plt.imshow(images[i],'gray')
 plt.title(titles[i])
 plt.xticks([ ]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
