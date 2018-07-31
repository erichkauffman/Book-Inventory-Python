from repositories.bookRepo import BookRepo

class BookService:
    def __init__(self, bookRepository: BookRepo):
        self.bookRepo = bookRepository
