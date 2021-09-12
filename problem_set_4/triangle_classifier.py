# Abhinav Balasubramanian
# March 17, 2021
# ICS3UO-C
# This program will calssify a triangle as scalene, isoceles or equilateral given the 3 side lengths

print("Hello, welcome to the triangle classifier") # displays welcome message

while True:

    while True: # while loop to handle invalid inputs
        try:
            side_1 = float(input("Enter the length of side 1: ")) # gets user input and casts it as an int     
        except ValueError: # catches value error
            print("Invalid input. Try entering a number this time.") # prints error message
            continue
        if side_1 <= 0: # checks if the length is less than 0
            print("Invalid input. Try entering a positive number this time.") # prints error message
            continue
        else:
            break
    
    while True: # while loop to handle invalid inputs
        try:
            side_2 = float(input("Enter the length of side 2: ")) # gets user input and casts it as an int     
        except ValueError: # catches value error
            print("Invalid input. Try entering a number this time.") # prints error message
            continue
        if side_2 <= 0: # checks if the length is less than 0
            print("Invalid input. Try entering a positive number this time.") # prints error message
            continue
        else:
            break
    
    while True: # while loop to handle invalid inputs
        try:
            side_3 = float(input("Enter the length of side 3: ")) # gets user input and casts it as an int     
        except ValueError: # catches value error
            print("Invalid input. Try entering a number this time.") # prints error message
            continue
        if side_3 <= 0: # checks if the length is less than 0
            print("Invalid input. Try entering a positive number this time.") # prints error message
            continue
        else:
            break
    
    if side_1 == side_2 and side_2 == side_3 and side_1 == side_3: # checks if all the side lengths are the same
        print("This is an equilateral triangle.")
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3: # checks if one of the side lengths are equal to another
        print("This is an isoceles triangle.")
    else:
        print("This is a scalene triangle.")

    user_quit = input("\nIf you wish to quit, type 'quit'. If not, input anything else: ") # gets user input and assigns it to user_quit
    print("\n=========================================================")
    if user_quit == "quit": # checks if input is equal to quit
       
        break # exits the loop
    else:
        continue # goes back to the start of the loop

print("Thank you for using the triangle classifier. Goodbye!") # prints goodbye message




    
        
