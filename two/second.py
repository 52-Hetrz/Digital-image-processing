# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:19:03 2020

@author: life
"""

import cv2
import numpy as np
img1=cv2.imread('diamond2.jpg')
img2=cv2.imread('flower2.jpg')
dst=cv2.addWeighted(img1,1,img2,-1,0)
cv2.imwrite('dst.jpg',dst)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()