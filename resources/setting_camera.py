import pandas as pd
import cv2 as cv 
cap = cv.VideoCapture(0)
cap.set(10,1000) ## adjust the Color of cameara
cap.set(3,1200) ## width 
cap.set(4,100) ## Height

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        if cv.waitKey(5) & 0xFF == ord('q'):
                break
    else:
            break
cap.release()
cv.destroyAllWindows()
        