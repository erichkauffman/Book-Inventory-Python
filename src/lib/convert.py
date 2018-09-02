from data.Item import Item
from data.Book import Book

def itemAssembler(dictionary):
	return Item(
		dictionary['itemId'],
		dictionary['title'],
		dictionary['upc'],
		dictionary['year'],
		dictionary['description'],
		dictionary['condition'],
		dictionary['datePurchased'],
		dictionary['locationPurchased'],
		dictionary['amountPaid'],
		dictionary['sellPrice'],
		dictionary['siteListed'],
		dictionary['removalAction'],
		dictionary['dateRemoved']
	)

def bookAssembler(dictionary):
	if 'item' in dictionary:
		item = itemAssembler(dictionary['item'])
	else:
		item = itemAssembler(dictionary)
	import sys
	return Book(
		item,
		dictionary['author'],
		dictionary['edition'],
		dictionary['printing'],
		dictionary['cover']
	)