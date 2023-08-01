#Write a program that finds the best grade of a student among the results of solving five exams.
#The grades for all five exams are entered in a single line and can only be integers from 1 to 100.


a, b, c, d, e = map(int, input("Please enter 5 grades: ").split())
print(max(a, b, c, d, e))


# print(max([15, 58, 100, 89, 100]))