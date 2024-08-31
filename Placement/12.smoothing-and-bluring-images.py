'''
Filters:
1.Homogeneous Filter -> Mean of a Kernel Neighbourse
2.Gaussian Filter
3.Median Filter
4.Bilateral Filter
'''
# 2D Convolutional
    # Low Pass Filter (LPF) Helps To Remove Noises And Bluring the images
    # High Pass Filter (HPF) Finding Edges in the Images

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opencv.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel = np.ones((5,2),np.float32)/25 # It uses the 25 px 
destination = cv.filter2D(img,-1,kernel)

# Blur the Image
blur = cv.blur(img,(5,5))
gassian_blur = cv.GaussianBlur(img,(5,5),0)   # 3rd Parameter SigmaX -> Itha Use panni Pixels a Normalize pannum
median_filter = cv.medianBlur(img,3)# It  Used for the salt and pepper Noise-> Apdina Dotted a Irukum Noise # And the kernel size always odd

images = [img,destination,blur,gassian_blur,median_filter]
title = ['img','2d convolutional','Blur','Gaussian Blur','median_filter']


for i in range(len(images)):
    plt.subplot(3,4,i+1)
    plt.imshow(images[i])
    plt.title(title[i])


plt.show()

