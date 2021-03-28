# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:52:49 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('moon.jpg',0)
#cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
laplacian=cv2.Laplacian(img,-1)
#laplacian=cv2.Laplacian(img,-cv2.CV_64F)

# 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
dst=cv2.addWeighted(img,1,laplacian,-1,0)
plt.subplot(2,3,5),plt.imshow(dst,cmap = 'gray')
plt.title('Sub'), plt.xticks([]), plt.yticks([])

plt.show()
#dst=cv2.addWeighted(img,1,laplacian,-1,0)
