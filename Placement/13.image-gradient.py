'''
https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('helloman.jpg',1)
lap = cv.Laplacian(img,cv.CV_64F,ksize=3)  
lap = np.uint8(np.absolute(lap))

# Canny Edge Detection
canny = cv.Canny(img,120,100)

images = [img,lap,canny]
title = ['img','lap','canny']

for i in range(len(images)):
    plt.subplot(3,4,i+1)
    plt.imshow(images[i])
    plt.title(title[i])

plt.show()

