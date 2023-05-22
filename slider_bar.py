import pandas as pd
import numpy as np
import cv2 as cv

path = "resources/dani1.png"
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 800, 400)

def slider(pos):
    pass

cv.createTrackbar("Hue Min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue Max", "Bars", 179, 179, slider)
cv.createTrackbar("Sat Min", "Bars", 0, 255, slider)
cv.createTrackbar("Sat Max", "Bars", 255, 255, slider)
cv.createTrackbar("Val Min", "Bars", 0, 255, slider)
cv.createTrackbar("Val Max", "Bars", 255, 255, slider)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min", "Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Bars")
    sat_min = cv.getTrackbarPos("Sat Min", "Bars")
    sat_max = cv.getTrackbarPos("Sat Max", "Bars")
    val_min = cv.getTrackbarPos("Val Min", "Bars")
    val_max = cv.getTrackbarPos("Val Max", "Bars")
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
    
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    msk_img = cv.inRange(hsv_img,lower,upper)
    out_img = cv.bitwise_and(img,img,mask=msk_img)
    
    

    # cv.imshow("Image", img)
    cv.imshow("hsv_img", hsv_img)
    cv.imshow("mask_img", msk_img)
    cv.imshow("out_img", out_img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
