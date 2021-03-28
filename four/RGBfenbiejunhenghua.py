# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:14:52 2020

@author: life
"""

import cv2
import numpy as np

img = cv2.imread('fig6.jpg')
#将原图像中的RGB部分分解出来
(b, g, r) = cv2.split(img)
#对R，G，B三部分分别进行均衡化处理
equal_b = cv2.equalizeHist(b)
equal_g = cv2.equalizeHist(g)
equal_r = cv2.equalizeHist(r)
#将分别均衡化处理之后的图像再整合
dst = cv2.merge((equal_b, equal_g, equal_r))
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
