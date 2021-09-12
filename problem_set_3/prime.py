# Abhinav Balasubramanian
# March 11, 2021
# ICS3UO-C
# This program will print all the prime numbers from 2-100

print("These are all the prime numbers from 2-100.") # displays welcome message

#PROCESSING AND OUTPUT

for num in range(2,101): # loops through all the numbers from 2-100
    is_prime = True # initializes is_prime variable
    for divisor in range(2,(num//2 + 1)): # loops through all possible divisors; the "//" means it is performing integer division and the result will always be a whole number
        if num % divisor == 0: # checks if the number is divisible by the divisor
            is_prime = False # since the number is divisible, it is not considered a prime number
            break # exits the loop
        else:
            continue # goes back to the top of the loop
    if is_prime == True: # checks if the number is prime
        print(str(num) + " is prime") # prints prime number
    else:
        continue # goes back to the top of the loop

        

    