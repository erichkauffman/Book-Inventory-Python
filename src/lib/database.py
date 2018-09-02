import sqlite3
from data.Item import Item
from data.Book import Book
from lib.convert import itemAssembler, bookAssembler

def item_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return itemAssembler(dictionary)

def book_factory(cursor, row):
	dictionary = {}
	for index, columnName in enumerate(cursor.description):
		dictionary[columnName[0]] = row[index]
	return bookAssembler(dictionary)
