import cv2

class image:
    __cap = 0
    __frame = 0
    __red = 0
    
    def __init__(self):
        self.__cap = cv2.VideoCapture(0)
        self.readImg()

    def readImg(self):
        self.__red, self.__frame = self.__cap.read()

    def displayImg(self):
        cv2.imshow("Driver View", driverView)

    def getFrame(self):
        return self.__frame

    def closeWindows(self):
        # Close the windows and release the capture
        self.__cap.release()
        cv2.destroyAllWindows() 

