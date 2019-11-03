## GLOBAL THRESHOLDING USING REAL TIME:-
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

while True:
    # reads frames from a camera
    url="http://192.168.1.3:8080/shot.jpg"
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(hsv,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(hsv,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(hsv,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('IpWebcam_global Threshold',thresh1)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()