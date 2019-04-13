from lib.convert import itemAssembler, bookAssembler, siteAssembler

def generic_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return dictionary

def item_factory(cursor, row):
	dictionary = generic_factory(cursor, row)
	return itemAssembler(dictionary)

def book_factory(cursor, row):
	dictionary = generic_factory(cursor, row)
	return bookAssembler(dictionary)

def site_factory(cursor, row):
	dictionary = generic_factory(cursor, row)
	return siteAssembler(dictionary)

def mini_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return dictionary
