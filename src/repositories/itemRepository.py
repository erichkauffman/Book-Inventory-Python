import sqlite3

from data.Item import Item

from lib.database import item_factory
from lib.database import mini_factory
from lib.exceptions import DatabaseIndexError

class ItemRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def allItems(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = item_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT *, group_concat(site.site), group_concat(site.siteId)
						  FROM item
						  LEFT JOIN site ON item.itemId = site.itemId
						  GROUP BY item.itemId''')
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
			item.consignment,
			item.amountPaid,
			item.sellPrice,
			item.shelfLocation,
			item.removalAction,
			item.siteSold,
			item.dateRemoved
		)
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('''INSERT INTO
							item (title, upc, year, description, condition, datePurchased,
								  locationPurchased, consignment, amountPaid, sellPrice, 
								  shelfLocation, removalAction, siteSold, dateRemoved)
							VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
						itemInsert)
		conn.commit()
		return cursor.lastrowid

	def editItem(self, item: Item):
		itemInsert = (
			item.title,
			item.upc,
			item.year,
			item.description,
			item.condition,
			item.datePurchased,
			item.locationPurchased,
			item.consignment,
			item.amountPaid,
			item.sellPrice,
			item.shelfLocation,
			item.itemId
		)
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('''UPDATE item SET title = ?, upc = ?, year = ?, description = ?,
						  condition = ?, datePurchased = ?, locationPurchased = ?,
						  consignment = ?, amountPaid = ?, sellPrice = ?, shelfLocation = ?
						  WHERE itemId = ?''', itemInsert)
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {item.itemId} does not exist in database')

	def getSellableItems(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = mini_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT item.itemId, title, upc, group_concat(site.siteId)
						  FROM item
						  LEFT JOIN site ON item.itemId = site.itemId
						  WHERE dateRemoved IS NULL
						  GROUP BY item.itemId''')
		return cursor.fetchall()

	def getItemById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = item_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT *, group_concat(site.site), group_concat(site.siteId)
						  FROM item
						  LEFT JOIN site ON item.itemId = site.itemId
						  WHERE item.itemId = ?
						  GROUP BY item.itemId''', (itemId,))
		count = cursor.rowcount
		item = cursor.fetchone()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {item.itemId} does not exist in database')
		return item

	def updateRemoveAction(self, itemId: int, status: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute("UPDATE item SET removalAction = ?, dateRemoved = date('now') WHERE itemId = ?", (status, itemId))
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')

	def updateItemAsSold(self, itemId: int, site: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute("UPDATE item SET removalAction = 0, siteSold = ?, dateRemoved = date('now') WHERE itemId = ?", (site, itemId))
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')
