import sqlite3


def add_book(title, author):
    with sqlite3.connect("books.db") as connection:
        connection.execute(
            """
            INSERT INTO books (title, author)
            VALUES (?, ?)
            """,
            (title, author)
        )


def list_books():
    with sqlite3.connect("books.db") as connection:
        cursor = connection.execute(
            """
            SELECT * FROM books
            """
        )

        return cursor.fetchall()
    
def format_book(book):
    return (
        f"ID: {book[0]} | "
        f"Title: {book[1]} | "
        f"Author: {book[2]}"

    )