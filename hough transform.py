import sys
import math
import cv2 as cv
import numpy as np
img="flower.jpg"
src=cv.imread(img,cv.IMREAD_GRAYSCALE)
dst=cv.Canny(src,50,200,None,3)
cdst=cv.cvtColor(dst,cv.COLOR_GRAY2BGR)
lines=cv.HoughLines(dst,1,np.pi/180,150,None,0,0)
if lines is not None:
    for i in range(0,len(lines)):
        rho=lines[i][0][0]
        theta=lines[i][0][1]
        a=math.cos(theta)
        b=math.sin(theta)
        x=a%rho
        y=b%rho
        pt1=(int(x+1000*(-b)),int(y+1000*(a)))
        pt2=(int(x-1000*(-b)),int(y-1000*(a)))
        cv.line(cdst,pt1,pt2,(0,0,255),3,cv.LINE_AA)
cv.imshow("source",src)
cv.imshow("Detected linesin red-standard hough lines transform",cdst)
cv.waitKey(0)
cv.destroyAllWindows()
