# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2. 

def string_prefix(str, n):
    if len(str) <= 2:
        return str * n
    else:
        return str[:2] * n
    
value = string_prefix('it', 10)
print(value)

#Here is my slution and a detail that can help to improve your code skills 
    # s[:2] is a slicing operation that extracts the first two characters of the string s.
    # For example, if s is 'hello', then s[:2] would be 'he'.
