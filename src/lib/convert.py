from data.Item import Item
from data.Book import Book
from data.Site import Site

def itemAssembler(dictionary):
	item = Item(
		dictionary['itemId'],
		dictionary['title'],
		dictionary['upc'],
		dictionary['year'],
		dictionary['description'],
		dictionary['condition'],
		dictionary['datePurchased'],
		dictionary['locationPurchased'],
		dictionary['consignment'],
		dictionary['amountPaid'],
		dictionary['sellPrice'],
		list(map(siteAssembler, dictionary['siteListed'])),
		dictionary['shelfLocation'],
		dictionary['removalAction'],
		dictionary['siteSold'],
		dictionary['dateRemoved']
	)
	return item

def bookFromDatabaseAssembler(dictionary):
	item = itemAssembler(dictionary)
	return Book(
		item,
		dictionary['author'],
		dictionary['edition'],
		dictionary['printing'],
		dictionary['cover']
	)

def bookFromRequestAssembler(dictionary):
	item = itemAssembler(dictionary['item'])
	return Book(
		item,
		dictionary['author'],
		dictionary['edition'],
		dictionary['printing'],
		dictionary['cover']
	)

def siteAssembler(dictionary):
	return Site(dictionary['site'], dictionary['siteId'])
