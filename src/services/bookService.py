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
		books = self.bookRepo.getListOfBooks()
		for index, book in enumerate(books):
			books[index].item.siteListed = self.siteRepo.getSitesById(book.item.itemId)
		return books

	def createBook(self, book: Book):
		itemId = self.itemService.createItem(book.item)
		book.item.itemId = itemId
		self.bookRepo.createNewBook(book)

	def getSellableBooks(self):
		books = self.bookRepo.getSellableBooks()
		for index, book in enumerate(books):
			books[index].item.siteListed = self.siteRepo.getSitesById(book.item.itemId)
		return books

	def getBookById(self, itemId: int):
		book = self.bookRepo.getBookById(itemId)
		book.item.siteListed = self.siteRepo.getSitesById(itemId)
		return book
