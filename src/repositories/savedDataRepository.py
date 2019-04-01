import sqlite3

class SavedDataRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getData(self, dataType: str):
		getSql = {
			'phrases': 'SELECT * FROM phrase',
			'locations': 'SELECT * FROM location'
		}
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute(getSql[dataType])
		conn.commit()
		dataTuples = cursor.fetchall()
		dataList = []
		for dataTuple in dataTuples:
			dataList.append(dataTuple[0])
		return dataList

	def setData(self, dataType: str, data: str):
		setSql = {
			'phrases': 'INSERT INTO phrase(phrase) VALUES (?)',
			'locations': 'INSERT INTO location(location) VALUES (?)'
		}
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute(setSql[dataType], (data,))
		conn.commit()

	def deleteData(self, dataType: str, data: str):
		deleteSql = {
			'phrases': 'DELETE FROM phrase WHERE phrase = ?',
			'locations': 'DELETE FROM location WHERE location = ?'
		}
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute(deleteSql[dataType], (data,))
		conn.commit()
