import numpy as np
import cv2
from tools import Tools

tool = Tools()
cap = cv2.VideoCapture(1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imshow('captura',tool.umbralizacion(frame,120))
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
