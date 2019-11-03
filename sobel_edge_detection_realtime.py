# SOBEL EDGE DETECTION USING REAL TIME:-
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
    # reads frames from a camera
    url="http://192.168.1.3:8080/shot.jpg"
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Calcution of Sobelx
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    # Calculation of Sobely
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    # Calculation of Laplacian
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imshow('laplacian',laplacian)
    if cv2.waitKey(5) & 0xFF==ord('q'):
       break
cv2.destroyAllWindows()