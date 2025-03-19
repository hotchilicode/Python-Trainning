# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

import datetime

# date1 = datetime.date(2014, 7, 2)
# date2 = datetime.date(2014, 7, 11)

# delta = date2 - date1

# print(delta.days)

def days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)

print(days_between_dates(date1, date2))

#You can do this using the datetime module just with either two variables or two tuples 