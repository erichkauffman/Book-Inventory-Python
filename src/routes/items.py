from flask import Blueprint, request
import jsonpickle

from services.itemService import ItemService
from repositories.itemRepository import ItemRepository
from lib.convert import itemAssembler
from config import database

ItemService = ItemService(ItemRepository(database))

itemRoutes = Blueprint("items", __name__)

@itemRoutes.route('/', methods=['GET', 'POST'])
def items():
	if request.method == 'GET':
		itemList = ItemService.getListOfItems()
		return jsonpickle.encode(itemList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		postedItem = itemAssembler(jsonreq)
		ItemService.createItem(postedItem)
		res = jsonpickle.encode({"success": "true"})
		return res
