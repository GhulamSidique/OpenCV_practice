# in this project we will write a code to capture the moving objects in a video or live camera
# for this we need to have a video downloaded or a live camera
# opencv is used to perform this kind of task

# import the opencv library
import cv2 as cv

# capture the live video from camera
video=cv.VideoCapture(0) 
# here 0 means 1 camera is used 
# if we have a video downloaded then we will simply write the path of that video in the parenthesis

subtractor=cv.createBackgroundSubtractorMOG2(20, 90)
# the subtractor is used to remove the background from the video to display the moving objects
# 30: This parameter represents the history length, which is the number of frames used to build the initial background model.
# 50: This parameter represents the threshold value, which is used to classify whether a pixel is part of the background or foreground. Pixels with a high enough difference from the background model are considered as foreground. 

# loop to capture each frame of the video
while True:
    # this loop will return a return value and a frame by reading the video each time it runs
    ret, frame = video.read()

    # condition if we get the moving objects in the form of return value
    if ret:
        # if there is any return value then we will apply the mask over each frame of the video's moving object
        mask=subtractor.apply(frame)
        
        # will display the mask 
        cv.imshow('Mask', mask)

        # condition to break the loop
        # if we press the 'x' key the video will stop
        if cv.waitKey(5)==ord('x'):
            break
    # if there is no return value then we will again reset the video
    else:
        video = cv.VideoCapture(0)

cv.destroyAllWindows()
video.release()
