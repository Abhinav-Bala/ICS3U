# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will calculate the most optimal change to give for an amount that is less than or equal to 99 cents

print('Welcome to the change calculator!') # prints welcome message

# INPUT
change = int(input('Enter a value that is less than or equal to 99: ')) # variable for inputed user's change casted as an int

# PROCESSING
quarters = int(change / 25) # determines the number of quarters
change -= quarters * 25 # subtracts the quarters from the change
dimes = int(change / 10) # determines the number of dimes
change -= dimes * 10 # subtracts the dimes from the change
nickels = int(change / 5) # determines the number of nickels
change -= nickels * 5 # subtracts the number of nickels from the change
pennies = change # assigns the remaining change to pennies

# OUTPUT
print('The most optimal change for the amount given is: ') # prints text
print(str(quarters) + ' quarter(s)') # prints casted string quarters
print(str(dimes) + ' dime(s)') # prints casted string dimes
print(str(nickels) + ' nickel(s)') # prints casted string nickels
print(str(pennies) + ' pennies') # prints casted string pennies