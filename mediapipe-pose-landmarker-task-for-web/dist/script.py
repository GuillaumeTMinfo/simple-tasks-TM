import numpy as np
import cv2

cap = cv2.VideoCapture('linusi.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

def 
# distance between Wz(Wrist landmark) and Sz(Shoulder landmark)