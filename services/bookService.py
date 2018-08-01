from repositories.bookRepo import BookRepo
from data.Book import Book

class BookService:
    def __init__(self, bookRepository: BookRepo):
        self.bookRepo = bookRepository

    def getListOfBooks(self):
        return self.bookRepo.getListOfBooks()

    def createBook(self, book: Book):
        self.bookRepo.createNewBook(book)