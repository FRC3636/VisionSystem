import cv2
import GreenFinder
import Distance
import TargetAngle
import AdjustValue

# Create objects
greenFinder = GreenFinder.greenFinder()
dist = Distance.distance()
targetAngle = TargetAngle.targetAngle()
adjValue = AdjustValue.adjustValue()


class targetFinder:
    
    def __init__(self):
        pass
        
    def targetPosition(self, frame):
        
        # Darken frame to help green finder
        frame = adjValue.darkenFrame(frame)
        
        # Locate target
        xpos, ypos = greenFinder.locateTarget(frame)
        
        # Find distance and angle
        distFromTarget = dist.findDistance(ypos)
        targetAngle = targetAngle.findAngle(xpos)
        
        # Return distance and angle
        return(distFromTarget, targetAngle)
        
    def driverView(self, frame):
        
        # Create driverView
        driverView = frame
        
        # Darken frame to help green finder
        frame = adjValue.darkenFrame(frame)
        
        # Put bounding box on driverView using frame
        driverView = greenFinder.drawBoundingBox(frame, driverView)
        
        # Return driverView
        return(driverView)
        
    def closeWindows(self, key):

        # Close the windows and release the capture
        cap.release()
        cv2.destroyAllWindows() 
            
  
        
        
