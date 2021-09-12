# Abhinav Balasubramanian
# March 17, 2021
# ICS3UO-C
# This program will calculate the factorial of a given number from the user.


print("Hello there, welcome to the factorial calculator.\n") # displays welcome message
print("A factorial of an integer is the product of all the\npositive integers less than or equal to it.\nThe factorial is denoted by '!'.\n")  # defines a factorial
print("For example 4! = 1 x 2 x 3 x 4 = 24.\n")  # gives example of a factorial
print("=======================================================")

while True:  # this while loop will ensure the program will run continuously until the user wishes to quit

    factorial = 1  # initializes factorial variable

    while True:  # while loop to handle invalid inputs
        try:
            user_num = int(input("Enter an integer greater than or equal to 0: ")) # gets user input and casts it as an int
        except ValueError:  # catches value error
            print("Invalid input. Try entering an integer this time.") # prints error message
            continue  # goes back to the start of the loop
        if user_num < 0:  # checks if user_num is less than 0
            print("Invalid input. Try entering an integer greater than or equal to 0.") # prints error message
            continue  # goes back to the start of the loop
        else:
            break # exits the loop

    if user_num == 0: # checks if the integer inputted is 0
        print("0! = 1") # prints hard coded answer for 0! becuase it is a special case
    else:
        # initializes factorial_string variable
        factorial_string = str(user_num) + "! = "

        # for loop to cycles through all the integers that are less than or equal to user_num
        for counter in range(1, user_num):
            # contenates the next integer multiplied to the factorial string
            factorial_string += str(counter) + " x "
            factorial *= counter  # multiplies the next integer to the current factorial product

        # contenates the final answer to the factorial string
        factorial_string += str(user_num) + " = " + str(factorial * user_num)

        print(factorial_string)  # prints the final answer

    # gets user input and assigns it to user_quit
    user_quit = input("\nIf you wish to quit, type 'quit'. If not, input anything else: ")
    if user_quit == "quit":  # checks if input is equal to quit
        break  # exits the loop
    else:
        continue  # goes back to the start of the loop

# displays goodbye message
print("\nThank you for using the factorial calculator. Goodbye!")
