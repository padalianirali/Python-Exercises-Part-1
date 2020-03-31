"""
Program 7

Write a program which takes 2 digits (X and Y) as input and generate a 2-dimensional array
The element value in the i-th row and j-th column of the array should be i*j.
The program should print the 2-dimensional array as output with X number of rows and Y number of columns

"""
#console input
input_str = input("Enter any 2 numbers:")

#seperating input numbers by comma to generate a list
split_string = input_str.split(',')
print(split_string)

#converting the list of string format to int format
dimensions=[int(x) for x in split_string]
print(dimensions)

#assigning number of rows and columns
rowNum=dimensions[0]
colNum=dimensions[1]

#generating 2-D array
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
        
#printing 2-D array
print (multilist)