import numpy as np
import cv2 as cv

img = cv.imread("resources/dani.jpg")
img = cv.resize(img,(500,700))
print(img.shape)
### Crop the Image 
##25:450 is the adjusting the height 
## 100:400 is adjust the width of the Image
crop_img = img[25:450,100:400]

cv.imshow("original",img)
cv.imshow("crop",crop_img)


cv.waitKey(0)
cv.destroyAllWindows()
