import sqlite3
import sys

from lib.database import item_factory

class ItemRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getListOfItems(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = item_factory
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM item ORDER BY title')
		return cursor.fetchall()