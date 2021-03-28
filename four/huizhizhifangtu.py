# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:35:23 2020

@author: life
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('flower3.jpg',0)
plt.hist(img.ravel(),256,[0,256]);
plt.show()




