# Punyaja Mishra
# 066001
# Optinal Line Detection for Bonus Mark

import matplotlib.pyplot 
import numpy as np
from PIL import Image, ImageOps

myImage = matplotlib.pyplot.imread('flower.png')

height=myImage.shape[0]
width=myImage.shape[1]

#converting to grayscale
for x in range(0, height-1):
    for y in range(0,width-1):
        r = myImage[x,y,0]
        g = myImage[x,y,1]
        b = myImage[x,y,2]
        avg = (r+g+b)/3
        myImage[x,y,0] = avg
        myImage[x,y,1] = avg
        myImage[x,y,2] = avg

#line detection code
newArray = np.ones((height,width,3), dtype=np.float64)
for x in range(0, height-1):
  for y in range(0, width-1):
    if (myImage[x,y,0] - myImage[x+1,y,0]) > 0.03 and (myImage[x,y,0] - myImage[x,y+1,0]) > 0.03 :
      newArray[x,y,0] = 0
      newArray[x,y,1] = 0
      newArray[x,y,2] = 0

imgplot = matplotlib.pyplot.imshow(newArray)
matplotlib.pyplot.show()
