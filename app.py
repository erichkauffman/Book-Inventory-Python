from flask import Flask, request
import json

from data.Book import Book
from services.bookService import BookService
from repositories.bookRepo import BookRepo
from lib.serializer import serialize
from lib.status import createStatus
from config import database

app = Flask(__name__)

bookService = BookService(BookRepo(database))

@app.route('/')
def index():
    return("Hello!")

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        bookList = bookService.getListOfBooks()
        jsonBookList = serialize(bookList)
        return jsonBookList

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
            return createStatus(200, True)
        
        except:
            return createStatus(500, reason="Something went wrong")

    else:
        return createStatus(405, reason="That request method is not implemented")