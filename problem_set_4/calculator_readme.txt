Author: Abhinav Balsburamanian
Class: ICS3U0 - C
Date: March 18th, 2021
Version: 2.4
Unit: 4
Question: 1
Programming Language: Python 3.9.1

Programming Description: This program serves as a calculator that 
can perform addition, subtraction, divison, multiplication, 
exponent, modulus operations and calculate the root(s) of a quadratic. 
The program will prompt the user to provide certain inputs to select
the preferred operation and then to provide the operands.

Program Assumptions: In order to perform a calculation, the user must
input the correct operation type by entering the corresponding integer
as shown in the main menu. Furthermore, the program assumes that the 
user has used a physical calculator before and knows how to perform 
calculations on them. For the quadratic root operation, the program
assumes the user understands how to identify 'a', 'b' and 'c' in the
equation by themselves. Fluency of English is another assumption because 
all the prompts are written in English.

Features of the Program: In addition to the features a regular calculator
includes, this program can also calculate the root(s) of a quadratic
equation using the standard quadratic formula. The program also features a 
very user-friendly experience with a startup and goodbye screen of an ASCII 
text art calculator.

Restrictions: Once an operation has been selected, the user must provide all
the operands and allow the program to output the result before being asked
to quit the program. 

Known Errors: The program cannot perform calculations that are not possible by
a real life calculator, specifically operations for which the result is undefined
(i.e. dividing a number by zero, n mod 0 where n is any integer). The program will
have an OverFlow error if the user tries to multiply very large numbers by each other.
However for common use cases, the program will be able to print the entire result
without experiencing an error.