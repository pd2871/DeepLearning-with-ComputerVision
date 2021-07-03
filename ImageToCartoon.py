import cv2
import numpy as np
from statistics import median

car = cv2.imread('car.jpg')
gray_car = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
blurred_car = cv2.GaussianBlur(gray_car, (3,3), sigmaX=2, sigmaY=9)
edges = cv2.adaptiveThreshold(blurred_car, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9)

cartoon = cv2.bilateralFilter(car, 9, 20,250)
cartoon = cv2.bitwise_and(cartoon, cartoon, mask=edges)
cartoon = cv2.resize(cartoon, (700,500))
cv2.imshow('Cartoon', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()