# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:28:55 2021

@author: life
"""

import cv2

img = cv2.imread("lena.jpg", 0)
t, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # t表示返回的阈值

t2, otsu = cv2.threshold(img, 0,1, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#  第二个参数必须是0， 第四个参数的第一位可以是之前博客说的那五种阈值处理的方式
test=cv2.multiply(otsu,dst)
#  自适应的输入图片必须是单通道图片
cv2.imshow('openCV-ostu', dst)
cv2.waitKey()
cv2.destroyAllWindows()