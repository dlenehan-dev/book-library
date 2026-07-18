from database import get_book_by_id, update_book 
from ui import format_book 
from validation import is_valid_book 


def test_format_book():
    book = (1, "The Hobbit", "J.R.R. Tolkien")

    result = format_book(book)

    assert result == (
        "ID: 1 | "
        "Title: The Hobbit | "
        "Author: J.R.R. Tolkien"
    )


def test_valid_book():
    assert is_valid_book("Dune", "Frank Herbert") is True


def test_empty_title():
    assert is_valid_book("", "Frank Herbert") is False


def test_empty_author():
    assert is_valid_book("Dune", "") is False


def test_get_book_by_id_not_found():
    result = get_book_by_id(999)

    assert result is None

def test_update_book():
    assert update_book(1,"The Hobbit Returns", "J.K. Tolkien") is True 
    updated_book = get_book_by_id(1)
    assert updated_book is not None
    _, title, author = updated_book
    assert title == "The Hobbit Returns"
    assert author == "J.K. Tolkien"

    assert update_book(999,"a","b") is False
    