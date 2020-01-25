import numpy as np 
import cv2 


index = 2 + cv2.CAP_MSMF
cap = cv2.VideoCapture('http://10.176.34.6:4747/mjpegfeed?640x480')

# Bounding box around reflective tape
def GreenFinder(img):
    # Convert colorspace
    binaryImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    # Changing to binary image    
    binaryImg = cv2.inRange(binaryImg, (40, 80, 200),( 100, 255, 255))

    # Cleaning up binary image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    binaryImg = cv2.morphologyEx(binaryImg, cv2.MORPH_OPEN, kernel)
    
       
    # Bounding rectangle
    x,y,w,h = cv2.boundingRect(binaryImg)
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
    xpos = x + (w/2)
    ypos = y + (h/2)
    return(xpos, ypos, img)

# Calculate distance
def distance(y):
    
    # Parabola varibles
    a = 0.000278323
    b = -0.0107435
    c = 59.8373
    
    # Find distance
    dist = ((a*y)*(a*y))+b*y+c
    
    # Convert to feet
    dist = dist/12
    
    # Return distance in feet
    return(dist)

while(True):
    
    # Check for keypress
    key = cv2.waitKey(1) & 0xFF
    
    
    # Capture frame-by-frame
    red, frame = cap.read()
    frame = cv2.resize(frame, (640*2, 480*2), interpolation = cv2.INTER_LINEAR)
    
    # Run the green finder
    xpos, ypos, frame = GreenFinder(frame)
    
    # Find distance 
    distFromWall = distance(ypos)
    distFromWall = str(distFromWall)
    
    # Print distance to screen
    cv2.putText(frame, distFromWall, (10, 40), 1, 2, 255)
    
    # Testing Functions
    #print(frame.shape)
    #print(gray.shape)
    
    #Display the resulting frame 
    cv2.imshow('frame',frame)
    #cv2.imshow('binaryImg',binaryImg)
    
    
    
    
    # Print ypos on press
    if key == 32:
        print(ypos)
    
    
    # Break    
    if key == 27:
        break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
