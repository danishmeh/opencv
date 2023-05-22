## How to Find the Coordinates of Images
## Step-1 Import Libaries
import cv2 as cv
import numpy as np
import pandas as pd

# find the coordinates by using flags
def find_coord(event,x,y,flags,parms):
    # left mouse click
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,'',y) # this will show value at terminal
        # how to show on the window
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,str(x) +','+ str(y),(x,y),font,1,color=(255,0,0),thickness=2)
        # image show and text on the Image
        cv.imshow("Image",img)
    # FOR Color Fining 
    if event == cv.EVENT_RBUTTONDOWN:
            print(x,'',y)# this will show value at terminal
            # how to show on the window
           
            font = cv.FONT_HERSHEY_SIMPLEX
            b = img[y,x,0]
            g = img[y,x,1]
            r = img[y,x,2]
            cv.putText(img,str(b)+','+str(g)+','+str(r),(x,y),font,1,color=(255,0,2),thickness=2)
            cv.imshow("Image",img)
         

# Calling the Function
## Load and display the image:
if __name__ == "__main__":
    img = cv.imread("resources/img12.jpg")
 
    cv.imshow("Image",img)
    # Set the mouse callback function to find_coord:
    cv.setMouseCallback("Image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()     
        
        
        
        
        
        
        
        
        