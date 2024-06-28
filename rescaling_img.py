import cv2 as cv 
img = cv.imread('data\digits.png')
cv.imshow('image',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimensions= (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img,scale = 0.5)
cv.imshow('resized_image',resized_image)

cv.waitKey(0)