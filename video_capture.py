''' Video Capture from file'''
import cv2
import numpy as np
cap = cv2.VideoCapture('F:/Downloads/gaur.mp4')   # Reading a Video,if read from camera
# pass 0 as argument in VideoCapture
while True:
    _, frame = cap.read()
    cv2.imshow('video_frame', frame)   # showing frame same as I did in image
    if cv2.waitKey(1) & 0xFF == ord('q'):  # we use waitkey to pause each frame for particular milliseconds
        break
cap.release()
cv2.destroyAllWindows()
