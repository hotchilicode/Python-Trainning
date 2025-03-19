# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference. 

def difference_from_17(number):
    if number > 17:
        return (number - 17) * 2
    else:
        return 17 - number

number = int(input("Enter a number: "))
result = difference_from_17(number)
print(result)

#Here's one way to do so with a function