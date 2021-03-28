# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:58:04 2020

@author: life
"""

import cv2
import numpy as np
img = cv2.imread('fig5.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('hist',res)
cv2.imwrite('hist.jpg',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
