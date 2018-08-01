import sqlite3
from sqlite3 import Error
from data.Book import Book

# Example for proper query creation:
# db.execute('SELECT * FROM book WHERE Id = ?', 3)

class BookRepo:
    def __init__(self, dbConnection: str):
        try:
            self.db = sqlite3.connect(dbConnection).cursor()
        except Error as e:
            print(e)

    def getListOfBooks(self):
        self.db.execute("SELECT * FROM book")
        return self.db.fetchall()

    def createNewBook(self, book: Book):
        bookInsert = (
            book.title,
            book.author,
            book.isbn,
            book.edition,
            book.printing,
            book.cover,
            book.yearPrinted,
            book.description,
            book.condition,
            book.datePurchased,
            book.locationPurchased,
            book.amountPaid,
            book.sellPrice,
            book.siteListed
        )
        self.db.execute('INSERT INTO book VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', bookInsert)
        self.db.commit()