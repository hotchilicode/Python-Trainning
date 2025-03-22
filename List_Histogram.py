def histo_checker(value):
    
    for i in value:
        char = '#' * i
        print(f'{value}: {char}')

data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(histo_checker(data))

#Here's my result, I ranged those in a semi triangule  