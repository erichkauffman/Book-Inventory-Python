import sqlite3

from data.Item import Item

from lib.database import item_factory
from lib.exceptions import DatabaseIndexError

class ItemRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getListOfItems(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = item_factory
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM item ORDER BY title')
		return cursor.fetchall()

	def createNewItem(self, item: Item):
		itemInsert = (
			item.title,
			item.upc,
			item.year,
			item.description,
			item.condition,
			item.datePurchased,
			item.locationPurchased,
			item.amountPaid,
			item.sellPrice,
			item.siteListed,
			item.removalAction,
			item.dateRemoved
		)
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('''INSERT INTO
							item (title, upc, year, description, condition, datePurchased,
								  locationPurchased, consignment, amountPaid, sellPrice, siteListed, 
								  shelfLocation, removalAction, dateRemoved)
							VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
					itemInsert)
		conn.commit()
		return cursor.lastrowid

	def getSellableItems(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = item_factory
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM item WHERE dateRemoved IS NULL ORDER BY title')
		return cursor.fetchall()

	def deleteItem(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('DELETE FROM item WHERE itemId = ?', (itemId,))
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')

	def updateRemoveAction(self, itemId: int, status: bool):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute("UPDATE item SET removalAction = ? WHERE itemId = ?", (status, itemId))
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')
