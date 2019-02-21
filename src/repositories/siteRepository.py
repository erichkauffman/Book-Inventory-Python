import sqlite3

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def setSite(self, itemId: int, site: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('INSERT INTO siteListed(itemId, site) VALUES (?,?)', (itemId, site))
		conn.commit()

	def getSitesById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('SELECT site FROM siteListed WHERE itemId = ?', (itemId,))
		conn.commit()
		siteTuples = cursor.fetchall()
		sites = []
		for siteTuple in siteTuples:
			sites.append(siteTuple[0])
		return sites
