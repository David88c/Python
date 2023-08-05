#Write a program that calculates the length of a line segment (i.e., the distance between two points) given
#two values x1 and x2 (can be either integers or float numbers)

import math
num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

dist = math.dist([num1], [num2])
print(dist)
