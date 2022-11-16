import cv2
cap=cv2.VideoCapture(r"dog.mp4")
if(cap.isOpened()==False):
 print("Error")
else:
 fps=cap.get(5)
 print("Frames per sec:",fps,"FPS")
 frame_count=cap.get(7)
 print("Frame count:",frame_count)
i=30
cap.release()
cv2.destroyAllWindows()
