import pytest
from unittest import mock

from app import app
from data.Book import Book

@mock.patch('routes.books.BookService.getListOfBooks')
def test_book_route_when_a_get_request_is_used(mock_getListOfBooks):
    testApp = app.test_client()
    mock_getListOfBooks.return_value = [Book(
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

    result = testApp.get('/books/')
    assert result.status_code == 200
    assert result.is_json == True

    jsonResult = result.get_json()
    assert len(jsonResult) == 1
    jsonResult = jsonResult[0]
    assert jsonResult['id'] == 5
    assert jsonResult['title'] == "Cracking the Coding Interview"
    assert jsonResult['author'] == "Gayle Laakmann McDowell"
    assert jsonResult['isbn'] == "9870984782857"
    assert jsonResult['edition'] == 6
    assert jsonResult['printing'] == 15
    assert jsonResult['cover'] == 0
    assert jsonResult['yearPrinted'] == 2015
    assert jsonResult['description'] == "A very good book for practicing algorithms"
    assert jsonResult['condition'] == 2
    assert jsonResult['datePurchased'] == "2016-12-6"
    assert jsonResult['locationPurchased'] == "Online"
    assert jsonResult['amountPaid'] == 2000
    assert jsonResult['sellPrice'] == 1200
    assert jsonResult['siteListed'] == 1
    assert jsonResult['removalAction'] == None
    assert jsonResult['dateRemoved'] == None

@mock.patch('routes.books.BookService.createBook')
def test_book_route_when_a_post_request_is_used(mock_createBook):
    testApp = app.test_client()

    result = testApp.post('/books/',
                          json={'amountPaid': 2000,
                                'author': 'Gayle Laakmann McDowell',
                                'condition': 2,
                                'cover': 0,
                                'datePurchased': '2016-12-6',
                                'dateRemoved': None,
                                'description': 'A very good book for practicing algorithms',
                                'edition': 6,
                                'id': 5,
                                'isbn': '9870984782857',
                                'locationPurchased': 'Online',
                                'printing': 15,
                                'removalAction': None,
                                'sellPrice': 1200,
                                'siteListed': 1,
                                'title': 'Cracking the Coding Interview',
                                'yearPrinted': 2015
                                })
    assert result.status_code == 200
    