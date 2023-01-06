# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:03:16 2023

@author: lenovo
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
space_color = int(input("""
        ___________________________
        INGRESE SU ESPACIO DE COLOR
        ===========================
        
        (1) YCrCb
        (2) Lab

"""))
if space_color == 1:
    color_sp = cv2.COLOR_RGB2YCR_CB
    inv_color = cv2.COLOR_YCR_CB2RGB
    n1 = 2
    n2 = 0
elif space_color == 2:
    color_sp = cv2.COLOR_RGB2LAB
    inv_color = cv2.COLOR_LAB2RGB
    n1 = 1
    n2 = 0
    
frame = cv2.imread('img_r.png')
hsv = cv2.cvtColor(frame, color_sp)

##########################
plt.subplots(1,4, figsize=(20,5))
plt.subplot(141)
plt.imshow(hsv)

plt.subplot(142)
plt.imshow(hsv[...,0], cmap='gray')
plt.subplot(143)
plt.imshow(hsv[...,1], cmap='gray')
plt.subplot(144)
plt.imshow(hsv[...,2], cmap='gray')

plt.show()

##########################
plt.subplots(3,1, figsize=(10,10))
plt.subplot(311)
plt.imshow(hsv[...,n1], cmap='gray')
plt.axhline(y=210, color='r')
plt.axvline(x=520, color='b')

plt.subplot(312)
plt.plot(hsv[210,:,n1], 'r')

plt.subplot(313)
plt.plot(hsv[:,520,n1], 'b')

plt.show()
#######################
# umbral = np.int32(hsv[...,0] > 140) 
# # plt.imshow(umbral, cmap='gray')

# hsv[...,2] = hsv[...,2] * umbral

umbral2 = np.int32(hsv[...,n1] > 170) 
# plt.imshow(umbral, cmap='gray')

hsv[...,n2] = hsv[...,n2] * umbral2
print(":",np.max(umbral2))
img_rgb = cv2.cvtColor(hsv, inv_color)

cv2.imshow("imagen rojo",img_rgb)


# Mostrar el frame original y el resultado
# cv2.imshow('Frame', frame)es)
cv2.waitKey(0)