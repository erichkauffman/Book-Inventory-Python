import sqlite3

from data.Item import Item

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
								  locationPurchased, amountPaid, sellPrice, siteListed, 
								  removalAction, dateRemoved)
							VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
					itemInsert)
		conn.commit()
		return cursor.lastrowid
