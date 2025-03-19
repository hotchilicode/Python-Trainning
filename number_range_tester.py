# Write a Python program to test whether a number is within 100 of 1000 or 2000. 

def range_tester(n):
    if n <= 100:
        print('Within 100')
    elif n > 100 and n <= 1000:
        print('Within 1000')
    else:
        print('Within 2000')
        return
    
try: 
    testeo = int(input('Please Type a number to check: '))
    range_tester(testeo)
except ValueError:
    print('please enter a valid integer.')


    #------------------------------------------------------------#

#     def range_tester(n):
#     if n <= 100:
#         return 'Within 100'  # Return a string instead of printing
#     elif n > 100 and n <= 1000:
#         return 'Within 1000'  # Return a string instead of printing
#     else:
#         return 'Within 2000'  # Return a string instead of printing

# # Get user input
# try:
#     testeo = int(input('Please type a number to check: '))  # Use input() and convert to int
#     result = range_tester(testeo)  # Call the function and store the result
#     print(result)  # Print the result
# except ValueError:
#     print("Please enter a valid integer.")


#     The function now uses return statements to return strings instead of printing them directly.
#     The result of the function call is stored in the variable result, which is then printed.

# When to Use Return:

#     Use return when you want to send a value back to the caller of the function, allowing you to use that value later in your code.
#     If your function's purpose is solely to perform an action (like printing), you may not need a return statement.


# n summary, whether to use return depends on how you want to use the output of your function. If you want to use the output later in your code, use return. If you just want to display the output immediately, you can stick with print.


