# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:36:30 2023

@author: lenovo
"""
import cv2
import numpy as np


# 1) Acceder a la cámara
cap = cv2.VideoCapture(0)

# 2) Realizar en tiempo real 
while(1):
    
    frame = cap.read()[1]
    
    #3) Convertir a Espacio HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #4) Selección de umbrales de color
    umbral = np.int32(hsv[..., 0] < 10)
    umbral2 = np.int32(hsv[..., 1] > 100)
    umbral3 = np.int32(hsv[..., 2] > 100)
    
    #5) Segmentamos los colores
    hsv[..., 2] = hsv[..., 2] * umbral
    hsv[..., 2] = hsv[..., 2] * umbral2
    hsv[..., 2] = hsv[..., 2] * umbral3
   
    
    #6) Transformamos a Espacio BGR
    img_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    cv2.imshow("imagen rojo",img_rgb)
    cv2.imshow("frame",frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
