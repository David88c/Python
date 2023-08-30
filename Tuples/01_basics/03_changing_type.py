#tuple definition

my_tuple = ('David',5,35,False,'age',56)
print(type(my_tuple))
print(my_tuple)

#converting tuple to list

my_list = list(my_tuple)
print(type(my_list))
print(my_list)

#adding element by append()

my_list[2]=105
my_list.append(True)
print(my_list)

#convert modified list to tuple again
my_tuple=tuple(my_list)
print(type(my_list))
print(my_list)

#converting a tuple to be a list by using * unpacking method

unpacked_list=[* my_tuple]
print(f"{unpacked_list= }")