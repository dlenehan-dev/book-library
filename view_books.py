import sqlite3

print("Opening database...")

with sqlite3.connect("books.db") as connection:
    print("Connected.")

    cursor = connection.execute("SELECT * FROM books")

    for row in cursor:
        print(row)

print("Connection closed.")