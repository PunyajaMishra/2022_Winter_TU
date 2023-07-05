# Punyaja Mishra
# 0660001
# Lab 2

##################  Part 2 : Checking fo rrandomness
# Program to create 1000 random INTEGERS between 1 & 10.
# Program then counts the number of times the random integer
# generated is less than or equal to 5 && greater than 5. 


# import the required functionalites to be used/libraries
import time
import random
from random import seed

# define the variables high and low to calculate <=5 and >5
higher = 0
lower = 0

#seed random number generator
seed(1)

#create 1000 integer random numbers
#create a for loop that repeats 1000 times
for i in range(1000):
    #random integer is created in range 1-10
    number = int(random.uniform(1,10))
    #now conditions are checked for higher or lower
    if number > 5:
        higher+=1
    else:
        lower+=1

print("\n Numbers greater than 5 : ", higher)
print("\n Numbers less than equal to 5 : ", lower)


