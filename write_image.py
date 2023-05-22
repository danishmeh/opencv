import cv2 as cv
import pandas as pd

img = cv.imread("resources/img12.jpg")
print(img.shape)
img = cv.resize(img,(900,800))
cv.imshow("img",img)
cv.imwrite("resources/img12.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()