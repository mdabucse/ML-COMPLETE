import cv2 as cv
import numpy as np

# Create image using Numpy
img_numpy = np.zeros([512,512,4],np.uint8)

img = cv.imread('helloman.jpg',1)
# Draw the line 
img = cv.line(img,(0,0),(255,255),(255,0,0),5,)
# Draw a Arrow Line
img = cv.arrowedLine(img,(120,0),(255,255),(0,0,255),5,)
# Create A Rectangle
img = cv.rectangle(img,(120,0),(255,255),(0,255,0),-1)# In the Final Parameter it is thickness when giving the -1 it fill the Rectangle Area
#Create a Circle
img = cv.circle(img,(250,10),60,(255,255,0),5)
# To add the Text Inside the Image
img = cv.putText(img,"Hello World",(10,400),4,1.0,(230,100,25),5)
cv.imshow('Window name',img)
cv.waitKey(0)
cv.destroyAllWindows()