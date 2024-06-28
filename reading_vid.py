import cv2 as cv
capture = cv.VideoCapture('vtest.avi')     #reading video
while True:
    isTrue, frame = capture.read()   #storing frames of video in frame
    cv.imshow('Videos',frame)    #displaying each frame

    if cv.waitKey(20) & 0xFF==ord('d'):         #if d is pressed break the loop
        break

capture.release()
cv.destroyAllWindows()

'''
the error after completion of video shows that the video ran out of frame 
so it stopped and window is destroyed.
'''