import cv2 as cv

import numpy as np

img = cv.imread("resources/asf.jpg")
img = cv.resize(img,(800,600))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("image1",img)
cv.imshow("GRAY_image",gray)
cv.waitKey(0)
cv.destroyAllWindows()