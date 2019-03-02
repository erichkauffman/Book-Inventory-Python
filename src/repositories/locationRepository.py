import sqlite3

class LocationRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getLocations(self):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM location')
		conn.commit()
		return list(cursor.fetchall())

	def setLocation(self, location: str):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('INSERT INTO location(location) VALUES (?)', (location,))
		conn.commit()
