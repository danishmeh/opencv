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
## Writing Video Format,codec,Video Writer Object
frame_width  =  int(cap.get(3))
frame_height =  int(cap.get(4))
out = cv.VideoWriter("resources/fhd.avi",cv.VideoWriter_fourcc('M','J','P','G'),30,(frame_width,frame_height))

while(cap.isOpened()):
    (ret,frame) = cap.read()
    if ret == True:
            # Write the Video
            out.write(frame)
             ## To display the Camera
            cv.imshow("WEB_ON",frame)
            ## To quit the Camera with q
            if cv.waitKey(1) & 0xFF == ord("q"):
                break          
cap.release()
cv.destroyAllWindows()