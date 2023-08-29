#The program receives a
#list of integers as input . Your task is to find the average of the entered list of numbers.

num= list(map(int, input("Enter two numbers: : ").split()))
avg = sum(num)/len(num)
print(avg)
