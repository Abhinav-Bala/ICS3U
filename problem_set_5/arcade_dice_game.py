# Abhinav Balasubramanian
# March 23, 2021
# ICS3UO-C
# This program is a variation of the common higher or lower game.
# In the classic mode, the game will prompt the player to place a bet on whether 
# the sum of the next roll will be high or low, high being 8-12 inclusive and low 
# being 2-6 inclusive. If the sum is 7 or if the player guessed the wrong option, 
# they will lose all the coins they bet. If not, they will win double the coins back.
# In the blitz mode, the player will place a bet on the exact sum of the next roll. If
# they are correct, they will win 5x their bet amount. If they are off by one, they will
# win 3x their bet amount.

import random # imports python random library

# this function will checks if the user wants to quit the program
def checkQuit(user_input): # takes a string as a parameter
    if(user_input == 'quit'): # checks if the string is equal to quit
        print("==================================")
        print("\nGoodbye!\n\nShutting Down...\n") # prints goodbye message
        exit() # exits the program

# this function will check if the user wants to play again
def gameOver(): 
    print("\n=======================================================================================\n") # prints a spacer
    print("Uh oh, looks like you lost all your coins.") # game over message
    choice = input("To exit the game type 'quit'. To go back to the main menu type anything else: ") # gets input
    checkQuit(choice) # passes choice to checkQuit function

# this function will return a valid bet from the user
def getValidUserBet(current_balance): # takes the balance as a parameter

    while True: # loop will run until a valid input is given
        bet = input("Enter a bet amount: ") # gets input
        checkQuit(bet) # passes bet to checkQuit function
        try:
            bet = int(bet) # gets user input and casts it as an int
        except ValueError: # catches value error
            print("Invalid input. Enter an integer value this time") # prints error message
            continue
        if(bet > current_balance): # checks if the bet is greater than the balance
            print(f"Your bet is too large. The max. bet is {current_balance} coins") # prints error message
            continue
        elif bet < 1:
            print("Invalid bet. Enter a positive integer this time.")
            continue
        else:
            return bet # returns the validated bet variable

# this function will return a valid guess for the classic game mode
def getUserClassicGuess():
    while True: # loop will run until a valid input is given
        guess = input("Enter your guess: ") # gets user input
        checkQuit(guess) # passes guess to checkQuit function
        if(guess == 'high' or guess == 'low'): # checks if valid input is given
            return guess # returns validated guess
        else:
            print("Invalid guess. The two guesses are 'high' and 'low'.") # prints error message
            continue

# this function will return a valid guess for the blitz game mode
def getUserBlitzGuess():
    while True: # loop will run until a valid guess is given
        guess = input("Enter your guess: ") # gets input
        checkQuit(guess) # passes the guess to the checkQuit variable
        try:
            guess = int(guess) # tries to cast it as an int
        except ValueError: # catches value error
            print("Invalid input. Enter an integer this time") # prints error message
            continue
        if(guess < 2 or guess > 12): # checks if the guess is outside of the valid guess range
            print("Invalid input. Enter an integer between 2-12 this time.") # prints error message
            continue # goes back to the top of the loop
        else:
            return guess # returns the validated guess variable    

# this function will simulate rolling a pair of die and calculate the sum of their roll
def getDiceRoll():
    print("\nRolling...\n") # prints message
    dice_1 = random.randint(1, 6) # generates a random integer from 1-6
    print(f"Dice 1: {dice_1}") # prints the value of the first roll
    print("\nRolling...\n") # prints message
    dice_2 = random.randint(1, 6) # generates another random integer from 1-6
    print(f"Dice 2: {dice_2}\n") # prints the value of the second roll
    sum = dice_1 + dice_2 # adds both numbers together
    return sum # returns the sum

# this function prints the main menu and instructions
def printMainMenu():
    print('''
    Hello, welcome to the dice arcade.

    Here are the two game modes you can play:

    1) Classic
    2) Blitz

    To select a mode, just type the name. For example, if you 
    wanted to play the classic game mode type 'Classic'.

    If you would like to exit the game at any point, just type 'quit'.
    ''')     

