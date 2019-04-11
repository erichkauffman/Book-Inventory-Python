from sqlite3 import IntegrityError
from flask import Blueprint, request

from services.bookService import BookService
from services.itemService import ItemService
from repositories.bookRepository import BookRepository
from repositories.itemRepository import ItemRepository
from repositories.siteRepository import SiteRepository
from lib.convert import bookAssembler
from lib.response import makeJson, makeJsonResponse, makeCsvResponse
from lib.exceptions import DatabaseIndexError
from initialize import socketio
from config import database

itemService = ItemService(ItemRepository(database), SiteRepository(database))
bookService = BookService(BookRepository(database), SiteRepository(database), itemService)

bookRoutes = Blueprint("books", __name__)

@bookRoutes.route('/', methods=['POST', 'PUT'])
def books():
	if request.method == 'POST':
		try:
			jsonreq = request.get_json(force=True)
			postedBook = bookAssembler(jsonreq)
			itemId = bookService.createBook(postedBook)
			mini = {'itemId': itemId,
					'title': postedBook.item.title,
					'upc': postedBook.item.upc,
					'author': postedBook.author}
			socketio.emit('new_book', makeJson(mini), broadcast=True)
			return makeJsonResponse({"success": True})
		except KeyError as e:
			return makeJsonResponse({"success": False, "message": f"Could not find {str(e)} key in received data"}), 400
		except IntegrityError as e:
			failedKey = str(e).split()[-1].split('.')
			return makeJsonResponse({"success": False, "message": f"'{failedKey[-1]}' must not be null"}), 400

	elif request.method == 'PUT':
		try:
			jsonreq = request.get_json(force=True)
			putBook = bookAssembler(jsonreq)
			bookService.editBook(putBook)
			mini = {'itemId': putBook.item.itemId,
					'title': putBook.item.title,
					'upc': putBook.item.upc,
					'author': putBook.author}
			socketio.emit('update_book', makeJson(mini), broadcast=True)
			return makeJsonResponse({"success": True})
		except KeyError as e:
			return makeJsonResponse({"success": False, "message": f"Could not find {str(e)} key in received data"}), 400
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404
		except IntegrityError as e:
			failedKey = str(e).split()[-1].split('.')
			return makeJsonResponse({"success": False, "message": f"'{failedKey[-1]}' must not be null"}), 400

@bookRoutes.route('/sellable/', methods=['GET'])
def booksSellable():
	if request.method == 'GET':
		bookList = bookService.getSellableBooks()
		return makeJsonResponse(bookList)

@bookRoutes.route('/<int:itemId>/', methods=['GET'])
def bookById(itemId):
	if request.method == 'GET':
		try:
			book = bookService.getBookById(itemId)
			return makeJsonResponse(book)
		except DatabaseIndexError as e:
			return makeJsonResponse({"success": False, "message": str(e)}), 404

@bookRoutes.route('/csv/', methods=['GET'])
def itemCsv():
	if request.method == 'GET':
		csv = bookService.buildCsv()
		return makeCsvResponse(csv)
