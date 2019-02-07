from unittest import mock

from data.Book import Book
from data.Item import Item
from services.bookService import BookService
from services.itemService import ItemService
from repositories.bookRepository import BookRepository

def test_getting_a_list_of_books():
	mockItemService = mock.create_autospec(ItemService)
	mockRepo = mock.create_autospec(BookRepository)
	mockRepo.getListOfBooks.return_value = [Book(
		Item(
        	5,
        	"Cracking the Coding Interview",
        	"9870984782857",
        	2015,
        	"A very good book for practicing algorithms",
        	2,
        	"2016-12-6",
        	"Online",
        	2000,
       		1200,
        	1,
			"FBA",
        	None,
        	None
		),
        "Gayle Laakmann McDowell",
        6,
        15,
        0,
    )]
	service = BookService(mockRepo, mockItemService)

	returnedListOfBooks = service.getListOfBooks()
	assert len(returnedListOfBooks) == 1

	returnedBook = returnedListOfBooks[0]
	assert returnedBook.item.itemId == 5
	assert returnedBook.item.title == "Cracking the Coding Interview"
	assert returnedBook.author == "Gayle Laakmann McDowell"
	assert returnedBook.item.upc == "9870984782857"
	assert returnedBook.edition == 6
	assert returnedBook.printing == 15
	assert returnedBook.cover == 0
	assert returnedBook.item.year == 2015
	assert returnedBook.item.description == "A very good book for practicing algorithms"
	assert returnedBook.item.condition == 2
	assert returnedBook.item.datePurchased == "2016-12-6"
	assert returnedBook.item.locationPurchased == "Online"
	assert returnedBook.item.amountPaid == 2000
	assert returnedBook.item.sellPrice == 1200
	assert returnedBook.item.shelfLocation == "FBA"
	assert returnedBook.item.siteListed == 1
	assert returnedBook.item.removalAction is None
	assert returnedBook.item.dateRemoved is None
