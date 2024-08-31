import cv2 as cv
import numpy as np

# Call Back Function
def nothing(x):
    print(x)

    
img = np.zeros((250,500,3),np.uint8)
cv.namedWindow('image')


# Track bar creation
cv.createTrackbar('B','image',0,255,nothing)  # We must give the call back funtion when creating the Trackbar
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

# Creating a Switch
switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'image',0,1,nothing)


while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1)
    if k==27:
        break
    # Get The Channel Values from the Trackabar
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')
    print("The Track Bar Values",b,g,r)
    if s==0:
        img[:]=0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()


