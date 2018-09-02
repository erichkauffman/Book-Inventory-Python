from repositories.bookRepository import BookRepository
from services.itemService import ItemService
from data.Book import Book

class BookService:
	def __init__(self, bookRepository: BookRepository, itemService: ItemService):
		self.bookRepo = bookRepository
		self.itemService = itemService

	def getListOfBooks(self):
		return self.bookRepo.getListOfBooks()

	def createBook(self, book: Book):
		itemId = self.itemService.createItem(book.item)
		book.item.itemId = itemId
		self.bookRepo.createNewBook(book)
