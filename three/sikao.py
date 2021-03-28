# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:08:26 2020

@author: life
"""

import cv2
import numpy as np
i=0
#使用place来存储用户选择的四个点坐标
place=[[0,0],[0,0],[0,0],[0,0]]
img=cv2.imread('lily.tif')

def get_cursor_place(event,x,y,flags,param):
    global i
    if event==cv2.EVENT_LBUTTONDOWN:
        #将用户选择的四个点赋给place数组
        if i<4:
            place[i]=[x,y]
        print(x,y)
        i=i+1
        #用户已经选择完四个点，根据选择的四个点，对局部区域进行仿射处理，变换到200*200大小的区域
        if i==4:
            #源图像中的三个点
            pts1=np.float32([place[0],place[1],place[2]])
            #映射到正方形区域的相应点位置
            pts2=np.float32([[0,0],[200,0],[0,200]])
            M=cv2.getAffineTransform(pts1,pts2)
            dst=cv2.warpAffine(img,M,(200,200))
            cv2.imshow('Output',dst)
            cv2.imwrite('思考.jpg',dst)
            i=0
            
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',get_cursor_place)
while(1):
    cv2.imshow('frame',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break