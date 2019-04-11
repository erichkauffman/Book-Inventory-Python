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
		None,
		dictionary['shelfLocation'],
		dictionary['removalAction'],
		dictionary['siteSold'],
		dictionary['dateRemoved']
	)
	if 'siteListed' in dictionary:
		item.siteListed = dictionary['siteListed']
	return item

def bookAssembler(dictionary):
	if 'item' in dictionary:
		item = itemAssembler(dictionary['item'])
	else:
		item = itemAssembler(dictionary)
	return Book(
		item,
		dictionary['author'],
		dictionary['edition'],
		dictionary['printing'],
		dictionary['cover']
	)

def siteAssembler(dictionary):
	return Site(dictionary['site'], dictionary['siteId'])
