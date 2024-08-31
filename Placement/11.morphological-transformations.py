'''
* Morphologocal Transformations are some simple operations based on the image shape
* Normally performed on Binary Images
Requirements:
1.Original Image
2.Kernel -> It decide the nature of the operation

# Must See
https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img  = cv.imread('j.png',0)
_,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)

# Dilation -> This is the method to reduce the unwanted dots inside the image after filtering
dilation = cv.dilate(mask,kernel,iterations=2)

# Erosion -> add a boundary on the substance inside the image
erosion = cv.erode(mask,kernel,iterations=2)

images = [img,mask,dilation,erosion]
titles = ['img','masking','dilation','erosion']

for i in range(len(images)):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
