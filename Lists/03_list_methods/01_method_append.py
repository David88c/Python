cars = ["BMW", "AUDI"]

print(cars)

cars.append("Tesla")

print(cars)

cars.append(["VW", "TOYOTA"])

print(cars)

cars.append(8)

print(len(cars))

print(cars)

cars.append(9)
cars.append(10)

#cars.append(10, 11) TypeError: list.append() takes exactly one argument (2 given)
print(cars)