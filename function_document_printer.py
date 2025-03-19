# Function Documentation Printer

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.


def abs():
    print(abs.__doc__) #To print the documentation of a Python built-in function, you can use the help() function or the __doc__

# Other Methods:
# print(help(abs))