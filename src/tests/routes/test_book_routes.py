from unittest import mock

from app import app
from data.Book import Book
from data.Item import Item

@mock.patch('routes.books.BookService.getListOfBooks')
def test_book_route_when_a_get_request_is_made(mock_getListOfBooks):
	testApp = app.test_client()
	mock_getListOfBooks.return_value = [Book(
		Item(
			5,
			"Cracking the Coding Interview",
			"9870984782857",
			2015,
			"A very good book for practicing algorithms",
			2,
			"2016-12-6",
			"Online",
			2000,
			1200,
			1,
			"FBA",
			None,
			None
		),
		"Gayle Laakmann McDowell",
		6,
		15,
		0
	)]

	result = testApp.get('/books/')
	assert result.status_code == 200
	assert result.is_json is True

	jsonResult = result.get_json()
	assert len(jsonResult) == 1
	jsonResult = jsonResult[0]
	assert jsonResult['item']['itemId'] == 5
	assert jsonResult['item']['title'] == "Cracking the Coding Interview"
	assert jsonResult['item']['upc'] == "9870984782857"
	assert jsonResult['item']['year'] == 2015
	assert jsonResult['item']['description'] == "A very good book for practicing algorithms"
	assert jsonResult['item']['condition'] == 2
	assert jsonResult['item']['datePurchased'] == "2016-12-6"
	assert jsonResult['item']['locationPurchased'] == "Online"
	assert jsonResult['item']['amountPaid'] == 2000
	assert jsonResult['item']['sellPrice'] == 1200
	assert jsonResult['item']['siteListed'] == 1
	assert jsonResult['item']['shelfLocation'] == "FBA"
	assert jsonResult['item']['removalAction'] is None
	assert jsonResult['item']['dateRemoved'] is None
	assert jsonResult['author'] == "Gayle Laakmann McDowell"
	assert jsonResult['edition'] == 6
	assert jsonResult['printing'] == 15
	assert jsonResult['cover'] == 0

@mock.patch('routes.books.BookService.createBook')
@mock.patch('lib.convert.bookAssembler')
def test_book_route_when_a_post_request_is_made(mock_createBook, mock_bookAssembler):
	testApp = app.test_client()

	result = testApp.post('/books/',
						  json={
							  'item': {
						  		'amountPaid': 2000,
								'condition': 2,
								'datePurchased': '2016-12-6',
								'dateRemoved': None,
								'description': 'A very good book for practicing algorithms',
								'itemId': 5,
								'upc': '9870984782857',
								'locationPurchased': 'Online',
								'removalAction': None,
								'sellPrice': 1200,
								'siteListed': 1,
								'shelfLocation': 'FBA',
								'title': 'Cracking the Coding Interview',
								'year': 2015
							  },
							  'author': 'Gayle Laakmann McDowell',
							  'cover': 0,
							  'edition': 6,
							  'printing': 15
							})
	assert result.status_code == 200
