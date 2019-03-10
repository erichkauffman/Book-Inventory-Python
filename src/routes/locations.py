from flask import Blueprint, request

from services.locationService import LocationService
from repositories.locationRepository import LocationRepository
from lib.response import makeJsonResponse
from config import database

locationService = LocationService(LocationRepository(database))

locationRoutes = Blueprint("locations", __name__)

@locationRoutes.route('/', methods=['GET', 'POST', 'DELETE'])
def locations():
	if request.method == 'GET':
		locationList = locationService.getListOfLocations()
		return makeJsonResponse(locationList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		location = jsonreq['data']
		locationService.createLocation(location)
		return makeJsonResponse({"success": True})
	elif request.method == 'DELETE':
		jsonreq = request.get_json(force=True)
		location = jsonreq['data']
		locationService.removeLocation(location)
		return makeJsonResponse({"success": True})
