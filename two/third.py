# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:39:42 2020

@author: life
"""

import cv2
import numpy as np
img1=cv2.imread('diamond2.jpg')
img2=cv2.imread('flower2.jpg')
img3=cv2.multiply(img1,img2)
cv2.imshow('dst',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()