import cv2 as cv 
from cv2 import imwrite
cap = cv.VideoCapture("resources/video.mp4")
# This file check the video are Stream or Not
if (cap.isOpened()== False):
    print("Error opening video stream or file ---may be File Name is not Correct")
    
## Reading the Video
# This line starts a while loop that runs as 
# long as the video capture object is open and frames can be read
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        cv.waitKey(5) & 0xFF == ord('q')
    else:
        break

cap.release()
cv.destroyAllWindows()
    
    