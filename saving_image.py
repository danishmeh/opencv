import cv2 as cv

img = cv.imread("resources/asf.jpg")
img = cv.resize(img, (200, 200))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh,binary) = cv.threshold(gray,101,300,cv.THRESH_BINARY)

cv.imshow("Grayscale Image",gray)
cv.imshow("Original Image",img)

cv.waitKey(0)

cv.imwrite("resources/myfoto.jpg",img)
cv.imwrite("Binary.jpg",binary)


# cv.waitKey(0)
# cv.destroyAllWindows()