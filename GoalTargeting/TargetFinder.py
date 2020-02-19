import cv2
import GreenFinder
import Distance
import TargetAngle
import AdjustValue
import Image

class targetFinder:
    __img = 0
    __greenFinder = 0
    __dist = 0
    __targetAngle = 0
    __adjValue = 0 
    __distance = 0
    __angle = 0
    __frame = 0

    def __init__(self, img):
        self.__frame = img
        self.__img = Image.image()
        self.__greenFinder = GreenFinder.greenFinder()
        self.__dist = Distance.distance()
        self.__targetAngle = TargetAngle.targetAngle()
        self.__adjValue = AdjustValue.adjustValue()

    def update(self):
        self.__img.readImg()
        self.__frame = self.__img.getFrame()
        self.__distance, self.__angle = self.targetPosition()
        self.displayImg()
        self.__greenFinder.update(self.__frame)
        self.__adjValue.update(self.__frame)

    def targetPosition(self):
        # Darken frame to help green finder
        darkFrame = self.__adjValue.darkenFrame()

        greenFinder.update()

        # Locate target
        __xPos, __yPos = self.__greenFinder.locateTarget()
        
        # Find distance and angle
        __distFromTarget = self.__dist.findDistance(__yPos)
        __targetAngle = self.__targetAngle.findAngle(__xPos)
        
        # Return distance and angle
        return __distFromTarget, __targetAngle
        
    def driverView(self):
        
        # Create driverView
        driverView = self.__frame
        
        # Darken frame to help green finder
        frame = self.__adjValue.darkenFrame()
        
        # Put bounding box on driverView using frame
        driverView = self.__greenFinder.drawBoundingBox()
        
        # Return driverView
        return driverView

    def displayImg(self):
        cv2.imshow("Driver View", self.driverView())


