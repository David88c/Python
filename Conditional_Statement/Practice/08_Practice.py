num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 == num3:
    result = 3

elif num1 == num2 or num1 == num3 or num2 == num3:
    result = 2

else:
    result = 0

print(result)