# Abhinav Balasubramanian
# March 1, 2021
# ICS3UO-C
# This program will determine a user's credit card points given various information inputted from the user

# INPUT
print("This program will evaluate your credit card application and output a suitable credit card for you.") # displays welcome message
age = int(input("Please enter your age: ")) # gets user input and casts it as an int
address = int(input("How long have you been at your current address? ")) # gets user input and casts it as an int
income = int(input("Enter your annual income: ")) # gets user input and casts it as an int
job = int(input("How long have you been at your current job? ")) # gets user input and casts it as an int

#PROCESSING
# determines the amount of points for the user's age
if age <= 20: # checks if age is less than 20 or equal
    points = -10 # assigns value to points
elif 21 <= age <= 30: # checks if age is less than or equal to 30 and greater than or eqaul to 21
    points = 0 # assigns value to points
elif 31 <= age <= 50: # checks if age is greater than or equal to 31 and less than or equal to 50
    points = 20 # assigns value to points
elif age > 50: # checks if age is greater than 50
    points = 25 # assigns value to points

# determines the amount of points for the user's current address
if address < 1: # checks if address is less than 1
    points += -5 # subtracts -5 from points
elif 1 <= address <= 3: # checks if address is greater than or equal to 1 and less than or equal to 3
    points += 5 # adds 5 to points
elif 4 <= address <= 8: # checks if address is greater than or equal to 4 and less than or equal to 8
    points += 12 # adds 12 to points
elif address > 8:
    points += 20 # adds 20 to points

# determines the amount of points for the user's income
if 15000 <= income < 25000: # checks if income is between 15000-25000
    points += 12 # adds 12 to points
elif 25000 <= income < 40000: # checks if income is less than 40000
    points += 24 # adds 24 to points
elif income >= 40000: # checks if income is greater than or equal to 40000
    points += 30 # adds 30 to points

# determines the amount of points for the user's job
if job < 2: # checks if job is less than 2
    points += -4 # subtracts 4 from points
elif 2 <= job <= 4: # checks if job is between 2-4
    points += 8 # adds 8 to points
elif job > 4:
    points += 15 # adds 15 to points

# OUTPUT
if points <= 20: # checks if points is less than or equal to 20
    print("No card.") # prints answer
elif 21 <= points <= 35: # checks if points is greater than or equal to 21 and less than or equal to 35
    print("Card with $500 limit.") # prints answer
elif 36 <= points <= 60: # checks if points is greater than or equal to 36 and less than or equal to 60
    print("Card with $2000 limit.") # prints answer
else:
    print("Card with $5000 limit.") # prints answer

