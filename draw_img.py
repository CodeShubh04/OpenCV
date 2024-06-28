import cv2 as cv
import numpy as np

#creating a dummy image
blank = np.zeros((500,500,3),dtype='uint8')  #in shape- height, width, no of colour channels
cv.imshow('blank',blank)
'''
#paint the image a certain colour
blank[:] = 0,255,255   # painting whole screen ; r,g,b
cv.imshow('Green',blank)

# painting a certain part
blank[200:300 , 300:400] = 0,255,0
cv.imshow('a_part',blank)
'''
#Draw a rectangle
cv.rectangle(blank, (0,0), (200,500), (0,0,255), thickness = -1)
cv.imshow('rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,255,0), thickness= -1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness= 3)
cv.imshow('line',blank)

#write text on an image
cv.putText(blank, "Hello", (255,355), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,255), 2)
cv.imshow("text",blank)

cv.waitKey(0)