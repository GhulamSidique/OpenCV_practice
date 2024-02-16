# in this project we will set an alarm that will beep on motion detection
# for this we nee to have imutils and

# import the libraries
import cv2 as cv
import imutils # used for minor changes like resizing etc
import threading # in order to handle and display multiple changes in the data
import winsound # this is used to make a beep sound

# set the camera
cam=cv.VideoCapture(0) # will capture the live video from the camera

# setting the width and height of above camera
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640) # the width of the captured frames to 440 pixels.
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)# the height of the captured frames to 480 pixels.

# calculate the difference in the frames
_, start_frame=cam.read()

# resize the width of rame to 500 pixels
start_frame=imutils.resize(start_frame, width=500)

# change the colour of the frame
start_frame=cv.cvtColor(start_frame, cv.COLOR_BGR2GRAY)

# Gaussian blur to the initial frame to reduce noise.
start_frame=cv.GaussianBlur(start_frame, (21, 21), 0)

# setting the alarm modes initillay not active
alarm =False
alarm_mode=False
alarm_counter=0 # initially zero but will change when motion is detected

# function to beep an alarm
def beep_alarm():
    # setting the alarm var as global
    global alarm
    # loop till 3 consecutive beeps
    for _ in range(3):
        # condition to check if we are not in alarm mode
        # in following condition if we are not in alarm mode then we will break the loop
        if not alarm_mode:
            break

        # if we are in alarm mode then will beep the sound
        print("Alarm mode")
        winsound.Beep(2500, 1000)
    alarm=False

# main loop to capture the frames and many more
while True:
    _, frame=cam.read()
    # resize the frame
    frame=imutils.resize(frame, width=500)

    # if we are in alarm mode
    if alarm_mode:
        # then will change the frame colour into black and white

        frame_bw=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # blur the frame
        frame_bw=cv.GaussianBlur(frame_bw, (5, 5), 0)

        #now calculate the difference between the start_frame and the latest frame
        difference=cv.absdiff(start_frame, frame_bw)

        # set the threshold to get either white or black bgs
        # anything below 25 will be completely black and anything above it till 255 will be white
        thres=cv.threshold(difference, 25, 255, cv.THRESH_BINARY)[1] # here 1 means we will be 2nd value from the returned values that either 0 or 1

        # now setting the start frame to the current frame
        start_frame=frame_bw

        # now condition to check the threshold value to beep the sound
        # here we can set any value other than 300 it is used to capture the motion where it will start beeping
        # higher the threshold value higher must be the movement of the body or an object
        if thres.sum()>3000:
            # increase sthe alarm counter every time it beeps
            alarm_counter+=1

        # in case above condition is false
        else:
            if alarm_counter>0:
                # decrease the alarm counter if we do not see any movement
                alarm_counter-=1
        # so if we are in alarm mode then will shoe the movement in the video
        cv.imshow("Alarm mode", thres)
    else:
        # otherwise show the normal image
        cv.imshow("Normal image", frame)

    # condition to beep or not
    if alarm_counter>20:
        if not alarm:
            alarm=True
            # now cause the alarm
            threading.Thread(target=beep_alarm).start()

    # setting the key to be in alarm mode, not in alarm mode and quite the video
    pressed_key=cv.waitKey(30)
    # conditon to be in original/alarm video
    if pressed_key==ord('t'):
        alarm_mode=not alarm_mode
        alarm_counter=0

    # codition to quite the video
    if pressed_key==ord('q'):
        alarm_mode=False
        break

# now release the video
cam.release()
cv.destroyAllWindows()