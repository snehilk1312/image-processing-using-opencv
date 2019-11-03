# Image reading
import cv2
img = cv2.imread('F:/Downloads/ronaldo.jpg')
cv2.imshow('CR7', img)
cv2.waitKey(0)  # for 1000 ms  the window will remain open
cv2.destroyAllWindows()
