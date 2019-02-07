from flask import Flask
from lib.response import makeJsonResponse
from data.Book import Book
from data.Item import Item

app = Flask(__name__)

def test_make_json_response_from_object():
	with app.app_context():
		book = [Book(
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
	        0
	    )]
		response = makeJsonResponse(book)
		assert response.status_code == 200
		assert response.is_json is True

		jsonResult = response.get_json()
		assert len(jsonResult) == 1
		jsonResult = jsonResult[0]
		assert jsonResult['item']['itemId'] == 5
		assert jsonResult['item']['title'] == "Cracking the Coding Interview"
		assert jsonResult['item']['upc'] == "9870984782857"
		assert jsonResult['item']['year'] == 2015
		assert jsonResult['item']['description'] == "A very good book for practicing algorithms"
		assert jsonResult['item']['condition'] == 2
		assert jsonResult['item']['datePurchased'] == "2016-12-6"
		assert jsonResult['item']['locationPurchased'] == "Online"
		assert jsonResult['item']['amountPaid'] == 2000
		assert jsonResult['item']['sellPrice'] == 1200
		assert jsonResult['item']['siteListed'] == 1
		assert jsonResult['item']['shelfLocation'] == "FBA"
		assert jsonResult['item']['removalAction'] is None
		assert jsonResult['item']['dateRemoved'] is None
		assert jsonResult['author'] == "Gayle Laakmann McDowell"
		assert jsonResult['edition'] == 6
		assert jsonResult['printing'] == 15
		assert jsonResult['cover'] == 0
