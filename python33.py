def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the factorial function
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")
