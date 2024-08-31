import cv2 as cv
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv.imread('helloman.jpg')


# Bitwise and Operator
bitAnd = cv.bitwise_and(img1[:100,:100],img2[:100,:100]) # The Both images have same size
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('bitAnd',bitAnd)

cv.waitKey(0)
cv.destroyAllWindows()