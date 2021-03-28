# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:50:27 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.bmp')
blur3 = cv2.GaussianBlur(img,(3,3),0)
blur5 = cv2.GaussianBlur(img,(5,5),0)
blur7 = cv2.GaussianBlur(img,(7,7),0)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur3),plt.title('Gaussian 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur5),plt.title('Gaussian 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur7),plt.title('Gaussian 7*7')
plt.xticks([]), plt.yticks([])
plt.show()