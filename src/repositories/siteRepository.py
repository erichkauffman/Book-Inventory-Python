import sqlite3

from data.Site import Site

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def setSite(self, itemId: int, site: Site):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('INSERT INTO site(itemId, site, siteId) VALUES (?,?,?)', (itemId, site.site, site.siteId))
		conn.commit()

	def getSitesById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('SELECT site FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		siteTuples = cursor.fetchall()
		sites = []
		for siteTuple in siteTuples:
			sites.append(siteTuple[0])
		return sites

	def editSite(self, itemId: int, sites: Site):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('DELETE FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		for site in sites:
			self.setSite(itemId, site)
