# in this project we will capture the edges of the objects within the video

# import libraries
import cv2 as cv
import numpy as np

# capture the video
video=cv.VideoCapture(0) 
# here 0 means we will capture the video from our laptop's camera

# we will capture edges through two methods
# one is laplacian method and another one is canny
# loop to get the return ad frames of the video
while True:
    # capture the return and frame
    ret,frame=video.read()
    # now applying laplacian method to capture the edges from the video
    lap=cv.Laplacian(frame, cv.CV_64F) # CV_64F means we will capture the 64 bit floating point number

    # converting above 64F into integers from 0 to 255
    lap=np.uint8(lap)

    # to display the screen of captured edges through laplacian method
    cv.imshow('Laplacian', lap)
    #====================================================================================

    # now to capture the edges through canny method
    can=cv.Canny(frame, 100, 100)
    # 100: lower threshold value. Any gradient value below this threshold is considered not to be an edge.
    # 100: higher threshold value. Any gradient value above this threshold is considered to be an edge

    # now display the results
    cv.imshow('Canny', can)


    if cv.waitKey(5)==ord('x'):
        break

cv.destroyAllWindows()
video.release()