# Abhinav Balasubramanian
# March 16, 2021
# ICS3UO-C
# This program serves as a calculator that can perform addition, subtraction, divison,
# multiplication, exponent, modulus operations and calculate the root(s) of a quadratic

import cmath  # imports the complex math library

# displays a text art calculator welcome screen
print('''
 _____________________
|  _________________  |
| | Hello :D        | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

# displays welcome message
print("Welcome, this is a calculator that can perform basic mathematical operations!\n")

while True:  # this loop will make sure the program will run until the user wants to quit

    # prints the menu and explains how to use the calculator
    print("Here are the various operations you can perform:\n")
    print("1) Additon\n2) Subtraction\n3) Division\n4) Multiplication\n5) Exponent\n6) Modulus\n7) Quadratic Roots\n0) Quit\n")
    print("To select an operation or action, enter the corresponding number. For example,")
    print("if you wanted to perform an addition operation, you would enter '1'.")
    print("\n==============================================================================\n")

    while True:  # while loop to keep asking for input until user provides a valid action
        try:  # error handling
            # gets user input and assigns
            action = int(input("Enter an integer for the corresponding action: "))
        except ValueError:  # catches value error
            # prints error message
            print("Inavlid input. Enter a valid integer this time.")
            continue
        if(action > -1 and action < 8):  # checks if the input is within the valid range
            break
        else:
            # prints error message
            print("Invalid action. Enter an option between 0 and 6.")

    if(action == 0):  # checks if input is equal to 0
        break  # exits the loop

    # addition calculator
    elif(action == 1):  # checks if input is equal to 1
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_1 = float(input("Enter the first number you wish to add: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_2 = float(input("Enter the second number you wish to add: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        print(str(num_1) + " + " + str(num_2) + " = " + str(num_2 + num_1))  # calculates and prints the sum

    # subtraction calculator
    elif(action == 2):  # checks if input is equal to 2
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_1 = float(input("Enter the first number: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_2 = float(
                    input("Enter the number you wish to subtract from " + str(num_1) + " : "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        # calculates and prints the difference
        print(str(num_1) + " - " + str(num_2) + " = " + str(num_1 - num_2))

    # division calculator
    elif(action == 3):  # checks if input is equal to 3
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_1 = float(input("Enter the dividend: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and casts it as a float
                num_2 = float(input("Enter the divisor: "))
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
            if(num_2 == 0):
                print("Invalid input. Enter a non-zero number this time.")
            else:
                break
        print(str(num_1) + " / " + str(num_2) + " = " + str(num_1 / num_2))  # calculates prints the result

    # multiplication calculator
    elif(action == 4):  # checks if input is equal to 4
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input
                num_1 = float(input("Enter the first number: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input
                num_2 = float(input("Enter the second number: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        # calculates and prints the product
        print(str(num_1) + " x " + str(num_2) + " = " + str(num_1 * num_2))

    # exponent calculator
    elif(action == 5):  # checks if input is equal to 5
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                num_1 = float(input("Enter the base: "))  # gets user input
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                num_2 = float(input("Enter the exponent: "))  # gets user input
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        try:
            print(str(num_1) + "^" + str(num_2) + " = " + str(num_1 ** num_2))  # prints the result
        except OverflowError:  # catches overflow error
            print("The exponent produces a result that is too large to be displayed")

    # modulus calculator
    elif(action == 6):  # checks if input is equal to 6
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and assigns
                num_1 = int(input("Enter the dividend: "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a integer number this time.")
                continue
        while True:  # while loop to keep asking for input until user provides a valid number
            try:  # error handling
                # gets user input and assigns
                num_2 = int(input("Enter the divisor: "))
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid integer this time.")
                continue
            if(num_2 == 0):
                print("Invalid input. Enter a non-zero integer this time.")
            else:
                break
        print(str(num_1) + " mod " + str(num_2) + " = " + str(num_1 % num_2))  # prints the result

    # quadratic root calculator
    elif(action == 7):  # checks if input is equal to 7
        while True:  # while loop will run until a valid input is given
            try:  # error handling
                # gets user input
                quadratic_a = float(input("Enter the value of 'a': "))
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
            if(quadratic_a == 0):
                print("Invalid input. Enter a non-zero number this time.")
            else:
                break
        while True:  # while loop will run until a valid input is given
            try:  # error handling
                # gets user input
                quadratic_b = float(input("Enter the value of 'b': "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        while True:  # while loop will run until a valid input is given
            try:  # error handling
                # gets user input
                quadratic_c = float(input("Enter the value of 'c': "))
                break
            except ValueError:
                # prints error message
                print("Inavlid input. Enter a valid number this time.")
                continue
        # calculates the discriminant using the quadratic formula and then rounds to 6 decimal places
        discriminant = round((quadratic_b ** 2) - (4 * quadratic_a * quadratic_c), 6)
        # calculates the first root of the quadratic
        quad_sol_1 = (-quadratic_b - cmath.sqrt(discriminant)) / (2 * quadratic_a)
        # calculates the second root of the quadratic
        quad_sol_2 = (-quadratic_b + cmath.sqrt(discriminant)) / (2 * quadratic_a)
        if quadratic_b * quadratic_b < 4 * quadratic_a * quadratic_c: # checks if the quadratic has no real roots
            print("This quadratic has no real roots.")
        # checks if both of the roots are the same
        elif(quad_sol_1 == quad_sol_2 and quadratic_b * quadratic_b >= 4 * quadratic_a * quadratic_c):
            print("The root in the quadratic is x = " + str(quad_sol_2))  # prints the singular root
        else:
            print("The roots in the quadratic are x = " + str(quad_sol_1) + " and x = " + str(quad_sol_2))  # prints the two roots

    # gets user input
    user_quit = input("\nIf you wish to quit, type 'quit'. \nIf you want to perform another calculation enter anything else: ")
    if(user_quit == 'quit'):  # checks if the input is equal to 'quit'
        break  # exits the loop
    else:
        print("\n=============================================================\n")
        continue  # goes to the top of the loop

# prints goodbye message
print("\nThank you for using the calculator. Goodbye!")
print('''
 _____________________
|  _________________  |
| | Shutting down...| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
