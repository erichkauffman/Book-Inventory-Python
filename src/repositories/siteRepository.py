import sqlite3

from data.Site import Site

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getSiteValuesById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('SELECT site FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		siteTuples = cursor.fetchall()
		sites = []
		for siteTuple in siteTuples:
			sites.append(siteTuple[0])
		return sites

	def setSites(self, itemId: int, sites: Site):
		sitesInsert = []
		for site in sites:
			sitesInsert.append((itemId, site.site, site.siteId))
		conn = sqlite3.connect(self.dbConnection)
		conn.executemany('INSERT INTO site(itemId, site, siteId) VALUES (?,?,?)', sitesInsert)
		conn.commit()

	def editSites(self, itemId: int, sites: Site):
		conn = sqlite3.connect(self.dbConnection)
		conn.execute('DELETE FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		self.setSites(itemId, sites)
