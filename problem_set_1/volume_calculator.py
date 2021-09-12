# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will output the volume of a rectangular prism given the width, length and height from the user

print('This program will caclulate the volume of a given rectangular prism.') # prints welcome message

# INPUT
width = float(input('Please enter the width of your rectangular prism: ')) # variable for inputted width casted as a float
length = float(input('Please enter the length of your rectangular prism: ')) # variable for inputted length casted as a float
height = float(input('Please enter the height of your rectangular prism: ')) # variable for inputted height casted as a float

# PROCESSING
volume = round((width * length * height), 1) # determines the volume using width, length and height; then rounds to one decimal place

# OUTPUT
print('The volume of your rectangular prism is ' + str(volume) + ' m^3') # outputs text and concatenates the casted string volume