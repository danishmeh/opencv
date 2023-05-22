## WebCAM ON 
## Import Libaries 
import cv2 as cv
import pandas as pd
# Read the Frame from Camera 
cap = cv.VideoCapture(0) ## cam 01
while(cap.isOpened()):
    ## Capature Frame by frame
    ret,frame = cap.read()
    if ret == True:
            ## To display the Camera
            cv.imshow("WEB_ON",frame)
            ## To quit the Camera with q
            if cv.waitKey(1) & 0xFF == ord("q"):
                break           
cap.release()
cv.destroyAllWindows()