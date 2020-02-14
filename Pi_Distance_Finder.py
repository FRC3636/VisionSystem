import numpy as np
import cv2
import math
import copy

index = 2 + cv2.CAP_MSMF
#cap = cv2.VideoCapture('http://10.176.33.27:4747/mjpegfeed?640x480')
cap = cv2.VideoCapture(0)

# Variables
ySize = 480

# Find angle of target
def TargetAngel(x):
	
	# Variables
	horizontalFOV = 51.889
	
	# Find degree per pixel
	pixelDeg = horizontalFOV / ySize
	
	# Find degrees to x
	xAngle = pixelDeg * x
	
	# Subtract half of FOV to make it be negative if below 50%
	targetAngle = xAngle - (horizontalFOV / 2)
	
	# Return targetAngle
	return(targetAngle)
	
	
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
    
    # Variables for distance
    # Phone camera FOV = 44.835
    FOV = 38.002
    targetHeight = 7.583*12
    camHeight = 7.375 
    camAngle = 38.155
    
    # Calculate targetAngle
    targetAngle = -((FOV/ySize)*y) + (FOV/2)
    
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
    
    # Round to nearest tenth
    dist = round(dist*10)/10
    
    # Return distance in feet
    return dist
    
    # Old distance finding alg
    # Parabola variables
    #a = 0.000310679
    #b = -0.031794
    #c = 62.2457
    
    # Find distance
    #dist = a*(y**2)+(b*y)+c
    
    
    
    
    
# Angle finding function
def camAngle(dist, y):

    # Variables
     
    FOV = 38.002                                                                                                        
    targetHeight = 7.583*12
    camHeight = 7.375

    # Calculate targetAngle
    targetAngle = -((FOV/ySize)*y) + (FOV/2)

    # Calculate totalHeight
    totalHeight = targetHeight - camHeight

    # Calculate angle
    camAngle = (math.atan(totalHeight / dist)*(180/math.pi)) - targetAngle

    return camAngle


# Lighten image to send to driver
def lightenUp(img):
    
    # Change to HSV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Asign img to array
    array = copy.copy(img)
    
    # Increase value to lighten image
    array[:,:,2] *= 2
    
    # Convert back to BGR
    array = cv2.cvtColor(array, cv2.COLOR_HSV2BGR)
    
    # Return array
    return array
    
    
    

while(True):
    
    # Check for keypress
    key = cv2.waitKey(1) & 0xFF
    
    
    # Capture frame-by-frame
    red, frame = cap.read()
    #frame = cv2.resize(frame, (640*2, 480*2), interpolation = cv2.INTER_LINEAR)
    
    # Lighten image for driver view
    driverView = lightenUp(frame)
    
    # Run the green finder
    xpos, ypos, frame, binaryImg = GreenFinder(frame)
    
    # Find distance 
    distFromWall = distance(ypos)
    distFromWall = str(distFromWall)
    
    # Find angle from target
    horizontalAngle = TargetAngle(xpos)
    horizontalAngle = str(horizontalAngle)
    
    # Print distance to screen
    cv2.putText(frame, distFromWall + 'ft, ' + horizontalAngle + 'deg', (10, 70), 1, 2, 255, 2)
    
    
    # Testing Functions
    #print(frame.shape)
    #print(gray.shape)
    if ypos == 240:
        cv2.rectangle(frame, (30, 30), (610, 450), 200, 5)
    
    
    # Display the resulting frame 
    cv2.imshow('frame',frame)
    #cv2.imshow('driverView', driverView)
    #cv2.imshow('binaryImg',binaryImg)
    
    
    # Recalabrate camera angle
    if key == ord('r'):
        camAngle = camAngle(90, ypos)
        print(camAngle)
        
    # Print ypos on press
    if key == 32:
        print(ypos)
    
    # Break    
    if key == 27:
        break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
