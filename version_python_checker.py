# Write a Python program to find out what version of Python you are using. 
# The current version i got so far is  python 3.13.2

#First Solution
# def check_version(version):
#     versions = ['3.13.2', '3.12.0', '3.11.0', '3.10.0', '3.9.0', '3.8.0', '3.7.0', '3.6.0', '3.5.0', '3.4.0', '3.3.0', '3.2.0', '3.1.0', '3.0.0']
#     if version in versions:
#         print(f'You are using python version {version}')
#     else:
#         print('You are not using a valid version of python')


# check_version('3.13.2')


#Second Solution

import sys
def check_version(version):
    current_version = sys.version_info
    if current_version >= version:
        print(f'Python version is compatible with {current_version}')
    else:
        print(f'Python version is not compatible with your device {current_version}. Required version is {version}')

required_version = (3, 13, 2) # you can change the version of your preferred python
check_version(required_version)

