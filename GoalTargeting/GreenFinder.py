import numpy as np
import cv2

def greenBinary(img):
    # Convert colorspace
    greenImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    # Changing to binary image    
    greenImg = cv2.inRange(greenImg, (40, 80, 200),( 100, 255, 255))

    # Cleaning up binary image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    greenImg = cv2.morphologyEx(greenImg, cv2.MORPH_OPEN, kernel)
    
    return(greenImg)
    
def boundingBox(binaryImg):
    
    # Find bounding rectangle
    x,y,w,h = cv2.boundingRect(binaryImg)
    
    # Return Bounding rectangle
    return(x, y, w, h)
    
class greenFinder:

    def __init__(self):
        pass
    
    def locateTarget(self, img):
        
        # Convert to binary image
        greenImg = greenBinary(img)
        
        # Get location
        x, y, w, h = boundingBox(greenImg)
        
        # Find middle of bounding box   
        xpos = x + int(w / 2)
        ypos = y + int(h / 2)
        
        # Return Target center
        return(xpos, ypos)
    
    
    def drawBoundingBox(self, darkImg, img):
        
        # Convert to binary image
        greenImg = greenBinary(darkImg)
        
        # Get location
        x, y, w, h = boundingBox(greenImg)
        
        # Draw bounding box
        img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255))
        
        # Return the image with bounding box
        return(img)

