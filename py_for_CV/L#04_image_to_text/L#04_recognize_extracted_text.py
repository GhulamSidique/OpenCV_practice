# in this project we will recognize the extraced text from a picture
import PIL.Image
import pytesseract
import cv2 as cv

# make configuration by looking at above list
config1=r"--psm 3 --oem 3"

# read the image
image=cv.imread('E:/computer vision/py_for_CV/L#04_image3.jpg')

# catch the height and width of the text
height, width, _=image.shape

# create the boxes
boxes=pytesseract.image_to_boxes(image, config=config1)

# loop around the boxes
for box in boxes.splitlines(): # we have separate individual characters at each line
    # split the text based on space
    box=box.split(" ") 

    # creating the boxes
    image=cv.rectangle(image, (int(box[1]), height-int(box[2])), (int(box[3]), height-int(box[4])), (0,255,0),2)

cv.imshow("image",image)
cv.waitKey(0)
