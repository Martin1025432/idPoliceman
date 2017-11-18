# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:09:42 2017

@author: Administrator
"""
import cv2

cap = cv2.VideoCapture(0)
while(1):
# get a frame
    ret, frame = cap.read()
# show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("test3.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()
