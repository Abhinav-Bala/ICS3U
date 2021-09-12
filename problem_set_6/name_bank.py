# Abhinav Balasubramanian
# March 31, 2021
# ICS3UO-C
# This program will ask the user to input names and then store them in a list. 
# Then the user will be presented with a menu of actions to perform including: displaying
# all the names, editing, adding, or removing a name.

# this functions prints the main menu
def printMainMenu():
    print(''' 
==============================================================
Here are the various actions you can perform:

1) Display all the names currently stored in the bank
2) Edit an existing name in the bank
3) Add a new name to the bank
4) Remove an existing name from the bank
0) Exit the program

To select an action, enter the corresponding number. For example,
to display all the names, you would enter '1'.
==============================================================
    ''')

# this function prints the display menu
def printDisplayMenu():
    print(''' 

    Here are the various ways to display the names:

    1) The order it was entered in
    2) Alphabetical by first name
    3) Reverse alphabetical by first name

    To select an action, enter the corresponding number. For example,
    to display the names in alphabetical order, you would enter '1'.

    To return to the main menu enter '0'

    ''')

# this function gets a valid initial list size from the user
def getListSize():
    while True: # loop until a valid input is given
        try:
            size = int(input("Enter the initial list size: ")) # tries to get input and cast as int
        except ValueError: # catches value error
            print("Invalid input. Enter an integer this time") # prints error message
            continue
        if size < 1: # checks if size is less than 1
            print("Invalid input. Enter an integer greater than or equal to 1.") # prints error message
            continue
        else:
            return size # returns valid size

# this function will get the initial list from the user
def getInitialList(list_size): # takes a size as parameter
    for counter in range(1, list_size + 1): # loops through until all names are given
        while True: # loops until a valid input is given
            first_name = input("Please enter the first name of person #" + str(counter) + ": ") # gets user input for first name
            last_name = input("Please enter the last name of person #" + str(counter) + ": ") # gets user input for last name
            if first_name_list.count(first_name) > 0 and last_name_list.count(last_name) > 0: # checks if name is already in the list
                print("Sorry, looks like this name is already in the bank") # prints error message
                continue
            elif first_name.isalpha() != True or last_name.isalpha() != True: # checks if the name contains invalid characters
                print("Invalid input. Names can only have letters of the alphabet.") # prints error messagte
            else:
                first_name_list.append(first_name) # adds first name to list
                last_name_list.append(last_name) # adds last name to list
                break # exits the loop

# this function gets a valid action from the user   
def getUserAction(min, max): # takes min and max values as parameters
    while True:  # while loop to keep asking for input until user provides a valid action
        try:  # error handling
            # gets user input and assigns
            action = int(input("Enter an integer for the corresponding action: "))
        except ValueError:  # catches value error
            # prints error message
            print("Inavlid input. Enter a valid integer this time.")
            continue
        if(action >= min and action <= max):  # checks if the input is within the valid range
            return action
        else:
            # prints error message
            print(f"Invalid action. Enter an option between {min} and {max}.")

# this function displays the current names in the bank
def displayNameBank():
    print("==============================================================")
    print("Here are all the names in the name bank:\n")
    for index in range(len(first_name_list)):
        print( "("+ str(index) + ") " + str(first_name_list[index]) + " " + str(last_name_list[index]))
    print("\n==============================================================\n")

# this function displays the edit name menu
def displayEditNameMenu():
    print('''
==============================================================
To edit a name in the name bank, you must enter the index of
the name you wish to edit. For example, if you wanted to edit
the first name on the list, you would type '0'.        
==============================================================    
    ''')

# this function displays the remove name menu
def displayRemoveNameMenu():
    print('''
==============================================================
To remove a name in the name bank, you must enter the index of
the name you wish to remove. For example, if you wanted to
remove the first name on the list, you would type '0'.        
==============================================================    
    ''')    

# this function edits a name in the bank
def editNameBank(index): # takes index as a parameter
    print("You have selected to edit: " + str(first_name_list[index]) + " " + str(last_name_list[index])) # prints the name selected
    while True: # waits for a valid name to be inputted
            first_name = input("Please enter the new first name: ") # gets first name
            last_name = input("Please enter the new last name: ") # gets last name
            if first_name_list.count(first_name) > 0 and last_name_list.count(last_name) > 0: # checks if the name is already in the list
                print("Sorry, looks like this name is already in the bank") # prints error message
                continue 
            elif first_name.isalpha() != True or last_name.isalpha() != True: # checks if invalid characters are inputted
                print("Invalid input. Names can only have letters of the alphabet.") # prints error message
            else:
                first_name_list[index] = first_name # edits the name in the bank
                last_name_list[index] = last_name # edits the name in the bank
                break

# this function adds a name to the list
def addNewName():
    print("You have selected to add a new name to the bank.") 
    while True: # loops until valid input is given
        first_name = input("Please enter the first name: ") # gets first name
        last_name = input("Please enter the last name: ") # gets last name
        if first_name_list.count(first_name) > 0 and last_name_list.count(last_name) > 0: # checks if name is already in the list
            print("Sorry, looks like this name is already in the bank") # prints error message
            continue
        elif first_name.isalpha() != True or last_name.isalpha() != True: # checks if an invalid character was inputted
            print("Invalid input. Names can only have letters of the alphabet.") # prints error message
        else:
            first_name_list.append(first_name) # adds first name to list
            last_name_list.append(last_name) # adds last name to list
            break # exits loop

# this function removes a name from the list
def removeName(index): # takes index as parameter
    del first_name_list[index] # removes the first name at the given index
    del last_name_list[index] # removes the last name at the given index
    print("Name removed.\n")
    

# initializes variables
first_name_list = []
last_name_list = []
phone_list = []

print("Hello, this is the name bank.") # prints welcome message
user_size = getListSize() # gets the initial size
getInitialList(user_size) # gets the initial name bank

while True: # main while loop
    printMainMenu()
    user_action = getUserAction(0, 4) # gets the valid action from the user

    if user_action == 0: # checks if the user wants to quit
        break
    elif user_action == 1: # checks if the user wants to display the names
        displayNameBank()
    elif user_action == 2: # checks if the user wants to edit a name
        displayEditNameMenu()
        displayNameBank()
        edit_index = getUserAction(0, len(first_name_list) - 1) # gets a valid index from the user
        editNameBank(edit_index)
    elif user_action == 3: # checks if the user wants to add a new name
        addNewName()
    elif user_action == 4: # checks if the user wants to remove a  name
        displayRemoveNameMenu()
        displayNameBank()
        remove_index = getUserAction(0, len(first_name_list) - 1) # gets a valid index
        removeName(remove_index)
    print("If you want to exit the program, type 'quit'.")
    user_quit = input("If you want to perform another action enter anything else: ") # gets user quit input 
    if(user_quit == 'quit' or user_quit == 'Quit'): # checks if the user want to quit
        break # exits the loop
    else: 
        continue # goes back to top of the loop
    
print("Goodbye!\nShutting down...") # prints goodbye message


            







        