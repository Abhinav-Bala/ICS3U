# Abhinav Balasubramanian
# Feb. 18, 2021
# ICS3UO-C
# This program will output the date and month that easter will fall on for a given year

print('This program will caclulate the date of easter.') # displays welcome message

# INPUT
year = int(input('Enter the year: ')) # variable for inputted user's year casted as an int

# PROCESSING
# Calculates the date and month using the formula from the document
z = year % 19
y = year / 100
x = year % 100
w = y / 4
v = y % 4
u = (8*y + 13) / 25
t = (19*z + y - w - u + 15) % 30
s = (z + 11*t) / 319
r = x / 4
q = x % 4
p = (2*v + 2*r - t - s - q + 32) % 7
month = (t - s + p + 90) / 28
day = (t - s + p + month + 19) % 32


# Casting month and day as int to get rid of decimal places
month = int(month)
day = int(day)

# OUTPUT
print('The date of easter for the year of ' + str(year) + ' is: ' + str(month) + ', ' + str(day)) # prints text and the casted string month and day
