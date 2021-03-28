# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:15:11 2021

@author: life
"""

import cv2
import numpy as np

def myOtsu2Threshold(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度转换   将图片进行灰色转换   后面canny需图片是8位的
    threshold = 0                               #记录最好的分割点
    all_variance=0                              #全局方差
    part_variance=0                             #类间方差
    best_threshold_variance_result=0            #记录最好的分割方法所得出的方差比结果
    variance_result=0                           #存储当前分割方法方差比结果
    MG=0                                        #平均灰度值
    m1=0                                        #实体的平均灰度值
    m2=0                                        #背景的平均灰度值
    weight,height= img.shape
    new=np.zeros([weight,height])  
    all_num = weight * height                   #全部像素点个数
    hest = np.zeros([256],dtype=np.int32)       #每个像素点的数量
    P_hest=np.zeros([256])                      #每个像素点所占的比例
    
    #统计每个的像素点的数量
    for row in range(weight):
        for col in range(height):
            pv = img[row, col]
            hest[pv] += 1
            
    #计算每种像素点所占的比例以及图像的全局平均灰度值
    for i in range(255):
        P_hest[i]=hest[i]/all_num
        MG+=i*P_hest[i]
        
    #计算全局方差
    for i in range(255):
        all_variance+=np.square(i-MG)*P_hest[i]
    
    background_Num = 0
    object_Num = 0
    
    #分析某一次以像素点k为分割点的情况
    for k in range(0,254):
        m1=0
        m2=0
        part_variance=0
        object_Num+= hest[i]                    #统计划分为主体的像素点个数
        #统计划分为背景的像素点个数
        background_Num=all_num-object_Num
        for i in range(k):
            m1+=i*hest[i]/object_Num
        for j in range(k,255):
            m2+=j*hest[j]/background_Num
            
        #计算类间方差
        part_variance=(object_Num/all_num)*np.square(m1-MG)+(background_Num/all_num)*np.square(m2-MG)
        variance_result=part_variance/all_variance
        if part_variance>best_threshold_variance_result:
            best_threshold_variance_result=part_variance
            threshold=k
            
    for i in range(weight):
        for j in range(height):
            if img[i,j]<threshold:
                new[i,j]=0
            else:
                new[i,j]=1
    return new


img = cv2.imread("lena.jpg")
cv2.imshow("img", img)
dst=myOtsu2Threshold(img)
img = cv2.imread("lena.jpg",0)
t, openCV_dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # t表示返回的阈值
cv2.imshow("myOstu", dst)
cv2.imshow('openCV_Ostu',openCV_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()