import numpy as np
import cv2
import AdjustValue

def greenBinary(__img):
    # Convert colorspace
    greenImg = cv2.cvtColor(__img, cv2.COLOR_BGR2HSV)

    # Changing to binary image    
    greenImg = cv2.inRange(greenImg, (40, 80, 200), (100, 255, 255))

    # Cleaning up binary image
    __kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    __greenImg = cv2.morphologyEx(greenImg, cv2.MORPH_OPEN, __kernel)

    return __greenImg


def boundingBox(__binaryImg):
    # Find bounding rectangle
    x, y, w, h = cv2.boundingRect(__binaryImg)

    # Return Bounding rectangle
    return x, y, w, h


class greenFinder:
    __img = 0
    __adjValues = 0
    __darkImg = 0

    def __init__(self):
        self.__adjValues = AdjustValue.adjustValue()

    def update(self, frame):
        self.__img = frame
        self.__darkImg = adjValues.darkenFrame(self.__img)

    def locateTarget(self):
        # Convert to binary image
        __greenImg = greenBinary(self.__darkImg)

        # Get location
        x, y, w, h = boundingBox(__greenImg)

        # Find middle of bounding box   
        __xPos = x + int(w / 2)
        __yPos = y + int(h / 2)

        # Return Target center
        return __xPos, __yPos

    def drawBoundingBox(self):
        # Convert to binary image
        __greenImg = greenBinary(self.__darkimg)

        # Get location
        x, y, w, h = boundingBox(__greenImg)

        # Draw bounding box
        self.__img = cv2.rectangle(self.__img, (x, y), (x + w, y + h), (0, 0, 255))

        # Return the image with bounding box
        return self.__img
