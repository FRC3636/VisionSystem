import cv2
import TargetFinder
import Network


network = Network.network()
targetFinder = TargetFinder.targetFinder()

while 1:

    key = cv2.waitKey(1) & 0xFF

    targetFinder.update()

    targetFinder.driverView()

    distance, angle = targetFinder.getPosition()

    network.uploadPosition('Distance', distance)
    network.uploadPosition('Angle', angle)

    if key == 27:
        break

# Close windows and release capture
targetFinder.exit()
