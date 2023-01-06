# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:27:05 2023

@author: lenovo
"""

import cv2                      # Importamos OpenCV2 
import numpy as np              # Librería numpy para Arrays


# 0. Cargar imágenes
im = cv2.imread('taj_mahal.png') 

# 1) Convertir la imagen RGB al espacio YUV.
im_yuv = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)

# 2) Calcular la media de los canales U y V.
mean_u = np.mean(im_yuv[:,:,1])
mean_v = np.mean(im_yuv[:,:,2])
mean = (mean_u + +mean_v)/2
print("Valores por defecto")
print("Media canal U: {} | Media canal V: {}".format(mean_u,mean_v))

# 3) Modificar U y V (suma) de manera que la media sea 128.
im_yuv[:,:,1] = im_yuv[:, :, 1] + ((128 - mean_u) * (im_yuv[:, :, 1])/255)
im_yuv[:,:,2] = im_yuv[:, :, 2] + ((128 - mean_v) * (im_yuv[:, :, 2])/255)
mean_u = np.mean(im_yuv[:,:,1])
mean_v = np.mean(im_yuv[:,:,2])
print("Media canal U: {} | Media canal V: {}".format(mean_u,mean_v))
# 4) Transformar la imagen YUV al espacio RGB.
img_rgb = cv2.cvtColor(im_yuv, cv2.COLOR_YUV2BGR)


cv2.imshow('Imagen balanceada', img_rgb)
cv2.imwrite('img_blank.png',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()