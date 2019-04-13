from lib.convert import itemAssembler, bookAssembler, siteAssembler

def generic_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return dictionary

def item_factory(cursor, row):
	dictionary = {}
	sites = []
	siteIds = []
	for index, columnName in enumerate(cursor.description):
		if columnName[0] == 'group_concat(site.site)':
			sites = row[index].split(',')
		elif columnName[0] == 'group_concat(site.siteId)':
			siteIds = row[index].split(',')
		else:
			dictionary[columnName[0]] = row[index]
	dictionary['siteListed'] = []
	for site, siteId in zip(sites, siteIds):
		dictionary['siteListed'].append({'site':int(site), 'siteId':siteId})
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
		if columnName[0] == 'group_concat(site.siteId)':
			dictionary['siteId'] = row[index].split(',')
		else:
			dictionary[columnName[0]] = row[index]
	return dictionary
