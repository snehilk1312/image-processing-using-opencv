# LOCAL THRESHOLDING
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('F:/Downloads/ronaldo.jpg',0)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('ronaldo_local_threshold',th4)
cv2.waitKey(0)