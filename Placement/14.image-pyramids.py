'''
Usually we need to convert an image to a size different than its original. For this, there are two possible options:
1.Upsize the image (zoom in) 
2.Downsize it (zoom out)

There are two common kinds of image pyramids:
Gaussian pyramid: Used to downsample images
Laplacian pyramid: Used to reconstruct an upsampled image from an image lower in the pyramid (with less resolution)

'''
import cv2 as cv
import numpy as np
img = cv.imread("helloman.jpg")


# Gaussian Pyramid
lower_down = cv.pyrDown(img)
upper_down = cv.pyrUp(img)



cv.imshow("Original image", img)
cv.imshow("Lower_Down image", lower_down)
cv.imshow("Upper_down image", upper_down)
cv.waitKey(0)
cv.destroyAllWindows()