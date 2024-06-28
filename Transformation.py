import cv2 as cv
import numpy as np
img = cv.imread('data\lena.jpg')
cv.imshow('lena',img)

# Translation - shifting an image on x and y axis
def translate(img, x, y):
    # x and y are pixels to be shift on axis
    # creating translation matrix
    transMat = np.float32([[1,0,x] , [0,1,y]])                  #this func takes a list containing 2 lists
    # dimensions = (width , height)
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left           -y --> up
# x --> right           y --> down

translated = translate(img, -100, 100)
cv.imshow('translated', translated)

cv.waitKey(0)
