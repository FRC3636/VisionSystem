import urllib.request
import cv2
import numpy as np
import time

url = "http://10.49.78.136:8080"

while True:

        imb_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.unt8)
        img = cv2.imdecode(img_arr, -1)
        cv2.imsrow('IPWebcam', img)

        if cv2.waitKey(1):
            break
