values = input('Input some comma-separated numbers: ')
list = values.split(",")
tuple = tuple(list)
print('List:', list)
print('Tuple:', tuple)

#First we need to split the string into a list
#Then we need to convert the list into a tuple