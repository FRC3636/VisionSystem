import cv2
import TargetFinder
import Network
import Image

# Create objects
# targetFinder = TargetFinder.targetFinder()
# cap = cv2.VideoCapture(1)
img = Image.image()
targetFinder = TargetFinder.targetFinder()
# net = Network.network()

while 1:

    # Get frame
    # red, frame = cap.read()
    img.readImg()

    # Get Key press
    key = cv2.waitKey(1) & 0xFF

    # Get the target position
    # distance, angle = targetFinder.targetPosition(frame)

    # Get driverview
    # driverView = targetFinder.driverView(frame)

    # Show the driverview
    # cv2.imshow('Driver View', driverView)
    targetFinder.update()

    # Send distance and angle to roboRio
    # net.uploadPosition('Distance', distance)
    # net.uploadPosition('Angle', angle)

    # Break while loop when key pressed
    if key == 27:
        break

# Close windows and release capture
img.closeWindows()
