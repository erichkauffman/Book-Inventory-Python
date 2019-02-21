from lib.convert import itemAssembler
from lib.convert import bookAssembler

def test_item_assembler():
	itemDict = {
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
	}
	itemObject = itemAssembler(itemDict)
	assert itemObject.itemId == 5
	assert itemObject.title == "Cracking the Coding Interview"
	assert itemObject.upc == "9870984782857"
	assert itemObject.year == 2015
	assert itemObject.description == "A very good book for practicing algorithms"
	assert itemObject.condition == 2
	assert itemObject.datePurchased == "2016-12-6"
	assert itemObject.locationPurchased == "Online"
	assert itemObject.consignment == 0
	assert itemObject.amountPaid == 2000
	assert itemObject.sellPrice == 1200
	assert itemObject.shelfLocation == 'FBA'
	assert itemObject.siteListed == [1]
	assert itemObject.removalAction is None
	assert itemObject.dateRemoved is None


def test_book_assembler_when_item_is_a_subdictionary():
	bookDict = {
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
			'shelfLocation': 'FBA',
			'siteListed': [1],
			'title': 'Cracking the Coding Interview',
			'year': 2015
		},
		'author': 'Gayle Laakmann McDowell',
		'cover': 0,
		'edition': 6,
		'printing': 15
	}
	bookObject = bookAssembler(bookDict)
	assert bookObject.item.itemId == 5
	assert bookObject.item.title == "Cracking the Coding Interview"
	assert bookObject.author == "Gayle Laakmann McDowell"
	assert bookObject.item.upc == "9870984782857"
	assert bookObject.edition == 6
	assert bookObject.printing == 15
	assert bookObject.cover == 0
	assert bookObject.item.year == 2015
	assert bookObject.item.description == "A very good book for practicing algorithms"
	assert bookObject.item.condition == 2
	assert bookObject.item.datePurchased == "2016-12-6"
	assert bookObject.item.locationPurchased == "Online"
	assert bookObject.item.consignment == 0
	assert bookObject.item.amountPaid == 2000
	assert bookObject.item.sellPrice == 1200
	assert bookObject.item.shelfLocation == 'FBA'
	assert bookObject.item.siteListed == [1]
	assert bookObject.item.removalAction is None
	assert bookObject.item.dateRemoved is None

def test_book_assembler_when_item_is_not_a_subdictionary():
	bookDict = {
		'amountPaid': 2000,
		'condition': 2,
		'datePurchased': '2016-12-6',
		'dateRemoved': None,
		'description': 'A very good book for practicing algorithms',
		'itemId': 5,
		'upc': '9870984782857',
		'locationPurchased': 'Online',
		'consignment': 0,
		'removalAction': None,
		'sellPrice': 1200,
		'shelfLocation': 'FBA',
		'siteListed': [1],
		'title': 'Cracking the Coding Interview',
		'year': 2015,
		'author': 'Gayle Laakmann McDowell',
		'cover': 0,
		'edition': 6,
		'printing': 15
	}

	bookObject = bookAssembler(bookDict)
	assert bookObject.item.itemId == 5
	assert bookObject.item.title == "Cracking the Coding Interview"
	assert bookObject.author == "Gayle Laakmann McDowell"
	assert bookObject.item.upc == "9870984782857"
	assert bookObject.edition == 6
	assert bookObject.printing == 15
	assert bookObject.cover == 0
	assert bookObject.item.year == 2015
	assert bookObject.item.description == "A very good book for practicing algorithms"
	assert bookObject.item.condition == 2
	assert bookObject.item.datePurchased == "2016-12-6"
	assert bookObject.item.locationPurchased == "Online"
	assert bookObject.item.consignment == 0
	assert bookObject.item.amountPaid == 2000
	assert bookObject.item.sellPrice == 1200
	assert bookObject.item.shelfLocation == 'FBA'
	assert bookObject.item.siteListed == [1]
	assert bookObject.item.removalAction is None
	assert bookObject.item.dateRemoved is None
