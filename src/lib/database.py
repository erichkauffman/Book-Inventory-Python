import sqlite3
from data.Item import Item

def item_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
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