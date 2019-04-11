from repositories.itemRepository import ItemRepository
from repositories.siteRepository import SiteRepository
from data.Item import Item
from lib.csv import itemCsv

class ItemService:
	def __init__(self, itemRepository: ItemRepository, siteRepository: SiteRepository):
		self.itemRepo = itemRepository
		self.siteRepo = siteRepository

	def createItem(self, item: Item):
		itemId = self.itemRepo.createNewItem(item)
		for site in item.siteListed:
			self.siteRepo.setSite(itemId, site)
		return itemId

	def editItem(self, item: Item):
		self.itemRepo.editItem(item)
		self.siteRepo.editSite(item.itemId, item.siteListed)

	def getSellableItems(self):
		return self.itemRepo.getSellableItems()

	def getItemById(self, itemId: int):
		item = self.itemRepo.getItemById(itemId)
		item.siteListed = self.siteRepo.getSitesById(itemId)
		return item

	def updateRemoveAction(self, itemId: int, status: int):
		self.itemRepo.updateRemoveAction(itemId, status)

	def sellItem(self, itemId: int, site: int):
		self.itemRepo.updateItemAsSold(itemId, site)

	def buildCsv(self):
		csv = ''
		itemList = self.itemRepo.allItems()
		for item in itemList:
			csv += itemCsv(item) + '\n'
		return csv
