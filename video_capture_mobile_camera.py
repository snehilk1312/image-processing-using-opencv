import cv2
import numpy as np
import urllib.request
while True:
    # reads frame from camera
    url = "http://192.168.1.3:8080/shot.jpg"
    # Use urllib to get the image and convert into a cv2 usable format
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype = np.uint8)
    image = cv2.imdecode(imgNp, -1)
    # put the image on screen
    cv2.imshow('IpWebcam',image)
    if cv2.waitKey(5)  & 0xFF== ord('q'):
        break
cv2.destroyAllWindows()

