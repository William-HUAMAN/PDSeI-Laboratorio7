# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:03:16 2023

@author: lenovo
"""
import cv2

import numpy as np
import matplotlib.pyplot as plt

frame = cv2.imread('img_r.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Ploteamos todas los canales del esapcio HSV
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
# Visualizamos canal H (0) o S(1)
plt.subplots(3,1, figsize=(10,10))
plt.subplot(311)
plt.imshow(hsv[...,0], cmap='gray')
plt.axhline(y=210, color='r')
plt.axvline(x=520, color='b')

plt.subplot(312)
plt.plot(hsv[210,:,0], 'r')

plt.subplot(313)
plt.plot(hsv[:,520,0], 'b')

plt.show()

# Selección de umbrales canal H
umbral = np.int32(hsv[...,0] > 140) 
hsv[...,2] = hsv[...,2] * umbral
# Selección de umbrales canal S
umbral2 = np.int32(hsv[...,1] > 20) 
hsv[...,2] = hsv[...,2] * umbral2

# Transformación al espacio HSV
img_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("imagen rojo",img_rgb)


# Mostrar el frame original y el resultado
# cv2.imshow('Frame', frame)es)
cv2.waitKey(0)