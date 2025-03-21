# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is". 

def add_is(string):
    if string.startswith('Is'):
        return string
    else:
        return 'Is ' + string
    
print(add_is('hello'))
print(add_is('Is world'))

# The startswith() method in Python is a string method that returns True if the string starts with the specified value, otherwise it returns False.
# string.startswith(value, start, end)
#value: The value to check if the string starts with.
# start: Optional. The starting position of the string to check. Default is 0.
# end: Optional. The ending position of the string to check. Default is the end of the string.