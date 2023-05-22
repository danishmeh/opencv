import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
# Resolution set

def hd_resolution():
    cap.set(3,1280)
    cap.set(4,720)
def sd_resolution():
    cap.set(3,640)
    cap.set(4,480)
def fhd_resolution():
    cap.set(3,1920)
    cap.set(4,1080)
    
fhd_resolution()
    
while(cap.isOpened()):
    (ret,frame) = cap.read()
    if ret == True:
            ## To display the Camera
            cv.imshow("WEB_ON",frame)
            ## To quit the Camera with q
            if cv.waitKey(1) & 0xFF == ord("q"):
                break           
cap.release()
cv.destroyAllWindows()