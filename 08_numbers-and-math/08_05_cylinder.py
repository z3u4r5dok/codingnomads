# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

# import a fucntion
import math

# Define variables
radius = 3.14
height = 5

# Calculate volume
volume = math.pi * (radius ** 2) * height

# Calculate surface area
surface_area = (2 * math.pi * radius ** 2) + (2 * math.pi * radius * height)

# Print results
print("Volume of the cylinder:", volume)
print("Surface area of the cylinder", surface_area)


