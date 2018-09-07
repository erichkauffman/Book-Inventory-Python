from flask import Blueprint, request
from sqlite3 import IntegrityError

from services.itemService import ItemService
from repositories.itemRepository import ItemRepository
from lib.convert import itemAssembler
from lib.response import makeJsonResponse
from lib.exceptions import DatabaseIndexError
from config import database

ItemService = ItemService(ItemRepository(database))

itemRoutes = Blueprint("items", __name__)

@itemRoutes.route('/', methods=['GET', 'POST'])
def items():
	if request.method == 'GET':
		itemList = ItemService.getListOfItems()
		return makeJsonResponse(itemList)
	elif request.method == 'POST':
		try:
			jsonreq = request.get_json(force=True)
			postedItem = itemAssembler(jsonreq)
			ItemService.createItem(postedItem)
			return makeJsonResponse({"success": True})
		except KeyError as e:
			return makeJsonResponse({"success": False, "message": f"Could not find {str(e)} key in received data"}), 400
		except IntegrityError as e:
			messageString = str(e).split()
			if (messageString[0] == "NOT" and
			   messageString[1] == "NULL" and
			   messageString[2] == "constraint" and
			   messageString[3] == "failed:"):
			   failedKey = messageString[-1].split('.')
			   return makeJsonResponse({"success": False, "message": f"'{failedKey[-1]}' must not be null"}), 400

			return makeJsonResponse({"success": False, "message": "Something went wrong, please make sure your data is correct"}), 400


@itemRoutes.route('/<int:itemId>/', methods=['DELETE'])
def itemById(itemId):
	if request.method == 'DELETE':
		try:
			ItemService.deleteItem(itemId)
			return makeJsonResponse({"success": True})
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404
