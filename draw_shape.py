# how to Draw Shape in Python 
import pandas as pd
import numpy as np
import cv2 as cv


# img2 = np.ones((600,600))  ## this is white Canvas
color_img = np.zeros((600,600,3),np.uint8)
color_img[:] = 222,22,330   ## full image Colored
## Part of Image add in the main window
color_img[0:500,0:300] = 250,168,255 
## Add line in image 
cv.line(color_img,(0,0),(600,600),(50,100,255),3)  
cv.rectangle(color_img,(50,250),(300,400),(241,124,0),3)
## Rectrange filled
cv.rectangle(color_img,(50,250),(300,400),(155,159,147),cv.FILLED)
## Circle Fill
cv.circle(color_img,(400,300),50,(125,215,127),3)
## How circle Filled
cv.circle(color_img,(400,300),50,(50,100,255),cv.FILLED)
cv.imshow("image1",color_img)
## Adding Text 

# Add the text to the image
# Specify the position, font, font scale, color, and thickness of the text
text = "Hello, OpenCV!"
position = (50, 100)  # Coordinates of the bottom-left corner of the text
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
color = (0, 0, 0)  # BGR color format (green in this case)
thickness = 2

cv.putText(color_img,"Danish",(200,500),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
           
cv.waitKey()
cv.destroyAllWindows()