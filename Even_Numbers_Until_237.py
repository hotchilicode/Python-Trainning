# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Sample numbers list :

# def even_numbers(list):
#     numbers_result = []
#     for i in list: 
#         if i %2 == 0:
#             return numbers_result.list[i].append(i)
#         elif i > 237:
#             break
#     else:
#         return 'It Is ODD'
    
# array = [8,52,84,5,7,651,14,6,747,54,66,41]
# array2 = [8, 2, 6, 46, 0]
# print(even_numbers(array2))


def even_numbers(numbers):
    numbers_result = []
    for i in numbers: 
        if i % 2 == 0:
            numbers_result.append(i)  # Append the even number to the result list
        elif i > 237:
            break  # Exit the loop if a number greater than 237 is encountered
    if numbers_result:  # Check if there are any even numbers found
        return numbers_result
    else:
        return 'IT IS ODD'  # If no even numbers found

array2 = [8, 2, 6, 46, 0, 9]
print(even_numbers(array2))

#Here's my logic