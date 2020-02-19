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

    def __init__(self, img):
        self.__img = img
        self.__greenFinder = GreenFinder.greenFinder()
        self.__dist = Distance.distance()
        self.__targetAngle = TargetAngle.targetAngle()
        self.__adjValue = AdjustValue.adjustValue()

    def update(self):
        self.__img.readImg()
        self.__distance, self.__angle = self.targetPosition()
        self.displayImg()

    def targetPosition(self):
        
        # Darken frame to help green finder
        frame = self.__adjValue.darkenFrame(self.__img.getFrame())
        
        # Locate target
        xpos, ypos = self.__greenFinder.locateTarget(self.__img.getFrame())
        
        # Find distance and angle
        distFromTarget = self.__dist.findDistance(ypos)
        targetAngle = self.__targetAngle.findAngle(xpos)
        
        # Return distance and angle
        return(distFromTarget, targetAngle)
        
    def driverView(self):
        
        # Create driverView
        driverView = self.__img.getFrame()
        
        # Darken frame to help green finder
        frame = self.__adjValue.darkenFrame(self.__img.getFrame())
        
        # Put bounding box on driverView using frame
        driverView = self.__greenFinder.drawBoundingBox(self.__img.getFrame(), driverView)
        
        # Return driverView
        return(driverView)

    def displayImg(self):
        cv2.imshow("Driver View", self.driverView())


