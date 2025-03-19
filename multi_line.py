# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example


print("""a string that you "don't" have to escape
This
is a ....... multi-line"
heredoc string --------> example""")
#Here's an example of a multi-line heredoc string
#Also you can pass it in a variable like this.

a = """a string that you "don't" have to escape
This
is a ....... multi-line"
heredoc string --------> example"""

print(a)

#Directely or using a variable you can print it