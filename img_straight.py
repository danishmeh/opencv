### Image straightness
import pandas as pd
import numpy as np
import cv2 as cv

img =cv.imread("resources/img12.jpg")
# img = cv.resize(img,(600,600))
print(img.shape)##(1280, 960, 3)
point1 = np.float32([[222,134],[633,154],[44,759],[890,756]])

width,height = 800,900

point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2)

out_img = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("pic",img)
cv.imshow("Tranasformed",out_img)
cv.waitKey(0)
cv.destroyAllWindows()