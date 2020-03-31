"""
Program 10

Write a program that accepts a sequence of whitespace separated words as input, removes duplicate words and sorts alphabetically.
The program should print all unique words in sorted order.

"""
#console input
input_sent = input("Enter any sentence:")

#seperating input words by space to generate a list
split_sent = input_sent.split(' ')

#removing duplicates using set
nodup_sent = set(split_sent)

#creating a list from the set
list_sent = list(nodup_sent)

#sorting input words
sort_sent = sorted(list_sent)

#joining listed words to generate a space seperated sequence
final_sent = " ".join(sort_sent)

#printing the sorted, no duplicate sequence
print(final_sent)