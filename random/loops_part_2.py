# Abhinav Balasubramanian
# March 3, 2021
# ICS3UO-C
# This program will print a square that has the width and length of the user's input

# INPUT
print("Welcome to the square maker.") # displays welcome message
user_int = int(input("Enter an integer above 0: ")) # gets user input and casts it as an int


#PROCESSING
length = ":D " * user_int
if user_int < 1: # checks if the integer is less than 1
    print("Enter a valid integer and try again") # prints error message
else:
    for counter in range (0, user_int): # loops the print statement until it is equal to user_int
        print(length) # prints one line of the square
        