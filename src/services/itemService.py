from repositories.itemRepository import ItemRepository
from repositories.siteRepository import SiteRepository
from data.Item import Item

class ItemService:
	def __init__(self, itemRepository: ItemRepository, siteRepository: SiteRepository):
		self.itemRepo = itemRepository
		self.siteRepo = siteRepository

	def getListOfItems(self):
		items = self.itemRepo.getListOfItems()
		for index, item in enumerate(items):
			items[index].siteListed = self.siteRepo.getSitesById(item.itemId)
		return items

	def createItem(self, item: Item):
		itemId = self.itemRepo.createNewItem(item)
		for site in item.siteListed:
			self.siteRepo.setSite(itemId, site)
		return itemId

	def getSellableItems(self):
		items = self.itemRepo.getSellableItems()
		for index, item in enumerate(items):
			items[index].siteListed = self.siteRepo.getSitesById(item.itemId)
		return items

	def deleteItem(self, itemId: int):
		self.itemRepo.deleteItem(itemId)

	def updateRemoveAction(self, itemId: int, status: bool):
		self.itemRepo.updateRemoveAction(itemId, status)
