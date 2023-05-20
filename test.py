import pandas as pd
import cv2 as cv
import numpy as np



img = cv.imread("resources/dani.jpg")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blurr_img = cv.GaussianBlur(img,(23,23),1)
## edges show
edg_img   = cv.Canny(img,53,53)
# thickness of edges
mat_kernel = np.ones((9,9),np.uint8)
dilat_img = cv.dilate(edg_img,(mat_kernel),iterations=1)
## make a thin line by using erode
erod_img = cv.erode(dilat_img,(mat_kernel),iterations=1)


resize_img = cv.resize(img,(200,400))
# gray = cv.resize(gray,(200,400))
# blurr_img = cv.resize(blurr_img,(200,400))
edg_imgg = cv.resize(edg_img,(200,400))
dilat_imgg = cv.resize(dilat_img,(200,400))
erod_imgg = cv.resize(erod_img,(200,400))





# cv.imshow("resize", resize_img)
# cv.imshow("gray", gray)
# cv.imshow("blur_image",blurr_img)
cv.imshow("edg_imge",edg_imgg)
cv.imshow("dilat_lines",dilat_imgg)
cv.imshow("erossion",erod_imgg)
cv.waitKey(0)
cv.destroyAllWindows()