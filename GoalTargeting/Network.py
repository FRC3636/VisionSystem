import threading
from networktables import NetworkTables


cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    #cond = threading.Condition()
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

class network:

    __sd = 0
    
    def __init__(self):
        NetworkTables.initialize(server='10.36.36.2')
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()

        # Insert your processing code here
        print("Connected!")
        self.__sd = NetworkTables.getTable('SmartDashboard')


    def uploadPosition(self, distance, angle):
        #sd = NetworkTables.getTable('SmartDashboard')

        self.__sd.putNumber('Distance', distance)
        self.__sd.putNumber('Angle', angle)
