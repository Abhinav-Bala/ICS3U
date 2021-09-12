# Abhinav Balasubramanian
# March 1, 2021
# ICS3UO-C
# This program will check whether an inputted integer is even or odd and positive, negative or zero

#INPUT
print("This program will determine whether an integer is even or odd.\nIt will also determine if the integer is positive, negative or zero") # displays welcome message
user_int = int(input("Enter your integer: ")) # gets user input, casts it as a float and then assings it to the variable user_int

#PROCESSING AND OUTPUT

# checks if user_int is positive or negative
if user_int % 2 == 0: # if the remainder is zero that means it is divisible by two
    print(str(user_int) + " is an even integer.") # concatenates user_int and prints that the integer is even
else:
    print(str(user_int) + " is an odd integer.") # concatenates user_int and prints that the integer is odd

# checks if user_int is positive, negative or 0
if user_int == 0: # checks if user_int is the integer 0
    print("This integer is also 0 (not positive or negative).") # concatenates user_int and prints that the integer is 0
elif user_int > 0: # checks if user_int is greater than 0
    print("This integer is also positive.") # prints that the integer is positive
else:
    print("This integer is also negative.") # prints that the integer is negative


