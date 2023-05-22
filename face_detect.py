import cv2 as cv

# Load the face cascade classifier
face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

# Check if the cascade classifier loaded successfully
if face_cascade.empty():
    raise FileNotFoundError("Failed to load the cascade classifier XML file.")

# Read the image
img = cv.imread("resources/images.jpg")
img = cv.resize(img,(700,700))

# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
cv.imshow("Image", img)
cv.imwrite("resources/Image_detect.png",img)

# Wait for a key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()

