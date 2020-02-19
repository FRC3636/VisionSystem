import threading
from networktables import NetworkTables

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

class network:
    def __init__(self):
        cond = threading.Condition()
        notified = [False]
        NetworkTables.initialize(server='10.36.36.2')
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()

        # Insert your processing code here
        print("Connected!")

    def uploadPosition(self, distance, angle):
        sd = NetworkTables.getTable('SmartDashboard')

        sd.putNumber('Distance', distance);
        sd.putNumber('Angle', angle)
