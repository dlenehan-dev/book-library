from database import format_book


from database import format_book

def test_format_book():
    book = (1, "The Hobbit", "J.R.R. Tolkien")

    result = format_book(book)

    assert result == (
        "ID: 1 | Title: The Hobbit | Author: J.R.R. Tolkien"
    )