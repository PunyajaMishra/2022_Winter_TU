# Punyaja Mishra
# 0660001
# Lab 4

# Program: multiplies 2 square matrices of same size after the user enters the
#   size of matrices


####################Part 1 -Runtime measurements with timing measurement
# using 'time' module to calculate elapsed time
# Ran the code multiple times for different times - 10, 50, 100, 250, 350, 500
# Clearly as expeted the time increased. For 10, elapsedTime was less than 10^-2 while
# for size 500 - when number of elements become 250000, the time was 24.5 ms
# The time per element keeps increasing with increasing size which makes sense since
# as the number of elements are increasing, the amount of memory being used increases which
# leads to an increases in time required to calculate per element.
# for elements = 2500 it was 0.0113 then for elements=10000 it was 0.0274
#for elements = 62500, it was 0.0473 then for elemets=1225500 it was 0.6679
#for elements=250000 it was 0.0980


###############Part 2: Runtime measuements with addition of profiler
# At first there was also an error of "module not found" so first had to pip install memory_profiler
#After adding the profiler, the amount of time to get the output increased drastically.
# The time which would be hardly closer to 1 second, was equal to 8 seconds for the same size
# for size 250, which means 62500 elements, the total elapsed time was actually equal to
# almost 15 minutes!
# i think the reason for such an increase and chnage in the time from part 1 is that we
# are now adding a new 'profiling' function. The program iteself is calucalting the
# the time the funciton takes and therefore, our manual calculation came out to be too long
# we can see the number of recurrences, so what line is recursed how many times and how
# much memory it uses from th e column of 'mem usage'
# pofiling would be a good method to understand the efficiency of a set of code. 





import random
import time
from memory_profiler import profile


@profile
def multiply():
    for i in range(size):
        for j in range(size):
            for k in range(size):
                P[i][j]=P[i][j]+(A[i][k]*B[k][j]) #multiplication



size=int(input("Enter size: "))

r1=size
c1=size
r2=size
c2=size


A=[[0 for i in range(c1)] for j in range(r1)] #initialize matrix A

#input matrix A
for i in range(r1):
    for j in range(c1):
        x=random.randint(1,100)
        A[i][j]=x

B=[[0 for i in range(c2)] for j in range(r2)] #initialize matrix B

#input matrix B
for i in range(r2):
    for j in range(c2):
        x=random.randint(1,100)
        B[i][j]=x

P=[[0 for i in range(c2)] for j in range(r1)] #initialize product matrix

#INSERT CODE TO START TIMER
start = time.time()
multiply() 
#INSERT CODE TO STOP TIMER
end = time.time()
#INSERT CODE TO COMPUTE ELAPSED TIME
elapsedTime = end - start #in seconds
elements = size * size
timePerElement = (elapsedTime/elements)*1000 #in ms
#INSERT CODE TO PRINT OVERALL TIME (IN s, NUMBER OF ELEMENTS IN THE RESULT MATRIX, AND TIME PER ELEMENT (IN ms)
print("Overall time: ", elapsedTime, " s",
      "\nNumber of elemtns in Result Matrix: ",elements,
      "\ntime per element: ", timePerElement, " ms")


