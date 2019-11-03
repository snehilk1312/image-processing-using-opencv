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
    w = 160
    h = 120
    url="http://192.168.1.3:8080/shot.jpg"
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret,label,center=cv2.kmeans(Z,K,None,criteria,100,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    cv2.imshow('res2',res2)
    if cv2.waitKey(5) & 0xFF==ord('q'):
       break
cv2.destroyAllWindows()