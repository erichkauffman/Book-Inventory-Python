from repositories.bookRepository import BookRepository
from repositories.siteRepository import SiteRepository
from services.itemService import ItemService
from data.Book import Book

class BookService:
	def __init__(self, bookRepository: BookRepository, siteRepository: SiteRepository, itemService: ItemService):
		self.bookRepo = bookRepository
		self.siteRepo = siteRepository
		self.itemService = itemService

	def getListOfBooks(self):
		return self.bookRepo.getListOfBooks()

	def createBook(self, book: Book):
		itemId = self.itemService.createItem(book.item)
		book.item.itemId = itemId
		self.bookRepo.createNewBook(book)

	def getSellableBooks(self):
		return self.bookRepo.getSellableBooks()

	def deleteBook(self, itemId: int):
		self.bookRepo.deleteBook(itemId)
		self.itemService.deleteItem(itemId)
