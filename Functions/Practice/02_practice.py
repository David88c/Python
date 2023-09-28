name_list = ["Yoav", "Ron", "Aviva", "Ronen" , "Dan", "Galit"]
len_list = list(map(lambda x: len(x), name_list))

print(len_list)

filtered_names = list(filter(lambda x: len(x) > 4, name_list))
print(filtered_names)
    
