import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
'''These code from the 9.threshold py file'''
# Plot multiple images inside a single plot
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

images = [image,th1,th2,th3,th4,ada_image,ada_thresh_mean,ada_thresh_gaussian]
title = ["Image",'Binary','Binary_Inverse','Truncate','TOZERO',"Ada Image",'ADAPTIVE_THRESH_MEAN_C','ADAPTIVE_THRESH_GAUSSIAN_C']
# print(len(images),len(title))

plt.figure(figsize=(20,20))
for i in range(len(images)):
    plt.subplot(2,4,i+1) 
    plt.imshow(images[i],'gray')
    plt.title(title[i])


plt.show()

