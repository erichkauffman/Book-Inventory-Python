from lib.convert import itemAssembler, bookAssembler, siteAssembler

def item_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return itemAssembler(dictionary)

def book_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return bookAssembler(dictionary)

def site_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return siteAssembler(dictionary)

def mini_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return dictionary
