import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(grayframe,127,121,cv.THRESH_BINARY)
    if ret ==True:
        cv.imshow('Original_frame',frame)
        cv.imshow("gray",grayframe)
        cv.imshow("binary",binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv.destroyAllWindows()        