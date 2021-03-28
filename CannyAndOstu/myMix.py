# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:11:45 2021

@author: life
"""

import numpy as np
import cv2

def myMix(background,mix_video,mix_x,mix_y,capture_num,isOutPut):
    ordinaryBackground=cv2.imread(background)
    ordinaryBackground=cv2.flip(ordinaryBackground,1,dst=None)
    ordinaryBackground_gray=cv2.cvtColor(ordinaryBackground, cv2.COLOR_BGR2GRAY)
    rows,cols,channels=ordinaryBackground.shape
    cap1 = cv2.VideoCapture(capture_num) #摄像头编号。
    if isOutPut:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')#  注意编码器
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (rows,cols))

    cap1.set(3,rows)
    cap1.set(4,cols)
    cap2 = cv2.VideoCapture(mix_video)
    while(cap1.isOpened() and cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        #sub=np.zeros([rows,cols]) 
        if (ret1==True and ret2==True) :
        
            newBackground=cv2.flip(frame2,1)
            newBackground_flip=cv2.flip(newBackground,1,dst=None)
            newBackground_gray=cv2.cvtColor(newBackground_flip,cv2.COLOR_BGR2GRAY)
            roi_newBackground=newBackground_flip[mix_x:rows+mix_x,mix_y:cols+mix_y]
        
            frame1 = cv2.flip(frame1,1)
            roi_video=frame1[0:rows,0:cols]
            video_gray = cv2.cvtColor(roi_video, cv2.COLOR_BGR2GRAY)   
            sub=cv2.addWeighted(ordinaryBackground_gray,1,video_gray,-1,0)
        
            for x in range(0,rows-1):
                for y in range(0,cols-1):
                    if sub[x][y]>0:
                        #sub[x][y]=255
                        roi_newBackground[x][y]=0
                    else:
                        roi_video[x][y]=0
            
            mix_img=cv2.addWeighted(roi_newBackground,1,roi_video,1,0)
            frame2[mix_x:rows+mix_x,mix_y:cols+mix_y]=mix_img
        
            cv2.imshow('frame2',frame2)
            if isOutPut:
                out.write(frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.waitKey()
    cap1.release()
    cap2.release()
    out.release()
    cv2.destroyAllWindows()

myMix('background1.jpg','vtest.avi',100,100,0,False)