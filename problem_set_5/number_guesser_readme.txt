Author: Abhinav Balsburamanian 
Class: ICS3U0 - C
Date: March 26th, 2021
Version: 2.7
Unit: 4
Question: 1
Programming Language: Python 3.9.1

Programming Description: This program will start by displaying the main menu and 
instructions on how to select a game mode. In the classic game mode, the program will
generate a random integer from 1-10 inclusive and the player's job is to guess the number
correctly. The player starts off with 10 lives and everytime they enter an incorrect guess
they will lose a life. If they guess correctly they will get one point and then a new number
will be generated. This process will repeat until the player has no more lives. The custom
mode adds a feature where the user can select the range in which the integer will be generated.
Other than that, it follows the same rules and procedure as the classic mode. 

Program Assumptions: In order to play the game, the user must enter a valid guess (an integer within 
the given range). Additionally, the program assumes the user understands the min and max range
values they enter are inclusive in the custom mode. Furthermore, the player is responsible for
remembering their previous guesses and making sure not to enter duplicate guesses in the same
round. Fluency of English is another assumption because all the prompts are written in English.

Features of the Program: As mentioned before, the program has a second mode called custom where
the user can select the range of the random integer by entering the min and max values. 
Additionally, the program introduces the concept of lives and prints a heart (♥) to represent
a single life. 

Restrictions: Once a game mode has been selected, the player must play the game until
they run out of lives before being prompted to switch to a different mode.

Known Errors: N/A