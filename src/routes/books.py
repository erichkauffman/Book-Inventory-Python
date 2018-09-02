from flask import Blueprint, request
import jsonpickle

from data.Book import Book
from services.bookService import BookService
from services.itemService import ItemService
from repositories.bookRepository import BookRepository
from repositories.itemRepository import ItemRepository
from lib.serializer import serialize
from lib.convert import bookAssembler
from config import database

itemService = ItemService(ItemRepository(database))
bookService = BookService(BookRepository(database), itemService)

bookRoutes = Blueprint("books", __name__)

@bookRoutes.route('/', methods=['GET', 'POST'])
def books():
	if request.method == 'GET':
		bookList = bookService.getListOfBooks()
		return jsonpickle.encode(bookList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		postedBook = bookAssembler(jsonreq)
		bookService.createBook(postedBook)
		res = jsonpickle.encode({"success": "true"})
		return res

#        except:
#            res = jsonify({"success": "false", "reason": "Something went wrong"})
#            res.status_code = 500
#            return res

	else:
		res = jsonpickle.encode({"success": "false", "reason":"That request method is not implemented"})
		res.status_code = 403
		return res
 