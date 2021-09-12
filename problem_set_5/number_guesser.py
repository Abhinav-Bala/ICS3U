# Abhinav Balasubramanian
# March 24, 2021
# ICS3UO-C
# This program will ask the user to enter a guess and then
# generate a random number within a specified range (if the user
# selected the classic mode, the range would be 1-10 or else
# the range would be custom). If the guess is equal to the random
# number, the player will win a point. The goal is to see how many
# points you can get before losing all your lives.

import random # imports the random library 

# this function generates the magic number given a min and max range as parameters
def generateMagicNumber(min, max):
    return random.randint(min, max) # returns a random integer within the given range

# this function will get a valid guess from the user given a min and max range as parameters
def getValidUserGuess(min, max):
    while True: # this loop will run until a valid input is given
        guess = input("Enter your guess: ") # gets user input
        checkQuit(guess) # runs the checkQuit function with guess as the parameter
        try:
            guess = int(guess) # casts guess as an int
            if(guess > max or guess < min): # checks if guess is not within the valid range
                print("Invalid input, enter an integer within the valid range.") # print error message
                continue
            else:
                return guess # returns the validated input
        except TypeError: # catches TypeError
            print("Invalid input, enter a number this time.") # prints error message
        except ValueError: # catches ValueError
            print("Invalid input, enter an integer this time.") # prints error message

# this function prints the main menu and instructions
def printMainMenu():
    print('''
    Hello, welcome to the number guesser.

    Here are the two game modes you can play:

    1) Classic
    2) Custom

    To select a mode, just type the name. For example, if you 
    wanted to play the classic game mode type 'Classic'.

    If you would like to exit the game at any point, just type 'quit'.
    ''')      

# this function will check if the user wishes to quit the program
def checkQuit(user_input): # gets a string as a parameter
    if(user_input == 'quit'): # checks if user_input is equal to 'quit'
        print("\nGoodbye!\nShutting Down...") # prints goodbye message
        exit() # exits the program

# this function will check if the guess is correct
def checkGuess(guess, magic_num): # takes a guess and magic_num as a parameter
    if(guess == magic_num): # checks if both values are equal
        print("\nGood job you guessed the number correctly.") # prints message
        return True # returns a boolean True
    else:
        print("\nSorry, your guess was incorrect. Try again.") # prints message
        return False # returns a boolean False

# this function will print the current game stats
def printGameStats(user_wins, user_lives): # takes wins and lives as a parameter
    print(f"Current score: {user_wins}") # prints the score
    print("Lives: " + str("♥ " * user_lives) + "\n") # prints the number of lives left

# this function prints the classic mode instructions
def printClassicInstructions():
    print('''
    You have selected the classic mode.

    In this mode, the program will generate a random number from 1-10 and your job
    will be to guess the number correctly. You will be given 10 lives and everytime
    you guess incorrectly, you will lose a life. When you lose all your lives, the game
    will end. Let's see how many times you can win before losing all your lives.

    ====================================================================================
        ''')

# this function prints the custom mode instructions
def printCustomInstructions():
    print('''
        You have selected the custom mode.

        In this mode, the program will generate a random number from a custom range
        you will provide and your job will be to guess the number correctly. You will be given 
        five lives and everytime you guess incorrectly, you will lose a life. When you lose 
        all your lives, the game will end. Let's see how many times you can win before the game
        is over.
        =======================================================================================
        ''')

# this function checks if the user wishes to play again
def gameOver(score):
    # prints game over message
    print("Uh oh, looks like you have run out of lives.")
    print(f"Your final score was {score}.")
    print("\n==============================================\n")
    user_quit = input("If you want to exit the game, type 'quit'. To play again type anything else: ") # asks the user if they want to play again
    checkQuit(user_quit) # passes user_quit to the checkQuit function

while True: # main while loop that makes sure the program runs continously

    #initializes variables
    min_range = int(1)
    max_range = int(10)
    classic_mode = True
    lives = 10
    wins = 0 
    
    while True: # loop will run until valid input is given
        printMainMenu()
        game_mode_type = input("Enter the game mode you wish to play: ") # gets user input
        checkQuit(game_mode_type) # passes game_mode_type to checkQuit function
        if(game_mode_type == 'classic' or game_mode_type == 'Classic'): # checks if user selected classic game mode
            break
        elif(game_mode_type == 'custom' or game_mode_type == 'Custom'): # checks if user selected custom game mode
            classic_mode = False # sets classic_mode to False
            break
        else:
            print("Invalid input. Please enter a valid game mode") # prints error message
    
    if classic_mode: # checks if the mode is set to classic
        printClassicInstructions()    
    else:
        printCustomInstructions()
        while True: # loop will run until a valid min value is given
            min_range = input("Enter the min range of your magic number: ") # gets user input
            checkQuit(min_range) # passes min_range to checkQuit function
            try:
                min_range = int(min_range) # casts as an int
                break
            except ValueError: # catches value error
                print("Enter an integer this time.") # prints error message
                continue
        while True: # loop will run until a valid max range is given
            max_range = input("Enter the max range of your magic number: ") # gets user input
            checkQuit(max_range) # passes max_range to checkQuit function
            try:
                max_range = int(max_range) # casts as an int
            except ValueError: # catches value error
                print("Enter an integer this time.")
                continue
            if max_range <= min_range: # checks if the max value is less than or equal to the min value
                print(f"Enter a max range that is greater than {min_range}") # prints error message
                continue
            else:
                break
    
    while True: # loop will generate a new magic number every round
        magic_number = generateMagicNumber(min_range, max_range) # generates a random number in a given range
        print(f"Round #{wins + 1}") # prints round #
        while True: # loop will run until user guesses correctly or loses all their lives
            user_guess = getValidUserGuess(min_range, max_range)        
            if checkGuess(user_guess, magic_number): # checks if the guess is correct
                wins += 1 # increments the win by 1
                break
            else:
                lives -= 1 # subtracts 1 from lives
                print("Lives: " + str("♥ " * lives) + "\n") # prints the current lives
                if lives == 0: # exits the loop if there are no more lives left
                    break
        if lives == 0: # checks if the user has 0 lives       
            gameOver(wins)
            break # exits the loop
        printGameStats(wins, lives)
            
        
        


            

     
