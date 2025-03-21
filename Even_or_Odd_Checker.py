# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 


def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


number = int(input("Enter a number: "))
even_or_odd(number)

#Here's one way to do so