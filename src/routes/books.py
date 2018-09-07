from flask import Blueprint, request

from services.bookService import BookService
from services.itemService import ItemService
from repositories.bookRepository import BookRepository
from repositories.itemRepository import ItemRepository
from lib.convert import bookAssembler
from lib.response import makeJsonResponse
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
		return makeJsonResponse({"success": "true"})

@bookRoutes.route('/<int:itemId>/', methods=['DELETE'])
def bookById(itemId):
	if request.method == 'DELETE':
		bookService.deleteBook(itemId)
		return makeJsonResponse({"success": "true"})
