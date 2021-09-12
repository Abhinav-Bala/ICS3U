# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will take a 3 digit number and output the hundreds, tens and ones place

print('This program will output the hundreds, tens and ones place of a given 3 digit number.') # prints welcome message

# INPUT
user_num = int(input('Enter your 3 digit number: ')) # variable for inputted number casted as an int

# PROCESSING
hundreds = int(user_num/100) * 100 # determines the amount of hundreds 
user_num -= hundreds # subtracts the hundreds from the user's number
tens = int(user_num/10) * 10 # determines the amount of tens
user_num -= tens # subtracts the tens from the user's number
ones = user_num # assings the remaining to the ones

# OUTPUT
print('The number you have entered can be split into: ' + str(hundreds) + ' + ' + str(tens) + ' + ' + str(ones)) # prints text and concatenates the hundred, tens and ones 

