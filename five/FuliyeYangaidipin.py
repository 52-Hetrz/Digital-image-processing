# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:09:43 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
#进行频率变换
f = np.fft.fft2(img)
#将直流分量移到图像的中心
fshift = np.fft.fftshift(f)
#获取图像的尺寸
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
#掩盖低频分量
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#进行逆平移操作
f_ishift = np.fft.ifftshift(fshift)
#傅里叶逆变换
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
