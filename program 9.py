"""
Program 9

Write a program that accepts sequence of lines as input and make each line capitalized
The program should print all capitalized lines as output

"""
#initializing an empty list to store capitalized lines
cap_lines = []

#console input
while True:
    input_lines = input()
     
    #converting each character of input line to uppercase
    if input_lines:
        cap_lines.append(input_lines.upper())
    else:
        break;

#printing capitalized lines
for s in cap_lines:
    print(s)