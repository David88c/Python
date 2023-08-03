#Write a program that calculates the length of a line segment (i.e., the distance between two points) given
#two values x1 and x2 (can be either integers or float numbers)
#import math
#dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
#num1 = float(input("Enter the first number:"))
#num2 = float(input("Enter the second number:"))


#print("Distance between two point is:"(num1, num2)(dist))

import math

def distance_between_points(x1, x2):
    return abs(x2 - x1)

# Input the x-coordinates of the two points
x1 = float(input("Enter the x-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))

# Calculate and print the distance
distance = distance_between_points(x1, x2)
print(f"The length of the line segment is: {distance}")