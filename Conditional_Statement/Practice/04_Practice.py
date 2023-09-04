word1 = input("Enter a first word: ")
word2 = input("Enter a second word: ")

if word1[::-1] == word2:
    print("YES")
else:
    print("NO")    