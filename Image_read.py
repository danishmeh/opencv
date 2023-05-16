## Reading the Image

import cv2 as cv

img = cv.imread("resources/asf.jpg")
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()