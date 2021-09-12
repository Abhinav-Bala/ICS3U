# Abhinav Balasubramanian
# March 11, 2021
# ICS3UO-C
# This program will print a number pyramid that has a height equal to the user's input

check = False # initializes check variable; this variable will be true when a valid input is given
print("Hello, this program will print a number pyramid.") # displays welcome message

#INPUT
while check == False: # while loop to handle invalid inputs
    try:
        height = int(input("Enter the height of the pyramid: ")) # gets user input and casts it as an int   
    except ValueError: # catches value error
        print("Invalid input. Try entering an integer this time.") # prints error message
        continue
    if height < 1: # checks if height is less than 1
        print("Invalid input. Try entering an integer greater than 0.") # prints error message
    else:
        check = True

#PROCESSING AND OUTPUT
for counter in range (1, (height + 1)): # loop until counter is equal to the height + 1
    print((str(counter) + " ") * counter) # prints one layer of the pyramid at a time

