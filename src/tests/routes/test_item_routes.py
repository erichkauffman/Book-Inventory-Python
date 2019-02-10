from unittest import mock

from app import app
from data.Item import Item

@mock.patch('routes.items.ItemService.getListOfItems')
def test_item_route_when_a_get_request_is_made(mock_getListOfItems):
	testApp = app.test_client()
	mock_getListOfItems.return_value = [Item(
		5,
        "Cracking the Coding Interview",
        "9870984782857",
        2015,
        "A very good book for practicing algorithms",
        2,
        "2016-12-6",
        "Online",
		0,
        2000,
        1200,
		1,
		"FBA",
		None,
		None
	)]

	result = testApp.get('/items/')
	assert result.status_code == 200
	assert result.is_json is True

	jsonResult = result.get_json()
	assert len(jsonResult) == 1
	jsonResult = jsonResult[0]
	assert jsonResult['itemId'] == 5
	assert jsonResult['title'] == "Cracking the Coding Interview"
	assert jsonResult['upc'] == "9870984782857"
	assert jsonResult['year'] == 2015
	assert jsonResult['description'] == "A very good book for practicing algorithms"
	assert jsonResult['condition'] == 2
	assert jsonResult['datePurchased'] == "2016-12-6"
	assert jsonResult['locationPurchased'] == "Online"
	assert jsonResult['amountPaid'] == 2000
	assert jsonResult['sellPrice'] == 1200
	assert jsonResult['shelfLocation'] == "FBA"
	assert jsonResult['siteListed'] == 1
	assert jsonResult['removalAction'] is None
	assert jsonResult['dateRemoved'] is None

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
            'siteListed': 1,
            'title': 'Cracking the Coding Interview',
            'year': 2015
		})
	assert result.status_code == 200
