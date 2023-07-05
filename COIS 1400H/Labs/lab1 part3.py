# Punyaja Mishra
# 0660001
# Lab 2

################# Part 3: Estimating Pi via a Monte Carlo approach
# Program caluclates the vlaue of pi by choosing random locations


# import the required modules
import random
import time
import math
from random import seed

# dfine the required variables
#number of random number inside and outside the circle & iterations
inside = 0
outside = 0
iterations = 1000000

#seed the random number generator
seed(1)

#iterating a 100000 times, so that we get enough random points inside and
#outside circle so that they can be equated to the area
for i in range(iterations):

    #random number generation - x & y
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    #caluclate distance from origin
    distance = math.sqrt(x*x + y*y)

    #conditions - inside circle
    if distance <= 1:
        inside+=1
    
    outside+=1

# calculate value of pi and then print the calculated value
pi = 4*(inside/outside)

print("\n pi = ", pi)

    
###### trying for a smaller iterations to see how pi value gets afected
for i in range(1000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    distance = math.sqrt(x*x + y*y)

    if distance <= 1:
        inside+=1
    
    outside+=1

pi = 4*(inside/outside)

print("\n pi = ", pi)
