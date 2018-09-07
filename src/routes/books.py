from flask import Blueprint, request
from sqlite3 import IntegrityError

from services.bookService import BookService
from services.itemService import ItemService
from repositories.bookRepository import BookRepository
from repositories.itemRepository import ItemRepository
from lib.convert import bookAssembler
from lib.response import makeJsonResponse
from lib.exceptions import DatabaseIndexError
from config import database

itemService = ItemService(ItemRepository(database))
bookService = BookService(BookRepository(database), itemService)

bookRoutes = Blueprint("books", __name__)

@bookRoutes.route('/', methods=['GET', 'POST'])
def books():
	if request.method == 'GET':
		bookList = bookService.getListOfBooks()
		return makeJsonResponse(bookList)
	elif request.method == 'POST':
		try:
			jsonreq = request.get_json(force=True)
			postedBook = bookAssembler(jsonreq)
			bookService.createBook(postedBook)
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

@bookRoutes.route('/<int:itemId>/', methods=['DELETE'])
def bookById(itemId):
	if request.method == 'DELETE':
		try:
			bookService.deleteBook(itemId)
			return makeJsonResponse({"success": True})
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404
