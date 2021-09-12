# Abhinav Balasubramanian
# March 1, 2021
# ICS3UO-C
# This program will check whether an inputted year is a leap year or not

#INPUT
print("This program will check to see whether a given year is a leap year.") # displays welcome message
year = int(input("Please enter a year: ")) # gets user input for year and then casts it as an int

#PROCESSING AND OUTPUT

if year % 4 == 0: # checks if the year is divisible by 4
    if year % 100 == 0: # checks if the year is divisible by 100
        if year % 400 == 0: # checks if the year is divisible by 400
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is not a leap year.")
    else:
        print(str(year) + " is a leap year.")
        
else:
    print(str(year) + " is not a leap year.") # concatenates the year and prints the answer