import cv2 as cv
from cv2 import blur
img = cv.imread('data\lena.jpg')
cv.imshow('lena',img)

#Edge Cacade- to find the edges present in the image
# canny edge detector- multistep process that includes lot of blurring and grading computations

canny = cv.Canny(img,123,145)
cv.imshow('Canny', canny)
#the number of thresholds increases, lesser the appearance of edges in the canny image  --123 and 145 are thresholds

cv.waitKey(0)