# this function prints the classic game mode instructions
def printClassicInstructions():
    print('''
    You have selected the classic game mode.

    In this mode you will be prompted to place a bet and then guess 
    whether the sum of the roll of two dice will be high or low.

    A sum is considered high if the sum is 8-12 inclusive.
    A sum is considered low if the sum is 2-6 inclusive.
    If the sum is equal to 7, you will lose all the coins you bet :(

    If you guess correctly, you will receive double the coins you bet.
    If you guess incorrectly, you will lose all the coins you bet.

    Here are the rules:
    1) You can only bet an integer amount of coins

    To quit the game, just enter 'quit' at any time.
''')

# this function prints the blitz game mode instructions
def printBlitzInstructions():
    print('''
    You have selected the blitz game mode.

    In this mode you will be prompted to place a bet and then guess 
    the exact sum of a roll of two dice.

    If you guess correctly, you will receive 5x the coins you bet.
    If your guess is off by 1 either higher or lower, you will win 3x the coins you bet.
    If you are completely wrong, you will lose all the coins you bet.

    Here are the rules:
    1) You can only bet an integer amount of coins

    To quit the game, just enter 'quit' at any time.
''')

# this function prints the current balance of the user
def printBalance(balance):
    print("Your current balance is " + str(balance) + "\n")

while True: # main while loop that ensures the program is continuous
    # initializes variables
    coin_balance = 1000
    classic_mode = True
    
    while True: # loop will run until valid input is given
        printMainMenu()
        game_mode_type = input("Enter the game mode you wish to play: ") # gets user input
        checkQuit(game_mode_type) # passes game_mode_type to checkQuit function
        if(game_mode_type == 'classic' or game_mode_type == 'Classic'): # checks if user selected classic game mode
            break
        elif(game_mode_type == 'blitz' or game_mode_type == 'Blitz'): # checks if user selected blitz game mode
            classic_mode = False # sets classic_mode to False
            break
        else:
            print("Invalid input. Please enter a valid game mode") # prints error message
    
    if classic_mode: # checks if mode is set to classic
        printClassicInstructions()
        while True: # while loop will run until the user runs out of coins
            printBalance(coin_balance)
            user_bet = getValidUserBet(coin_balance) # gets the bet and assings it to user_bet
            user_guess = getUserClassicGuess() # gets the guess and assigns it to user_guess
            current_roll = getDiceRoll() # gets the random dice roll sum
            print(f"The sum of the two dice rolls is {current_roll}") # prints the dice roll sum
            if(current_roll < 7 and user_guess == 'low') or (current_roll > 7 and user_guess == 'high'): # checks if the user guessed correctly
                print("Since you guessed correctly, you win " + str(user_bet) + " coins.") # prints win message
                coin_balance += user_bet # adds the bet to the coin_balance

            else:
                print("Since you guessed incorrectly, you lost " + str(user_bet) + " coins.") # prints lose message
                coin_balance -= user_bet # subtracts the bet from the coin_balance
                if coin_balance <= 0: # checks if the user is bankrupt
                    break # exits the loop
                else:
                    pass
    else: # blitz mode
        printBlitzInstructions()
        while True: # while loop will run until the user runs out of coins
            printBalance(coin_balance)
            user_bet = getValidUserBet(coin_balance) # gets the bet and assings it to user_bet
            user_guess = getUserBlitzGuess() # gets the guess and assigns it to user_guess
            current_roll = getDiceRoll() # gets the random dice roll sum
            print(f"The sum of the two dice rolls is {current_roll}") # prints the dice roll sum
            if user_guess == current_roll: # checks if the guess is equal to the sum
                print("Since you guessed correctly, you win " + str(user_bet * 5) + " coins.") # prints win message
                coin_balance += user_bet * 5 # adds the bet x 5 to the balance
            elif (user_guess == current_roll - 1) or (user_guess == current_roll + 1): # checks if the guess was off by one
                print("Since your guess was close, you win " + str(user_bet * 3) + " coins.") # prints partial win message
                coin_balance += user_bet * 3 # adds the bet x 3 to the balance
            else:
                print("Since you guessed incorrectly, you lost " + str(user_bet) + " coins.") # prints lose message
                coin_balance -= user_bet # subtracts the bet from the balance
                if coin_balance <= 0: # checks if the user is bankrupt
                    break # exits the loop
                else:
                    pass 
    
    gameOver() # checks if the user wants to play again



