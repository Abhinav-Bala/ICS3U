# Abhinav Balasubramanian
# March 11, 2021
# ICS3UO-C
# This program will check whether an input is the password or not

print("Welcome to the password checker.") # prints welcome message

#INPUT 
password = input("Please enter your password: ") # gets user input and assigns it to password
password_2 = input("Please enter your password again: ") # gets user input and assigns it to password_2

while password != password_2: # loops aslong as both passwords do not match
    print("The passwords you have entered do not match.") # prints error message
    password = input("Please enter your password: ") # gets user input and assigns it to password
    password_2 = input("Please enter your password again: ") # gets user input and assigns it to password_2

print("\n=============")
print("Now we can check your password.")

#PROCESSING AND OUTPUT
user_string = input("Enter your guess: ") # gets input from the user and assings it to user_string
while password != user_string: # while loop will run until the input matches the password
    user_string = input("Sorry that was incorrect, try again: ") # gets input from the user and assigns it to user_string
print("You guessed your password correctly!") # prints ending message

