import os
import requests

def postToTrello(title: str, message: str):
	data = {"name":title,
			"desc":message,
			"pos":"top",
			"idList":os.environ["TRELLO_BOARD_ID"],
			"idLabels":os.environ["TRELLO_LABEL_ID"],
			"key":os.environ["TRELLO_API_KEY"],
			"token":os.environ["TRELLO_API_TOKEN"]
			}

	url = "https://api.trello.com/1/cards"
	return requests.request("POST", url, params=data)
