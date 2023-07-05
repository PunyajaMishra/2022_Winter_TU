# Punyaja Mishra
# 0660001
# Lab 2

############################## PART 2 : Estimating the error
# program shows us floating point issues. Since toAd = 0.1, the iteration should print 0.1, 0.2, 0.3, and so on, however, as we can see, out of the 10 iterations, there were 6 right iterations while 4 wrong sum printed.
# FOR ITERATIONS = 10 - the differnece is veryyy small, it goes to e^-16 as we can see, which means 0.000001
# FOR ITERATIONS = 100 - the differnece is still small, but it increased to e^-14
# FOR ITERATTIONS = 1000 - the difference increased by e+2, and is now e^-12
# Thus, it would be safe to conclude, that with increasing power of 10, the error increases by e+2. 10^1 -> error was e^-16 | 10^3 -> e^-12
# FOR 10^9, the error, should at least not be a float with e-12 and so on, but something as large as the number we are adding which in this case is ".1"


############################## PART 3 : Estimating the scope of the problem
# 2 numbers between 0 and 1 for which there are also incorrect results for 100 iterations
#       0.15, 0.99

# 2 numbers between 0 and 1 for which there are correct results for 100 iterations
#       0.5, 0.25

# 0.15 and 0.99 cannot be represented EXACTLY as binary, whereas it is easier to represent 0.5 nd 0.25 to represent them as binary. Therefore, they give correct answer while the other 2 does not. 
# Some numbers upon being added repeatedly yields wrong sum, while other yield correct results. One thing to notice is that the 2 numbers that I found to give correct sum are multiples of 5, like 0.5, 0.25. This is because,
# these nubers can also be written easily as a base of 10, which is a decimal. As we will see in next part, decimal gives correct answer than a float. Converting base 10 to base 2 gives a pretty more accurate answer.


############################## PART 4 : One potential solution
# upon using decimal module, the difference was much greater than when using flaoting point. The sum of numbers when using decimal, was much greater than the correct result.
# correct result = 10
# for floating, sum = 9.99999999999998
# for decimal, Sum =  19.99999999999998101518627860
# upon doing a little research online, it seems, that decimal module is actually a better way to deal with decimal numbers.
# However, they also hve a default predefined context which conatains defualt values for precision, rounding, flags, minimum and maximum numbers allowed. So, it is also important to look at this predefined context so we can either
# work around it or change the precision and context for the program. Therefore, if we change the precision let's say, we should be getting a better answer, and not WORSE than FLOATING POINT. 



import decimal

sum = 0
toAdd = .1
max = 100 #ENTER NUMBER OF ITERATIONS HERE
correctResult = sum + max*toAdd

############### first loop
for i in range (0, max, 1):
        sum = sum + toAdd
difference = correctResult - sum

#ADD A PRINT STATEMENT HERE THAT PRINTS (WHEN THE LOOP IS FINISHED) THE NUMBER
#OF ITERATIONS, THE NUMBER YOU ADDED, THE SUM YOU CALCULATED, AND
#THE DIFFERENCE BETWEEN THE CORRECT RESULT AND YOUR SUM
print("\nNumber of Iterations = ", max,
      "\nNumber added = ", toAdd,
      "\nSum = ", sum,
      "\nCorrect Result = ",correctResult ,
      "\nDifference = ", difference )

############### second loop      
for i in range (0, max, 1):
        sum = decimal.Decimal(sum) + decimal.Decimal(toAdd)

difference = decimal.Decimal(correctResult) - sum


#ADD A PRINT STATEMENT HERE THAT PRINTS (WHEN THE LOOP IS FINISHED) THE NUMBER
#OF ITERATIONS, THE NUMBER YOU ADDED, THE SUM YOU CALCULATED, AND
#THE DIFFERENCE BETWEEN THE CORRECT RESULT AND YOUR SUM
print("\nNumber of Iterations = ", max,
      "\nNumber added = ", toAdd,
      "\nSum = ", sum,
      "\nCorrect Result = ",correctResult ,
      "\nDifference = ", difference )





