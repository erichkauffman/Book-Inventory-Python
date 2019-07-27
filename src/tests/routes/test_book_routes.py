from unittest import mock
from ast import literal_eval

from app import app
from initialize import socketio
from data.Book import Book

restTestApp = app.test_client()
socketTestApp = socketio.test_client(app, flask_test_client=restTestApp)

@mock.patch('routes.books.bookService.createBook')
def test_book_route_when_a_post_request_is_made(mock_createBook):
	testItemId = 1
	testTitle = 'Cracking the Coding Interview'
	testUpc = '9870984782857'
	testAuthor = 'Gayle Laakmann McDowell'
	mock_createBook.return_value = testItemId

	restResult = restTestApp.post('/books/',
		json={
			'item': {
				'amountPaid': 2000,
				'condition': 2,
				'consignment': False,
				'datePurchased': '2016-12-6',
				'dateRemoved': None,
				'description': 'A very good book for practicing algorithms',
				'itemId': None,
				'upc': testUpc,
				'locationPurchased': 'Online',
				'removalAction': None,
				'sellPrice': 1200,
				'shelfLocation': 'A1',
				'siteListed': [{'site':1, 'siteId':1234567890}],
				'siteSold': None,
				'title': testTitle,
				'year': 2015
			},
			'author': testAuthor,
			'cover': 1,
			'edition': 1,
			'printing': 1
		}
	)
	socketResult = socketTestApp.get_received()

	assert restResult.status_code == 200

	jsonResult = socketResult[0]['args']
	assert len(jsonResult) == 1
	jsonResult = literal_eval(jsonResult[0])
	assert jsonResult['itemId'] == testItemId
	assert jsonResult['title'] == testTitle
	assert jsonResult['upc'] == testUpc
	assert jsonResult['author'] == testAuthor

@mock.patch('routes.books.bookService.editBook')
def test_book_routes_when_a_put_request_is_made(mock_bookItem):
	testItemId = 1
	testTitle = 'Cracking the Coding Interview'
	testUpc = '9870984782857'
	testAuthor = 'Gayle Laakmann McDowell'

	restResult = restTestApp.put('/books/',
		json={
			'item': {
				'amountPaid': 2000,
				'condition': 2,
				'consignment': False,
				'datePurchased': '2016-12-6',
				'dateRemoved': None,
				'description': 'A very good book for practicing algorithms',
				'itemId': testItemId,
				'upc': testUpc,
				'locationPurchased': 'Online',
				'removalAction': None,
				'sellPrice': 1200,
				'shelfLocation': 'A1',
				'siteListed': [{'site':1, 'siteId':1234567890}],
				'siteSold': None,
				'title': testTitle,
				'year': 2015
			},
			'author': testAuthor,
			'cover': 1,
			'edition': 1,
			'printing': 1,
		}
	)
	socketResult = socketTestApp.get_received()

	assert restResult.status_code == 200

	jsonResult = socketResult[0]['args']
	assert len(jsonResult) == 1
	jsonResult = literal_eval(jsonResult[0])
	assert jsonResult['itemId'] == testItemId
	assert jsonResult['title'] == testTitle
	assert jsonResult['upc'] == testUpc
	assert jsonResult['author'] == testAuthor

@mock.patch('routes.books.bookService.getSellableBooks')
def test_book_route_when_get_request_is_made_to_sellable(mock_getSellableBooks):
	mock_getSellableBooks.return_value = [{
		"itemId": 1,
		"title": "Cracking the Coding Interview",
		"upc": "9870984782857",
		"author": "Gayle Laakmann McDowell"
	}]

	restResult = restTestApp.get('/books/sellable/')

	assert restResult.status_code == 200
	assert restResult.is_json is True

	jsonResult = restResult.get_json()

	assert len(jsonResult) == 1
	jsonResult = jsonResult[0]
	assert jsonResult['itemId'] == 1
	assert jsonResult['title'] == "Cracking the Coding Interview"
	assert jsonResult['upc'] == "9870984782857"
	assert jsonResult['author'] == "Gayle Laakmann McDowell"
