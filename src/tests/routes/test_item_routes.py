from unittest import mock
from ast import literal_eval

from app import app
from initialize import socketio
from data.Item import Item

restTestApp = app.test_client()
socketTestApp = socketio.test_client(app, flask_test_client=restTestApp)

@mock.patch('routes.items.itemService.createItem')
def test_item_route_when_a_post_request_is_made(mock_createItem):
	testItemId = 1
	testTitle = 'Cracking the Coding Interview'
	testUpc = '9870984782857'
	mock_createItem.return_value = testItemId

	restResult = restTestApp.post('/items/',
		json={
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
			'siteListed': 1,
			'siteSold': None,
			'title': testTitle,
			'year': 2015
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

@mock.patch('routes.items.itemService.editItem')
def test_item_routes_when_a_put_request_is_made(mock_editItem):
	testItemId = 1
	testTitle = 'Cracking the Coding Interview'
	testUpc = '9870984782857'

	restResult = restTestApp.put('/items/',
		json={
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
			'siteListed': 1,
			'siteSold': None,
			'title': testTitle,
			'year': 2015
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

@mock.patch('routes.items.itemService.getSellableItems')
def test_item_route_when_get_request_is_made_to_sellable(mock_getSellableItems):
	mock_getSellableItems.return_value = [{
		"itemId": 1,
		"title": "Cracking the Coding Interview",
		"upc": "9870984782857"
	}]

	restResult = restTestApp.get('/items/sellable/')

	assert restResult.status_code == 200
	assert restResult.is_json is True

	jsonResult = restResult.get_json()

	assert len(jsonResult) == 1
	jsonResult = jsonResult[0]
	assert jsonResult['itemId'] == 1
	assert jsonResult['title'] == "Cracking the Coding Interview"
	assert jsonResult['upc'] == "9870984782857"

@mock.patch('routes.items.itemService.updateRemoveAction')
def test_item_route_when_a_put_request_is_made_to_remove_action(mock_updateRemoveAction):
	restResult = restTestApp.put('/items/1/removeAction/1/')
	socketResult = socketTestApp.get_received()

	assert restResult.status_code == 200
	assert len(socketResult[0]['args']) == 1
	assert socketResult[0]['args'][0] == 1

@mock.patch('routes.items.itemService.sellItem')
def test_item_route_when_a_put_request_is_made_to_sell_item(mock_sellItem):
	restResult = restTestApp.put('/items/1/sell/', json={'site':0})
	socketResult = socketTestApp.get_received()

	assert restResult.status_code == 200
	assert len(socketResult[0]['args']) == 1
	assert socketResult[0]['args'][0] == 1
