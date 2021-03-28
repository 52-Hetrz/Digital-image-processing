# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:52:55 2020

@author: life
"""

import cv2
import numpy as np

img=cv2.imread('lily.tif')
rows,cols,ch=img.shape
pts1=np.float32([[50,50],[200,20],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Input',img)
cv2.imshow('Output',dst)
cv2.imwrite('getAffineTransformImg.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
