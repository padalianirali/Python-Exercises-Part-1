"""
Program 8

Write a program that accepts a comma separated sequence of words as input sorting them alphabetically.
The program should print a comma seperated sorted sequence of words as output

"""
#console input
words = input("Enter any 5 words:")

#seperating input words by comma to generate a list
words_list = words.split(',')

#sorting the words alphabetically
words_list.sort()

#joining listed words to generate a comma seperated sequence
sorted_words = ','.join(words_list)

#printing the sorted sequence
print(sorted_words)