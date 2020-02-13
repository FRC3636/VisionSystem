import numpy as np 
import cv2 
import math

index = 2 + cv2.CAP_MSMF
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(4)


# Bounding box around reflective tape
def GreenFinder(img):
    # Convert colorspace
    binaryImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    # Changing to binary image    
    binaryImg = cv2.inRange(binaryImg, (40, 80, 200),( 100, 255, 255))

    # Cleaning up binary image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    binaryImg = cv2.morphologyEx(binaryImg, cv2.MORPH_OPEN, kernel)
    
    # Find contours
    contours, _  = cv2.findContours(binaryImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
    # Draw the contour
    cv2.drawContours(img, contours, 0, (0, 0, 255), 5) 
       
    # Bounding rectangle
    x,y,w,h = cv2.boundingRect(binaryImg)
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
    xpos = x + (w/2)
    ypos = y + (h/2)
    return(xpos, ypos, img, binaryImg)
    

# Calculate distance
def distance(y):
    
    # Varibles for distance
    # Phone camera FOV = 44.835
    FOV = 44.835
    targetHeight = 7.583*12
    camHeight = 7.375 
    camAngle = 39.345
    
    # Calculate targetAngle
    targetAngle = -((FOV/480)*y) + (FOV/2)
    
    # Calculate totalAngle
    totalAngle = camAngle + targetAngle
    
    # Calculate triHeight
    triHeight = targetHeight - camHeight
    
    # Change totalAngle to radians for math.tan function
    totalAngle = totalAngle*(math.pi/180)
    
    # Calculate distance from target
    dist =  triHeight / math.tan(totalAngle)
   
    # Convert to feet
    dist = dist/12 
    
    # Return distance in feet
    return dist, totalAngle
    
    # Old distance finding alg
    # Parabola varibles
    #a = 0.000310679
    #b = -0.031794
    #c = 62.2457
    
    # Find distance
    #dist = a*(y**2)+(b*y)+c
    
    
    
    # Round to nearest tenth
    #dist = round(dist*10)/10
    
    
    

while(True):
    
    # Check for keypress
    key = cv2.waitKey(1) & 0xFF
    
    
    # Capture frame-by-frame
    red, frame = cap.read()
    #frame = cv2.resize(frame, (640*2, 480*2), interpolation = cv2.INTER_LINEAR)
    
    # Run the green finder
    xpos, ypos, frame, binaryImg = GreenFinder(frame)
    
    # Find distance 
    distFromWall, triAngle = distance(ypos)
    distFromWall = str(distFromWall)
    triAngle = str(triAngle)
    
    # Print distance to screen
    cv2.putText(frame, distFromWall+"  "+triAngle, (10, 70), 1, 2, 255, 2)
    
    
    # Testing Functions
    #print(frame.shape)
    #print(gray.shape)
    if ypos == 240:
        cv2.rectangle(frame, (30, 30), (610, 450), 200, 5)
    
    
    # Display the resulting frame 
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
