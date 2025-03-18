get_data = input("Enter the file name, don't forget the extension, pleases: ")

file_extension = get_data.split(".")[-1]

print(file_extension)


# The line of code file_extension = get_data.split(".")[-1] performs the following actions:

#     Splitting the String: The split(".") method is called on the string get_data. This method splits the string into a list of substrings based on the delimiter provided, which in this case is a period ("."). For example, if get_data is "example.txt", the result of get_data.split(".") would be ["example", "txt"].

#     Accessing the Last Element: The [-1] index accesses the last element of the list produced by the split() method. In Python, negative indexing allows you to access elements from the end of a list. So, [-1] refers to the last item in the list. Continuing with the previous example, ["example", "txt"][-1] would return "txt".

#     Assigning to file_extension: The result of the above operation (the last element of the split list) is then assigned to the variable file_extension. In the example, file_extension would be set to "txt".
