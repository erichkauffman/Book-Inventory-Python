import sqlite3

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def setSite(self, itemId: int, site: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('INSERT INTO siteListed(itemId, site) VALUES (?,?)', (itemId, site))
		conn.commit()
