import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    verde_bajos = np.array([140,130,130])
    verde_altos = np.array([200, 255, 255])
    mask = cv2.inRange(hsv, verde_bajos, verde_altos)
    moments = cv2.moments(mask)
    area = moments['m00']
    # Our operations on the frame come here
    if(area > 200000):
	    #Buscamos los centros
	    x = int(moments['m10']/moments['m00'])
	    y = int(moments['m01']/moments['m00'])

	    #Escribimos el valor de los centros
	    #print()"Centro de masa: "+ str(x) + "," + str(y)


	    #Dibujamos el centro con un rectangulo
	    cv2.rectangle(frame, (x, y), (x+20, y+20),(0,0,255), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
