# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:16:08 2021

@author: life
"""


import cv2
import numpy as np


def edge_demo(image):
    
    
    blurred = cv2.GaussianBlur(image, (3, 3), 0)     # 高斯模糊   输入图片image  keral大小3*3,
                                                    # sigmax,sigmay设置为0，使用默认形式
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)  # 灰度转换   将图片进行灰色转换   后面canny需图片是8位的
    # X Gradient   计算梯度
    xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)       # 采用sobel函数对图片纵方向梯度计算
    # Y Gradient
    ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)       # 采用sobel函数对图片横方向梯度计算
    # edge
    edge_outputx = cv2.Canny(xgrad, ygrad, 50, 150)  # canny（）检测，设置双阈值。低阈值50，高阈值150
    edge_outputy = cv2.Canny(gray, 50, 150)  # 注意这一步和上面一行一样都是做边缘检测，
                                            # cv.Canny()算法重载了多种入参方式，会有不同的结果

    cv2.imshow("Canny Edge x", edge_outputx)
    cv2.imshow("Canny Edge y", edge_outputy)

    dst = cv2.bitwise_and(image, image, mask=edge_outputx)
    cv2.imshow("Color Edge", dst)


print("--------- Python OpenCV Tutorial ---------")
src = cv2.imread("lena.jpg")                              # 加载图片，这里图片是相对路径，需把图片放在程序文件夹中
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)        # 图片窗口和原图自动保持一致
#cv.namedWindow("input image", cv.WINDOW_NORMAL)
cv2.imshow("input image", src)                            # 显示原图，第一个参数是窗口title，第二个参数是图片
edge_demo(src)                                           # 调用edge_demo函数，将原图src作为参数传入
cv2.waitKey(0)

cv2.destroyAllWindows()
