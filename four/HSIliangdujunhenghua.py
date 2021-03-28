# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:03:04 2020

@author: life
"""

import cv2
import numpy as np

img = cv2.imread('fig6.jpg')
#把RGB转成HSI
his = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
cv2.imshow('img', img)
#只保留对I亮度的处理
his_i = his[:, :, 1]
#亮度均衡化处理之后的结果
equal_i = cv2.equalizeHist(his_i)
his[:, :, 1] = equal_i
#将HSI转换成RGB图
dst = cv2.cvtColor(his, cv2.COLOR_HLS2BGR)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
