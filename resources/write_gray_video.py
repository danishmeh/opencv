import pandas as pd
import cv2 as cv

cap = cv.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/BLACK.mp4", cv.VideoWriter_fourcc('X', '2', '6', '4'), 50, (frame_width, frame_height), isColor=False)

while(cap.isOpened()):
    ret,frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    if ret == True:
        
        out.write(grayframe)
        cv.imshow('frame',grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv.destroyAllWindows()