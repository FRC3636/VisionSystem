import numpy as np
import cv2
import math

# Variables for distance
# Phone camera FOV = 44.835
vertFOV = 38.002
targetHeight = 7.583*12
camHeight = 7.375 
camAngle = 38.155
ySize = 480    


# Distance Class
class distance:
    
    def __init__(self):
        pass

    def findDistance(self, ypos):
        # Calculate targetAngle
        targetAngle = -((vertFOV/ySize)*ypos) + (vertFOV/2)
        
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
        return(dist)
