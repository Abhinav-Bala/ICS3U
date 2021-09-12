# Abhinav Balasubramanian
# March 18, 2021
# ICS3UO-C
# This program will calculate the class average given the student's grades. It will also display the distribution of grades and how many are failing or passing.

print("Hello, this program will calculate your class average and the distribution of grades.") # displays welcome message

while True: # this loop will run until the user decides to quit

    # initializes and resets the variable values
    a_grades = 0
    b_grades = 0
    c_grades = 0
    d_grades = 0
    e_grades = 0
    f_grades = 0
    grades_sum = 0.0

    while True: # while loop to handle invalid inputs
        try:
            students = int(input("Enter the number of the students in your class: ")) # gets user input and casts it as an int     
        except ValueError: # catches value error
            print("Invalid input. Try entering an integer this time.") # prints error message
            continue
        if students < 1: # checks if students is less than 1
            print("Invalid input. Try entering an integer greater than 0.") # prints error message
            continue
        else:
            break
    
    for counter in range(1, students + 1): # for loop that repeats until all the student grades have been inputted
        while True: # while loop to handle invalid inputs
            try:
                student_grade = float(input("Enter the grade of student #" + str(counter) + " : ")) # gets user input and casts it as an int     
            except ValueError: # catches value error
                print("Invalid input. Try entering a number this time") # prints error message
                continue
            if student_grade > 100 or student_grade < 0: # checks if student grade is within the valid range
                print("Invalid input. Try entering an grade greater than 0 and less than 100.") # prints error message
                continue
            else:
                grades_sum += student_grade # adds the current grade to the total grade sum
                if(student_grade < 40): # checks if grade is classified as an F
                    f_grades+= 1 # increments by 1
                elif(student_grade < 50): # checks if grade is classified as an E
                    e_grades+= 1 # increments by 1
                elif(student_grade < 60): # checks if grade is classified as an D
                    d_grades+= 1 # increments by 1
                elif(student_grade < 70): # checks if grade is classified as an C
                    c_grades+= 1 # increments by 1
                elif(student_grade < 80): # checks if grade is classified as an B
                    b_grades+= 1 # increments by 1
                else:
                    a_grades+= 1 # increments by 1
                break # exits the loop
    
    print("\n----------------------------------------------------")
    print("\nIn you class of " + str(students) + " students:\n")
    print("The average is: " + str(round((grades_sum / students), 2)) + "%") # calculates and prints the class average rounded to two decimals
    print(str(e_grades + f_grades) + " students are failing.") # calculates and prints the amount of students failing
    print(str(students - e_grades - f_grades) + " students are passing.\n") # calculates and prints the amount of students passing
    print("The grade distribution is as follows:\n") # prints the grade distribution of each grade
    # generates a '=' for each student with that specific grade and then prints the number value
    # this helps the user visualize the grade distribution
    print("A: " + str("="* int(a_grades)) + " (" + str(a_grades) + ")")
    print("B: " + str("="* int(b_grades)) + " (" + str(b_grades) + ")")
    print("C: " + str("="* int(c_grades)) + " (" + str(c_grades) + ")")
    print("D: " + str("="* int(d_grades)) + " (" + str(d_grades) + ")")
    print("E: " + str("="* int(e_grades)) + " (" + str(e_grades) + ")")
    print("F: " + str("="* int(f_grades)) + " (" + str(f_grades) + ")\n")

    user_quit = input("\nIf you wish to quit, type 'quit'. \nIf you want to calculate the grade for another class, enter anything else: ") # gets user string input
    if(user_quit == 'quit'): # checks if the user entered 'quit'
        break # exits the loop
    else:
        print("\n=============================================================\n") 
        continue # goes back to the top of the loop

print("Goodbye!") # prints goodbye message


                