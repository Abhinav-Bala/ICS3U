# Abhinav Balasubramanian
# March 31, 2021
# ICS3UO-C 
# This program will take a string input and then create a dictionary with the
# count of each type of character. It will also print the distribution of letters

# this function will count the amount of characters in a string
def countCharacter(character_string, lowerCase): # takes a string and boolean as parameters
    if lowerCase == True: # checks if lowerCase is True
        character_string = character_string.lower() # changes all the characters to lower case
    character_dictionary = {} # initializes dictionary
    for char in character_string: # loops for every character in the string
        exisiting_characters = character_dictionary.keys() # gets all the current keys
        if char in exisiting_characters: # checks if the character is already in the dictionary
            character_dictionary[char] += 1 # increments the corresponding count
        else:
            character_dictionary[char] = 1 # creates a new key and sets the count to 1
    return character_dictionary # returns the dictionary of the character count

# prints a visual distribution of the letters
def printLetterDistribution(char_dict): # takes a dictionary as parameter
    print("This is a visual representation of the distribution of letters") 
    for char in char_dict: # loops for every character in the dictionary
        print(char + ": " + str(char_dict[char] * '=')) # prints the distribution

# displays welcome message and instructions
print("Hello, welcome to the character counter.")
print("This program will take in a string and then output the count of each character.\n")

while True: # main while loop
    user_string = input("To begin, please enter the string you wish to sort: ") # gets the initial string
    print("\nIf you would like to count upper case and lower case as same characters enter 'yes'.") 
    bothSame = input("If not, enter anything else: ") # checks if the user wants to count higher and lower case as the same
    if bothSame == 'yes' or bothSame == 'Yes': # checks if the input is 'yes' or 'Yes'
        user_dictionary = countCharacter(user_string, True) # counts higher and lower case as the same
    else:
        user_dictionary = countCharacter(user_string, False) # counts higher and lower case as different
    print("\n")
    print(user_dictionary) # prints the dictionary
    print("\n")
    printLetterDistribution(user_dictionary) # prints the distribution

    print("\nIf you would like to exit the program enter 'quit'.")
    user_quit = input("If you would like to count another string, enter anything else: ") # gets user input for quit
    if user_quit == 'quit' or user_quit == 'Quit': # checks if the user wants to quit the program
        print("Goodbye. Shutting down...") # prints goodbye message
        exit() # exits the program
    else:
        continue # goes back to the start of the loop
