from data.Item import Item
from data.Book import Book

def itemCsv(item: Item):
	csv = f'"{item.itemId}", "{item.title}", "{item.upc}", "{item.year}", '
	csv += f'"{item.description}", "{item.condition}", "{item.datePurchased}", '
	csv += f'''"{item.locationPurchased}", "{item.consignment}", "{'%.2f'%(item.amountPaid/100)}", '''
	csv += f'''"{'%.2f'%(item.sellPrice/100)}", "{item.siteListed}", "{item.shelfLocation}", '''
	csv += f'"{item.removalAction}", "{item.siteSold}", "{item.dateRemoved}"'
	return csv

def bookCsv(book: Book):
	csv = itemCsv(book.item) + ', '
	csv += f'"{book.author}", "{book.edition}", "{book.printing}", "{book.cover}"'
	return csv
