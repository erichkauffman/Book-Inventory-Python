from flask import Blueprint, request

from services.locationService import LocationService
from repositories.locationRepository import LocationRepository
from lib.response import makeJsonResponse
from config import database

locationService = LocationService(LocationRepository(database))

locationRoutes = Blueprint("locations", __name__)

@locationRoutes.route('/', methods=['GET'])
def locations():
	if request.method == 'GET':
		locationList = locationService.getListOfLocations()
		return makeJsonResponse(locationList)

@locationRoutes.route('/<string:location>/', methods=['POST', 'DELETE'])
def setLocation(location):
	if request.method == 'POST':
		locationService.createLocation(location)
		return makeJsonResponse({"success": True})
	if request.method == 'DELETE':
		locationService.removeLocation(location)
		return makeJsonResponse({"success": True})
