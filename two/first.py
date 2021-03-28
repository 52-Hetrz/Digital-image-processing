import cv2
import numpy as np

'''
img1=cv2.imread('diamond2.jpg')
img2=cv2.imread('flower2.jpg')
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imwrite('dst.jpg',dst)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



img=cv2.imread('lily.tif',0)
img1 = cv2.add(img,80)
img2=cv2.subtract(img,80)
cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

