#Write a program that takes two integers as input in separate lines and prints their sum on the screen.

 print(int(input("Enter number 1: ")) + int(input("Enter number 2: ")))

 list_of_nums = [2, 4, 6]
 print(sum(list_of_nums))

 num_1, num_2 = map(int, input("Enter 2 numbers: ").split())
 print(num_1 + num_2)

print(sum(list(map(int, input("put the score here: ").split()))))