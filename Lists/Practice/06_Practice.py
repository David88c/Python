numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

numbers2 = numbers.pop(-1) + numbers.pop(0) + numbers.pop(7) + numbers.pop(11)

print(numbers)
print(f"Sum of removed = {numbers2}")
