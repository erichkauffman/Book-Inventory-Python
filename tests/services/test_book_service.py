import pytest
from unittest import mock

from data.Book import Book
from services.bookService import BookService
from repositories.bookRepository import BookRepository

def test_getting_a_list_of_books():
    mockRepo = mock.create_autospec(BookRepository)
    mockRepo.getListOfBooks.return_value = [Book(
        5,
        "Cracking the Coding Interview",
        "Gayle Laakmann McDowell",
        "9870984782857",
        6,
        15,
        0,
        2015,
        "A very good book for practicing algorithms",
        2,
        "2016-12-6",
        "Online",
        2000,
        1200,
        1,
        None,
        None
    )]
    service = BookService(mockRepo)

    returnedListOfBooks = service.getListOfBooks()
    assert len(returnedListOfBooks) == 1
    
    returnedBook = returnedListOfBooks[0]
    assert returnedBook.id == 5
    assert returnedBook.title == "Cracking the Coding Interview"
    assert returnedBook.author == "Gayle Laakmann McDowell"
    assert returnedBook.isbn == "9870984782857"
    assert returnedBook.edition == 6
    assert returnedBook.printing == 15
    assert returnedBook.cover == 0
    assert returnedBook.yearPrinted == 2015
    assert returnedBook.description == "A very good book for practicing algorithms"
    assert returnedBook.condition == 2
    assert returnedBook.datePurchased == "2016-12-6"
    assert returnedBook.locationPurchased == "Online"
    assert returnedBook.amountPaid == 2000
    assert returnedBook.sellPrice == 1200
    assert returnedBook.siteListed == 1
    assert returnedBook.removalAction == None
    assert returnedBook.dateRemoved == None