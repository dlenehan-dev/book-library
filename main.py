from database import add_book, list_books

print("Book Library")
print("1. Add Book")
print("2. View Books")
print("3. Exit")

choice = input("Choose an option: ")
print(type(choice))

if choice == "1":
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    add_book(title, author)

    print("Book added.")

elif choice == "2":
    books = list_books()

    for book in books:
        print(book)

elif choice == "3":
    print("Goodbye")
else:
    print("Invalid option")