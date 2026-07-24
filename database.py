import sqlite3

DATABASE_NAME = "books.db"

def get_connection(database_name=DATABASE_NAME) -> sqlite3.Connection:
    return sqlite3.connect(database_name)


def initialise_database(database_name=DATABASE_NAME):
    with get_connection(database_name) as connection:
        connection.execute(
            """
        create table if not exists books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT
        );
        """
        )
        connection.commit()
        

def add_book(title, author):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO books (title, author)
            VALUES (?, ?)
            """,
            (title, author)
        )
        connection.commit()

def list_books():
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT * FROM books
            """
        )

        return cursor.fetchall()
    

def get_book_by_id(book_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )

        return cursor.fetchone()
    
    
def delete_book(book_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )
        connection.commit()

        return cursor.rowcount
    

def update_book(book_id: int, title: str, author: str) -> bool:
    with get_connection() as connection:
        cursor = connection.execute(
           """
           UPDATE books
             SET title = ?,
                 author = ?
           WHERE id = ?
           """,
          (title, author, book_id)
)

        connection.commit()

        return cursor.rowcount > 0 

