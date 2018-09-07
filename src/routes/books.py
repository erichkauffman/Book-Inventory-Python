from flask import Blueprint, request

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
		jsonreq = request.get_json(force=True)
		postedBook = bookAssembler(jsonreq)
		bookService.createBook(postedBook)
		return makeJsonResponse({"success": True})

@bookRoutes.route('/<int:itemId>/', methods=['DELETE'])
def bookById(itemId):
	if request.method == 'DELETE':
		try:
			bookService.deleteBook(itemId)
			return makeJsonResponse({"success": True})
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404
