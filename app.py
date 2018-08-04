from flask import Flask, request, jsonify
import json

from data.Book import Book
from services.bookService import BookService
from repositories.bookRepository import BookRepository
from lib.serializer import serialize
from lib.status import createStatus
from config import database

app = Flask(__name__)

bookService = BookService(BookRepository(database))

@app.route('/')
def index():
    return("Hello!")

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        bookList = bookService.getListOfBooks()
        return jsonify([book.__dict__ for book in bookList])
        

    elif request.method == 'POST':
        try:
            jsonreq = request.get_json(force=True)
        
            postedBook = Book(
                0,
                jsonreq['title'],
                jsonreq['author'],
                jsonreq['isbn'],
                jsonreq['edition'],
                jsonreq['printing'],
                jsonreq['cover'],
                jsonreq['yearPrinted'],
                jsonreq['description'],
                jsonreq['condition'],
                jsonreq['datePurchased'],
                jsonreq['locationPurchased'],
                jsonreq['amountPaid'],
                jsonreq['sellPrice'],
                jsonreq['siteListed'],
                jsonreq['removalAction'],
                jsonreq['dateRemoved']
            )
            bookService.createBook(postedBook)
            res = jsonify({"success": "true"})
            return res
        
        except:
            res = jsonify({"success": "false", "reason": "Something went wrong"})
            res.status_code = 500
            return res

    else:
        res = jsonify({"success": "false", "reason":"That request method is not implemented"})
        res.status_code = 403
        return res
        