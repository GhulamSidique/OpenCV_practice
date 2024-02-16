# in this project we will extract the text from an image

'''
we have to select the psm modes from any of the following for text extractions


0 Orientation and script detection (0SD) only.
1 Automatic page segmentation with OSD.
2 Automatic page segmentation, but no OSD, or OCR.
5 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
a Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of text.
7 Treat the image as a single text Line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw Line. Treat the image as a single text Line,
'''

'''
Select any of follwoing OCR engine modes

0 Legacy engine only.
1 Neural nets LSTM engine only.
2 Legacy + LSTM engines.
3 Default, based on what is available
'''

import PIL.Image
import cv2 as cv
import pytesseract

# make the configurations by selecting the psm and oem values
config1=r"--psm 6 --oem 3"
config2=r"--psm 6 --oem 3"
config3=r"--psm 10 --oem 3"
config4=r"--psm 11 --oem 3"

# extracting the text
text1=pytesseract.image_to_string(PIL.Image.open('E:/computer vision/py_for_CV/L#04_image1.png'), config=config1)
print("The text from image 1")
print(text1)
print("===============================================================================\n\n")
text2=pytesseract.image_to_string(PIL.Image.open('E:/computer vision/py_for_CV/L#04_image2.PNG'), config=config2)
print("The text from image 2")
print(text2)
print("===============================================================================\n\n")
text3=pytesseract.image_to_string(PIL.Image.open('E:/computer vision/py_for_CV/L#04_image3.jpg'), config=config1)
print("The text from image 3")
print(text3)
print("===============================================================================\n\n")
text4=pytesseract.image_to_string(PIL.Image.open('E:/computer vision/py_for_CV/L#04_image4.webp'), config=config4)
print("The text from image 3")
print(text4)
print("===============================================================================\n\n")