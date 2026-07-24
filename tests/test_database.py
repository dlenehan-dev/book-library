import pytest
from database import get_book_by_id, update_book 
from ui import format_book 
from validation import is_valid_book 

@pytest.fixture
def hobbit_book():
    return (1,"The Hobbit","J.R.R. Tolkien")

@pytest.fixture
def multiple_books():
    return [(2,"To Kill a Mockingbird","Harper Lee"),
            (3,"Great Expectations","Charles Dickens")
    ]



@pytest.mark.parametrize(
        "title, author, expected",
        [   ("Dune","Frank Herbert",True),
             ("","Frank Herbert",False),
             ("Dune","",False)
        ]
)

def test_is_valid_book(title, author, expected):
    assert is_valid_book(title, author) is expected

def test_format_book(hobbit_book):
    
    result = format_book(hobbit_book)

    assert result == (
        "ID: 1 | "
        "Title: The Hobbit | "
        "Author: J.R.R. Tolkien"
    )

def test_format_multiple_books(multiple_books):

    for book in multiple_books: 
        result = format_book(book)
        book_id,title,author = book 
        assert title in result 
        assert author in result 
        assert str(book_id) in result 



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
    