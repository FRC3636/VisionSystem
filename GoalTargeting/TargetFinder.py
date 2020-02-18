import cv2
import GreenFinder
import Distance
import TargetAngle
import AdjustValue

# Create objects
gnfd = GreenFinder.GreenFinder()
dist = Distance.distance()
tgan = TargetAngle.targetAngle()
adjvl = AdjustValue.adjustValue()


class targetFinder:
    
    def __init__(self):
        pass
        
    def targetPosition(self, frame):
        
        # Darken frame to help green finder
        frame = adjvl.darkenFrame(frame)
        
        # Locate target
        xpos, ypos = gnfd.locateTarget(frame)
        
        # Find distance and angle
        distFromTarget = dist.findDistance(ypos)
        targetAngle = tgan.findAngle(xpos)
        
        # Return distance and angle
        return(distFromTarget, targetAngle)
        
    def driverView(self, frame):
        
        # Create driverView
        driverView = frame
        
        # Darken frame to help green finder
        frame = adjvl.darkenFrame(frame)
        
        # Put bounding box on driverView using frame
        driverView = gnfd.drawBoundingBox(frame, driverView)
        
        # Return driverView
        return(driverView)
        
    def closeWindows(self, key):

        # Close the windows and release the capture
        cap.release()
        cv2.destroyAllWindows() 
            
  
        
        
