import sqlite3

from data.Book import Book
from lib.database import book_factory, mini_factory
from lib.exceptions import DatabaseIndexError

class BookRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def allBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.execute('''SELECT *, group_concat(site.site), group_concat(site.siteId)
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  LEFT JOIN site ON book.itemId = site.itemId
						  GROUP BY book.itemId''')
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
		conn.execute('''INSERT INTO book
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
		cursor = conn.execute('''UPDATE book SET author = ?, edition = ?,
						  printing = ?, cover = ?
						  WHERE itemId = ?''', bookInsert)
		count = cursor.rowcount
		conn.commit()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {book.item.itemId} does not exist in database')

	def getSellableBooks(self):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = mini_factory
		cursor = conn.execute('''SELECT book.itemId, title, upc, author, group_concat(site.siteId)
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  LEFT JOIN site ON book.itemId = site.itemId
						  WHERE item.dateRemoved IS NULL
						  GROUP BY book.itemId''')
		return cursor.fetchall()

	def getBookById(self, itemId: int):
		conn = sqlite3.connect(self.dbConnection)
		conn.row_factory = book_factory
		cursor = conn.execute('''SELECT *, group_concat(site.site), group_concat(site.siteId)
						  FROM book
						  INNER JOIN item ON book.itemId = item.itemId
						  LEFT JOIN site ON book.itemId = site.itemId
						  WHERE book.itemId = ?
						  GROUP BY book.itemId''', (itemId,))
		count = cursor.rowcount
		book = cursor.fetchone()
		if not count:
			raise DatabaseIndexError(f'Item with itemId = {itemId} does not exist in database')
		return book
