# Write a Python program that returns a string that is n (non-negative integer) copies of a given string. 

def string_converter(string, n):
    result = string * n
    return result

print(string_converter('hello ', 10))

#This is my solution, but also you can do it with a for loop

# def larger_string(text, n):
    
#     result = ""
#     for i in range(n):
#         result = result + text
#     return result

# print(larger_string('Lobo ', 5))
# print(larger_string('.py', 3))