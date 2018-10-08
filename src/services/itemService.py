from repositories.itemRepository import ItemRepository
from data.Item import Item

class ItemService:
	def __init__(self, itemRepository: ItemRepository):
		self.itemRepo = itemRepository

	def getListOfItems(self):
		return self.itemRepo.getListOfItems()

	def createItem(self, item: Item):
		return self.itemRepo.createNewItem(item)

	def deleteItem(self, itemId: int):
		self.itemRepo.deleteItem(itemId)

	def updateRemoveAction(self, itemId: int, status: bool):
		self.itemRepo.updateRemoveAction(itemId, status)
