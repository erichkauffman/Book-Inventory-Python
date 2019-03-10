from unittest import mock

from app import app
from data.Item import Item

@mock.patch('routes.items.ItemService.createItem')
@mock.patch('lib.convert.itemAssembler')
def test_item_route_when_a_post_request_is_made(mock_createItem, mock_itemAssembler):
	testApp = app.test_client()

	result = testApp.post('/items/',
		json={
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
			'shelfLocation': 'FBA',
            'siteListed': [1],
            'title': 'Cracking the Coding Interview',
            'year': 2015
		})
	assert result.status_code == 200
