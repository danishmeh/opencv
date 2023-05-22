import pandas as pd
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")
frameNr = 0
while(True):
    ret,frame = cap.read()
    if ret == True:
        cv.imwrite(f"resources/frame/frame_{frameNr}.jpg",frame)
        frameNr = frameNr+1
    else:
        break
cap.release()
cv.waitKey()
cv.destroyAllWindows()