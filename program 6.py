"""
Program 6

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
The program should print the numbers obtained in decimal format.

"""
#importing math library for square root function
import math

#static values for C and H variables in the formula
C = 50
H = 30

#console input
nums = input("Enter your numbers")

#seperating input numbers by comma to generate a list
nums_list = [n for n in nums.split(',')]

#initializing an empty list to store sqaure roots of the given numbers
result_list = []

#calculating as per given formula
#float - to convert input from string to number as math works with numbers only
#int - to convert result from float to int as required by the program definition
#str - to convert result from int to str as join works with strings only
for n in nums_list:
    result_list.append(str(int(math.sqrt((2*C*float(n))/H))))

print(','.join(result_list))
    
