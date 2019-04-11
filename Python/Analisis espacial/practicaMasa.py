import cv2
import numpy as np
import time
cam = cv2.VideoCapture(1)
while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    t, dst = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(dst,kernel,iterations = 5)
    cv2.imshow('real',frame)
    cv2.imshow('binarizada',erosion)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
