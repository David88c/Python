#The program reads a natural number n, and then outputs a double inequality involving that number and its neighboring numbers.

number = int(input())
print(number-1, number, number+1, sep='<')
