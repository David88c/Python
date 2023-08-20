def getlastchar(s):
	return s[len(s):1]

str1 = str("This is a test message!")
#str1 = input("Enter a message: ")
print(f"Lowercase:  {str1.lower()}")
print(f"Uppercase: {str1.upper()}")
print(f"Capitalized: {str1.capitalize()}")
print(f"Title Case: {str1.title()}")
print(f'Words: {sorted(str1.split(), key=getlastchar)}')
print(f"Alphabetic First Word: {str1.split(' ',1)[0]}")
print(f"Alphabetic Last Word: {str1.split(' ',-1)[-1]}")