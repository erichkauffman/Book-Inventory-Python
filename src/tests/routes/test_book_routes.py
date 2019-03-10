from unittest import mock

from app import app

@mock.patch('routes.books.BookService.createBook')
@mock.patch('lib.convert.bookAssembler')
def test_book_route_when_a_post_request_is_made(mock_createBook, mock_bookAssembler):
	testApp = app.test_client()

	result = testApp.post('/books/',
						  json={
							  'item': {
						  		'amountPaid': 2000,
								'condition': 2,
								'consignment': 0,
								'datePurchased': '2016-12-6',
								'dateRemoved': None,
								'description': 'A very good book for practicing algorithms',
								'itemId': 5,
								'upc': '9870984782857',
								'locationPurchased': 'Online',
								'removalAction': None,
								'sellPrice': 1200,
								'siteListed': [1],
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
