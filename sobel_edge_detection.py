# SOBEL EDGE DETECTION:-
import cv2
import numpy as np
img = cv2.imread('F:/Downloads/ronaldo.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Calcution of Sobelx
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# Calculation of Sobely
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# Calculation of Laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('laplacian',laplacian)
cv2.waitKey(0)