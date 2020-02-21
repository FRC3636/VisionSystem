import cv2
import copy
import math
import numpy

# Lighten image to send to driver
class adjustValue:
    __frame = 0
    __hsv = 0

    def __init__(self):
        pass

    def update(self, __frame):
        self.__frame = __frame
        self.__hsv = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)
        

    def lightenFrame(self):
        img = self.__hsv

        # Increase value to lighten image
        img[:, :, 2] *= 2
        
        # Convert back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return img
        
    def darkenFrame(self):
        # Change to HSV
        img = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)

        # Decrease value to darken image
        img[:, :, 2] -= 100
        
        # Convert back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return img
