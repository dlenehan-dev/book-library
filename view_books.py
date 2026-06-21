from database import list_books

books = list_books()

print(f"Found {len(books)} books")

for book in books:
    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]}")