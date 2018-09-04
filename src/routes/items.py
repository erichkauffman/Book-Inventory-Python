from flask import Blueprint, request

from services.itemService import ItemService
from repositories.itemRepository import ItemRepository
from lib.convert import itemAssembler
from lib.response import makeJsonResponse
from config import database

ItemService = ItemService(ItemRepository(database))

itemRoutes = Blueprint("items", __name__)

@itemRoutes.route('/', methods=['GET', 'POST'])
def items():
	if request.method == 'GET':
		itemList = ItemService.getListOfItems()
		return makeJsonResponse(itemList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		postedItem = itemAssembler(jsonreq)
		ItemService.createItem(postedItem)
		return makeJsonResponse({"success": "true"})

@itemRoutes.route('/<int:itemId>/', methods=['DELETE'])
def itemById(itemId):
	if request.method == 'DELETE':
		ItemService.deleteItem(itemId)
		return makeJsonResponse({"success": "true"})
