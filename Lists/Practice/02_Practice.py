#The program receives a list of integers as input. Your task is to output
#True if the value 777 is a part
#of the given list, otherwise output False

# Function to check if 777 is in the list
def has_777(input_list):
    return 777 in input_list

# Input list of integers
input_list = [1, 2, 3, 4, 5, 777, 8, 9]

# Check if 777 is in the list
result = has_777(input_list)

# Output the result
print(result)