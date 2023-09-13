upper_number = int(input("Enter a number: "))

while upper_number < 30:
    print("The number is lower than 30: ")
    upper_number = int(input("Try again: "))
    
for i in range(1, upper_number + 1):
    if i % 4 == 0 and i % 7 == 0:
            print("Israel Forever") 
    elif i % 4 == 0:
           print("Israel")
    elif i % 5 == 0:
           print("Forever")
    else:
        print(i)           
                              