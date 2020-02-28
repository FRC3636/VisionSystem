import numpy as np
import cv2
import math


# Distance Class
class distance:
    # Phone camera FOV = 44.835
    __vertFOV = 38.002
    __targetHeight = 230.5 
    __camHeight = 20
    __camAngle = 40
    __ySize = 240

    def __init__(self):
        pass

    def findDistance(self, yPos):
        # Calculate targetAngle
        targetAngle = -((self.__vertFOV/self.__ySize)*yPos) + (self.__vertFOV/2)
        
        # Calculate totalAngle
        totalAngle = self.__camAngle + targetAngle
        
        # Calculate triHeight
        triHeight = self.__targetHeight - self.__camHeight
        
        # Change totalAngle to radians for math.tan function
        totalAngle = totalAngle*(math.pi/180)
        
        # Calculate distance from target
        dist = triHeight / math.tan(totalAngle)

        # Round to nearest tenth
        dist = round(dist*10)/10
        
        # Return distance in feet
        return dist
