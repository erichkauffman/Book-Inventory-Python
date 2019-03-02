from flask import Blueprint, request

from services.locationService import LocationService
from repositories.locationRepository import LocationRepository
from lib.response import makeJsonResponse
from config import database

locationService = LocationService(LocationRepository(database))

locationRoutes = Blueprint("locations", __name__)

@locationRoutes.route('/', methods=['GET'])
def locations():
	if request.methods == 'GET':
		locationList = locationService.getListOfLocations()
		return makeJsonResponse(locationList)

@locationRoutes.route('/<str:location>/', methods=['POST'])
def setLocation(location):
	if request.methods == 'POST':
		locationService.createLocation(location)
		return makeJsonResponse({"success": True})
