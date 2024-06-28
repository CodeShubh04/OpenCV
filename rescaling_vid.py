import cv2 as cv

#works for video, images and live videos
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)    # 1 is for width
    height= int(frame.shape[0] * scale)   #0 is for height
    dimensions= (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#changing resolution of video
#only for live video
'''
def changeRes(width,height):
    capture.set(3,width)    # 3 = width
    capture.set(4,height)   # 4 = height
'''

capture = cv.VideoCapture('vtest.avi')     #reading video
while True:
    isTrue, frame = capture.read()   #storing frames of video in frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Videos',frame)    #displaying each frame
    cv.imshow('video_resized',frame_resized)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'):         #if d is pressed break the loop
        break

capture.release()
cv.destroyAllWindows()