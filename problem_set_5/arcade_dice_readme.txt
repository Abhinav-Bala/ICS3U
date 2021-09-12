Author: Abhinav Balsburamanian 
Class: ICS3U0 - C
Date: March 26th, 2021
Version: 2.17
Unit: 4
Question: 2
Programming Language: Python 3.9.1

Programming Description: This program is a variation of the commonly played
high or low game. The program begins by presenting the player with two
game modes, classic or blitz. At the start, the player is given 1000 coins in 
their balance. The classic game mode first prompts the player
to place a bet and then guess whether the sum of a pair of die will be high
or low. A high roll is defined as a sum of 8-12 inclusive. A low roll is
defined as a sum of 2-6. If the sum is 7, the player loses their bet automatically.
If the player guesses correctly, then win double what they risked. If they are
incorrect, they lose the bet. In the blitz game mode, the player must place a bet
and then guess the exact sum of the pair of die. If they are correct they win 5x
the amount they bet. If they are off by 1 either higher or lower, the win 3x the
amount they bet. If their guess is completely wrong, they lose the amount they bet.
In both game modes the game is over when the player has a coin balance below 1.

Program Assumptions: In order to play the game, the user must enter a valid bet and 
guess depending on the game mode. Additionally, it is assumed that the player knows
a dice has 6 faces and each face has a number from 1-6. Fluency of English is another 
assumption because all the prompts are written in English.

Features of the Program: The blitz mode was added as a high-risk, high-reward version
of the dice game. While the odds are not favorable to guess correctly. When the guess
is correct, the player is rewarded with a much higher return on bet.

Restrictions: Once a game mode has been selected, the player must play the game until
they run out of money before being prompted to switch to a different mode.

Known Errors: N/A