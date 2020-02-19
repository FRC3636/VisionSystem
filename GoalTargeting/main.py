import cv2
import TargetFinder
import Network

# Create objects
targetFinder = TargetFinder.targetFinder()
cap = cv2.VideoCapture(1)
net = Network.network()

while(1):
    
    # Get frame
    red, frame = cap.read()

    # Get Key press
    key = cv2.waitKey(1) & 0xFF
    
    # Get the target position
    distance, angle = targetFinder.targetPosition(frame)
    
    # Get driverview
    driverView = targetFinder.driverView(frame)
    
    # Show the driverview
    cv2.imshow('Driver View', driverView)
    
    # Send distance and angle to roborio
    net.uploadPosition('Distance', distance)
    net.uploadPosition('Angle', angle)
    
    # Break while loop when key pressed
    if key == 27:
        break
        
    

# Close windows and release capture
tgfd.closeWindow()
