# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:43:04 2021

@author: life
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0) #摄像头编号。
cap.set(3,160)
cap.set(4,120)
ordinaryBackground=cv2.imread('background4.jpg')
ordinaryBackground_gray=cv2.cvtColor(ordinaryBackground, cv2.COLOR_BGR2GRAY)
rows,cols,channels=ordinaryBackground.shape


'''
people_image=cv2.imread('people3.jpg')
people=people_image[0:rows,0:cols]
people_gray=cv2.cvtColor(people, cv2.COLOR_BGR2GRAY)
substract=cv2.addWeighted(ordinaryBackground_gray,1,people_gray,-1,0)
#t1,substract_ostu=cv2.threshold(substract, 0,1, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#people_ostu=cv2.multiply(substract_ostu,people_gray)
#mask_inv = cv2.bitwise_not(substract_ostu)
#background_ostu=cv2.multiply(mask_inv,newBackground_gray)
#print(people_ostu)
for x in range(0,rows-1):
    for y in range(0,cols-1):
        if substract[x][y]>0:
            substract[x][y]=255
            roi_newBackground[x][y]=0
        else:
            people[x][y]=0
mix=cv2.addWeighted(roi_newBackground,1,people,1,0)
cv2.imshow('substract',substract)
cv2.imshow('mix',mix)
cv2.imshow('people',people)
#cv2.imshow('mix',mix_img)
'''

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        newBackground=cv2.imread('newBackground.jpg')
        newBackground_gray=cv2.cvtColor(newBackground,cv2.COLOR_BGR2GRAY)
        roi_newBackground=newBackground[0:rows,0:cols]
        
        frame = cv2.flip(frame,1)
        roi_video=frame[0:rows,0:cols]
        video_gray = cv2.cvtColor(roi_video, cv2.COLOR_BGR2GRAY)   
        substract=cv2.addWeighted(ordinaryBackground_gray,1,video_gray,-1,0)
        for x in range(0,rows-1):
            for y in range(0,cols-1):
                if substract[x][y]>10:
                    substract[x][y]=255
                    roi_newBackground[x][y]=0
                else:
                    roi_video[x][y]=0
        mix_img=cv2.addWeighted(roi_newBackground,1,roi_video,1,0)
        cv2.imshow('frame',mix_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 # Release everything if job is finished

cv2.waitKey()
cap.release()
cv2.destroyAllWindows()