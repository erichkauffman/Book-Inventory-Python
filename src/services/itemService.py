from repositories.itemRepository import ItemRepository
from services.siteService import SiteService
from data.Item import Item
from lib.itemCsv import itemCsv

class ItemService:
	def __init__(self, itemRepository: ItemRepository, siteService: SiteService):
		self.itemRepo = itemRepository
		self.siteService = siteService

	def createItem(self, item: Item):
		itemId = self.itemRepo.createNewItem(item)
		self.siteService.setSites(itemId, item.siteListed)
		return itemId

	def editItem(self, item: Item):
		self.itemRepo.editItem(item)
		self.siteService.editSite(item.itemId, item.siteListed)

	def getSellableItems(self):
		return self.itemRepo.getSellableItems()

	def getItemById(self, itemId: int):
		item = self.itemRepo.getItemById(itemId)
		item.siteListed = self.siteService.getSitesById(itemId)
		return item

	def updateRemoveAction(self, itemId: int, status: int):
		self.itemRepo.updateRemoveAction(itemId, status)

	def sellItem(self, itemId: int, site: int):
		self.itemRepo.updateItemAsSold(itemId, site)

	def buildCsv(self):
		csv = ''
		itemList = self.itemRepo.allItems()
		for index, item in enumerate(itemList):
			itemList[index].siteListed = self.siteService.getSitesById(item.itemId)
		for item in itemList:
			csv += itemCsv(item) + '\n'
		return csv
