import sqlite3
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

def item_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return itemAssembler(dictionary)

def book_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	item = itemAssembler(dictionary)
	return Book(
		item,
		dictionary['author'],
		dictionary['edition'],
		dictionary['printing'],
		dictionary['cover']
	)