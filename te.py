import pandas as pd
import numpy as np
import cv2 as cv

img =cv.imread("resources/img11.jpg")
print(img.shape)##(1280, 960, 3)
point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])

# cv.imshow("pic",img)
cv.waitKey(0)
cv.destroyAllWindows()