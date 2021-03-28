# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:36:57 2021

@author: life
"""

import cv2
import numpy as np
import math

def Gauss(img_path):
    img=cv2.imread(img_path)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_Gauss=cv2.GaussianBlur(img_gray, (3, 3), 0) 
    return img_Gauss

def Calculate_Gradient(img):
    weight,height=img.shape
    Gdx=np.zeros([weight-1,height-1])           #x方向的梯度值
    Gdy=np.zeros([weight-1,height-1])           #y方向的梯度值
    Amplitude=np.zeros([weight-1,height-1])     #该点处的梯度幅度值
    theta=np.zeros([weight-1,height-1])         #该点处的梯度方向
    for x in range(weight-1):
        for y in range(height-1):
            Gdx[x,y]=img[x+1,y]-img[x,y]
            Gdy[x,y]=img[x,y+1]-img[x,y]
            Amplitude[x,y]=np.sqrt(np.square(Gdx[x,y])+np.square(Gdy[x,y]))
            theta[x,y]=(Gdx[x,y]/(Gdy[x,y]+0.00000001))
    return Gdx,Gdy,Amplitude,theta

def Calculate_Gradient1(img):
    weight,height=img.shape
    Gdx = cv2.Sobel(img, cv2.CV_16SC1, 1, 0)       # 采用sobel函数对图片纵方向梯度计算
    # Y Gradient
    Gdy = cv2.Sobel(img, cv2.CV_16SC1, 0, 1)       # 采用sobel函数对图片横方向梯度计算
    Amplitude=np.zeros([weight-1,height-1])     #该点处的梯度幅度值
    theta=np.zeros([weight-1,height-1])         #该点处的梯度方向
    for x in range(weight-1):
        for y in range(height-1):
            Amplitude[x,y]=np.sqrt(np.square(Gdx[x,y])+np.square(Gdy[x,y]))
            theta[x,y]=math.tan(Gdx[x,y]/(Gdy[x,y]+0.00000001))
    return Gdx,Gdy,Amplitude,theta

def NMS(Amplitude, dx, dy):    
    d = np.copy(Amplitude)
    weight, height = Amplitude.shape
    NMS = np.copy(d)
    NMS[0, :] = NMS[weight-1, :] = NMS[:, 0] = NMS[:, height-1] = 0
        
    for i in range(1, weight-1):
        for j in range(1, height-1):
                
            # 如果当前梯度为0，该点就不是边缘点
            if Amplitude[i, j] == 0:
                NMS[i, j] = 0
                    
            else:
                gradX = dx[i, j] # 当前点 x 方向导数
                gradY = dy[i, j] # 当前点 y 方向导数
                gradTemp = d[i, j] # 当前梯度点
                    
                # 如果 y 方向梯度值比较大，说明导数方向趋向于 y 分量
                if np.abs(gradY) > np.abs(gradX):
                    weight = np.abs(gradX) / np.abs(gradY) # 权重
                    grad2 = d[i-1, j]
                    grad4 = d[i+1, j]
                        
                    # 如果 x, y 方向导数符号一致
                    # 像素点位置关系
                    # g1 g2
                    #    c
                    #    g4 g3
                    if gradX * gradY > 0:
                        grad1 = d[i-1, j-1]
                        grad3 = d[i+1, j+1]
                        
                    # 如果 x，y 方向导数符号相反
                    # 像素点位置关系
                    #    g2 g1
                    #    c
                    # g3 g4
                    else:
                        grad1 = d[i-1, j+1]
                        grad3 = d[i+1, j-1]
                    
                # 如果 x 方向梯度值比较大
                else:
                    weight = np.abs(gradY) / np.abs(gradX)
                    grad2 = d[i, j-1]
                    grad4 = d[i, j+1]
                        
                    # 如果 x, y 方向导数符号一致
                    # 像素点位置关系
                    #      g3
                    # g2 c g4
                    # g1
                    if gradX * gradY > 0:

                        grad1 = d[i+1, j-1]
                        grad3 = d[i-1, j+1]
                        
                    # 如果 x，y 方向导数符号相反
                    # 像素点位置关系
                    # g1
                    # g2 c g4
                    #      g3
                    else:
                        grad1 = d[i-1, j-1]
                        grad3 = d[i+1, j+1]
                        
                # 利用 grad1-grad4 对梯度进行插值
                gradTemp1 = weight * grad1 + (1 - weight) * grad2
                gradTemp2 = weight * grad3 + (1 - weight) * grad4
                    
                # 当前像素的梯度是局部的最大值，可能是边缘点
                if gradTemp >= gradTemp1 and gradTemp >= gradTemp2:
                    NMS[i, j] = gradTemp
                        
                else:
                    # 不可能是边缘点
                    NMS[i, j] = 0
                        
    return NMS

def NMS1(Amplitude, dx, dy,theta):    
    d = np.copy(Amplitude)
    weight, height = Amplitude.shape
    NMS = np.copy(d)
    NMS[0, :] = NMS[weight-1, :] = NMS[:, 0] = NMS[:, height-1] = 0   
    for i in range(1, weight-1):
        for j in range(1, height-1):
            tan=theta[i,j]
            # 如果当前梯度为0，该点就不是边缘点
            if Amplitude[i, j] == 0:
                NMS[i, j] = 0
            else:
                if tan>=10:
                    grad1=d[i,j-1]
                    grad2=d[i,j+1]
                    
                elif tan>=0.2 :
                    grad1=d[i+1,j-1]
                    grad2=d[i-1,j+1]
                    
                elif tan>=-0.2 :
                    grad1=d[i-1,j]
                    grad1=d[i+1,j]
                elif tan>=-10:
                    grad1=d[i-1,j-1]
                    grad2=d[i+1,j+1]
            
            if Amplitude[i,j]>max(grad1,grad2):
                NMS[i,j]=Amplitude[i,j]
            else:
                NMS[i,j]=0
    return NMS

def double_threshold(NMS,TL,TH):   
    weight, height = NMS.shape
    DT = np.zeros([weight, height])     
    for i in range(1, weight-1):
        for j in range(1, height-1):
           # 双阈值选取
            if (NMS[i, j] < TL):
                DT[i, j] = 0                
            elif (NMS[i, j] > TH):
                DT[i, j] = 1               
           # 连接
            elif (NMS[i-1, j-1:j+1] < TH).any() or (NMS[i+1, j-1:j+1].any()
                    or (NMS[i, [j-1, j+1]] < TH).any()):
                DT[i, j] = 0
    return DT 
    
def Canny(img_path):
    image=Gauss(img_path)
    Gdx,Gdy,Amplitude,theta=Calculate_Gradient1(image)
    nms=NMS(Amplitude, Gdx, Gdy)
    return double_threshold(nms,10,40)

def Canny1(img_path):
    image=Gauss(img_path)
    Gdx,Gdy,Amplitude,theta=Calculate_Gradient1(image)
    nms=NMS1(Amplitude, Gdx, Gdy,theta)
    return double_threshold(nms,10,40)

canny_img=Canny("lena.jpg")
cv2.imshow("myCanny",canny_img)


image=cv2.imread('lena.jpg')
blurred = cv2.GaussianBlur(image, (3, 3), 0)     # 高斯模糊   输入图片image  keral大小3*3,                                                   # sigmax,sigmay设置为0，使用默认形式
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)  # 灰度转换   将图片进行灰色转换   后面canny需图片是8位的
xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)       # 采用sobel函数对图片纵方向梯度计算
ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)       # 采用sobel函数对图片横方向梯度计算
edge_outputx = cv2.Canny(xgrad, ygrad, 50, 150)  # canny（）检测，设置双阈值。低阈值50，高阈值150
cv2.imshow("OpenCV Canny", edge_outputx)

cv2.waitKey(0)
cv2.destroyAllWindows()

    
    
    
    
    
