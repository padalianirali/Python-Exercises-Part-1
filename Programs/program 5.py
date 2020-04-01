"""
Program 5

Define a class which has at least two methods. Also please initialize an object to test these class methods
1) to get a string from console input
2) to print the string in upper case

"""

#defining a class
class GetSetString(object):
    
    def __init__(self):
        self.str = ''
        
    def get_str(self):
        self.str = input("Enter any string:")
    
    def set_str(self):
        print (self.str.upper())

#initializing an object 
str_obj = GetSetString()

#calling class methods
str_obj.get_str()
str_obj.set_str()
    
