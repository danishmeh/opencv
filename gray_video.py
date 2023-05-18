import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")
if (cap.isOpened() == False):
    print("Error opening video stream or file.")

while(True):
    ret, frame = cap.read()
    if ret == True:
        grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("video", grayframe)
        if cv.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
