tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1] = [222 ,33]
list1 = tuple(list1)
print(list1)

