# Abhinav Balasubramanian
# Feb. 24, 2021
# ICS3UO-C
# This program will output the corresponding level and letter grade for the inputted percentage

#INPUT
name = input("Welcome to the grade calculator, please enter your name: ") # displays welcome message and takes name input
course = input("Hi " + name + ", please enter your course name: ") # gets user input for course name
grade = float(input("Please enter the percentage you acheived in " + course + ": ")) # gets user input for course grade
if grade < 100.0 and grade > 0: # checks to see whether the grade is within the valid range
    
    #PROCESSING AND OUTPUT
    if grade < 50.0: # checks whether grade is less than 50
        print("You acheived a letter grade of F and level grade of R") 
    elif grade < 60.0: # check whether grade is less than 60
        print("You acheived a letter grade of D and level grade of 1")
    elif grade < 70.0: # checks whether grade is less than 70
        print("You acheived a letter grade of C and level grade of 2")
    elif grade < 80.0: # checks whether grade is less than 80
        print("You achieved a letter grade of B and level grade of 3")
    else:
        print("You acheived a letter grade of A and level grade of 4. Keep up the good work!")
else:
    print("Please try again and enter a valid percentage.") # prints error message indicating to enter a valid percentage