import cv2 as cv
img = cv.imread('data\lena.jpg')
cv.imshow('lena',img)

# Resize
resized = cv.resize(img, (300,300))
cv.imshow('resized image',resized)

resizing = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resizing)

# interpolation=INTER_AREA- to shrink the dimensions of the image than the original image
# INTER_LINEAR or INTER_CUBIC - enlarging the image
# CUBIC is much slower than other functions but gives high quality image

#Cropping- cropped to some dimensions
cropped = img[50:200 , 200:400]
cv.imshow('cropped image', cropped)

cv.waitKey(0)
