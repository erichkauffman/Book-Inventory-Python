from flask import make_response
import jsonpickle

def makeJson(data):
	return jsonpickle.encode(data)

def makeJsonResponse(data):
	jsonData = makeJson(data)
	res = make_response(jsonData)
	res.headers['Content-Type'] = 'application/json'
	return res

def makeCsvResponse(csv):
	res = make_response(csv)
	res.headers['Content-Disposition'] = 'attachment; filename=db.csv'
	res.headers['Content-type'] = 'text/csv'
	return res
