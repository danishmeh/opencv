import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")
if cap.isOpened() == False:
    print("Error opening video stream or file.")

# Writing Format, codec, video Writer Object and File Output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/Black&White.mp4", cv.VideoWriter_fourcc('X', '2', '6', '4'), 10, (frame_width, frame_height), isColor=False)

while True:
    ret, frame = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # To show in Player
    if ret:
        out.write(grayframe)
        cv.imshow("video", grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):  # Wait 1ms for a key press
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
