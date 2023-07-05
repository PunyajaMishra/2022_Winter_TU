# Punyaja Mishra
# 0660001
# Lab 10 : Numpy

# Part 3: Create a 1-D array with 1000 random integers between 1 & 100. PRint out the
# shape & datatype of array; print min, max, sum, mean, standard deviation of values of array


###############################################
# Part 4: OBSERVATION
# When I tried to run the program with array size till 10000 - the elapsed time for all kinds
# of sort was VERYY less - 0.0 seconds. Therefore, I had to increase the size of teh 1-D array by a lot

# 1. For both sizes '10000000' & '100000000' - the quickest method is the 'Quicksort'
#   method and the longest is the 'Heapsort'.
# 2. As the size of the array increses by a 10th, the time taken for sorting increase by a lot of SECONDS
#    For example, the time went from 0.03 to 3 seconds; similarly for merge sort the time went from 0.05
#    to 7 seconds - that is the increase is almost "100 times"!! That is a drastic increase
# 3. The time difference in the Mergesort & Heapsort is up by 1 for the left most value
#    In other words, the difference in time for mergesort & heapsort is not as much as between the quicksort
#    and the other 2 (merge and heap)



import numpy as np
import time

##### Part 3 #####

# create 1-D array with 1000 random integers from 1-100
myArray = np.random.randint(100, size = 1000)

# print dimensions of the array
print("My Array Dimensions: ", myArray.ndim)

# print shape of the array
print("My Array Shape: ", myArray.shape)

# print datatype of the array
print("My Array Data Type: ", myArray.dtype)

# minimum of values in array
print("Minimum of values in My Array: ", np.min(myArray))

# maximum of values in array
print("Maximum of values in My Array: ", np.max(myArray))

# sum of values in array
print("Sum of values in My Array: ", np.sum(myArray))

# mean of values in array
print("Mean of values in My Array: ", np.mean(myArray))

# standard deviation of values in array
print("Standard Deviation of values in My Array: ", np.std(myArray))



##### Part 4 #####

print("-------------------------------------------------")
for i in range(3):
    # take size of array as a variable
    arraySize = int(input("Enter the size of array: "))

    # create 1-D array
    myArray = np.random.randint(100, size = arraySize)

    print("Size = ", arraySize)

    # Quick sort
    start = time.time()
    array1 = np.sort(myArray)
    end = time.time()
    print("Quicksort Time: ", (end-start))

    # Mergesort
    start = time.time()
    array2 = np.sort(myArray, kind='mergesort')
    end = time.time()
    print("Mergesort Time: ", (end-start))
        
    #Heapsort
    start = time.time()
    array3 = np.sort(myArray, kind='heapsort')
    end = time.time()
    print("Heapsort Time: ", (end-start))
    






