# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will output the length of the hypotenuse given the two other sides of a triangle

import math # imports the math library

print('Hello, this program will calculate the legnth of the hypotenuse of a right-triangle.') # prints welcome message

# INPUT
side_a = float(input('Enter the length of the first side: ')) # variable for inputted side a casted as a float
side_b = float(input('Enter the length of the second side: ')) # variable for inputted side b casted as a float

# PROCESSING
side_c = math.sqrt((side_a * side_a) + (side_b * side_b)) # determines the length of side c using the pythagorean theorem
side_c = round(side_c, 1) # rounding the length of side c to 1 decimal place

# OUTPUT
print('The length of the hypotenuse is: ' + str(side_c) + ' cm') # outputs text and concatenates the casted string side c                       
