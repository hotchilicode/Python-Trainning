# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum. 

def triple_sum(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
        return sum
    else:
        return sum
    
try:
    num1 = int(input('Please type the first integer: '))
    num2 = int(input('Please type the second integer: '))
    num3 = int(input('Please type the third integer: '))
    testeo = triple_sum(num1, num2, num3)
    print(testeo)
except:
    print('Please type a valid integer!')

#Here's my result