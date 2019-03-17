import sqlite3

from data.Book import Book
from lib.database import book_factory, mini_factory
from lib.exceptions import DatabaseIndexError

class BookRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

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
		cursor.execute('''INSERT INTO book
						  (author, edition, printing, cover, itemId)
						  VALUES(?,?,?,?,?)''', bookInsert)
		conn.commit()

	def editBook(self, book: Book):
		bookInsert = (
			book.author,
			book.edition,
			book.printing,
			book.cover,
			book.item.itemId
		)
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('''UPDATE book SET author = ?, edition = ?,
						  printing = ?, cover = ?
						  WHERE itemId = ?''', bookInsert)
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {book.item.itemId} does not exist in database')

	def getSellableBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = mini_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT item.itemId, title, upc, author
						  FROM item
						  INNER JOIN book ON item.itemId = book.itemId
						  WHERE item.dateRemoved IS NULL''')
		return cursor.fetchall()

	def getBookById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT *
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  WHERE book.itemId = ?''', (itemId,))
		count = cursor.rowcount
		book = cursor.fetchone()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')
		return book
