Author: Abhinav Balsburamanian
Class: ICS3U0 - C
Date: March 18th, 2021
Version: 2.7
Unit: 4
Question: 2
Programming Language: Python 3.9.1

Programming Description: This program serves as a class statistics
calculator than can determine the average grade, how many students
are passing or failing, and display the grade distribution. The
program will prompt the user for the class size and the grade for
each individual student. Then it will output the various statistics.

Program Assumptions: In order to display the statistics, the user must
input a valid class size (an integer greater than zero). Furthermore, 
the program assumes that the user is using a grading system where 0% is
the lowest mark acheivable and 100% is the highest mark. Fluency of English 
is another assumption because all the prompts are written in English.

Features of the Program: To create a better user experience for the program,
the grade distribution is shown graphically using '=' to represent 1 student.
Additionally, the number value of the distribution is shown to make it clear
for the user. 

Restrictions: Once a class size has been given, the user must provide all
grades for each student and allow all statistics to be displayed before being 
able to quit the program. As mentioned before, the program will only accept
grades between 0%-100%. 

Known Errors: If any of the statistics are equal to 1, the program will still print the
plural form of words. For example, the program will print: '1 students are failing'.
This is only a grammatical error in the print statements and does not impact the 
calculations or statistics in any way.