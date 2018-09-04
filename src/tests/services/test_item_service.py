from unittest import mock

from data.Item import Item
from services.itemService import ItemService
from repositories.itemRepository import ItemRepository

def test_getting_a_list_of_items():
	mockRepo = mock.create_autospec(ItemRepository)
	mockRepo.getListOfItems.return_value = [Item(
		5,
        "Cracking the Coding Interview",
        "9870984782857",
        2015,
        "A very good book for practicing algorithms",
        2,
        "2016-12-6",
        "Online",
        2000,
       	1200,
        1,
        None,
        None
	)]
	service = ItemService(mockRepo)
	returnedListOfItems = service.getListOfItems()
	assert len(returnedListOfItems) == 1

	returnedItem = returnedListOfItems[0]
	assert returnedItem.itemId == 5
	assert returnedItem.title == "Cracking the Coding Interview"
	assert returnedItem.upc == "9870984782857"
	assert returnedItem.year == 2015
	assert returnedItem.description == "A very good book for practicing algorithms"
	assert returnedItem.condition == 2
	assert returnedItem.datePurchased == "2016-12-6"
	assert returnedItem.locationPurchased == "Online"
	assert returnedItem.amountPaid == 2000
	assert returnedItem.sellPrice == 1200
	assert returnedItem.siteListed == 1
	assert returnedItem.removalAction is None
	assert returnedItem.dateRemoved is None