from database import add_book, list_books, format_book

def get_menu_choice():
    while True:
        choice = input("> ")

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid input. Please enter 1, 2 or 3.")


def main():
    while True:
        print("\n=== Book Library ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = get_menu_choice()

        if choice not in ["1", "2", "3"]:
           print("DEBUG: Please enter 1, 2 or 3.")
           input("press enter to continue...")
           continue

        if choice == "1":
           title = input("Title: ")
           author = input("Author: ")
           add_book(title, author)
           print("Book added successfully.")    
           
        elif choice == "2":
            books = list_books()
            for book in books:
                print(format_book(book))

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()