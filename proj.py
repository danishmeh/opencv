import pandas as pd
import cv2 as cv
import numpy as np

img = cv.imread("resources/dani.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
resize_img = cv.resize(img,(800,600))
blurr_img = cv.GaussianBlur(img,(23,23),1)
## edges show
cv.imshow("resize", resize_img)
cv.imshow("gray", gray)
cv.imshow("blur_image",blurr_img)
# cv.imshow("edg_imge",edg_imgg)
cv.imshow("dilat_lines",dilat_imgg)
cv.imshow("erossion",erod_imgg)
cv.waitKey(0)
cv.destroyAllWindows()