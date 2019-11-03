''' image writing '''
import cv2
img = cv2.imread('F:/Downloads/ronaldo.jpg')
outpath = "F:/Desktop/ronaldo.jpg"
cv2.imwrite(outpath, img)
# out_img = cv2.imread(outpath)
# cv2.imshow('CR7', out_img)
cv2.imshow('CR7', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
