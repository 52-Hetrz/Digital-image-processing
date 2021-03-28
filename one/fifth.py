# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:26:29 2020

@author: life
"""

import numpy as np
import cv2 


#单击出现字幕
text=False
def isText(event,x,y,flags,param):
    global text
    if event==cv2.EVENT_LBUTTONDOWN:
        text=not text

cap = cv2.VideoCapture('vtest.avi')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',isText)

while(cap.isOpened()):     
    ret, frame = cap.read()     
    if text:        
        img2=cv2.putText(frame,"okk",(123,123),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)
        cv2.imshow('frame',img2)
    else:
        cv2.imshow('frame',frame)     
    if cv2.waitKey(1) & 0xFF == ord('q') :         
        break
cap.release()
cv2.destroyAllWindows()



'''

i=0
string=["asd","123"]
text=False
def isText(event,x,y,flags,param):
    global text
    if event==cv2.EVENT_LBUTTONDOWN:
        text=not text

cap = cv2.VideoCapture('vtest.avi')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',isText)

while(cap.isOpened()):     
    ret, frame = cap.read()       
    if (i%20)>10 :
        img2=cv2.putText(frame,string[0],(123,123),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)
        cv2.imshow('frame',img2)
    else :
        img2=cv2.putText(frame,string[1],(123,123),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)
        cv2.imshow('frame',img2)
    i=i+1
    if cv2.waitKey(40) & 0xFF == ord('q') :         
        break
cap.release()
cv2.destroyAllWindows()

#img2=cv2.putText(frame,"okk",(123,123),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)
#cv2.imshow('frame',img2)
'''

