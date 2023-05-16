### Resize the Image
import cv2 as cv

img = cv.imread("resources/asf.jpg")
img = cv.resize(img,(800,600))

cv.imshow("second Image",img)
cv.waitKey(0)
cv.destroyAllWindows()