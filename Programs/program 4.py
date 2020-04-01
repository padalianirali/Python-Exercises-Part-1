"""
Program:4

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
The program should print a list and a tuple for the given sequence of numbers as final output

"""
#console input
seq = input("Enter your numbers:")

#seperating input numbers by comma to generate a list
seq_list = seq.split(',')

#using tuple method to directly convert list created above into a tuple
seq_tuple = tuple(seq_list)

#printing output list and tuple
print(seq_list)
print(seq_tuple)
