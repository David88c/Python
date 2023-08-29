#The program receives a list of integers as input. Your task is to output the last three elements of this
#list using slicing. The list should have at least five elements.

num = list(map(int, input("Enter numbers: ").split()))

print(num[-3:])