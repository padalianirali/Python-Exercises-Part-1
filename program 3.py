"""
Program:3

Write a program to generate a dictionary that contains (i, i*i) for the given number between 1 and n (both included) 
The program should print a dictionary as final output

"""

#console input
num = int(input("Enter any number"))

#initializing an empty dictionary to store squares for the given range
square_dict = {}

#calculating and assigning squares as values to the given range of numbers as keys
for i in range(1,num+1):
    square_dict[i]=i*i

#printing output dictionary
print(square_dict)