# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


exam_st_date = (11, 12, 2014)

formatted_data = '/'.join(map(str, exam_st_date))
print(formatted_data)


    #1. map(str, exam_st_date): This converts each element of the tuple exam_st_date into a string.
    #2. '/'.join(...): This joins the string representations of the elements with a slash (/) as the separator.
    #3. print(formatted_date): This prints the formatted date string.
