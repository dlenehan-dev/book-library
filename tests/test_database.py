from database import format_book, is_valid_book, get_book_by_id


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