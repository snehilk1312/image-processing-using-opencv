# EROSION & DILATION USING REAL TIME:-
import cv2
import urllib.request
import numpy as np
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
while(1):
    url="http://192.168.1.3:8080/shot.jpg"
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(thresh1, kernel, iterations=3)
    img_dilation = cv2.dilate(thresh1, kernel, iterations=3)
    cv2.imshow('Edges',img_erosion)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()