from database import add_book, list_books, get_book_by_id, delete_book
from validation import is_valid_book
from ui import format_book

def get_menu_choice():
    while True:
        choice = input("> ")

        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("Invalid input. Please enter 1, 2, 3, 4 or 5.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter a number")


def display_book(book):
    if book is None:
        print("Book not found")
    else:
        print(format_book(book))



def add_book_flow():
    title = input("Title: ")
    author = input("Author: ")

    if not is_valid_book(title, author):
        print("Title and author cannot be empty.")
        return

    add_book(title, author)
    print("Book added successfully.")







def main():
    while True:
        print("\n=== Book Library ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Find book by ID")
        print("4. Delete Book by ID")
        print("5. Exit")

        choice = get_menu_choice()

        if choice == "1":
           add_book_flow()
           
        elif choice == "2":
            books = list_books()
            for book in books:
                print(format_book(book))

        elif choice == "3":
            
            book_id = get_int_input("Enter book ID: ")

            book = get_book_by_id(book_id)

            display_book(book)


        elif choice == "4":
            
            book_id = get_int_input("Enter book ID to delete: ")

            result = delete_book(book_id)

            if result == 0:
                print("Book not found")
            else:
                print("Book deleted successfully")
            

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()