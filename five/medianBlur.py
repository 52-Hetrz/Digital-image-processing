# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:47:15 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.bmp')
blur3 = cv2.medianBlur(img,3)
blur5 = cv2.medianBlur(img,5)
blur7 = cv2.medianBlur(img,7)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur3),plt.title('Median 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur5),plt.title('Median 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur7),plt.title('Median 7*7')
plt.xticks([]), plt.yticks([])
plt.show()