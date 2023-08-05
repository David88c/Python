#Find the result of the expression: |a| + |b|
#The values of variables 'a' and 'b' are provided as input on separate lines and can
#only be of integer type.

a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))

# Calculate the result
result = abs(a) + abs(b)

# Display the result
print("The result of |a| + |b| is:", result)