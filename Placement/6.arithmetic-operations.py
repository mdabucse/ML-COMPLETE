import cv2 as cv

img = cv.imread('helloman.jpg')
print(img.shape) # No of rows and columns
print(img.size) # Total no of Pixels
print(img.dtype) # image datatype

# To seperate all channels in the image
b,g,r = cv.split(img)


# if we want to merge all channels
img = cv.merge((b,g,r))

# ROI -> Region of Interest -> Crop the Image we need specific object in the image
cv.imshow('image-window',img)
man_head = img[20:27, 107:220]


# Add Two images -> If we want to add those things the two array size was same 
img_gray = cv.imread(r'A:\ML-COMPLETE\Placement\helloman-gray.jpg')
img = cv.resize(img,(512,512))
img_gray = cv.resize(img_gray,(512,512))
dst = cv.add(img,img_gray)


cv.imshow('manhead-window',man_head)
cv.imshow('added images',dst)
cv.waitKey(0)
cv.destroyAllWindows() 