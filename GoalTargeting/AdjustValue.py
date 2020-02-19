import cv2
import copy
import math
import numpy

# Lighten image to send to driver
class adjustValue:
    __frame = 0

    def __init__(self):
        pass

    def update(self, __frame):
        self.__frame = __frame
        print

    def lightenFrame(self):
        # Change to HSV
        __img = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)
        
        # Increase value to lighten image
        __img[:, :, 2] *= 2
        
        # Convert back to BGR
        __img = cv2.cvtColor(__img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return __img
        
    def darkenFrame(self):
        # Change to HSV
        __img = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)
        
        # Decrease value to darken image
        __img[:, :, 2] -= 50
        
        # Convert back to BGR
        __img = cv2.cvtColor(__img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return __img
