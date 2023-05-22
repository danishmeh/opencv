## Reading the Image

import cv2 as cv
import numpy as np

img = cv.imread("resources/img2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res_img = cv.resize(img,(200,200))
gray_img = cv.resize(gray,(200,200))
cv.imshow("Image",res_img)
cv.imshow("Image2",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()