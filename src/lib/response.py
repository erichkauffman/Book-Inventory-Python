from flask import make_response
import jsonpickle

def makeJsonResponse(data):
	jsonData = jsonpickle.encode(data)
	res = make_response(jsonData)
	res.headers['Content-Type'] = 'application/json'
	return res
