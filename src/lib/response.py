from flask import make_response
import jsonpickle

def makeJson(data):
	return jsonpickle.encode(data)

def makeJsonResponse(data):
	jsonData = makeJson(data)
	res = make_response(jsonData)
	res.headers['Content-Type'] = 'application/json'
	return res
