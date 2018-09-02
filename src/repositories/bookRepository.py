import sqlite3

from data.Book import Book
from lib.database import book_factory

# Example for proper query creation:
# db.execute('SELECT * FROM book WHERE Id = ?', 3)

class BookRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getListOfBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM book INNER JOIN item ON book.itemId = item.itemId ORDER BY book.author, item.title')
		return cursor.fetchall()

	def createNewBook(self, book: Book):
		bookInsert = (
            book.author,
            book.edition,
            book.printing,
            book.cover,
			book.item.itemId
 		)
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('INSERT INTO book (author, edition, printing, cover, itemId) VALUES(?,?,?,?,?)', bookInsert)
		conn.commit()