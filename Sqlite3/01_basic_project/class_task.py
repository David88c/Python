import sqlite3

# Create a connection to the DB
connection_manager = sqlite3.connect("users.db")

# Create a cursor object
my_cursor = connection_manager.cursor()

# Create a new table
my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (title TEXT, first_name TEXT, last_name TEXT, age INTEGER, address TEXT)")

query_string = """
INSERT INTO users VALUES (?,?,?,?,?)
"""

title = str(input("Title: "))
first_name = str(input("First Name: "))
last_name = str(input("Last Name: "))
age = int(input("Age: "))
address = str(input("Address: "))

tuple_of_data = (title, first_name, last_name, age, address)

my_cursor.execute(query_string, tuple_of_data)

connection_manager.commit()

for row in my_cursor.execute("SELECT * FROM users"):
    print(row)

connection_manager.close()