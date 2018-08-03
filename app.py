from flask import Flask, request
from flask_api import status

from data.Book import Book
from services.bookService import BookService
from repositories.bookRepo import BookRepo
from lib.serializer import serialize
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
        postedBook = Book(
            0,
            request.form['title'],
            request.form['author'],
            request.form['isbn'],
            request.form['edition'],
            request.form['printing'],
            request.form['cover'],
            request.form['yearPrinted'],
            request.form['description'],
            request.form['condition'],
            request.form['datePurchased'],
            request.form['locationPurchased'],
            request.form['amountPaid'],
            request.form['sellPrice'],
            request.form['siteListed'],
            request.form['removalAction'],
            request.form['dateRemoved']
        )
        bookService.createBook(postedBook)
    else:
        return status.HTTP_400_BAD_REQUEST