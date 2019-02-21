import sqlite3

from data.Book import Book
from lib.database import book_factory
from lib.exceptions import DatabaseIndexError

class BookRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getListOfBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT *
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  ORDER BY book.author, item.title''')
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
		cursor.execute('''INSERT INTO book
						  (author, edition, printing, cover, itemId)
						  VALUES(?,?,?,?,?)''', bookInsert)
		conn.commit()

	def getSellableBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.cursor()
		cursor.execute('''SELECT *
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  WHERE item.dateRemoved IS NULL
						  ORDER BY book.author, item.title''')
		return cursor.fetchall()

	def deleteBook(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('DELETE FROM book WHERE itemId = ?', (itemId,))
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f"Book with itemId = {itemId} does not exist in database")
