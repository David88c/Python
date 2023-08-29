#The program receives a list of integers as input. Your task is to transform it in a way that the
#elements are arranged in reverse order.

num = list(map(int, input("Enter numbers: ").split()))
num.reverse()
print(num)

