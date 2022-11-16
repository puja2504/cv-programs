import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread('flower.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('histogram img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
histg = cv2.calcHist([img],[0],None,[250],[0,256])
plt.plot (histg)
plt.show()
