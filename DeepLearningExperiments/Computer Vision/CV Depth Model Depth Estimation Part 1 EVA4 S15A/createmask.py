# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:50:34 2020

@author: raajesh.rameshbabu
"""

import cv2
import matplotlib.pyplot as plt

im = cv2.imread('fg_1.png',cv2.IMREAD_UNCHANGED)
print(im.shape)
imagealpha = im[:,:,3]
print(imagealpha.shape)
plt.imshow(imagealpha,cmap='gray')
cv2.imwrite('mask.png',imagealpha)