'''
Hue - > Color Palette Used to change the color
Saturation -> Color Density or Intensity
Value -> Brightess Of the Color

'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the image
height = 256
width = 256

# Create a gradient from black (0) to white (1)
gradient = np.linspace(0, 1, width)

# Create a 2D array where each row is the gradient
image = np.zeros((height, width))

for i in range(height):
    image[i, :] = gradient

# Creating Threshold (Simple Thresholding)
_ , th1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
_ , th2 = cv.threshold(image,127,255,cv.THRESH_BINARY_INV)
_ , th3 = cv.threshold(image,127,255,cv.THRESH_TRUNC)  # After The Threshold value the value remains same using the truncate
_ , th4 = cv.threshold(image,127,255,cv.THRESH_TOZERO)

# Adaptive Threshold
ada_image = cv.imread('sudoko.png',0)
ada_thresh_mean = cv.adaptiveThreshold(ada_image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
ada_thresh_gaussian = cv.adaptiveThreshold(ada_image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)




cv.imshow("image",image)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('sudoko',ada_image)
cv.imshow('adaptive_mean',ada_thresh_mean)
cv.imshow('adaptive_gaussian',ada_thresh_gaussian)

cv.waitKey(0)
cv.destroyAllWindows()

