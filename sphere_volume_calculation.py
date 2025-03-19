# Write a Python program to get the volume of a sphere with radius six.

import math

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

result = sphere_volume(6)
print(result)

#Here's other way to do this without a function

# radius = 6
# volume = (4 / 3) * math.pi * (radius ** 3)
# print(volume)