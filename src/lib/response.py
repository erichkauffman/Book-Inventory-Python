from flask import make_response
import jsonpickle

def makeJson(data):
	return jsonpickle.encode(data)

def makeJsonResponse(data):
	jsonData = makeJson(data)
	res = make_response(jsonData)
	res.headers['Content-Type'] = 'application/json'
	return res

def makeCsvResponse(csv, name):
	res = make_response(csv)
	res.headers['Content-Disposition'] = f'attachment; filename={name}.csv'
	res.headers['Content-type'] = 'text/csv'
	return res
