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
        connection.commit()

def list_books():
    with sqlite3.connect("books.db") as connection:
        cursor = connection.execute(
            """
            SELECT * FROM books
            """
        )

        return cursor.fetchall()
    
def format_book(book):
    book_id = book[0]
    title = book[1]
    author = book[2]

    return f"ID: {book_id} | Title: {title} | Author: {author}"


def is_valid_book(title, author):
    return title.strip() != "" and author.strip() != ""


def get_book_by_id(book_id):
    with sqlite3.connect("books.db") as connection:
        cursor = connection.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )

        return cursor.fetchone()
    
    
def delete_book(book_id):
    with sqlite3.connect("books.db") as connection:
        cursor = connection.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )
        connection.commit()

        return cursor.rowcount

