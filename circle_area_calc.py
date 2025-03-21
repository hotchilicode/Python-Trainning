def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    diameter = radius * 2
    area = 3.14 * (radius ** 2)
    return area

result = circle_area()
print(result)


#Other way to do this more exactly with the library:

# Import the 'pi' constant from the 'math' module to calculate the area of a circle
#from math import pi

# Prompt the user to input the radius of the circle
#r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
#area = pi * r ** 2

# Display the result, including the radius and calculated area
#print("The area of the circle with radius " + str(r) + " is: " + str(area))