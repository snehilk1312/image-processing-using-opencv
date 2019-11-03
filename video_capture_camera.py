import cv2
cap = cv2.VideoCapture(0)  # 0 is passed if I have 1 camera, if multiple camera
# pass 1 , 2 ,etc also
while True:
    _ , frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()