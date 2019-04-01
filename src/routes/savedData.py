from flask import Blueprint, request

from services.savedDataService import SavedDataService
from repositories.savedDataRepository import SavedDataRepository
from lib.response import makeJson, makeJsonResponse
from initialize import socketio
from config import database

savedDataService = SavedDataService(SavedDataRepository(database))

savedDataRoutes = Blueprint("savedData", __name__)
savedDataTypes = ['phrases', 'locations']

@savedDataRoutes.route('/<string:dataType>/', methods=['GET', 'POST', 'DELETE'])
def savedData(dataType):
	if dataType not in savedDataTypes:
		return makeJsonResponse({"success": False, "message": f"'{dataType}' is not a valid type"}), 404
	if request.method == 'GET':
		dataList = savedDataService.getListOfData(dataType)
		return makeJsonResponse(dataList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		data = jsonreq['data']
		savedDataService.createData(dataType, data)
		dataPack = {'type':dataType, 'data':data}
		socketio.emit('new_data', makeJson(dataPack), broadcast=True)
		return makeJsonResponse({"success": True})
	elif request.method == 'DELETE':
		jsonreq = request.get_json(force=True)
		data = jsonreq['data']
		savedDataService.removeData(dataType, data)
		dataPack = {'type':dataType, 'data':data}
		socketio.emit('delete_data', makeJson(dataPack), broadcast=True)
		return makeJsonResponse({"success": True})
