from sqlite3 import IntegrityError
from flask import Blueprint, request

from services.itemService import ItemService
from repositories.itemRepository import ItemRepository
from repositories.siteRepository import SiteRepository
from lib.convert import itemAssembler
from lib.response import makeJson, makeJsonResponse
from lib.exceptions import DatabaseIndexError
from initialize import socketio
from config import database

itemService = ItemService(ItemRepository(database), SiteRepository(database))

itemRoutes = Blueprint("items", __name__)

@itemRoutes.route('/', methods=['POST', 'PUT'])
def items():
	if request.method == 'POST':
		try:
			jsonreq = request.get_json(force=True)
			postedItem = itemAssembler(jsonreq)
			itemId = itemService.createItem(postedItem)
			mini = {'itemId': itemId,
					'title': postedItem.title,
					'upc': postedItem.upc}
			socketio.emit('new_item', makeJson(mini), broadcast=True)
			return makeJsonResponse({"success": True})
		except KeyError as e:
			return makeJsonResponse({"success": False, "message": f"Could not find {str(e)} key in received data"}), 400
		except IntegrityError as e:
			failedKey = str(e).split()[-1].split('.')
			return makeJsonResponse({"success": False, "message": f"'{failedKey[-1]}' must not be null"}), 400

	elif request.method == 'PUT':
		try:
			jsonreq = request.get_json(force=True)
			putItem = itemAssembler(jsonreq)
			itemService.editItem(putItem)
			mini = {'itemId': putItem.itemId,
					'title': putItem.title,
					'upc': putItem.upc}
			socketio.emit('update_item', makeJson(mini), broadcast=True)
			return makeJsonResponse({"success": True})
		except KeyError as e:
			return makeJsonResponse({"success": False, "message": f"Could not find {str(e)} key in received data"}), 400
		except IntegrityError as e:
			failedKey = str(e).split()[-1].split('.')
			return makeJsonResponse({"success": False, "message": f"'{failedKey[-1]}' must not be null"}), 400
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404

@itemRoutes.route('/sellable/', methods=['GET'])
def itemsSellable():
	if request.method == 'GET':
		itemList = itemService.getSellableItems()
		return makeJsonResponse(itemList)

@itemRoutes.route('/<int:itemId>/', methods=['GET'])
def itemById(itemId):
	if request.method == 'GET':
		try:
			item = itemService.getItemById(itemId)
			return makeJsonResponse(item)
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404

@itemRoutes.route('/<int:itemId>/removeAction/<int:status>/', methods=['PUT'])
def updateRemoveAction(itemId, status):
	if request.method == 'PUT':
		try:
			itemService.updateRemoveAction(itemId, status)
			socketio.emit('delete_item', itemId)
			return makeJsonResponse({"success": True})
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404

@itemRoutes.route('/<int:itemId>/sell/', methods=['PUT'])
def sellItem(itemId):
	if request.method == 'PUT':
		try:
			jsonreq = request.get_json(force=True)
			itemService.sellItem(itemId, jsonreq['site'])
			socketio.emit('delete_item', itemId)
			return makeJsonResponse({"success": True})
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404
