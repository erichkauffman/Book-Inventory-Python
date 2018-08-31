from flask import Blueprint, request, jsonify
import json

from data.Item import Item
from services.itemService import ItemService
from repositories.itemRepository import ItemRepository
from lib.serializer import serialize
from config import database

ItemService = ItemService(ItemRepository(database))

itemRoutes = Blueprint("items", __name__)

@itemRoutes.route('/', methods=['GET'])
def items():
	if request.method == 'GET':
		itemList = ItemService.getListOfItems()
		return jsonify([item.__dict__ for item in itemList])