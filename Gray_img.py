import cv2 as cv
img = cv.imread('data\lena.jpg')
cv.imshow('lena',img)

#converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

cv.waitKey(0)