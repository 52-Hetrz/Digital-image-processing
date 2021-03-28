# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 00:43:31 2020

@author: life
"""

import numpy as np
import cv2

cap1 = cv2.VideoCapture(0) #摄像头编号。
cap1.set(3,160)
cap1.set(4,120)
cap2 = cv2.VideoCapture('vtest.avi')
ordinaryBackground=cv2.imread('background5.jpg')
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
while(cap1.isOpened() and cap2.isOpened()):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if (ret1==True and ret2==True) :
        
        newBackground=cv2.flip(frame2,1)
        newBackground_flip=cv2.flip(newBackground,1,dst=None)
        newBackground_gray=cv2.cvtColor(newBackground_flip,cv2.COLOR_BGR2GRAY)
        roi_newBackground=newBackground_flip[100:rows+100,100:cols+100]
        
        frame1 = cv2.flip(frame1,1)
        roi_video=frame1[0:rows,0:cols]
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
        frame2[100:rows+100,100:cols+100]=mix_img
        '''
        people_img_substract=cv2.addWeighted(ordinaryBackground,1,roi_video,-1,0)
        #cv2.imshow('sub',people_img_substract)
        peoplegray = cv2.cvtColor(people_img_substract,cv2.COLOR_BGR2GRAY)
        ret, mask_front = cv2.threshold(peoplegray, 175, 255, cv2.THRESH_BINARY) #这是图像分割方法，后面讲到。
        #cv2.imshow('maskfront',mask_front)
        mask_inv = cv2.bitwise_not(mask_front)
        #cv2.imshow('maskinv',mask_inv)
        img1_fg=cv2.bitwise_and(roi_newBackground,roi_newBackground,mask=mask_inv)
        img2_fg = cv2.bitwise_and(frame,frame,mask = mask_front)
        dst=cv2.add(img1_fg,img2_fg)
        frame[0:rows,0:cols]=dst
        '''
        cv2.imshow('frame2',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 # Release everything if job is finished

cv2.waitKey()
cap1.release()
cap2.release()
cv2.destroyAllWindows()