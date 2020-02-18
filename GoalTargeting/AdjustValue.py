import cv2
import copy
import math
import numpy

# Lighten image to send to driver
class adjustValue:
        
    def __init__(self):
        pass
        
    def lightenFrame(self, img):    
        # Change to HSV
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Increase value to lighten image
        img[:,:,2] *= 2
        
        # Convert back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return img
        
    def darkenFrame(self, img):
        # Change to HSV
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Decrease value to darken image
        img[:,:,2] -= 50
        
        # Convert back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        # Return array
        return img
