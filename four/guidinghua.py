# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:21:55 2020

@author: life
"""

import cv2
import numpy as np

img = cv2.imread('fig7a.jpg')
dst = cv2.imread('fig7b.jpg')
def_img = cv2.imread('fig7a.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    #将直方图变成一维
    hist1, bins = np.histogram(img[:, :, i].ravel(), 256, [0, 256])
    hist2, bins = np.histogram(dst[:, :, i].ravel(), 256, [0, 256])
    # 获得累计直方图
    cdf1 = hist1.cumsum()
    cdf2 = hist2.cumsum()
    # 归一化处理,获得灰度值累计值的比例
    cdf1_hist = hist1.cumsum() / cdf1.max()
    cdf2_hist = hist2.cumsum() / cdf2.max()

    # diff_cdf 里是每2个灰度值比率间的差值
    diff_cdf = [[0 for j in range(256)] for k in range(256)]
    for j in range(256):
        for k in range(256):
            diff_cdf[j][k] = abs(cdf1_hist[j] - cdf2_hist[k])
    # FigA 中的灰度级与目标灰度级的对应表
    lut = [0 for j in range(256)]
    #找出差值最小的那一对，此处依据直方图规定化的映射原理
    for j in range(256):
        squ_min = diff_cdf[j][0]
        index = 0
        for k in range(256):
            if squ_min > diff_cdf[j][k]:
                squ_min = diff_cdf[j][k]
                index = k
        lut[j] = ([j, index])
        
    h = int(img.shape[0])
    w = int(dst.shape[1])
    # 对原图像进行灰度值的映射
    for j in range(h):
        for k in range(w):
            def_img[j, k, i] = lut[img[j, k, i]][1]
    
cv2.namedWindow('Fig6A', 0)
cv2.resizeWindow('Fig6A', 400, 520)
cv2.namedWindow('Fig6B', 0)
cv2.resizeWindow('Fig6B', 400, 520)
cv2.namedWindow('def', 0)
cv2.resizeWindow('def', 400, 520)
cv2.imshow('Fig6A', img)
cv2.imshow('Fig6B', dst)
cv2.imshow('def', def_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

