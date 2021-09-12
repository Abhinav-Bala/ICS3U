# Abhinav Balasubramanian
# March 3, 2021
# ICS3UO-C
# This program will determine the square, square root and cube of the numbers from 1-7
import math # imports the math library

#PROCESSING AND OUTPUT
for counter in range (0,7):
    print(str(round(math.sqrt(counter), 3)) + "\t" + str(counter * counter) + "\t" + str(counter * counter * counter)) # calculates square root, square and cube of the number and prints it