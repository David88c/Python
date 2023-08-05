#Write a program that takes three integers as input in a single line separated by spaces and then outputs
#them sequentially with commas.

a, b, c = map(int, input().split())
print(a, b, c, sep=',')
