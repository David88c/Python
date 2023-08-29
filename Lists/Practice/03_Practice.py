#The program receives a list of integers as input. Your task is to output
#sorted list and reverse sorted list

num= list(map(int, input("Enter numbers: : ").split()))
print(f" Sorted list: {sorted(num)}")
print(f" Reverse Sorted list: {sorted(num, reverse = True)}")

