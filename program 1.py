"""
Program:1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)
The program should print the numbers obtained in a comma-separated sequence on a single line

"""
#initializing an empty list to store all numbers which are divisible by 7 and not a multiple of 5
num_list = []

#checking for all numbers from 2000 to 3200 which are divisible by 7 and not a multiple of 5
for num in range(2000,3200):
    if num%7 == 0 and num%5 !=0:
        num_list.append(str(num))
        
#printing output list and sequence
print("\n")
print(num_list)
print("\n")
print (','.join(num_list))