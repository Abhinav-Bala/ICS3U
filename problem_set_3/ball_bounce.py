# Abhinav Balasubramanian
# March 11, 2021
# ICS3UO-C
# This program will print the height of the consecutive bounces of a ball given its initial height

check = False # initializes check variable
print("Welcome to the tennis ball height calculator.") # displays welcome message

# INPUT
while check == False: # while loop to handle invalid inputs
    try:
        height = float(input("Enter the initial drop height: ")) # gets user input and casts it as a float    
    except ValueError: # catches value error
        print("Invalid input. Try entering a number this time.") # prints error message 
        continue
    if height <= 0.0000000000000001: # checks if the height is less than 0.0000000000000001
        print("Invalid input. Try entering an number greater than 0.0000000000000001.") # prints error message
    else:
        break # exits the loop

# PROCESSING AND OUTPUT
bounce = 1 # initializes bounce variable
while height >= 0.0000000000000001: # while loop to determine all the bounce heights
    height = height / 2.0 # calculates the bounce height
    print("After bounce #" + str(bounce) + " the ball is " + str(height) + " meters high") # prints the height of the ball
    bounce += 1 # adds 1 to bounce variable
print("The ball will bounce a total of " + str(bounce - 1) + " times.")