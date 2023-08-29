users = []
print(f"users = {users}")
users = ['Kevin', 'Bob', 'Alice']
print(f"users = {users}")
del users[1]
print(f"users = {users}")
users.reverse()
print(f"rev_users = {users}")
users.reverse()
users.insert(1, "Melody")
print(f"users = {users}")
users.extend(["Andy", "Wanda", "Jim"])
print(f"users = {users}")
print(f"Center users: {users[2:4]}")