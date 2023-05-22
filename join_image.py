import pandas as pd
import numpy as np
import cv2 as cv

img = cv.imread("resources/dani.jpg")
img = cv.resize(img,(400,400))

## StacK Horizontal Image
# hor_img = np.hstack((img,img))

## Vertical Stack
ver_img = np.vstack((img,img))

cv.imshow("orifinal",ver_img)

cv.waitKey(0)
cv.destroyAllWindows()