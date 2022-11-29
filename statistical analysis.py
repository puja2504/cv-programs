import cv2
import numpy as np
img=cv2.imread("flower.jpg")
array=np.asarray(img)
print(array)
print("\nThe mean of the image=",np.mean(array))
print("\nThe minimum of the image=",np.min(array))
print("\nThe maximum of the image=",np.max(array))
print("\nThe variance of the image=",np.var(array))
print("\nThe standard deviation of the image=",np.std(array))
cv2.waitKey(0)
cv2.destroyAllWindows()
