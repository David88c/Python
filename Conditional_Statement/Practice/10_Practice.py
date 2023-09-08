pass1 = input("Enter your password: ")
pass2 = input("Confirm your password: ")

if pass1 != pass2:
    print("Difference")
elif len(pass1) and len(pass2) < 7:
    print("Short")
elif len(pass1) and len(pass2) > 7:
    print("OK")
    