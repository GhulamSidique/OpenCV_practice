# to extract colors from image we need to have colorthief intsalled and imported
# to install it we have to run the following command line on the command prompt
# pip install colorthief

# now import it
from colorthief import ColorThief
import matplotlib.pyplot as plt

# extract the color
ct=ColorThief("E:/computer vision/py_for_CV/L#06_extract_colors_from_images/image1.webp")

# getting top 5 colors from image
palettes=ct.get_palette(color_count=5)

# show the palettes
plt.imshow([[palettes[i] for i in range(5)]] )      
plt.show()