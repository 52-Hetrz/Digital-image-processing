# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:39:51 2020

@author: life
"""

import cv2
import numpy as np
img=cv2.imread('flowerx.png')
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
cv2.imshow('res',res)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destotyAllWindows()