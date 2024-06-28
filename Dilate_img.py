import cv2 as cv
img = cv.imread('data\lena.jpg')
#cv.imshow('lena',img)

canny = cv.Canny(img,123,145)
#cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)
# increase in iterations makes the edges appear thicker

# Eroding 
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow('eroded image',eroded)

cv.waitKey(0)