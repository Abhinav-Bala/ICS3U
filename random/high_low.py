# Abhinav Balasubramanian
# March 23, 2021
# ICS3UO-C
# This program will simulate a higher/lower game where
# the players guesses whether the number will be higher
# or lower

import random

def generateNum():
    number = random.randint(0, 100)
    return number
    
while True:
    currentNum = generateNum()

