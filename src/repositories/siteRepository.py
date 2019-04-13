import sqlite3

from data.Site import Site
from lib.database import site_factory

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getSitesById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = site_factory
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		return cursor.fetchall()

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
		conn.executemany('INSERT INTO site(itemId, site, siteId) VALUES (?,?,?)', (itemId, site.site, site.siteId))
		conn.commit()

	def editSite(self, itemId: int, sites: Site):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('DELETE FROM site WHERE itemId = ?', (itemId,))
		conn.commit()
		for site in sites:
			self.setSite(itemId, site)
