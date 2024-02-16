# in this project we will try to make less readable image into more readable one
import cv2 as cv

# read the image
image=cv.imread('E:/computer vision/py_for_CV/L#03_image.jpeg')

# covert the image colour
image=cv.cvtColor(image, cv.COLOR_RGB2GRAY)

# catch the return and result values
ret, result=cv.threshold(image, 100, 255, cv.THRESH_BINARY)
# here image is the source 
# we deal with pixels of the image starting from 0 to 255, 0 means completely black and 255 means completely white
# here 35 means any value that is darker will be converted into white or vice versa
#  means we need to convert the image from darker to white
# cv.THRESH_BINARY it is the built algo name 

adaptive=cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 51, 10)
# here adaptiveThreshold is used which gives better results than threshold
# 255 means the brightes region
# cv.ADAPTIVE_THRESH_GAUSSIAN_C It is Gaussian method, Adaptive thresholding calculates thresholds for small regions of the image based on the local mean or weighted sum of pixels values.
# cv.THRESH_BINARY it's converting pixel values above the threshold to the maximum value (255) and pixel values below the threshold to 0.
# 81 This parameter specifies the size of the local region around each pixel for calculating the adaptive threshold. It's typically an odd number representing the size of the pixel neighborhood.
# 10 This parameter specifies a constant value that is subtracted from the calculated mean or weighted sum of pixels values.

# actual image
cv.imshow('Actual', image)
# using threshold 
cv.imshow("Through threshold", result)
# using adaptive method
cv.imshow('Through adaptive', adaptive)

cv.waitKey(0) # the screen will be closed when it is closed
cv.destroyAllWindows()