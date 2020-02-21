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

    def __init__(self):
        self.__img = Image.image()
        self.__greenFinder = GreenFinder.greenFinder()
        self.__dist = Distance.distance()
        self.__targetAngle = TargetAngle.targetAngle()
        self.__adjValue = AdjustValue.adjustValue()


    def update(self):
        self.__img.readImg()
        self.__frame = self.__img.getFrame()
        self.__greenFinder.update(self.__frame)
        self.__distance, self.__angle = self.targetPosition()

    def targetPosition(self):

        self.__greenFinder.update(self.__frame)

        # Locate target
        xPos, yPos = self.__greenFinder.locateTarget()
        
        # Find distance and angle
        distFromTarget = self.__dist.findDistance(yPos)
        targetAngle = self.__targetAngle.findAngle(xPos)

        # Return distance and angle
        return distFromTarget, targetAngle
        
    def driverView(self):
        # Create driverView
        driverView = self.__frame
        
        # Put bounding box on driverView using frame
        driverView = self.__greenFinder.drawBoundingBox()

        cv2.imshow("Driver View", driverView)

    def getPosition(self):
        return self.__distance, self.__angle

    def exit(self):
        self.__img.closeWindows()



