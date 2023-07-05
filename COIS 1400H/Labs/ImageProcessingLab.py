# Punyaja Mishra
# 066001
# Lab5: Image Processing Lab

##### PART 1: Converting an image to Black and White and Grayscale
# get the r,g,b values for each pixel - done by using height & width of image image[height, width, p]
# where p  is the r,g,b value - 0 for red, 1 for green & 2 for blue
# calculate average and set the r,g,b values to average

##### PART 2: Inverting an image


import matplotlib.pyplot
import numpy as np
from PIL import Image, ImageOps


myImage = matplotlib.pyplot.imread('flower.png')

#getting the size of an image
height=myImage.shape[0]
width=myImage.shape[1]

#going over the 2D array to eb able to access each pixel
for x in range(0, height-1):
    for y in range(0,width-1):
        # getting the RGB for each pixel
        r = myImage[x,y,0]
        g = myImage[x,y,1]
        b = myImage[x,y,2]
        #calculating average to convert to grayscale
        avg = (r+g+b)/3
        # setting the rgb values for each pixel to the new avg value
        myImage[x,y,0] = avg
        myImage[x,y,1] = avg
        myImage[x,y,2] = avg

# printing the grayscale image  
imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()


# Part 2
# since it has to be inverted and it is a numpy array so we cannot use invert function directly

#convert the image from numpy array using from array
tempImage = myImage*255
tempImage = tempImage.astype(np.uint8)
testImage = Image.fromarray(tempImage)

# converting image into supported mode - 'RGB' & inverting
invertedImage = ImageOps.invert(testImage.convert('RGB') )

#printing the image
imgplot = matplotlib.pyplot.imshow(invertedImage)
matplotlib.pyplot.show()
