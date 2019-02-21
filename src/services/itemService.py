from repositories.itemRepository import ItemRepository
from repositories.siteRepository import SiteRepository
from data.Item import Item

class ItemService:
	def __init__(self, itemRepository: ItemRepository, siteRepository: SiteRepository):
		self.itemRepo = itemRepository
		self.siteRepo = siteRepository

	def getListOfItems(self):
		return self.itemRepo.getListOfItems()

	def createItem(self, item: Item):
		return self.itemRepo.createNewItem(item)

	def getSellableItems(self):
		return self.itemRepo.getSellableItems()

	def deleteItem(self, itemId: int):
		self.itemRepo.deleteItem(itemId)

	def updateRemoveAction(self, itemId: int, status: bool):
		self.itemRepo.updateRemoveAction(itemId, status)
