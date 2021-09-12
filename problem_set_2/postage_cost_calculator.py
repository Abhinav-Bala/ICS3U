# Abhinav Balasubramanian
# March 1, 2021
# ICS3UO-C
# This program will determine the cost of postage given the inputted weight (g).

# INPUT
print("Hello, this program will determine the cost of postage based on the weight of the package in grams.") # displays welcome message
weight = float(input("Enter the weight of your package in grams: ")) # gets input and casts as float

# PROCESSING AND OUTPUT
if weight == 0:
    print("Your package does not have a weight, please try again.") # prints answer
elif 0 < weight <= 30: # checks if weight is greater than 0 and less than or equal to 30
    print("The cost of postage will be $0.48.") # prints answer
elif 30 < weight <= 50: # checks if weight is greater than 30 and less than or equal to 50
    print("The cost of postage will be $0.70.") # prints answer
elif 50 < weight <= 100: # checks if weight is greater than 50 and less than or equal to 100
    print("The cost of postage will be $0.90.") # prints answer
elif weight > 100: # checks if weight is greater than 100
    additional_cost = round(((weight - 100) * 0.03 + 0.90), 2) # determines the additional cost and rounds to two decimal places
    print("The cost of your postage will be $" + str(additional_cost)) # prints answer
else:
    print("Please enter a valid weight and try again.") # prints error message
