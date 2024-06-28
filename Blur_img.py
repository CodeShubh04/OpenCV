import cv2 as cv
img = cv.imread('data\lena.jpg')
cv.imshow('lena',img)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
# to increase the blur effect, increase the kernel size i.e., (3,3)

canny = cv.Canny(blur,123,145)
cv.imshow('canny',canny)
cv.waitKey(0)