import cv2
import TargetFinder
import time

# Create objects
tgfd = TargetFinder.targetFinder()
cap = cv2.VideoCapture(1)

while(1):
    
    # Get frame
    red, frame = cap.read()

    # Get Key press
    key = cv2.waitKey(1) & 0xFF
    
    # Get the target position
    distance, angle = tgfd.targetPosition(frame)
    
    # Get driverview
    driverView = tgfd.driverView(frame)
    
    # Show the driverview
    cv2.imshow('Driver View', driverView)
    
    # Break while loop when key pressed
    if key == 27:
        break
        
    

# Close windows and release capture
tgfd.closeWindow()
