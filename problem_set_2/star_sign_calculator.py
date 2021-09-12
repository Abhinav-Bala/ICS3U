# Abhinav Balasubramanian
# March 1, 2021
# ICS3UO-C
# This program will determine the user's star sign

# INPUT
print("This program will determine your star sign.")
day = int(input("Enter your birthday: ")) # gets user input for day and casts it as an int
month = int(input("Enter the month you were born on: ")) # gets user input for month and casts it as an int

# PROCESSING AND OUTPUT
if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19): # checks to see if the birthday falls under Aries
    print("You are an Aries!") # prints answer
elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20): # checks to see if the birthday falls under Taurus
    print("You are a Taurus!") # prints answer
elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 21): # checks to see if the birthday falls under Gemini
    print("You are a Gemini!") # prints answer
elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22): # checks to see if the birthday falls under Cancer
    print("You are a Cancer!") # prints answer
elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22): # checks to see if the birthday falls under Leo
    print("You are a Leo!") # prints answer
elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22): # checks to see if the birthday falls under Virgo
    print("You are a Virgo!") # prints answer
elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 23): # checks to see if the birthday falls under Libra
    print("You are a Libra!") # prints answer
elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 21): # checks to see if the birthday falls under Scorpio
    print("You are a Scorpio!") # prints answer
elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21): # checks to see if the birthday falls under Sagittarius
    print("You are a Sagitttarius!") # prints answer
elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19): # checks to see if the birthday falls under Capricorn
    print("You are a Capricorn!") # prints answer
elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18): # checks to see if the birthday falls under Aquarius
    print("You are a Aquarius!") # prints answer
elif (month == 2 and 19 <= day <= 28) or (month == 3 and 1 <= day <= 20): # checks to see if the birthday falls under Pisces
    print("You are a Pisces!") # prints answer
else:
    print("Please enter a valid month and day, and try again.") # error message      

    
        