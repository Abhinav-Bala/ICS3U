# Abhinav Balasubramanian
# March 11, 2021
# ICS3UO-C
# This program will calculate the average and sum of a set of student's grades

check = False # initializes check variable 
print("Hello, this program will determine the average and sum of a set of grades") # displays welcome message

#INPUT AND PROCESSING
while check == False: # while loop to handle invalid inputs
    try:
        students = int(input("Enter the number of the students: ")) # gets user input and casts it as an int     
    except ValueError: # catches value error
        print("Invalid input. Try entering an integer this time.") # prints error message
        continue
    if students < 1: # checks if students is less than 1
        print("Invalid input. Try entering an integer greater than 0.") # prints error message
    else:
        check = True

sum = 0.0 # initializes sum variable
for counter in range(1,students + 1): # loop to get all the user inputs for the student grades
    while True: # infinite while loop to handle invalid inputs
        try:
            grade = int(input("Enter the grade of student #" + str(counter) + ": ")) # gets user input and casts it as a float     
        except ValueError: # catches value error
            print("Invalid input. Try entering an integer this time.") # prints error message
            continue
        if grade < 0.0 or grade > 100.0: # checks if sum is less than 0 or greater than 100
            print("Invalid input. Try entering a value greater than or equal to 0 and less than or equal to 100.") # prints error message
        else:
            sum+= grade # adds the current grade to the sum
            break # exits the while loop

average = round((sum / students), 2)

#OUTPUT
print("The sum of the students grades is: " + str(sum)) # prints the sum of the grades
print("The average of the students grades is: " + str(average)) # prints the average of the grades