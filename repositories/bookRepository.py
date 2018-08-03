import sqlite3
from sqlite3 import Error
from data.Book import Book

# Example for proper query creation:
# db.execute('SELECT * FROM book WHERE Id = ?', 3)

class BookRepository:
    def __init__(self, dbConnection: str):
        try:
            self.db = sqlite3.connect(dbConnection, check_same_thread=False)
        except Error as e:
            print(e)

    def getListOfBooks(self):
        self.db.execute("SELECT rowid, * FROM book ORDER BY author, title")
        listOfBookTuples = self.db.cursor().fetchall()
        bookList = []
        for bookTuple in listOfBookTuples:
            newBook = Book(bookTuple[0],
                           bookTuple[1],
                           bookTuple[2],
                           bookTuple[3],
                           bookTuple[4],
                           bookTuple[5],
                           bookTuple[6],
                           bookTuple[7],
                           bookTuple[8],
                           bookTuple[9],
                           bookTuple[10],
                           bookTuple[11],
                           bookTuple[12],
                           bookTuple[13],
                           bookTuple[14],
                           bookTuple[15],
                           bookTuple[16])
            bookList.append(newBook)
        return bookList

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
            book.siteListed,
            book.removalAction,
            book.dateRemoved
        )
        self.db.cursor().execute('INSERT INTO book VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', bookInsert)
        self.db.commit()