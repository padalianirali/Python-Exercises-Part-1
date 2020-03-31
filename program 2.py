"""
Program:2

Write a program which can compute the factorial of a given number
The program should print factorial of the given number as final output

"""

#console input 
num = int(input("Enter any number:"))

#function defined to calculate factorial of number
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

#printing factorial of the number entered
print(fact(num))