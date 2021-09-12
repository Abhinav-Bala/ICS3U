# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will output the circumference of a circle given the radius from the user

import math # import the math library
print('This program will caclulate the circumference of a given circle.') # prints welcome message

# INPUT
radius = float(input('Enter the radius of the circle: ')) # variable for inputted user's radius casted as a float

# PROCESSING
circumference = round((2 * math.pi * radius), 1) # determines the circumference using the given radius; then rounds to 1 decimal place

# OUTPUT
print('The circumference of your circle is ' + str(circumference) + ' cm') # outputs text and concatenates the casted string circumference