from repositories.bookRepository import BookRepository
from services.siteService import SiteService
from services.itemService import ItemService
from data.Book import Book
from lib.itemCsv import bookCsv

class BookService:
	def __init__(self, bookRepository: BookRepository, siteService: SiteService, itemService: ItemService):
		self.bookRepo = bookRepository
		self.siteService = siteService
		self.itemService = itemService

	def createBook(self, book: Book):
		itemId = self.itemService.createItem(book.item)
		book.item.itemId = itemId
		self.bookRepo.createNewBook(book)
		return itemId

	def editBook(self, book: Book):
		self.itemService.editItem(book.item)
		self.bookRepo.editBook(book)

	def getSellableBooks(self):
		return self.bookRepo.getSellableBooks()

	def getBookById(self, itemId: int):
		book = self.bookRepo.getBookById(itemId)
		book.item.siteListed = self.siteService.getSitesById(itemId)
		return book

	def buildCsv(self):
		csv = ''
		bookList = self.bookRepo.allBooks()
		for book in bookList:
			csv += bookCsv(book) + '\n'
		return csv
