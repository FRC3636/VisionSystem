import numpy as np
import cv2
import AdjustValue

def greenBinary(img):
    # Convert colorspace
    greenImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    rangeLow = (70, 170, 100)
    rangeHigh = (90, 255, 255)

    # Blur to help with converting
    greenImg = cv2.GaussianBlur(greenImg, (3, 3), cv2.BORDER_DEFAULT)

    # Changing to binary image    
    greenImg = cv2.inRange(greenImg, rangeLow, rangeHigh)


    # Cleaning up binary image 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    greenImg = cv2.morphologyEx(greenImg, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow("color", greenImg)

    return greenImg


def boundingBox(__binaryImg):
    # Find bounding rectangle
    x, y, w, h = cv2.boundingRect(__binaryImg)

    # Return Bounding rectangle
    return x, y, w, h


class greenFinder:
    __frame = 0
    __adjValues = 0
    __darkImg = 0
    __x = 0
    __y = 0
    __w = 0
    __h = 0

    def __init__(self):
        #self.__adjValues = AdjustValue.adjustValue()
        pass
    
    def update(self, __frame):
        self.__frame = __frame
        #self.__adjValues.update(self.__frame)
        #self.__darkImg = self.__adjValues.darkenFrame()
        greenImg = greenBinary(self.__frame)
        self.__x, self.__y, self.__w, self.__h = boundingBox(greenImg)

    def locateTarget(self):

        # Find middle of bounding box   
        __xPos = self.__x + int(self.__w / 2)
        __yPos = self.__y + int(self.__h / 2)

        # Return Target center
        return __xPos, __yPos

    def drawBoundingBox(self):

        # Draw bounding box
        self.__frame = cv2.rectangle(self.__frame, (self.__x, self.__y), (self.__x + self.__w, self.__y + self.__h), (0, 0, 255))

        # Return the image with bounding box
        return self.__frame
