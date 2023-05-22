import pandas as pd
import numpy as np
import cv2 as cv

img = cv.imread("resources/img2.jpg")
resize = cv.resize(img,(500,500))
blurr_img = cv.GaussianBlur(resize,(23,23),0)
## edge thickness
edge_image = cv.Canny(resize,48,48)
#
mat_kernel = np.ones((1,1),np.uint8)
dilate_img = cv.dilate(edge_image,(mat_kernel),iterations=1)

## make Thiner 

erode = cv.erode(dilate_img,mat_kernel,iterations=1)

cv.imshow("dilat_lines",dilate_img)

cv.imshow("Original",resize)
# cv.imshow("blurr",blurr_img)
cv.imshow("edge_imag",edge_image)
cv.imshow("erode_imag",erode)
cv.waitKey() 
cv.destroyAllWindows()