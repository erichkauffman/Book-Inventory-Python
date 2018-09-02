from repositories.itemRepository import ItemRepository
from data.Item import Item

class ItemService:
	def __init__(self, itemRepository: ItemRepository):
		self.itemRepo = itemRepository

	def getListOfItems(self):
		return self.itemRepo.getListOfItems()
	
	def createItem(self, item: Item):
		return self.itemRepo.createNewItem(item)