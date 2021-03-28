# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:04:27 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
#对信号进行频率变换
f = np.fft.fft2(img)
#将直流分量（频率为0）部分输出在图像中心
fshift = np.fft.fftshift(f)
#构建振幅
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
