import sqlite3

connection = sqlite3.connect("books.db")

connection.execute("""
INSERT INTO books (title, author)
VALUES ('The Hobbit', 'J.R.R. Tolkien')
""")


connection.commit()

print("insert complete")

connection.close()