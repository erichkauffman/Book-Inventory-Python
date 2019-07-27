from lib.convert import itemAssembler, bookFromDatabaseAssembler

def factory_helper(cursor, row):
	dictionary = {}
	sites = []
	siteIds = []
	for index, columnName in enumerate(cursor.description):
		if columnName[0] == 'group_concat(site.site)' and row[index] is not None:
			sites = row[index].split(',')
		elif columnName[0] == 'group_concat(site.siteId)' and row[index] is not None:
			siteIds = row[index].split(',')
		else:
			dictionary[columnName[0]] = row[index]
	dictionary['siteListed'] = []
	for site, siteId in zip(sites, siteIds):
		dictionary['siteListed'].append({'site':int(site), 'siteId':siteId})
	return dictionary

def item_factory(cursor, row):
	dictionary = factory_helper(cursor, row)
	return itemAssembler(dictionary)

def book_factory(cursor, row):
	dictionary = factory_helper(cursor, row)
	return bookFromDatabaseAssembler(dictionary)

def mini_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		if columnName[0] == 'group_concat(site.siteId)' and row[index] is not None:
			dictionary['siteId'] = row[index].split(',')
		else:
			dictionary[columnName[0]] = row[index]
	return dictionary
