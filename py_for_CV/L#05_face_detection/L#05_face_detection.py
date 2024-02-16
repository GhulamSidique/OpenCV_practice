# in this projest we will detect reall time front face of people
import cv2 as cv
import pathlib

# to find the path of file from opencv
# this path will load the frontal face path and we will use it to detect the front face
cv_path=pathlib.Path(cv.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
# print(cv_path)

# we will use a classifier
clf=cv.CascadeClassifier(str(cv_path))

# to catch the video
video=cv.VideoCapture(0)

# loop to cath the frame
while True:
    _, frame=video.read()

    # changing the frames into gray
    g_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # now cath the faces
    faces=clf.detectMultiScale(
        g_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    for(x,y,height, width) in faces:
        cv.rectangle(frame, (x,y), (x+width, y+width), (255, 255, 0), 2)

        cv.imshow("faces", frame)
        if cv.waitKey(1)==ord("x"):
            break

video.release()
cv.destroyAllWindows()

