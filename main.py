#python3
#Author: Gabriele Chelossi
#Created the 28th of July, 2018
#Last Modified: 28/07/2018 (DD/MM/YYY)

import os
from PIL import Image
from pytesseract import image_to_string

dirname = os.path.dirname(__file__)
fileOne = os.path.join(dirname, 'img/1.png')
fileTwo = os.path.join(dirname, 'img/2.png')
fileThree = os.path.join(dirname, 'img/3.png')

myText = image_to_string(Image.open(fileOne))
print(myText)
myText = image_to_string(Image.open(fileTwo))
print(myText)
myText = image_to_string(Image.open(fileThree))
print(myText)
