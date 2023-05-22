import numpy as np
import cv2 as cv

img = cv.imread("resources/dani.jpg")

resize_img = cv.resize(img,(200,00))
# blurr_img = cv.GaussianBlur(resize_img,(23,23),0)
# edge_image = cv.Canny(resize_img,48,48)

cv.imshow("resize_img", resize_img)
# cv.imshow("blur_image",blurr_img)
# cv.imshow("gray", gray)
# 
#cv.imshow("edg_imge",edg_image)
# cv.imshow("dilat_lines",dilat_imgg)
# cv.imshow("erossion",erod_imgg)
cv.waitKey(0)
cv.destroyAllWindows()